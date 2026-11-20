import unittest,random,math,hashlib
from chemistry_atlas.models import ChemistryModelError,R_GAS
from chemistry_atlas.advanced import *
from chemistry_atlas.advanced_cases import advanced_casebook

class ChargeBalance(unittest.TestCase):
 def specie(self,name,atoms,charge):return {'label':name,'atoms':atoms,'charge':charge}
 def test_cases(self):self.assertEqual(advanced_casebook()['status'],'passed');self.assertEqual(advanced_casebook()['count'],14)
 def test_acid(self):
  x=balance_charge_and_atoms([self.specie('H+',{'H':1},1),self.specie('OH-',{'O':1,'H':1},-1)],[self.specie('H2O',{'H':2,'O':1},0)])
  self.assertEqual(x['coefficient_vector'],[1,1,1]);self.assertEqual(x['charge_residual'],0)
 def test_electron(self):
  x=balance_charge_and_atoms([self.specie('Fe3+',{'Fe':1},3),self.specie('e-',{},-1)],[self.specie('Fe2+',{'Fe':1},2)])
  self.assertTrue(x['math_conservation_verified']);self.assertFalse(x['physical_reaction_verified'])
 def test_bad_charge(self):
  with self.assertRaises(ChemistryModelError):balance_charge_and_atoms([self.specie('A',{'Fe':1},2)],[self.specie('B',{'Fe':1},3)])
 def test_duplicate(self):
  with self.assertRaises(ChemistryModelError):balance_charge_and_atoms([self.specie('A',{'H':1},0),self.specie('A',{'O':1},0)],[self.specie('B',{'H':1,'O':1},0)])
 def test_wrong_electron(self):
  with self.assertRaises(ChemistryModelError):balance_charge_and_atoms([self.specie('e',{},0)],[self.specie('Fe',{'Fe':1},0)])
 def test_underdetermined(self):
  with self.assertRaises(ChemistryModelError):balance_charge_and_atoms([self.specie('A',{'H':2},0),self.specie('B',{'H':1},0)],[self.specie('C',{'H':2},0)])
 def test_bool_charge(self):
  with self.assertRaises(ChemistryModelError):balance_charge_and_atoms([self.specie('A',{'H':1},True)],[self.specie('B',{'H':1},0)])
 def test_negative_atoms(self):
  with self.assertRaises(ChemistryModelError):balance_charge_and_atoms([self.specie('A',{'H':-1},0)],[self.specie('B',{'H':1},0)])

class Thermo(unittest.TestCase):
 def row(self,name,G,H):return {'id':name,'coefficient':1,'gibbs_formation_J_mol':G,'enthalpy_formation_J_mol':H}
 def test_delta(self):
  x=thermodynamic_reaction_delta([self.row('A',-1,-1)],[self.row('B',-10,-9)],300)
  self.assertEqual(x['delta_G_standard_J_per_mol_reaction'],-9);self.assertEqual(x['delta_H_standard_J_per_mol_reaction'],-8)
 def test_refuses_unobserved(self):
  with self.assertRaises(ChemistryModelError):thermodynamic_reaction_delta([{'id':'A','coefficient':1,'gibbs_formation_J_mol':1}], [self.row('B',1,1)],300)
 def test_logK_zero(self):self.assertAlmostEqual(thermodynamic_reaction_delta([self.row('A',0,0)],[self.row('B',0,0)],300)['log_equilibrium_constant'],0)
 def test_invalid_temperature(self):
  with self.assertRaises(ChemistryModelError):thermodynamic_reaction_delta([self.row('A',0,0)],[self.row('B',0,0)],0)
 def test_vanthoff_exact_ref(self):self.assertEqual(vanthoff_logK(10,300,300,1000)['logK_target'],10)
 def test_vanthoff_endothermic_increase(self):self.assertGreater(vanthoff_logK(0,300,400,1000)['logK_target'],0)
 def test_vanthoff_sign(self):self.assertLess(vanthoff_logK(0,300,400,-1000)['logK_target'],0)
 def test_overflow_refusal(self):self.assertIsNone(vanthoff_logK(0,300,301,1e10)['ratio_K_target_to_reference'])
 def test_bad_T(self):
  with self.assertRaises(ChemistryModelError):vanthoff_logK(1,0,300,100)

