"""ATLAS FORGE #17; deterministic, offline unittest acceptance."""
import unittest
import tempfile
import pathlib
import random
import sqlite3
from collections import Counter
from db_reference import (sql_and,sql_or,sql_not,sql_eq,lru_trace,fifo_trace,
                          estimate_scan_vs_index,exact_conjunctive_selectivity,
                          independence_selectivity,hash_join,merge_join,
                          external_merge_sort,SortedLeafIndex,MVCCVisibility,sqlite_observation)


class NullSemantics(unittest.TestCase):
    def test_tristate_tables(self):
        truth=[True,False,None]
        a_table={(True,True): True,(True,False):False,(True,None):None,
                 (False,True):False,(False,False):False,(False,None):False,
                 (None,True):None,(None,False):False,(None,None):None}
        o_table={(True,True): True,(True,False):True,(True,None):True,
                 (False,True):True,(False,False):False,(False,None):None,
                 (None,True):True,(None,False):None,(None,None):None}
        for a in truth:
            self.assertIs(sql_not(a),{True:False,False:True,None:None}[a])
            for b in truth:
                self.assertIs(sql_and(a,b),a_table[a,b]);self.assertIs(sql_or(a,b),o_table[a,b])
    def test_null_equality(self):
        self.assertIsNone(sql_eq(None,None))
        self.assertIsNone(sql_eq(3,None))
        self.assertIs(sql_eq(4,4),True)
        self.assertIs(sql_eq(4,5),False)
    def test_actual_sqlite_null_semantics(self):
        conn=sqlite3.connect(':memory:')
        for op,fn in [('AND',sql_and),('OR',sql_or)]:
            for a in [True,False,None]:
                for b in [True,False,None]:
                    actual=conn.execute(f'SELECT ? {op} ?', (a,b)).fetchone()[0]
                    expected=fn(a,b)
                    self.assertIsNone(actual) if expected is None else self.assertEqual(bool(actual),expected)
        conn.close()


class CacheTests(unittest.TestCase):
    def test_empty_zero_capacity(self):
        self.assertEqual(lru_trace([],2),([],()))
        self.assertEqual(lru_trace([1,1,2],0),([False]*3,()))
        self.assertEqual(fifo_trace([1,1,2],0),([False]*3,()))
    def test_lru_hit_moves_to_mru(self):
        self.assertEqual(lru_trace([1,2,1,3,2],2),([False,False,True,False,False],(3,2)))
    def test_fifo_hit_does_not_move(self):
        self.assertEqual(fifo_trace([1,2,1,3,2],2),([False,False,True,False,True],(2,3)))
    def test_negative_capacity(self):
        with self.assertRaises(ValueError): lru_trace([1],-1)
        with self.assertRaises(ValueError): fifo_trace([1],-1)
    def test_cache_determinism(self):
        rng=random.Random(392)
        for _ in range(200):
            x=[rng.randrange(12) for _ in range(50)]
            self.assertEqual(lru_trace(x,3),lru_trace(x,3))
            self.assertEqual(fifo_trace(x,3),fifo_trace(x,3))


class OptimizerTests(unittest.TestCase):
    def test_empty_and_selectivity(self):
        v=estimate_scan_vs_index(0,100,0.5)
        self.assertEqual(v.table_pages,0)
        self.assertEqual(v.scan_cost,0)
    def test_index_favored_low_selectivity(self):
        self.assertEqual(estimate_scan_vs_index(100000,100,0.00001).selected,'index')
    def test_seq_favored_high_selectivity(self):
        self.assertEqual(estimate_scan_vs_index(100000,100,0.9).selected,'scan')
    def test_clustered_helps_range(self):
        a=estimate_scan_vs_index(100000,100,0.10,clustered=True)
        b=estimate_scan_vs_index(100000,100,0.10,clustered=False)
        self.assertLessEqual(a.index_cost,b.index_cost)
    def test_bad_estimator_inputs(self):
        for vals in [(-1,100,.2),(1,0,.2),(10,10,1.1),(10,10,-.1)]:
            with self.assertRaises(ValueError): estimate_scan_vs_index(*vals)
    def test_correlated_predicates_break_independence(self):
        rows=[(i%5,i%5) for i in range(100)]
        actual=exact_conjunctive_selectivity(rows,0,2,1,2)
        estimated=independence_selectivity(rows,0,2,1,2)
        self.assertAlmostEqual(actual,.2)
        self.assertAlmostEqual(estimated,.04)
        self.assertGreater(actual/estimated,4)
    def test_zero_row_statistics(self):
        self.assertEqual(exact_conjunctive_selectivity([],0,1,1,2),0)
        self.assertEqual(independence_selectivity([],0,1,1,2),0)


