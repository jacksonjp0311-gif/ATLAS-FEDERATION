"""Finite, reconstructible algorithm references for Computation Atlas v0.2.

No networking, untrusted code execution, production cryptography, deployment,
or inference of physical/scientific generalization.
"""
from __future__ import annotations
from collections import deque
from fractions import Fraction
from math import cos,sin,pi,exp,log,sqrt,isfinite
import hashlib,json

class ComputationError(ValueError):pass

class DisjointSets:
    """Union-find using path compression and union by size; labels 0..n-1."""
    def __init__(self,n):
        if type(n)!=int or not 1<=n<=100000:raise ComputationError('n must be integer in 1..100000')
        self.parent=list(range(n));self.size=[1]*n;self.components=n
    def find(self,x):
        if type(x)!=int or not 0<=x<len(self.parent):raise ComputationError('unknown element')
        while x!=self.parent[x]:
            self.parent[x]=self.parent[self.parent[x]];x=self.parent[x]
        return x
    def union(self,x,y):
        a,b=self.find(x),self.find(y)
        if a==b:return False
        if self.size[a]<self.size[b] or (self.size[a]==self.size[b] and a>b):a,b=b,a
        self.parent[b]=a;self.size[a]+=self.size[b];self.components-=1
        return True
    def same(self,x,y):return self.find(x)==self.find(y)

def kruskal_forest(n,edges):
    """Minimum spanning forest on an undirected weighted multigraph with finite weights."""
    uf=DisjointSets(n)
    if not isinstance(edges,list) or len(edges)>200000:raise ComputationError('bounded edge list required')
    parsed=[]
    for idx,e in enumerate(edges):
        if not isinstance(e,(list,tuple)) or len(e)!=3:raise ComputationError('edge must be (u,v,cost)')
        u,v,c=e;uf.find(u);uf.find(v)
        if type(c) not in (int,float) or not isfinite(c):raise ComputationError('finite edge weight required')
        parsed.append((float(c),min(u,v),max(u,v),idx))
    selected=[];total=0
    for w,u,v,idx in sorted(parsed):
        if uf.union(u,v):selected.append(idx);total+=w
    return {'selected_edge_indices':selected,'total_cost':total,'components':uf.components,
            'status':'minimum_spanning_forest_for_declared_graph',
            'limitations':['Only declared undirected graph, not hidden network costs',
                           'Finite tested inputs are not a universal proof of source interpretation']}

def max_flow_min_cut(n,edges,source,sink):
    """Edmonds–Karp flow and matching min cut for a small directed network.

    Multiple directed arcs and opposite arcs are aggregated, capacities finite >=0.
    Complexity O(V E^2) abstract augmentations. No live network flows.
    """
    if type(n)!=int or not 2<=n<=60 or type(source)!=int or type(sink)!=int or source==sink or not 0<=source<n or not 0<=sink<n:
        raise ComputationError('invalid bounded network/endpoints')
    if not isinstance(edges,list) or len(edges)>5000:raise ComputationError('bounded edges required')
    caps=[[0.0]*n for _ in range(n)];adj=[set() for _ in range(n)]
    for e in edges:
        if not isinstance(e,(list,tuple)) or len(e)!=3:raise ComputationError('edge tuple required')
        u,v,c=e
        if type(u)!=int or type(v)!=int or not 0<=u<n or not 0<=v<n or type(c) not in (float,int) or not isfinite(c) or c<0:raise ComputationError('invalid capacity')
        if u==v:continue
        caps[u][v]+=float(c)
        if not isfinite(caps[u][v]):raise ComputationError('capacity aggregation overflow')
        adj[u].add(v);adj[v].add(u)
    residual=[row[:] for row in caps];flow=0.0;augmentations=0
    while True:
        parent=[None]*n;parent[source]=source;Q=deque([source])
        while Q and parent[sink] is None:
            u=Q.popleft()
            for v in sorted(adj[u]):
                if parent[v] is None and residual[u][v]>0:
                    parent[v]=u;Q.append(v)
        if parent[sink] is None:break
        path=[];v=sink;delta=float('inf')
        while v!=source:
            u=parent[v];delta=min(delta,residual[u][v]);path.append((u,v));v=u
        if delta<=0 or not isfinite(delta):raise ComputationError('numeric augmentation failure')
        for u,v in path:
            residual[u][v]-=delta;residual[v][u]+=delta
            if residual[u][v]<0 and abs(residual[u][v])<1e-10:residual[u][v]=0.0
        flow+=delta;augmentations+=1
        if augmentations>n*max(1,len(edges))**2:raise ComputationError('unexpected augmentation bound')
    reachable={source};todo=[source]
    while todo:
        u=todo.pop()
        for v in adj[u]:
            if v not in reachable and residual[u][v]>1e-12:reachable.add(v);todo.append(v)
    cut=sum(caps[u][v] for u in reachable for v in range(n) if v not in reachable)
    return {'max_flow':flow,'min_cut_capacity':cut,'source_side':sorted(reachable),'augmentations':augmentations,
            'flow_cut_gap':abs(flow-cut),'status':'flow_cut_match_under_declared_network',
            'limitations':['Capacities are caller-supplied; no external effects',
                           'Float precision and near-zero residual tolerance may matter for extreme inputs']}

