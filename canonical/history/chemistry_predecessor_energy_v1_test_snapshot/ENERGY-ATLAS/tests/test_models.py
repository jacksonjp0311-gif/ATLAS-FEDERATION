import math,random,unittest
from energy_atlas.models import *
from energy_atlas.cases import casebook
class EnergyReferenceTests(unittest.TestCase):
 def test_casebook(self):self.assertEqual(casebook()['status'],'passed');self.assertEqual(casebook()['count'],25)
 def test_convert_bidirectional(self):self.assertEqual(unit_convert(unit_convert(5,'kWh','J'),'J','kWh'),5)
 def test_convert_wh(self):self.assertEqual(unit_convert(1,'Wh','J'),3600)
 def test_convert_bad_unit(self):
  with self.assertRaises(InvalidPhysicalModel):unit_convert(1,'watt','J')
 def test_balance(self):self.assertEqual(steady_energy_balance([40,60],[50,25],25)['residual_j'],0)
 def test_balance_missing(self):self.assertEqual(steady_energy_balance([100],[],0)['residual_j'],100)
 def test_balance_negative_reject(self):
  with self.assertRaises(InvalidPhysicalModel):steady_energy_balance([-1],[],0)
 def test_efficiency(self):self.assertAlmostEqual(converter_efficiency(100,80)['efficiency'],.8)
 def test_overunity_refusal(self):
  with self.assertRaises(InvalidPhysicalModel):converter_efficiency(100,200)
 def test_zero_input_refusal(self):
  with self.assertRaises(InvalidPhysicalModel):converter_efficiency(0,0)
 def test_carnot(self):self.assertAlmostEqual(carnot_engine(400,300)['max_thermal_efficiency'],.25)
 def test_carnot_cop(self):self.assertAlmostEqual(carnot_engine(400,300)['ideal_heating_cop'],4)
 def test_carnot_reverse_refusal(self):
  with self.assertRaises(InvalidPhysicalModel):carnot_engine(300,400)
 def test_carnot_negative_refusal(self):
  with self.assertRaises(InvalidPhysicalModel):carnot_engine(400,-1)
 def test_ideal_gas_reversal(self):self.assertAlmostEqual(reversible_ideal_gas_work(1,300,1,2)['work_by_gas_j'],-reversible_ideal_gas_work(1,300,2,1)['work_by_gas_j'])
 def test_ideal_gas_zero_volume(self):
  with self.assertRaises(InvalidPhysicalModel):reversible_ideal_gas_work(1,300,0,1)
 def test_conduction_double_area(self):self.assertAlmostEqual(conduction_rate(2,2,1,320,300),2*conduction_rate(2,1,1,320,300))
 def test_conduction_bad_thickness(self):
  with self.assertRaises(InvalidPhysicalModel):conduction_rate(1,1,0,320,300)
 def test_conduction_wrong_sign(self):
  with self.assertRaises(InvalidPhysicalModel):conduction_rate(1,1,.2,300,320)
 def test_convective_sign(self):self.assertEqual(convection_rate(2,3,300,310),-60)
 def test_radiation_hot_cold_reversal(self):self.assertAlmostEqual(radiation_rate(.7,1,350,300),-radiation_rate(.7,1,300,350))
 def test_emissivity_bound(self):
  with self.assertRaises(InvalidPhysicalModel):radiation_rate(1.2,1,320,300)
 def test_lumped_time_zero(self):self.assertEqual(lumped_cooling(320,280,0,5,500,30,4)['temperature_K'],320)
 def test_lumped_time_infinity(self):self.assertAlmostEqual(lumped_cooling(320,280,1e9,5,500,30,4)['temperature_K'],280)
 def test_ohm(self):self.assertEqual(dc_ohms_law(V=12,I=2)['resistance_ohm'],6)
 def test_ohm_missing_three(self):
  with self.assertRaises(InvalidPhysicalModel):dc_ohms_law()
 def test_ohm_invalid(self):
  with self.assertRaises(InvalidPhysicalModel):dc_ohms_law(V=12,I=0)
 def test_rc_initial_energy(self):self.assertAlmostEqual(rc_discharge(10,0,5,.2)['energy_J'],10)
 def test_rc_one_tau(self):self.assertAlmostEqual(rc_discharge(10,1,5,.2)['voltage_V'],10/math.e)
 def test_rc_invalid(self):
  with self.assertRaises(InvalidPhysicalModel):rc_discharge(10,1,0,1)
 def test_ac_pfactor(self):self.assertAlmostEqual(ac_single_phase(120,10,.8)['real_W'],960)
 def test_ac_aggregation(self):self.assertAlmostEqual(balanced_three_phase(400,10,.9)['real_W'],math.sqrt(3)*3600)
 def test_ac_invalid_pf(self):
  with self.assertRaises(InvalidPhysicalModel):balanced_three_phase(100,2,1.1)
 def test_ac_sign(self):self.assertLess(ac_single_phase(100,2,.5,-1)['reactive_var'],0)
 def test_transformer_ratios(self):self.assertEqual(ideal_transformer(120,100,50,2)['V_secondary'],60)
 def test_transformer_invalid(self):
  with self.assertRaises(InvalidPhysicalModel):ideal_transformer(120,0,50,2)
 def test_i2r(self):self.assertEqual(line_resistive_loss(2,5,2),40)
 def test_i2r_integer_guard(self):
  with self.assertRaises(InvalidPhysicalModel):line_resistive_loss(2,5,2.0)
 def test_pv_stc(self):self.assertEqual(solar_pv_power(1000,1000,25,-.004)['dc_power_W'],1000)
 def test_pv_temperature(self):self.assertEqual(solar_pv_power(1000,1000,50,-.004)['dc_power_W'],900)
 def test_pv_zero_sun(self):self.assertEqual(solar_pv_power(1000,0,25,-.004)['dc_power_W'],0)
 def test_pv_invalid(self):
  with self.assertRaises(InvalidPhysicalModel):solar_pv_power(1000,1000,100,-.5)
 def test_betz(self):self.assertAlmostEqual(wind_turbine_power(1,2,3,BETZ_MAX)['ideal_betz_W'],2*27/2*BETZ_MAX)
 def test_wind_power_cubic(self):
  a=wind_turbine_power(1,1,5,.4)['ideal_extracted_W'];b=wind_turbine_power(1,1,10,.4)['ideal_extracted_W'];self.assertEqual(b,8*a)
 def test_wind_unphysical_cp(self):
  with self.assertRaises(InvalidPhysicalModel):wind_turbine_power(1,1,5,.9)
 def test_hydro_linear(self):self.assertEqual(hydroelectric_power(1000,2,10,.8),2*hydroelectric_power(1000,1,10,.8))
 def test_battery_roundtrip(self):
  a=battery_step(5,10,1,charge_input_kW=1,eta_charge=.9)
  b=battery_step(a['stored_kWh'],10,1,discharge_output_kW=.81,eta_discharge=.9)
  self.assertAlmostEqual(b['stored_kWh'],5)
 def test_battery_loss(self):self.assertGreater(battery_step(5,10,1,discharge_output_kW=2,eta_discharge=.5)['loss_kWh'],0)
 def test_battery_overfull(self):
  with self.assertRaises(InvalidPhysicalModel):battery_step(9,10,1,charge_input_kW=2)
 def test_battery_overempty(self):
  with self.assertRaises(InvalidPhysicalModel):battery_step(1,10,1,discharge_output_kW=2)
 def test_battery_simultaneous_reject(self):
  with self.assertRaises(InvalidPhysicalModel):battery_step(5,10,1,charge_input_kW=1,discharge_output_kW=1)
 def test_capacity_factor(self):self.assertEqual(capacity_factor(100,20,10),.5)
 def test_capacity_factor_over_one(self):
  with self.assertRaises(InvalidPhysicalModel):capacity_factor(201,20,10)
 def test_lcoe_one_year(self):self.assertAlmostEqual(simple_levelized_cost(100,[10],[100],0)['currency_per_kWh'],1.1)
 def test_lcoe_zero_gen(self):
  with self.assertRaises(InvalidPhysicalModel):simple_levelized_cost(100,[10],[0],0)
 def test_nuclear_E_mc2(self):self.assertAlmostEqual(nuclear_mass_energy(1),float(C_LIGHT**2),delta=32)
 def test_trapezoid_constant(self):self.assertEqual(piecewise_energy_j([0,3,6],[10,10,10])['joules'],60)
 def test_trapezoid_nonmonotone(self):
  with self.assertRaises(InvalidPhysicalModel):piecewise_energy_j([0,5,4],[10,10,10])
 def test_nan_refused(self):
  with self.assertRaises(InvalidPhysicalModel):unit_convert(float('nan'),'J','kWh')
 def test_bool_refused(self):
  with self.assertRaises(InvalidPhysicalModel):dc_ohms_law(V=True,R=3)
