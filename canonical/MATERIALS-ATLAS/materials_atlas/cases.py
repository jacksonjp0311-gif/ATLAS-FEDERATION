"""Reproducible author-made teaching cases; never actual material observations."""
from .methods import *

def casebook()->dict:
    cases=[]
    def add(case,calc,checks,description):
        ok=all(checks.values())
        cases.append({'id':case,'origin':'synthetic_authored_teaching','description':description,'calculation':calc,'checks':checks,'passed':ok,'not_real_material_validation':True})
    x=lattice_density(atomic_mass_g_per_mol=63.546,atoms_per_cell=4,cubic_a_angstrom=4)
    add('unit-cell-density',x,{'expected_toy_density':abs(x['density_g_cm3']-6.5946)<.01},'Toy cubic lattice with fictional atom positions; not a copper specimen.')
    x=bragg_spacing(wavelength_angstrom=1.54,two_theta_degrees=44)
    add('indexed-peak-spacing',x,{'range_2_to_2p1_angstrom':2<x['d_angstrom']<2.1},'Toy indexed first-order reflection, not phase identification.')
    x=lever_rule(overall_fraction_b=.4,alpha_fraction_b=.2,beta_fraction_b=.7)
    add('binary-tie-line',x,{'mass_balance':abs(.2*x['fraction_alpha']+.7*x['fraction_beta']-.4)<1e-12},'Toy equilibrium binary tie line; not measured phase fractions.')
    x=thermal_mismatch(alpha_a_per_k=23e-6,alpha_b_per_k=12e-6,delta_temperature_k=60)
    add('thermal-free-strain',x,{'microstrain':abs(x['microstrain_difference']-660)<1e-10},'No constraint or stress model, only thermal expansion mismatch.')
    x=engineering_tensile_point(force_newtons=5000,area_mm2=20,elongation_mm=.5,gauge_length_mm=50)
    add('tensile-point',x,{'mpa':x['engineering_stress_mpa']==250,'strain':x['engineering_strain']==.01},'One illustrative tensile point, not yield or ultimate strength.')
    x=mixture_modulus_bounds(modulus_a_gpa=200,modulus_b_gpa=3,volume_fraction_a=.3)
    add('ideal-modulus-mixture',x,{'voigt':abs(x['iso_strain_voigt_gpa']-62.1)<1e-9,'positive':x['iso_stress_reuss_gpa']>0},'Scalar ideal parallel/series assumptions, not tested composite modulus.')
    x=formation_energy_per_atom(total_energy_ev=-11,formula_counts={'A':1,'B':2},element_reference_ev_per_atom={'A':-2,'B':-3})
    add('toy-formation-energy',x,{'expected':abs(x['formation_energy_ev_per_atom']+1)<1e-12},'Fictitious electronic energies on one reference; no external DFT performed.')
    x=binary_hull_distance(phases=[{'id':'A','x_b':0,'energy_ev_atom':0},{'id':'AB','x_b':.5,'energy_ev_atom':-.4},{'id':'B','x_b':1,'energy_ev_atom':0}],candidate_x_b=.3,candidate_energy_ev_atom=-.18)
    add('toy-hull-above',x,{'above_hull':abs(x['signed_candidate_minus_hull_ev_atom']-.06)<1e-9},'Finite supplied toy phase set; not a real database stability estimate.')
    x=binary_hull_distance(phases=[{'id':'A','x_b':0,'energy_ev_atom':0},{'id':'B','x_b':1,'energy_ev_atom':0}],candidate_x_b=.5,candidate_energy_ev_atom=-.2)
    add('incomplete-hull-detection',x,{'below_reference':x['candidate_below_reference_hull']},'New candidate below current reference hull shows the existing list was incomplete.')
    meta={'property':'modulus','unit':'GPa','method':'tensile','temperature_k':300,'direction':'longitudinal','condition':'annealed','origin':'measured','value':50,'uncertainty':3}
    try:compare_properties(meta,dict(meta,origin='computed'));caught=False
    except MaterialsInputError:caught=True
    add('measured-versus-computed-refusal',{'refusal_expected':caught},{'refusal':caught},'Equal labels or units do not make computed and measured data interchangeable.')
    try:lever_rule(overall_fraction_b=.9,alpha_fraction_b=.2,beta_fraction_b=.7);caught=False
    except MaterialsInputError:caught=True
    add('invalid-tie-line-refusal',{'refusal_expected':caught},{'refusal':caught},'Negative phase fraction is not physically reported.')
    return {'schema':'atlas.materials-casebook/1','status':'passed' if all(x['passed'] for x in cases) else 'failed',
            'cases':cases,'count':len(cases),'physical_measurements':False,'external_DFT_or_datasets_run':False,'independent_review':False}
