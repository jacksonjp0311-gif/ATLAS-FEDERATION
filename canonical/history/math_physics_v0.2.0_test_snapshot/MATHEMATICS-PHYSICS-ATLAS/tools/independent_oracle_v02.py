"""Optional independent finite-case checks using NumPy + analytic PDE solutions.

Not laboratory experiments, theorem proofs, physical calibration, or peer review.
Output counts cases, not individual element comparisons; never claims to
validate a full general SVD beyond the bounded analytic 2x2 diagnostic.
"""
import json,math,random,sys
from pathlib import Path
import numpy as np
from math_physics_atlas.v02_models import (qr_least_squares,svd2_diagnostics,fft_radix2,
                  nonlinear_rk4_adaptive,heat1d_dirichlet,wave1d_dirichlet,NumericalDomainError)

def verify(seed=20261115):
    rng=random.Random(seed)
    tested={};maxerr={}
    def check(group, err, tol):
        if not math.isfinite(err) or err>tol:
            raise AssertionError(f'{group} error {err} exceeds {tol}')
        tested[group]=tested.get(group,0)+1
        maxerr[group]=max(maxerr.get(group,0.0),err)
    for _ in range(300):
        m=rng.randint(4,18);n=rng.randint(1,3)
        a=np.array([[rng.uniform(-1,1) for _ in range(n)] for j in range(m)],dtype=float)
        # Add identity-like anchors, avoid near-rank-deficient examples for this oracle.
        a[:n,:]+=np.eye(n)
        b=np.array([rng.uniform(-2,2) for _ in range(m)],dtype=float)
        our=qr_least_squares(a.tolist(),b.tolist())['solution']
        ref=np.linalg.lstsq(a,b,rcond=None)[0]
        check('householder_qr_vs_lapack_lstsq',float(np.max(np.abs(np.array(our)-ref))),2e-9)
    for _ in range(300):
        a=np.array([[rng.uniform(-4,4) for _ in range(2)] for _ in range(2)],dtype=float)
        our=svd2_diagnostics(a.tolist())['singular_values']
        ref=np.linalg.svd(a,compute_uv=False)
        check('analytic_svd2_vs_lapack_svd',float(np.max(np.abs(np.array(our)-ref))),1e-10)
    for _ in range(200):
        n=2**rng.randint(0,7)
        s=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for k in range(n)]
        ours=fft_radix2(s)
        ref=np.fft.fft(np.asarray(s))
        check('radix2_fft_vs_numpy_fft',float(np.max(np.abs(np.asarray(ours)-ref))),1e-10)
        inv=fft_radix2(ours,inverse=True)
        check('radix2_inverse_roundtrip',float(np.max(np.abs(np.asarray(inv)-np.asarray(s)))),1e-10)
    for _ in range(120):
        y0=rng.uniform(0.05,0.95); t=rng.uniform(0.1,7)
        our=nonlinear_rk4_adaptive(lambda tt,y:y*(1-y),0,y0,t,step=0.4)['state']
        ref=1/(1+(1/y0-1)*math.exp(-t))
        check('adaptive_rk4_vs_analytic_logistic',abs(our-ref),2e-6)
    for _ in range(100):
        n=rng.choice((20,40,80)); dx=1/n;alpha=rng.uniform(0.03,0.2)
        dt=0.25*dx*dx/alpha;steps=rng.randint(1,80)
        u=[math.sin(math.pi*i/n) for i in range(n+1)]
        ours=heat1d_dirichlet(u,alpha,dx,dt,steps)
        ref=math.exp(-alpha*math.pi**2*dt*steps)
        check('ftcs_heat_vs_analytic_eigenmode',max(abs(x-ref*v) for x,v in zip(ours,u)),8e-3)
    for _ in range(100):
        n=rng.choice((20,40,80));dx=1/n;c=rng.uniform(0.2,2)
        dt=0.5*dx/c;steps=rng.randint(1,90)
        u=[math.sin(math.pi*i/n) for i in range(n+1)]
        ours=wave1d_dirichlet(u,c,dx,dt,steps)
        ref=math.cos(c*math.pi*dt*steps)
        check('leapfrog_wave_vs_analytic_eigenmode',max(abs(x-ref*v) for x,v in zip(ours,u)),8e-3)
    negative=0
    def must_reject(fn,*args):
        nonlocal negative
        try:fn(*args)
        except NumericalDomainError:negative+=1
        else:raise AssertionError('domain guard failed: '+fn.__name__)
    for k in range(30):
        must_reject(qr_least_squares,[[1.,2.],[2.,4.],[3.,6.]],[1,2,3])
        must_reject(fft_radix2,[0]*rng.choice((3,5,6,7)))
        must_reject(heat1d_dirichlet,[0,1,0],1.0,1.0,0.6,1)
        must_reject(wave1d_dirichlet,[0,1,0],1.0,1.0,1.1,1)
    tested['deliberate_domain_refusals']=negative
    return {'schema':'atlas.math-physics-v02-independent-oracle/1','seed':seed,'result':'passed',
            'numeric_cases':sum(v for k,v in tested.items() if k!='deliberate_domain_refusals'),
            'rejected_invalid_cases':negative,'counts':tested,'max_abs_error':maxerr,
            'numpy_version':np.__version__,'methods':'NumPy LAPACK/FFT and separate analytic ODE/PDE eigenmode formulas',
            'physical_experiments':0,'independent_scientific_peer_review':False,'original_publisher_files_authenticated':0,
            'general_svd_solver_implemented':False}

if __name__=='__main__':
    x=verify();out=Path(sys.argv[1]) if len(sys.argv)>1 else None
    if out:out.write_text(json.dumps(x,indent=2)+'\n')
    print(json.dumps(x,indent=2))