def gaussian_solve_exact(matrix,rhs):
    """Gauss-Jordan elimination on small square exact rational systems.

    String/integers recommended for exact decimal input: Fraction(0.1) retains
    an already-rounded float, while Fraction('0.1') denotes exact 1/10.
    """
    if not isinstance(matrix,list) or not 1<=len(matrix)<=12:raise ComputationError('square matrix dimension 1..12')
    n=len(matrix)
    if not isinstance(rhs,list) or len(rhs)!=n or any(not isinstance(row,list) or len(row)!=n for row in matrix):raise ComputationError('matrix dimension mismatch')
    try:a=[[Fraction(v) for v in row]+[Fraction(rhs[i])] for i,row in enumerate(matrix)]
    except (TypeError,ZeroDivisionError,ValueError,OverflowError) as e:raise ComputationError('rational entries required') from e
    for col in range(n):
        pivot=next((i for i in range(col,n) if a[i][col]!=0),None)
        if pivot is None:raise ComputationError('singular system; uniqueness not established')
        a[col],a[pivot]=a[pivot],a[col]
        fac=a[col][col];a[col]=[x/fac for x in a[col]]
        for row in range(n):
            if row!=col and a[row][col]!=0:
                fac=a[row][col];a[row]=[x-fac*y for x,y in zip(a[row],a[col])]
    x=[row[-1] for row in a]
    # Independent residual recomputation against original exact entries
    if any(sum(Fraction(matrix[i][j])*x[j] for j in range(n))!=Fraction(rhs[i]) for i in range(n)):
        raise ComputationError('rational residual failed')
    return {'solution':[str(q) for q in x],'exact_residual_zero':True,
            'status':'unique_solution_for_supplied_rational_matrix',
            'limitations':['No floating-point conditioning estimate or large sparse solver',
                           'Input conversion from binary float preserves its rounded value']}

def fft_radix2(values,inverse=False):
    """Radix-2 DFT with bounded power-of-two length. Rounding error remains."""
    if not isinstance(values,(list,tuple)) or not 1<=len(values)<=2048 or len(values)&(len(values)-1):raise ComputationError('power-of-two length 1..2048')
    n=len(values)
    try:
        a=[complex(x) for x in values]
        if any(not isfinite(z.real) or not isfinite(z.imag) for z in a):raise ComputationError('nonfinite input')
    except (TypeError,ValueError) as e:raise ComputationError('numeric complex input required') from e
    j=0
    for i in range(1,n):
        bit=n>>1
        while j&bit:j^=bit;bit>>=1
        j^=bit
        if i<j:a[i],a[j]=a[j],a[i]
    length=2
    while length<=n:
        angle=(2 if inverse else -2)*pi/length;root=complex(cos(angle),sin(angle));half=length//2
        for start in range(0,n,length):
            phase=1+0j
            for k in range(half):
                u=a[start+k];v=a[start+k+half]*phase
                a[start+k]=u+v;a[start+k+half]=u-v;phase*=root
        length*=2
    if inverse:a=[z/n for z in a]
    return a