if __name__=='__main__':unittest.main()
class MicrogridEnergyOnlyTests(unittest.TestCase):
 def test_surplus_store(self):
  a=microgrid_interval_dispatch(1,3,0,5,1,5,5,eta_charge=.8)
  self.assertAlmostEqual(a['stored_after_kWh'],1.6)
  self.assertEqual(a['unmet_load_kW'],0)
  self.assertAlmostEqual(a['balance_residual_kWh'],0)
 def test_deficit_measured(self):
  a=microgrid_interval_dispatch(3,0,1,5,1,5,5,eta_discharge=.8)
  self.assertAlmostEqual(a['battery_discharge_kW'],.8)
  self.assertAlmostEqual(a['unmet_load_kW'],2.2)
  self.assertAlmostEqual(a['stored_after_kWh'],0)
 def test_deficit_grid_available(self):
  a=microgrid_interval_dispatch(3,0,0,5,1,5,5,grid_available=True)
  self.assertEqual(a['grid_import_kW'],3)
  self.assertEqual(a['unmet_load_kW'],0)
 def test_charge_power_limit(self):
  a=microgrid_interval_dispatch(1,8,0,5,1,2,5)
  self.assertEqual(a['battery_charge_kW'],2)
  self.assertEqual(a['renewable_curtailed_kW'],5)
 def test_charge_capacity_limit(self):
  a=microgrid_interval_dispatch(0,5,4.5,5,1,5,5,eta_charge=.5)
  self.assertAlmostEqual(a['battery_charge_kW'],1)
  self.assertAlmostEqual(a['stored_after_kWh'],5)
 def test_discharge_power_limit(self):
  a=microgrid_interval_dispatch(10,0,5,5,1,5,2)
  self.assertEqual(a['battery_discharge_kW'],2)
  self.assertEqual(a['unmet_load_kW'],8)
 def test_grid_type_reject(self):
  with self.assertRaises(InvalidPhysicalModel):microgrid_interval_dispatch(1,0,0,5,1,1,1,grid_available=1)
 def test_no_overunity(self):
  for k in range(20):
   a=microgrid_interval_dispatch(k/2,k/4,1,5,.5,3,3,.87,.78)
   self.assertAlmostEqual(a['balance_residual_kWh'],0,places=11)
   self.assertGreaterEqual(a['stored_after_kWh'],-1e-10)
   self.assertLessEqual(a['stored_after_kWh'],5+1e-10)
