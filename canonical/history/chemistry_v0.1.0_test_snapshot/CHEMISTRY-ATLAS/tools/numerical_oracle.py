"""NumPy and independent arithmetic checks on authored, nonempirical chemistry fixtures.

No physical experiments, chemical safety study, original source verification,
trained chemical AI, reactor operation or compound authentication are claimed.
"""
from pathlib import Path
import json,random,sys,math
from functools import lru_cache
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from chemistry_atlas.models import *
rng=np.random.default_rng(20261114);counts={};max_error=0.
def check(name,x,y,tol=1e-11):
 global max_error
 x=float(x);y=float(y);delta=abs(x-y);max_error=max(max_error,delta)
 if not np.isfinite(delta) or delta>tol*max(1.,abs(x),abs(y)):raise AssertionError(f'{name}: {x=} {y=} {delta=}')
 counts[name]=counts.get(name,0)+1
# Exact independent atomic conservation of primitive balanced coefficients.
for r,p in [(['H2','O2'],['H2O']),(['Fe','O2'],['Fe2O3']),(['Ca(OH)2','HCl'],['CaCl2','H2O']),(['Na','Cl2'],['NaCl'])]:
 coeff=balance_reaction(r,p)['coefficient_vector'];assert atom_balance(r,p,coeff[:len(r)],coeff[len(r):])['balanced']
 check('exact_atom_balance_reference',1.,1.)
for _ in range(620):
 n=float(rng.uniform(0,1e6));M=float(rng.uniform(.01,300));m=n*M
 check('mole_mass_numpy',amount_of_substance(m,M)['moles'],float(np.divide(m,M)))
 atoms=parse_formula('C6H12O6');weights={'C':float(rng.uniform(10,14)),'H':float(rng.uniform(.8,1.3)),'O':float(rng.uniform(14,19))}
 expected=float(np.dot(np.array([atoms[k] for k in ('C','H','O')]),np.array([weights[k] for k in ('C','H','O')])))
 check('molar_mass_numpy',molar_mass('C6H12O6',weights)['molar_mass_g_mol'],expected)
 vol=float(rng.uniform(.00001,15));check('molarity_numpy',solution_molarity(n,vol)['molarity_mol_L'],float(np.divide(n,vol)))
 T=float(rng.uniform(100,1000));V=float(rng.uniform(.001,20))
 check('ideal_gas_numpy',ideal_gas_pressure(n,T,V)['pressure_Pa'],float(np.divide(n*R_GAS*T,V)))
 dg=float(rng.uniform(-1e5,1e5));Q=float(np.exp(rng.uniform(-10,10)))
 check('gibbs_activity_log_numpy',reaction_free_energy(dg,T,Q)['delta_G_reaction_j_mol'],float(dg+R_GAS*T*np.log(Q)))
 check('equilibrium_logK_numpy',equilibrium_constant(dg,T)['ln_K_dimensionless'],float(-dg/(R_GAS*T)))
 Ea=float(rng.uniform(0,2e5));T2=float(rng.uniform(100,1000))
 check('arrhenius_ratio_numpy',arrhenius_log_ratio(Ea,T,T2)['ln_k2_over_k1'],float(-Ea/R_GAS*(1/T2-1/T)))
 k=float(rng.uniform(0,10));t=float(rng.uniform(0,100));c=float(rng.uniform(0,500))
 check('firstorder_numpy',first_order_kinetics(c,k,t)['concentration_mol_L'],float(c*np.exp(-k*t)))
 activity=float(np.exp(rng.uniform(-20,3)))
 check('pH_activity_numpy',pH_from_activity(activity)['pH'],float(-np.log10(activity)))
 potential=float(rng.uniform(-2,2));electrons=int(rng.integers(1,11))
 check('nernst_numpy',nernst_potential(potential,electrons,T,Q)['potential_V'],float(potential-R_GAS*T/(electrons*FARADAY)*np.log(Q)))
 carriers=float(rng.uniform(0,1e24));holes=float(rng.uniform(0,1e24));mn=float(rng.uniform(0,1));mp=float(rng.uniform(0,1))
 check('semiconductor_drift_numpy',conductivity_semiconductor(carriers,holes,mn,mp)['conductivity_S_m'],float(ELEMENTARY_CHARGE*np.dot(np.asarray([carriers,holes]),np.asarray([mn,mp]))))
 D=float(rng.uniform(0,1e-9));secs=float(rng.uniform(0,1e6));dimensions=int(rng.integers(1,4))
 check('diffusion_numpy',diffusion_length(D,secs,dimensions)['rms_displacement_m'],float(np.sqrt(2*dimensions*D*secs)))
 m0=float(rng.uniform(0,100));m1=float(rng.uniform(0,100));acc=float(rng.uniform(-50,50));r=mass_balance_process([m0],[m1],acc)
 check('mass_balance_numpy',r['unaccounted_residual_kg'],float(np.sum(np.array([m0,-m1,-acc]))))
report={'schema':'atlas.chemistry-numerical-oracle/1','status':'passed','seed':20261114,
  'comparisons':sum(counts.values()),'counts':counts,'max_absolute_difference':max_error,'numpy_version':np.__version__,
  'all_inputs':'original author-generated finite numerical fixtures',
  'physical_experiments':0,'original_publisher_source_rows_loaded':0,'trained_chemical_models':0,
  'expert_review':False,'limitations':['Independent arithmetic agreement verifies model implementation, not laboratory measurement or the broad truth of a chemical process',
  'Simplified formula balancing intentionally excludes charges, isotopes and multiple independent stoichiometries']}
p=Path(__file__).resolve().parents[1]/'evidence/numerical_oracle_v0.1.0.json';p.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
