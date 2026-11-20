"""ATLAS FORGE Mathematics & Physics v0.2 reference kernels.

Small bounded offline educational algorithms. Verification is mathematical and
numerical, not a claim of physical calibration or external scientific review.
No network access, data acquisition, GPU, or third-party runtime dependencies.
"""
from __future__ import annotations

from cmath import exp as cexp
from math import copysign, hypot, isfinite, pi, sqrt
from typing import Callable, Sequence

class NumericalDomainError(ValueError):
    """Undefined, ill-conditioned, or unsafe-to-evaluate reference problem."""


def _finite(x: float, name: str) -> float:
    if type(x) not in (int, float) or not isfinite(float(x)):
        raise NumericalDomainError(f"{name} must be a finite real scalar")
    return float(x)


def _positive(x: float, name: str) -> float:
    v = _finite(x, name)
    if v <= 0:
        raise NumericalDomainError(f"{name} must be positive")
    return v


def _vector(seq: Sequence[float], name: str, max_len: int = 512) -> list[float]:
    if not isinstance(seq, (tuple, list)) or not 1 <= len(seq) <= max_len:
        raise NumericalDomainError(f"{name} length must be in [1,{max_len}]")
    return [_finite(v, f"{name}[{i}]") for i, v in enumerate(seq)]


def qr_least_squares(matrix: Sequence[Sequence[float]], rhs: Sequence[float]) -> dict:
    """Full column rank real overdetermined LS via implicit Householder QR.

    Refuses underdetermined and numerically rank-deficient problems; does NOT
    form normal equations or pretend a small residual certifies parameter truth.
    """
    if not isinstance(matrix, (list, tuple)) or not 1 <= len(matrix) <= 128:
        raise NumericalDomainError("bounded rectangular design matrix required")
    rows = [_vector(row, "design row", 32) for row in matrix]
    m = len(rows); n = len(rows[0])
    if m < n or any(len(row) != n for row in rows):
        raise NumericalDomainError("matrix must be rectangular with m>=n")
    b = _vector(rhs, "right-hand side", 128)
    if len(b) != m:
        raise NumericalDomainError("rhs length mismatch")
    original = [row[:] for row in rows]; original_b = b[:]
    for k in range(n):
        col = [rows[i][k] for i in range(k, m)]
        norm = hypot(*col)
        if norm == 0:
            raise NumericalDomainError("rank deficient matrix")
        alpha = -copysign(norm, col[0])
        v = col[:]
        v[0] -= alpha
        vnorm2 = sum(x*x for x in v)
        if vnorm2 == 0 or not isfinite(vnorm2):
            raise NumericalDomainError("invalid Householder reflector")
        for j in range(k, n):
            projection = 2.0 * sum(v[i-k]*rows[i][j] for i in range(k,m)) / vnorm2
            for i in range(k,m):
                rows[i][j] -= projection * v[i-k]
        projb = 2.0 * sum(v[i-k]*b[i] for i in range(k,m)) / vnorm2
        for i in range(k,m):
            b[i] -= projb*v[i-k]
        rows[k][k] = alpha
        for i in range(k+1,m):
            rows[i][k] = 0.0
    diag = [abs(rows[i][i]) for i in range(n)]
    threshold = 20.0 * max(m,n) * 2.220446049250313e-16 * max(diag)
    if min(diag) <= threshold:
        raise NumericalDomainError("numerical rank loss; use an independent rank-aware method")
    sol = [0.0]*n
    for i in range(n-1,-1,-1):
        sol[i] = (b[i]-sum(rows[i][j]*sol[j] for j in range(i+1,n)))/rows[i][i]
    if not all(map(isfinite,sol)):
        raise NumericalDomainError("non-finite least-squares result")
    residuals = [sum(a*x for a,x in zip(row,sol))-bi for row,bi in zip(original,original_b)]
    residual_norm = hypot(*residuals)
    return {"solution":sol,"residual_l2":residual_norm,"r_diagonal_abs":diag,
            "full_column_rank_numerically":True,"units":"matrix coefficients and rhs must have compatible units"}


