"""External NumPy/SciPy algorithm comparisons for synthetic control models only."""
from __future__ import annotations
import json,random,math,sys,itertools
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
try:
 import numpy as np
 from scipy.optimize import minimize
except ImportError as e:
 print(json.dumps({'result':'not_run','reason':str(e)}));raise SystemExit(3)
from control_atlas.advanced import (
 mimo_2x2_return_difference,common_lyapunov_box_2x2,finite_horizon_lqr_2state,
 scalar_grid_open_loop_plan,normalized_innovation_two_sensor,arx_training_validation_split)
rng=random.Random(61426)
checks={};worst=0.;examples=[]

def compare(label,got,want,atol=1e-9,rtol=1e-8):
 global worst
 g=float(got);w=float(want)
 d=abs(g-w);worst=max(worst,d/max(1,abs(w)))
 checks[label]=checks.get(label,0)+1
 if not math.isfinite(d) or d>atol+rtol*abs(w):raise AssertionError(f'{label}: {g} != {w} {d}')

# One-point real MIMO singular value and inverse comparisons against numpy.linalg.
for z in range(250):
 G=np.array([[rng.uniform(-2,2) for j in range(2)] for i in range(2)])
 K=np.array([[rng.uniform(-.5,.5) for j in range(2)] for i in range(2)])
 I=np.eye(2);mat=I+G@K
 if np.linalg.cond(mat)>1e8:continue
 r=mimo_2x2_return_difference(G.tolist(),K.tolist())
 SV=np.linalg.svd(mat,compute_uv=False)
 for a,b in zip(r['singular_values'],SV):compare('MIMO singular value',a,b)
 compare('MIMO condition',r['condition_number'],np.linalg.cond(mat))
 S=np.linalg.inv(mat)
 for i in range(2):
  for j in range(2):compare('MIMO S inverse',r['S'][i][j],S[i,j])

# Vertex matrix Gram eigenvalues compared with np.linalg.eigvalsh and sampled
# matrix convex combinations for certified P. Does not validate physical box.
for z in range(120):
 eps=.03
 core=np.array([[rng.uniform(.05,.65),rng.uniform(-.15,.15)],[rng.uniform(-.15,.15),rng.uniform(.05,.65)]])
 box=[[[float(core[i,j]-eps),float(core[i,j]+eps)] for j in range(2)] for i in range(2)]
 P=np.array([[1.,.1],[.1,1.5]])
 ours=common_lyapunov_box_2x2(box,P.tolist())
 for vertex in ours['vertex_evidence']:
  A=np.array(vertex['A']);Q=P-A.T@P@A
  compare('common P vertex min Q',vertex['minimum_Q_eigenvalue'],float(np.linalg.eigvalsh(Q)[0]))
  # The code reports failure to certify on P, not instability.
 if ours['common_P_strict_decay_numerically_certified']:
  vals=np.array([[[rng.uniform(*box[i][j]) for j in range(2)] for i in range(2)] for t in range(3)])
  for A in vals:
   Q=P-A.T@P@A
   if np.linalg.eigvalsh(Q)[0]<ours['worst_minimum_Q_eigenvalue']-1e-9:
    raise AssertionError('convex-box certificate failed at sampled interior point')

# Compare DP Riccati values/control with independent full-control optimizations.
for z in range(90):
 A=np.array([[rng.uniform(.45,.95),rng.uniform(-.5,.5)], [rng.uniform(-.4,.4),rng.uniform(.5,.98)]])
 B=np.array([rng.uniform(-1,1),rng.uniform(-1,1)])
 Q=np.diag([rng.uniform(.01,5),rng.uniform(.01,5)]);Qf=np.diag([rng.uniform(.01,5),rng.uniform(.01,5)])
 R=rng.uniform(.1,3);x=np.array([rng.uniform(-3,3),rng.uniform(-3,3)]);H=rng.randint(2,8)
 a=finite_horizon_lqr_2state(A.tolist(),B.tolist(),Q.tolist(),R,Qf.tolist(),H,x.tolist())
 def cost(u):
  s=x.copy();v=0.
  for act in u:
   v+=float(s@Q@s+R*act**2);s=A@s+B*act
  return v+float(s@Qf@s)
 result=minimize(cost,np.zeros(H),method='BFGS',options={'gtol':1e-6,'maxiter':300})
 compare('LQR cost from optimize',a['realized_quadratic_cost'],result.fun,atol=2e-6,rtol=1e-6)
 compare('LQR Riccati identity',a['Riccati_value_x0'],a['realized_quadratic_cost'],atol=3e-8,rtol=1e-8)

