"""Original, synthetic casebook for phase/Bragg/Hahn1 diagnostic methods."""
from .phase_models import regular_solution_boundaries,regular_solution_state,regular_solution_energy,R
from .diffraction import cubic_peak_lattice,cubic_lattice_from_indexed_peaks
from .hahn_diagnostics import hahn1_residual_diagnostics
import math


def expanded_casebook()->dict:
    cases=[]
    def add(label,result,expected,limitations):
        cases.append({'id':label,'passed':bool(result),'observed':expected,'origin':'original_synthetic_demonstration_or_descriptive_published_data_reanalysis','limitations':limitations})
    omega=20000.;tc=omega/(2*R)
    hot=regular_solution_boundaries(temperature_k=1.2*tc,omega_j_mol=omega)
    add('above_critical_single_phase',hot['phase_regime']=='single_phase_all_compositions',{'critical_temperature_k':tc},['The critical point belongs only to stipulated constant-omega model'])
    cold=regular_solution_boundaries(temperature_k=.8*tc,omega_j_mol=omega)
    b,bb=cold['binodal_mole_fraction_b'];s,ss=cold['spinodal_mole_fraction_b']
    add('binodal_wider_than_spinodal',b<s<.5<ss<bb,{'binodal':cold['binodal_mole_fraction_b'],'spinodal':cold['spinodal_mole_fraction_b']},['Synthetic material; no measured composition'])
    unstable=regular_solution_state(temperature_k=.8*tc,omega_j_mol=omega,mole_fraction_b=.5)
    add('central_composition_unstable',unstable['state']=='spinodal_unstable_homogeneous_state' and unstable['free_energy_drop_to_equilibrium_j_mol']>0,{'free_energy_drop_j_mol':unstable['free_energy_drop_to_equilibrium_j_mol']},['No kinetics or actual phase morphology'])
    meta=regular_solution_state(temperature_k=.8*tc,omega_j_mol=omega,mole_fraction_b=(b+s)/2)
    add('metastable_not_stable',meta['state']=='metastable_homogeneous_state_with_two_phase_lower_energy',{'state':meta['state']},['Positive local curvature does not establish global equilibrium'])
    stable=regular_solution_state(temperature_k=.8*tc,omega_j_mol=omega,mole_fraction_b=b/2)
    add('outside_binodal_single_phase',stable['state']=='outside_miscibility_gap_or_on_boundary',{'state':stable['state']},['Homogeneous phase stable only within this model'])
    a=3.61;wave=1.5406
    peaks=[]
    for hkl in [(1,1,1),(2,0,0),(2,2,0),(3,1,1)]:
        nn=sum(q*q for q in hkl)
        tw=2*math.degrees(math.asin(wave*math.sqrt(nn)/(2*a)))
        peaks.append({'h':hkl[0],'k':hkl[1],'l':hkl[2],'two_theta_deg':tw,'u_two_theta_deg':.015})
    latt=cubic_lattice_from_indexed_peaks(wavelength_angstrom=wave,wavelength_standard_uncertainty_angstrom=.0001,peaks=peaks)
    add('synthetic_cubic_multi_peak',abs(latt['mean_lattice_parameter_angstrom']-a)<1e-11 and latt['chi_square']<1e-14,
        {'a_angstrom':latt['mean_lattice_parameter_angstrom'],'u_a_angstrom':latt['combined_standard_uncertainty_angstrom']},
        ['Indexed ideal peak positions, not real copper XRD, phase identity or uncertainty budget'])
    add('common_wavelength_component_not_reduced_by_n',latt['standard_uncertainty_shared_wavelength_angstrom']>0,
        {'u_shared_angstrom':latt['standard_uncertainty_shared_wavelength_angstrom']},
        ['Wavelength is a shared systematic uncertainty in this first-order model'])
    # SRD140_PUBLIC_WITHHELD: source-dependent residual case withheld.
    return {'schema':'atlas.materials-extended-casebook/1','version':'0.3.0','cases':cases,
        'status':'partial_rights_withheld' if all(v['passed'] for v in cases) else 'failed','count':len(cases),
        'original_new_physical_observations':0,'independent_human_review':False}
