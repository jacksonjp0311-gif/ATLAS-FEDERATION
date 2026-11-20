"""NumPy/SciPy comparator for generated control models (not real equipment data)."""
import json,sys,random,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
try:
 import numpy as np
 from scipy import signal,linalg
except ImportError as exc:
 print(json.dumps({'result':'not_run','reason':str(exc),'runtime_independent':False}));raise SystemExit(3)
from control_atlas.methods import (zoh_first_order,eigenvalues_2x2,rank_two_state,scalar_lqr,fit_scalar_arx,
   scalar_kalman_update,alias_frequency,simulate_zoh_first_order)
rng=random.Random(261112);errors=[];counts={}
def compare(k,got,want,atol=1e-9,rtol=1e-9):
 counts[k]=counts.get(k,0)+1
 if not math.isfinite(float(got)) or abs(got-want)>atol+rtol*abs(want):errors.append({'kind':k,'ours':got,'independent':float(want)})
for _ in range(130):
 gain=rng.uniform(-5,5);tau=rng.uniform(.25,20);dt=rng.uniform(.01,2)
 ours=zoh_first_order(gain,tau,dt)
 A=np.array([[-1/tau]]);B=np.array([[gain/tau]]);C=np.array([[1.]]);D=np.zeros((1,1))
 Ad,Bd,_,_,_=signal.cont2discrete((A,B,C,D),dt,method='zoh')
 compare('zoh_a',ours['a'],Ad[0,0]);compare('zoh_b',ours['b'],Bd[0,0])
 for j in range(5):
  u=[rng.uniform(-2,2) for _ in range(9)]
  v=simulate_zoh_first_order(gain,tau,dt,u,y0=.4)['states']
  e=.4
  for k,entry in enumerate(u):
   e=float(Ad[0,0])*e+float(Bd[0,0])*entry
   compare('zoh_trajectory',v[k+1],e,atol=1e-10)
for _ in range(120):
 A=np.array([[rng.uniform(-.9,.9),rng.uniform(-1,1)],[rng.uniform(-1,1),rng.uniform(-.9,.9)]])
 out=eigenvalues_2x2(A.tolist());compare('two_state_rho',out['spectral_radius'],max(abs(z) for z in np.linalg.eigvals(A)))
 B=np.array([rng.uniform(-1,1),rng.uniform(-1,1)]);C=np.array([rng.uniform(-1,1),rng.uniform(-1,1)])
 test=rank_two_state(A.tolist(),B.tolist(),C.tolist(),relative_determinant_cutoff=1e-12)
 W=np.column_stack([B,A@B]);O=np.stack([C,C@A])
 compare('reachability_det',test['controllability_determinant'],np.linalg.det(W))
 compare('observability_det',test['observability_determinant'],np.linalg.det(O))
for _ in range(120):
 A=rng.uniform(-1.5,1.5);B=rng.uniform(.1,2);Q=rng.uniform(.01,10);RR=rng.uniform(.01,10)
 ours=scalar_lqr(A,B,Q,RR)
 P=linalg.solve_discrete_are(np.array([[A]]),np.array([[B]]),np.array([[Q]]),np.array([[RR]]) )[0,0]
 k=(B*P*A)/(RR+B*B*P)
 compare('lqr_P',ours['P'],P,atol=1e-8,rtol=1e-8);compare('lqr_K',ours['feedback_gain'],k,atol=1e-8,rtol=1e-8)
for _ in range(120):
 a=rng.uniform(-2,2);mu=rng.uniform(-10,10);p=rng.uniform(0,3);q=rng.uniform(0,2);r=rng.uniform(.01,3);y=rng.uniform(-10,10)
 ours=scalar_kalman_update(a,mu,p,q,r,y);prior=a*a*p+q;gain=prior/(prior+r)
 compare('kalman_mean',ours['posterior_mean'],a*mu+gain*(y-a*mu))
 compare('kalman_var',ours['posterior_variance'],(1-gain)*prior)
for _ in range(120):
 n=30;A=rng.uniform(-.8,.9);B=rng.uniform(.1,.7);u=[rng.uniform(-3,3) for _ in range(n)];x=[.3]
 for uu in u:x.append(A*x[-1]+B*uu)
 ours=fit_scalar_arx(x,u)
 X=np.column_stack([x[:-1],u]);coeff=np.linalg.lstsq(X,x[1:],rcond=None)[0]
 compare('id_a',ours['a_hat'],coeff[0]);compare('id_b',ours['b_hat'],coeff[1])
for _ in range(90):
 fs=100;f=rng.randint(1,400)
 result=alias_frequency(f,fs)
 x=np.cos(2*np.pi*f*np.arange(100)/fs)
 spectrum=np.abs(np.fft.rfft(x));fpeak=int(np.argmax(spectrum))
 compare('alias_fft_bin',result['aliased_frequency_hz'],fpeak,atol=1e-8,rtol=0)
report={'schema':'atlas.control-oracle/1','result':'passed' if not errors else 'failed','counts':counts,'total':sum(counts.values()),
        'errors':errors[:10],'random_seed':261112,'numpy_version':np.__version__,'scipy_version':__import__('scipy').__version__,
        'synthetic_only':True,'physical_system_identified':False,'independent_scientific_review':False,
        'no_real_actuation':True}
print(json.dumps(report,indent=2));raise SystemExit(bool(errors))
