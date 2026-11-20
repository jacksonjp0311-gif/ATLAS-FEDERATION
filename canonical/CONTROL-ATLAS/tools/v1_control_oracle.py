"""NumPy crosscheck of bounded multivariable observer, ARX and holdout metrics.

The oracle uses independent arrays and np.linalg.lstsq. This validates code
and simulated numeric cases only, not measured noise bounds or plant safety.
"""
import json,random,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from control_atlas.multivariable import two_by_two_observer_error_tube,two_sensor_consistency
from control_atlas.empirical import parse_openmct,validate_openmct_identification,COLUMNS
rng=random.Random(61113)
maxerr=0;count=0
for _ in range(450):
 A=np.array([[rng.uniform(-.3,.8) for j in range(2)] for i in range(2)])
 C=np.array([[rng.uniform(-.5,1) for j in range(2)] for i in range(2)])
 L=np.array([[rng.uniform(-.3,.6) for j in range(2)] for i in range(2)])
 e0=np.array([rng.random()/3 for i in range(2)]);W=np.array([rng.random()/20 for i in range(2)]);V=np.array([rng.random()/15 for i in range(2)])
 v=two_by_two_observer_error_tube(A=A.tolist(),C=C.tolist(),L=L.tolist(),initial_error_radii=e0.tolist(),process_error_radii=W.tolist(),measurement_error_radii=V.tolist(),steps=12)
 F=A-L@C;absF=np.abs(F);forcing=W+np.abs(L)@V
 e=e0.copy()
 for k in range(13):
  diff=max(abs(e-np.array(v['error_radii'][k])));maxerr=max(maxerr,float(diff));count+=2
  if diff>1e-11:raise AssertionError(f'observer recurrence mismatch {diff}')
  e=absF@e+forcing
 for k in range(8):
  h=np.array([rng.gauss(0,1) for i in range(2)]);E=np.array([rng.random()/4 for i in range(2)]);noise=np.array([rng.random()/5 for i in range(2)]);y=C@h+np.array([rng.gauss(0,.1) for i in range(2)])
  result=two_sensor_consistency(estimate=h.tolist(),estimated_error_radii=E.tolist(),C=C.tolist(),sensor_values=y.tolist(),measurement_error_radii=noise.tolist())
  expected=[(C@h)[i]-sum(abs(C[i,j])*E[j] for j in range(2))-noise[i] <= y[i] <= (C@h)[i]+sum(abs(C[i,j])*E[j] for j in range(2))+noise[i] for i in range(2)]
  if result['sensor_level_compatibility']!=expected:raise AssertionError('sensor comparison mismatch')
  count+=2
# Different randomized author generator than tests. ARX training/holdout must agree with independent least-squares.
for m in range(120):
 speed=rng.uniform(10,100);rows=[];N=130
 for k in range(N):
  u=(55 if k//5%2 else 220);y=speed
  rows.append([100,y,20,500,510,u,'nan','nan','nan','nan'])
  speed=.7*speed+.26*u+4+rng.gauss(0,1)
 raw='Mode, System Identification\nDate, 2026-10-13\n'+','.join(COLUMNS)+'\n'+'\n'.join(','.join(str(v) for v in row) for row in rows)
 parsed=parse_openmct(raw);r=validate_openmct_identification(parsed)
 nn=r['training_transitions'];p=np.asarray([row['MEAS'] for row in parsed['samples']]);u=np.asarray([row['PWM'] for row in parsed['samples']]);
 X=np.column_stack([p[:nn],u[:nn],np.ones(nn)]);y=p[1:nn+1]
 coef=np.linalg.lstsq(X,y,rcond=None)[0];actual=np.array([r['model'][x] for x in ('a','b','c')]);diff=max(abs(coef-actual));maxerr=max(maxerr,float(diff))
 if diff>1e-8:raise AssertionError(f'ARX coefficient mismatch {diff}')
 baseline=p[nn:N-1];target=p[nn+1:N];yhat=coef[0]*baseline+coef[1]*u[nn:N-1]+coef[2]
 error=np.sqrt(np.mean((target-yhat)**2));reported=r['performance']['heldout_one_step_rmse_rpm']
 if abs(error-reported)>1e-8:raise AssertionError('ARX holdout mismatch')
 count+=4
report={'schema':'atlas.control-v1-oracle/1','result':'passed','comparisons':count,'numpy_version':np.__version__,
  'seed':61113,'max_abs_error':maxerr,'controls':{'observer_random_systems':450,'heldout_arx_random_systems':120},
  'empirical_publisher_data_evaluated':False,'source_data_authenticity_verified':False,
  'physical_control_or_safety_tested':False,'interpretation':'independently coded NumPy numeric oracles for synthetic models only'}
print(json.dumps(report,indent=2))
