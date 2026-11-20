"""Cubic powder peak-to-lattice calculation with uncertainty propagation.

This uses already indexed, user-supplied 2theta peaks and externally known
wavelength. No diffraction profile fitting, automatic indexing, crystallographic
phase solution, instrument offset correction or sample identification.
"""
from __future__ import annotations
import math
from typing import Sequence
from .methods import MaterialsInputError, _finite, _positive


def cubic_peak_lattice(*,wavelength_angstrom:float, h:int,k:int,l:int,
        two_theta_deg:float,order:int=1)->dict:
    wave=_positive('wavelength_angstrom',wavelength_angstrom)
    if type(order) is not int or order!=1:
        raise MaterialsInputError('this peak-indexing convention supports first-order hkl reflections only')
    if not all(type(q) is int for q in [h,k,l]):raise MaterialsInputError('hkl indices must be integers')
    N=h*h+k*k+l*l
    if not N or N>10000:raise MaterialsInputError('hkl must be nonzero and bounded')
    tw=_finite('two_theta_deg',two_theta_deg)
    if not 0<tw<180:raise MaterialsInputError('2theta must be between 0 and 180 degrees')
    theta=math.radians(tw/2)
    d=wave/(2*math.sin(theta))
    a=d*math.sqrt(N)
    if not math.isfinite(a):raise MaterialsInputError('lattice parameter overflow')
    return {'lattice_parameter_angstrom':a,'d_spacing_angstrom':d,'hkl':[h,k,l],
        'two_theta_deg':tw,'wavelength_angstrom':wave,'model':'first_order_bragg_cubic_metric',
        'limitations':['Requires externally justified cubic phase, indexing, first-order assignment and wavelength',
        'No background/peak-profile fit, phase identification, microstrain, refraction or instrument zero-offset correction']}


def cubic_lattice_from_indexed_peaks(*,wavelength_angstrom:float,
    wavelength_standard_uncertainty_angstrom:float,peaks:Sequence[dict])->dict:
    """Inverse-variance weighted a with independent random angle errors.

    Wavelength uncertainty is treated as one fully shared component; it is
    combined with statistical angular uncertainty only once, *not* per peak.
    The result is NOT a validated crystallographic refinement.
    """
    wave=_positive('wavelength_angstrom',wavelength_angstrom)
    uw=_finite('wavelength_standard_uncertainty_angstrom',wavelength_standard_uncertainty_angstrom)
    if uw<0: raise MaterialsInputError('wavelength uncertainty must be nonnegative')
    if not isinstance(peaks,(list,tuple)) or len(peaks)<3 or len(peaks)>100:
        raise MaterialsInputError('three to 100 independently indexed peaks required')
    rows=[];seen=set()
    for i,p in enumerate(peaks):
        if not isinstance(p,dict): raise MaterialsInputError('peak row must be a dictionary')
        if any(k not in p for k in ['h','k','l','two_theta_deg','u_two_theta_deg']):
            raise MaterialsInputError('peak missing required h,k,l,2theta or its standard uncertainty')
        h,k,l=(p[x] for x in ('h','k','l'))
        peak=cubic_peak_lattice(wavelength_angstrom=wave,h=h,k=k,l=l,two_theta_deg=p['two_theta_deg'])
        family=tuple(sorted([abs(h),abs(k),abs(l)]))
        if family in seen:raise MaterialsInputError('repeated cubic reflection family requires a correlated-error model')
        seen.add(family)
        u2=_positive('u_two_theta_deg',p['u_two_theta_deg'])
        theta=math.radians(peak['two_theta_deg']/2.)
        a=peak['lattice_parameter_angstrom']
        # 2theta in degrees, d(log a)/d(2theta) = -(pi/360) cot(theta).
        sensitivity=abs(a*math.cos(theta)/math.sin(theta)*math.pi/360)
        ua=sensitivity*u2
        if ua<=0 or not math.isfinite(ua):raise MaterialsInputError('angle uncertainty ill conditioned')
        rows.append({'hkl':peak['hkl'],'two_theta_deg':peak['two_theta_deg'],
            'lattice_parameter_angstrom':a,'u_a_angle_angstrom':ua,'u_2theta_deg':u2})
    scales=[r['u_a_angle_angstrom'] for r in rows]
    min_scale=min(scales)
    # Relative weights avoid a possible overflow of 1/u^2.
    weights=[(min_scale/s)**2 for s in scales]
    sw=math.fsum(weights)
    if sw<=0 or not math.isfinite(sw):raise MaterialsInputError('invalid relative precision')
    mean=math.fsum(w*r['lattice_parameter_angstrom'] for w,r in zip(weights,rows))/sw
    ua_rand=min_scale/math.sqrt(sw)
    ua_shared=abs(mean/wave)*uw
    combined=math.hypot(ua_rand,ua_shared)
    chisq=math.fsum(w*((r['lattice_parameter_angstrom']-mean)/min_scale)**2 for w,r in zip(weights,rows))
    if not all(map(math.isfinite,(mean,ua_rand,ua_shared,combined,chisq))):raise MaterialsInputError('nonfinite fit statistic')
    return {'mean_lattice_parameter_angstrom':mean,
        'standard_uncertainty_angle_angstrom':ua_rand,
        'standard_uncertainty_shared_wavelength_angstrom':ua_shared,
        'combined_standard_uncertainty_angstrom':combined,
        'chi_square':chisq,'degrees_of_freedom':len(rows)-1,
        'reduced_chi_square':chisq/(len(rows)-1),'n_reflections':len(rows),'peaks':rows,
        'caveats':['Inputs are independently assigned peaks and their angle standard uncertainties, not a profile refinement',
          'Random angle errors assumed independent; one fully shared wavelength uncertainty counted once',
          'No instrumental calibration offsets, sample displacement, texture, strain, peak overlap or covariance',
          'Chi-square is a diagnostic, not automatic uncertainty inflation or evidence of sample phase identity',
          'Wavelength uncertainty treated by first-order linearization; model valid for small relative uncertainties'],
        'evidence_origin':'user_supplied_indexed_peaks_or_synthetic_teaching_example'}
