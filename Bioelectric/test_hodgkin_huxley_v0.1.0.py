import unittest,math,random
from bioelectric_atlas.hodgkin_huxley import *
class HHTest(unittest.TestCase):
 def test_vtrap_removable_m(self):
  self.assertAlmostEqual(hh_rates(-40)['m'][0],1)
 def test_vtrap_removable_n(self):
  self.assertAlmostEqual(hh_rates(-55)['n'][0],0.1)
 def test_rates_positive(self):
  for v in range(-120,81,5):
   for x in hh_rates(v).values():self.assertTrue(x[0]>=0 and x[1]>0)
 def test_gates_are_probabilities(self):
  s=hh_rest_state()
  for x in (s.m,s.n,s.h):self.assertGreater(x,0);self.assertLess(x,1)
 def test_rest_rates(self):
  s=hh_rest_state(-65)
  self.assertAlmostEqual(s.m,0.05293,places=4)
  self.assertAlmostEqual(s.h,0.5961,places=3)
  self.assertAlmostEqual(s.n,0.3177,places=3)
 def test_gate_exact_at_steady(self):
  m,tau=gate_steady_state_and_tau(2,3)
  self.assertAlmostEqual(exact_gate_update(m,2,3,1),m)
 def test_gate_dt_zero(self):
  self.assertEqual(exact_gate_update(0.2,2,3,0),0.2)
 def test_gate_monotonic(self):
  self.assertGreater(exact_gate_update(0,2,3,1),0)
  self.assertLess(exact_gate_update(1,2,3,1),1)
 def test_rest_dv_near_zero(self):
  s=hh_rest_state()
  d=hh_step(s,0.01)
  self.assertLess(abs(d.v_mV-s.v_mV),0.0001)
 def test_current_summary(self):
  d=hh_ionic_currents(hh_rest_state())
  self.assertAlmostEqual(sum(d[k] for k in ('sodium_uA_per_cm2','potassium_uA_per_cm2','leak_uA_per_cm2')),d['total_uA_per_cm2'])
 def test_hh_trace_no_nan(self):
  result=hh_trace(500,0.01,0.0)
  self.assertTrue(all(math.isfinite(x) for x in result['membrane_mV']))
  self.assertEqual(len(result['membrane_mV']),501)
 def test_small_drive_changes_trace(self):
  x=hh_trace(100,0.01,0)
  y=hh_trace(100,0.01,5)
  self.assertNotEqual(x['membrane_mV'],y['membrane_mV'])
 def test_repeated_run_deterministic(self):
  self.assertEqual(hh_trace(30),hh_trace(30))
 def test_bad_voltage_range(self):
  with self.assertRaises(ValueError):hh_rates(500)
 def test_large_dt_refused(self):
  with self.assertRaises(ValueError):hh_step(hh_rest_state(),0.2)
 def test_large_drive_refused(self):
  with self.assertRaises(ValueError):hh_step(hh_rest_state(),0.01,10000)
 def test_nonphysical_gate_refused(self):
  with self.assertRaises(ValueError):HHState(-65,1.1,0.5,0.5)
 def test_invalid_gate_rate_refused(self):
  with self.assertRaises(ValueError):gate_steady_state_and_tau(0,0)
 def test_random_gate_bounds(self):
  r=random.Random(2026)
  for _ in range(300):
   x=r.random();alpha=r.uniform(0.001,10);beta=r.uniform(0.001,10)
   y=exact_gate_update(x,alpha,beta,r.uniform(0,5))
   self.assertLessEqual(y,1);self.assertGreaterEqual(y,0)
 def test_rest_model_nonclinical(self):
  t=hh_trace(1)
  self.assertFalse(t['medical_device_applicability'])
if __name__=='__main__':unittest.main()
