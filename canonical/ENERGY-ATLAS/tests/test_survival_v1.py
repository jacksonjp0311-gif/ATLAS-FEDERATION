"""Energy Atlas v1 release: unit tests on stipulated numerical values only."""
import unittest,random,math
from energy_atlas.survival_v1 import *
from energy_atlas.v1_cases import casebook_v1
from energy_atlas.models import InvalidPhysicalModel

class EnergySurvivalV1(unittest.TestCase):
    def test_casebook(self):
        r=casebook_v1();self.assertEqual(r['status'],'passed');self.assertEqual(r['count'],15)
    def test_weighted_two_cases(self):
        x=scenario_envelope([{'scenario_id':'x','demand_kWh':3,'unserved_kWh':3,'critical_unserved_kWh':2},{'scenario_id':'y','demand_kWh':3,'unserved_kWh':0,'critical_unserved_kWh':0}],[.1,.9]);self.assertAlmostEqual(x['scenario_weighted_unserved_kWh'],.3)
    def test_weighted_no_outage_probability(self):
        s=scenario_envelope([{'scenario_id':'x','demand_kWh':0,'unserved_kWh':0,'critical_unserved_kWh':0}]);self.assertFalse(s['physical_outage_probability_estimated'])
    def test_scenario_weights_bad(self):
        with self.assertRaises(InvalidPhysicalModel):scenario_envelope([{'scenario_id':'x','demand_kWh':1,'unserved_kWh':0,'critical_unserved_kWh':0}],[.9])
    def test_duplicate_scenario(self):
        row={'scenario_id':'x','demand_kWh':1,'unserved_kWh':0,'critical_unserved_kWh':0}
        with self.assertRaises(InvalidPhysicalModel):scenario_envelope([row,row],[.5,.5])
    def test_critical_subset(self):
        with self.assertRaises(InvalidPhysicalModel):scenario_envelope([{'scenario_id':'x','demand_kWh':2,'unserved_kWh':1,'critical_unserved_kWh':2}])
    def test_scenario_excess_unserved(self):
        with self.assertRaises(InvalidPhysicalModel):scenario_envelope([{'scenario_id':'x','demand_kWh':2,'unserved_kWh':3,'critical_unserved_kWh':0}])
    def test_bounded_supply(self):
        r=demand_generation_bounds(1,2,0,1,2)
        self.assertEqual(r['minimum_energy_shortfall_before_storage_kWh'],0);self.assertEqual(r['maximum_energy_shortfall_before_storage_kWh'],4)
    def test_bad_bounds(self):
        with self.assertRaises(InvalidPhysicalModel):demand_generation_bounds(2,1,0,1,2)
    def test_shelter_loss(self):
        r=heating_service_envelope(300,[{'inside_C':20,'outside_C':10,'hours':2,'internal_gain_kW':0}],thermal_efficiency=.5);self.assertAlmostEqual(r['input_heat_kWh'],12)
    def test_shelter_gains(self):
        r=heating_service_envelope(100,[{'inside_C':10,'outside_C':20,'hours':2,'internal_gain_kW':1}]);self.assertEqual(r['input_heat_kWh'],0)
    def test_water_energy_exact(self):
        r=water_energy_boundary(1,0,100,1);self.assertAlmostEqual(r['useful_thermal_J'],418400)
    def test_water_flags(self):self.assertFalse(water_energy_boundary(1,20,90,.9)['potability_verified'])
    def test_water_bad_eta(self):
        with self.assertRaises(InvalidPhysicalModel):water_energy_boundary(1,20,90,0)
    def test_empty_profile_reject(self):
        with self.assertRaises(InvalidPhysicalModel):survival_service_ledger([],1,2,reserve_kWh=0,discharge_limit_kW=1,charge_limit_kW=1)
    def test_extra_field_reject(self):
        with self.assertRaises(InvalidPhysicalModel):survival_service_ledger([{'critical_kW':1,'flexible_kW':0,'renewable_kW':0,'hours':1,'raw_voltage':999}],1,2,reserve_kWh=0,discharge_limit_kW=1,charge_limit_kW=1)
    def test_invalid_critical(self):
        with self.assertRaises(InvalidPhysicalModel):survival_service_ledger([{'critical_kW':-1,'flexible_kW':0,'renewable_kW':0,'hours':1}],1,2,reserve_kWh=0,discharge_limit_kW=1,charge_limit_kW=1)
    def test_initial_below_reserve(self):
        with self.assertRaises(InvalidPhysicalModel):survival_service_ledger([{'critical_kW':1,'flexible_kW':0,'renewable_kW':0,'hours':1}],.1,2,reserve_kWh=.2,discharge_limit_kW=1,charge_limit_kW=1)
    def test_backup_fuel_zero(self):
        r=survival_service_ledger([{'critical_kW':1,'flexible_kW':0,'renewable_kW':0,'hours':1}],.5,2,reserve_kWh=.5,discharge_limit_kW=1,charge_limit_kW=1,backup_output_limit_kW=2,backup_fuel_kWh=0);self.assertEqual(r['totals']['unserved_critical_kWh'],1)
    def test_backup_no_fuel_creation(self):
        r=survival_service_ledger([{'critical_kW':3,'flexible_kW':0,'renewable_kW':0,'hours':2}],.5,2,reserve_kWh=.5,discharge_limit_kW=1,charge_limit_kW=1,backup_output_limit_kW=5,backup_fuel_kWh=10,backup_electrical_efficiency=.4)
        self.assertEqual(r['totals']['backup_delivered_kWh'],4);self.assertEqual(r['totals']['unserved_critical_kWh'],2);self.assertEqual(r['final_fuel_chemical_kWh'],0)
    def test_non_real_approval(self):
        r=survival_service_ledger([{'critical_kW':1,'flexible_kW':0,'renewable_kW':1,'hours':1}],0,1,reserve_kWh=0,discharge_limit_kW=1,charge_limit_kW=1)
        self.assertFalse(r['electrical_installation_approved']);self.assertFalse(r['medical_load_continuity_verified'])
    def test_energy_conservation_random(self):
        rng=random.Random(490)
        for _ in range(400):
            n=rng.randint(1,15);p=[{'critical_kW':rng.random()*4,'flexible_kW':rng.random()*3,'renewable_kW':rng.random()*6,'hours':rng.random()*1.8+.1} for j in range(n)]
            cap=rng.random()*9+1;floor=cap*rng.random()*.5;init=floor+(cap-floor)*rng.random()
            r=survival_service_ledger(p,init,cap,reserve_kWh=floor,discharge_limit_kW=rng.random()*4,charge_limit_kW=rng.random()*3,
                charge_efficiency=.5+.5*rng.random(),discharge_efficiency=.5+.5*rng.random(),backup_output_limit_kW=rng.random()*3,
                backup_fuel_kWh=rng.random()*30,backup_electrical_efficiency=.2+.7*rng.random())
            self.assertAlmostEqual(r['conservation_residual_kWh'],0,delta=1e-8)
            self.assertAlmostEqual(r['load_balance_residual_kWh'],0,delta=1e-8)
            self.assertGreaterEqual(r['final_storage_kWh'],floor-1e-8);self.assertLessEqual(r['final_storage_kWh'],cap+1e-8)
            self.assertGreaterEqual(r['final_fuel_chemical_kWh'],-1e-8)
    def test_critical_not_sacrificed_for_flexible(self):
        r=survival_service_ledger([{'critical_kW':5,'flexible_kW':5,'renewable_kW':2,'hours':1}],0,1,reserve_kWh=0,discharge_limit_kW=0,charge_limit_kW=0)
        self.assertEqual(r['totals']['served_critical_kWh'],2);self.assertEqual(r['totals']['served_flexible_kWh'],0)
    def test_boundary_charge_limit(self):
        r=survival_service_ledger([{'critical_kW':0,'flexible_kW':0,'renewable_kW':10,'hours':1}],0,2,reserve_kWh=0,discharge_limit_kW=0,charge_limit_kW=1)
        self.assertAlmostEqual(r['final_storage_kWh'],.9);self.assertAlmostEqual(r['totals']['curtailed_renewable_kWh'],9)
    def test_pure_determinism(self):
        p=[{'critical_kW':1,'flexible_kW':2,'renewable_kW':.2,'hours':1}]
        a=survival_service_ledger(p,2,3,reserve_kWh=.1,discharge_limit_kW=1,charge_limit_kW=2)
        b=survival_service_ledger(p,2,3,reserve_kWh=.1,discharge_limit_kW=1,charge_limit_kW=2)
        self.assertEqual(a,b)
    def test_no_network_calls(self):
        import inspect,energy_atlas.survival_v1 as mod
        src=inspect.getsource(mod)
        for word in ('import requests','import serial','import socket','import subprocess'):
            self.assertNotIn(word,src)
if __name__=='__main__':unittest.main()
