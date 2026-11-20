"""Bounded exhaustive *macro-step* exploration of two-ballot single-decree Paxos.

No real asynchronous network, fairness, Byzantine fault tolerance or dynamic membership.
Actions nondeterministically choose prepare responder quorum and delivered accept subset,
including interleaving two proposers. Promise/accepted state is durable by assumption.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations

@dataclass(frozen=True)
class State:
    acceptors: tuple[tuple[int, int, str | None], ...]
    phase: tuple[int, int] = (0, 0)  # 0 not prepared, 1 prepared, 2 sent acceptance
    prepared: tuple[tuple[tuple[int, ...], str] | None, ...] = (None, None)
    chosen: tuple[str, ...] = ()



def options(ids):
    seq = tuple(ids)
    return (tuple(c for r in range(len(seq) + 1) for c in combinations(seq, r)))


def step(state: State, proposer: int, targets: tuple[int, ...], *, unsafe: bool = False) -> State:
    """One quorum prepare or one delivery-selected accept phase; zero replies model loss."""
    if proposer not in (0, 1):
        raise ValueError('two unique proposers, ballots 1 and 2')
    n = len(state.acceptors)
    if n < 3 or n % 2 != 1 or len(set(targets)) != len(targets) or any(i < 0 or i >= n for i in targets):
        raise ValueError('fixed odd-sized valid membership')
    ballot, value = proposer + 1, ('A', 'B')[proposer]
    q = n // 2 + 1
    a = list(state.acceptors)
    phase = list(state.phase)
    prepared = list(state.prepared)
    chosen = state.chosen
    if phase[proposer] == 0:
        # No-reply members are outside targets. Only higher ballots grant promises.
        response = []
        for idx in targets:
            promised, accepted_n, accepted_value = a[idx]
            if ballot > promised:
                response.append((idx, accepted_n, accepted_value))
                a[idx] = (ballot, accepted_n, accepted_value)
        # Each proposer gets only one bounded prepare attempt.
        phase[proposer] = 1 if len(response) >= q else 2
        if len(response) >= q:
            prior = [(bn, val) for _, bn, val in response if bn >= 0]
            value_selected = value if unsafe or not prior else max(prior, key=lambda x: x[0])[1]
            prepared[proposer] = (tuple(i for i, _, _ in response), value_selected)
    elif phase[proposer] == 1:
        responders, selected = prepared[proposer]
        if not set(targets).issubset(responders):
            raise ValueError('can only accept at prior promise responders')
        accepted = 0
        for idx in targets:
            pn, _, _ = a[idx]
            if ballot >= pn:
                a[idx] = (ballot, ballot, selected)
                accepted += 1
        phase[proposer] = 2
        if accepted >= q:
            chosen = chosen + (selected,)
    else:
        raise ValueError('proposer attempt completed')
    return State(tuple(a), tuple(phase), tuple(prepared), chosen)


def transitions(s: State, *, unsafe: bool = False):
    n = len(s.acceptors)
    for proposer in (0, 1):
        stage = s.phase[proposer]
        if stage == 0:
            # all responder subsets: absent replies, partitions, selective delivery
            choices = options(range(n))
        elif stage == 1:
            choices = options(s.prepared[proposer][0])
        else:
            continue
        for ids in choices:
            next_state = step(s, proposer, ids, unsafe=unsafe)
            yield (proposer, ids), next_state


def check_agreement(*, n=3, unsafe=False, max_states=50000):
    if n != 3: raise ValueError('verified search space is exactly three acceptors')
    initial = State(tuple((-1, -1, None) for _ in range(n)))
    queue = [(initial, ())]
    seen = {initial}
    idx = 0
    completed = 0
    while idx < len(queue):
        s, trace = queue[idx]; idx += 1
        if len(set(s.chosen)) > 1:
            return {'safe': False, 'states': len(seen), 'trace': trace, 'choices': s.chosen, 'exhausted': True}
        if s.phase == (2, 2): completed += 1
        for action, nxt in transitions(s, unsafe=unsafe):
            if nxt not in seen:
                if len(seen) >= max_states:
                    return {'safe': None, 'states': len(seen), 'trace': (), 'exhausted': False}
                seen.add(nxt)
                queue.append((nxt, trace + (action,)))
    return {'safe': True, 'states': len(seen), 'terminal_states': completed, 'trace': (), 'exhausted': True}
