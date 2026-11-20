import unittest,math,random
from fractions import Fraction
from chemistry_atlas.models import *
from chemistry_atlas.cases import casebook

class ChemistryTests(unittest.TestCase):
 def test_casebook(self):self.assertEqual(casebook()['status'],'passed');self.assertEqual(casebook()['case_count'],25)
 def test_formula_nesting(self):self.assertEqual(parse_formula('Ca3(PO4)2'),{'Ca':3,'O':8,'P':2})
 def test_formula_double_nested(self):self.assertEqual(parse_formula('K4(ON(SO3)2)2'),{'K':4,'N':2,'O':14,'S':4})
 def test_formula_single(self):self.assertEqual(parse_formula('NaCl'),{'Cl':1,'Na':1})
 def test_formula_malformed(self):
  for bad in ('H2O+','2H','Mg()2','(H2O','H2O)','', 'O0','H1000001','H(2)'):
   with self.subTest(bad=bad),self.assertRaises(ChemistryModelError):parse_formula(bad)
 def test_charge_not_supported(self):
  with self.assertRaises(ChemistryModelError):parse_formula('Na+')
 def test_balancing_simple(self):self.assertEqual(balance_reaction(['H2','O2'],['H2O'])['coefficient_vector'],[2,1,2])
 def test_balancing_iron(self):self.assertEqual(balance_reaction(['Fe','O2'],['Fe2O3'])['coefficient_vector'],[4,3,2])
 def test_balancing_salt(self):self.assertEqual(balance_reaction(['Ca(OH)2','HCl'],['CaCl2','H2O'])['coefficient_vector'],[1,2,1,2])
 def test_underdetermined(self):
  with self.assertRaises(ChemistryModelError):balance_reaction(['H2','O2','H2O2'],['H2O'])
 def test_impossible(self):
  with self.assertRaises(ChemistryModelError):balance_reaction(['H2'],['H2O'])
 def test_same_species_refuses(self):
  with self.assertRaises(ChemistryModelError):balance_reaction(['H2'],['H2'])
 def test_balance_rational_coeff(self):self.assertTrue(atom_balance(['H2','O2'],['H2O'],[1,Fraction(1,2)],[1])['balanced'])
 def test_balance_false(self):self.assertFalse(atom_balance(['H2'],['H'],[1],[1])['balanced'])
 def test_molar_mass(self):self.assertAlmostEqual(molar_mass('H2O',{'H':1.008,'O':15.999})['molar_mass_g_mol'],18.015)
 def test_molar_missing(self):
  with self.assertRaises(ChemistryModelError):molar_mass('NaCl',{'Na':23})
 def test_amount(self):self.assertEqual(amount_of_substance(18.015,18.015)['moles'],1)
 def test_amount_zero_mass(self):self.assertEqual(amount_of_substance(0,18)['moles'],0)
 def test_amount_negative(self):
  with self.assertRaises(ChemistryModelError):amount_of_substance(-1,18)
 def test_limiting(self):self.assertEqual(limiting_extent({'X':3,'Y':4},{'X':1,'Y':2})['max_reaction_extent_mol'],2)
 def test_limiting_tie(self):self.assertEqual(limiting_extent({'X':2,'Y':4},{'X':1,'Y':2})['limiting_species'],['X','Y'])
 def test_limiting_bad_species(self):
  with self.assertRaises(ChemistryModelError):limiting_extent({'X':2},{'Y':1})
 def test_solution(self):self.assertEqual(solution_molarity(.4,2)['molarity_mol_L'],.2)
 def test_solution_zero_volume(self):
  with self.assertRaises(ChemistryModelError):solution_molarity(.4,0)
 def test_dilution(self):self.assertAlmostEqual(dilution(.3,2,3)['final_concentration_mol_L'],.2)
 def test_dilution_no_concentrating(self):
  with self.assertRaises(ChemistryModelError):dilution(.3,2,1)
 def test_ideal_gas(self):self.assertAlmostEqual(ideal_gas_pressure(1,300,1)['pressure_Pa'],R_GAS*300)
 def test_gas_zero_K(self):
  with self.assertRaises(ChemistryModelError):ideal_gas_pressure(1,0,1)
 def test_gas_inverse_volume(self):self.assertAlmostEqual(ideal_gas_pressure(1,300,1)['pressure_Pa'],2*ideal_gas_pressure(1,300,2)['pressure_Pa'])
 def test_equilibrium_dG(self):self.assertAlmostEqual(reaction_free_energy(0,298,1)['delta_G_reaction_j_mol'],0)
 def test_equilibrium_lnK(self):self.assertAlmostEqual(equilibrium_constant(-R_GAS*300,300)['ln_K_dimensionless'],1)
 def test_equilibrium_Q_zero(self):
  with self.assertRaises(ChemistryModelError):reaction_free_energy(0,300,0)
 def test_hess(self):self.assertEqual(reaction_enthalpy({'A':-20,'B':-10},{'A':1},{'B':1})['delta_H_reaction_j_per_extent_mol'],10)
 def test_hess_missing(self):
  with self.assertRaises(ChemistryModelError):reaction_enthalpy({'A':0},{'A':1},{'B':1})
 def test_arrhenius_sameT(self):self.assertEqual(arrhenius_log_ratio(10000,300,300)['ln_k2_over_k1'],-0.0)
 def test_arrhenius_temperature(self):self.assertGreater(arrhenius_log_ratio(10000,300,320)['k2_over_k1'],1)
 def test_decay_halflife(self):self.assertAlmostEqual(first_order_kinetics(1,.2,math.log(2)/.2)['concentration_mol_L'],.5)
 def test_decay_zero(self):self.assertIsNone(first_order_kinetics(1,0,10)['half_life_s'])
 def test_activity_pH(self):self.assertAlmostEqual(pH_from_activity(1e-7)['pH'],7)
 def test_activity_over_one(self):self.assertLess(pH_from_activity(2)['pH'],0)
 def test_buffer_equal(self):self.assertEqual(henderson_hasselbalch(5,1,1)['pH_ideal_ratio'],5)
 def test_buffer_zero(self):
  with self.assertRaises(ChemistryModelError):henderson_hasselbalch(5,1,0)
 def test_nernst_one(self):self.assertEqual(nernst_potential(.3,1,298.15,1)['potential_V'],.3)
 def test_nernst_lowered(self):self.assertLess(nernst_potential(.3,1,300,2)['potential_V'],.3)
 def test_nernst_bad_n(self):
  with self.assertRaises(ChemistryModelError):nernst_potential(.3,1.2,300,2)
 def test_faraday_defining(self):self.assertAlmostEqual(faraday_charge(1)['charge_C'],96485.33212331002,places=6)
 def test_conductivity(self):self.assertGreater(conductivity_semiconductor(1e21,0,.1,0)['conductivity_S_m'],0)
 def test_conductivity_zero(self):self.assertIsNone(conductivity_semiconductor(0,0,0,0)['resistivity_ohm_m'])
 def test_diffusion(self):self.assertAlmostEqual(diffusion_length(2,4,1)['rms_displacement_m'],4)
 def test_diffusion_dimensions(self):self.assertAlmostEqual(diffusion_length(2,4,3)['rms_displacement_m'],math.sqrt(3)*4)
 def test_diffusion_invalid_dimension(self):
  with self.assertRaises(ChemistryModelError):diffusion_length(1,1,0)
 def test_mass_balance(self):self.assertEqual(mass_balance_process([10],[4,5],1)['unaccounted_residual_kg'],0)
 def test_mass_residual(self):self.assertEqual(mass_balance_process([10],[4,5],0)['unaccounted_residual_kg'],1)
 def test_nan_refused(self):
  with self.assertRaises(ChemistryModelError):ideal_gas_pressure(float('nan'),300,1)
 def test_bool_refused(self):
  with self.assertRaises(ChemistryModelError):faraday_charge(True)
 def test_random_conservation(self):
  rng=random.Random(18)
  for _ in range(50):
   a=rng.randint(1,20);b=rng.randint(1,20)
   c=atom_balance(['H2','O2'],['H2O'],[2*a*b,a*b],[2*a*b])
   self.assertTrue(c['balanced'])
