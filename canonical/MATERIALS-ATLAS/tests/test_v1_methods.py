# SRD69_PUBLIC_DERIVATIVE
import json,math,unittest
from pathlib import Path
from materials_atlas.v1_methods import *
from materials_atlas.v1_cases import v1_casebook

@unittest.skip('NIST SRD69 redistribution clearance pending; inputs and direct numerical outputs withheld from this public derivative.')
class ShomateTests(unittest.TestCase):
    def test_reference_copper_table(self):
        from materials_atlas.v1_cases import NIST_CU_CHECKS
        for T,cp,h,s in NIST_CU_CHECKS:
            d=copper_solid_shomate(T)
            for key,expected in [('Cp_J_per_mol_K',cp),('H_relative_29815_kJ_per_mol',h),('S_J_per_mol_K',s)]:
                self.assertLessEqual(abs(d[key]-expected),0.00501)
    def test_derivative_of_enthalpy_equals_heat_capacity(self):
        for t in [300,320,400,700,900,1200,1350]:
            h0=copper_solid_shomate(t-.0001)['H_relative_29815_kJ_per_mol']
            h1=copper_solid_shomate(t+.0001)['H_relative_29815_kJ_per_mol']
            cp=copper_solid_shomate(t)['Cp_J_per_mol_K']
            self.assertAlmostEqual(1000*(h1-h0)/.0002,cp,places=5)
    def test_stated_temperature_range(self):
        for t in [0,273.15,297.99,1358.01,3000,float('inf'),float('nan')]:
            with self.assertRaises(ValueError):copper_solid_shomate(t)
        for t in [298,1358]:self.assertTrue(copper_solid_shomate(t)['Cp_J_per_mol_K']>0)
    def test_reference_change(self):
        self.assertAlmostEqual(copper_enthalpy_change(400,900)['delta_H_kJ_per_mol'],
            -copper_enthalpy_change(900,400)['delta_H_kJ_per_mol'])

class CorrosionTests(unittest.TestCase):
    def test_derived_units_and_scaling(self):
        x=corrosion_uniform_loss_mm_year(.1,100,240,7.8)['equivalent_uniform_penetration_mm_per_year']
        self.assertAlmostEqual(x,0.1*87600/(100*240*7.8))
        self.assertAlmostEqual(corrosion_uniform_loss_mm_year(.2,100,240,7.8)['equivalent_uniform_penetration_mm_per_year'],2*x)
    def test_refusal(self):
        for args in [(-1,10,10,5),(.1,0,10,5),(.1,10,0,5),(.1,10,10,0),(.1,10,10,float('nan'))]:
            with self.assertRaises(ValueError):corrosion_uniform_loss_mm_year(*args)

class ThermalTests(unittest.TestCase):
    def test_resistance_contact_and_reverse_direction(self):
        a=series_conduction([(0.001,200),(0.005,1)],.1,50,(.3,))
        self.assertAlmostEqual(a['thermal_resistance_K_per_W'],.35005)
        b=series_conduction([(0.001,200),(0.005,1)],.1,-50,(.3,))
        self.assertAlmostEqual(b['heat_rate_W'],-a['heat_rate_W'])
    def test_contact_reduces_flux(self):
        a=series_conduction([(.01,1)],.1,100,())['heat_rate_W']
        b=series_conduction([(.01,1)],.1,100,(1,))['heat_rate_W']
        self.assertLess(b,a)
    def test_refuse_bad_conductivity(self):
        with self.assertRaises(ValueError):series_conduction([(.1,0)],.1,100)

class PhaseAndCreep(unittest.TestCase):
    def test_avrami(self):
        t=avrami_time_to_fraction(.01,3,.8)
        self.assertAlmostEqual(avrami_isothermal(.01,3,t)['fraction_transformed'],.8)
        self.assertEqual(avrami_isothermal(.01,3,0)['fraction_transformed'],0)
    def test_avrami_bad_fraction(self):
        for x in [0,1,-.1,1.2,float('nan')]:
            with self.assertRaises(ValueError):avrami_time_to_fraction(.01,3,x)
    def test_norton_stress_exponent(self):
        def f(s):return norton_steady_creep(s,1000,1e-8,3,150000,3600)['model_steady_strain_rate_per_s']
        self.assertAlmostEqual(f(100)/f(50),8)
    def test_creep_no_rupture_claim(self):
        d=norton_steady_creep(100,1000,1e-8,3,100000,3600)
        self.assertTrue(any('rupture' in x for x in d['limitations']))

class WeakestLink(unittest.TestCase):
    def test_hypothesis_mandatory(self):
        with self.assertRaises(ValueError):conditional_weakest_link_survival(150,200,4,100,100)
    def test_volume_scaling_only_conditional(self):
        a=conditional_weakest_link_survival(150,200,4,100,100,physical_weakest_link_assumed=True)
        b=conditional_weakest_link_survival(150,200,4,200,100,physical_weakest_link_assumed=True)
        self.assertAlmostEqual(b['conditional_survival_probability'],a['conditional_survival_probability']**2)
        self.assertAlmostEqual(b['conditional_failure_probability'],1-b['conditional_survival_probability'])
    def test_zero_stress(self):
        d=conditional_weakest_link_survival(0,100,2,100,100,physical_weakest_link_assumed=True)
        self.assertEqual(d['conditional_survival_probability'],1)

class IntegrationTests(unittest.TestCase):
    def test_all_worked_cases(self):
        d=v1_casebook();self.assertEqual(d['status'],'partial_rights_withheld');self.assertEqual(d['count'],8)
    def test_case_types(self):
        origins={c['origin'] for c in v1_casebook()['cases']}
        self.assertIn('rights-withheld',origins)
        self.assertIn('synthetic_kinetics',origins)
        self.assertEqual(v1_casebook()['new_physical_measurements'],0)

if __name__=='__main__':unittest.main()
