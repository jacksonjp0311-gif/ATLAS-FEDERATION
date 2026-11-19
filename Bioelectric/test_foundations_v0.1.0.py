import unittest,math
from bioelectric_atlas.foundations import *

class Fundamentals(unittest.TestCase):
 def test_boltzmann_avogadro_values(self):
  self.assertAlmostEqual(GAS_CONSTANT,8.31446261815324,places=9)
  self.assertAlmostEqual(FARADAY,96485.33212331,places=7)
 def test_thermal_300k(self):
  self.assertAlmostEqual(thermal_voltage(300),0.0258519997864,places=9)
 def test_nernst_unity(self):
  self.assertEqual(nernst_potential(1,1,1,300),0)
 def test_nernst_reversal(self):
  self.assertAlmostEqual(nernst_potential(1,2,4,300),-nernst_potential(1,4,2,300),places=12)
 def test_nernst_anion_sign(self):
  self.assertAlmostEqual(nernst_potential(-1,2,4,300),-nernst_potential(1,2,4,300),places=12)
 def test_nernst_chemical_temperature(self):
  self.assertAlmostEqual(nernst_potential(1,1,10,300)*2,nernst_potential(1,1,10,600))
 def test_nernst_valence_scaling(self):
  self.assertAlmostEqual(nernst_potential(2,1,10,300),nernst_potential(1,1,10,300)/2)
 def test_ghk_pure_k(self):
  x=ghk_voltage(1,0,0,140,5,10,110,4,104,310)
  self.assertAlmostEqual(x,nernst_potential(1,140,5,310))
 def test_ghk_pure_na(self):
  x=ghk_voltage(0,1,0,140,5,10,110,4,104,310)
  self.assertAlmostEqual(x,nernst_potential(1,10,110,310))
 def test_ghk_pure_chloride_anion(self):
  x=ghk_voltage(0,0,1,140,5,10,110,4,104,310)
  self.assertAlmostEqual(x,nernst_potential(-1,4,104,310))
 def test_ghk_equal_symmetric(self):
  self.assertEqual(ghk_voltage(1,1,1,10,10,10,10,10,10,300),0)
 def test_ghk_scale_permeability(self):
  args=(140,5,10,110,4,104,310)
  self.assertAlmostEqual(ghk_voltage(1,0.1,0.01,*args),ghk_voltage(100,10,1,*args))
 def test_bad_nernst_concentration(self):
  for x in (0,-1,float('nan'),float('inf'),True):
   with self.assertRaises(ValueError):nernst_potential(1,x,5,300)
 def test_bad_nernst_valence(self):
  for x in (0,True,0.5,9):
   with self.assertRaises(ValueError):nernst_potential(x,1,2,300)
 def test_bad_temperature(self):
  for x in (0,-1,True,float('nan')):
   with self.assertRaises(ValueError):thermal_voltage(x)
 def test_ghk_all_zero_permeability(self):
  with self.assertRaises(ValueError):ghk_voltage(0,0,0,1,1,1,1,1,1,300)
 def test_ghk_zero_concentration(self):
  with self.assertRaises(ValueError):ghk_voltage(1,1,1,0,1,1,1,1,1,300)
 def test_parallel_conductance_weighted(self):
  d=conductance_equilibrium([2,1],[-0.1,0.2]);self.assertAlmostEqual(d['equilibrium_volts'],0)
 def test_parallel_applied_current(self):
  d=conductance_equilibrium([2],[-0.1],0.2);self.assertAlmostEqual(d['equilibrium_volts'],0)
 def test_parallel_zero_g_refused(self):
  with self.assertRaises(ValueError):conductance_equilibrium([0,0],[-0.1,0.1])
 def test_passive_exact_tau(self):
  x=passive_membrane_voltage(1,0,1e-6,1e-3,0.001)
  self.assertAlmostEqual(x['voltage_volts'],1/math.e)
 def test_passive_nonzero_current(self):
  x=passive_membrane_voltage(0,0,1e-6,1e-3,100,1e-3)
  self.assertAlmostEqual(x['steady_state_volts'],1)
  self.assertAlmostEqual(x['voltage_volts'],1)
 def test_passive_time_zero(self):
  self.assertEqual(passive_membrane_voltage(0.5,0,1,1,0)['voltage_volts'],0.5)
 def test_passive_zero_conductance_refused(self):
  with self.assertRaises(ValueError):passive_membrane_voltage(0,0,1,0,2)
 def test_energy_positive(self):
  self.assertAlmostEqual(capacitor_stored_energy(2,3),9)
 def test_energy_even_in_voltage(self):
  self.assertEqual(capacitor_stored_energy(4,10),capacitor_stored_energy(4,-10))
 def test_capacitance_area(self):
  self.assertAlmostEqual(membrane_surface_capacitance(0.5,0.02),0.01)

if __name__=='__main__':unittest.main()