def svd2_diagnostics(matrix: Sequence[Sequence[float]], rank_rtol:float=1e-12) -> dict:
    """Analytic singular *values* of a real 2x2; not a general SVD solver.

    Rescaling avoids most overflow. The small singular value via determinant
    suffers expected limits under severe cancellation; report diagnostic only.
    """
    if not isinstance(matrix,(tuple,list)) or len(matrix)!=2:
        raise NumericalDomainError("2x2 matrix required")
    rows=[_vector(r,"row",2) for r in matrix]
    if any(len(r)!=2 for r in rows):
        raise NumericalDomainError("2x2 matrix required")
    a,b=rows[0];c,d=rows[1]
    rank_rtol=_finite(rank_rtol,"relative rank tolerance")
    if not 0<rank_rtol<1:
        raise NumericalDomainError("rank tolerance must lie in (0,1)")
    scale=max(abs(a),abs(b),abs(c),abs(d))
    if scale==0:
        return {"singular_values":[0.0,0.0],"condition_2":None,"rank_estimate":0,"rank_rtol":rank_rtol}
    a,b,c,d=(v/scale for v in (a,b,c,d))
    p=hypot(a+d,c-b); q=hypot(a-d,c+b)
    big=(p+q)/2.0
    small=abs(a*d-b*c)/big if big>0 else 0.0
    # Only the ratio is needed for robust condition diagnostics.
    rank=1+(small/big>rank_rtol)
    return {"singular_values":[scale*big,scale*small],
            "condition_2":(big/small if small>0 else None),
            "rank_estimate":rank,"rank_rtol":rank_rtol,
            "warning":"analytic 2x2 values only; cancellation can affect very small sigma"}


