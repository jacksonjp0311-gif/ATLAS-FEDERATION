"""Constructed deterministic v1 content-candidate investigations; not laboratory data."""
from .v1_models import (manufactured_equilibrium,solve_device,device_problem,
 physical_scaling,DomainError)

def casebook_v1():
 cases=[]
 for count,slope in ((4,-.6),(8,.5),(16,.8),(32,-.5),(64,.2)):
  problem,u,n,p=manufactured_equilibrium(count,slope=slope)
  result=solve_device(problem,tol=1e-9)
  err=max(abs(x-y) for x,y in zip(result.potential,u))
  ok=err<1e-10 and result.residuals['electron_conservation']<1e-10 and result.residuals['hole_conservation']<1e-10
  cases.append({'id':f'manufactured-equilibrium-{count}','status':'passed' if ok else 'failed','max_voltage_error':err})
 for count in (4,12,32):
  p=device_problem(count,1.,0.1,(0.,.4),(.5,.8),(.6,1.2))
  s=solve_device(p)
  ok=(s.residuals['poisson']<1e-8 and s.residuals['electron_conservation']<1e-8 and s.residuals['hole_conservation']<1e-8)
  cases.append({'id':f'biased-contact-{count}','status':'passed' if ok else 'failed','iterations':s.iterations})
 for length in (1e-6,2e-6):
  m=physical_scaling(300,length,1e-10,1e21)
  cases.append({'id':f'SI-to-dimensionless-{length}','status':'passed' if m['thermal_voltage_V']>0 and m['lambda_sq']>0 else 'failed','lambda_sq':m['lambda_sq']})
 try:
  p=device_problem(12,1.,.2,(0.,.4),(.4,.7),(.8,1.))
  solve_device(p,maxiter=1,relax=.3)
  passfail='failed'
 except DomainError:
  passfail='passed'
 cases.append({'id':'unconverged-rejection','status':passfail})
 return {'count':len(cases),'status':'passed' if all(x['status']=='passed' for x in cases) else 'failed',
   'cases':cases,'scope':'constructed zero-generation stationary and SI-unit examples; not real device observations'}