def convolution_linear(a,b):
    """Linear convolution by zero-padded FFT, not circular without padding."""
    if not isinstance(a,(list,tuple)) or not isinstance(b,(list,tuple)) or not a or not b:raise ComputationError('nonempty sequences')
    length=len(a)+len(b)-1;n=1
    while n<length:n*=2
    if n>2048:raise ComputationError('bounded convolution output')
    A=fft_radix2(list(a)+[0]*(n-len(a)))
    B=fft_radix2(list(b)+[0]*(n-len(b)))
    return fft_radix2([x*y for x,y in zip(A,B)],inverse=True)[:length]

def hoeffding_interval(samples,delta=0.05):
    """Conditional bound for independent [0,1] observations; NOT a verified CI.

    Two-sided Hoeffding: epsilon=sqrt(log(2/delta)/(2 n)).
    Independence and identical mean are supplied assumptions, not tested.
    """
    if not isinstance(samples,list) or not 1<=len(samples)<=100000 or type(delta) not in (float,int) or not 0<delta<1:raise ComputationError('samples/delta bounds')
    if any(type(x) not in (int,float) or not isfinite(x) or not 0<=x<=1 for x in samples):raise ComputationError('observations must be finite in [0,1]')
    n=len(samples);mean=sum(samples)/n;radius=sqrt(log(2/delta)/(2*n))
    return {'mean':mean,'clipped_interval':(max(0,mean-radius),min(1,mean+radius)),
            'unclipped_half_width':radius,'n':n,'delta':delta,
            'coverage_verified_for_actual_data':False,'status':'conditional_iid_bound_only',
            'limitations':['Independence and fixed common expected value not verified',
                           'Repeated tasks, leakage and adaptive tuning invalidate naive interpretation']}

def vector_clock_tick(clock,index):
    if not isinstance(clock,(list,tuple)) or not clock or any(type(x)!=int or x<0 for x in clock) or type(index)!=int or not 0<=index<len(clock):raise ComputationError('invalid vector clock')
    out=list(clock);out[index]+=1;return tuple(out)

def vector_clock_merge(left,right,index):
    if not isinstance(left,(list,tuple)) or not isinstance(right,(list,tuple)) or len(left)!=len(right) or not left or any(type(x)!=int or x<0 for x in [*left,*right]) or type(index)!=int or not 0<=index<len(left):raise ComputationError('invalid vector clock')
    out=[max(x,y) for x,y in zip(left,right)];out[index]+=1;return tuple(out)

def vector_clock_relation(a,b):
    if not isinstance(a,(list,tuple)) or not isinstance(b,(list,tuple)) or len(a)!=len(b) or not a or any(type(x)!=int or x<0 for x in [*a,*b]):raise ComputationError('valid equal-length vector clock required')
    le=all(x<=y for x,y in zip(a,b));ge=all(x>=y for x,y in zip(a,b))
    if le and ge:return 'equal'
    if le:return 'happened_before'
    if ge:return 'happened_after'
    return 'concurrent'

def canonical_json_digest(data):
    """Deterministic local canonicalization subset; not RFC 8785 full JCS."""
    try:raw=json.dumps(data,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
    except (ValueError,TypeError,UnicodeError) as e:raise ComputationError('noncanonical JSON value') from e
    if len(raw)>1000000:raise ComputationError('payload cap')
    return hashlib.sha256(raw).hexdigest()
