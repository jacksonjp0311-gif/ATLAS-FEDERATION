import unittest,random,math
from bioelectric_atlas.cable import *
class CableTest(unittest.TestCase):
 def test_constant_state_stays_constant(self):
  self.assertEqual(cable_step([1]*6,0.01,1,1,0,0),tuple([1]*6))
 def test_sealed_charge_conservation(self):
  x=[0.2,-0.4,1.3,0.2,0.1]
  for _ in range(200):
   self.assertAlmostEqual(sum(x),1.4,places=10)
   x=cable_step(x,0.1,1,2,0,0)
 def test_pure_diffusion_smooths(self):
  x=[0,0,1,0,0];n=cable_step(x,0.1,1,1,0,0)
  self.assertLess(n[2],x[2]);self.assertGreater(n[1],0);self.assertGreater(n[3],0)
 def test_ends_are_sealed(self):
  x=[1,0];n=cable_step(x,0.1,1,1,0,0)
  self.assertAlmostEqual(n[0],0.9);self.assertAlmostEqual(n[1],0.1)
 def test_single_node_leak(self):
  n=cable_step([1],0.1,1,0,1,0)
  self.assertAlmostEqual(n[0],0.9)
 def test_step_limit(self):
  self.assertAlmostEqual(cable_stability_bound_seconds(5,1,1,0)['bound_seconds'],0.5)
 def test_single_no_leak_bound(self):
  self.assertTrue(cable_stability_bound_seconds(1,1,0,0)['no_passive_decay_or_coupling'])
 def test_bad_high_step(self):
  with self.assertRaises(ValueError):cable_step([0,1,0],0.51,1,1,0,0)
 def test_invalid_negative_axial(self):
  with self.assertRaises(ValueError):cable_step([0,1],0.01,1,-1,0,0)
 def test_nonfinite_voltage(self):
  with self.assertRaises(ValueError):cable_step([0,math.nan],0.01,1,1,0,0)
 def test_mismatched_inputs(self):
  with self.assertRaises(ValueError):cable_step([0,0],0.01,1,1,0,0,[0])
 def test_source_charge_increment(self):
  a=cable_step([0,0],0.1,1,0,0,0,[0.2,0.3])
  self.assertAlmostEqual(sum(a),0.05)
 def test_charge_reference(self):
  self.assertAlmostEqual(cable_charge_coulombs([1,1],2,0),4)
 def test_trace_shape(self):
  t=cable_trace([0,1,0],0.01,10,1,1,0,0)
  self.assertEqual(len(t['states']),11)
 def test_random_sealed_conservation(self):
  rng=random.Random(42)
  for _ in range(100):
   x=[rng.uniform(-1,1) for _ in range(5)];s=sum(x)
   y=cable_step(x,0.2,1,1,0,0)
   self.assertAlmostEqual(sum(y),s,places=12)
if __name__=='__main__':unittest.main()
