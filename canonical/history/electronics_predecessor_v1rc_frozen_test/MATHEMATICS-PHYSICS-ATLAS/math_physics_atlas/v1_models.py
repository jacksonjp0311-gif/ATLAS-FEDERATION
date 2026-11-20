"""ATLAS FORGE v1 candidate: bounded steady 1-D coupled semiconductor equations.

Research-only *dimensionless* Poisson + electron and hole continuity with
Scharfetter-Gummel finite volumes and Dirichlet contacts. Equilibrium or steady
zero generation/recombination only. No transient, interface traps, high-field,
quantum, heat, measured mobility, or experimentally calibrated predictions.

Nondimensional equations on x in [0,1]:
    -lambda_sq * u_xx = p - n + C(x)
    (F_n)_x = (F_p)_x = 0
    F_n = -Dn*n_x + Dn*n*u_x, F_p = -Dp*p_x - Dp*p*u_x.

Here n,p,C are scaled by N_ref; u=qV/(k_B T); x=X/L.
A physical particle flux is F_dimless * (D_phys * N_ref/L), provided the
respective D passed to the dimensionless solver is D_phys/D_ref.
The constants q and k_B are exact SI defining constants, not fitted parameters.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import exp, isfinite
from .v05_models import bernoulli_bounded

class DomainError(ValueError):
    pass


def number(x, label):
    if type(x) not in (int, float):
        raise DomainError(f'{label}: real scalar required')
    try: y=float(x)
    except (ValueError, OverflowError) as e: raise DomainError(f'{label}: invalid') from e
    if not isfinite(y): raise DomainError(f'{label}: nonfinite')
    return y


def thomas(lower, diag, upper, rhs):
    """Bounded diagonally dominant tridiagonal solve without an external library."""
    m=len(diag)
    if not (m and m==len(lower)==len(upper)==len(rhs)):raise DomainError('tridiagonal shape')
    c=[0.]*m;d=[0.]*m
    for k in range(m):
        pivot=diag[k]-(lower[k]*c[k-1] if k else 0.)
        if not isfinite(pivot) or pivot<=1e-300:raise DomainError('singular or nonpositive pivot')
        c[k]=upper[k]/pivot if k+1<m else 0.
        d[k]=(rhs[k]-(lower[k]*d[k-1] if k else 0.))/pivot
    x=[0.]*m
    for k in range(m-1,-1,-1):x[k]=d[k]-(c[k]*x[k+1] if k+1<m else 0.)
    if not all(isfinite(z) for z in x):raise DomainError('nonfinite tridiagonal solution')
    return x


@dataclass(frozen=True)
class Device1D:
    interior:int
    lambda_sq:float
    doping:tuple[float,...]
    voltage:tuple[float,float]
    electrons:tuple[float,float]
    holes:tuple[float,float]
    diff_e:float
    diff_h:float
    h:float


def device_problem(interior, lambda_sq, doping=0.0, voltage=(0.,0.),
                   electrons=(1.,1.), holes=(1.,1.), diff_e=1., diff_h=1.):
    """Create a dimensionless n-cell, fixed-contact, isothermal 1D problem."""
    if type(interior) is not int or not 2<=interior<=128:raise DomainError('interior cells 2..128 integer')
    l=number(lambda_sq,'lambda_sq')
    if not 1e-5<=l<=1e5:raise DomainError('lambda_sq outside supported range')
    def pair(z,label,positive=False):
        if not isinstance(z,(list,tuple)) or len(z)!=2:raise DomainError(label+' boundary pair required')
        a,b=(number(x,label) for x in z)
        if positive and not(1e-10<=a<=1e6 and 1e-10<=b<=1e6):raise DomainError(label+' contact density out of bounds')
        if not positive and max(abs(a),abs(b))>15:raise DomainError(label+' voltage outside 15 thermal units')
        return a,b
    v=pair(voltage,'voltage');n=pair(electrons,'electron',True);p=pair(holes,'hole',True)
    en=number(diff_e,'D_e');ep=number(diff_h,'D_h')
    if not (1e-8<=en<=1e4 and 1e-8<=ep<=1e4):raise DomainError('diffusion coefficient range')
    if type(doping) in (float,int):c=tuple(number(doping,'doping') for _ in range(interior))
    elif isinstance(doping,(list,tuple)) and len(doping)==interior:c=tuple(number(x,'doping') for x in doping)
    else:raise DomainError('doping scalar or interior vector required')
    if any(abs(x)>1e6 for x in c):raise DomainError('doping too large for bounded reference')
    return Device1D(interior,l,c,v,n,p,en,ep,1./(interior+1))


def carrier_linear_system(u,contacts, *, charge_sign=1):
    """SG finite volume A x=b for electrons (sign +) or holes (sign -)."""
    if charge_sign not in (-1,1):raise DomainError('carrier sign')
    m=len(u)-2
    if m<2:raise DomainError('grid')
    if len(contacts)!=2:raise DomainError('contacts')
    lower=[0.]*m;diag=[0.]*m;upper=[0.]*m;rhs=[0.]*m
    for j in range(m):
        left=charge_sign*(u[j+1]-u[j]);right=charge_sign*(u[j+2]-u[j+1])
        if max(abs(left),abs(right))>40:raise DomainError('potential jump outside bounded SG regime')
        # edge F_{i+1/2} = B(-du)*density_i-B(du)*density_{i+1}
        al=bernoulli_bounded(-left);bl=bernoulli_bounded(left)
        ar=bernoulli_bounded(-right);br=bernoulli_bounded(right)
        diag[j]=bl+ar
        if j:lower[j]=-al
        else:rhs[j]+=al*contacts[0]
        if j+1<m:upper[j]=-br
        else:rhs[j]+=br*contacts[1]
    return lower,diag,upper,rhs


def solve_carriers(u, contacts, sign):
    vals=thomas(*carrier_linear_system(u,contacts,charge_sign=sign))
    if any(x<0 or x>1e8 or not isfinite(x) for x in vals):raise DomainError('nonphysical carrier state')
    return [contacts[0]]+vals+[contacts[1]]


def solve_poisson(prob, n, p):
    m=prob.interior;c=prob.lambda_sq/(prob.h*prob.h)
    lower=[0.]+[-c]*(m-1);upper=[-c]*(m-1)+[0.];diag=[2*c]*m
    rhs=[p[i+1]-n[i+1]+prob.doping[i] for i in range(m)]
    rhs[0]+=c*prob.voltage[0];rhs[-1]+=c*prob.voltage[1]
    u=thomas(lower,diag,upper,rhs)
    if any(abs(z)>30 for z in u):raise DomainError('potential leaves safe Boltzmann regime')
    return [prob.voltage[0]]+u+[prob.voltage[1]]


def edge_fluxes(u, densities, D, sign, h):
    """Dimensionless particle flow to the right; zero iff density ratio=e^(sign*du)."""
    return [D/h*(bernoulli_bounded(-sign*(u[i+1]-u[i]))*densities[i]
                 -bernoulli_bounded(sign*(u[i+1]-u[i]))*densities[i+1])
            for i in range(len(u)-1)]


def defects(prob, u, n, p):
    h=prob.h;c=prob.lambda_sq/h**2
    poisson=[c*(2*u[i+1]-u[i]-u[i+2])-(p[i+1]-n[i+1]+prob.doping[i]) for i in range(prob.interior)]
    fn=edge_fluxes(u,n,prob.diff_e,1,h)
    fp=edge_fluxes(u,p,prob.diff_h,-1,h)
    return {'poisson':max(abs(v) for v in poisson),'electron_conservation':max(abs(fn[i]-fn[i+1]) for i in range(len(fn)-1)),
            'hole_conservation':max(abs(fp[i]-fp[i+1]) for i in range(len(fp)-1)),
            'electron_flux':tuple(fn),'hole_flux':tuple(fp),
            'charge_gauss_balance':abs(c*((u[1]-u[0])-(u[-1]-u[-2]))-sum(p[i+1]-n[i+1]+prob.doping[i] for i in range(prob.interior)))}


@dataclass(frozen=True)
class DeviceSolution:
    potential:tuple[float,...]
    electrons:tuple[float,...]
    holes:tuple[float,...]
    iterations:int
    residuals:dict
    converged:bool


def solve_device(prob:Device1D, *, tol=1e-10, maxiter=250, relax=0.5):
    """Block Gummel iteration. Never silently succeeds on failed convergence.

    This is a solver on a bounded model domain, not a general semiconductor
    device solver; extreme coupled doping/bias can be rejected as unresolvable.
    """
    tol=number(tol,'tol');relax=number(relax,'relax')
    if not 1e-13<=tol<=1e-4:raise DomainError('tol outside tested range')
    if type(maxiter) is not int or not 1<=maxiter<=10000:raise DomainError('maxiter')
    if not 0<relax<=1:raise DomainError('relaxation in (0,1]')
    m=prob.interior
    u=[prob.voltage[0]+(prob.voltage[1]-prob.voltage[0])*i/(m+1) for i in range(m+2)]
    for it in range(1,maxiter+1):
        n=solve_carriers(u,prob.electrons,+1);p=solve_carriers(u,prob.holes,-1)
        u_new=solve_poisson(prob,n,p)
        step=max(abs(a-b) for a,b in zip(u,u_new))
        u=[a+relax*(b-a) if 0<i<m+1 else a for i,(a,b) in enumerate(zip(u,u_new))]
        if max(abs(x) for x in u)>20:raise DomainError('iterate beyond bounded voltage')
        n=solve_carriers(u,prob.electrons,+1);p=solve_carriers(u,prob.holes,-1)
        res=defects(prob,u,n,p)
        scale=max(1.,max(abs(x) for x in n+p),max(abs(x) for x in res['electron_flux']+res['hole_flux']))
        normalized=max(res['poisson'],res['electron_conservation'],res['hole_conservation'])/scale
        if normalized<=tol and step<=tol*max(1.,max(abs(x) for x in u))/relax:
            return DeviceSolution(tuple(u),tuple(n),tuple(p),it,res,True)
    raise DomainError('explicit nonconvergence: max iterations reached')


def physical_scaling(temperature_K, length_m, permittivity_F_per_m, reference_density_per_m3, mobility_m2_per_Vs=0.1):
    """Convert SI metrology into dimensionless Poisson scale and Einstein D.

    Nondegenerate Einstein relation is assumed, not generally valid at high
    doping/field. The SI defining constants are exact by definition.
    """
    T=number(temperature_K,'T');L=number(length_m,'L');eps=number(permittivity_F_per_m,'eps')
    N=number(reference_density_per_m3,'N');mu=number(mobility_m2_per_Vs,'mu')
    if not(100<=T<=800 and 1e-10<=L<=1e-1 and 1e-14<=eps<=1e-7 and 1e8<=N<=1e26 and 1e-8<=mu<=10):
        raise DomainError('unsupported physical scale')
    q=1.602176634e-19;kB=1.380649e-23
    vt=kB*T/q
    lam=eps*vt/(q*N*L**2)
    if not isfinite(lam) or not 1e-5<=lam<=1e5:raise DomainError('dimensionless Debye scale outside tested range')
    return {'thermal_voltage_V':vt,'lambda_sq':lam,'diffusion_m2_per_s':mu*vt,
            'charge_C':q,'boltzmann_J_per_K':kB,'electron_flux_scale_per_m2s':mu*vt*N/L,
            'current_density_scale_A_per_m2':q*mu*vt*N/L}


def manufactured_equilibrium(n, slope=0.6, intercept=-0.1, electron_density=0.8, hole_density=1.3):
    """Exact discrete equilibrium benchmark: u=a+b*x; n=N exp(u), p=P exp(-u), C=n-p."""
    if type(n) is not int or not 2<=n<=128:raise DomainError('n')
    a=number(intercept,'a');b=number(slope,'b');N=number(electron_density,'N');P=number(hole_density,'P')
    if not (abs(a)+abs(b)<=6 and 1e-8<=N,P<=1e4):raise DomainError('manufactured parameters')
    u=[a+b*i/(n+1) for i in range(n+2)]
    nv=[N*exp(v) for v in u];pv=[P*exp(-v) for v in u]
    doping=tuple(nv[i]-pv[i] for i in range(1,n+1))
    return device_problem(n,1.,doping,(u[0],u[-1]),(nv[0],nv[-1]),(pv[0],pv[-1])),tuple(u),tuple(nv),tuple(pv)
