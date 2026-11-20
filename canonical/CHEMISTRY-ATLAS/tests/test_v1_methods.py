import unittest,random,math
from chemistry_atlas.v1_models import *
from chemistry_atlas.v1_cases import casebook_v1
from chemistry_atlas.models import ChemistryModelError,R_GAS,FARADAY

class PhotonBandgap(unittest.TestCase):
 def test_casebook(self):self.assertEqual(casebook_v1()['status'],'passed');self.assertEqual(casebook_v1()['count'],14)
 def test_greater_wave_lower_energy(self):self.assertGreater(photon_bandgap(300,1)['photon_energy_eV'],photon_bandgap(800,1)['photon_energy_eV'])
 def test_threshold(self):self.assertFalse(photon_bandgap(1000,3)['energetically_above_supplied_gap'])
 def test_invalid(self):
  with self.assertRaises(ChemistryModelError):photon_bandgap(-1,2)
 def test_exact_constant(self):self.assertEqual(C_SI,299792458)

class Semiconductor(unittest.TestCase):
 def test_varshni_zero(self):self.assertEqual(varshni_bandgap(0,1.2,.001,10)['bandgap_eV'],1.2)
 def test_varshni_decreases(self):self.assertGreater(varshni_bandgap(200,1.5,.001,200)['bandgap_eV'],varshni_bandgap(300,1.5,.001,200)['bandgap_eV'])
 def test_bandgap_nonpositive_reject(self):
  with self.assertRaises(ChemistryModelError):varshni_bandgap(100,1,.1,10)
 def test_carrier_positive(self):self.assertGreater(intrinsic_carrier_density(1e24,1e24,1,300)['intrinsic_carrier_density_m3'],0)
 def test_carrier_temperature(self):self.assertGreater(intrinsic_carrier_density(1e25,1e25,1,400)['intrinsic_carrier_density_m3'],intrinsic_carrier_density(1e25,1e25,1,300)['intrinsic_carrier_density_m3'])
 def test_carrier_negative_gap(self):
  with self.assertRaises(ChemistryModelError):intrinsic_carrier_density(1e24,1e24,-1,300)
 def test_diode_zero(self):self.assertEqual(diode_ideal_current(1e-12,0,1,300)['current_A'],0)
 def test_diode_negative(self):self.assertLess(diode_ideal_current(1e-12,-.5,1,300)['current_A'],0)
 def test_diode_positive(self):self.assertGreater(diode_ideal_current(1e-12,.5,1,300)['current_A'],0)
 def test_diode_no_overflow(self):
  with self.assertRaises(ChemistryModelError):diode_ideal_current(1e-12,1000,1,300)

class Thermochemistry(unittest.TestCase):
 def test_cp_flat(self):
  r=shomate_thermochemistry(40,0,0,0,0,300,500,250,600)
  self.assertAlmostEqual(r['delta_H_J_mol'],8000);self.assertAlmostEqual(r['delta_S_J_mol_K'],40*math.log(500/300))
 def test_cp_zero_interval(self):self.assertEqual(shomate_thermochemistry(40,0,0,0,0,400,400,250,600)['delta_H_J_mol'],0)
 def test_cp_reverse(self):
  a=shomate_thermochemistry(40,2,3,4,5,300,400,250,600);b=shomate_thermochemistry(40,2,3,4,5,400,300,250,600)
  self.assertAlmostEqual(a['delta_H_J_mol'],-b['delta_H_J_mol'],places=9)
  self.assertAlmostEqual(a['delta_S_J_mol_K'],-b['delta_S_J_mol_K'],places=9)
 def test_cp_invalid_range(self):
  with self.assertRaises(ChemistryModelError):shomate_thermochemistry(40,2,3,4,5,200,400,250,600)
 def test_eq_cp_zero(self):
  r=equilibrium_with_heat_capacity(298,400,-100000,-200,0)
  self.assertEqual(r['delta_H_J_mol'],-100000);self.assertEqual(r['delta_S_J_mol_K'],-200)
 def test_eq_free_energy(self):
  r=equilibrium_with_heat_capacity(300,350,-10000,-40,10)
  self.assertAlmostEqual(r['delta_G_J_mol'],r['delta_H_J_mol']-350*r['delta_S_J_mol_K'])
 def test_eq_ref(self):
  r=equilibrium_with_heat_capacity(300,300,-10000,-40,10)
  self.assertAlmostEqual(r['delta_G_J_mol'],2000)

class Electrochemistry(unittest.TestCase):
 def test_work(self):self.assertAlmostEqual(electrochemical_work_bound(1.5,2)['reversible_work_magnitude_J'],3*FARADAY)
 def test_work_negative_reversal(self):self.assertEqual(electrochemical_work_bound(-1.5,1)['reversible_work_magnitude_J'],electrochemical_work_bound(1.5,1)['reversible_work_magnitude_J'])
 def test_work_overunit_efficiency(self):
  with self.assertRaises(ChemistryModelError):electrochemical_work_bound(1,1,1.1)
 def test_faraday_one_mole(self):self.assertAlmostEqual(faradaic_yield(FARADAY,1)['theoretical_mol'],1)
 def test_faraday_two_electrons(self):self.assertAlmostEqual(faradaic_yield(FARADAY,2)['theoretical_mol'],.5)
 def test_faraday_invalid_count(self):
  with self.assertRaises(ChemistryModelError):faradaic_yield(FARADAY,1.3)
 def test_faraday_zero(self):self.assertEqual(faradaic_yield(0,1)['theoretical_mol'],0)

class StructureAndUncertainty(unittest.TestCase):
 def test_bragg_30(self):self.assertAlmostEqual(bragg_first_order_spacing(.15,30)['d_spacing_nm'],.15)
 def test_bragg_second(self):self.assertAlmostEqual(bragg_first_order_spacing(.15,30,2)['d_spacing_nm'],.30)
 def test_bragg_theta_not_2theta(self):self.assertGreater(bragg_first_order_spacing(.15,15)['d_spacing_nm'],bragg_first_order_spacing(.15,30)['d_spacing_nm'])
 def test_bragg_zero_reject(self):
  with self.assertRaises(ChemistryModelError):bragg_first_order_spacing(.15,0)
 def test_uncorrelated_product(self):self.assertAlmostEqual(uncertainty_product(2,3,.1,.2)['standard_uncertainty'],math.sqrt(.25))
 def test_product_covariance(self):self.assertGreater(uncertainty_product(2,3,.1,.2,.015)['standard_uncertainty'],uncertainty_product(2,3,.1,.2)['standard_uncertainty'])
 def test_invalid_covariance(self):
  with self.assertRaises(ChemistryModelError):uncertainty_product(1,1,0,0,.001)
 def test_zero_uncertainty(self):self.assertEqual(uncertainty_product(1,1,0,0)['standard_uncertainty'],0)
 def test_nan_refused(self):
  with self.assertRaises(ChemistryModelError):varshni_bandgap(float('nan'),1,.01,100)
 def test_random_bragg_monotonic(self):
  for n in range(10,80,10):self.assertGreater(bragg_first_order_spacing(.1,n)['d_spacing_nm'],bragg_first_order_spacing(.1,n+1)['d_spacing_nm'])

if __name__=='__main__':unittest.main()
