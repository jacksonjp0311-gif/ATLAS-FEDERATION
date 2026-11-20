"""Optional regression oracle comparing bounded material formulas with NumPy.

These are two numerical implementations of STIPULATED models, NOT experimental
validation. Cases and seed are declared and retained for reproducibility.
"""
from __future__ import annotations
import json,math,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root))
from materials_atlas.advanced import (arrhenius_diffusivity,diffusion_rms_1d,fracture_mode_i,
    paris_fatigue_rate,engineering_true_before_necking,linear_thermal_strain_path)
try:
 import numpy as np
except ImportError:
 print(json.dumps({'result':'not_run','reason':'NumPy is optional, not installed'}));raise SystemExit(3)

SEED=112126; rng=np.random.default_rng(SEED)
checks=[]
def record(kind,local,oracle):
 a,b=float(local),float(oracle)
 scale=max(abs(b),abs(a),1e-15)
 err=abs(a-b)/scale
 checks.append((kind,err))
 if not (math.isfinite(err) and err<=2e-12):
  raise AssertionError(f'{kind}: {a} vs {b}; scaled_error={err}')

for i in range(180):
 t=float(rng.uniform(275,1450));d0=float(10**rng.uniform(-9,-3));q=float(rng.uniform(1000,185000))
 record('arrhenius',arrhenius_diffusivity(prefactor_m2_s=d0,activation_energy_j_mol=q,temperature_k=t)['diffusivity_m2_s'],
        np.exp(np.log(d0)-q/(np.float64(8.31446261815324)*np.float64(t))))
for i in range(180):
 d=float(10**rng.uniform(-18,-4));t=float(10**rng.uniform(-1,5))
 record('diffusion_rms',diffusion_rms_1d(diffusivity_m2_s=d,seconds=t)['rms_displacement_m'], np.sqrt(np.float64(2)*d*t))
for i in range(180):
 s=float(rng.uniform(1,1200));a=float(10**rng.uniform(-6,-1));y=float(rng.uniform(.2,5))
 record('fracture_mode_I',fracture_mode_i(stress_mpa=s,crack_length_m=a,geometry_factor=y)['stress_intensity_mpa_sqrt_m'], np.float64(s)*np.float64(y)*np.sqrt(np.float64(np.pi)*a))
for i in range(180):
 d=float(rng.uniform(3,80));C=float(10**rng.uniform(-12,-6));m=float(rng.uniform(1,5))
 record('paris_regime',paris_fatigue_rate(delta_k_mpa_sqrt_m=d,c_mm_per_cycle_per_k_power=C,exponent_m=m,valid_delta_k_min=1,valid_delta_k_max=100)['crack_growth_rate_mm_per_cycle'],
        np.exp(np.log(np.float64(C))+np.float64(m)*np.log(np.float64(d))))
for i in range(180):
 s=float(rng.uniform(.5,1800));e=float(rng.uniform(.01,.5))
 r=engineering_true_before_necking(engineering_stress_mpa=s,engineering_strain=e,uniform_deformation_assumed=True)
 record('true_stress_pre_neck',r['true_stress_mpa'],np.float64(s)*(np.float64(1)+np.float64(e)))
 record('true_log_strain_pre_neck',r['true_log_strain'],np.log(np.float64(1)+np.float64(e)))
for i in range(180):
 xs=np.cumsum(np.concatenate(([float(rng.uniform(150,450))],rng.uniform(10,100,5))));ys=rng.uniform(-20e-6,50e-6,size=6)
 r=linear_thermal_strain_path(temperature_k=xs.tolist(),alpha_per_k=ys.tolist(),reference_temperature_k=float(xs[0]))
 record('integrated_thermal_log_strain',r['integrated_log_length_change'],np.trapezoid(ys,xs))
 record('thermal_length_ratio',r['length_ratio_exp_integral'],np.exp(np.trapezoid(ys,xs)))
counts={k:sum(1 for a,_ in checks if a==k) for k in sorted(set(k for k,e in checks))}
out={'schema':'atlas.materials-method-oracle/1','result':'passed','seed':SEED,'numpy_version':np.__version__,
     'comparisons':len(checks),'per_method':counts,'max_scaled_abs_error':max(e for _,e in checks),
     'acceptance_scaled_absolute':2e-12,'validation_type':'author_seeded_separate_numpy_implementation',
     'independent_human_review':False,'physical_observations':False,'material_property_fit_or_certification':False}
print(json.dumps(out,indent=2))
