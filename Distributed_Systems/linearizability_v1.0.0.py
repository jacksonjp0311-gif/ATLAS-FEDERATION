"""Exact bounded completed register-history linearizability checker.

Models one atomic read/write register; response timestamps mark real-time order.
Pending calls, failed writes, ambiguous multi-object histories are rejected.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Op:
    ident: str
    kind: str
    start: int
    end: int
    value: str | None = None
    result: str | None = None


def history_witness(ops, initial='0', *, limit=9):
    ops = tuple(ops)
    if len(ops) > limit or len(ops) > 9 or len({o.ident for o in ops}) != len(ops):
        raise ValueError('invalid unique bounded operations')
    for op in ops:
        if op.kind not in ('read', 'write') or type(op.start) is not int or type(op.end) is not int or op.end <= op.start:
            raise ValueError('completed valid invocation-response required')
        if op.kind == 'write' and (not isinstance(op.value, str) or op.result != 'ok'):
            raise ValueError('successful write required')
        if op.kind == 'read' and (op.value is not None or not isinstance(op.result, str)):
            raise ValueError('known read response required')
    prereq = tuple(frozenset(i for i, a in enumerate(ops) if i != j and a.end <= b.start)
                   for j, b in enumerate(ops))
    def backtrack(done, val, order):
        if len(done) == len(ops): return order
        for idx, op in enumerate(ops):
            if idx in done or not prereq[idx].issubset(done): continue
            if op.kind == 'read' and op.result != val: continue
            result = backtrack(done | {idx}, op.value if op.kind == 'write' else val, order + (op.ident,))
            if result is not None: return result
        return None
    return backtrack(frozenset(), initial, ())
