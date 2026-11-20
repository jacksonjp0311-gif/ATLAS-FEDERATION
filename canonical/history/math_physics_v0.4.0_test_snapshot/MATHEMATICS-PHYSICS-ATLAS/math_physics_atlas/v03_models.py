"""ATLAS FORGE Mathematics & Physics v0.3.0: bounded offline reference algorithms.

Original educational implementation; Python >=3.10, standard library only.
Not qualified for safety-critical engineering, laboratory inference, or theorem certification.
Every solver refuses malformed/non-finite inputs, overlarge problems or nonconvergence.
"""
from __future__ import annotations

from math import copysign, fsum, hypot, isfinite, sqrt
from typing import Sequence

class ReferenceDomainError(ValueError):
    """Invalid input, unsupported numerical regime or solver nonconvergence."""


def _real(value, label):
    if type(value) not in (int, float):
        raise ReferenceDomainError(f"{label}: real scalar required")
    try:
        z=float(value)
    except (OverflowError, ValueError) as exc:
        raise ReferenceDomainError(f"{label}: float conversion failed") from exc
    if not isfinite(z):
        raise ReferenceDomainError(f"{label}: non-finite")
    return z


def _positive(value, label):
    v=_real(value,label)
    if v <= 0:
        raise ReferenceDomainError(f"{label}: must be positive")
    return v


def _vector(seq, label, max_len=4096):
    if not isinstance(seq,(list,tuple)) or not 1<=len(seq)<=max_len:
        raise ReferenceDomainError(f"{label}: length must be 1..{max_len}")
    return [_real(x,f"{label}[{i}]") for i,x in enumerate(seq)]


def _matrix(matrix, max_dim=32):
    if not isinstance(matrix,(list,tuple)) or not 1<=len(matrix)<=max_dim:
        raise ReferenceDomainError("matrix: 1..32 rows required")
    rows=[_vector(row,f"row{i}",max_dim) for i,row in enumerate(matrix)]
    n=len(rows[0])
    if not all(len(row)==n for row in rows):
        raise ReferenceDomainError("matrix: ragged rectangular input")
    return rows


