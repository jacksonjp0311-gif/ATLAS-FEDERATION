"""ATLAS FORGE v0.5 numerical bridge: bounded equilibrium and drift–diffusion flux.

Educational software-reference algorithms; no device calibration or measurement.
The nonlinear equation is dimensionless: -alpha*u'' + beta*sinh(u) = f(x),
with prescribed Dirichlet endpoint values. In a nondegenerate equilibrium
analogy u = V/V_T; beta*sinh represents modeled mobile carrier charge.
This is NOT a coupled drift–diffusion simulator, nor is alpha a measured device.

Scharfetter–Gummel edge flux exactly solves constant-field 1D drift–diffusion
J=-D(n' - n*u') for linearly interpolated u and constant D on one edge.
Units of J are number/(m**2 s) when n is number/m**3 and D m**2/s.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import cosh, exp, expm1, isfinite, sin, sinh, pi

class ReferenceDomainError(ValueError):
    """Unsupported finite-input range, invalid geometry, or ill-defined solve."""


def _finite(x, label: str) -> float:
    if type(x) not in (int, float):
        raise ReferenceDomainError(f'{label} must be a real scalar, not bool/string')
    try: y=float(x)
    except (OverflowError, ValueError) as exc: raise ReferenceDomainError(f'{label} cannot be converted') from exc
    if not isfinite(y): raise ReferenceDomainError(f'{label} is not finite')
    return y


def bernoulli_bounded(x: float) -> float:
    """Compute B(x)=x/(exp(x)-1), continuous at zero and stable for |x|<=150.

    B(-x)=B(x)+x. This identity is useful for independent checks.
    """
    x=_finite(x,'dimensionless potential jump')
    if abs(x)>150: raise ReferenceDomainError('jump outside bounded reference [-150,150]')
    if abs(x)<1e-4:
        x2=x*x
        return 1.0-x/2.0+x2/12.0-x2*x2/720.0+x2*x2*x2/30240.0
    if x>50:
        y=exp(-x)
        return x*y/(1-y)
    if x<-50:
        y=exp(x)
        return -x/(1-y)
    return x/expm1(x)


def exponential_fitted_flux(u_left, u_right, n_left, n_right, diffusion, edge_length):
    """SG particle flux, left-to-right, across a single fixed-field 1D edge.

    n>=0 in 1/m^3, D>0 in m^2/s, h>0 in m, u=V/V_T dimensionless.
    The sign assumes positive particle mobility under increasing u.
    When delta_u=0 this is Fick's law; if n_R=n_L*exp(delta_u), J=0.
    """
    u0=_finite(u_left,'u_left');u1=_finite(u_right,'u_right')
    n0=_finite(n_left,'n_left');n1=_finite(n_right,'n_right')
    D=_finite(diffusion,'diffusion');h=_finite(edge_length,'edge_length')
    if not (0<=n0<=1e26 and 0<=n1<=1e26):raise ReferenceDomainError('negative or enormous density')
    if not (1e-20<=D<=1e3 and 1e-12<=h<=1e6):raise ReferenceDomainError('D,h outside reference range')
    jump=u1-u0
    return_value=(D/h)*(bernoulli_bounded(-jump)*n0-bernoulli_bounded(jump)*n1)
    if not isfinite(return_value):raise ReferenceDomainError('flux overflow')
    return return_value


@dataclass(frozen=True)
class EquilibriumProblem1D:
    n:int; length:float; alpha:float; beta:float
    boundary_left:float; boundary_right:float
    forcing:tuple[float,...]; h:float


def equilibrium_problem(n, length, alpha, beta, forcing, boundaries=(0.0,0.0)):
    """Create bounded 1D dimensionless Poisson–Boltzmann boundary problem.

    forcing: scalar, callable(x) or list of n interior nodal values.
    alpha positive, beta nonnegative, x scaled to a dimensionless length.
    Model parameters are *normalized*; no physical dimensional calibration.
    """
    if type(n) is not int or not (3<=n<=1024):raise ReferenceDomainError('interior n must be integer 3..1024')
    L=_finite(length,'length');a=_finite(alpha,'alpha');b=_finite(beta,'beta')
    if not(1e-6<=L<=1e6 and 1e-10<=a<=1e8 and 0<=b<=1e8):
        raise ReferenceDomainError('dimensionless normalized scales outside bounded regime')
    if not isinstance(boundaries,(tuple,list)) or len(boundaries)!=2:
        raise ReferenceDomainError('two endpoint Dirichlet values required')
    left,right=(_finite(v,'boundary') for v in boundaries)
    if max(abs(left),abs(right))>20:raise ReferenceDomainError('boundary magnitude > 20 thermal voltages')
    h=L/(n+1)
    if callable(forcing):values=tuple(_finite(forcing((i+1)*h),'forcing') for i in range(n))
    elif type(forcing) in (int,float):values=tuple([_finite(forcing,'forcing')]*n)
    elif isinstance(forcing,(tuple,list)) and len(forcing)==n:values=tuple(_finite(f,'forcing') for f in forcing)
    else:raise ReferenceDomainError('forcing must be scalar, callable, or n-vector')
    if max(abs(f) for f in values)>1e8:raise ReferenceDomainError('forcing magnitude outside bounded regime')
    return EquilibriumProblem1D(n,L,a,b,left,right,values,h)


def _residual(p, u):
    c=p.alpha/(p.h*p.h)
    if len(u)!=p.n:raise ReferenceDomainError('interior vector wrong length')
    out=[]
    for i in range(p.n):
        z=u[i]
        if not isfinite(z) or abs(z)>20:
            raise ReferenceDomainError('iterate outside bounded nondegenerate approximation |u|<=20')
        prev=p.boundary_left if i==0 else u[i-1]
        next_=p.boundary_right if i+1==p.n else u[i+1]
        v=c*(2*z-prev-next_)+p.beta*sinh(z)-p.forcing[i]
        if not isfinite(v):raise ReferenceDomainError('residual nonfinite')
        out.append(v)
    return out


def _tridiagonal_solve(lower, diag, upper, rhs):
    """Fresh Thomas elimination; matrix supplied from independent Jacobian expression."""
    n=len(diag)
    if not(n==len(rhs)==len(lower)==len(upper)):raise ReferenceDomainError('tridiagonal shape')
    c=[0.]*n;d=[0.]*n
    for i in range(n):
        pivot=diag[i]-(lower[i]*c[i-1] if i else 0.0)
        if not isfinite(pivot) or pivot<=0:raise ReferenceDomainError('nonpositive Newton pivot')
        c[i]=upper[i]/pivot if i<n-1 else 0.0
        d[i]=(rhs[i]-(lower[i]*d[i-1] if i else 0.0))/pivot
    solution=[0.]*n
    for i in range(n-1,-1,-1): solution[i]=d[i]-(c[i]*solution[i+1] if i+1<n else 0.0)
    if not all(isfinite(x) for x in solution):raise ReferenceDomainError('tridiagonal solve diverged')
    return solution


def solve_equilibrium_1d(p:EquilibriumProblem1D, *, rtol=1e-11, atol=1e-11, maxiter=40):
    """Damped Newton and explicit convergence/failure diagnostics.

    The result includes its true nonlinear residual and nodal charge-flux
    balance. An algorithmic residual is not continuum discretization error.
    """
    if not isinstance(p, EquilibriumProblem1D):raise ReferenceDomainError('expected EquilibriumProblem1D')
    rtol=_finite(rtol,'rtol');atol=_finite(atol,'atol')
    if not(0<=rtol<=0.1 and 0<=atol<=0.1 and rtol+atol>0):raise ReferenceDomainError('invalid tolerance')
    if type(maxiter) is not int or not(1<=maxiter<=100):raise ReferenceDomainError('maxiter 1..100')
    u=[p.boundary_left+(p.boundary_right-p.boundary_left)*(i+1)/(p.n+1) for i in range(p.n)]
    reference=max(1.,max(abs(x) for x in p.forcing))
    threshold=atol+rtol*reference
    c=p.alpha/p.h**2; iterations=0;status='maxiter_exceeded'; rejected=0
    for iteration in range(maxiter+1):
        residual=_residual(p,u)
        norm=max(abs(x) for x in residual)
        if norm<=threshold:
            status='converged';break
        if iteration==maxiter:break
        diag=[2*c+p.beta*cosh(x) for x in u]
        correction=_tridiagonal_solve([-c]*p.n,diag,[-c]*p.n,[-x for x in residual])
        accepted=False
        for halves in range(26):
            step=2.**(-halves)
            cand=[x+step*s for x,s in zip(u,correction)]
            if max(abs(x) for x in cand)>20:
                rejected+=1;continue
            cand_norm=max(abs(x) for x in _residual(p,cand))
            if cand_norm<=norm*(1-1e-4*step):
                u=cand;accepted=True;iterations+=1;break
            rejected+=1
        if not accepted:
            status='line_search_failed';break
    # Compute discrete conservation independently of the linear solver norm.
    left_flux=p.alpha*(u[0]-p.boundary_left)/p.h
    right_flux=p.alpha*(u[-1]-p.boundary_right)/p.h
    charge_balance=(left_flux+right_flux)+p.h*p.beta*sum(sinh(x) for x in u)-p.h*sum(p.forcing)
    return {'converged':status=='converged','status':status,'iterations':iterations,
            'residual_linf':norm,'threshold':threshold,'line_search_rejections':rejected,
            'interior_potential_u':u,'potential_u':[p.boundary_left]+u+[p.boundary_right],
            'charge_flux_balance':charge_balance,'length_dimensionless':p.length,
            'grid_spacing_dimensionless':p.h,'equation':'-alpha u_xx+beta sinh(u)=forcing',
            'real_device_calibration':False,'experimental_data':False}


def manufactured_equilibrium_sine(n,alpha=1.,beta=0.4):
    """Compare continuous constructed exact u=sin(pi*x) against solved grid."""
    p=equilibrium_problem(n,1.,alpha,beta,lambda x:alpha*pi*pi*sin(pi*x)+beta*sinh(sin(pi*x)))
    r=solve_equilibrium_1d(p,rtol=1e-13,atol=1e-13,maxiter=60)
    if not r['converged']:
        raise ReferenceDomainError('manufactured solve did not converge')
    error=max(abs(r['interior_potential_u'][i]-sin(pi*(i+1)*p.h)) for i in range(n))
    return {'n':n,'h':p.h,'error_linf':error,'residual_linf':r['residual_linf']}
