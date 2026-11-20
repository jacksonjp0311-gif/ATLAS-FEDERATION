"""Independent numerical library comparison against NumPy/SciPy; mathematical only.

Do not mistake agreement in authored models for empirical control validation.
"""
from __future__ import annotations
import json,sys,random,math
from pathlib import Path
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root))
try:
 import numpy as np
 from scipy.linalg import solve_discrete_lyapunov
 from scipy.signal import TransferFunction, freqresp
 import scipy
except ImportError as e:
 print(json.dumps({'result':'not_run','reason':str(e)}));raise SystemExit(2)
from control_atlas.robust import (robust_scalar_feedback_interval,delay_one_sample_scalar,
  discrete_lyapunov_2x2,first_order_proportional_sensitivity,residual_lag1_diagnostic)
rng=random.Random(181126)
errors=[];counts={k:0 for k in ('interval_box','delay_roots','Lyapunov_Q','frequency_S_T','lag1_correlation')}
worst=0.0

def compare(which,a,b,tol=2e-10):
 global worst
 delta=abs(float(a)-float(b));scale=max(1,abs(float(a)),abs(float(b)))
 worst=max(worst,delta/scale);counts[which]+=1
 if delta>tol*scale:errors.append({'kind':which,'error':delta,'a':float(a),'b':float(b)})

for j in range(300):
 a0=rng.uniform(-1,1);a1=a0+rng.uniform(0.1,.8)
 b0=rng.uniform(-1,1);b1=b0+rng.uniform(.1,.8);K=rng.uniform(-2,2)
 x=robust_scalar_feedback_interval((a0,a1),(b0,b1),K)
 grid=np.array(np.meshgrid(np.linspace(a0,a1,19),np.linspace(b0,b1,19))).reshape(2,-1)
 compare('interval_box',x['worst_case_abs_pole'],np.max(np.abs(grid[0]-K*grid[1])))
for j in range(300):
 a=rng.uniform(-1.9,1.9);b=rng.uniform(-1.4,1.4);K=rng.uniform(-2,2)
 r=delay_one_sample_scalar(a,b,K)
 roots=np.roots([1,-a,b*K]);rho=max(abs(z) for z in roots)
 compare('delay_roots',r['one_sample_delay_spectral_radius'],rho)
for j in range(200):
 # Stable but potentially nonnormal 2x2; construct a positive definite P
 A=np.array([[rng.uniform(-.6,.6),rng.uniform(-.2,.2)],
             [rng.uniform(-.2,.2),rng.uniform(-.6,.6)]])
 if max(abs(z) for z in np.linalg.eigvals(A))>=.85:continue
 P=solve_discrete_lyapunov(A.T,np.eye(2))
 r=discrete_lyapunov_2x2(A.tolist(),P.tolist())
 if not r['numerically_positive_definite_P_and_Q']:errors.append({'kind':'Lyapunov_Q','error':'valid_p_candidate_not_detected'})
 Q=np.array(r['Q']);compare('Lyapunov_Q',np.linalg.norm(Q-np.eye(2),ord='fro'),0,2e-10)
for j in range(300):
 g=rng.uniform(.2,4);tau=rng.uniform(.02,15);K=rng.uniform(.1,3);w=rng.uniform(0,35)
 r=first_order_proportional_sensitivity(g,tau,K,w)
 _,Gc=freqresp(TransferFunction([g],[tau,1]),w=[w]);L=K*Gc[0];S=1/(1+L);T=L/(1+L)
 compare('frequency_S_T',r['sensitivity_magnitude'],abs(S))
 compare('frequency_S_T',r['complementary_sensitivity_magnitude'],abs(T))
for j in range(300):
 samples=np.array([rng.gauss(0,2) for _ in range(30)])
 m=samples-samples.mean();den=np.dot(m,m)
 expect=float(np.dot(m[:-1],m[1:])/den)
 r=residual_lag1_diagnostic(samples.tolist())
 compare('lag1_correlation',r['descriptive_lag1_correlation'],expect)
report={'schema':'atlas.control-robust-oracle/1','result':'passed' if not errors else 'failed',
 'seed':181126,'numpy':np.__version__,'scipy':scipy.__version__,
 'total_compared':sum(counts.values()),'per_method':counts,'maximum_scaled_absolute_error':worst,
 'errors':errors[:12],'source':'author_generated_models_not_observations',
 'independent_physical_validation':False,'hardware_actuation':False,'heldout_ai_evaluation':False}
print(json.dumps(report,indent=2));raise SystemExit(bool(errors))
