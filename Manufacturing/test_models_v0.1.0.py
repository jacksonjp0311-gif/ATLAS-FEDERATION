import unittest,math,random
from manufacturing_atlas import models as m

class ManufacturingTests(unittest.TestCase):
 def test_fit_clearance(self):
  r=m.tolerance_fit(10.02,10.05,9.97,9.99)
  self.assertEqual(r['class'],'clearance');self.assertAlmostEqual(r['minimum_clearance_mm'],.03)
 def test_fit_interference(self):self.assertEqual(m.tolerance_fit(9.9,9.95,10,10.02)['class'],'interference')
 def test_fit_transition(self):self.assertEqual(m.tolerance_fit(10,10.03,10.01,10.04)['class'],'transition_or_boundary')
 def test_fit_zero_boundary(self):self.assertEqual(m.tolerance_fit(10,10,10,10)['class'],'transition_or_boundary')
 def test_fit_reversed(self):
  with self.assertRaises(ValueError):m.tolerance_fit(2,1,1,2)
 def test_fit_nan(self):
  with self.assertRaises(ValueError):m.tolerance_fit(float('nan'),1,0,1)
 def test_stackup(self):self.assertEqual(m.interval_stackup([(1,3),(-2,-1),(4,5)]),(3.,7.))
 def test_stackup_bad(self):
  with self.assertRaises(ValueError):m.interval_stackup([(2,1)])
 def test_stackup_empty(self):
  with self.assertRaises(ValueError):m.interval_stackup([])
 def test_covariance_independent(self):self.assertAlmostEqual(m.covariance_stackup([3,4],[[9,0],[0,16]]),5)
 def test_covariance_positive(self):self.assertAlmostEqual(m.covariance_stackup([1,1],[[1,.5],[.5,1]]),3**.5)
 def test_covariance_negative(self):self.assertAlmostEqual(m.covariance_stackup([1,1],[[1,-.5],[-.5,1]]),1)
 def test_covariance_bad(self):
  with self.assertRaises(ValueError):m.covariance_stackup([1,1],[[1,2],[2,1]])
 def test_thermal(self):self.assertAlmostEqual(m.thermal_length(1,12e-6,20),1.00024)
 def test_thermal_bigstrain(self):
  with self.assertRaises(ValueError):m.thermal_length(1,1,.2)
 def test_cutting(self):
  r=m.cutting_estimate(10,100,4,.05,2,5,1500,.85)
  self.assertAlmostEqual(r['rpm'],10000/math.pi)
  self.assertAlmostEqual(r['cutting_W'],1500*r['mrr_mm3_min']/60000)
 def test_cutting_invalid_efficiency(self):
  with self.assertRaises(ValueError):m.cutting_estimate(10,100,4,.05,2,5,1500,1.2)
 def test_cutting_bad_teeth(self):
  with self.assertRaises(ValueError):m.cutting_estimate(10,100,2.4,.05,2,5,1500,.8)
 def test_cantilever(self):self.assertAlmostEqual(m.cantilever_deflection(10,1,200e9,1e-8),10/(3*2000))
 def test_cantilever_invalid(self):
  with self.assertRaises(ValueError):m.cantilever_deflection(10,1,0,1)
 def test_leadscrew(self):
  a=m.leadscrew_position(10,1,.02,200)
  self.assertAlmostEqual(a['ideal_mm'],10)
  self.assertAlmostEqual(a['reachable_interval_mm'][0],9.9775)
 def test_leadscrew_invalid(self):
  with self.assertRaises(ValueError):m.leadscrew_position(1,1,-.02,200)
 def test_capability_hold(self):self.assertIsNone(m.capability(9,11,10,.2)['cpk'])
 def test_capability_conditional(self):
  x=m.capability(9,11,10,.2,True,True)
  self.assertAlmostEqual(x['cp'],2/(6*.2));self.assertAlmostEqual(x['cpk'],1/(3*.2))
 def test_capability_invalid(self):
  with self.assertRaises(ValueError):m.capability(10,9,10,.2)
 def test_chart(self):self.assertEqual(m.control_chart_flags([10,10.5,13,13.001],10,1),[3])
 def test_guard_accept(self):self.assertEqual(m.guardband_verdict(10,9,11,.2),'accepted_under_declared_uncertainty')
 def test_guard_hold(self):self.assertEqual(m.guardband_verdict(10.9,9,11,.2),'indeterminate_measure_again')
 def test_guard_reject(self):self.assertEqual(m.guardband_verdict(12,9,11,.1),'rejected_under_declared_uncertainty')
 def test_calibration(self):
  r=m.linear_calibration([0,1,2,3,4],[1,3,5,7,9]);self.assertAlmostEqual(r['gain'],2);self.assertAlmostEqual(r['offset'],1);self.assertAlmostEqual(r['residual_sigma_indication_units'],0)
 def test_calibration_bad(self):
  with self.assertRaises(ValueError):m.linear_calibration([1,1,1],[3,4,5])
 def test_route_critical(self):
  r=m.critical_path({'A':{'duration_min':3},'B':{'duration_min':5,'requires':['A']},'C':{'duration_min':7},'D':{'duration_min':2,'requires':['B','C']}})
  self.assertEqual(r['makespan_min'],10)
 def test_route_cycle(self):
  with self.assertRaises(ValueError):m.critical_path({'A':{'duration_min':1,'requires':['B']},'B':{'duration_min':1,'requires':['A']}})
 def test_route_unknown(self):
  with self.assertRaises(ValueError):m.critical_path({'A':{'duration_min':1,'requires':['Q']}})
 def test_cast(self):self.assertAlmostEqual(m.cast_dimension_from_pattern(100,.02),98)
 def test_cast_invalid(self):
  with self.assertRaises(ValueError):m.cast_dimension_from_pattern(100,.5)
 def test_layer(self):self.assertAlmostEqual(m.deposited_height(100,.2,.01),20.2)
 def test_layer_bad(self):
  with self.assertRaises(ValueError):m.deposited_height(2.5,.2)
 def test_roughness(self):self.assertAlmostEqual(m.roughness_ra([0,1,-1]),2/3)
 def test_roughness_shift(self):self.assertAlmostEqual(m.roughness_ra([5,6,4]),2/3)
 def test_lumped_thermal_start(self):self.assertEqual(m.first_order_thermal_state(310,300,5,2,10,0),310)
 def test_lumped_thermal_long(self):self.assertAlmostEqual(m.first_order_thermal_state(310,300,5,2,10,1e9),310)
 def test_lumped_thermal_invalid(self):
  with self.assertRaises(ValueError):m.first_order_thermal_state(-2,300,5,2,10,1)
 def test_multiple_numeric_roundtrip(self):
  rnd=random.Random(20261116)
  for i in range(100):
   x=rnd.uniform(.01,10);y=rnd.uniform(.01,5)
   self.assertAlmostEqual(m.thermal_length(x,2e-5,y),x+x*2e-5*y)

if __name__=='__main__':unittest.main()