def jacobi_svd(matrix, *, rank_rtol=1e-10, pair_tol=1e-13, max_sweeps=120):
    """Thin real rectangular SVD by one-sided Jacobi on the longer orientation.

    Returns U, singular_values and Vt such that A ~= U diag(s) Vt. Columns
    corresponding to zero singular values have ZERO vectors on one side;
    orthogonality is promised for nonzero modes only. No Gram matrix is formed.
    Rank threshold is explicitly user-specified, not an empirical identifiability
    certificate. Matrices are bounded to 32x32; nonconvergence raises.
    """
    a=_matrix(matrix)
    m,n=len(a),len(a[0]);r=min(m,n)
    rank_rtol=_real(rank_rtol,'rank_rtol')
    pair_tol=_real(pair_tol,'pair_tol')
    if not (1e-15<=pair_tol<=1e-5 and 1e-15<=rank_rtol<0.1):
        raise ReferenceDomainError("tolerances outside supported range")
    if type(max_sweeps) is not int or not 1<=max_sweeps<=300:
        raise ReferenceDomainError("max_sweeps must be integer 1..300")
    largest=max(abs(x) for row in a for x in row)
    if largest>1e100:
        raise ReferenceDomainError("matrix entries too large for bounded reference")
    # Keep all products bounded; scaling preserves condition ratios.
    scaled=[[x/largest for x in row] for row in a] if largest else [[0.]*n for _ in range(m)]
    transposed=m<n
    b=[list(row) for row in zip(*scaled)] if transposed else [row[:] for row in scaled]
    height=len(b);width=len(b[0])
    v=[[float(i==j) for j in range(width)] for i in range(width)]
    converged=(largest==0 or width<2)
    sweeps=0
    if largest:
        for it in range(1,max_sweeps+1):
            sweeps=it;rotations=0
            for p in range(width-1):
                for q in range(p+1,width):
                    pp=fsum(b[k][p]*b[k][p] for k in range(height))
                    qq=fsum(b[k][q]*b[k][q] for k in range(height))
                    pq=fsum(b[k][p]*b[k][q] for k in range(height))
                    if pp==0 or qq==0:
                        continue
                    denom=sqrt(pp)*sqrt(qq)
                    if denom==0 or abs(pq)<=pair_tol*denom:
                        continue
                    zeta=(qq-pp)/(2*pq)
                    if abs(zeta)>1e150:
                        t=0.5/zeta
                    else:
                        t=copysign(1.,zeta)/(abs(zeta)+hypot(1.,zeta))
                    c=1./sqrt(1.+t*t);s=c*t
                    for k in range(height):
                        bp,bq=b[k][p],b[k][q]
                        b[k][p]=c*bp-s*bq
                        b[k][q]=s*bp+c*bq
                    for k in range(width):
                        vp,vq=v[k][p],v[k][q]
                        v[k][p]=c*vp-s*vq
                        v[k][q]=s*vp+c*vq
                    rotations+=1
            if rotations==0:
                converged=True;break
    if not converged:
        raise ReferenceDomainError("Jacobi SVD failed to converge within sweep budget")
    values=[hypot(*(b[k][j] for k in range(height))) for j in range(width)]
    idx=sorted(range(width),key=lambda k:(-values[k],k))
    singular=[largest*values[j] for j in idx]
    if not all(isfinite(x) for x in singular):
        raise ReferenceDomainError("unrepresentable singular value")
    # normalized B columns = left singular vectors of oriented matrix.
    oriented_left=[[b[i][j]/values[j] if values[j] else 0. for j in idx] for i in range(height)]
    oriented_right=[[v[i][j] for j in idx] for i in range(width)]
    if transposed:
        u=oriented_right
        vt=[list(col) for col in zip(*oriented_left)]
    else:
        u=oriented_left
        vt=[list(col) for col in zip(*oriented_right)]
    sigma0=singular[0] if singular else 0.
    rank=sum(s>rank_rtol*sigma0 for s in singular) if sigma0 else 0
    # Crosscheck reconstruction in scaled units to avoid overflow.
    recon=[[fsum(u[i][k]*values[idx[k]]*vt[k][j] for k in range(r)) for j in range(n)] for i in range(m)]
    recon_err=hypot(*(scaled[i][j]-recon[i][j] for i in range(m) for j in range(n)))
    denom=hypot(*(scaled[i][j] for i in range(m) for j in range(n)))
    relative_err=recon_err/denom if denom else 0.
    if not isfinite(relative_err) or relative_err>2e-8:
        raise ReferenceDomainError("SVD failed reconstruction residual check")
    # Orthogonality of the computed numerically nonzero singular modes.
    good=[k for k,s in enumerate(singular) if s>0. and s>rank_rtol*sigma0]
    u_def=max((abs(fsum(u[i][p]*u[i][q] for i in range(m))-(1. if p==q else 0.))
              for p in good for q in good),default=0.)
    v_def=max((abs(fsum(vt[p][j]*vt[q][j] for j in range(n))-(1. if p==q else 0.))
              for p in good for q in good),default=0.)
    if max(u_def,v_def)>1e-7:
        raise ReferenceDomainError("SVD failed active-subspace orthogonality check")
    return {'U':u,'singular_values':singular,'Vt':vt,
            'rank_estimate':rank,'rank_rtol':rank_rtol,
            'condition_2':(singular[0]/singular[-1] if singular[-1]>rank_rtol*sigma0 else None),
            'reconstruction_relative_frobenius':relative_err,
            'active_left_orthogonality_error':u_def,'active_right_orthogonality_error':v_def,
            'sweeps':sweeps,'converged':True,
            'limits':'bounded dense real matrix, floating point rank cutoff; no true-rank guarantee'}


def svd_least_squares(matrix,rhs,*,rank_rtol=1e-10):
    """Numerical minimum-norm truncated-pseudoinverse fit to Ax≈b."""
    a=_matrix(matrix)
    b=_vector(rhs,'rhs',32)
    if len(b)!=len(a):
        raise ReferenceDomainError('rhs dimension mismatch')
    res=jacobi_svd(a,rank_rtol=rank_rtol)
    u,vt,sig=res['U'],res['Vt'],res['singular_values']
    cutoff=rank_rtol*(sig[0] if sig else 0.)
    n=len(a[0]);m=len(a)
    factors=[fsum(u[i][k]*b[i] for i in range(m))/s if s>cutoff and s>0. else 0.
             for k,s in enumerate(sig)]
    sol=[fsum(vt[k][j]*factors[k] for k in range(len(sig))) for j in range(n)]
    residual=[fsum(a[i][j]*sol[j] for j in range(n))-b[i] for i in range(m)]
    if not all(map(isfinite,sol+residual)):
        raise ReferenceDomainError('non-finite least-squares output')
    return {'solution':sol,'residual_l2':hypot(*residual),'rank_estimate':res['rank_estimate'],
            'singular_values':sig,'rank_rtol':rank_rtol,
            'limits':'truncated numerical pseudoinverse; rank decisions depend on relative threshold'}


