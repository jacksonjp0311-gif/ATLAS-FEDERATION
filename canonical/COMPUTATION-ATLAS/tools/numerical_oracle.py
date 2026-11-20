"""Independent NumPy/SciPy/NetworkX and exhaustive oracles on synthetic inputs.

This is numerical algorithm validation on generated examples, NOT an empirical
scientific experiment or evidence of AI model improvement.
"""
from __future__ import annotations
import sys,math,random,itertools,json,platform,hashlib,statistics
from pathlib import Path
import numpy as np
import networkx as nx
from scipy.optimize import bisect as scipy_bisect
from fractions import Fraction
from computation_atlas.models import *
from computation_atlas.proofs import *

def check():
    counts={};rng=random.Random(20261113)
    def do(label,condition):
        if not condition:raise AssertionError(f'oracle disagreement: {label}')
        counts[label]=counts.get(label,0)+1
    for _ in range(400):
        a=[(rng.randint(-30,30),i) for i in range(rng.randint(0,35))]
        out=stable_mergesort(a,key=lambda a:a[0]);numpy_arr=np.array([t[0] for t in a])
        expected=[a[int(i)] for i in np.argsort(numpy_arr,kind='stable')]
        do('numpy_stable_mergesort',out==expected)
        vals=sorted(rng.randint(-50,50) for _ in range(rng.randint(0,60)))
        t=rng.randint(-52,52);do('numpy_searchsorted_left',lower_bound(vals,t)==int(np.searchsorted(vals,t,side='left')))
    for _ in range(420):
        n=rng.randint(2,12);g={str(i):{} for i in range(n)};nxx=nx.DiGraph();nxx.add_nodes_from(g)
        for u in g:
            for v in g:
                if u!=v and rng.random()<.22:
                    w=rng.randint(1,80);g[u][v]=w;nxx.add_edge(u,v,weight=w)
        ours=dijkstra(g,'0');expected=nx.single_source_dijkstra_path_length(nxx,'0')
        for v in g:do('networkx_dijkstra_node',ours['distances'][v]==expected.get(v,float('inf')))
        do('independent_distance_certificate',shortest_path_certificate(g,'0',ours))
    for _ in range(260):
        n=rng.randint(2,11);g={str(i):{} for i in range(n)};nxx=nx.DiGraph();nxx.add_nodes_from(g)
        for a in range(n):
            for b in range(a+1,n):
                if rng.random()<.35:
                    w=rng.randint(-10,12);g[str(a)][str(b)]=w;nxx.add_edge(str(a),str(b),weight=w)
        ours=bellman_ford(g,'0');expected=nx.single_source_bellman_ford_path_length(nxx,'0')
        do('bellman_dag_status',ours['status']=='finite_shortest_paths')
        for v in g:do('networkx_bellman_node',ours['distances'][v]==expected.get(v,float('inf')))
    for _ in range(350):
        n=rng.randint(0,9);weights=[rng.randint(0,15) for _ in range(n)];vals=[rng.randint(-20,30) for _ in range(n)];cap=rng.randint(0,32)
        ours=knapsack_01(weights,vals,cap)
        expected=max((sum(vals[i] for i in range(n) if mask>>i&1) for mask in range(1<<n) if sum(weights[i] for i in range(n) if mask>>i&1)<=cap),default=0)
        do('exhaustive_knapsack',ours['value']==expected)
        do('knapsack_witness_weight',sum(weights[i] for i in ours['indices'])<=cap)
        do('knapsack_witness_value',sum(vals[i] for i in ours['indices'])==ours['value'])
    for _ in range(320):
        root=rng.uniform(-2,2);offset=rng.uniform(.5,10);f=lambda x,r=root:x-r
        ours=bisection(f,root-offset,root+offset,continuous_confirmed=True,atol=1e-10)
        expected=scipy_bisect(f,root-offset,root+offset,xtol=1e-12)
        do('scipy_bisection_bracket',ours['interval'][0]-1e-12<=expected<=ours['interval'][1]+1e-12)
    for _ in range(300):
        a,b=sorted((rng.randint(-100,100),rng.randint(-100,100)));c,d=sorted((rng.randint(-100,100),rng.randint(-100,100)))
        ours=interval_mul((a,b),(c,d));arr=np.multiply.outer(np.array([a,b],dtype=np.int64),np.array([c,d],dtype=np.int64)).ravel()
        do('numpy_exact_small_interval_extrema',ours==(Fraction(int(arr.min())),Fraction(int(arr.max()))))
    for _ in range(400):
        a=rng.randint(-10**18,10**18);b=rng.randint(-10**18,10**18);g,x,y=extended_gcd(a,b)
        do('gcd_math_oracle',g==math.gcd(a,b));do('bezout_witness',a*x+b*y==g)
    for _ in range(300):
        values=np.asarray([rng.random() for i in range(rng.randint(1,14))]);values=values/values.sum()
        expected=float(-(values[values>0]*np.log2(values[values>0])).sum());ours=shannon_entropy(values.tolist())
        do('numpy_entropy',math.isclose(ours,expected,rel_tol=1e-12,abs_tol=1e-12))
    return {'schema':'computation.oracle/1','result':'passed','counts':counts,'comparisons':sum(counts.values()),'seed':20261113,'python':platform.python_version(),'numpy':np.__version__, 'scipy':__import__('scipy').__version__, 'networkx':nx.__version__, 'scope':'synthetic random graphs/numbers; independent implementations; no physical experiments, not mathematical universal proof','independent_scientific_peer_review':False,'live_ai_models_run':False}

if __name__=='__main__':
    v=check();print(json.dumps(v,indent=2));
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(json.dumps(v,indent=2)+'\n')
