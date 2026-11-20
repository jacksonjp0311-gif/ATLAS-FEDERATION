"""Pure-Python reference algorithms with explicit mathematical limits.

All external behavior is prohibited. Finite checks are examples, not universal proof.
Algorithmic implementations are independently authored for this research library.
"""
from __future__ import annotations
from collections import Counter, deque
from fractions import Fraction
from heapq import heappush,heappop
from math import isfinite, fsum, log2

class InvalidInput(ValueError):
    pass

def counter_machine(program: list[tuple], initial=(0, 0), step_budget=10000):
    """Two-counter Minsky-style program. Exhausting budget means UNKNOWN, not non-halting.

    Instructions: ('inc', register_index, next_pc), ('decjz', register_index,
    positive_pc, zero_pc), ('halt',). Registered counters remain nonnegative.
    """
    if not isinstance(step_budget,int) or not 0<=step_budget<=1000000:raise InvalidInput('bounded step budget required')
    if not isinstance(initial,(list,tuple)) or len(initial)!=2 or any(type(x)!=int or x<0 for x in initial):raise InvalidInput('two nonnegative integer counters required')
    if not isinstance(program,(list,tuple)) or not program or len(program)>10000:raise InvalidInput('finite nonempty program required')
    for op in program:
        if not isinstance(op,(tuple,list)) or not op or op[0] not in ('inc','decjz','halt'):raise InvalidInput('invalid instruction')
        if op[0]=='halt':
            if len(op)!=1:raise InvalidInput('halt takes no args')
        elif op[0]=='inc':
            if len(op)!=3 or op[1] not in (0,1) or type(op[2])!=int or not 0<=op[2]<len(program):raise InvalidInput('invalid inc target')
        else:
            if len(op)!=4 or op[1] not in (0,1) or any(type(v)!=int or not 0<=v<len(program) for v in op[2:]):raise InvalidInput('invalid branch target')
    regs=list(initial);pc=0
    for step in range(step_budget+1):
        op=program[pc]
        if op[0]=='halt':return {'status':'halted','steps':step,'registers':tuple(regs),'pc':pc}
        if step==step_budget:break
        if op[0]=='inc':
            regs[op[1]]+=1;pc=op[2]
        else:
            i=op[1]
            if regs[i]==0:pc=op[3]
            else:regs[i]-=1;pc=op[2]
    return {'status':'unknown_budget_exhausted','steps':step_budget,'registers':tuple(regs),'pc':pc}

def stable_mergesort(items, key=None):
    """Stable merge sort; arbitrary Python objects must have orderable keys."""
    key=(lambda x:x) if key is None else key
    values=[(key(v),i,v) for i,v in enumerate(items)]
    def sort(seq):
        if len(seq)<=1:return seq
        mid=len(seq)//2; a=sort(seq[:mid]); b=sort(seq[mid:]);out=[];i=j=0
        while i<len(a) and j<len(b):
            if a[i][0]<=b[j][0]:out.append(a[i]);i+=1
            else:out.append(b[j]);j+=1
        return out+a[i:]+b[j:]
    return [tr[2] for tr in sort(values)]

def lower_bound(sorted_values,target):
    """Position of first element >= target, given a non-decreasing input."""
    lo,hi=0,len(sorted_values)
    while lo<hi:
        mid=(lo+hi)//2
        if sorted_values[mid]<target:lo=mid+1
        else:hi=mid
    return lo

def validate_graph(graph,allow_negative=False):
    if not isinstance(graph,dict) or not graph:raise InvalidInput('nonempty adjacency dictionary required')
    nodes=set(graph)
    if any(not isinstance(n,str) or not n for n in nodes):raise InvalidInput('node IDs must be strings')
    if any(not isinstance(edges,dict) for edges in graph.values()):raise InvalidInput('adjacency neighbors must be dictionaries')
    for src,adj in graph.items():
        for dst,w in adj.items():
            if dst not in nodes or type(w) not in (int,float) or not isfinite(w):raise InvalidInput('unknown node or nonfinite edge')
            if not allow_negative and w<0:raise InvalidInput('Dijkstra requires nonnegative weights')
    return sorted(nodes)

