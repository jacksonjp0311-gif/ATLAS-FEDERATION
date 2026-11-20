#!/usr/bin/env python3
"""Independent SciPy dense nonlinear root and Decimal/quad comparisons for v0.5.

Optional verification only; core reference models use standard-library Python.
Fixtures are constructed, deterministic, and not independent physical studies.
"""
import json,sys,math,random,decimal
from pathlib import Path
import numpy as np
from scipy.optimize import root
from scipy.integrate import quad
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from math_physics_atlas.v05_models import (
    equilibrium_problem,solve_equilibrium_1d,bernoulli_bounded,exponential_fitted_flux,ReferenceDomainError)

def main():
    rng=random.Random(20261116)
    nonlinear=0; potential_entries=0; max_potential_difference=0.;max_external_residual=0.
    for _ in range(100):
        n=rng.randint(5,23);length=rng.uniform(.8,2.3);alpha=rng.uniform(.5,2.2);beta=rng.uniform(0.05,1.)
        boundary=(rng.uniform(-0.4,.4),rng.uniform(-0.4,.4))
        forcing=[rng.uniform(-1.2,1.2) for __ in range(n)]
        p=equilibrium_problem(n,length,alpha,beta,forcing,boundary)
        candidate=solve_equilibrium_1d(p,rtol=2e-13,atol=1e-13,maxiter=70)
        if not candidate['converged']:raise AssertionError('reference Newton did not converge')
        h=length/(n+1);factor=alpha/h**2
        A=np.diag(np.full(n,2*factor)) + np.diag(np.full(n-1,-factor),1) + np.diag(np.full(n-1,-factor),-1)
        forcing_np=np.array(forcing,dtype=float)
        forcing_np[0]+=factor*boundary[0];forcing_np[-1]+=factor*boundary[1]
        fun=lambda u: A@u+beta*np.sinh(u)-forcing_np
        other=root(fun,np.linspace(boundary[0],boundary[1],n+2)[1:-1],method='hybr',tol=1e-12)
        if not other.success and np.linalg.norm(fun(other.x),np.inf)>5e-9:
            raise AssertionError('external root failed')
        diff=float(np.max(np.abs(other.x-np.asarray(candidate['interior_potential_u']))))
        res=float(np.max(np.abs(fun(np.asarray(candidate['interior_potential_u'])))))
        if diff>5e-9 or res>5e-9:raise AssertionError(('independent comparison',diff,res))
        max_potential_difference=max(max_potential_difference,diff)
        max_external_residual=max(max_external_residual,res)
        nonlinear+=1;potential_entries+=n
    decimal.getcontext().prec=70
    bernoulli=0;max_rel_error=0.
    for x in [-149.,-120.,-75.,-25.,-1.,-1e-5,-1e-10,0.,1e-10,1e-5,1.,25.,75.,120.,149.]+[rng.uniform(-140,140) for _ in range(200)]:
        dx=decimal.Decimal(str(x))
        target=decimal.Decimal(1) if x==0 else dx/(dx.exp()-1)
        computed=bernoulli_bounded(x)
        target_float=float(target)
        # Decimal avoids catastrophic cancellation for near-zero x; absolute floor handles tiny outputs.
        err=abs(computed-target_float)/max(1e-55,abs(target_float))
        if err>1e-10:raise AssertionError(('Bernoulli decimal mismatch',x,err))
        max_rel_error=max(max_rel_error,err);bernoulli+=1
    quadrature=0;max_flux_rel=0.
    for i in range(160):
        du=rng.uniform(-12,12);n0=rng.uniform(.1,5);n1=rng.uniform(.1,5)
        D=rng.uniform(.02,2);h=rng.uniform(.1,3)
        # integrating-factor independent representation for constant linear u across edge
        integral=quad(lambda t:math.exp(-du*t),0.,1.,epsabs=1e-13,epsrel=1e-13)[0]
        integral_flux=(D/h)*(n0-n1*math.exp(-du))/integral
        model=exponential_fitted_flux(0.,du,n0,n1,D,h)
        err=abs(model-integral_flux)/max(1e-8,abs(integral_flux))
        if err>2e-8:raise AssertionError(('quadrature flux mismatch',du,err))
        quadrature+=1;max_flux_rel=max(max_flux_rel,err)
    rejection=0
    for x in (True,float('inf'),float('-inf'),float('nan'),'0',151.,-151.):
        try:bernoulli_bounded(x)
        except ReferenceDomainError:rejection+=1
        else:raise AssertionError('rejected input accepted')
    result={'schema':'atlas.math-v05-independent-numerical-oracle/1','result':'passed','seed':20261116,
       'independent_scipy_dense_nonlinear_roots':nonlinear,'potential_values_compared':potential_entries,
       'max_absolute_potential_difference_dimensionless':max_potential_difference,
       'max_independently_assembled_nonlinear_residual':max_external_residual,
       'high_precision_decimal_bernoulli_values':bernoulli,'max_relative_bernoulli_difference':max_rel_error,
       'separate_quadrature_edge_flux_comparisons':quadrature,'max_relative_flux_difference':max_flux_rel,
       'invalid_input_rejections':rejection,'numpy_version':np.__version__,
       'software_verification_only':True,'physical_experiment_count':0,'independent_peer_review':False,
       'authenticated_publisher_transport_files':0}
    print(json.dumps(result,indent=2))
    return result
if __name__=='__main__':main()
