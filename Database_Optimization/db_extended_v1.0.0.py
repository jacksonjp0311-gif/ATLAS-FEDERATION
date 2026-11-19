"""ATLAS FORGE #17: further offline database-planner and recovery reference models.

Finite, bounded pedagogical algorithms, not a server, production optimizer,
serializability verifier, physical I/O model or crash-durability certification.
All implementations use only the Python standard library.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations
from math import ceil, isfinite


def external_sort_page_io(pages: int, buffer_pages: int) -> dict:
    """Count sequential I/O under materialized run-generation and all merge passes.

    N input pages, B page frames, fan-in B-1. A final fully materialized
    sorted file is counted as N writes; no replacement selection or pipelining.
    """
    if pages < 0 or buffer_pages < 3:
        raise ValueError('pages>=0 and buffer_pages>=3 required')
    if pages == 0:
        return {'initial_runs': 0, 'merge_passes': 0, 'pages_read': 0,
                'pages_written': 0, 'total_page_io': 0}
    runs = ceil(pages/buffer_pages)
    initial = runs
    passes = 0
    while runs > 1:
        runs = ceil(runs/(buffer_pages-1))
        passes += 1
    io = 2*pages*(1+passes)
    return {'initial_runs': initial,'merge_passes': passes,
            'pages_read': pages*(1+passes),
            'pages_written': pages*(1+passes),'total_page_io': io}


@dataclass(frozen=True)
class JoinOrder:
    indices: tuple[int, ...]
    abstract_comparisons: float
    final_estimated_rows: float
    model_limits: str = 'Left-deep nested-loop only; independent pair-selectivity; no actual DBMS calibration'


def left_deep_dp(base_rows: tuple[int, ...], pair_selectivity: dict[tuple[int,int],float]) -> JoinOrder:
    """Exact optimal left-deep order for the stated *abstract* nested-loop model.

    r(S) = product base sizes * product pair factors within S (independence).
    C(S followed by j) = C(S) + r(S)*rows[j]. This is an educational
    planning model, not a measured optimizer. Ties broken lexicographically.
    """
    n = len(base_rows)
    if not 1 <= n <= 8 or any(type(r) is not int or r < 0 for r in base_rows):
        raise ValueError('1..8 nonnegative integer row counts required')
    for key, v in pair_selectivity.items():
        if not (isinstance(key,tuple) and len(key)==2 and
                all(type(x) is int and 0 <= x < n for x in key) and
                key[0] < key[1] and isinstance(v,(float,int)) and isfinite(v) and 0<=v<=1):
            raise ValueError('only sorted distinct pair keys and selectivities 0..1')
    def rows(mask: int) -> float:
        out = 1.0
        for i in range(n):
            if mask>>i&1:out*=base_rows[i]
        for (i,j),factor in pair_selectivity.items():
            if mask>>i&1 and mask>>j&1:out*=factor
        return out
    best = {1<<i: (float(base_rows[i]),(i,)) for i in range(n)}
    for size in range(2,n+1):
        for group in combinations(range(n),size):
            mask=sum(1<<i for i in group)
            options=[]
            for last in group:
                prev=mask ^ (1<<last)
                cost,order=best[prev]
                options.append((cost+rows(prev)*base_rows[last],order+(last,)))
            best[mask]=min(options)
    cost, order=best[(1<<n)-1]
    return JoinOrder(order,cost,rows((1<<n)-1))


def index_only_visibility(row_heap_pages: tuple[int, ...], all_visible_pages: frozenset[int]):
    """Index-only access viability: MVCC may still force a heap visibility check.

    counts candidate rows, not unique pages; actual DBMS fetch/caching differs.
    """
    if any(type(p) is not int or p<0 for p in row_heap_pages):
        raise ValueError('row heap page identifiers must be >=0 integers')
    if any(type(p) is not int or p<0 for p in all_visible_pages):
        raise ValueError('visibility set must contain nonnegative page IDs')
    heap_checks=sum(1 for p in row_heap_pages if p not in all_visible_pages)
    return {'candidate_rows':len(row_heap_pages),
            'heap_visibility_checks':heap_checks,
            'index_only_rows':len(row_heap_pages)-heap_checks}


def detects_two_tx_write_skew(first_reads: set[str], first_writes: set[str],
                             second_reads: set[str], second_writes: set[str]) -> bool:
    """Detect a two-transaction rw-dependency cycle under a common snapshot.

    A *necessary warning* for the specific two-transaction cycle; not a
    complete serializability checker and not proof of a real concurrency bug.
    """
    return bool(first_reads & second_writes) and bool(second_reads & first_writes)


def wal_committed_prefix(events: list[tuple]) -> dict:
    """Replay committed in-memory transaction records; ignore incomplete tails.

    Events: ('BEGIN',tid), ('WRITE',tid,key,value), ('COMMIT',tid).
    This model does NOT flush, fsync, detect torn sectors, or prove durability.
    """
    pending: dict[object,dict] = {}
    committed: dict = {}
    for event in events:
        if not isinstance(event,tuple) or len(event)<2: raise ValueError('invalid event')
        kind,tid=event[:2]
        if kind=='BEGIN' and len(event)==2:
            if tid in pending:raise ValueError('duplicate active BEGIN')
            pending[tid]={}
        elif kind=='WRITE' and len(event)==4:
            if tid not in pending:raise ValueError('WRITE without BEGIN')
            pending[tid][event[2]]=event[3]
        elif kind=='COMMIT' and len(event)==2:
            if tid not in pending:raise ValueError('COMMIT without BEGIN')
            committed.update(pending.pop(tid))
        else:raise ValueError('unknown or malformed WAL record')
    return committed


def plan_regret(predicted: tuple[float, ...], measured: tuple[float, ...]) -> dict:
    """Identify risk of a miscalibrated cost estimator; zero is optimal observed cost.

    Observed values are caller-provided and are NOT physical measurements
    performed by this module.
    """
    if not predicted or len(predicted)!=len(measured):raise ValueError('nonempty matched plans')
    if any(not(isinstance(x,(int,float)) and isfinite(x) and x>=0) for x in predicted+measured):
        raise ValueError('costs must be finite nonnegative numbers')
    chosen=min(range(len(predicted)),key=lambda k:(predicted[k],k))
    optimal=min(range(len(measured)),key=lambda k:(measured[k],k))
    return {'chosen':chosen,'observed_best':optimal,
            'absolute_regret':float(measured[chosen]-measured[optimal]),
            'cost_model_certified':False}
