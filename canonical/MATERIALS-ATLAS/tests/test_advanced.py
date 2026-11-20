import math,unittest,hashlib,json,random
from pathlib import Path
from materials_atlas.advanced import (
  hahn1_observations,hahn1_prediction,published_hahn1_replay,arrhenius_diffusivity,
  diffusion_rms_1d,fracture_mode_i,paris_fatigue_rate,engineering_true_before_necking,
  linear_thermal_strain_path,H1_CERT_RSS
)
from materials_atlas.methods import MaterialsInputError

class TestNistPublished(unittest.TestCase):
 def test_236(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_spots(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_temperature_span(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_certified_numerical_benchmark(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_extrapolation_refused(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_denominator_guard(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_nan_bad_beta(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_bad_beta_length(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_local_data_archive_hash(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')

class TestMaterialExamples(unittest.TestCase):
 def test_arrhenius(self):
  a=arrhenius_diffusivity(prefactor_m2_s=1e-4,activation_energy_j_mol=80000,temperature_k=1000)
  self.assertAlmostEqual(a['diffusivity_m2_s'],1e-4*math.exp(-80000/(8.31446261815324*1000)))
 def test_arrhenius_monotone(self):
  vals=[arrhenius_diffusivity(prefactor_m2_s=1e-5,activation_energy_j_mol=100000,temperature_k=t)['diffusivity_m2_s'] for t in [600,800,1000]]
  self.assertEqual(vals,sorted(vals))
 def test_arrhenius_bad(self):
  for x in [0,-1,10001]:
   with self.assertRaises(MaterialsInputError):arrhenius_diffusivity(prefactor_m2_s=1e-5,activation_energy_j_mol=100000,temperature_k=x)
 def test_arrhenius_no_negative_energy(self):
  with self.assertRaises(MaterialsInputError):arrhenius_diffusivity(prefactor_m2_s=1e-5,activation_energy_j_mol=-1,temperature_k=500)
 def test_diffusion_rms(self):self.assertAlmostEqual(diffusion_rms_1d(diffusivity_m2_s=1e-12,seconds=100)['rms_displacement_m'],math.sqrt(2e-10))
 def test_diffusion_negative_refusal(self):
  with self.assertRaises(MaterialsInputError):diffusion_rms_1d(diffusivity_m2_s=-1,seconds=10)
 def test_fracture(self):self.assertAlmostEqual(fracture_mode_i(stress_mpa=100,crack_length_m=.001,geometry_factor=1)['stress_intensity_mpa_sqrt_m'],100*math.sqrt(math.pi*.001))
 def test_fracture_missing_geometry(self):
  with self.assertRaises(MaterialsInputError):fracture_mode_i(stress_mpa=100,crack_length_m=.001,geometry_factor=0)
 def test_paris(self):
  r=paris_fatigue_rate(delta_k_mpa_sqrt_m=10,c_mm_per_cycle_per_k_power=1e-7,exponent_m=3,valid_delta_k_min=5,valid_delta_k_max=20)
  self.assertAlmostEqual(r['crack_growth_rate_mm_per_cycle'],1e-4)
 def test_paris_extrapolation_refusal(self):
  with self.assertRaises(MaterialsInputError):paris_fatigue_rate(delta_k_mpa_sqrt_m=40,c_mm_per_cycle_per_k_power=1e-7,exponent_m=3,valid_delta_k_min=5,valid_delta_k_max=20)
 def test_true_conversion(self):
  r=engineering_true_before_necking(engineering_stress_mpa=200,engineering_strain=.1,uniform_deformation_assumed=True)
  self.assertAlmostEqual(r['true_stress_mpa'],220)
  self.assertAlmostEqual(r['true_log_strain'],math.log(1.1))
 def test_true_conversion_guard(self):
  with self.assertRaises(MaterialsInputError):engineering_true_before_necking(engineering_stress_mpa=200,engineering_strain=.1,uniform_deformation_assumed=False)
 def test_thermal_constant(self):
  r=linear_thermal_strain_path(temperature_k=[300,400,500],alpha_per_k=[2e-5]*3,reference_temperature_k=300)
  self.assertAlmostEqual(r['integrated_log_length_change'],.004)
  self.assertAlmostEqual(r['length_ratio_exp_integral'],math.exp(.004))
 def test_thermal_trapezoidal(self):
  r=linear_thermal_strain_path(temperature_k=[300,400],alpha_per_k=[1e-5,3e-5],reference_temperature_k=300)
  self.assertAlmostEqual(r['integrated_log_length_change'],.002)
 def test_thermal_bad_grid(self):
  with self.assertRaises(MaterialsInputError):linear_thermal_strain_path(temperature_k=[300,300],alpha_per_k=[2e-5,3e-5],reference_temperature_k=300)
 def test_thermal_ref_guard(self):
  with self.assertRaises(MaterialsInputError):linear_thermal_strain_path(temperature_k=[300,400],alpha_per_k=[2e-5,3e-5],reference_temperature_k=350)
 def test_grid_random_constant(self):
  r=random.Random(9911)
  for _ in range(150):
   t0=290+r.random()*30;t1=t0+10+r.random()*200;a=r.random()*1e-4
   result=linear_thermal_strain_path(temperature_k=[t0,(t0+t1)/2,t1],alpha_per_k=[a]*3,reference_temperature_k=t0)
   self.assertAlmostEqual(result['integrated_log_length_change'],a*(t1-t0),places=13)

if __name__=='__main__':unittest.main()
