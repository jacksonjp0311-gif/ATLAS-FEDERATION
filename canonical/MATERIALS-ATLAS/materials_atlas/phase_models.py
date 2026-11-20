"""A bounded symmetric binary regular-solution model.

This is an explicitly stipulated, finite-temperature, mean-field teaching model.
Do not identify it with an alloy, a CALPHAD assessment, a DFT convex hull,
or a validated manufacturing phase diagram. It assumes one symmetric solution
phase with a constant molar interaction parameter omega.
"""
from __future__ import annotations
import math
from .methods import MaterialsInputError, _finite, _positive
R = 8.31446261815324  # J mol^-1 K^-1


def _inputs(*,temperature_k:float,omega_j_mol:float)->tuple[float,float]:
    t=_positive('temperature_k',temperature_k)
    w=_finite('omega_j_mol',omega_j_mol)
    if w<0: raise MaterialsInputError('this bounded model requires omega_j_mol >= 0; attractive mixing is not evaluated')
    if not math.isfinite(w/(R*t)):raise MaterialsInputError('omega/(RT) is not finite')
    return t,w


def _fraction(x:float)->float:
    z=_finite('mole_fraction_b',x)
    if not 0<z<1:raise MaterialsInputError('0 < mole_fraction_b < 1 required; pure-component limits require separate treatment')
    return z


def regular_solution_energy(*,temperature_k:float,omega_j_mol:float,mole_fraction_b:float)->dict:
    """Return molar mixing Gibbs energy and first/second composition derivatives."""
    t,w=_inputs(temperature_k=temperature_k,omega_j_mol=omega_j_mol)
    x=_fraction(mole_fraction_b)
    rt=R*t
    g=rt*(x*math.log(x)+(1-x)*math.log1p(-x))+w*x*(1-x)
    d1=rt*(math.log(x)-math.log1p(-x))+w*(1-2*x)
    d2=rt/(x*(1-x))-2*w
    if not all(map(math.isfinite,(g,d1,d2))):raise MaterialsInputError('numeric result is nonfinite')
    return {'gibbs_mixing_j_mol':g,'first_derivative_j_mol':d1,
        'second_derivative_j_mol':d2,'mole_fraction_b':x,'temperature_k':t,
        'omega_j_mol':w,'model':'constant_omega_symmetric_regular_solution',
        'limitations':['Mean-field homogeneous solution with ideal entropy, one symmetric phase and constant omega',
                       'G of mixing is relative to pure-component reference and is not an absolute Gibbs energy',
                       'No real phase diagram, kinetic pathway, nucleation barrier or material stability is established']}


def regular_solution_boundaries(*,temperature_k:float,omega_j_mol:float)->dict:
    """Numerical binodal and analytic spinodal of symmetric regular solution.

    The binodal is the *noncentral* zero of derivative g' on (0,x_spinodal).
    For extremely narrow end compositions this double-precision model refuses
    rather than returning a false zero or silently clipping at x=0.
    """
    t,w=_inputs(temperature_k=temperature_k,omega_j_mol=omega_j_mol)
    result={'temperature_k':t,'omega_j_mol':w,
      'model':'constant_omega_symmetric_regular_solution',
      'limitations':['Coexistence assumes equilibrium within a single symmetric regular-solution model',
      'Not an experimental alloy phase diagram, not a kinetic simulation, not a computed materials-project phase hull',
      'No nucleation rates, phase-interface energy, interfacial or elastic penalty modeled']}
    if w==0:
        return dict(result,phase_regime='single_phase_all_compositions',critical_temperature_k=None,
                    binodal_mole_fraction_b=None,spinodal_mole_fraction_b=None)
    critical=w/(2*R)
    result['critical_temperature_k']=critical
    if t>=critical:
        return dict(result,phase_regime='single_phase_all_compositions',binodal_mole_fraction_b=None,spinodal_mole_fraction_b=None)
    q=2*R*t/w
    sq=math.sqrt(max(0.,1-q))
    # Cancellation-resistant lower spinodal root.
    sp_lo=q/(2*(1+sq));sp_hi=1-sp_lo
    # A well-conditioned *physical* root must be distinct from x=0 in double precision.
    lo=1e-14
    if sp_lo<=lo:
        raise MaterialsInputError('binodal/spinodal too near zero to resolve at this precision')
    def grad(x):return R*t*(math.log(x)-math.log1p(-x))+w*(1-2*x)
    g_lo=grad(lo);g_hi=grad(sp_lo)
    if not g_lo<0<g_hi:
        raise MaterialsInputError('binodal not numerically resolvable with the required bracket; refuse')
    hi=sp_lo
    # Bisection avoids derivative-zero attraction to x=0.5.
    for _ in range(160):
        mid=(lo+hi)*.5
        if grad(mid)>0:hi=mid
        else:lo=mid
    b_lo=(lo+hi)*.5
    return dict(result,phase_regime='miscibility_gap',
        binodal_mole_fraction_b=[b_lo,1-b_lo],
        spinodal_mole_fraction_b=[sp_lo,sp_hi],
        binodal_stationarity_residual_j_mol=grad(b_lo),
        numerics='bisection_160_steps_noncentral_root_analytic_spinodal')


def regular_solution_state(*,temperature_k:float,omega_j_mol:float,mole_fraction_b:float)->dict:
    """Classify a supplied overall composition and compute equilibrium lever fractions."""
    e=regular_solution_energy(temperature_k=temperature_k,omega_j_mol=omega_j_mol,mole_fraction_b=mole_fraction_b)
    b=regular_solution_boundaries(temperature_k=temperature_k,omega_j_mol=omega_j_mol)
    x=e['mole_fraction_b']
    if b['phase_regime']=='single_phase_all_compositions':
        return {'state':'single_phase_within_model','overall_mole_fraction_b':x,'equilibrium_two_phase_fractions':None,
            'free_energy_drop_to_equilibrium_j_mol':0.0,'boundaries':b,
            'caution':'At critical point, susceptibility diverges in this mean-field model; not a kinetic or test result'}
    a,z=b['binodal_mole_fraction_b'];sa,sz=b['spinodal_mole_fraction_b']
    tol=2e-14
    if x<=a+tol or x>=z-tol:
        status='outside_miscibility_gap_or_on_boundary';frac=None;drop=0.
    else:
        if sa < x < sz:status='spinodal_unstable_homogeneous_state'
        else:status='metastable_homogeneous_state_with_two_phase_lower_energy'
        high=(x-a)/(z-a)
        frac={'low_x_phase':1-high,'high_x_phase':high,'low_x_composition':a,'high_x_composition':z}
        g_a=regular_solution_energy(temperature_k=temperature_k,omega_j_mol=omega_j_mol,mole_fraction_b=a)['gibbs_mixing_j_mol']
        g_z=regular_solution_energy(temperature_k=temperature_k,omega_j_mol=omega_j_mol,mole_fraction_b=z)['gibbs_mixing_j_mol']
        mix=(1-high)*g_a+high*g_z
        drop=e['gibbs_mixing_j_mol']-mix
        if drop < -1e-8:raise MaterialsInputError('two-phase state unexpectedly increases energy; numeric method refused')
    return {'state':status,'overall_mole_fraction_b':x,'homogeneous_curvature_j_mol':e['second_derivative_j_mol'],
            'equilibrium_two_phase_fractions':frac,'free_energy_drop_to_equilibrium_j_mol':max(drop,0),
            'boundaries':b,'caution':'Positive curvature alone does not imply global thermodynamic stability inside the binodal'}
