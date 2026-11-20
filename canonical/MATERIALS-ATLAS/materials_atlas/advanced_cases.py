"""Authored method exercises; published Hahn1 is labeled separately."""
from .advanced import (published_hahn1_replay,arrhenius_diffusivity,diffusion_rms_1d,
                       fracture_mode_i,paris_fatigue_rate,engineering_true_before_necking,
                       linear_thermal_strain_path)
from .methods import MaterialsInputError

def advanced_casebook()->dict:
    cases=[]
    def add(name,r,ok,origin='synthetic_authored'):
        cases.append({'case':name,'origin':origin,'calculation':r,'passed':bool(ok)})
    # SRD140_PUBLIC_WITHHELD: source-dependent case withheld.
    d=arrhenius_diffusivity(prefactor_m2_s=1e-5,activation_energy_j_mol=100000,temperature_k=850)
    add('arrhenius-supplied-parameters',d,0<d['diffusivity_m2_s']<1e-10)
    r=diffusion_rms_1d(diffusivity_m2_s=1e-12,seconds=3600)
    add('one-dimensional-diffusion-scale',r,8e-5<r['rms_displacement_m']<9e-5)
    k=fracture_mode_i(stress_mpa=200,crack_length_m=.001,geometry_factor=1)
    add('stress-intensity-not-fracture-certificate',k,11<k['stress_intensity_mpa_sqrt_m']<12)
    g=paris_fatigue_rate(delta_k_mpa_sqrt_m=10,c_mm_per_cycle_per_k_power=1e-7,exponent_m=3,valid_delta_k_min=5,valid_delta_k_max=20)
    add('paris-regime-only',g,abs(g['crack_growth_rate_mm_per_cycle']-1e-4)<1e-14)
    x=engineering_true_before_necking(engineering_stress_mpa=400,engineering_strain=.05,uniform_deformation_assumed=True)
    add('uniform-tensile-conversion',x,abs(x['true_stress_mpa']-420)<1e-9)
    x=linear_thermal_strain_path(temperature_k=[300,350,400],alpha_per_k=[18e-6,20e-6,22e-6],reference_temperature_k=300)
    add('temperature-varying-alpha',x,abs(x['integrated_log_length_change']-.002)<1e-12)
    try:fracture_mode_i(stress_mpa=200,crack_length_m=.001,geometry_factor=0);refused=False
    except MaterialsInputError:refused=True
    add('missing-fracture-geometry-refusal',{'refused':refused},refused)
    try:paris_fatigue_rate(delta_k_mpa_sqrt_m=30,c_mm_per_cycle_per_k_power=1e-7,exponent_m=3,valid_delta_k_min=5,valid_delta_k_max=20);refused=False
    except MaterialsInputError:refused=True
    add('paris-range-extrapolation-refusal',{'refused':refused},refused)
    return {'schema':'atlas.materials-advanced-cases/1','status':'partial_rights_withheld' if all(z['passed'] for z in cases) else 'failed',
            'cases':cases,'count':len(cases),'physical_experiments_performed':False,
            'published_case_number':0,'synthetic_case_number':len(cases),'public_edition_notice':'Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.'}