def fft_radix2(samples: Sequence[complex], inverse:bool=False) -> list[complex]:
    """Cooley–Tukey DFT with the conventional negative forward exponent."""
    if not isinstance(samples,(list,tuple)) or not 1<=len(samples)<=4096:
        raise NumericalDomainError("FFT size must be 1..4096")
    n=len(samples)
    if n & (n-1):
        raise NumericalDomainError("FFT size must be a power of two")
    if type(inverse) is not bool:
        raise NumericalDomainError("inverse must be boolean")
    out=[]
    for x in samples:
        if type(x) not in (int,float,complex):
            raise NumericalDomainError("samples must be real or complex numbers")
        z=complex(x)
        if not isfinite(z.real) or not isfinite(z.imag):
            raise NumericalDomainError("FFT requires finite samples")
        out.append(z)
    bits=n.bit_length()-1
    for i in range(n):
        j=int(f"{i:0{bits}b}"[::-1],2) if bits else 0
        if j>i:
            out[i],out[j]=out[j],out[i]
    length=2
    while length<=n:
        wstep=cexp((2j if inverse else -2j)*pi/length)
        for start in range(0,n,length):
            w=1+0j
            for k in range(length//2):
                a=out[start+k]
                b=out[start+k+length//2]*w
                out[start+k]=a+b
                out[start+k+length//2]=a-b
                w*=wstep
        length*=2
    if inverse:
        out=[z/n for z in out]
    return out


def nonlinear_rk4_adaptive(rhs:Callable[[float,float],float], t0:float, y0:float,
                           t1:float, *, step:float=0.1, atol:float=1e-9,
                           rtol:float=1e-7, max_attempts:int=100000) -> dict:
    """Adaptive scalar RK4 step-doubling, Richardson correction, bounded work.

    Local error control is not a stiffness detector or a global solution bound.
    """
    if not callable(rhs):
        raise NumericalDomainError("rhs must be callable")
    t=_finite(t0,"start time");y=_finite(y0,"initial state");end=_finite(t1,"end time")
    if end<=t:
        raise NumericalDomainError("end time must exceed start")
    h=min(_positive(step,"initial step"),end-t)
    atol=_positive(atol,"absolute tolerance");rtol=_positive(rtol,"relative tolerance")
    if type(max_attempts) is not int or not 1<=max_attempts<=200000:
        raise NumericalDomainError("invalid attempt budget")
    def f(time, val):
        value=_finite(rhs(time,val),"derivative")
        return value
    def rk4(time,val,span):
        k1=f(time,val)
        k2=f(time+span/2,val+span*k1/2)
        k3=f(time+span/2,val+span*k2/2)
        k4=f(time+span,val+span*k3)
        ans=val+span*(k1+2*k2+2*k3+k4)/6
        return _finite(ans,"RK4 state")
    accepted=rejected=0
    for _ in range(max_attempts):
        if t>=end:
            break
        h=min(h,end-t)
        if t+h==t:
            raise NumericalDomainError("step underflow")
        whole=rk4(t,y,h)
        half=rk4(t,y,h/2)
        fine=rk4(t+h/2,half,h/2)
        estimate=abs(fine-whole)/15.0
        tolerance=atol+rtol*max(abs(y),abs(fine))
        if estimate<=tolerance:
            y=_finite(fine+(fine-whole)/15.0,"extrapolated state")
            t+=h
            accepted+=1
        else:
            rejected+=1
        factor=5.0 if estimate==0 else min(5.0,max(0.2,0.9*(tolerance/estimate)**0.2))
        h*=factor
    if t<end:
        raise NumericalDomainError("attempt budget exhausted before end time")
    return {"time":t,"state":y,"accepted_steps":accepted,"rejected_steps":rejected,
            "error_control":"heuristic local RK4 step doubling, not global or stiff guarantee"}


def heat1d_dirichlet(initial:Sequence[float], alpha:float, dx:float, dt:float, steps:int) -> list[float]:
    """Forward-time central-space heat equation on a uniform fixed-zero grid.

    Thermal diffusivity alpha [m^2/s], spatial step dx [m], dt [s].
    Enforces Fourier number 0 < alpha*dt/dx^2 <= 1/2 for monotone update.
    """
    u=_vector(initial,"heat grid",512)
    if len(u)<3:
        raise NumericalDomainError("heat grid requires >=3 points")
    if abs(u[0])>1e-14 or abs(u[-1])>1e-14:
        raise NumericalDomainError("Dirichlet boundaries must be zero")
    alpha=_positive(alpha,"diffusivity");dx=_positive(dx,"spatial step");dt=_positive(dt,"time step")
    if type(steps) is not int or not 0<=steps<=10000:
        raise NumericalDomainError("invalid time-step count")
    fourier=alpha*(dt/dx)/dx
    if not 0<fourier<=0.5:
        raise NumericalDomainError("FTCS positivity/maximum-principle stability condition violated")
    for _ in range(steps):
        u=[0.0]+[u[i]+fourier*(u[i-1]-2*u[i]+u[i+1]) for i in range(1,len(u)-1)]+[0.0]
        if not all(map(isfinite,u)):
            raise NumericalDomainError("nonfinite heat state")
    return u


def wave1d_dirichlet(displacement:Sequence[float], c:float, dx:float,
                     dt:float, steps:int) -> list[float]:
    """Centered leapfrog second-order wave u_tt=c^2*u_xx, zero initial speed.

    Grid fixed-zero endpoints, c [m/s], dx [m], dt [s], c*dt/dx <= 1.
    """
    u0=_vector(displacement,"wave grid",512)
    if len(u0)<3 or abs(u0[0])>1e-14 or abs(u0[-1])>1e-14:
        raise NumericalDomainError("wave requires >=3 points and zero endpoints")
    c=_positive(c,"wave speed");dx=_positive(dx,"spatial step");dt=_positive(dt,"time step")
    if type(steps) is not int or not 0<=steps<=10000:
        raise NumericalDomainError("invalid time-step count")
    courant=c*(dt/dx)
    if courant>1:
        raise NumericalDomainError("wave CFL condition violated")
    if steps==0:
        return u0
    q=courant*courant
    old=u0
    now=[0.0]+[old[j]+0.5*q*(old[j-1]-2*old[j]+old[j+1]) for j in range(1,len(old)-1)]+[0.0]
    for _ in range(1,steps):
        nxt=[0.0]+[2*now[j]-old[j]+q*(now[j-1]-2*now[j]+now[j+1]) for j in range(1,len(now)-1)]+[0.0]
        old,now=now,nxt
        if not all(map(isfinite,now)):
            raise NumericalDomainError("nonfinite wave state")
    return now
