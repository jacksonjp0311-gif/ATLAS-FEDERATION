import unittest,math,random
from bioelectric_atlas.excitability import *
class ExcitabilityTest(unittest.TestCase):
 def test_fhn_known_equilibrium_derivative(self):
  s=FHNState(0,0)
  a,b=fhn_derivative(s,0,0,1,0.08)
  self.assertEqual((a,b),(0,0))
 def test_small_step(self):
  s=FHNState(0,0);self.assertEqual(fhn_rk4_step(s,0.01,0,0,1),s)
 def test_drive_effect(self):
  s=FHNState(0,0)
  self.assertGreater(fhn_rk4_step(s,0.01,1).v,fhn_rk4_step(s,0.01,0).v)
 def test_small_dt_consistency(self):
  x=FHNState(-1,0)
  a=fhn_rk4_step(x,0.02)
  b=fhn_rk4_step(fhn_rk4_step(x,0.01),0.01)
  self.assertAlmostEqual(a.v,b.v,places=7)
 def test_trace(self):
  t=fhn_trace(FHNState(-1,0),10,0.01)
  self.assertEqual(len(t['states']),11)
 def test_nonclinical_flag(self):
  self.assertFalse(fhn_trace(FHNState(0,0),2,0.01)['diagnostic_or_therapeutic_validity'])
 def test_state_range_rejected(self):
  with self.assertRaises(ValueError):FHNState(99,0)
 def test_step_too_large_rejected(self):
  with self.assertRaises(ValueError):fhn_rk4_step(FHNState(0,0),0.3)
 def test_bad_params(self):
  with self.assertRaises(ValueError):fhn_derivative(FHNState(0,0),epsilon=-1)
 def test_replay_deterministic(self):
  self.assertEqual(fhn_trace(FHNState(-1,0),100,0.01),fhn_trace(FHNState(-1,0),100,0.01))
if __name__=='__main__':unittest.main()
