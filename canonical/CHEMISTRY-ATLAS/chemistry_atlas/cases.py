"""Author-created chemical science casebook; no synthesis or real experiment."""
from .models import *

def casebook():
    out=[]
    def add(name, data, passed, limit):out.append({'id':name,'result':data,'passed':bool(passed),'origin':'author_constructed_toy_model','boundary':limit})
    a=parse_formula('Al2(SO4)3');add('formula-nesting',a,a=={'Al':2,'O':12,'S':3},'Neutral formula syntax only')
    a=balance_reaction(['H2','O2'],['H2O']);add('water-molecule-balance',a,a['coefficient_vector']==[2,1,2],'Mathematical atom count, not gas reaction protocol')
    a=balance_reaction(['Fe','O2'],['Fe2O3']);add('oxide-stoichiometry',a,a['coefficient_vector']==[4,3,2],'No prediction of kinetics/corrosion from coefficients')
    a=balance_reaction(['Ca(OH)2','HCl'],['CaCl2','H2O']);add('neutralization-count',a,a['coefficient_vector']==[1,2,1,2],'No mixing procedure or hazard claim')
    a=atom_balance(['H2','O2'],['H2O'],[1,1],[1]);add('detect-atom-imbalance',a,not a['balanced'],'An element mismatch does not identify the actual reaction')
    a=molar_mass('H2O',{'H':1.008,'O':15.999});add('molar-mass-caller-data',a,abs(a['molar_mass_g_mol']-18.015)<1e-12,'Values illustrative and isotope-dependent')
    a=amount_of_substance(36.03,18.015);add('moles-from-mass',a,abs(a['moles']-2)<1e-12,'Needs correct molar mass and phase')
    a=limiting_extent({'A':2,'B':5},{'A':1,'B':2});add('reaction-extent-limit',a,a['max_reaction_extent_mol']==2 and a['limiting_species']==['A'],'Complete theoretical conversion, not yield')
    a=solution_molarity(0.2,0.5);add('solution-final-volume',a,a['molarity_mol_L']==.4,'Concentration alone not activity or safety')
    a=dilution(0.5,1,2);add('dilution-conservation',a,a['final_concentration_mol_L']==.25,'Arithmetic only; no chemical mixing procedure')
    a=ideal_gas_pressure(1,300,.024);add('ideal-gas-equation',a,a['pressure_Pa']>100000,'Ideal gas under declared conditions')
    a=reaction_free_energy(0,298.15,2);add('free-energy-with-quotient',a,a['delta_G_reaction_j_mol']>0,'Activities, not concentration, reaction rate unknown')
    a=equilibrium_constant(0,298.15);add('equilibrium-K-one',a,a['K_dimensionless']==1,'Standard states required')
    a=reaction_enthalpy({'A':-10,'B':-20},{'A':1},{'B':1});add('hess-law',a,a['delta_H_reaction_j_per_extent_mol']==-10,'Hypothetical formation enthalpies, same reference state')
    a=arrhenius_log_ratio(20000,300,330);add('arrhenius-temperature-effect',a,a['k2_over_k1']>1,'Empirical Arrhenius parameters; no mechanism proof')
    a=first_order_kinetics(1,0.1,10);add('first-order-decay',a,abs(a['concentration_mol_L']-exp(-1))<1e-12,'Not general chemical kinetics')
    a=pH_from_activity(1e-7);add('pH-from-activity',a,abs(a['pH']-7)<1e-10,'Not concentration-only pH in all solutions')
    a=henderson_hasselbalch(5,2,1);add('buffer-equilibrium-ratio',a,a['pH_ideal_ratio']>5,'Only conjugate pair equilibrium; not a preparation protocol')
    a=nernst_potential(1,1,298.15,1);add('nernst-Q-one',a,a['potential_V']==1,'Reversible cell only, no battery performance prediction')
    a=faraday_charge(1);add('faraday-si-derived-charge',a,abs(a['charge_C']-96485.33212331002)<1e-7,'No electrolysis procedure or current safety')
    a=conductivity_semiconductor(1e21,0,.1,0);add('semiconductor-carrier-conductivity',a,a['conductivity_S_m']>0,'Carrier mobility and densities are caller supplied')
    a=diffusion_length(1e-12,100);add('diffusion-rms-length',a,abs(a['rms_displacement_m']-sqrt(2e-10))<1e-12,'Not semiconductor diffusion thermal process recipe')
    a=mass_balance_process([100],[70,20],10);add('chemical-process-mass-closure',a,a['unaccounted_residual_kg']==0,'Mass-only accounting; unknown emissions/phase changes')
    a=mass_balance_process([100],[60,20],10);add('unaccounted-material-residual',a,a['unaccounted_residual_kg']==10,'Cannot infer which material path is missing')
    try:balance_reaction(['H2'],['H2O']);good=False
    except ChemistryModelError:good=True
    add('invalid-balancing-refuses',{'refusal':good},good,'Mathematical refusal, not evidence of a chemical impossibility')
    return {'schema':'atlas.chemistry-casebook/1','status':'passed' if all(x['passed'] for x in out) else 'failed',
      'case_count':len(out),'cases':out,'authentic_experiments':0,'independent_chemistry_review':False,'real_compounds_handled':False}
