"""Independent numerical algorithms validating authored Computation 0.2 fixtures.

NetworkX, NumPy, SciPy are development oracles, not live scientific evidence.
"""
from __future__ import annotations
import json,math,random
import numpy as np
import networkx as nx
from scipy.linalg import solve as scipy_solve
from pathlib import Path
from computation_atlas.advanced_v02 import (kruskal_forest,max_flow_min_cut,gaussian_solve_exact,
     fft_radix2,convolution_linear,hoeffding_interval,vector_clock_relation)
from fractions import Fraction
SEED=20261114;rng=random.Random(SEED);counts={};error=0.0

def check(label,actual,expected,tolerance=1e-9):
 global error
 if actual is None and expected is None:pass
 else:
  diff=abs(float(actual)-float(expected));error=max(diff,error)
  if not math.isfinite(diff) or diff>tolerance*max(1.0,abs(float(expected))):raise AssertionError(f'{label}: {actual} != {expected}')
 counts[label]=counts.get(label,0)+1
for _ in range(250):
 n=rng.randint(2,14);edges=[];G=nx.Graph();G.add_nodes_from(range(n))
 for u in range(n):
  for v in range(u+1,n):
   if rng.random()<.4:
    w=rng.randint(-5,20);edges.append((u,v,w));G.add_edge(u,v,weight=w)
 forest=kruskal_forest(n,edges)
 expected=nx.minimum_spanning_tree(G,weight='weight',algorithm='kruskal')
 check('networkx_mst_weight',forest['total_cost'],sum(dat['weight'] for _,_,dat in expected.edges(data=True)))
 check('networkx_mst_component_count',forest['components'],nx.number_connected_components(G))
for _ in range(220):
 n=rng.randint(2,10);edges=[];G=nx.DiGraph();G.add_nodes_from(range(n))
 for u in range(n):
  for v in range(n):
   if u!=v and rng.random()<.3:
    cap=rng.randint(0,20);edges.append((u,v,cap));G.add_edge(u,v,capacity=cap)
 r=max_flow_min_cut(n,edges,0,n-1)
 ans=nx.maximum_flow_value(G,0,n-1,capacity='capacity')
 check('networkx_max_flow',r['max_flow'],ans)
 check('flow_cut_duality',r['max_flow'],r['min_cut_capacity'])
for _ in range(260):
 n=rng.randint(1,6);xx=np.array([rng.randint(-5,5) for i in range(n)],dtype=float)
 A=np.array([[rng.randint(-9,9) for j in range(n)] for i in range(n)],dtype=float)
 if abs(np.linalg.det(A))<.5:continue
 b=A@xx
 got=gaussian_solve_exact(A.astype(int).tolist(),b.astype(int).tolist())
 solu=np.array([float(Fraction(x)) for x in got['solution']]);oracle=scipy_solve(A,b)
 for x,y in zip(solu,oracle):check('scipy_gauss_elimination',x,y,1e-7)
for _ in range(250):
 n=2**rng.randint(0,8)
 seq=np.array([complex(rng.randint(-5,5),rng.randint(-5,5)) for j in range(n)])
 ref=np.fft.fft(seq);got=fft_radix2(seq.tolist())
 for x,y in zip(got,ref):check('numpy_fft_real',x.real,y.real,1e-8);check('numpy_fft_imag',x.imag,y.imag,1e-8)
 inv=fft_radix2(got,inverse=True)
 for x,y in zip(inv,seq):check('fft_round_trip',abs(x-y),0,1e-8)
for _ in range(250):
 na=rng.randint(1,80);nb=rng.randint(1,70)
 a=np.array([rng.randint(-5,5) for _ in range(na)],float);b=np.array([rng.randint(-5,5) for _ in range(nb)],float)
 reference=np.convolve(a,b);got=convolution_linear(a.tolist(),b.tolist())
 for x,y in zip(got,reference):check('numpy_convolution_real',x.real,y,1e-7);check('numpy_convolution_imag',x.imag,0,1e-7)
for _ in range(250):
 n=rng.randint(1,200);s=np.array([rng.random() for i in range(n)]);delta=.05
 r=hoeffding_interval(s.tolist(),delta)
 check('hoeffding_rho',r['unclipped_half_width'],math.sqrt(math.log(2/delta)/(2*n)))
 check('numpy_sample_mean',r['mean'],float(np.mean(s)))
for _ in range(200):
 n=rng.randint(1,9);a=[rng.randint(0,20) for _ in range(n)];b=[rng.randint(0,20) for _ in range(n)]
 expected='equal' if a==b else 'happened_before' if all(x<=y for x,y in zip(a,b)) else 'happened_after' if all(x>=y for x,y in zip(a,b)) else 'concurrent'
 check('clock_relation',int(vector_clock_relation(a,b)==expected),1)
result={'schema':'atlas.computation-v02-oracle/1','status':'passed','seed':SEED,'comparisons':sum(counts.values()),'categories':counts,'max_absolute_deviation':error,
        'numpy_version':np.__version__,'networkx_version':nx.__version__,'scipy_available':True,
        'data_origin':'author_generated_synthetic_inputs','physical_science_review':False,'unseen_ai_model_performance':False,
        'limitations':['Numerical agreement under generated samples does not prove universal correctness',
                       'Adversarial, extreme precision, and nonnumeric performance questions require additional study']}
p=Path(__file__).resolve().parents[1]/'evidence/numerical_oracle_v0.2.0.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