class SolutionChemistry(unittest.TestCase):
 def test_ionic_strength(self):
  x=ionic_strength([{'ion':'a','molarity_mol_L':.02,'charge':2},{'ion':'b','molarity_mol_L':.04,'charge':-1}]);self.assertAlmostEqual(x['I_molarity_basis_mol_L'],.06)
 def test_charge_imbalance_preserved(self):self.assertFalse(ionic_strength([{'ion':'a','molarity_mol_L':.01,'charge':2}])['electroneutrality_proven'])
 def test_duplicate_ion(self):
  a={'ion':'a','molarity_mol_L':.01,'charge':1}
  with self.assertRaises(ChemistryModelError):ionic_strength([a,a])
 def test_debye_at_zero(self):self.assertEqual(debye_huckel_limiting_log_gamma(1,0,0.509)['gamma'],1)
 def test_debye_charge_squared(self):self.assertAlmostEqual(debye_huckel_limiting_log_gamma(2,.001,.509)['log10_mean_idealized_gamma'],4*debye_huckel_limiting_log_gamma(1,.001,.509)['log10_mean_idealized_gamma'])
 def test_debye_concentration_refusal(self):
  with self.assertRaises(ChemistryModelError):debye_huckel_limiting_log_gamma(1,.1,.509)
 def test_debye_noncharge(self):
  with self.assertRaises(ChemistryModelError):debye_huckel_limiting_log_gamma(0,.001,.509)

class Semiconductor(unittest.TestCase):
 def test_intrinsic(self):
  x=semiconductor_carrier_neutrality(0,1e16);self.assertAlmostEqual(x['electron_density_m3'],1e16);self.assertAlmostEqual(x['hole_density_m3'],1e16)
 def test_donor(self):self.assertGreater(semiconductor_carrier_neutrality(1e20,1e16)['electron_density_m3'],1e20)
 def test_acceptor(self):self.assertGreater(semiconductor_carrier_neutrality(-1e20,1e16)['hole_density_m3'],1e20)
 def test_mass_action(self):
  rng=random.Random(31)
  for _ in range(160):
   net=(rng.random()*2-1)*1e20;ni=10**rng.uniform(10,19);x=semiconductor_carrier_neutrality(net,ni)
   self.assertAlmostEqual(x['electron_density_m3']*x['hole_density_m3']/ni**2,1,delta=1e-10)
   self.assertAlmostEqual((x['electron_density_m3']-x['hole_density_m3']-net)/max(1,abs(net)),0,delta=1e-10)
 def test_ni_zero(self):
  with self.assertRaises(ChemistryModelError):semiconductor_carrier_neutrality(1e20,0)

class TransportAndMeasurement(unittest.TestCase):
 def test_flux_gradient(self):self.assertGreater(fick_flux_1d(1e-12,2,1,.1)['flux_mol_m2_s'],0)
 def test_flux_zero_D(self):self.assertEqual(fick_flux_1d(0,2,1,.1)['flux_mol_m2_s'],0)
 def test_d_zero_reject(self):
  with self.assertRaises(ChemistryModelError):fick_flux_1d(1e-12,2,1,0)
 def test_diffusion_conservation(self):
  a=diffuse_no_flux_1d([0.,0.,1.,0.,0.],.1,1,1,30)
  self.assertAlmostEqual(a['integral_after_mol_m2'],a['integral_before_mol_m2'],delta=1e-11)
 def test_reflect_symmetry(self):
  a=diffuse_no_flux_1d([0.,0.,1.,0.,0.],.2,1,1,20)['concentrations_mol_m3'];self.assertEqual(a,a[::-1])
 def test_cfl_reject(self):
  with self.assertRaises(ChemistryModelError):diffuse_no_flux_1d([1.,0.],1.,1.,1.,1)
 def test_diffusion_zero(self):self.assertEqual(diffuse_no_flux_1d([1.,2.],0,1,1,10)['concentrations_mol_m3'],[1.,2.])
 def test_beer(self):self.assertAlmostEqual(beer_lambert_absorbance(100,1,.01)['absorbance_decadic'],1)
 def test_beer_low_transmission(self):self.assertIsNone(beer_lambert_absorbance(1e5,1,.01)['transmitted_fraction_ideal'])
 def test_invalid_absorbance(self):
  with self.assertRaises(ChemistryModelError):beer_lambert_absorbance(1,-1,.02)

class SourceFixity(unittest.TestCase):
 def test_matching_hash_not_license(self):
  b=b'original constructed bytes';r=source_bytes_audit(b,hashlib.sha256(b).hexdigest(),'test','cleared_for_archive')
  self.assertTrue(r['matches_supplied_expected_digest']);self.assertFalse(r['automatically_republishable']);self.assertFalse(r['publisher_origin_authenticated'])
 def test_wrong_hash(self):self.assertFalse(source_bytes_audit(b'abc','f'*64,'test','restricted')['matches_supplied_expected_digest'])
 def test_restricted(self):
  b=b'abc';x=source_bytes_audit(b,hashlib.sha256(b).hexdigest(),'test','restricted');self.assertFalse(x['eligible_for_external_rights_review'])
 def test_bad_sha(self):
  with self.assertRaises(ChemistryModelError):source_bytes_audit(b'abc','ABC','test','unknown')
 def test_absent_bytes(self):self.assertFalse(source_bytes_audit(None,None,'test','unknown')['local_bytes_present'])

if __name__=='__main__':unittest.main()
