"""Independent authored SciPy root+NumPy reference oracle (optional dependencies).

Uses direct dense residual equations, not ATLAS banded solves or the solver's
Bernoulli implementation. All inputs are synthetic, not experimental data.
"""
from __future__ import annotations
import json,random,math,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from scipy.optimize import root
from math_physics_atlas.v1_models import device_problem,solve_device,manufactured_equilibrium,DomainError

def expbern(x):
 x=np.asarray(x,dtype=float)
 return np.where(np.abs(x)<1e-5,1-x/2+x*x/12-x**4/720,x/np.expm1(np.where(np.abs(x)<1e-5,1.,x)))

def independent_residual(y,pro):
 m=pro.interior
 u=np.r_[pro.voltage[0],y[:m],pro.voltage[1]]
 n=np.r_[pro.electrons[0],y[m:2*m],pro.electrons[1]]
 p=np.r_[pro.holes[0],y[2*m:3*m],pro.holes[1]]
 du=np.diff(u)
 fn=(pro.diff_e/pro.h)*(expbern(-du)*n[:-1]-expbern(du)*n[1:])
 fp=(pro.diff_h/pro.h)*(expbern(du)*p[:-1]-expbern(-du)*p[1:])
 poisson=pro.lambda_sq/pro.h**2*(2*u[1:-1]-u[:-2]-u[2:])-(p[1:-1]-n[1:-1]+np.asarray(pro.doping))
 return np.r_[poisson,np.diff(fn),np.diff(fp)]

def run():
 rng=random.Random(20261116);cases=0;scalars=0;max_error=0.;max_res=0.;negative_refusals=0
 # Independent dense nonlinear root solve, starts with linear state not ATLAS solution.
 for k in range(60):
  n=rng.randrange(2,10);a=rng.uniform(-.3,.3);b=rng.uniform(-.3,.3)
  nc=(rng.uniform(.35,1.1),rng.uniform(.35,1.1));pc=(rng.uniform(.35,1.1),rng.uniform(.35,1.1))
  dop=[rng.uniform(-.2,.2) for _ in range(n)]
  problem=device_problem(n,rng.uniform(.7,2.5),dop,(a,b),nc,pc)
  u_guess=np.linspace(a,b,n+2)[1:-1]
  ini=np.r_[u_guess,np.linspace(nc[0],nc[1],n+2)[1:-1],np.linspace(pc[0],pc[1],n+2)[1:-1]]
  opt=root(independent_residual,ini,args=(problem,),method='hybr',options={'xtol':1e-11})
  residual=float(np.max(np.abs(independent_residual(opt.x,problem))))
  if residual>2e-9 or not np.isfinite(opt.x).all():raise AssertionError(f'Independent root residual failure {k} {residual} {opt.message}')
  solver=solve_device(problem,tol=1e-10,relax=.5)
  atlas=np.r_[solver.potential[1:-1],solver.electrons[1:-1],solver.holes[1:-1]]
  err=float(np.max(np.abs(atlas-opt.x)))
  if err>2e-8:raise AssertionError(f'Independent comparison failed {k}: {err}')
  max_error=max(max_error,err);max_res=max(max_res,residual);cases+=1;scalars+=len(atlas)
 for n in (3,7,15,31,63,127):
  pr,u,nv,pv=manufactured_equilibrium(n,slope=.5)
  ans=solve_device(pr,tol=1e-9)
  if max(abs(aa-bb) for aa,bb in zip(ans.potential,u))>2e-10:raise AssertionError('manufactured mismatch')
  cases+=1
 for n in (0,1,129,True):
  try:device_problem(n,1.)
  except DomainError:negative_refusals+=1
  else:raise AssertionError('input should have failed')
 return {'schema':'atlas.math-physics-v1-independent-oracle/1','result':'passed','seed':20261116,
    'dense_scipy_root_systems':60,'scalar_state_comparisons':scalars,'max_absolute_difference':max_error,
    'max_dense_root_residual':max_res,'manufactured_equilibrium_cases':6,'invalid_grid_rejections':negative_refusals,
    'numpy':np.__version__,'science':'algorithmic comparisons on constructed data; no experiments or independent expert review'}
if __name__=='__main__':print(json.dumps(run(),indent=2))
