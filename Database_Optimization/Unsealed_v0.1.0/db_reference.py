"""ATLAS FORGE original #17: bounded, offline database-optimization reference.

Educational models; not a production database, durability certificate, or real cost model.
Python standard library only. See SCIENTIFIC_LIMITS.md for the precise assumptions.
"""
from __future__ import annotations
from collections import OrderedDict
from dataclasses import dataclass
from heapq import heappop, heappush
from math import ceil, log2
from typing import Iterable
import sqlite3


def sql_and(a: bool | None, b: bool | None) -> bool | None:
    if a is False or b is False: return False
    if a is None or b is None: return None
    return True


def sql_or(a: bool | None, b: bool | None) -> bool | None:
    if a is True or b is True: return True
    if a is None or b is None: return None
    return False


def sql_not(a: bool | None) -> bool | None:
    return None if a is None else not a


def sql_eq(a, b) -> bool | None:
    if a is None or b is None: return None
    return a == b


def lru_trace(pages: Iterable[int], capacity: int) -> tuple[list[bool], tuple[int, ...]]:
    """Return per-request cache hit and final LRU->MRU page IDs."""
    if capacity < 0: raise ValueError('capacity must be nonnegative')
    recent: OrderedDict[int, None] = OrderedDict()
    hits: list[bool] = []
    for page in pages:
        hit = page in recent
        hits.append(hit)
        if hit: recent.move_to_end(page)
        elif capacity:
            recent[page] = None
            if len(recent) > capacity: recent.popitem(last=False)
    return hits, tuple(recent)


def fifo_trace(pages: Iterable[int], capacity: int) -> tuple[list[bool], tuple[int, ...]]:
    """Return FIFO hits and oldest->newest resident IDs; hits do not change order."""
    if capacity < 0: raise ValueError('capacity must be nonnegative')
    residents: dict[int, None] = {}
    queue: list[int] = []
    hits = []
    for page in pages:
        hit = page in residents
        hits.append(hit)
        if not hit and capacity:
            if len(queue) == capacity:
                old = queue.pop(0); residents.pop(old)
            queue.append(page); residents[page] = None
    return hits, tuple(queue)


@dataclass(frozen=True)
class PlanEstimate:
    scan_cost: float
    index_cost: float
    selected: str
    expected_rows: int
    table_pages: int
    qualification: str = 'heuristic only; not calibrated to hardware or any DBMS'


def estimate_scan_vs_index(rows: int, rows_per_page: int, selectivity: float,
                           sequential_page_cost: float = 1.0, random_page_cost: float = 4.0,
                           cpu_row_cost: float = 0.01, clustered: bool = False) -> PlanEstimate:
    """Simple positive-cost *illustration* of scan / single-column index tradeoffs."""
    if rows < 0 or rows_per_page <= 0 or not 0 <= selectivity <= 1:
        raise ValueError('invalid table size or selectivity')
    if min(sequential_page_cost, random_page_cost, cpu_row_cost) < 0:
        raise ValueError('cost weights must be nonnegative')
    table_pages = ceil(rows / rows_per_page)
    match_rows = ceil(rows * selectivity)
    traversal = ceil(log2(table_pages + 1)) if rows else 0
    seek_pages = min(table_pages, ceil(match_rows / rows_per_page) if clustered else match_rows)
    scan = table_pages * sequential_page_cost + rows * cpu_row_cost
    index = traversal * random_page_cost + seek_pages * random_page_cost + match_rows * cpu_row_cost
    return PlanEstimate(scan, index, 'index' if index < scan else 'scan', match_rows, table_pages)


def exact_conjunctive_selectivity(rows: list[tuple], i: int, ai, j: int, bj) -> float:
    return sum(r[i] == ai and r[j] == bj for r in rows) / len(rows) if rows else 0.0


def independence_selectivity(rows: list[tuple], i: int, ai, j: int, bj) -> float:
    """The independence assumption can severely underestimate correlated columns."""
    if not rows: return 0.0
    return (sum(r[i] == ai for r in rows) / len(rows) *
            sum(r[j] == bj for r in rows) / len(rows))


def hash_join(left: list[tuple], right: list[tuple], left_key: int, right_key: int):
    """Bag-semantics equijoin; None is SQL NULL and never matches."""
    buckets: dict[object, list[tuple]] = {}
    for b in right:
        k = b[right_key]
        if k is not None: buckets.setdefault(k, []).append(b)
    return [(a, b) for a in left if a[left_key] is not None
            for b in buckets.get(a[left_key], [])]


