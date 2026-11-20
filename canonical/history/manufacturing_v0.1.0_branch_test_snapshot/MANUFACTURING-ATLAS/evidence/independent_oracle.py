"""Numerically independent NumPy checks for finite, authored manufacturing models.

No historical measured factory samples or source originals. Run from the MANUFACTURING-ATLAS root.
"""
from __future__ import annotations
import json,random,math
import numpy as np
from manufacturing_atlas import models as m

def run(seed=20261116):
 rnd=random.Random(seed);count={};max_err=0.0
 def check(k,a,b,tol=1e-9):
  nonlocal max_err
  diff=abs(float(a)-float(b));max_err=max(max_err,diff)
  if diff>tol*max(1,abs(float(b))):raise AssertionError((k,a,b,diff))
  count[k]=count.get(k,0)+1
 for i in range(500):
  hole=rnd.uniform(1,100); hw=rnd.uniform(0,.5);shaft=hole+rnd.uniform(-.4,.4);sw=rnd.uniform(0,.5)
  x=m.tolerance_fit(hole,hole+hw,shaft,shaft+sw)
  # Independent vector corners and extrema
  corners=np.subtract.outer(np.array([hole,hole+hw]),np.array([shaft,shaft+sw])).reshape(-1)
  check('fits_min',x['minimum_clearance_mm'],corners.min());check('fits_max',x['maximum_clearance_mm'],corners.max())
 for i in range(400):
  items=[(rnd.uniform(-3,0),rnd.uniform(0,3)) for _ in range(3)]
  a,b=m.interval_stackup(items)
  arr=np.array(items)
  check('interval_lower',a,arr[:,0].sum());check('interval_upper',b,arr[:,1].sum())
 for i in range(350):
  a=rnd.uniform(1e-3,10);cte=rnd.uniform(-3e-5,3e-5);dT=rnd.uniform(-70,70)
  v=m.thermal_length(a,cte,dT)
  check('thermal_length',v,np.multiply(a,np.add(1,np.multiply(cte,dT))))
 for i in range(300):
  D=rnd.uniform(2,40);vc=rnd.uniform(10,200);z=rnd.randint(2,6);fz=rnd.uniform(.005,.2);ap=rnd.uniform(.01,4);ae=rnd.uniform(.1,10);kc=rnd.uniform(400,2500);eta=rnd.uniform(.2,1)
  x=m.cutting_estimate(D,vc,z,fz,ap,ae,kc,eta)
  n=vc/(np.pi*(D/1000)); feed=n*z*fz;Q=feed*ap*ae
  for k,u in [('rpm',n),('feed_mm_min',feed),('mrr_mm3_min',Q),('cutting_W',kc*(Q/60.)*.001),('input_W_lower_bound',kc*(Q/60.)*.001/eta)]:check('cut_'+k,x[k],u)
 for i in range(400):
  F=rnd.uniform(-100,100);L=rnd.uniform(.01,2);E=rnd.uniform(1e8,3e11);I=rnd.uniform(1e-11,1e-6)
  check('beam',m.cantilever_deflection(F,L,E,I),np.divide(np.multiply(F,np.power(L,3)),np.multiply(3,np.multiply(E,I))))
 for i in range(300):
  x=np.array([rnd.uniform(-10,10) for _ in range(8)])
  if np.ptp(x)<.001:continue
  b=rnd.uniform(.1,10);a=rnd.uniform(-3,3);y=a+b*x+np.array([rnd.gauss(0,.005) for _ in x]);actual=m.linear_calibration(list(x),list(y))
  fit=np.linalg.lstsq(np.column_stack((x,np.ones(len(x)))),y,rcond=None)[0]
  check('calibration_gain',actual['gain'],fit[0]);check('calibration_offset',actual['offset'],fit[1])
 for i in range(200):
  A=np.array([[rnd.uniform(.1,4),0,0],[0,rnd.uniform(.1,4),0],[0,0,rnd.uniform(.1,4)]])
  U=np.array([rnd.uniform(-.5,.5) for _ in range(3)])
  C=A+np.outer(U,U)
  sd=np.sqrt(np.diag(C));x=m.covariance_stackup(list(sd),C.tolist());want=np.sqrt(np.ones(3)@C@np.ones(3))
  check('covariance',x,want)
 for i in range(300):
  samples=np.array([rnd.gauss(0,2) for _ in range(60)])
  check('roughness',m.roughness_ra(samples.tolist()),np.abs(samples-samples.mean()).mean())
 for i in range(400):
  init=rnd.uniform(280,340);ambient=rnd.uniform(275,325);power=rnd.uniform(-5,40);R=rnd.uniform(.1,10);C=rnd.uniform(1,50);t=rnd.uniform(0,300)
  y=m.first_order_thermal_state(init,ambient,power,R,C,t)
  # Separate matrix exponential of scalar linear ODE represented by eigendecomposition (0x0 excluded)
  steady=ambient+power*R
  expected=steady+np.exp(-t/(R*C))*(init-steady)
  check('thermal_response',y,expected)
 for i in range(500):
  y=rnd.uniform(-3,3);low=-1;high=1;unc=rnd.uniform(0,.2)
  result=m.guardband_verdict(y,low,high,unc)
  expect='accepted_under_declared_uncertainty' if y-unc>=low and y+unc<=high else ('rejected_under_declared_uncertainty' if y+unc<low or y-unc>high else 'indeterminate_measure_again')
  if result!=expect:raise AssertionError(('guardband',result,expect))
  count['guardband_decision']=count.get('guardband_decision',0)+1
 for i in range(300):
  # DAG with only edges from earlier to later nodes, independently enumerate all paths.
  nodes=['A','B','C','D','E'];ops={}
  for j,n in enumerate(nodes):ops[n]={'duration_min':rnd.randint(0,15),'requires':[k for k in nodes[:j] if rnd.random()<.35]}
  out=m.critical_path(ops);exp={}
  for n in nodes:exp[n]=ops[n]['duration_min']+max([exp[k] for k in ops[n]['requires']],default=0)
  check('routing_makespan',out['makespan_min'],max(exp.values()))
 for i in range(100):
  p=rnd.uniform(0,200);s=rnd.uniform(0,.1)
  if p==0:continue
  check('cast_shrink',m.cast_dimension_from_pattern(p,s),np.multiply(p,np.subtract(1,s)))
 if sum(count.values())<5000:raise AssertionError(('too few',sum(count.values())))
 return {'schema':'atlas.manufacturing-independent-oracle/1','result':'passed','seed':seed,'comparisons':sum(count.values()),'per_family':count,'max_absolute_difference':max_err,'numpy_version':np.__version__,'authentic_manufactured_samples':0,'independent_science_peer_review':False,'meaning':'Independent NumPy arithmetic and linear algebra implementations for finite authored cases; no physical equipment proof or certified process'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
