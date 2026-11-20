"""Typed, bounded Materials Atlas examples. These are not certification methods.

Only ``published_hahn1_replay`` operates on a transcription of source-reported
experimental observations. Other methods operate on supplied or synthetic data.
"""
from __future__ import annotations
import hashlib
import math
from importlib.resources import files
from typing import Sequence
from .methods import MaterialsInputError, _finite, _positive

H1_BETA = None  # SRD140_PUBLIC_WITHHELD
H1_CERT_RSS = None  # SRD140_PUBLIC_WITHHELD
H1_CERT_RSD = None  # SRD140_PUBLIC_WITHHELD
H1_CERT_DF = None  # SRD140_PUBLIC_WITHHELD


def hahn1_observations():
    raise MaterialsInputError('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')


def hahn1_prediction(temperature_k:float, beta:Sequence[float]|None=None) -> float:
    """NIST's *published* seven-coefficient cubic/cubic rational function.

    Inputs do not imply validity outside observed temperatures. For arbitrary
    coefficient sets the denominator may vanish: reject, never emit infinity.
    """
    if beta is None: raise MaterialsInputError('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
    t=_positive('temperature_k',temperature_k)
    if len(beta)!=7:raise MaterialsInputError('expected seven rational coefficients')
    b=[_finite(f'beta[{i}]',q) for i,q in enumerate(beta)]
    denom=1+t*(b[4]+t*(b[5]+t*b[6]))
    if not math.isfinite(denom) or abs(denom)<1e-14:
        raise MaterialsInputError('rational denominator too close to zero')
    value=(b[0]+t*(b[1]+t*(b[2]+t*b[3])))/denom
    if not math.isfinite(value):raise MaterialsInputError('nonfinite model prediction')
    return value


def published_hahn1_replay():
    raise MaterialsInputError('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')


def arrhenius_diffusivity(*,prefactor_m2_s:float,activation_energy_j_mol:float,temperature_k:float)->dict:
    """One stipulated Arrhenius relation, not material-specific fitting."""
    d0=_positive('prefactor_m2_s',prefactor_m2_s)
    q=_finite('activation_energy_j_mol',activation_energy_j_mol)
    t=_positive('temperature_k',temperature_k)
    if q<0:raise MaterialsInputError('requires nonnegative activation energy')
    if not 1<=t<=10000:raise MaterialsInputError('temperature outside supported numeric demonstration range')
    value=d0*math.exp(-q/(8.31446261815324*t))
    return {'diffusivity_m2_s':value,'temperature_k':t,
     'limitations':['Supplied prefactor and activation energy only; no experiment or fitting',
                    'Single-mode activated transport assumed within a validated phase/range, not established by this calculation',
                    'Cannot equate a thermal acceleration prediction with a safety or aging qualification.']}


def diffusion_rms_1d(*,diffusivity_m2_s:float,seconds:float)->dict:
    d=_finite('diffusivity_m2_s',diffusivity_m2_s);t=_finite('seconds',seconds)
    if d<0 or t<0:raise MaterialsInputError('diffusivity/time cannot be negative')
    return {'rms_displacement_m':math.sqrt(2*d*t),
            'assumptions':['Unbounded 1-D Fickian Brownian displacement with constant D','No gradients, traps, interfaces, phase changes or finite boundaries']}


def fracture_mode_i(*,stress_mpa:float,crack_length_m:float,geometry_factor:float)->dict:
    s=_positive('stress_mpa',stress_mpa);a=_positive('crack_length_m',crack_length_m);y=_positive('geometry_factor',geometry_factor)
    result=y*s*math.sqrt(math.pi*a)
    return {'stress_intensity_mpa_sqrt_m':result,'assumptions':['Linear elastic mode I stress intensity with externally established geometry factor Y','Crack length a uses the same geometric convention as supplied Y'],
           'limitations':['K_I is NOT automatically K_IC or fracture onset','No thickness, plastic-zone, crack-shape, residual stress or test validity established']}


def paris_fatigue_rate(*,delta_k_mpa_sqrt_m:float,c_mm_per_cycle_per_k_power:float,exponent_m:float,valid_delta_k_min:float,valid_delta_k_max:float)->dict:
    dk=_positive('delta_k_mpa_sqrt_m',delta_k_mpa_sqrt_m)
    C=_positive('c_mm_per_cycle_per_k_power',c_mm_per_cycle_per_k_power)
    m=_positive('exponent_m',exponent_m)
    lo=_positive('valid_delta_k_min',valid_delta_k_min);hi=_positive('valid_delta_k_max',valid_delta_k_max)
    if lo>=hi or not lo<=dk<=hi:raise MaterialsInputError('delta K outside supplied validated Paris regime')
    try:value=C*dk**m
    except OverflowError as e:raise MaterialsInputError('numeric overflow') from e
    if not math.isfinite(value):raise MaterialsInputError('numeric overflow')
    return {'crack_growth_rate_mm_per_cycle':value,
            'coefficient_unit_interpretation':f'mm/cycle / (MPa sqrt(m))^{m:g}',
            'limitations':['Only given empirical Paris-regime constants; no fatigue threshold or instability model',
                           'Cannot integrate full component fatigue life without crack geometry, load history and remaining regimes']}


def engineering_true_before_necking(*,engineering_stress_mpa:float,engineering_strain:float,uniform_deformation_assumed:bool)->dict:
    sig=_finite('engineering_stress_mpa',engineering_stress_mpa)
    e=_finite('engineering_strain',engineering_strain)
    if sig<0 or e<0:raise MaterialsInputError('nonnegative tensile stress/strain required')
    if uniform_deformation_assumed is not True:
        raise MaterialsInputError('refuse conversion absent stated uniform deformation assumption')
    return {'true_stress_mpa':sig*(1+e),'true_log_strain':math.log1p(e),
            'limitations':['Only before diffuse necking under approximately uniform uniaxial deformation and plastic incompressibility',
                           'No post-necking area correction, elastic/plastic decomposition, machine compliance or failure prediction']}


def linear_thermal_strain_path(*,temperature_k:Sequence[float],alpha_per_k:Sequence[float],reference_temperature_k:float)->dict:
    """Trapezoid integrate a supplied expansion-coefficient curve, no inferred units.

    Use when alpha is known as reciprocal kelvin; NIST Hahn1 response units are
    NOT resolved, so do not pass Hahn1 values into this tool as physical alpha.
    """
    if not isinstance(temperature_k,(list,tuple)) or not isinstance(alpha_per_k,(list,tuple)) or len(temperature_k)!=len(alpha_per_k) or len(temperature_k)<2:
        raise MaterialsInputError('equal-length arrays with >=2 points required')
    xs=[_positive('temperature',z) for z in temperature_k]
    ys=[_finite('thermal coefficient',z) for z in alpha_per_k]
    if any(xs[i]>=xs[i+1] for i in range(len(xs)-1)):raise MaterialsInputError('temperatures must increase strictly')
    if reference_temperature_k!=xs[0]:raise MaterialsInputError('reference temperature must match first sample')
    integ=math.fsum((xs[i+1]-xs[i])*(ys[i]+ys[i+1])*.5 for i in range(len(xs)-1))
    if not math.isfinite(integ) or abs(integ)>700:raise MaterialsInputError('numeric integral outside finite exponential range')
    return {'integrated_log_length_change':integ,'length_ratio_exp_integral':math.exp(integ),
            'small_strain_approximation':integ,
            'limitations':['Piecewise-linear alpha(T), trapezoidal quadrature, no extrapolation','Assumes alpha=d(ln L)/dT; no specimen, direction, hysteresis, uncertainty or instrument effects']}
