import unittest,sys,json,math,random
from pathlib import Path
from materials_atlas.methods import (MaterialsInputError,lattice_density,bragg_spacing,lever_rule,thermal_mismatch,
      engineering_tensile_point,mixture_modulus_bounds,formation_energy_per_atom,binary_hull_distance,compare_properties)
from materials_atlas.cases import casebook

class TestMaterialsMethods(unittest.TestCase):
    def test_density(self):
        r=lattice_density(atomic_mass_g_per_mol=63.546,atoms_per_cell=4,cubic_a_angstrom=4)
        self.assertAlmostEqual(r['density_g_cm3'],6.5947,places=3)
    def test_density_zero(self):
        with self.assertRaises(MaterialsInputError):lattice_density(atomic_mass_g_per_mol=1,atoms_per_cell=0,cubic_a_angstrom=4)
    def test_density_too_small(self):
        with self.assertRaises(MaterialsInputError):lattice_density(atomic_mass_g_per_mol=1,atoms_per_cell=1,cubic_a_angstrom=0)
    def test_density_nan(self):
        with self.assertRaises(MaterialsInputError):lattice_density(atomic_mass_g_per_mol=float('nan'),atoms_per_cell=1,cubic_a_angstrom=2)
    def test_bragg(self):
        self.assertAlmostEqual(bragg_spacing(wavelength_angstrom=1.54,two_theta_degrees=44)['d_angstrom'],1.54/(2*math.sin(math.radians(22))))
    def test_bragg_second_order(self):
        self.assertAlmostEqual(bragg_spacing(wavelength_angstrom=1,two_theta_degrees=60,order=2)['d_angstrom'],2)
    def test_bragg_outside_range(self):
        for x in (0,180,-1,181):
            with self.subTest(x=x),self.assertRaises(MaterialsInputError):bragg_spacing(wavelength_angstrom=1,two_theta_degrees=x)
    def test_bragg_boolean_order(self):
        with self.assertRaises(MaterialsInputError):bragg_spacing(wavelength_angstrom=1,two_theta_degrees=40,order=True)
    def test_lever(self):
        r=lever_rule(overall_fraction_b=.4,alpha_fraction_b=.2,beta_fraction_b=.7)
        self.assertAlmostEqual(r['fraction_beta'],.4);self.assertAlmostEqual(r['fraction_alpha'],.6)
    def test_lever_endpoints(self):
        self.assertEqual(lever_rule(overall_fraction_b=.2,alpha_fraction_b=.2,beta_fraction_b=.8)['fraction_beta'],0)
    def test_lever_invalid(self):
        for val in (-.2,.1,.95,1.1):
            with self.subTest(v=val),self.assertRaises(MaterialsInputError):lever_rule(overall_fraction_b=val,alpha_fraction_b=.2,beta_fraction_b=.8)
    def test_lever_equal_endpoints(self):
        with self.assertRaises(MaterialsInputError):lever_rule(overall_fraction_b=.5,alpha_fraction_b=.5,beta_fraction_b=.5)
    def test_thermal(self):
        self.assertAlmostEqual(thermal_mismatch(alpha_a_per_k=23e-6,alpha_b_per_k=12e-6,delta_temperature_k=60)['microstrain_difference'],660)
    def test_thermal_signed(self):
        self.assertLess(thermal_mismatch(alpha_a_per_k=23e-6,alpha_b_per_k=12e-6,delta_temperature_k=-60)['free_strain_difference'],0)
    def test_stress(self):
        r=engineering_tensile_point(force_newtons=5000,area_mm2=20,elongation_mm=.5,gauge_length_mm=50)
        self.assertEqual(r['engineering_stress_mpa'],250);self.assertEqual(r['engineering_strain'],.01)
    def test_stress_bad_geometry(self):
        with self.assertRaises(MaterialsInputError):engineering_tensile_point(force_newtons=1,area_mm2=0,elongation_mm=1,gauge_length_mm=3)
    def test_mixture(self):
        r=mixture_modulus_bounds(modulus_a_gpa=200,modulus_b_gpa=3,volume_fraction_a=.3)
        self.assertAlmostEqual(r['iso_strain_voigt_gpa'],62.1)
        self.assertLess(r['iso_stress_reuss_gpa'],r['iso_strain_voigt_gpa'])
    def test_mixture_negative_fraction(self):
        with self.assertRaises(MaterialsInputError):mixture_modulus_bounds(modulus_a_gpa=200,modulus_b_gpa=3,volume_fraction_a=1.2)
    def test_formation(self):
        r=formation_energy_per_atom(total_energy_ev=-11,formula_counts={'A':1,'B':2},element_reference_ev_per_atom={'A':-2,'B':-3})
        self.assertAlmostEqual(r['formation_energy_ev_per_atom'],-1)
    def test_formation_missing_species(self):
        with self.assertRaises(MaterialsInputError):formation_energy_per_atom(total_energy_ev=-11,formula_counts={'A':1},element_reference_ev_per_atom={'B':-2})
    def test_formation_bad_stoichiometry(self):
        with self.assertRaises(MaterialsInputError):formation_energy_per_atom(total_energy_ev=-11,formula_counts={'A':0},element_reference_ev_per_atom={'A':-2})
    def test_hull(self):
        r=binary_hull_distance(phases=[{'id':'A','x_b':0,'energy_ev_atom':0},{'id':'AB','x_b':.5,'energy_ev_atom':-.4},{'id':'B','x_b':1,'energy_ev_atom':0}],candidate_x_b=.3,candidate_energy_ev_atom=-.18)
        self.assertAlmostEqual(r['hull_energy_ev_per_atom'],-.24)
        self.assertAlmostEqual(r['signed_candidate_minus_hull_ev_atom'],.06)
        self.assertFalse(r['candidate_below_reference_hull'])
    def test_hull_low(self):
        r=binary_hull_distance(phases=[{'id':'A','x_b':0,'energy_ev_atom':0},{'id':'B','x_b':1,'energy_ev_atom':0}],candidate_x_b=.5,candidate_energy_ev_atom=-.2)
        self.assertTrue(r['candidate_below_reference_hull'])
    def test_hull_missing_elemental_endpoint(self):
        with self.assertRaises(MaterialsInputError):binary_hull_distance(phases=[{'id':'A','x_b':0,'energy_ev_atom':0},{'id':'AB','x_b':.5,'energy_ev_atom':-.2}],candidate_x_b=.3,candidate_energy_ev_atom=-.18)
    def test_hull_duplicate_id(self):
        with self.assertRaises(MaterialsInputError):binary_hull_distance(phases=[{'id':'A','x_b':0,'energy_ev_atom':0},{'id':'A','x_b':1,'energy_ev_atom':0}],candidate_x_b=.5,candidate_energy_ev_atom=1)
    def test_hull_endpoints(self):
        phases=[{'id':'A','x_b':0,'energy_ev_atom':0},{'id':'B','x_b':1,'energy_ev_atom':0}]
        self.assertEqual(binary_hull_distance(phases=phases,candidate_x_b=0,candidate_energy_ev_atom=0)['hull_energy_ev_per_atom'],0)
    def test_compare_pass(self):
        a={'property':'yield','unit':'MPa','method':'M1','temperature_k':300,'direction':'rolling','condition':'annealed','origin':'measured','value':200,'uncertainty':5}
        b=dict(a,value=210)
        self.assertEqual(compare_properties(a,b)['difference_a_minus_b'],-10)
    def test_compare_method_mismatch(self):
        a={'property':'yield','unit':'MPa','method':'M1','temperature_k':300,'direction':'rolling','condition':'annealed','origin':'measured','value':200,'uncertainty':5}
        with self.assertRaises(MaterialsInputError):compare_properties(a,dict(a,method='M2'))
    def test_compare_temperature_mismatch(self):
        a={'property':'yield','unit':'MPa','method':'M1','temperature_k':300,'direction':'rolling','condition':'annealed','origin':'measured','value':200,'uncertainty':5}
        with self.assertRaises(MaterialsInputError):compare_properties(a,dict(a,temperature_k=400))
    def test_compare_predicted_measured_refusal(self):
        a={'property':'modulus','unit':'GPa','method':'M1','temperature_k':300,'direction':'rolling','condition':'annealed','origin':'measured','value':200,'uncertainty':5}
        with self.assertRaises(MaterialsInputError):compare_properties(a,dict(a,origin='computed'))
    def test_casebook(self):self.assertEqual(casebook()['status'],'passed')

