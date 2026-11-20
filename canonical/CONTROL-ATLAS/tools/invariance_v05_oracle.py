"""Optional independent NumPy vertex/state-box enumeration for Control v0.5.

An algorithmic oracle on seeded synthetic models; no physical plant data or
independent scientific review. Never sends hardware commands.
"""
from __future__ import annotations
import json,random,itertools,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
try:
 import numpy as np
except ImportError:
 print(json.dumps({'result':'not_run','reason':'NumPy optional dependency missing'}));raise SystemExit(3)
from control_atlas.invariance import robust_invariant_box_2x2,scalar_robust_interval,simulate_2x2_state_feedback
rng=random.Random(20261113);comparisons=0;worst_error=0.0;count={'vertex_bound':0,'scalar':0,'simulation':0}
def check(a,b,kind):
 global comparisons,worst_error
 err=abs(float(a)-float(b));worst_error=max(worst_error,err);comparisons+=1;count[kind]+=1
 if err>2e-11*max(1,abs(float(a)),abs(float(b))):raise AssertionError((kind,a,b,err))
for _ in range(120):
 a=[[(rng.uniform(-.8,.1),rng.uniform(.1,.8)),(-.1,.1)],[(-.2,.1),(.1,.5)]]
 b=[(.3,.5),(.1,.2)];k=[rng.uniform(-.7,.7),rng.uniform(-.7,.7)]
 r=[rng.uniform(.2,3),rng.uniform(.2,3)];w=[rng.uniform(0,.3),rng.uniform(0,.3)]
 v=robust_invariant_box_2x2(A_intervals=a,B_intervals=b,state_feedback_K=k,state_radii=r,disturbance_radii=w,actuator_limit=2,full_state_available=True)
 peak=np.array([0.,0.])
 for bits in itertools.product([0,1],repeat=6):
  arr=np.array([[a[0][0][bits[0]],a[0][1][bits[1]]],[a[1][0][bits[2]],a[1][1][bits[3]]]],dtype=float)
  bv=np.array([b[0][bits[4]],b[1][bits[5]]],dtype=float)
  F=arr-np.outer(bv,np.array(k))
  for signs in itertools.product((-1,1),repeat=2):
   nxt=np.abs(F@np.array([signs[0]*r[0],signs[1]*r[1]]))+np.array(w)
   peak=np.maximum(peak,nxt)
 for j in (0,1):check(v['max_successor_abs_bound'][j],peak[j],'vertex_bound')
 g=rng.uniform(-1.5,1.5);r0=rng.uniform(.1,2);d0=rng.uniform(0,.4)
 v=scalar_robust_interval(closed_loop_gain=g,state_radius=r0,
                          disturbance_radius=d0,input_gain=.2,input_limit=.3,state_feedback_exact=True)
 # Direct independent enumeration of both state and disturbance extrema.
 ref=max(abs(g*x+z) for x in (-r0,r0) for z in (-d0,d0))
 check(v['worst_one_step_abs_state'],ref,'scalar')
 for _ in range(2):
  A=np.array([[.5,.1],[0,.7]])
  B=np.array([.3,.1]);K=np.array([.2,.2]);x0=np.array([rng.uniform(-1,1),rng.uniform(-1,1)])
  ds=[np.array([rng.uniform(-.1,.1),rng.uniform(-.1,.1)]) for _ in range(10)]
  sim=simulate_2x2_state_feedback(A=A.tolist(),B=B.tolist(),K=K.tolist(),x0=x0.tolist(),disturbances=[x.tolist() for x in ds],input_limit=.5)
  x=x0.copy()
  for i,wv in enumerate(ds):
   u=float(np.clip(-K@x,-.5,.5));x=A@x+B*u+wv
   for j in (0,1):check(sim['states'][i+1][j],x[j],'simulation')
result={'schema':'atlas.control-invariance-oracle/1','result':'passed','seed':20261113,
 'comparisons':comparisons,'per_method':count,'max_abs_error':worst_error,
 'numpy_version':np.__version__,'declared_tolerance_scaled':2e-11,
 'data_origin':'authored_seeded_synthetic_only','physical_plant_evidence':False,
 'independent_human_science_review':False,'no_actuation':True}
print(json.dumps(result,indent=2))
