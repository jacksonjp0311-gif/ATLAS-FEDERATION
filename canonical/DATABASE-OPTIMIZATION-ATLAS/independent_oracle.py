"""Finite independent checks for ATLAS FORGE original domain #17.

Independence: SQLite executes SQL truth / equijoin; brute nested-loop, built-in sort,
plain reference lists, and independent snapshot replay evaluate reference models.
Deterministic constructed data, NOT measured DBMS performance or a scientific audit.
"""
from __future__ import annotations
import random, sqlite3, hashlib, json, pathlib
from collections import Counter
from db_reference import (lru_trace, fifo_trace, hash_join, merge_join,
    SortedLeafIndex, external_merge_sort, sql_and, sql_or,
    MVCCVisibility, exact_conjunctive_selectivity,
    independence_selectivity,estimate_scan_vs_index)

rng=random.Random(170026)
comparisons=0
checks={}

def verify(condition:bool,category:str):
    global comparisons
    if not condition: raise AssertionError(f'oracle failure in {category}')
    comparisons+=1
    checks[category]=checks.get(category,0)+1


def lru_slow(trace,cap):
    cache=[]; hits=[]
    for page in trace:
        hit=page in cache
        hits.append(hit)
        if hit: cache.remove(page); cache.append(page)
        elif cap:
            if len(cache)==cap: cache.remove(cache[0])
            cache.append(page)
    return hits,tuple(cache)


def fifo_slow(trace,cap):
    cache=[];hits=[]
    for page in trace:
        hit=page in cache
        hits.append(hit)
        if not hit and cap:
            if len(cache)==cap: cache.remove(cache[0])
            cache.append(page)
    return hits,tuple(cache)


def oracle_main():
    conn=sqlite3.connect(':memory:')
    vals=[True,False,None]
    for a in vals:
        for b in vals:
            for op,fn in [('AND',sql_and),('OR',sql_or)]:
                row=conn.execute('SELECT ? '+op+' ?', (a,b)).fetchone()[0]
                expected=fn(a,b)
                verify((row is None and expected is None) or (row is not None and bool(row)==expected), 'sqlite_truth')
    for _ in range(7000):
        trace=[rng.randrange(17) for _ in range(rng.randrange(28))]
        cap=rng.randrange(7)
        verify(lru_trace(trace,cap)==lru_slow(trace,cap),'lru_naive')
        verify(fifo_trace(trace,cap)==fifo_slow(trace,cap),'fifo_naive')
    for _ in range(5000):
        left=[(rng.choice([None,0,1,2,3,4,5]),rng.randrange(5)) for _ in range(rng.randrange(25))]
        right=[(rng.choice([None,0,1,2,3,4,5]),rng.randrange(5)) for _ in range(rng.randrange(25))]
        expected=Counter((a,b) for a in left for b in right if a[0] is not None and b[0] is not None and a[0]==b[0])
        verify(Counter(hash_join(left,right,0,0))==expected,'hash_join_naive')
        verify(Counter(merge_join(left,right,0,0))==expected,'merge_join_naive')
        # Independent real SQLite bag-semantics count for exactly matching keys, NULL excluded.
        conn.executescript('DROP TABLE IF EXISTS l; DROP TABLE IF EXISTS r; CREATE TABLE l(k INTEGER, v INTEGER); CREATE TABLE r(k INTEGER, v INTEGER);')
        conn.executemany('INSERT INTO l VALUES(?,?)',left)
        conn.executemany('INSERT INTO r VALUES(?,?)',right)
        sql=conn.execute('SELECT l.k,l.v,r.k,r.v FROM l JOIN r ON l.k=r.k').fetchall()
        verify(Counter(((a,b),(c,d)) for a,b,c,d in sql)==expected,'join_sqlite')
    for _ in range(7000):
        pairs=[(rng.randrange(20),i) for i in range(rng.randrange(50))]
        index=SortedLeafIndex.from_entries(pairs, rng.randrange(2,11))
        lo=rng.randrange(-2,23); hi=rng.randrange(-2,23)
        verify(index.search(lo)==sorted(id for k,id in pairs if k==lo),'fence_lookup')
        verify(index.range(lo,hi)==sorted((k,id) for k,id in pairs if lo<=k<=hi),'fence_range')
        verify(external_merge_sort(pairs,0,rng.randrange(1,12))==sorted(pairs,key=lambda r:r[0]),'external_merge_sort')
    for _ in range(2000):
        s=MVCCVisibility(); ledger=[]
        for z in range(rng.randrange(1,16)):
            changes={rng.randrange(6):rng.choice([None,-1,0,1,2,3]) for k in range(rng.randrange(5))}
            s.commit(changes);ledger.append(changes)
        snapshot=rng.randrange(len(ledger)+1)
        expected={}
        for row in ledger[:snapshot]:
            for k,v in row.items():
                if v is None: expected.pop(k,None)
                else: expected[k]=v
        verify(s.scan(snapshot)==expected,'mvcc_naive_replay')
    # Verify loss of information from correlation explicitly: estimator is NOT an oracle of actual performance.
    for _ in range(1000):
        mod=rng.randrange(2,20)
        rows=[(i%mod,i%mod) for i in range(100)]
        k=rng.randrange(mod)
        actual=exact_conjunctive_selectivity(rows,0,k,1,k)
        assumed=independence_selectivity(rows,0,k,1,k)
        verify(actual+1e-12>=assumed,'correlated_selectivity_negative_control')
        plan=estimate_scan_vs_index(100000,100,rng.random())
        verify(plan.scan_cost>=0 and plan.index_cost>=0,'nonnegative_heuristic_cost')
    conn.close()
    return {'schema':'atlas.db-optimization.independent-finite-oracle/1',
            'domain':'database-optimization-atlas','original_priority':17,
            'comparisons':comparisons,'failures':0,'counts':checks,
            'status':'constructed_offline_finite_reference_only',
            'scientific_v1_accepted':False,
            'limitations':['Oracle covers finite, bounded inputs only',
                           'Not database performance or production concurrency certification',
                           'No storage/power-failure tests',
                           'No claim of independent peer review']}

if __name__=='__main__':
    result=oracle_main()
    output=pathlib.Path(__file__).with_name('ORACLE_RECEIPT.json')
    output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,sort_keys=True))
