"""Materials Atlas v1: transparent, input-bounded reference calculations.

No source text is executable, no source data are authenticated by these functions,
and no result is a materials qualification, safety recommendation, or new measurement.
Requires only the Python standard library.
"""
from __future__ import annotations
from math import exp, log, isfinite, log1p, expm1

# A small factual parameter set from NIST SRD69, copper solid Shomate representation;
# Chase 1998, data reviewed June 1977. NIST identifies a 298--1358 K fitted domain.
# Source: https://webbook.nist.gov/cgi/inchi?ID=C7440508&Table=on&Type=JANAFS
# NIST describes a rights-reserved data compilation. No table/full publication mirrored.
_CU_SOLID = None  # Source coefficients withheld pending SRD69 clearance.


def _number(name, v, *, positive=False, nonnegative=False):
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not isfinite(v):
        raise ValueError(f'{name} must be a finite numerical scalar')
    if positive and v <= 0:
        raise ValueError(f'{name} must be strictly positive')
    if nonnegative and v < 0:
        raise ValueError(f'{name} must be nonnegative')
    return float(v)


def copper_solid_shomate(T_kelvin: float):
    """Published-fit evaluation only, 298 <= T <= 1358 K.

    Returns Cp J/(mol K), H(T)-H(298.15) kJ/mol and S J/(mol K).
    The source coefficient rounding yields a tiny nonzero H at 298.15 K.
    This is a NIST compilation fit, not a fresh thermochemical measurement.
    """
    raise ValueError('NIST SRD69 redistribution clearance pending; inputs and direct numerical outputs withheld from this public derivative.')  # SRD69_PUBLIC_DERIVATIVE
    T = _number('T_kelvin', T_kelvin, positive=True)
    if not 298 <= T <= 1358:
        raise ValueError('solid copper Shomate fit published for 298--1358 K only')
    A, B, C, D, E, F, G, H = _CU_SOLID
    t = T / 1000
    cp = A + B*t + C*t*t + D*t**3 + E/t**2
    enthalpy = A*t + B*t*t/2 + C*t**3/3 + D*t**4/4 - E/t + F - H
    entropy = A*log(t) + B*t + C*t*t/2 + D*t**3/3 - E/(2*t*t) + G
    return {'temperature_K':T, 'Cp_J_per_mol_K':cp,
            'H_relative_29815_kJ_per_mol':enthalpy,'S_J_per_mol_K':entropy,
            'source':'NIST WebBook SRD69 copper solid Shomate (Chase 1998)',
            'origin':'publisher_compilation_parametric_reproduction',
            'domain':'solid phase, fitted 298--1358 K; not uncertainty-certified',
            'limitations':['coefficients are rounded in publisher display',
                            'not transferable to an unspecified copper alloy or specimen',
                            'no latent heat or solid-to-liquid phase switching']}


def copper_enthalpy_change(T1_kelvin:float,T2_kelvin:float):
    p=copper_solid_shomate(T1_kelvin);q=copper_solid_shomate(T2_kelvin)
    return {'delta_H_kJ_per_mol':q['H_relative_29815_kJ_per_mol']-p['H_relative_29815_kJ_per_mol'],
            'T_start_K':p['temperature_K'],'T_end_K':q['temperature_K'],
            'limitations':['only same solid-phase published fit','no phase-boundary crossing']}


def corrosion_uniform_loss_mm_year(mass_loss_g:float,exposed_area_cm2:float,
                                   duration_h:float,density_g_cm3:float):
    """Average equivalent penetration inferred from corrected mass loss.

    Converts W/(rho*A) cm to mm, scaled by 8760 h/year (365 days).
    Does not reveal localized pitting, under-deposit attack or equipment life.
    """
    W=_number('mass_loss_g',mass_loss_g,nonnegative=True)
    area=_number('exposed_area_cm2',exposed_area_cm2,positive=True)
    hours=_number('duration_h',duration_h,positive=True)
    density=_number('density_g_cm3',density_g_cm3,positive=True)
    mm_per_year=(W/area/density)*10*8760/hours
    if not isfinite(mm_per_year):raise ValueError('nonfinite rate: input scale outside representable range')
    return {'equivalent_uniform_penetration_mm_per_year':mm_per_year,
            'assumptions':['corrected mass loss of coupon in grams','constant exposed area',
                           'known actual specimen density','average equivalent uniform loss'],
            'not_inferred':['maximum pit depth','localized corrosion morphology',
                            'field corrosion rate','remaining useful life'],
            'origin':'mass_volume_geometry_model_not_physical_observation'}


def series_conduction(layers, area_m2:float,delta_temperature_K:float,
                      contact_resistances_K_per_W=()):
    """Steady 1D, lateral-insulated conduction through a declared layer stack.

    Each layer = (thickness_m, conductivity_W_per_m_K); contact R in K/W.
    Returns heat rate in watts, *not* surface temperature, stress or lifecycle.
    """
    A=_number('area_m2',area_m2,positive=True)
    DT=_number('delta_temperature_K',delta_temperature_K)
    if not isinstance(layers,(tuple,list)) or not layers:raise ValueError('at least one layer required')
    resistances=[]
    for i,item in enumerate(layers):
        if len(item)!=2: raise ValueError('layer must supply thickness and conductivity')
        L=_number(f'layer_{i}_thickness_m',item[0],positive=True)
        k=_number(f'layer_{i}_conductivity_W_m_K',item[1],positive=True)
        resistances.append(L/(k*A))
    for i,rc in enumerate(contact_resistances_K_per_W):
        resistances.append(_number(f'contact_resistance_{i}',rc,nonnegative=True))
    total=sum(resistances)
    if not total or not isfinite(total):raise ValueError('thermal resistance must be finite and positive')
    Q=DT/total
    if not isfinite(Q):raise ValueError('nonfinite heat rate, input scale outside model range')
    return {'thermal_resistance_K_per_W':total,'heat_rate_W':Q,
            'layer_resistances_K_per_W':resistances[:len(layers)],
            'assumptions':['steady 1D plane-parallel conduction','constant stated conductivities',
                           'no internal heat generation','no unmodeled contact resistance or convection'],
            'not_inferred':['transient thermal history','actual interface temperature',
                            'mechanical thermal stress or service life']}


