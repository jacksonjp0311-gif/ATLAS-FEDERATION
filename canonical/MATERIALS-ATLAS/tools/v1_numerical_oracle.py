"""Separate scipy/NumPy numerical algorithms for the v1 bounded models.

This tests computation, not actual physical model validity or scientific review.
"""
from pathlib import Path
import json,sys,random,math,platform
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scipy.integrate import quad
import scipy,numpy
from materials_atlas.v1_methods import (copper_solid_shomate,copper_enthalpy_change,
      corrosion_uniform_loss_mm_year,series_conduction,avrami_time_to_fraction,
      avrami_isothermal,norton_steady_creep,conditional_weakest_link_survival)
from materials_atlas.v1_cases import NIST_CU_CHECKS
rng=random.Random(11212026)
checks=[]
def check(name,val,expected,atol=1e-9,rtol=1e-9):
    delta=abs(val-expected);scale=max(atol,rtol*max(abs(val),abs(expected)))
    checks.append({'kind':name,'absolute_error':delta,'scaled_error':delta/scale,'passed':delta<=scale})
# SRD69_PUBLIC_DERIVATIVE: source-display and derived-integral checks unavailable.
for j in range(125):
    w=rng.uniform(.0001,.5);a=rng.uniform(5,1000);h=rng.uniform(24,5000);d=rng.uniform(2,20)
    rate=corrosion_uniform_loss_mm_year(w,a,h,d)['equivalent_uniform_penetration_mm_per_year']
    # Independent geometry route: cm lost = mass/density/area; scale to mm and per yr.
    expect=(w/d/a)*10*(365*24/h)
    check('coupon_dimensional_geometry',rate,expect,atol=1e-12,rtol=1e-12)
for j in range(125):
    layers=[(rng.uniform(.0001,.05),rng.uniform(.05,600)) for _ in range(rng.randint(1,5))]
    area=rng.uniform(.01,2);contacts=[rng.uniform(0,.5) for _ in range(rng.randint(0,3))]
    DT=rng.uniform(-200,200)
    rate=series_conduction(layers,area,DT,contacts)['heat_rate_W']
    expect=DT/(sum(L/(k*area) for L,k in layers)+sum(contacts))
    check('thermal_series_network',rate,expect,atol=5e-11,rtol=1e-11)
for j in range(100):
    k=rng.uniform(.0001,.03);n=rng.uniform(.3,5);fraction=rng.uniform(.01,.98)
    t=avrami_time_to_fraction(k,n,fraction)
    check('avrami_inverse',avrami_isothermal(k,n,t)['fraction_transformed'],fraction,atol=2e-13,rtol=2e-13)
for j in range(100):
    n=rng.uniform(1,6);T=rng.uniform(600,1400);stress=rng.uniform(30,150);A=10**rng.uniform(-11,-5);Q=rng.uniform(60e3,220e3)
    ra=norton_steady_creep(stress,T,A,n,Q,100)['model_steady_strain_rate_per_s']
    rb=norton_steady_creep(stress*1.2,T,A,n,Q,100)['model_steady_strain_rate_per_s']
    check('norton_ratio',rb/ra,1.2**n,atol=1e-11,rtol=1e-11)
for j in range(100):
    shape=rng.uniform(1,10);stress=rng.uniform(1,150);scale=rng.uniform(150,300);volume=rng.uniform(10,10000)
    kw=dict(stress_MPa=stress,reference_scale_MPa=scale,weibull_shape=shape,
     component_volume_mm3=volume,reference_volume_mm3=10000,physical_weakest_link_assumed=True)
    a=conditional_weakest_link_survival(**kw)['conditional_survival_probability']
    kw['component_volume_mm3']=volume*2
    b=conditional_weakest_link_survival(**kw)['conditional_survival_probability']
    check('weibull_conditional_survival_double_volume',b,a*a,atol=1e-13,rtol=1e-12)
failed=[x for x in checks if not x['passed']]
report={'schema':'atlas.materials-v1-oracle/1','status':'partial_rights_withheld' if not failed else 'failed',
    'unavailable_case_ids':sorted({'enthalpy-integral-consistency', 'nist-copper-shomate'}), 'comparisons':len(checks),'max_scaled_error':max(x['scaled_error'] for x in checks),
    'max_abs_error':max(x['absolute_error'] for x in checks),
    'failed_cases':failed[:10],'numpy_version':numpy.__version__,'scipy_version':scipy.__version__,
    'python':platform.python_version(),'random_seed':11212026,
    'independent_human_review':False,'new_material_experiments':0,
    'comment':'Separate integration/linear-algebra/arithmetic comparisons; not independent physical validation or material certification.'}
out=Path(__file__).resolve().parents[1]/'evidence/v1_numerical_oracle.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
raise SystemExit(bool(failed))
