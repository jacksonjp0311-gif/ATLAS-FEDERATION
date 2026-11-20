import unittest,random,math
from energy_atlas.survival_models import *
from energy_atlas.survival_cases import casebook_survival
from energy_atlas.models import InvalidPhysicalModel

class SurvivalEnergyMath(unittest.TestCase):
 def test_cases(self):self.assertEqual(casebook_survival()['status'],'passed');self.assertEqual(casebook_survival()['count'],11)
 def test_water_zero(self):self.assertEqual(water_lift_energy(0,40,.9)['required_input_Wh'],0)
 def test_water_scaling(self):self.assertAlmostEqual(water_lift_energy(2,7,.75)['required_input_energy_j'],2*water_lift_energy(1,7,.75)['required_input_energy_j'])
 def test_water_efficiency(self):self.assertGreater(water_lift_energy(1,10,.4)['required_input_Wh'],water_lift_energy(1,10,.8)['required_input_Wh'])
 def test_water_invalid_eff(self):
  with self.assertRaises(InvalidPhysicalModel):water_lift_energy(1,1,0)
 def test_water_negative_head(self):
  with self.assertRaises(InvalidPhysicalModel):water_lift_energy(1,-1,.7)
 def test_heating_energy(self):self.assertEqual(heating_energy(1,1000,20,40)['useful_heat_j'],20000)
 def test_heating_efficiency(self):self.assertAlmostEqual(heating_energy(1,1000,20,40,useful_fraction=.5)['input_heat_j'],40000)
 def test_heating_not_disinfection(self):self.assertFalse(heating_energy(1,1000,20,40)['water_potability_verified'])
 def test_heating_cooling_reject(self):
  with self.assertRaises(InvalidPhysicalModel):heating_energy(1,1000,40,20)
 def test_shelter_loss(self):self.assertEqual(shelter_heat_loss(400,25)['heat_loss_kWh'],10)
 def test_shelter_negative(self):
  with self.assertRaises(InvalidPhysicalModel):shelter_heat_loss(1,-1)
 def test_fuel_account(self):self.assertAlmostEqual(fuel_to_delivered_electricity(3,36,.3)['electricity_at_assumed_efficiency_kWh'],9)
 def test_fuel_zero_eff(self):
  with self.assertRaises(InvalidPhysicalModel):fuel_to_delivered_electricity(3,36,0)
 def test_fuel_not_operational(self):self.assertIn('NO instructions',fuel_to_delivered_electricity(3,36,.3)['limitations'][1])
 def test_priority_exact(self):
  x=emergency_load_allocation([{'service_id':'a','priority':1,'requested_kW':2,'minimum_kW':1}, {'service_id':'b','priority':2,'requested_kW':3,'minimum_kW':0}],2)
  self.assertAlmostEqual(x['services']['a']['served_kW'],2);self.assertEqual(x['services']['b']['served_kW'],0)
 def test_priority_tie_proportional(self):
  x=emergency_load_allocation([{'service_id':'a','priority':1,'requested_kW':2,'minimum_kW':0}, {'service_id':'b','priority':1,'requested_kW':3,'minimum_kW':0}],2)
  self.assertAlmostEqual(x['services']['a']['served_kW'],.8);self.assertAlmostEqual(x['services']['b']['served_kW'],1.2)
 def test_priority_reordering(self):
  x=[{'service_id':'a','priority':1,'requested_kW':2,'minimum_kW':0}, {'service_id':'b','priority':1,'requested_kW':3,'minimum_kW':0}]
  self.assertEqual(emergency_load_allocation(x,2)['services'],emergency_load_allocation(x[::-1],2)['services'])
 def test_priority_oversubscribed(self):self.assertFalse(emergency_load_allocation([{'service_id':'a','priority':1,'requested_kW':2,'minimum_kW':2}],1)['all_declared_minima_met'])
 def test_priority_zero(self):self.assertEqual(emergency_load_allocation([{'service_id':'a','priority':1,'requested_kW':0,'minimum_kW':0}],0)['unserved_kW'],0)
 def test_priority_negative(self):
  with self.assertRaises(InvalidPhysicalModel):emergency_load_allocation([{'service_id':'a','priority':-1,'requested_kW':1,'minimum_kW':0}],3)
 def test_priority_duplicate(self):
  with self.assertRaises(InvalidPhysicalModel):emergency_load_allocation([{'service_id':'a','priority':1,'requested_kW':1,'minimum_kW':0}]*2,3)
 def test_reserve(self):self.assertEqual(energy_reserve_estimate(1,5,1,.2,1)['usable_delivered_kWh'],4)
 def test_reserve_lower_soc(self):
  with self.assertRaises(InvalidPhysicalModel):energy_reserve_estimate(1,5,.1,.2)
 def test_reserve_zero_demand(self):self.assertIsNone(energy_reserve_estimate(0,5)['illustrative_days_at_constant_daily_load'])
 def test_profile_empty_refused(self):
  with self.assertRaises(InvalidPhysicalModel):microgrid_profile([],0,4,charge_limit_kW=1,discharge_limit_kW=1)
 def test_profile_no_generation(self):
  p=[{'load_kW':2,'renewable_kW':0,'dt_hours':1,'grid_available':False}]*3
  x=microgrid_profile(p,0,2,charge_limit_kW=1,discharge_limit_kW=1)
  self.assertEqual(x['totals']['unserved_kWh'],6)
 def test_profile_balance(self):
  rng=random.Random(21)
  for _ in range(150):
   profile=[{'load_kW':rng.random()*10,'renewable_kW':rng.random()*10,'dt_hours':rng.uniform(.05,3),'grid_available':bool(rng.getrandbits(1))} for j in range(20)]
   r=microgrid_profile(profile,5,15,charge_limit_kW=3,discharge_limit_kW=4,eta_charge=.85,eta_discharge=.88)
   self.assertAlmostEqual(r['totals']['energy_balance_residual_kWh'],0,places=7)
   self.assertGreaterEqual(r['minimum_storage_kWh'],-1e-8)
   self.assertLessEqual(r['final_storage_kWh'],15+1e-8)
   self.assertGreaterEqual(r['totals']['unserved_kWh'],-1e-8)
 def test_profile_bad_grid_field(self):
  with self.assertRaises(InvalidPhysicalModel):microgrid_profile([{'load_kW':1,'renewable_kW':2,'dt_hours':1,'grid_available':1}],0,2,charge_limit_kW=1,discharge_limit_kW=1)
 def test_profile_negative_generation(self):
  with self.assertRaises(InvalidPhysicalModel):microgrid_profile([{'load_kW':1,'renewable_kW':-2,'dt_hours':1,'grid_available':False}],0,2,charge_limit_kW=1,discharge_limit_kW=1)
 def test_profile_missing_state(self):
  with self.assertRaises(InvalidPhysicalModel):microgrid_profile([{'load_kW':1,'renewable_kW':2,'dt_hours':1}],0,2,charge_limit_kW=1,discharge_limit_kW=1)
 def test_profile_demand_distinct_from_energy(self):
  p=[{'load_kW':1,'renewable_kW':0,'dt_hours':.5,'grid_available':False}]
  x=microgrid_profile(p,0,5,charge_limit_kW=0,discharge_limit_kW=0)
  self.assertEqual(x['totals']['unserved_kWh'],.5)
 def test_scenarios(self):
  a=[{'scenario_id':'bad','profile':[{'load_kW':5,'renewable_kW':0,'dt_hours':3,'grid_available':False}]},
     {'scenario_id':'ok','profile':[{'load_kW':.1,'renewable_kW':2,'dt_hours':3,'grid_available':False}]}]
  r=evaluate_survival_scenarios(a,0,2,charge_limit_kW=1,discharge_limit_kW=1)
  self.assertEqual(r['worst_supplied_unserved_energy']['scenario_id'],'bad')
  self.assertFalse(r['population_outage_probability_known'])
 def test_scenarios_duplicate(self):
  p={'scenario_id':'a','profile':[{'load_kW':0,'renewable_kW':0,'dt_hours':1,'grid_available':False}]}
  with self.assertRaises(InvalidPhysicalModel):evaluate_survival_scenarios([p,p],0,2,charge_limit_kW=1,discharge_limit_kW=1)

if __name__=='__main__':unittest.main()
