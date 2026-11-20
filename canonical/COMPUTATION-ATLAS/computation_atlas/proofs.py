"""Finite-state verification and mathematical cost models.

These are bounded checks. None is a theorem prover for arbitrary programs.
"""
from __future__ import annotations
from collections import deque
from math import sqrt,isfinite
from .models import InvalidInput

def finite_reachability(initial,transitions,goal,limit=10000):
    """Exhaust a finite supplied transition graph; limit hit -> unknown.

    transitions maps hashable states to finite successor sets. The returned path
    is one witness, not a proof about states outside supplied graph.
    """
    if not isinstance(transitions,dict) or limit<1:raise InvalidInput('finite transition map and positive limit required')
    if initial not in transitions:raise InvalidInput('initial state missing')
    visited={initial};front=deque([(initial,[initial])]);expanded=0
    while front:
        if expanded>=limit:return {'status':'unknown_budget_exhausted','explored':expanded}
        state,path=front.popleft();expanded+=1
        if goal(state):return {'status':'witness','path':path,'explored':expanded}
        for next_state in transitions[state]:
            if next_state not in transitions:raise InvalidInput('transition outside declared system')
            if next_state not in visited:visited.add(next_state);front.append((next_state,path+[next_state]))
    return {'status':'not_reachable_in_declared_finite_graph','explored':expanded}

def inductive_invariant(states,initial,successors,predicate):
    """Check initialization and preservation on a stated *finite* state universe.

    If state universe fails to include actual system states the conclusion is void.
    """
    states=set(states)
    if initial not in states:raise InvalidInput('missing initial state')
    if not predicate(initial):return {'status':'counterexample_initial','state':initial}
    for s in states:
        if predicate(s):
            for t in successors(s):
                if t not in states:raise InvalidInput('successor outside finite declared universe')
                if not predicate(t):return {'status':'counterexample_step','from':s,'to':t}
    return {'status':'inductive_in_declared_universe','universe_size':len(states)}

def witness_rank_decrease(states,successors,rank,terminal):
    """For finite graph: prove strictly decreasing nonnegative ranks outside terminals.

    A rank function is an input witness, not automatically discovered.
    """
    states=set(states)
    if not states:raise InvalidInput('nonempty state set')
    for s in states:
        k=rank(s)
        if type(k)!=int or k<0:raise InvalidInput('nonnegative integer rank needed')
        if terminal(s):continue
        nxt=list(successors(s))
        if not nxt:return {'status':'stuck_nonterminal','state':s}
        for t in nxt:
            if t not in states:raise InvalidInput('undeclared successor')
            if rank(t)>=k:return {'status':'rank_not_decreasing','from':s,'to':t}
    return {'status':'ranking_certificate_for_declared_finite_system','universe_size':len(states)}

def amdahl_speedup(parallel_fraction,workers,overhead_fraction=0.0):
    """Amdahl idealized speedup; overhead relative to one worker baseline.

    Assumes fixed work and uniform ideal parallel fraction, ignores I/O and skew
    unless represented by the caller-declared overhead term.
    """
    if any(type(x) not in (int,float) or not isfinite(x) for x in (parallel_fraction,workers,overhead_fraction)) or not 0<=parallel_fraction<=1 or type(workers)!=int or workers<1 or not 0<=overhead_fraction<=1e6:
        raise InvalidInput('invalid Amdahl model')
    return 1/((1-parallel_fraction)+parallel_fraction/workers+overhead_fraction)

def wilson_interval(successes,n,z=1.96):
    """Approximate frequentist Bernoulli score interval, not a guarantee."""
    if type(n)!=int or type(successes)!=int or not 1<=n or not 0<=successes<=n or not isfinite(z) or z<=0:raise InvalidInput('invalid Bernoulli sample')
    p=successes/n; q=z*z/n
    center=(p+q/2)/(1+q)
    half=z*sqrt(p*(1-p)/n+q/(4*n))/(1+q)
    return center-half,center+half

def estimate_operation_budget(n,branching,depth):
    """Upper bound for full b-ary search node visits, with strict caps."""
    if any(type(v)!=int for v in (n,branching,depth)) or n<0 or not 0<=branching<=1000 or not 0<=depth<=200:raise InvalidInput('bounded integer model')
    if branching==1:nodes=depth+1
    elif branching==0:nodes=1
    else:nodes=(branching**(depth+1)-1)//(branching-1)
    return {'nodes':nodes,'total_state_slots':nodes*n,'scope':'upper bound for declared complete b-ary tree; not a real program runtime'}
