"""Optional independently coded numerical crosschecks, not physical replication."""
import json,sys,random,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
try:
 import numpy as np
 from scipy.optimize import linprog
except ImportError as exc:
 print(json.dumps({'result':'not_run','reason':str(exc)}));raise SystemExit(2)
from materials_atlas.methods import lever_rule, mixture_modulus_bounds, binary_hull_distance,lattice_density,bragg_spacing
rng=np.random.default_rng(71226)
counts={'lever':0,'mixtures':0,'hull_linprog':0,'density':0,'bragg':0};errors=[];worst=0.0
for _ in range(300):
 lo=float(rng.uniform(0,.35));hi=float(rng.uniform(.65,1));x=float(rng.uniform(lo,hi))
 r=lever_rule(overall_fraction_b=x,alpha_fraction_b=lo,beta_fraction_b=hi)
 ref=np.linalg.solve(np.array([[1.,1.],[lo,hi]]),np.array([1.,x]))
 z=max(abs(r['fraction_alpha']-ref[0]),abs(r['fraction_beta']-ref[1]));worst=max(worst,z)
 if z>1e-10:errors.append('lever')
 counts['lever']+=1
for _ in range(300):
 ea=float(rng.uniform(1,500));eb=float(rng.uniform(1,500));v=float(rng.uniform(0,1))
 r=mixture_modulus_bounds(modulus_a_gpa=ea,modulus_b_gpa=eb,volume_fraction_a=v)
 # independently construct compliance and parallel energy calculation
 vals=np.array([ea,eb]);fr=np.array([v,1-v]);ref_v=float(fr@vals);ref_r=float(1/np.dot(fr,1/vals))
 z=max(abs(r['iso_strain_voigt_gpa']-ref_v),abs(r['iso_stress_reuss_gpa']-ref_r));worst=max(worst,z)
 if z>1e-10:errors.append('mix')
 counts['mixtures']+=1
for _ in range(200):
 xs=np.array([0.,float(rng.uniform(.1,.4)),float(rng.uniform(.6,.9)),1.])
 es=np.array([0.,float(rng.uniform(-.7,.3)),float(rng.uniform(-.7,.3)),0.])
 x=float(rng.random());cand=float(rng.uniform(-.8,.2));phases=[{'id':f'p{i}','x_b':float(a),'energy_ev_atom':float(b)} for i,(a,b) in enumerate(zip(xs,es))]
 ours=binary_hull_distance(phases=phases,candidate_x_b=x,candidate_energy_ev_atom=cand)['hull_energy_ev_per_atom']
 lp=linprog(es,A_eq=np.array([np.ones(4),xs]),b_eq=np.array([1.,x]),bounds=(0,None),method='highs')
 if not lp.success:errors.append('linprog_failed');continue
 z=abs(ours-float(lp.fun));worst=max(worst,z)
 if z>1e-10:errors.append('hull')
 counts['hull_linprog']+=1
for _ in range(200):
 mass=float(rng.uniform(1,240));a=float(rng.uniform(2,12));n=int(rng.integers(1,9))
 our=lattice_density(atomic_mass_g_per_mol=mass,atoms_per_cell=n,cubic_a_angstrom=a)['density_g_cm3']
 ref=(n*mass/6.02214076e23)/(a**3*1e-24)
 z=abs(our-ref)/max(1,abs(ref));worst=max(worst,z)
 if z>1e-12:errors.append('density')
 counts['density']+=1
for _ in range(200):
 lam=float(rng.uniform(.3,4));angle=float(rng.uniform(5,170))
 d=bragg_spacing(wavelength_angstrom=lam,two_theta_degrees=angle)['d_angstrom']
 lhs=2*d*np.sin(np.deg2rad(angle/2))
 z=abs(lhs-lam);worst=max(worst,z)
 if z>1e-12:errors.append('bragg')
 counts['bragg']+=1
out={'schema':'atlas.materials-numerical-oracle/1','result':'passed' if not errors else 'failed','counts':counts,'total':sum(counts.values()),'worst_scaled_absolute_error':worst,'failures':errors[:12], 'seed':71226,'numpy_version':np.__version__, 'scipy_version':__import__('scipy').__version__, 'independent_algorithm_not_independent_scientific_review':True}
print(json.dumps(out,indent=2));raise SystemExit(bool(errors))