def avrami_isothermal(rate_constant_per_s:float,exponent:float,time_s:float):
    """JMAK phenomenological fraction at one constant temperature.

    X=1-exp(-(k*t)^n), only if calibrated for the state and isothermal path.
    Does not extrapolate to arbitrary heating/cooling protocols.
    """
    k=_number('rate_constant_per_s',rate_constant_per_s,positive=True)
    n=_number('exponent',exponent,positive=True)
    t=_number('time_s',time_s,nonnegative=True)
    if t==0:
        x=0.0
    else:
        log_z=n*(log(k)+log(t))
        # Avoid overflow and cancellation. Report numerical saturation as an ideal-model
        # limit, NOT proof of physically complete transformation.
        x=1.0 if log_z>40 else -expm1(-exp(log_z))
    return {'fraction_transformed':x,'time_s':t,
            'origin':'isothermal_phenomenological_model',
            'limitations':['model parameters must be fitted for the particular material/state',
                           'no continuous cooling, grain-size or mechanism inference',
                           'does not account for impingement beyond fitted model',
                           'rounded fraction one may be numerical saturation, not physical completion']}


def avrami_time_to_fraction(rate_constant_per_s:float,exponent:float,desired_fraction:float):
    k=_number('rate_constant_per_s',rate_constant_per_s,positive=True)
    n=_number('exponent',exponent,positive=True)
    x=_number('desired_fraction',desired_fraction)
    if not 0<x<1:raise ValueError('desired_fraction must be strictly between zero and one')
    return (-log1p(-x))**(1/n)/k


def norton_steady_creep(stress_MPa:float,temperature_K:float,
                        prefactor_per_s_MPa_to_minus_n:float,
                        stress_exponent:float,activation_energy_J_per_mol:float,
                        duration_s:float):
    """Norton Arrhenius steady-rate model, not a creep rupture calculation.

    epsdot=A*(sigma in MPa)^n*exp(-Q/(R*T)). A carries MPa^-n s^-1.
    Only a homogeneous constant-stress, constant-T steady-regime estimate.
    """
    sigma=_number('stress_MPa',stress_MPa,positive=True)
    T=_number('temperature_K',temperature_K,positive=True)
    A=_number('prefactor',prefactor_per_s_MPa_to_minus_n,positive=True)
    n=_number('stress_exponent',stress_exponent,positive=True)
    Q=_number('activation_energy_J_per_mol',activation_energy_J_per_mol,nonnegative=True)
    seconds=_number('duration_s',duration_s,nonnegative=True)
    log_rate=log(A)+n*log(sigma)-Q/(8.31446261815324*T)
    if log_rate < -740:raise ValueError('strain-rate magnitude underflows float; cannot report zero')
    if log_rate > 700:raise ValueError('strain-rate magnitude overflows float; invalid model regime')
    rate=exp(log_rate)
    strain_increment=rate*seconds
    if not isfinite(strain_increment):raise ValueError('computed strain increment overflow')
    return {'model_steady_strain_rate_per_s':rate,'model_steady_strain_increment':strain_increment,
            'origin':'assumed_steady_creep_kinetic_model',
            'limitations':['parameters must be fitted to material and service regime',
                           'no primary or tertiary creep','no damage/rupture-time prediction',
                           'constant stress and temperature and in-regime use only']}


def conditional_weakest_link_survival(stress_MPa:float,reference_scale_MPa:float,
                                      weibull_shape:float,component_volume_mm3:float,
                                      reference_volume_mm3:float,
                                      *, physical_weakest_link_assumed:bool=False):
    """Conditional volume scaling; NOT the ordinary empirical Weibull CDF alone.

    Requires explicit hypothesis of independent equal flaw-population subvolumes.
    Area/surface flaw models need different scaling and cannot use this model.
    """
    if physical_weakest_link_assumed is not True:
        raise ValueError('explicit physical_weakest_link_assumed=True is required; empirical Weibull fits do not establish size scaling')
    sig=_number('stress_MPa',stress_MPa,nonnegative=True)
    scale=_number('reference_scale_MPa',reference_scale_MPa,positive=True)
    shape=_number('weibull_shape',weibull_shape,positive=True)
    v=_number('component_volume_mm3',component_volume_mm3,positive=True)
    v0=_number('reference_volume_mm3',reference_volume_mm3,positive=True)
    if sig==0:
        hazard=0.0
    else:
        log_h=shape*(log(sig)-log(scale))+log(v)-log(v0)
        if log_h>700:raise ValueError('conditional hazard numerical overflow; not physically interpretable')
        hazard=exp(log_h)
    survival=exp(-hazard)
    return {'conditional_survival_probability':survival,
            'conditional_failure_probability':-expm1(-hazard),
            'origin':'declared_independent_volume_weakest_link_model',
            'limitations':['flaw population stationarity and independent subvolumes unverified',
                           'stress assumed spatially uniform','surface-limited flaws excluded',
                           'not an empirical component reliability qualification']}
