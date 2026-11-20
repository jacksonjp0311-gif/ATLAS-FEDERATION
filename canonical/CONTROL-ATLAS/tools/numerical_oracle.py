"""Optional independent numerical comparison, not physical control verification."""
import sys,json,random,math,platform
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from scipy.signal import cont2discrete
from scipy.optimize import minimize
from control_atlas.models import zoh_first_order,state_rank_2x2,scalar_finite_lqr,first_order_response,scalar_kalman
rng=random.Random(6101126)
counts={'zoh_via_matrix_exponential':0,'two_state_matrix_rank':0,'scalar_lqr_via_scipy_optimizer':0,'scalar_kalman_via_separate_recursion':0}
maxerr=0.
def verify(category,a,b,tol=3e-8):
 global maxerr
 delta=abs(float(a)-float(b));scale=max(1,abs(float(b)))
 maxerr=max(maxerr,delta/scale)
 if delta>tol*scale:raise AssertionError((category,a,b))
 counts[category]+=1
for i in range(150):
 gain=rng.uniform(.01,5);tau=rng.uniform(.2,15);dt=rng.uniform(.01,1.5)
 got=zoh_first_order(gain=gain,tau_s=tau,sample_s=dt)
 A,B,C,D,delay=cont2discrete((np.array([[-1/tau]]),np.array([[gain/tau]]),np.array([[1.]]),np.array([[0.]])),dt,method='zoh')
 verify('zoh_via_matrix_exponential',got['a'],A[0,0]);verify('zoh_via_matrix_exponential',got['b'],B[0,0])
for i in range(150):
 A=np.array([[rng.uniform(-2,2),rng.uniform(-2,2)],[rng.uniform(-2,2),rng.uniform(-2,2)]])
 B=np.array([rng.uniform(-2,2),rng.uniform(-2,2)])
 C=np.array([rng.uniform(-2,2),rng.uniform(-2,2)])
 g=state_rank_2x2(A=A.tolist(),B=B.tolist(),C=C.tolist(),tol=1e-9)
 cont=np.column_stack((B,A@B));obs=np.vstack((C,C@A))
 if min(abs(np.linalg.det(cont)),abs(np.linalg.det(obs)))<1e-5:continue
 verify('two_state_matrix_rank',float(g['controllable_at_absolute_det_tol']),float(np.linalg.matrix_rank(cont)==2),tol=0)
 verify('two_state_matrix_rank',float(g['observable_at_absolute_det_tol']),float(np.linalg.matrix_rank(obs)==2),tol=0)
for i in range(80):
 a=rng.uniform(.4,1.4);b=rng.uniform(.5,2);q=rng.uniform(.1,3);r=rng.uniform(.05,1.5);qf=rng.uniform(.1,2);x0=rng.uniform(-2,2);n=4
 got=scalar_finite_lqr(a=a,b=b,q=q,r=r,terminal_q=qf,horizon=n,x0=x0)
 def objective(u):
  x=x0;cost=0
  for j in range(n):cost+=q*x*x+r*u[j]*u[j];x=a*x+b*u[j]
  return cost+qf*x*x
 # independent convex quadratic optimizer with a known minimum but no use of Riccati.
 fit=minimize(objective,np.zeros(n),method='BFGS',options={'gtol':1e-10,'maxiter':300})
 verify('scalar_lqr_via_scipy_optimizer',got['optimal_cost'],fit.fun,tol=2e-6)
for i in range(100):
 a=rng.uniform(.7,1.2);c=rng.uniform(.7,1.5);q=rng.uniform(.001,.1);r=rng.uniform(.01,.5)
 p=rng.uniform(.1,2);x=rng.uniform(-1,1);readings=[rng.uniform(-1,1) for _ in range(8)]
 got=scalar_kalman(a=a,c=c,process_variance=q,measurement_variance=r,initial_estimate=x,initial_variance=p,measurements=readings)
 for y in readings:
  x_pred=a*x;p_pred=a*a*p+q
  k=p_pred*c/(c*c*p_pred+r)
  x=x_pred+k*(y-c*x_pred);p=p_pred-k*c*p_pred
 verify('scalar_kalman_via_separate_recursion',got['final_estimate'],x)
 verify('scalar_kalman_via_separate_recursion',got['final_variance'],p)
out={'schema':'atlas.control-numerical-oracle/1','status':'passed','seed':6101126,'method_counts':counts,'comparisons':sum(counts.values()),
 'maximum_scaled_absolute_error':maxerr,'numpy_version':np.__version__,'scipy_version':__import__('scipy').__version__,
 'validation':'separate numerical algorithms on synthetic parameters, not independent scientific review, physical experiment, or real agent behavior'}
print(json.dumps(out,indent=2))