def dijkstra(graph,source):
    nodes=validate_graph(graph)
    if source not in graph:raise InvalidInput('unknown source')
    dist={n:float('inf') for n in nodes};parent={n:None for n in nodes};dist[source]=0
    h=[(0,source)]
    while h:
        d,u=heappop(h)
        if d>dist[u]:continue
        for v,w in sorted(graph[u].items()):
            nd=d+w
            if nd<dist[v]:dist[v]=nd;parent[v]=u;heappush(h,(nd,v))
    return {'distances':dist,'parents':parent,'source':source,'claim':'shortest paths for nonnegative edge costs'}

def bellman_ford(graph,source):
    nodes=validate_graph(graph,allow_negative=True)
    if source not in graph:raise InvalidInput('unknown source')
    dist={n:float('inf') for n in nodes};parent={n:None for n in nodes};dist[source]=0.0
    edges=[(u,v,w) for u in nodes for v,w in sorted(graph[u].items())]
    for _ in range(len(nodes)-1):
        updated=False
        for u,v,w in edges:
            if isfinite(dist[u]) and dist[u]+w<dist[v]:dist[v]=dist[u]+w;parent[v]=u;updated=True
        if not updated:break
    if any(isfinite(dist[u]) and dist[u]+w<dist[v] for u,v,w in edges):
        return {'status':'reachable_negative_cycle','distances':None,'parents':None}
    return {'status':'finite_shortest_paths','distances':dist,'parents':parent}

def topological_order(graph):
    """Directed graph adjacency mapping to iterable neighbor IDs."""
    if not isinstance(graph,dict):raise InvalidInput('graph required')
    nodes=set(graph);indeg={n:0 for n in nodes}
    for u,ns in graph.items():
        for v in set(ns):
            if v not in indeg:raise InvalidInput('unknown node')
            indeg[v]+=1
    h=[]
    for n,d in indeg.items():
        if d==0:heappush(h,n)
    order=[]
    while h:
        u=heappop(h);order.append(u)
        for v in set(graph[u]):
            indeg[v]-=1
            if indeg[v]==0:heappush(h,v)
    if len(order)!=len(nodes):raise InvalidInput('cycle: no topological ordering')
    return order

def edit_distance(a,b):
    """Unit-cost Levenshtein distance using O(min(n,m)) auxiliary space."""
    if len(a)<len(b):a,b=b,a
    prior=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        row=[i]
        for j,cb in enumerate(b,1):
            row.append(min(row[j-1]+1,prior[j]+1,prior[j-1]+(ca!=cb)))
        prior=row
    return prior[-1]

def knapsack_01(weights, values, capacity):
    """Nonnegative integer weights/capacity: pseudo-polynomial O(n * capacity)."""
    if not isinstance(capacity,int) or capacity<0 or capacity>100000:raise InvalidInput('capacity cap')
    if len(weights)!=len(values) or len(weights)*(capacity+1)>2000000:raise InvalidInput('size bound')
    if any(type(w)!=int or w<0 for w in weights):raise InvalidInput('nonnegative integer weights')
    if any(type(v) not in (int,float) or not isfinite(v) for v in values):raise InvalidInput('finite values')
    dp=[[0.0]*(capacity+1) for _ in range(len(weights)+1)]
    for i,(w,v) in enumerate(zip(weights,values),1):
        for c in range(capacity+1):
            dp[i][c]=dp[i-1][c]
            if w<=c and dp[i-1][c-w]+v>dp[i][c]:dp[i][c]=dp[i-1][c-w]+v
    c=capacity;selected=[]
    for i in range(len(weights),0,-1):
        w=weights[i-1];v=values[i-1]
        if w<=c and dp[i][c]>dp[i-1][c]:selected.append(i-1);c-=w
    return {'value':dp[-1][-1],'indices':tuple(reversed(selected)),'capacity':capacity}

def extended_gcd(a,b):
    """For integer a,b, produce nonnegative gcd and Bezout coefficients."""
    if type(a)!=int or type(b)!=int:raise InvalidInput('integers required')
    x0,x1,y0,y1=1,0,0,1
    aa,bb=a,b
    while bb:
        q=aa//bb;aa,bb=bb,aa-q*bb;x0,x1=x1,x0-q*x1;y0,y1=y1,y0-q*y1
    return (abs(aa), x0 if aa>=0 else -x0, y0 if aa>=0 else -y0)

