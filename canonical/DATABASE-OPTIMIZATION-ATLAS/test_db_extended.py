"""Bounded deterministic failure/control tests for database optimizers and WAL."""
import itertools,random,unittest
from db_extended import (external_sort_page_io,left_deep_dp,index_only_visibility,
                         detects_two_tx_write_skew,wal_committed_prefix,plan_regret)

class PageIO(unittest.TestCase):
    def test_empty(self):self.assertEqual(external_sort_page_io(0,3)['total_page_io'],0)
    def test_single_run(self):self.assertEqual(external_sort_page_io(17,32)['total_page_io'],34)
    def test_merge_pass(self):self.assertEqual(external_sort_page_io(100,10)['merge_passes'],2)
    def test_small_buffer(self):self.assertGreater(external_sort_page_io(100,3)['merge_passes'],1)
    def test_reject_negative(self):
        for a,b in [(-1,3),(0,2),(10,0)]:
            with self.assertRaises(ValueError):external_sort_page_io(a,b)
    def test_capacity_is_monotone(self):
        for n in (10,100,1000):
            self.assertLessEqual(external_sort_page_io(n,20)['total_page_io'],external_sort_page_io(n,3)['total_page_io'])
class JoinOrderTests(unittest.TestCase):
    def test_single(self):self.assertEqual(left_deep_dp((8,),{}).indices,(0,))
    def test_empty_rejected(self):
        with self.assertRaises(ValueError):left_deep_dp((),{})
    def test_negative_rejected(self):
        with self.assertRaises(ValueError):left_deep_dp((2,-1),{})
    def test_wrong_pair_rejected(self):
        for p in [{(1,0):.5},{(0,0):.5},{(0,1):1.1}]:
            with self.assertRaises(ValueError):left_deep_dp((2,3),p)
    def test_cheap_first(self):self.assertEqual(left_deep_dp((2,50,200),{}).indices[0],0)
    def test_zero_rows(self):self.assertEqual(left_deep_dp((0,5,7),{}).final_estimated_rows,0)
    def test_deterministic(self):self.assertEqual(left_deep_dp((100,1,50),{}),left_deep_dp((100,1,50),{}))
class VisibilityTests(unittest.TestCase):
    def test_allvisible(self):self.assertEqual(index_only_visibility((0,1,1),frozenset({0,1}))['heap_visibility_checks'],0)
    def test_not_visible(self):self.assertEqual(index_only_visibility((2,2),frozenset())['heap_visibility_checks'],2)
    def test_mixed(self):self.assertEqual(index_only_visibility((2,1,2),frozenset({2}))['index_only_rows'],2)
    def test_bad_id(self):
        with self.assertRaises(ValueError):index_only_visibility((-1,),frozenset())
class ConcurrencyWarnings(unittest.TestCase):
    def test_rw_cycle(self):self.assertTrue(detects_two_tx_write_skew({'a'},{'b'},{'b'},{'a'}))
    def test_no_cycle(self):self.assertFalse(detects_two_tx_write_skew({'a'},{'b'},{'c'},{'d'}))
    def test_same_writes_no_cycle(self):self.assertFalse(detects_two_tx_write_skew({'a'},{'x'},{'b'},{'x'}))
class WALTests(unittest.TestCase):
    def test_empty(self):self.assertEqual(wal_committed_prefix([]),{})
    def test_uncommitted_tail_ignored(self):self.assertEqual(wal_committed_prefix([('BEGIN',1),('WRITE',1,'a',9)]),{})
    def test_committed_only(self):
        e=[('BEGIN',1),('WRITE',1,'a',1),('COMMIT',1),('BEGIN',2),('WRITE',2,'a',2)]
        self.assertEqual(wal_committed_prefix(e),{'a':1})
    def test_commit_without_begin(self):
        with self.assertRaises(ValueError):wal_committed_prefix([('COMMIT',3)])
    def test_write_without_begin(self):
        with self.assertRaises(ValueError):wal_committed_prefix([('WRITE',3,'a',1)])
    def test_duplicate_begin(self):
        with self.assertRaises(ValueError):wal_committed_prefix([('BEGIN',1),('BEGIN',1)])
    def test_unknown_event(self):
        with self.assertRaises(ValueError):wal_committed_prefix([('FLUSH',1)])
    def test_interleaved(self):
        e=[('BEGIN','a'),('BEGIN','b'),('WRITE','a','k',1),('WRITE','b','m',2),('COMMIT','b'),('COMMIT','a')]
        self.assertEqual(wal_committed_prefix(e),{'k':1,'m':2})
class RegretTests(unittest.TestCase):
    def test_zero_regret(self):self.assertEqual(plan_regret((1,2),(1,2))['absolute_regret'],0)
    def test_missed_plan(self):self.assertEqual(plan_regret((1,2),(100,1))['absolute_regret'],99)
    def test_tie_index(self):self.assertEqual(plan_regret((1,1),(1,1))['chosen'],0)
    def test_negative_rejected(self):
        with self.assertRaises(ValueError):plan_regret((1,-2),(1,2))
    def test_bad_length(self):
        with self.assertRaises(ValueError):plan_regret((1,),(1,2))
if __name__=='__main__':unittest.main()