class TestMaterialsRandomProperties(unittest.TestCase):
    def test_300_lever_mass_balances(self):
        rng=random.Random(741);count=0
        for _ in range(300):
            a=rng.random()*.4;b=.6+rng.random()*.4;c=a+rng.random()*(b-a)
            x=lever_rule(overall_fraction_b=c,alpha_fraction_b=a,beta_fraction_b=b)
            self.assertAlmostEqual(x['fraction_alpha']*a+x['fraction_beta']*b,c,delta=3e-15)
            count+=1
        self.assertEqual(count,300)
    def test_200_mixture_ordering(self):
        rng=random.Random(112)
        for _ in range(200):
            ea=1+1000*rng.random();eb=1+1000*rng.random();v=rng.random()
            x=mixture_modulus_bounds(modulus_a_gpa=ea,modulus_b_gpa=eb,volume_fraction_a=v)
            self.assertLessEqual(x['iso_stress_reuss_gpa'],x['iso_strain_voigt_gpa']+1e-11)
    def test_100_hull_not_above_single_endpoints(self):
        rng=random.Random(421)
        for _ in range(100):
            em=-rng.random();x=rng.random();phases=[{'id':'A','x_b':0,'energy_ev_atom':0},{'id':'mid','x_b':.5,'energy_ev_atom':em},{'id':'B','x_b':1,'energy_ev_atom':0}]
            calc=binary_hull_distance(phases=phases,candidate_x_b=x,candidate_energy_ev_atom=0)
            self.assertLessEqual(calc['hull_energy_ev_per_atom'],0)

if __name__=='__main__':unittest.main()
