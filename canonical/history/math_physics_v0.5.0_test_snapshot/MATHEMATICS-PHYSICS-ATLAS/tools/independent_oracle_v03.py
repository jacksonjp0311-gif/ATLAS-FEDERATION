#!/usr/bin/env python3
"""Independent NumPy and analytic checks of authored finite v0.3 kernels.

Oracle comparisons are numerical software evidence, NOT independent peer review,
scientific instrument measurements, or validation of underlying physical laws.
"""
from pathlib import Path
import json,math,random,sys
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from math_physics_atlas.v03_models import (jacobi_svd,svd_least_squares,
    poisson1d_dirichlet,implicit_heat1d_dirichlet,tridiagonal_solve,ReferenceDomainError)

def main():
    rng=np.random.default_rng(20261115);rnd=random.Random(20261115)
    counts={};maxerr=0.;failures=[]
    def record(cat,actual,expected,atol=1e-9,rtol=1e-9):
        nonlocal maxerr
        a=np.asarray(actual,dtype=np.float64);b=np.asarray(expected,dtype=np.float64)
        err=float(np.max(np.abs(a-b)))
        maxerr=max(maxerr,err)
        if not np.allclose(a,b,atol=atol,rtol=rtol):
            failures.append(f'{cat} residual={err:.4g} expected={b.flatten()[:3]} actual={a.flatten()[:3]}')
        counts[cat]=counts.get(cat,0)+1
    for i in range(360):
        m=int(rng.integers(1,9));n=int(rng.integers(1,9))
        a=rng.normal(size=(m,n))
        if i%5==0 and n>1:a[:,-1]=a[:,0]
        if i%11==0:a*=1e-4
        got=jacobi_svd(a.tolist())
        expected=np.linalg.svd(a,compute_uv=False)
        record('svd_singular_values_numpy',got['singular_values'],expected,atol=2e-10,rtol=1e-8)
        if got['reconstruction_relative_frobenius']>1e-9:failures.append('SVD reconstruction error')
    for i in range(360):
        m=int(rng.integers(1,9));n=int(rng.integers(1,9))
        a=rng.normal(size=(m,n))
        if i%7==0 and n>1:a[:,-1]=a[:,0]
        b=rng.normal(size=m)
        got=svd_least_squares(a.tolist(),b.tolist(),rank_rtol=1e-10)
        reference=np.linalg.lstsq(a,b,rcond=1e-10)[0]
        record('svd_minimum_norm_numpy',got['solution'],reference,atol=2e-8,rtol=2e-7)
    for i in range(240):
        cells=int(rng.integers(1,100));L=float(rng.uniform(.1,4.))
        eps=float(rng.uniform(.1,10.));rho=float(rng.uniform(-2,2))
        left=float(rng.normal());right=float(rng.normal())
        got=poisson1d_dirichlet([rho]*cells,eps,L,left,right)
        expected=[left+(right-left)*x/L+rho*x*(L-x)/(2*eps) for x in got['x_m']]
        record('poisson_analytic_quadratic',got['potential_volts'],expected,atol=1e-10,rtol=1e-9)
        if abs(got['gauss_balance_residual_C_per_m2'])>1e-8:failures.append('Gauss balance')
    for i in range(240):
        cells=int(rng.integers(1,27));N=cells+2
        original=rng.normal(size=N)
        alpha=float(rng.uniform(.05,4));dx=float(rng.uniform(.03,.3));fourier=float(10**rng.uniform(-2,2))
        dt=fourier*dx*dx/alpha
        method='backward_euler' if i%2 else 'crank_nicolson'
        got=implicit_heat1d_dirichlet(original.tolist(),alpha,dx,dt,1,method=method)
        r=fourier
        if method=='backward_euler':
            main=1+2*r;off=-r
            rhs=original[1:-1].copy();rhs[0]+=r*original[0];rhs[-1]+=r*original[-1]
        else:
            main=1+r;off=-r/2
            rhs=original[1:-1]+r/2*(original[:-2]-2*original[1:-1]+original[2:]);rhs=rhs.copy()
            rhs[0]+=r/2*original[0];rhs[-1]+=r/2*original[-1]
        dense=np.diag(np.full(cells,main))+np.diag(np.full(cells-1,off),1)+np.diag(np.full(cells-1,off),-1)
        reference=np.concatenate([[original[0]],np.linalg.solve(dense,rhs),[original[-1]]])
        record('implicit_heat_dense_numpy',got['state'],reference,atol=1e-10,rtol=1e-9)
    for i in range(100):
        n=int(rng.integers(1,50));lower=rng.uniform(-.2,.2,size=n-1)
        upper=rng.uniform(-.2,.2,size=n-1);diag=rng.uniform(1.5,2.5,size=n);rhs=rng.normal(size=n)
        a=np.diag(diag)+np.diag(lower,-1)+np.diag(upper,1)
        reference=np.linalg.solve(a,rhs)
        got=tridiagonal_solve(lower.tolist(),diag.tolist(),upper.tolist(),rhs.tolist())
        record('tridiagonal_numpy',got,reference,atol=1e-10,rtol=1e-9)
    bad=[lambda:jacobi_svd([[float('nan')]]),lambda:jacobi_svd([[1.,2.],[3.]]),
         lambda:jacobi_svd([[1.]],rank_rtol=0.),lambda:svd_least_squares([[1.]],[]),
         lambda:poisson1d_dirichlet([1.],0.,1.),lambda:poisson1d_dirichlet([1.],1.,-1.),
         lambda:implicit_heat1d_dirichlet([0.,1.,0.],1.,1.,0.,1),
         lambda:tridiagonal_solve([], [0.], [], [1.])]
    refusals=0
    for i in range(120):
        try:bad[i%len(bad)]()
        except ReferenceDomainError:refusals+=1
        else:failures.append('invalid input incorrectly accepted')
    result={'schema':'atlas.math-physics-v03-independent-numerical/1','status':'passed' if not failures else 'failed',
            'seed':20261115,'numpy_version':np.__version__,'counts':counts,
            'comparisons':sum(counts.values()),'invalid_input_refusals':refusals,
            'max_absolute_error_in_native_units':maxerr,'failures':failures[:25],
            'evidence_limits':['Finite NumPy/analytic numerical comparisons on generated inputs only',
              'Some reference formulas are based on the same underlying mathematical model',
              'No publisher files authenticated; no real physical measurements or AI model evaluations',
              'No mathematical theorem of universal convergence or scientific peer review']}
    print(json.dumps(result,indent=2))
    return result
if __name__=='__main__':
    x=main();raise SystemExit(x['status']!='passed')
