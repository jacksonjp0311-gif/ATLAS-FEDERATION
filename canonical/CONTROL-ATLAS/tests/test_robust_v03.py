"""Deterministic robustness and input-refusal tests, NOT controller certification."""
import math,random,unittest
from control_atlas.robust import *
from control_atlas.robust_cases import casebook

class IntervalTests(unittest.TestCase):
 def test_interval_stable(self):
  a=robust_scalar_feedback_interval([.9,1.1],[.25,.45],1)
  self.assertTrue(a['strict_uniform_asymptotic_stability_within_assumed_model'])
  self.assertEqual(len(a['every_vertex']),4)
 def test_interval_failure(self):
  self.assertFalse(robust_scalar_feedback_interval([1.35,1.8],[.05,.25],1)['strict_uniform_asymptotic_stability_within_assumed_model'])
 def test_bad_interval(self):
  for b in ([2,1],[1],['bad',2]):
   with self.subTest(b=b),self.assertRaises(ControlInputError):robust_scalar_feedback_interval(b,[0,1],1)
 def test_dense_sampling_worst_corner(self):
  rng=random.Random(311)
  for _ in range(200):
   a1=rng.uniform(-2,1);a2=a1+rng.uniform(.01,2);b1=rng.uniform(-2,1);b2=b1+rng.uniform(.01,2);k=rng.uniform(-2,2)
   result=robust_scalar_feedback_interval([a1,a2],[b1,b2],k)
   maxcorner=result['worst_case_abs_pole']
   for _ in range(10):
    a=rng.uniform(a1,a2);b=rng.uniform(b1,b2)
    self.assertLessEqual(abs(a-b*k),maxcorner+1e-12)

class DelayTests(unittest.TestCase):
 def test_delayed_unstable(self):
  d=delay_one_sample_scalar(1.5,1,1.2)
  self.assertTrue(d['zero_delay_stable']);self.assertFalse(d['one_sample_delayed_model_stable'])
  self.assertAlmostEqual(d['one_sample_delay_spectral_radius'],math.sqrt(1.2))
 def test_delay_zero_gain(self):
  d=delay_one_sample_scalar(.9,1,0)
  self.assertAlmostEqual(d['one_sample_delay_spectral_radius'],.9)
 def test_delay_roots_satisfy_quadratic(self):
  r=random.Random(427)
  for _ in range(150):
   a,b,k=[r.uniform(-2,2) for _ in range(3)]
   d=delay_one_sample_scalar(a,b,k)
   for z in d['one_sample_delay_roots']:
    c=complex(z['real'],z['imag'])
    self.assertLess(abs(c*c-a*c+b*k),1e-11)

class LyapunovTests(unittest.TestCase):
 def test_certificate(self):
  r=discrete_lyapunov_2x2([[.7,0],[0,.9]],[[1,0],[0,1]])
  self.assertTrue(r['numerically_positive_definite_P_and_Q'])
 def test_failed_candidate_not_unstable(self):
  r=discrete_lyapunov_2x2([[.5,4],[0,.5]],[[1,0],[0,1]])
  self.assertFalse(r['numerically_positive_definite_P_and_Q'])
 def test_reject_nonsymmetric(self):
  with self.assertRaises(ControlInputError):discrete_lyapunov_2x2([[.5,0],[0,.5]],[[1,1],[0,1]])
 def test_unstable_A_not_certified_identity(self):
  self.assertFalse(discrete_lyapunov_2x2([[1.1,0],[0,.2]],[[1,0],[0,1]])['numerically_positive_definite_P_and_Q'])

class SensitivityAndResidual(unittest.TestCase):
 def test_frequency_identity(self):
  r=first_order_proportional_sensitivity(2,3,1,.5)
  self.assertAlmostEqual(r['S_plus_T_identity_residual'],0)
 def test_zero_controller(self):
  r=first_order_proportional_sensitivity(2,3,0,.5)
  self.assertAlmostEqual(r['sensitivity_magnitude'],1)
  self.assertEqual(r['complementary_sensitivity_magnitude'],0)
 def test_singularity_rejected(self):
  with self.assertRaises(ControlInputError):first_order_proportional_sensitivity(1,1,-1,0)
 def test_frequency_nonnegative(self):
  with self.assertRaises(ControlInputError):first_order_proportional_sensitivity(1,1,1,-1)
 def test_alternating_residual(self):
  r=residual_lag1_diagnostic([1,-1]*8)
  self.assertLess(r['descriptive_lag1_correlation'],-.8)
 def test_constant_residual_refused(self):
  with self.assertRaises(ControlInputError):residual_lag1_diagnostic([1]*8)
 def test_short_residual_refused(self):
  with self.assertRaises(ControlInputError):residual_lag1_diagnostic([1,-1])

class WatchdogPolicy(unittest.TestCase):
 def test_explicit_blocking(self):
  r=casebook()
  self.assertEqual(r['status'],'passed');self.assertEqual(r['count'],8)
  t=next(x for x in r['cases'] if x['id']=='illustrative_fault_gate')['result']
  self.assertEqual(t['blocked_count'],3)
 def test_future_timestamp_refusal(self):
  with self.assertRaises(ControlInputError):watchdog_policy_trace([{'now_s':1,'measurement_timestamp_s':2,'measurement_valid':True,'innovation':0,'requested_output':1}],1,1)
 def test_boolean_validity(self):
  with self.assertRaises(ControlInputError):watchdog_policy_trace([{'now_s':1,'measurement_timestamp_s':1,'measurement_valid':1,'innovation':0,'requested_output':1}],1,1)
 def test_nondecreasing_clock_refusal(self):
  l=[{'now_s':1,'measurement_timestamp_s':1,'measurement_valid':True,'innovation':0,'requested_output':1}]*2
  with self.assertRaises(ControlInputError):watchdog_policy_trace(l,1,1)
 def test_outside_innovation_threshold(self):
  r=watchdog_policy_trace([{'now_s':1,'measurement_timestamp_s':1,'measurement_valid':True,'innovation':2,'requested_output':100}],1,1,0)
  self.assertEqual(r['trace'][0]['output'],0)
 def test_empty_refusal(self):
  with self.assertRaises(ControlInputError):watchdog_policy_trace([],1,1)

if __name__=='__main__':unittest.main()
