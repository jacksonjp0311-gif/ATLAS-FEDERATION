"""Eight transparent Materials Atlas v1 investigations; no new experiments."""
from .v1_methods import (copper_solid_shomate,copper_enthalpy_change,
    corrosion_uniform_loss_mm_year,series_conduction,avrami_isothermal,
    avrami_time_to_fraction,norton_steady_creep,conditional_weakest_link_survival)

# Selected rounded NIST publisher display points for computational checks,
# NOT copied full source table and NOT original source-file bytes.
# URL: https://webbook.nist.gov/cgi/inchi?ID=C7440508&Table=on&Type=JANAFS
NIST_CU_CHECKS = None  # SRD69_PUBLIC_DERIVATIVE

def _rejects(f,*a,**kw):
    try: f(*a,**kw)
    except ValueError:return True
    return False

def v1_casebook():
    cases=[]
    cases.extend([{'id': key, 'origin': 'rights-withheld', 'status': 'unavailable', 'passed': None, 'reason': 'NIST SRD69 redistribution clearance pending; inputs and direct numerical outputs withheld from this public derivative.'} for key in ('nist-copper-shomate', 'enthalpy-integral-consistency')])

    a=corrosion_uniform_loss_mm_year(.1,100,240,7.8)
    twice=corrosion_uniform_loss_mm_year(.2,100,240,7.8)
    cases.append({'id':'corrosion-equivalent-loss','origin':'synthetic_coupon_parameters',
                  'passed':abs(twice['equivalent_uniform_penetration_mm_per_year']/a['equivalent_uniform_penetration_mm_per_year']-2)<1e-14,
                  'rate_mm_year':a['equivalent_uniform_penetration_mm_per_year'],
                  'zero_loss_is_not_zero_pitting':'possible unobserved localized attack',
                  'limits':a['not_inferred']})

    thermal=series_conduction(((.001,200),(.005,1)),.1,50, (.3,))
    cases.append({'id':'thermal-series-boundaries','origin':'synthetic_layer_stack',
                  'passed':abs(thermal['thermal_resistance_K_per_W']-.35005)<1e-12,
                  'heat_rate_W':thermal['heat_rate_W'],
                  'limits':'steady 1D, geometry/contacts asserted; no thermal stress or system certification'})

    t=avrami_time_to_fraction(.001,2,.5)
    got=avrami_isothermal(.001,2,t)
    cases.append({'id':'isothermal-avrami-reversibility','origin':'synthetic_kinetics',
                  'passed':abs(got['fraction_transformed']-.5)<1e-12,
                  'half_transformation_s':t,
                  'limits':'no continuous cooling, no fitted real material coefficients'})

    base=norton_steady_creep(50,900,1e-8,3,200e3,3600)
    double=norton_steady_creep(100,900,1e-8,3,200e3,3600)
    cases.append({'id':'creep-stress-exponent','origin':'synthetic_creep_model',
                  'passed':abs(double['model_steady_strain_rate_per_s']/base['model_steady_strain_rate_per_s']-8)<1e-12,
                  'rate_at_50_MPa_per_s':base['model_steady_strain_rate_per_s'],
                  'limits':'no creep rupture or failure time'})

    kw={'stress_MPa':120,'reference_scale_MPa':200,'weibull_shape':5,
        'component_volume_mm3':1000,'reference_volume_mm3':1000,'physical_weakest_link_assumed':True}
    one=conditional_weakest_link_survival(**kw)
    kw['component_volume_mm3']=2000
    two=conditional_weakest_link_survival(**kw)
    cases.append({'id':'weibull-mechanism-vs-fit','origin':'synthetic_declared_weakest_link',
                  'passed':abs(two['conditional_survival_probability']-one['conditional_survival_probability']**2)<1e-14,
                  'single_volume_survival':one['conditional_survival_probability'],
                  'double_volume_survival':two['conditional_survival_probability'],
                  'implicit_volume_scaling_refused':_rejects(conditional_weakest_link_survival,120,200,5,1000,1000),
                  'limits':'conditional physical flaw model, not an empirical Weibull fit validated for scaling'})

    cases.append({'id':'invalid-input-refusal','origin':'authored_negative_test',
                  'passed':all([
                      # SRD69 unavailable functions are not counted as negative controls.
                      _rejects(corrosion_uniform_loss_mm_year,-.01,100,240,7.8),
                      _rejects(series_conduction,[(.01,-.1)],1,100),
                      _rejects(avrami_time_to_fraction,.01,2,1),
                      _rejects(norton_steady_creep,1,0,1,2,5,20)
                  ]), 'limits':'invalid-input rejection is not evidence of materials model truth'})
    return {'schema':'materials.v1-casebook/1','version':'1.0.0','cases':cases,'count':len(cases),
            'status':'partial_rights_withheld' if all(c['passed'] for c in cases if c.get('status') != 'unavailable') else 'failed',
            'independent_human_review':False,'new_physical_measurements':0,
            'live_bitwork_or_model_result':False}