def rational_interval(lo,hi):
    a,b=Fraction(lo),Fraction(hi)
    if a>b:raise InvalidInput('inverted interval')
    return a,b

def interval_add(a,b):
    al,ah=rational_interval(*a);bl,bh=rational_interval(*b)
    return al+bl,ah+bh

def interval_mul(a,b):
    al,ah=rational_interval(*a);bl,bh=rational_interval(*b)
    p=[x*y for x in (al,ah) for y in (bl,bh)]
    return min(p),max(p)

def bisection(f,a,b,*,continuous_confirmed=False,atol=1e-10,max_steps=256):
    """Returns a bracket. Root-existence claim requires caller-declared continuity."""
    if not continuous_confirmed:raise InvalidInput('cannot claim intermediate-value theorem without continuity assumption')
    if not 0<atol<1 or not 1<=max_steps<=10000 or not a<b:raise InvalidInput('invalid bracket/tolerance')
    fa,fb=f(a),f(b)
    if not isfinite(fa) or not isfinite(fb):raise InvalidInput('nonfinite function')
    if fa==0:return {'interval':(a,a),'estimate':a,'iterations':0,'status':'certified_under_declared_continuity'}
    if fb==0:return {'interval':(b,b),'estimate':b,'iterations':0,'status':'certified_under_declared_continuity'}
    if (fa<0)==(fb<0):raise InvalidInput('no sign change')
    for step in range(max_steps):
        if (b-a)<=atol:break
        mid=a+(b-a)/2
        if mid==a or mid==b:break
        fm=f(mid)
        if not isfinite(fm):raise InvalidInput('nonfinite midpoint')
        if fm==0:return {'interval':(mid,mid),'estimate':mid,'iterations':step+1,'status':'certified_under_declared_continuity'}
        if (fm<0)==(fa<0):a,fa=mid,fm
        else:b,fb=mid,fm
    return {'interval':(a,b),'estimate':a+(b-a)/2,'iterations':step+1,'status':'bounded_bracket_under_declared_continuity'}

def kahan_sum(xs):
    total=0.;correction=0.
    for x in xs:
        if not isfinite(float(x)):raise InvalidInput('nonfinite sum term')
        y=float(x)-correction;t=total+y;correction=(t-total)-y;total=t
    return total

def shannon_entropy(probabilities):
    ps=list(probabilities)
    if not ps or any(type(p) not in (int,float) or not isfinite(p) or p<0 for p in ps) or abs(fsum(ps)-1)>1e-10:raise InvalidInput('normalized finite probability vector required')
    return -fsum(p*log2(p) for p in ps if p>0)

def sorted_permutation_certificate(before,after):
    """One finite output certificate. It cannot establish universal algorithm correctness."""
    return len(before)==len(after) and all(after[i]<=after[i+1] for i in range(len(after)-1)) and Counter(before)==Counter(after)

def shortest_path_certificate(graph,source,result):
    """Check parent-chain reachability and triangle constraints, not runtime provenance.

    The certificate is valid for finite nonnegative weights and exact arithmetic up to tolerance.
    """
    try:
        nodes=validate_graph(graph)
        d=result['distances'];parent=result['parents']
        if set(d)!=set(nodes) or set(parent)!=set(nodes) or d[source]!=0 or parent[source] is not None:return False
        for u in nodes:
            if d[u]<0 or (not isfinite(d[u]) and d[u]!=float('inf')):return False
            if u==source:continue
            if isfinite(d[u]):
                visited=set();v=u
                while v!=source:
                    if v in visited:return False
                    visited.add(v);p=parent[v]
                    if p is None or v not in graph[p] or not isfinite(d[p]) or abs(d[p]+graph[p][v]-d[v])>1e-8:return False
                    v=p
            elif parent[u] is not None:return False
        for u in nodes:
            for v,w in graph[u].items():
                if d[v]>d[u]+w+1e-8:return False
        return True
    except (KeyError,TypeError,InvalidInput,ValueError,OverflowError):return False

def prefix_free(codes):
    values=list(codes)
    if any(not isinstance(c,str) or not c or any(bit not in '01' for bit in c) for c in values):return False
    if len(values)!=len(set(values)):return False
    return all(not v.startswith(u) for u in values for v in values if u!=v)
