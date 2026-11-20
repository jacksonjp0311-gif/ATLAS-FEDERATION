"""Independent NumPy numerical comparisons on ORIGINAL constructed Chemistry inputs.

Not authentic NIST tables or chemical measurements, experimental chemistry
validation, semiconductor production or industrial chemical process simulation.
"""
from pathlib import Path
import sys,random,math,json
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from chemistry_atlas.advanced import *

rng=np.random.default_rng(20261114)
counts={};max_error=0.;max_normalized_error=0.
def verify(k,got,expected,tol=1e-10):
    global max_error,max_normalized_error
    if not math.isfinite(float(got)) or not math.isfinite(float(expected)):raise AssertionError(k+' nonfinite')
    err=abs(float(got)-float(expected));max_error=max(max_error,err)
    max_normalized_error=max(max_normalized_error,err/max(1.,abs(float(got)),abs(float(expected))))
    if err>tol*max(1.,abs(float(got)),abs(float(expected))):raise AssertionError((k,got,expected))
    counts[k]=counts.get(k,0)+1

# Construct known charge/atom solutions and independently verify the matrix AX=0.
fixtures=[([
  {'label':'cation','atoms':{'H':1},'charge':1},{'label':'anion','atoms':{'H':1,'O':1},'charge':-1}],
  [{'label':'water','atoms':{'H':2,'O':1},'charge':0}]),
  ([{'label':'ferric','atoms':{'Fe':1},'charge':3},{'label':'electron','atoms':{},'charge':-1}],
   [{'label':'ferrous','atoms':{'Fe':1},'charge':2}])]
for i in range(350):
    lhs,rhs=fixtures[i%2]
    b=balance_charge_and_atoms(lhs,rhs);elements=sorted(set(k for x in lhs+rhs for k in x['atoms']))
    mat=np.asarray([[int(x['atoms'].get(e,0))*(1 if j<len(lhs) else -1) for j,x in enumerate(lhs+rhs)] for e in elements]+
      [[int(x['charge'])*(1 if j<len(lhs) else -1) for j,x in enumerate(lhs+rhs)]],dtype=np.int64)
    coeff=np.asarray(b['coefficient_vector'],dtype=np.int64)
    verify('independent_atom_charge_matrix',float(np.sum(np.abs(mat@coeff))),0)

for _ in range(600):
    n=int(rng.integers(1,8));m=int(rng.integers(1,8))
    react=[{'id':f'r{i}','coefficient':float(rng.uniform(.1,3.0)),
            'gibbs_formation_J_mol':float(rng.normal(0,100000)),
            'enthalpy_formation_J_mol':float(rng.normal(0,150000))} for i in range(n)]
    prod=[{'id':f'p{i}','coefficient':float(rng.uniform(.1,3.0)),
            'gibbs_formation_J_mol':float(rng.normal(0,100000)),
            'enthalpy_formation_J_mol':float(rng.normal(0,150000))} for i in range(m)]
    t=float(rng.uniform(250,1800));out=thermodynamic_reaction_delta(react,prod,t)
    Gp=np.dot(np.array([x['coefficient'] for x in prod]),np.array([x['gibbs_formation_J_mol'] for x in prod]));
    Gr=np.dot(np.array([x['coefficient'] for x in react]),np.array([x['gibbs_formation_J_mol'] for x in react]));
    Hp=np.dot(np.array([x['coefficient'] for x in prod]),np.array([x['enthalpy_formation_J_mol'] for x in prod]));
    Hr=np.dot(np.array([x['coefficient'] for x in react]),np.array([x['enthalpy_formation_J_mol'] for x in react]));
    verify('reaction_Gibbs_numpy',out['delta_G_standard_J_per_mol_reaction'],Gp-Gr)
    verify('reaction_enthalpy_numpy',out['delta_H_standard_J_per_mol_reaction'],Hp-Hr)
    verify('reaction_logK_numpy',out['log_equilibrium_constant'],-(Gp-Gr)/(R_GAS*t))

