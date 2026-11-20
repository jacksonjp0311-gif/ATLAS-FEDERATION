"""Separate NumPy/NetworkX algorithms on constructed teaching problems.

Never refer to these author-generated cases as live agent data or independent
scientific review. NetworkX and NumPy are optional development dependencies.
"""
from __future__ import annotations
import json,random,sys,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
try:
 import numpy as np
 import networkx as nx
except ImportError:
 print(json.dumps({'status':'not_run','reason':'optional NumPy/NetworkX unavailable'}));raise SystemExit(2)
from agent_atlas.foundations_v1 import belief_update,finite_horizon_mdp,shortest_path_reference,offline_importance_value
rng=random.Random(20261113);checks=0;max_err=0.0;groups={}
def verify(category,a,b,tolerance=1e-9):
 global checks,max_err
 aa,bb=float(a),float(b)
 err=abs(aa-bb);max_err=max(max_err,err);checks+=1;groups[category]=groups.get(category,0)+1
 if err>tolerance*max(1,abs(aa),abs(bb)):raise AssertionError(f'{category}: got {a}, expected {b}')
# Independent matrix multiplication and normalization (different implementation)
for _ in range(220):
 prior=np.array([rng.random(),rng.random(),rng.random()],float);prior/=prior.sum()
 transition=np.array([[rng.random()+.1 for _ in range(3)] for i in range(3)],float)
 transition/=transition.sum(axis=1,keepdims=True)
 obs=np.array([[rng.random()+.1 for _ in range(2)] for i in range(3)],float)
 obs/=obs.sum(axis=1,keepdims=True)
 k=rng.randrange(2)
 local=belief_update(prior.tolist(),transition.tolist(),obs.tolist(),k)
 pred=prior@transition;w=pred*obs[:,k];p=w/w.sum()
 for j in range(3):verify('belief_posterior',local['posterior'][j],p[j])
 verify('observation_evidence',local['observation_probability'],w.sum())
# Independent linear algebra Bellman backup
for _ in range(220):
 n=3;a=2;steps=rng.randrange(1,7);gamma=rng.random()
 t=np.array([[[rng.random()+.1 for j in range(n)] for z in range(a)] for s in range(n)],float)
 t/=t.sum(axis=2,keepdims=True)
 rew=np.array([[[rng.uniform(-2,3) for j in range(n)] for z in range(a)] for s in range(n)],float)
 terminal=np.array([rng.uniform(-1,1) for i in range(n)])
 local=finite_horizon_mdp(t.tolist(),rew.tolist(),terminal.tolist(),steps,gamma)
 V=terminal.copy()
 for i in range(steps):V=np.max(np.sum(t*(rew+gamma*V[None,None,:]),axis=2),axis=1)
 for j in range(n):verify('bellman_values',local['start_values'][j],V[j])
# NetworkX independent shortest-path solver on directed weighted graph
for _ in range(200):
 n=7;nodes=[str(i) for i in range(n)]
 g={s:{} for s in nodes};G=nx.DiGraph();G.add_nodes_from(nodes)
 for i in range(n):
  for j in range(n):
   if j!=i and rng.random()<.3:
    w=rng.randint(1,10);g[str(i)][str(j)]=w;G.add_edge(str(i),str(j),weight=w)
 try:expected=nx.shortest_path_length(G,'0','6',weight='weight')
 except nx.NetworkXNoPath:expected=None
 local=shortest_path_reference(g,'0','6')
 verify('dijkstra_networkx',(local['dijkstra_witness']['cost'] if expected is not None else -1),expected if expected is not None else -1)
# IPS and ESS independent vector arithmetic with NumPy
for _ in range(200):
 n=12;rows=[];arr=[]
 for k in range(n):
  p=.2+.7*rng.random();selected=rng.random()<p;reward=1 if rng.random()<.6 else 0
  rows.append({'logged_action':'A' if selected else 'B','target_action':'A','logging_probability':p,'reward':reward})
  arr.append((1/p if selected else 0,reward))
 if not any(w for w,y in arr):continue
 local=offline_importance_value(rows,max_weight=100)
 W=np.array([x[0] for x in arr]);Y=np.array([x[1] for x in arr])
 verify('ips_mean',local['ips_mean'],np.mean(W*Y))
 verify('weighted_ess',local['effective_sample_size'],W.sum()**2/(W@W))
 verify('ips_self_normalized',local['self_normalized_ratio'],(W@Y)/W.sum())
report={'schema':'atlas.agent-v1-numerical-oracle/1','status':'passed','comparisons':checks,'by_algorithm':groups,
        'max_abs_error':max_err,'seed':20261113,'numpy_version':np.__version__,'networkx_version':nx.__version__,
        'authored_synthetic_only':True,'independent_human_scientific_review':False,
        'measured_agent_performance':False,'scientific_reliability_claim':'none'}
p=Path(__file__).resolve().parents[1]/'evidence/v1_numeric_oracle.json';p.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
