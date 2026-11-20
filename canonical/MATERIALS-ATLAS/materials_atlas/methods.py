"""Materials Atlas 0.1: bounded, typed numerical teaching utilities.

Pure calculations. None certifies material properties, phase identity, or safety.
"""
from __future__ import annotations
from math import isfinite, sin, radians
from collections.abc import Sequence

class MaterialsInputError(ValueError):
    """Required physical metadata, range, or numerical conditions are invalid."""

def _finite(name: str, value: float) -> float:
    if type(value) not in (float, int) or not isfinite(value):
        raise MaterialsInputError(f'{name} must be a finite real number')
    return float(value)

def _positive(name: str, v: float) -> float:
    x = _finite(name, v)
    if x <= 0: raise MaterialsInputError(f'{name} must be positive')
    return x

def lattice_density(*, atomic_mass_g_per_mol: float, atoms_per_cell: int, cubic_a_angstrom: float) -> dict:
    """Mass / volume for a supplied cubic lattice and supplied composition.
    It is not an experimental identification of structure or chemical species.
    """
    mass = _positive('atomic_mass_g_per_mol', atomic_mass_g_per_mol)
    a = _positive('cubic_a_angstrom', cubic_a_angstrom)
    if type(atoms_per_cell) is not int or not 1 <= atoms_per_cell <= 10000:
        raise MaterialsInputError('atoms_per_cell must be a positive integer')
    avogadro = 6.02214076e23  # SI-defining exact constant
    volume_cm3 = (a * 1e-8) ** 3
    density = (atoms_per_cell * mass / avogadro) / volume_cm3
    if not isfinite(density) or density <= 0: raise MaterialsInputError('overflow or underflow')
    return {'density_g_cm3': density,'inputs_given_not_measured': True,
            'assumptions':['Cubic cell','All sites represented by stated average atomic mass','No defects or porosity represented']}

def bragg_spacing(*, wavelength_angstrom: float, two_theta_degrees: float, order: int = 1) -> dict:
    """n*lambda=2*d*sin(theta). Input is full 2theta diffraction angle."""
    wave = _positive('wavelength_angstrom', wavelength_angstrom)
    angle = _finite('two_theta_degrees', two_theta_degrees)
    if not 0 < angle < 180: raise MaterialsInputError('require 0 < 2theta < 180 deg')
    if type(order) is not int or order < 1: raise MaterialsInputError('order must be positive integer')
    spacing = order*wave/(2*sin(radians(angle/2)))
    if not isfinite(spacing): raise MaterialsInputError('nonfinite result')
    return {'d_angstrom':spacing,'theta_degrees':angle/2,
            'limitations':['Diffraction peak assignment and order supplied, not inferred','No instrument or refraction corrections']}

def lever_rule(*, overall_fraction_b:float, alpha_fraction_b:float, beta_fraction_b:float) -> dict:
    """Phase fractions from a two-phase equilibrium tie line in one binary composition convention."""
    c0=_finite('overall_fraction_b',overall_fraction_b)
    ca=_finite('alpha_fraction_b',alpha_fraction_b)
    cb=_finite('beta_fraction_b',beta_fraction_b)
    if not (0<=ca < cb<=1 and ca<=c0<=cb):
        raise MaterialsInputError('require ordered 0 <= alpha <= overall <= beta <= 1')
    fb=(c0-ca)/(cb-ca)
    return {'fraction_alpha':1-fb,'fraction_beta':fb,'assumptions':['Binary two-phase equilibrium tie line at specified conditions','All fractions use same compositional basis','Complete mass conservation; no third phase']}

def thermal_mismatch(*, alpha_a_per_k:float,alpha_b_per_k:float,delta_temperature_k:float) -> dict:
    """Free thermal strain mismatch only, not stress or failure prediction."""
    a=_finite('alpha_a_per_k',alpha_a_per_k);b=_finite('alpha_b_per_k',alpha_b_per_k)
    dt=_finite('delta_temperature_k',delta_temperature_k)
    return {'free_strain_difference':(a-b)*dt,'microstrain_difference':(a-b)*dt*1e6,
        'limitations':['Constant scalar coefficients, no temperature dependence or tensor direction','No constraint, stress, fatigue, or interface strength model']}

def engineering_tensile_point(*,force_newtons:float,area_mm2:float,elongation_mm:float,gauge_length_mm:float) -> dict:
    f=_finite('force_newtons',force_newtons);area=_positive('area_mm2',area_mm2)
    e=_finite('elongation_mm',elongation_mm);length=_positive('gauge_length_mm',gauge_length_mm)
    if f < 0 or e < 0:raise MaterialsInputError('teaching tensile case requires nonnegative force and extension')
    return {'engineering_stress_mpa':f/area,'engineering_strain':e/length,
            'limitations':['Initial area and initial gauge length only','Cannot determine modulus, yield or failure strength from one point','No specimen geometry compliance, temperature or strain rate supplied']}