class JoinsAndSort(unittest.TestCase):
    def test_duplicates_and_null(self):
        l=[(1,'a'),(1,'b'),(None,'n'),(3,'c')]
        r=[(1,'x'),(1,'y'),(None,'z'),(4,'u')]
        expected=Counter((a,b) for a in l for b in r if a[0] is not None and b[0] is not None and a[0]==b[0])
        self.assertEqual(Counter(hash_join(l,r,0,0)),expected)
        self.assertEqual(Counter(merge_join(l,r,0,0)),expected)
    def test_empty_join(self):
        self.assertEqual(hash_join([],[(1,)],0,0),[])
        self.assertEqual(merge_join([],[(1,)],0,0),[])
    def test_random_joins(self):
        rng=random.Random(21)
        for _ in range(200):
            l=[(rng.choice([None,0,1,2,3]),i) for i in range(rng.randrange(25))]
            r=[(rng.choice([None,0,1,2,3]),i) for i in range(rng.randrange(25))]
            reference=Counter((a,b) for a in l for b in r if a[0] is not None and b[0] is not None and a[0]==b[0])
            self.assertEqual(Counter(hash_join(l,r,0,0)),reference)
            self.assertEqual(Counter(merge_join(l,r,0,0)),reference)
    def test_external_sort_stable(self):
        rng=random.Random(22)
        for n in range(50):
            rows=[(rng.randrange(5),i) for i in range(n)]
            for k in [1,2,3,9,100]:
                self.assertEqual(external_merge_sort(rows,0,k),sorted(rows,key=lambda r:r[0]))
    def test_external_sort_invalid(self):
        with self.assertRaises(ValueError): external_merge_sort([],0,0)


class IndexTests(unittest.TestCase):
    def test_empty(self):
        idx=SortedLeafIndex.from_entries([])
        self.assertEqual(idx.search(0),[]); self.assertEqual(idx.range(0,2),[])
    def test_boundary_duplicates(self):
        idx=SortedLeafIndex.from_entries([(1,i) for i in range(27)]+[(2,99)],2)
        self.assertEqual(idx.search(1),list(range(27)))
        self.assertEqual(idx.range(1,1),[(1,i) for i in range(27)])
    def test_random_lookup_and_range(self):
        rng=random.Random(44)
        for n in range(75):
            entries=[(rng.randrange(12),i) for i in range(n)]
            idx=SortedLeafIndex.from_entries(entries,rng.randrange(2,10))
            for key in range(-1,14):
                self.assertEqual(idx.search(key),sorted(rid for k,rid in entries if k==key))
                self.assertEqual(idx.range(key,key+2),sorted((k,rid) for k,rid in entries if key<=k<=key+2))
    def test_invalid_index_capacity(self):
        with self.assertRaises(ValueError): SortedLeafIndex.from_entries([(1,2)],1)


class SnapshotTests(unittest.TestCase):
    def test_old_versions_stable(self):
        s=MVCCVisibility(); t0=s.begin()
        self.assertEqual(s.read('a',t0),None)
        t1=s.commit({'a':5}); t2=s.begin()
        s.commit({'a':8,'b':3})
        self.assertEqual(t1,1)
        self.assertEqual(s.read('a',t2),5)
        self.assertEqual(s.scan(t2),{'a':5})
        self.assertEqual(s.scan(s.begin()),{'a':8,'b':3})
        s.commit({'a':None})
        self.assertNotIn('a',s.scan(s.begin()))
    def test_bad_snapshot(self):
        s=MVCCVisibility()
        for i in [-1,1]:
            with self.assertRaises(ValueError): s.read('a',i)
    def test_zero_change_clock(self):
        s=MVCCVisibility();s.commit({});self.assertEqual(s.begin(),1)


class RealSQLite(unittest.TestCase):
    def test_observed_plan_and_equal_answers(self):
        db=sqlite3.connect(':memory:')
        db.execute('CREATE TABLE parts (part_id INTEGER PRIMARY KEY, category INTEGER, cost INTEGER)')
        db.executemany('INSERT INTO parts (part_id,category,cost) VALUES (?,?,?)',
                       [(i,i%37,i*2) for i in range(1,2501)])
        q='SELECT part_id,cost FROM parts WHERE category=?'
        before=sqlite_observation(db,q,(7,))
        db.execute('CREATE INDEX parts_category_cost ON parts(category,cost)')
        db.execute('ANALYZE')
        after=sqlite_observation(db,q,(7,))
        self.assertEqual(before['rows'],after['rows'])
        self.assertEqual(before['total_rows'],after['total_rows'])
        self.assertGreater(len(before['plan']),0)
        self.assertGreater(len(after['plan']),0)
        self.assertEqual(db.execute('PRAGMA integrity_check').fetchone(),('ok',))
        db.close()
    def test_wal_transaction_reopen(self):
        with tempfile.TemporaryDirectory() as d:
            dbfile=pathlib.Path(d)/'test.db'
            c=sqlite3.connect(dbfile)
            self.assertEqual(c.execute('PRAGMA journal_mode=WAL').fetchone()[0],'wal')
            c.execute('CREATE TABLE x (id INTEGER PRIMARY KEY, payload TEXT)')
            with c: c.execute('INSERT INTO x VALUES (?,?)',(1,'committed'))
            c.close()
            dbr=sqlite3.connect(dbfile)
            self.assertEqual(dbr.execute('SELECT * FROM x').fetchall(),[(1,'committed')])
            self.assertEqual(dbr.execute('PRAGMA integrity_check').fetchone(),('ok',))
            dbr.close()
    def test_nonselect_blocked(self):
        c=sqlite3.connect(':memory:')
        with self.assertRaises(ValueError): sqlite_observation(c,'DELETE FROM x')
        c.close()

if __name__=='__main__': unittest.main()