def tridiagonal_solve(lower,diag,upper,rhs):
    """Thomas elimination; rejects near-zero pivots; no generic pivoting."""
    d=_vector(diag,'diag',4096);n=len(d)
    b=_vector(rhs,'rhs',4096)
    if len(b)!=n or not isinstance(lower,(list,tuple)) or not isinstance(upper,(list,tuple)):
        raise ReferenceDomainError('tridiagonal array shape mismatch')
    if len(lower)!=n-1 or len(upper)!=n-1:
        raise ReferenceDomainError('off-diagonal shape mismatch')
    a=[_real(x,'lower') for x in lower];c=[_real(x,'upper') for x in upper]
    scale=max(map(abs,d+a+c))
    if not scale:
        raise ReferenceDomainError('zero matrix')
    tol=2e-14*scale
    cp=[0.]*n;dp=[0.]*n
    if abs(d[0])<=tol:raise ReferenceDomainError('zero/small first pivot')
    if n>1:cp[0]=c[0]/d[0]
    dp[0]=b[0]/d[0]
    for i in range(1,n):
        pivot=d[i]-a[i-1]*cp[i-1]
        if not isfinite(pivot) or abs(pivot)<=tol:
            raise ReferenceDomainError('zero/small reduced pivot')
        if i<n-1:cp[i]=c[i]/pivot
        dp[i]=(b[i]-a[i-1]*dp[i-1])/pivot
    result=[0.]*n;result[-1]=dp[-1]
    for i in range(n-2,-1,-1):result[i]=dp[i]-cp[i]*result[i+1]
    if not all(map(isfinite,result)):
        raise ReferenceDomainError('non-finite tridiagonal solution')
    return result


def poisson1d_dirichlet(charge_density,epsilon,length,left_volts=0.,right_volts=0.):
    """-epsilon V_xx=rho [C/m^3], constant eps [F/m], 1-D slab [m].

    This is the simplest electrostatic Poisson boundary-value idealization;
    no doping, transport, nonlinear permittivity, quantum or device physics.
    """
    rho=_vector(charge_density,'rho',4096)
    eps=_positive(epsilon,'epsilon');L=_positive(length,'length')
    left=_real(left_volts,'left_volts');right=_real(right_volts,'right_volts')
    h=L/(len(rho)+1)
    scaled=[r*h*h/eps for r in rho]
    if not all(map(isfinite,scaled)):
        raise ReferenceDomainError('scaled charge overflows')
    scaled[0]+=left;scaled[-1]+=right
    n=len(rho)
    V=[left]+tridiagonal_solve([-1.]*(n-1),[2.]*n,[-1.]*(n-1),scaled)+[right]
    efields=[-(V[i+1]-V[i])/h for i in range(n+1)]
    displacement=[eps*x for x in efields]
    residual=[-eps*(V[i+2]-2*V[i+1]+V[i])/(h*h)-rho[i] for i in range(n)]
    gauss_error=displacement[-1]-displacement[0]-h*fsum(rho)
    if not all(map(isfinite,V+efields+displacement+residual+[gauss_error])):
        raise ReferenceDomainError('non-finite physical result')
    return {'potential_volts':V,'x_m':[h*k for k in range(n+2)],'field_volts_per_m':efields,
            'displacement_coulomb_per_m2':displacement,'grid_spacing_m':h,
            'max_poisson_residual_C_per_m3':max(map(abs,residual)),
            'gauss_balance_residual_C_per_m2':gauss_error,
            'limitations':'1D constant linear permittivity; numerical Gauss identity not empirical calibration'}


def implicit_heat1d_dirichlet(initial,alpha_m2_s,dx_m,dt_s,steps,*,method='backward_euler'):
    """Fixed-end 1D diffusion by backward Euler or Crank-Nicolson.

    Neither model includes material-dependent properties or real-world heating.
    Crank-Nicolson is linearly stable but can have sign oscillations for large r.
    """
    u=_vector(initial,'initial',2049)
    if len(u)<3:raise ReferenceDomainError('need two boundaries and >=1 interior point')
    alpha=_positive(alpha_m2_s,'alpha_m2_s');dx=_positive(dx_m,'dx_m');dt=_positive(dt_s,'dt_s')
    if type(steps) is not int or not 0<=steps<=10000:raise ReferenceDomainError('steps must be integer 0..10000')
    if method not in ('backward_euler','crank_nicolson') or type(method) is not str:
        raise ReferenceDomainError('unsupported heat stepping method')
    r=alpha*dt/(dx*dx)
    if not isfinite(r) or r>1e12:
        raise ReferenceDomainError('time-step stiffness outside bounded scale')
    n=len(u)-2
    if method=='backward_euler':
        diag=[1+2*r]*n;side=[-r]*(n-1)
    else:
        diag=[1+r]*n;side=[-r/2]*(n-1)
    initial_sum=fsum(u[1:-1])
    for _ in range(steps):
        if method=='backward_euler':
            rhs=u[1:-1]
            rhs[0]+=r*u[0];rhs[-1]+=r*u[-1]
        else:
            rhs=[u[i]+0.5*r*(u[i-1]-2*u[i]+u[i+1]) for i in range(1,len(u)-1)]
            rhs[0]+=0.5*r*u[0];rhs[-1]+=0.5*r*u[-1]
        u=[u[0]]+tridiagonal_solve(side,diag,side,rhs)+[u[-1]]
    return {'state':u,'fourier_number':r,'time_s':dt*steps,
            'integrated_interior_change':dx*(fsum(u[1:-1])-initial_sum),
            'method':method,
            'limits':'1D linear constant diffusivity, fixed boundaries; CN may oscillate at large Fourier number'}