def mixture_modulus_bounds(*, modulus_a_gpa:float, modulus_b_gpa:float, volume_fraction_a:float) -> dict:
    ea=_positive('modulus_a_gpa',modulus_a_gpa);eb=_positive('modulus_b_gpa',modulus_b_gpa)
    v=_finite('volume_fraction_a',volume_fraction_a)
    if not 0<=v<=1:raise MaterialsInputError('volume fraction must be 0..1')
    voigt=v*ea+(1-v)*eb
    reuss=1/(v/ea+(1-v)/eb)
    return {'iso_strain_voigt_gpa':voigt,'iso_stress_reuss_gpa':reuss,
            'assumptions':['Idealized two-phase linear elastic scalar model','No voids, interface degradation or anisotropy included'],
            'limitations':['Not a universal safe stiffness range for arbitrary microstructure, nonlinear loading or anisotropy']}

def formation_energy_per_atom(*,total_energy_ev:float, element_reference_ev_per_atom:dict[str,float], formula_counts:dict[str,int]) -> dict:
    total=_finite('total_energy_ev',total_energy_ev)
    if not isinstance(formula_counts,dict) or not formula_counts or set(formula_counts)!=set(element_reference_ev_per_atom):
        raise MaterialsInputError('identical nonempty elemental keys required')
    n=0; reference=0.0
    for elem,count in formula_counts.items():
        if not isinstance(elem,str) or not elem or type(count) is not int or count<1:raise MaterialsInputError('positive integral stoichiometries required')
        n+=count;reference+=count*_finite(f'reference {elem}',element_reference_ev_per_atom[elem])
    value=(total-reference)/n
    return {'formation_energy_ev_per_atom':value,'atom_count':n,
            'assumptions':['Same energy normalization, functional and compatible correction scheme','Inputs may be computed values; not measured enthalpies'],
            'limitations':['No finite-temperature entropy, pressure, kinetics or synthesis feasibility claim']}

def binary_hull_distance(*, phases: Sequence[dict], candidate_x_b:float,candidate_energy_ev_atom:float) -> dict:
    """Reference-normalized lower convex envelope for a *complete supplied phase set*.

    Includes pure endpoints. Energy is per atom on one common coherent model scale.
    Lower hull at query x = min convex combination of supplied phase pairs.
    Does not infer which real competing phases were omitted.
    """
    x=_finite('candidate_x_b',candidate_x_b); energy=_finite('candidate_energy_ev_atom',candidate_energy_ev_atom)
    if not 0<=x<=1:raise MaterialsInputError('composition x must lie 0..1')
    if not isinstance(phases,(list,tuple)) or len(phases)<2:raise MaterialsInputError('at least two reference phases required')
    rows=[];ident=set()
    for idx,p in enumerate(phases):
        if not isinstance(p,dict) or set(p)!={'id','x_b','energy_ev_atom'}: raise MaterialsInputError('phase requires id,x_b,energy_ev_atom')
        pid=p['id'];xp=_finite('phase x',p['x_b']);ep=_finite('phase energy',p['energy_ev_atom'])
        if not isinstance(pid,str) or not pid or pid in ident or not 0<=xp<=1:raise MaterialsInputError('duplicate/invalid phase ID or composition')
        ident.add(pid);rows.append((pid,xp,ep))
    if not any(q[1]==0 for q in rows) or not any(q[1]==1 for q in rows):
        raise MaterialsInputError('both pure-element endpoints must be supplied')
    best=None
    for p in rows:
        if p[1]==x:
            if best is None or p[2]<best[0]:best=(p[2],[p[0]])
    for i,p in enumerate(rows):
        for q in rows[i+1:]:
            if p[1]==q[1] or not min(p[1],q[1])<=x<=max(p[1],q[1]):continue
            a=(q[1]-x)/(q[1]-p[1]); b=1-a; e=a*p[2]+b*q[2]
            if best is None or e<best[0]:best=(e,[p[0],q[0]])
    if best is None:raise MaterialsInputError('no phase combination brackets composition')
    above=energy-best[0]
    # The submitted candidate need not be among competing phases; signed values permitted.
    return {'hull_energy_ev_per_atom':best[0], 'signed_candidate_minus_hull_ev_atom':above,
            'supporting_phase_ids':best[1],
            'candidate_below_reference_hull':above<-1e-10,
            'scope':'Finite supplied competition set only, at declared common electronic-energy reference',
            'limitations':['A negative distance means phase set is incomplete relative to candidate, not negative real energy-above-hull','No entropy, kinetics, structural stability, synthesis or material safety proven','DFT mixing and release compatibility not checked automatically']}

def compare_properties(a:dict,b:dict) -> dict:
    """Refuse to declare a material winner unless typed metadata agrees.
    Value comparison alone says nothing about application fitness.
    """
    keys={'property','unit','method','temperature_k','direction','condition','origin','value','uncertainty'}
    if not isinstance(a,dict) or not isinstance(b,dict) or set(a)!=keys or set(b)!=keys:
        raise MaterialsInputError('property records must explicitly give identical required metadata fields')
    for key in ('property','unit','method','temperature_k','direction','condition','origin'):
        if a[key]!=b[key]:
            raise MaterialsInputError(f'incompatible observations: {key} differs')
    va=_finite('value a',a['value']);vb=_finite('value b',b['value'])
    ua=_finite('uncertainty a',a['uncertainty']);ub=_finite('uncertainty b',b['uncertainty'])
    if ua<0 or ub<0:raise MaterialsInputError('uncertainty must be nonnegative')
    return {'difference_a_minus_b':va-vb,'note':'Arithmetic only. Coverage/correlation and common covariance unspecified; cannot infer statistical significance or material selection.'}
