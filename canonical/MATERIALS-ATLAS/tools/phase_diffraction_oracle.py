"""Separate NumPy/SciPy numerical comparison. Optional developer tool, not certification."""
from __future__ import annotations
import json,math,platform,random,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from scipy.optimize import minimize_scalar
from materials_atlas.phase_models import R,regular_solution_boundaries,regular_solution_state
from materials_atlas.diffraction import cubic_lattice_from_indexed_peaks
from materials_atlas.hahn_diagnostics import hahn1_residual_diagnostics
from materials_atlas.advanced import hahn1_observations,hahn1_prediction

def run():
 r=random.Random(20261112);num_phase=0;num_diff=0;diffs=[];fail=[]
 for j in range(90):
  omega=4000+r.random()*40000;ratio=.3+r.random()*.64;temp=(omega/(2*R))*ratio
  p=regular_solution_boundaries(temperature_k=temp,omega_j_mol=omega)
  def g(x):
   return R*temp*(x*np.log(x)+(1-x)*np.log1p(-x))+omega*x*(1-x)
  # Different numerical objective from Atlas root of dG/dx: minimize G directly.
  oracle=minimize_scalar(g,bounds=(max(1e-13,p['spinodal_mole_fraction_b'][0]*.0001),p['spinodal_mole_fraction_b'][0]),method='bounded',options={'xatol':1e-13})
  if not oracle.success:fail.append('scipy minimization failed')
  b=p['binodal_mole_fraction_b'][0];e=abs(b-oracle.x);diffs.append(e)
  if e>4e-6:fail.append(f'phase {j} b={b} independent minimum={oracle.x} error={e}')
  num_phase+=1
  st=regular_solution_state(temperature_k=temp,omega_j_mol=omega,mole_fraction_b=.5)
  if st['state']!='spinodal_unstable_homogeneous_state':fail.append('central instability classification')
 for j in range(240):
  a=2.5+r.random()*4;wl=.5+r.random()*.8
  hkl=[(1,0,0),(1,1,0),(1,1,1),(2,0,0),(2,1,0),(2,1,1),(2,2,0),(3,0,0)]
  sub=hkl[:3+j%6]
  peaks=[]
  for h,k,l in sub:
   n=h*h+k*k+l*l
   ang=2*math.degrees(math.asin(wl*math.sqrt(n)/(2*a)))
   peaks.append({'h':h,'k':k,'l':l,'two_theta_deg':ang+r.gauss(0,.003),'u_two_theta_deg':.01+.02*r.random()})
  uw=.0001+.0006*r.random()
  got=cubic_lattice_from_indexed_peaks(wavelength_angstrom=wl,wavelength_standard_uncertainty_angstrom=uw,peaks=peaks)
  # Recompute from vectorized physical equation, weights and covariance.
  theta=np.deg2rad(np.array([p['two_theta_deg'] for p in peaks])/2)
  ns=np.array([p['h']**2+p['k']**2+p['l']**2 for p in peaks],dtype=float)
  A=wl*np.sqrt(ns)/(2*np.sin(theta));u2=np.array([p['u_two_theta_deg'] for p in peaks])
  sd=np.abs(A/np.tan(theta)*np.pi/360*u2)
  w=np.divide(1,sd**2);mu=np.sum(w*A)/np.sum(w);ind=np.sqrt(1/np.sum(w));shared=mu*uw/wl
  chi=np.sum(((A-mu)/sd)**2)
  for k,v in [('mean_lattice_parameter_angstrom',mu),('standard_uncertainty_angle_angstrom',ind),('standard_uncertainty_shared_wavelength_angstrom',shared),('chi_square',chi)]:
   gotv=got[k];atol=1e-9+abs(v)*1e-10
   if abs(gotv-v)>atol:fail.append(f'diffraction {j} {k}: {gotv} vs {v}')
  num_diff+=4
 # SRD140_PUBLIC_WITHHELD: source-dependent residual comparisons withheld.
 return {'schema':'atlas.materials-v0.3-numeric-oracle/1','result':'partial_rights_withheld' if not fail else 'failed','phase_cases':num_phase,
 'diffraction_scalar_checks':num_diff,'hahn_residual_bin_cases':0,'public_edition_notice':'Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.',
 'largest_phase_boundary_difference':max(diffs),'numpy_version':np.__version__,
 'scipy_version':__import__('scipy').__version__,'python':platform.python_version(),
 'oracle':'scipy direct energy minimization; NumPy vectorized peak regression; NumPy Hahn1 residual bins',
 'failures':fail[:25],'independent_human_review':False,'new_physical_measurements':False}

if __name__=='__main__':
 v=run();print(json.dumps(v,indent=2));raise SystemExit(v['result']!='passed')
