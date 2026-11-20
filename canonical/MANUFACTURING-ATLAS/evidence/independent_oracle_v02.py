"""Independently assembled manufactured/synthetic mathematical oracles.

NumPy/SciPy are used only in this audit, not by manufacturing reference models.
No laboratory data, original publisher bytes, or expert verification is claimed.
"""
import numpy as np
from scipy.stats import norm
from pathlib import Path
import math,random,json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from manufacturing_atlas.v02_models import (covariance_budget_psd,wilson_yield_interval,
 normal_inspection_acceptance_risk,stable_process_capability,resource_bounded_schedule,
 datum_rigid_transform_xy,traceability_chain_audit,manufacturing_evidence_gate)


def run(seed=20261116):
 rng=random.Random(seed)
 counts={};max_diffs={}
 def check(k,a,b,tol=1e-10):
  if isinstance(a,(float,int)) and isinstance(b,(float,int)):
   if not math.isfinite(a) or not math.isfinite(b):raise AssertionError('nonfinite '+k)
   err=abs(a-b);max_diffs[k]=max(max_diffs.get(k,0.),err)
   if err > tol*max(1.,abs(a),abs(b)):raise AssertionError((k,a,b,err))
  elif a!=b:raise AssertionError((k,a,b))
  counts[k]=counts.get(k,0)+1
 # Independent PSD via numpy.linalg.eigvalsh + direct quadratic form.
 for _ in range(320):
  n=rng.randint(1,8)
  A=np.array([[rng.uniform(-2,2) for j in range(n)] for i in range(n)],dtype=float)
  mat=A.T@A;coe=np.array([rng.uniform(-2,2) for i in range(n)])
  got=covariance_budget_psd(mat.tolist(),coe.tolist())
  want=np.sqrt(max(0.,float(coe@mat@coe)))
  check('covariance_quadratic_form',got['standard_uncertainty'],want,3e-9)
  if got['minimum_covariance_eigenvalue'] < -2e-8*max(1,float(abs(mat).max())):
   raise AssertionError('bad PSD eigenvalue')
 for _ in range(80):
  s=rng.uniform(.1,5)
  mat=[[s,.9*s,.9*s],[.9*s,s,-.9*s],[.9*s,-.9*s,s]]
  assert min(np.linalg.eigvalsh(mat)) < -0.1*s
  try:covariance_budget_psd(mat)
  except ValueError:counts['nonPSD_refusals']=counts.get('nonPSD_refusals',0)+1
  else:raise AssertionError('non-PSD accepted')
 z=float(norm.ppf(.975))
 for _ in range(550):
  n=rng.randint(1,1000);success=rng.randrange(n+1)
  got=wilson_yield_interval(success,n)
  p=success/n
  cen=(p+z*z/(2*n))/(1+z*z/n)
  half=z/(1+z*z/n)*math.sqrt(p*(1-p)/n+z*z/(4*n*n))
  check('wilson_lower',got['lower'],max(0.,cen-half),1e-12)
  check('wilson_upper',got['upper'],min(1.,cen+half),1e-12)
 for _ in range(450):
  value=rng.uniform(-5,5);sig=rng.uniform(.1,2)
  lsl=rng.uniform(-5,-1);usl=rng.uniform(1,5);guard=rng.uniform(0,(usl-lsl)/2)
  got=normal_inspection_acceptance_risk(value,sig,lsl,usl,guard)
  want=float(norm.cdf((usl-guard-value)/sig)-norm.cdf((lsl+guard-value)/sig))
  check('normal_acceptance_risk',got['accept_given_true_value_probability'],max(0.,want),1e-12)
 for _ in range(330):
  n=rng.randint(8,90);v=[rng.gauss(.05,.4) for i in range(n)]
  lo=-1.;hi=1.
  got=stable_process_capability(v,lo,hi,True,True)
  check('conditional_capability_cp',got['cp'],(hi-lo)/(6*np.std(v,ddof=1)),1e-12)
  check('conditional_capability_cpk',got['cpk'],min(hi-np.mean(v),np.mean(v)-lo)/(3*np.std(v,ddof=1)),1e-12)
  hold=stable_process_capability(v,lo,hi,False,True)
  check('capability_HOLD_without_stability_evidence',hold['cp'],None)
 for _ in range(310):
  n=rng.randint(1,9)
  ops={}
  for i in range(n):
   ops[f'op{i}']={'duration_min':rng.uniform(.01,10),'resource':f'bay{rng.randrange(3)}',
                 'depends_on':[f'op{j}' for j in range(i) if rng.random()<.15]}
  r=resource_bounded_schedule(ops)
  for ident,record in r['schedule'].items():
   for dep in ops[ident]['depends_on']:
    if record['start_min'] < r['schedule'][dep]['end_min']-1e-12:raise AssertionError('precedence violation')
   for other,q in r['schedule'].items():
    if ident>=other or record['resource']!=q['resource']:continue
    if max(record['start_min'],q['start_min']) < min(record['end_min'],q['end_min'])-1e-12:
     raise AssertionError('resource overlap')
   counts['independent_schedule_constraints']=counts.get('independent_schedule_constraints',0)+1
 for _ in range(540):
  theta=rng.uniform(-math.pi,math.pi);x,y=rng.uniform(-100,100),rng.uniform(-100,100)
  tx,ty=rng.uniform(-100,100),rng.uniform(-100,100);scale=rng.uniform(.1,10)
  rot=np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])
  want=scale*(rot@np.array([x,y]))+np.array([tx,ty])
  got=datum_rigid_transform_xy((x,y),(tx,ty),theta,scale)
  check('datum_transform_x',got[0],float(want[0]),1e-12)
  check('datum_transform_y',got[1],float(want[1]),1e-12)
 for _ in range(150):
  sha='a'*64
  chain={'tool':{'parent':'lab','unit':'mm','standard_uncertainty':.01,'valid_through':20271231,'sha256':sha},
         'lab':{'parent':None,'unit':'mm','standard_uncertainty':.001,'valid_through':20271231,'sha256':sha}}
  result=traceability_chain_audit(chain,'tool',20261116)
  check('declared_traceability_still_NOT_authenticated',result['original_source_bytes_authenticated'],False)
  assert result['status']=='documentation_present_not_source_authenticated'
 for _ in range(150):
  nodes={'process':{'depends_on':[],'inputs':['stock'],'outputs':['part'],'required_evidence':['inspection']}}
  a=manufacturing_evidence_gate(nodes,['stock'],{})
  assert not a['structurally_complete']
  b=manufacturing_evidence_gate(nodes,['stock'],{'inspection':'synthetic-metadata'})
  assert b['structurally_complete'] and not b['independently_certified']
  counts['evidence_gate_fail_closed_and_noncertification']=counts.get('evidence_gate_fail_closed_and_noncertification',0)+2
 return {'schema':'atlas.manufacturing-v02-independent-oracle/1','result':'passed','seed':seed,
         'independent_numeric_and_logical_comparisons':sum(counts.values()),'groups':counts,
         'max_absolute_errors_by_group':max_diffs,'numpy':np.__version__,
         'scipy':'1.17.0','physical_parts_manufactured':0,
         'calibration_authenticity_proved':False,'independent_expert_review':False}

if __name__=='__main__':
 result=run()
 print(json.dumps(result,indent=2))
 if len(sys.argv)>1:Path(sys.argv[1]).write_text(json.dumps(result,indent=2)+'\n')
