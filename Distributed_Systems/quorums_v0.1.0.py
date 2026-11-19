"""Finite sets and count-based crash-fault quorums. No network assumptions."""
from itertools import combinations

def majority_size(n):
    if type(n) is not int or n<1:raise ValueError('positive node count required')
    return n//2+1

def all_quorums(n,q):
    if not 1<=q<=n or type(n)!=int or type(q)!=int:raise ValueError('invalid quorum')
    return (frozenset(c) for c in combinations(range(n),q))

def guaranteed_overlap(n,q1,q2):
    if any(type(v)!=int for v in (n,q1,q2)) or n<1 or not (1<=q1<=n and 1<=q2<=n):raise ValueError('invalid quorum parameters')
    return q1+q2>n

def intersection_lower_bound(n,q1,q2):
    guaranteed_overlap(n,q1,q2)
    return max(0,q1+q2-n)

def worst_case_crash_availability(n,q,failed):
    guaranteed_overlap(n,q,q)
    if type(failed)!=int or not 0<=failed<=n:raise ValueError('invalid failures')
    return n-failed>=q
