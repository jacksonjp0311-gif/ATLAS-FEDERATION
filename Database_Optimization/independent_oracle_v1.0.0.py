"""Finite verification with structurally different oracles, not performance certification."""
from __future__ import annotations
from itertools import permutations
import json,random
from math import ceil,prod
from db_extended import (external_sort_page_io,left_deep_dp,index_only_visibility,
                         detects_two_tx_write_skew,wal_committed_prefix,plan_regret)

def brute_join(sizes,sel,order):
    prior=[];cost=float(sizes[order[0]])
    for j in order:
        if not prior:prior.append(j);continue
        r=prod(sizes[i] for i in prior)
        for a,aa in enumerate(prior):
            for bb in prior[a+1:]:r*=sel.get((min(aa,bb),max(aa,bb)),1.0)
        cost+=r*sizes[j];prior.append(j)
    return cost

def run():
    rng=random.Random(20261119);stats={};checks=0
    def check(cond,kind):
        nonlocal checks
        assert cond,kind
        checks+=1;stats[kind]=stats.get(kind,0)+1
    # DP vs factorial exhaustive enumeration; independent cost loop.
    for _ in range(1400):
        n=rng.randrange(1,7)
        sizes=tuple(rng.randrange(0,150) for _ in range(n))
        sel={(i,j):rng.choice([0.0,.01,.1,.25,.5,1.0]) for i in range(n) for j in range(i+1,n)}
        result=left_deep_dp(sizes,sel)
        possibilities=[(brute_join(sizes,sel,perm),perm) for perm in permutations(range(n))]
        # floating point summation across different orders can differ at 1e-10;
        # use bounded comparison instead of exact bit-level matching.
        minimum=min(k for k,p in possibilities)
        check(abs(result.abstract_comparisons-minimum)<=max(1e-7,abs(minimum)*1e-9),'left_deep_vs_bruteforce')
        check(sorted(result.indices)==list(range(n)),'join_permutation_valid')
    # External sort I/O independent iterative simulator.
    for _ in range(5000):
        n=rng.randrange(0,10000);b=rng.randrange(3,100)
        out=external_sort_page_io(n,b)
        chunks=[min(b,n-b*i) for i in range((n+b-1)//b)]
        passes=0
        while len(chunks)>1:
            nxt=[]
            for i in range(0,len(chunks),b-1):nxt.append(sum(chunks[i:i+b-1]))
            chunks=nxt;passes+=1
        check(out['merge_passes']==passes and out['total_page_io']==(2*n*(1+passes) if n else 0),'external_sort_iterative')
    # MVCC visibility by direct row filtering, including repeated heap page IDs.
    for _ in range(5000):
        row_pages=tuple(rng.randrange(64) for _ in range(rng.randrange(100)))
        vis=frozenset(rng.sample(range(64),rng.randrange(65)))
        out=index_only_visibility(row_pages,vis)
        visits=[p for p in row_pages if p not in vis]
        check(out['heap_visibility_checks']==len(visits) and out['index_only_rows']==len(row_pages)-len(visits),'visibility_direct')
    # Interleaved WAL modeled as materialized log; compare independently by scanning
    # the full retained prefix, filtering every transaction that has a COMMIT record.
    for _ in range(4000):
        events=[];actual={};tid=0
        for i in range(rng.randrange(8)):
            tid+=1;events.append(('BEGIN',tid))
            writes={rng.randrange(10):rng.randrange(100) for _ in range(rng.randrange(5))}
            events.extend(('WRITE',tid,k,v) for k,v in writes.items())
            if rng.randrange(4):
                events.append(('COMMIT',tid));actual.update(writes)
        check(wal_committed_prefix(events)==actual,'committed_prefix_independent')
        if events:
            j=rng.randrange(len(events)+1)
            prefix=events[:j]
            complete=set(e[1] for e in prefix if e[0]=='COMMIT')
            expected={}
            for e in prefix:
                if e[0]=='WRITE' and e[1] in complete:expected[e[2]]=e[3]
            check(wal_committed_prefix(prefix)==expected,'midrecord_tail_independent')
    for _ in range(3000):
        p=tuple(rng.randrange(1000)/10 for i in range(rng.randrange(1,8)))
        actual=tuple(rng.randrange(1000)/10 for i in range(len(p)))
        out=plan_regret(p,actual)
        check(abs(out['absolute_regret']-(actual[p.index(min(p))]-min(actual)))<1e-10,'plan_regret_direct')
    for _ in range(1200):
        a,b,c,d=(set(rng.sample(range(15),rng.randrange(8))) for i in range(4))
        check(detects_two_tx_write_skew(a,b,c,d)==(any(x in d for x in a) and any(x in b for x in c)),'rw_cycle_sets')
    return {'schema':'atlas.database-v1-finite-oracle/1','result':'passed','comparisons':checks,'failures':0,'seed':20261119,'categories':stats,
            'independence':'distinct brute-permutation, iterative page I/O, direct scan and materialized-log algorithms; same local Python runtime',
            'production_database_concurrency_certified':False,'physical_storage_durability_verified':False}
if __name__=='__main__':print(json.dumps(run(),indent=2))
