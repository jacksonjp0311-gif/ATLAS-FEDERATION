#!/usr/bin/env python3
"""Independent NumPy dense-matrix oracle for ATLAS FORGE v0.4 2D Poisson.

Assembles the finite-difference matrix independently from problem inputs.
This is a second software implementation (NOT an independent experiment).
"""
import json,math,random,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from math_physics_atlas.v04_models import poisson2d_problem,solve_poisson2d_cg,manufactured_sine_refinement


def independent_matrix(nx,ny,lx,ly,eps,rho,bound):
    h=lx/(nx+1);k=ly/(ny+1);N=nx*ny
    A=np.zeros((N,N),dtype=np.float64);b=np.zeros(N,dtype=np.float64)
    for j in range(1,ny+1):
        for i in range(1,nx+1):
            row=(j-1)*nx+i-1
            b[row]=rho[j,i]
            for di,dj,ds in [(-1,0,h),(1,0,h),(0,-1,k),(0,1,k)]:
                ni=i+di;nj=j+dj
                e1=float(eps[j,i]);e2=float(eps[nj,ni]);face=2/(1/e1+1/e2)
                weight=face/(ds*ds)
                A[row,row]+=weight
                if 1<=ni<=nx and 1<=nj<=ny:
                    A[row,(nj-1)*nx+ni-1]-=weight
                else:
                    b[row]+=weight*bound[nj,ni]
    return A,b


def run(seed=20261115, trials=144):
    rnd=random.Random(seed)
    checked_values=0;max_error=0.0;max_residual_ratio=0.
    for t in range(trials):
        nx=rnd.randint(2,8);ny=rnd.randint(2,7)
        lx=rnd.uniform(0.7,2.4);ly=rnd.uniform(0.5,2.1)
        e_base=rnd.uniform(0.2,2.0)
        eps=np.array([[e_base*(1+0.1*i+0.15*j+rnd.uniform(-0.03,0.03))
                       for i in range(nx+2)] for j in range(ny+2)])
        rho=np.array([[rnd.uniform(-1.0,1.0) for i in range(nx+2)] for j in range(ny+2)])
        bound=np.array([[rnd.uniform(-0.6,0.6) for i in range(nx+2)] for j in range(ny+2)])
        model=poisson2d_problem(nx,ny,lx,ly,eps.tolist(),rho.tolist(),bound.tolist())
        out=solve_poisson2d_cg(model,rtol=2e-11,maxiter=2500)
        if not out['converged']:
            raise AssertionError(f'CG did not converge on trial {t}: {out["status"]}')
        A,b=independent_matrix(nx,ny,lx,ly,eps,rho,bound)
        direct=np.linalg.solve(A,b)
        field=np.array(out['potential_volts'])[1:ny+1,1:nx+1].ravel()
        error=float(np.max(np.abs(field-direct)))
        max_error=max(max_error,error)
        checked_values+=len(direct)
        if error>2e-8:
            raise AssertionError(f'oracle solution mismatch: trial {t}, max error {error:.3g}')
        relative=float(np.linalg.norm(A@field-b)/max(np.linalg.norm(b),1e-30))
        max_residual_ratio=max(max_residual_ratio,relative)
        if relative>1e-8:
            raise AssertionError(f'independent residual failed: trial {t}, {relative:.3g}')
        # Independently sum all physical boundary fluxes. The finite-volume
        # balance uses per-unit-invariant-depth C/m, no calibrated physics.
        potential=np.asarray(out['potential_volts'])
        flux=0.0
        for j in range(1,ny+1):
            for i,neigh in ((1,0),(nx,nx+1)):
                face=2/(1/eps[j,i]+1/eps[j,neigh])
                flux+=face*(potential[j,i]-potential[j,neigh])/model.hx*model.hy
        for i in range(1,nx+1):
            for j,neigh in ((1,0),(ny,ny+1)):
                face=2/(1/eps[j,i]+1/eps[neigh,i])
                flux+=face*(potential[j,i]-potential[neigh,i])/model.hy*model.hx
        q=sum(float(rho[j,i]) for j in range(1,ny+1) for i in range(1,nx+1))*model.hx*model.hy
        if abs(flux-q)>1e-8:
            raise AssertionError(f'independent Gauss flux mismatch trial {t}: {flux-q}')
    refinement=manufactured_sine_refinement((7,15,31,63))
    if min(refinement['error_ratios'])<3.95:
        raise AssertionError('spatial order-of-accuracy refinement failed')
    return {'schema':'atlas.math-v04-independent-numpy-oracle/1','result':'passed',
      'seed':seed,'dense_independent_systems':trials,'independently_compared_potential_values':checked_values,
      'independent_operator_residuals':trials,'independent_boundary_gauss_checks':trials,
      'max_absolute_potential_difference':max_error,
      'max_relative_dense_operator_residual':max_residual_ratio,
      'manufactured_sine_refinement':refinement,
      'numpy_version':np.__version__,'physical_measurements':0,
      'experimental_validation':False,'independent_peer_review':False,
      'scope':'NumPy direct solves of independently assembled small-grid systems; these are software/numerical checks, not laboratory experiments'}

if __name__=='__main__':
    r=run()
    print(json.dumps(r,indent=2))
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(json.dumps(r,indent=2)+'\n')