def merge_join(left: list[tuple], right: list[tuple], left_key: int, right_key: int):
    """Sorted equijoin preserving duplicate multiplicity; comparable keys required."""
    a = sorted((x for x in left if x[left_key] is not None), key=lambda x: x[left_key])
    b = sorted((x for x in right if x[right_key] is not None), key=lambda x: x[right_key])
    i = j = 0; result = []
    while i < len(a) and j < len(b):
        x, y = a[i][left_key], b[j][right_key]
        if x < y: i += 1; continue
        if x > y: j += 1; continue
        istart, jstart = i, j
        while i < len(a) and a[i][left_key] == x: i += 1
        while j < len(b) and b[j][right_key] == y: j += 1
        result.extend((aa, bb) for aa in a[istart:i] for bb in b[jstart:j])
    return result


def external_merge_sort(values: list[tuple], key_index: int, run_limit: int) -> list[tuple]:
    """Bounded run sort + k-way merge (runs are materialized here, not disk spilled)."""
    if run_limit < 1: raise ValueError('positive run_limit required')
    runs = [sorted(values[i:i+run_limit], key=lambda v: v[key_index])
            for i in range(0, len(values), run_limit)]
    heap: list[tuple] = []
    for i, run in enumerate(runs):
        if run: heappush(heap, (run[0][key_index], i, 0))
    out = []
    while heap:
        _, ridx, pos = heappop(heap)
        out.append(runs[ridx][pos]); pos += 1
        if pos < len(runs[ridx]):
            heappush(heap, (runs[ridx][pos][key_index], ridx, pos))
    return out


@dataclass
class SortedLeafIndex:
    """Bulk-loaded leaf/fence index, not a full concurrent B+ tree.

    Key order must be a mutually comparable scalar and values are row IDs.
    Leaf maximum fences ensure duplicate keys spanning leaves are not missed.
    """
    leaves: list[list[tuple]]
    maxima: list

    @classmethod
    def from_entries(cls, entries: list[tuple], leaf_capacity: int = 4):
        if leaf_capacity < 2: raise ValueError('leaf_capacity must be >= 2')
        entries = sorted(entries, key=lambda p: (p[0], p[1]))
        leaves = [entries[i:i+leaf_capacity] for i in range(0, len(entries), leaf_capacity)]
        return cls(leaves, [leaf[-1][0] for leaf in leaves])

    def _first_leaf(self, key) -> int:
        lo, hi = 0, len(self.maxima)
        while lo < hi:
            mid = (lo+hi)//2
            if self.maxima[mid] < key: lo = mid + 1
            else: hi = mid
        return lo

    def search(self, key) -> list:
        out = []
        for leaf in self.leaves[self._first_leaf(key):]:
            for k, rid in leaf:
                if k == key: out.append(rid)
                elif k > key: return out
        return out

    def range(self, low, high) -> list:
        if low > high: return []
        out = []
        for leaf in self.leaves[self._first_leaf(low):]:
            for k, rid in leaf:
                if k > high: return out
                if k >= low: out.append((k, rid))
        return out


class MVCCVisibility:
    """Immutable history, commit-sequence snapshots; not concurrency control/SSI."""
    def __init__(self):
        self.clock = 0
        self.versions: dict[object, list[tuple[int, object | None]]] = {}

    def begin(self) -> int: return self.clock

    def commit(self, changes: dict):
        self.clock += 1
        for key, value in changes.items():
            self.versions.setdefault(key, []).append((self.clock, value))
        return self.clock

    def read(self, key, snapshot: int):
        if snapshot < 0 or snapshot > self.clock: raise ValueError('invalid snapshot')
        for ts, value in reversed(self.versions.get(key, [])):
            if ts <= snapshot: return value
        return None

    def scan(self, snapshot: int):
        return {k: v for k in self.versions if (v := self.read(k,snapshot)) is not None}


def sqlite_observation(conn: sqlite3.Connection, query: str, params: tuple = ()) -> dict:
    """Grounded observation from the actual SQLite engine; read-only SELECT only."""
    if not query.lstrip().upper().startswith('SELECT '):
        raise ValueError('read-only SELECT query required')
    plan = conn.execute('EXPLAIN QUERY PLAN '+query,params).fetchall()
    rows = conn.execute(query,params).fetchall()
    return {'plan': [tuple(r) for r in plan], 'rows': rows, 'total_rows': len(rows)}
