"""ATLAS FORGE v0.4: matrix-free 2D electrostatic Poisson reference.

Solve -div(epsilon grad V) = rho with Dirichlet boundaries on a rectangular
regular node-centred grid; epsilon is a specified positive *linear dielectric*.
Unknowns are interior nodal potentials. Five-point conservative face fluxes
use harmonic averaging of neighbouring nodal permittivities. A is real SPD.

Scope: finite, bounded Python software model, NOT a calibrated semiconductor
simulator, field-measured dielectric, or replacement for industrial solvers.
Units: epsilon F/m; rho C/m^3; V volts; lengths metres; net 2D charge and
boundary flux are both C/m per unit invariant third-dimension length.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import fsum, isfinite, sqrt
from typing import Callable

class ReferenceDomainError(ValueError):
    """Invalid shape, inputs, unsupported numerical range, or CG breakdown."""

MAX_AXIS=64
MAX_UNKNOWN=4096

def _number(x, name):
    if type(x) not in (int,float):
        raise ReferenceDomainError(f'{name}: expected real numeric scalar, not boolean/string')
    try:
        z=float(x)
    except (OverflowError, ValueError) as exc:
        raise ReferenceDomainError(f'{name}: cannot represent as finite float') from exc
    if not isfinite(z):
        raise ReferenceDomainError(f'{name}: nonfinite')
    return z

def _grid(values, rows, columns, name, positive=False):
    if not isinstance(values,(tuple,list)) or len(values)!=rows:
        raise ReferenceDomainError(f'{name}: expected {rows} rows')
    out=[]
    for j,row in enumerate(values):
        if not isinstance(row,(tuple,list)) or len(row)!=columns:
            raise ReferenceDomainError(f'{name}[{j}]: expected {columns} columns')
        vals=tuple(_number(x,f'{name}[{j}][{i}]') for i,x in enumerate(row))
        if positive and any(v<=0 for v in vals):
            raise ReferenceDomainError(f'{name}: must be strictly positive everywhere')
        out.append(vals)
    return tuple(out)

def _sample_spec(spec, nx, ny, dx, dy, name, *, boundary=False, positive=False):
    if type(spec) in (int,float):
        z=_number(spec,name)
        if positive and z<=0:raise ReferenceDomainError(f'{name}: strictly positive')
        return tuple(tuple(z for _ in range(nx+2)) for __ in range(ny+2))
    if callable(spec):
        vals=[]
        for j in range(ny+2):
            vals.append(tuple(_number(spec(i*dx,j*dy),f'{name}({i},{j})') for i in range(nx+2)))
        if positive and any(v<=0 for row in vals for v in row):
            raise ReferenceDomainError(f'{name}: must be strictly positive everywhere')
        return tuple(vals)
    if boundary or positive:
        return _grid(spec,ny+2,nx+2,name,positive=positive)
    # rho accepts full 2D grid or an interior-only rectangle.
    if not isinstance(spec,(list,tuple)):
        raise ReferenceDomainError(f'{name}: numeric scalar, callable or row-major array')
    if len(spec)==ny:
        mid=_grid(spec,ny,nx,name)
        return tuple([tuple(0. for _ in range(nx+2))]+[
            tuple([0.]+list(row)+[0.]) for row in mid]+[tuple(0. for _ in range(nx+2))])
    return _grid(spec,ny+2,nx+2,name)

def _harmonic(a,b):
    # No a*b overflow before division; positive finite a,b.
    return (2*a*b/(a+b)) if max(a,b)<1e140 else (2.0/(1.0/a+1.0/b))

@dataclass(frozen=True)
class PoissonProblem2D:
    nx:int; ny:int; lx:float; ly:float
    hx:float; hy:float
    eps:tuple; charge:tuple; boundaries:tuple
    east:tuple; west:tuple; north:tuple; south:tuple
    diagonal:tuple; rhs:tuple

    def matvec(self, vec):
        if not isinstance(vec,(tuple,list)) or len(vec)!=self.nx*self.ny:
            raise ReferenceDomainError('matvec: vector shape mismatch')
        x=[_number(v,'matvec component') for v in vec]
        out=[]
        for j in range(self.ny):
            for i in range(self.nx):
                k=j*self.nx+i
                s=self.diagonal[k]*x[k]
                if i: s-=self.west[k]*x[k-1]
                if i<self.nx-1:s-=self.east[k]*x[k+1]
                if j:s-=self.south[k]*x[k-self.nx]
                if j<self.ny-1:s-=self.north[k]*x[k+self.nx]
                if not isfinite(s):raise ReferenceDomainError('matvec overflow')
                out.append(s)
        return out


def poisson2d_problem(nx:int, ny:int, lx, ly, epsilon, rho, boundary=0.):
    """Build SPD nodal finite-volume-like operator and Dirichlet RHS.

    epsilon and boundary: scalar, callable(x,y), or full (ny+2)x(nx+2) grid.
    rho additionally accepts ny-by-nx interior grid. Callable evaluated at
    node positions. All lengths metres; no periodic/Neumann/heterogeneous
    tensor medium. Harmonic mean approximates face epsilon and is symmetric.
    """
    if type(nx) is not int or type(ny) is not int or not(2<=nx<=MAX_AXIS and 2<=ny<=MAX_AXIS) or nx*ny>MAX_UNKNOWN:
        raise ReferenceDomainError(f'nx,ny must be integer 2..{MAX_AXIS}; <= {MAX_UNKNOWN} unknowns')
    lx=_number(lx,'lx');ly=_number(ly,'ly')
    if not (1e-10<=lx<=1e9 and 1e-10<=ly<=1e9):
        raise ReferenceDomainError('length in metres must be 1e-10..1e9')
    hx=lx/(nx+1);hy=ly/(ny+1)
    eps=_sample_spec(epsilon,nx,ny,hx,hy,'epsilon',positive=True)
    charge=_sample_spec(rho,nx,ny,hx,hy,'rho')
    bnd=_sample_spec(boundary,nx,ny,hx,hy,'boundary',boundary=True)
    # Limit excessive contrast to a regime in which doubles can represent
    # both face weights and the preconditioned system; not a physics limit.
    all_eps=[v for row in eps for v in row]
    if min(all_eps)<1e-24 or max(all_eps)>1e24:
        raise ReferenceDomainError('epsilon outside bounded numerical reference range 1e-24..1e24 F/m')
    ex=[];wx=[];nyc=[];sy=[];diag=[];rhs=[]
    for j in range(1,ny+1):
        for i in range(1,nx+1):
            v=eps[j][i]
            e=_harmonic(v,eps[j][i+1])/(hx*hx)
            w=_harmonic(v,eps[j][i-1])/(hx*hx)
            n=_harmonic(v,eps[j+1][i])/(hy*hy)
            s=_harmonic(v,eps[j-1][i])/(hy*hy)
            d=fsum((e,w,n,s));f=charge[j][i]
            if i==1:f+=w*bnd[j][0]
            if i==nx:f+=e*bnd[j][nx+1]
            if j==1:f+=s*bnd[0][i]
            if j==ny:f+=n*bnd[ny+1][i]
            if not all(isfinite(a) for a in (e,w,n,s,d,f)) or d<=0:
                raise ReferenceDomainError('unrepresentable finite coefficient or right-hand side')
            ex.append(e);wx.append(w);nyc.append(n);sy.append(s);diag.append(d);rhs.append(f)
    return PoissonProblem2D(nx,ny,lx,ly,hx,hy,eps,charge,bnd,tuple(ex),tuple(wx),tuple(nyc),tuple(sy),tuple(diag),tuple(rhs))

def _dot(a,b):
    z=fsum(x*y for x,y in zip(a,b))
    if not isfinite(z):raise ReferenceDomainError('nonfinite vector dot product')
    return z

def _norm(a):
    return sqrt(max(0.0,_dot(a,a)))

def _gauss(problem, state):
    """Discrete divergence theorem in units C/m per unit z-depth."""
    g=problem
    full=[list(row) for row in g.boundaries]
    for j in range(1,g.ny+1):
        for i in range(1,g.nx+1):
            full[j][i]=state[(j-1)*g.nx+(i-1)]
    flux=[]
    for j in range(1,g.ny+1):
        k=(j-1)*g.nx
        flux.extend((g.west[k]*(full[j][1]-full[j][0])*g.hx*g.hy,
                     g.east[k+g.nx-1]*(full[j][g.nx]-full[j][g.nx+1])*g.hx*g.hy))
    for i in range(1,g.nx+1):
        k=i-1; top=(g.ny-1)*g.nx+i-1
        flux.extend((g.south[k]*(full[1][i]-full[0][i])*g.hx*g.hy,
                     g.north[top]*(full[g.ny][i]-full[g.ny+1][i])*g.hx*g.hy))
    charge=fsum(g.charge[j][i] for j in range(1,g.ny+1) for i in range(1,g.nx+1))*g.hx*g.hy
    flux_sum=fsum(flux)
    return full, charge, flux_sum, flux_sum-charge

def solve_poisson2d_cg(problem:PoissonProblem2D, *, rtol=1e-10,atol=0.0,maxiter=6000):
    """Jacobi-preconditioned CG, explicit residual and exit status.

    Require positive interior Dirichlet operator. Nonconvergence is reported
    as converged=False rather than silently emitting a physical 'solution'.
    """
    if not isinstance(problem,PoissonProblem2D):raise ReferenceDomainError('expected PoissonProblem2D')
    rtol=_number(rtol,'rtol');atol=_number(atol,'atol')
    if not 0<=rtol<0.2 or not 0<=atol<1e100 or (rtol==0 and atol==0):
        raise ReferenceDomainError('need a positive convergence tolerance')
    if type(maxiter) is not int or not(1<=maxiter<=40000):
        raise ReferenceDomainError('maxiter must be integer 1..40000')
    n=problem.nx*problem.ny
    b=problem.rhs;x=[0.]*n;r=list(b)
    z=[r[i]/problem.diagonal[i] for i in range(n)]
    p=list(z);rz=_dot(r,z)
    normb=_norm(b);threshold=max(atol,rtol*normb)
    if _norm(r)<=threshold:
        grid,charge,flux,gauss=_gauss(problem,x)
        return {'converged':True,'iterations':0,'status':'converged','relative_residual':0.,
                'residual_l2':0.,'threshold':threshold,'potential_volts':grid,
                'charge_per_depth_C_per_m':charge,'boundary_flux_per_depth_C_per_m':flux,
                'gauss_balance_residual_C_per_m':gauss,'unknowns':n,'solver':'Jacobi-preconditioned CG'}
    converged=False;iterations=0;status='maxiter_exceeded'
    for it in range(1,maxiter+1):
        ap=problem.matvec(p)
        denom=_dot(p,ap)
        if denom<=0 or not isfinite(denom) or rz<=0:
            raise ReferenceDomainError('CG lost positive-definite descent; numerical breakdown')
        alpha=rz/denom
        x=[xi+alpha*pi for xi,pi in zip(x,p)]
        r=[ri-alpha*ai for ri,ai in zip(r,ap)]
        if not all(isfinite(v) for v in x):raise ReferenceDomainError('CG nonfinite iterate')
        iterations=it
        # Validate with true matrix residual to reject recursive drift.
        if _norm(r)<=threshold or it%50==0:
            ax=problem.matvec(x)
            true_r=[bi-ai for bi,ai in zip(b,ax)]
            if _norm(true_r)<=threshold:
                r=true_r;converged=True;status='converged';break
            if _norm(r)<=threshold:  # restart after residual replacement
                r=true_r
                z=[r[i]/problem.diagonal[i] for i in range(n)]
                p=list(z);rz=_dot(r,z)
                continue
        z=[r[i]/problem.diagonal[i] for i in range(n)]
        next_rz=_dot(r,z)
        if rz<=0 or next_rz<0:raise ReferenceDomainError('CG negative preconditioned norm')
        beta=next_rz/rz
        p=[zi+beta*pi for zi,pi in zip(z,p)]
        rz=next_rz
    true_r=[bi-ai for bi,ai in zip(b,problem.matvec(x))]
    residual=_norm(true_r)
    if residual<=threshold:converged=True;status='converged'
    grid,charge,flux,gauss=_gauss(problem,x)
    return {'converged':converged,'iterations':iterations,'status':status,
            'residual_l2':residual,'relative_residual':residual/normb if normb else residual,
            'threshold':threshold,'potential_volts':grid,
            'charge_per_depth_C_per_m':charge,'boundary_flux_per_depth_C_per_m':flux,
            'gauss_balance_residual_C_per_m':gauss,'unknowns':n,'solver':'Jacobi-preconditioned CG',
            'limitations':'2D linear isotropic dielectric; Dirichlet boundaries; no carrier transport, calibrated measurements, contacts, 3D effects or physical device qualification'}


def manufactured_sine_refinement(sizes=(7,15,31), epsilon=1.0):
    """Separate algebraic convergence from second-order spatial discretization.

    Analytic V=sin(pi*x/Lx)sin(pi*y/Ly), Lx=Ly=1, rho=2*pi^2*eps*V.
    This is a manufactured mathematical example, not an experiment.
    """
    from math import sin,pi
    results=[]
    for n in sizes:
        e=_number(epsilon,'epsilon')
        if e<=0:raise ReferenceDomainError('epsilon must be positive')
        exact=lambda x,y:sin(pi*x)*sin(pi*y)
        model=poisson2d_problem(n,n,1.0,1.0,e,
                   lambda x,y:2*pi*pi*e*exact(x,y),0.0)
        result=solve_poisson2d_cg(model,rtol=1e-12,maxiter=4000)
        if not result['converged']:
            raise ReferenceDomainError('manufactured solution did not converge')
        err=max(abs(result['potential_volts'][j][i]-exact(i*model.hx,j*model.hy))
                for j in range(1,n+1) for i in range(1,n+1))
        results.append({'n':n,'h_m':model.hx,'error_linf_volts':err,
                        'solver_residual_l2':result['residual_l2'],'iterations':result['iterations']})
    return {'cases':results,'error_ratios':[a['error_linf_volts']/b['error_linf_volts'] for a,b in zip(results,results[1:])],
            'scope':'manufactured analytic sine solution; truncation error not model-form or physical uncertainty'}