# Independently enumerate all sequences for a finite input grid; grid optimum
# has no claim to continuous-input optimality.
for z in range(140):
 A=rng.uniform(.1,1.5);B=rng.uniform(.2,1.5);x=rng.uniform(-1,1)
 H=rng.randint(1,4); grid=[-.6,0,.6];q=rng.uniform(0,5);R=rng.uniform(.05,3);qf=rng.uniform(0,4);xb=rng.uniform(1,3)
 ours=scalar_grid_open_loop_plan(A,B,x,H,grid,.6,xb,q,R,qf)
 vals=[]
 for u in itertools.product(grid,repeat=H):
  states=[x]
  if not all(abs(states[0])<=xb+1e-12 for x in [0]):raise AssertionError('bad sample')
  for act in u:states.append(A*states[-1]+B*act)
  if all(abs(s)<=xb+1e-12 for s in states):
   value=sum(q*states[i]**2+R*u[i]**2 for i in range(H))+qf*states[-1]**2
   vals.append(value)
 if vals:
  assert ours['status']=='feasible_grid_candidate'
  compare('grid minimum objective',ours['best']['grid_cost'],min(vals))
 else:assert ours['status']=='no_feasible_candidate_on_grid'

# NIS vs linalg.solve with SPD matrices.
for z in range(280):
 m=np.array([[rng.uniform(-2,2),rng.uniform(-2,2)] for i in range(2)])
 C=m.T@m+.05*np.eye(2);nu=np.array([rng.uniform(-3,3),rng.uniform(-3,3)])
 ours=normalized_innovation_two_sensor(nu.tolist(),C.tolist())
 compare('NIS solve',ours['NIS'],float(nu@np.linalg.solve(C,nu)),atol=2e-9,rtol=1e-8)

# ARX time split vs NumPy least-squares, with training and validation data.
for z in range(120):
 H=40;tr=27;a=rng.uniform(.1,.9);b=rng.uniform(.2,.8)
 inp=[rng.uniform(-2,2) for j in range(H)];states=[rng.uniform(-1,1)]
 for i,u in enumerate(inp):states.append((a if i<tr else a+rng.uniform(-.15,.15))*states[-1]+b*u)
 ours=arx_training_validation_split(states,inp,tr)
 X=np.array([[states[i],inp[i]] for i in range(tr)]);Y=np.array(states[1:tr+1])
 co=np.linalg.lstsq(X,Y,rcond=None)[0]
 compare('ARX a fit',ours['fitted_a'],co[0]);compare('ARX b fit',ours['fitted_b'],co[1])
 errors=np.array([states[t+1]-co[0]*states[t]-co[1]*inp[t] for t in range(tr,H)])
 compare('ARX later RMS',ours['later_one_step_RMS'],float(np.sqrt(np.mean(errors**2))))

out={'schema':'atlas.control-v04-independent-numeric-oracle/1','result':'passed',
 'source':'author_generated_models_not_physical_measurements',
 'seed':61426,'comparison_counts':checks,'total_comparisons':sum(checks.values()),
 'maximum_relative_to_one_scaled_error':worst,'numpy_version':np.__version__,
 'scipy_version':__import__('scipy').__version__,'independent_scientific_review':False,
 'hardware_actuated':False,'heldout_ai_evaluation':False}
print(json.dumps(out,indent=2))