for _ in range(600):
    log0=float(rng.normal());t0=float(rng.uniform(200,700));t=float(rng.uniform(200,1500));h=float(rng.uniform(-5e4,5e4))
    out=vanthoff_logK(log0,t0,t,h)
    verify('vanthoff_numpy',out['logK_target'],log0+h/R_GAS*(1/t0-1/t))
    ion_count=int(rng.integers(1,20));c=rng.uniform(0,0.1,ion_count);z=rng.integers(-3,4,ion_count)
    z[z==0]=1
    ions=[{'ion':'z'+str(i),'molarity_mol_L':float(c[i]),'charge':int(z[i])} for i in range(ion_count)]
    out=ionic_strength(ions)
    verify('ionic_strength_numpy',out['I_molarity_basis_mol_L'],.5*np.dot(c,z.astype(float)**2))
    verify('electroneutrality_residual_numpy',out['charge_balance_residual_mol_L_equivalent'],np.dot(c,z.astype(float)))
    I=float(rng.uniform(0,0.01));A=float(rng.uniform(.1,1.0));zcharge=int(rng.choice([1,2,3,-1,-2]))
    out=debye_huckel_limiting_log_gamma(zcharge,I,A)
    verify('Debye_Huckel_numpy',out['log10_mean_idealized_gamma'],-A*zcharge**2*np.sqrt(I))

for _ in range(650):
    ni=float(10**rng.uniform(9,21));dop=float(rng.normal(0,1)*1e19)
    out=semiconductor_carrier_neutrality(dop,ni)
    ele=out['electron_density_m3'];hole=out['hole_density_m3']
    verify('carrier_mass_action',ele*hole,ni*ni)
    verify('carrier_charge_neutrality',(ele-hole)/max(1.,abs(dop)),dop/max(1.,abs(dop)),tol=1e-5)
    D=float(10**rng.uniform(-16,-8));a=float(rng.uniform(0,100));b=float(rng.uniform(0,100));dx=float(rng.uniform(1e-5,1))
    verify('Fick_gradient_flux',fick_flux_1d(D,a,b,dx)['flux_mol_m2_s'],-D*(b-a)/dx)
    eps=float(rng.uniform(0,10000));path=float(rng.uniform(0,2));conc=float(rng.uniform(0,.01))
    verify('Beer_Lambert_absorbance',beer_lambert_absorbance(eps,path,conc)['absorbance_decadic'],eps*path*conc)

# Independently vectorized no-flux update (not Python cell iteration from the model).
for _ in range(320):
    n=int(rng.integers(2,33));initial=rng.uniform(0,10,n);lam=float(rng.uniform(0,.49));step=int(rng.integers(0,60))
    actual=diffuse_no_flux_1d(initial.tolist(),lam,1,1,step)
    vector=initial.copy()
    for t in range(step):
        left=np.r_[vector[0],vector[:-1]];right=np.r_[vector[1:],vector[-1]]
        vector=vector+lam*(left-2*vector+right)
    verify('1d_diffusion_numpy_replay',float(np.max(np.abs(vector-np.asarray(actual['concentrations_mol_m3'])))),0,tol=1e-8)
    verify('1d_diffusion_total_mass',float(np.sum(vector)),float(np.sum(initial)),tol=1e-8)

report={'schema':'atlas.chemistry-v02-numerical-oracle/1','result':'passed','seed':20261114,
  'comparisons':sum(counts.values()),'by_method':counts,'max_absolute_difference_units_vary':max_error,'max_normalized_difference':max_normalized_error,
  'numpy_version':np.__version__,'data_origin':'author-generated finite numerical fixtures',
  'real_chemical_source_rows_imported':0,'actual_wafer_or_battery_measured':False,
  'independent_scientific_peer_review':False,
  'limitations':['Independent NumPy/formula arithmetic does not verify thermochemical data, measurement accuracy or real materials physics',
                 'No published original scientific dataset or laboratory experiment was imported, operated or reproduced']}
Path(__file__).resolve().parents[1].joinpath('evidence/numerical_oracle_v0.2.0.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
