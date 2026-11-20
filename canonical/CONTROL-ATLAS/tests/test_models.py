import unittest,math,random
from control_atlas.models import *
from control_atlas.cases import casebook

class TestModels(unittest.TestCase):
 def test_firstorder_t0(self):self.assertEqual(first_order_response(initial=2,final=3,time_s=0,tau_s=5)['state'],2)
 def test_firstorder_tau(self):self.assertAlmostEqual(first_order_response(initial=0,final=1,time_s=5,tau_s=5)['state'],1-math.exp(-1))
 def test_negative_time(self):
  with self.assertRaises(ControlInputError):first_order_response(initial=0,final=1,time_s=-.1,tau_s=4)
 def test_bad_tau(self):
  with self.assertRaises(ControlInputError):zoh_first_order(gain=1,tau_s=0,sample_s=1)
 def test_zoh_gain_equilibrium(self):
  for t in [.1,.3,1.2,5.0]:
   d=zoh_first_order(gain=3,tau_s=2,sample_s=t)
   self.assertAlmostEqual(d['b']/(1-d['a']),3)
 def test_scalar_stability(self):
  self.assertTrue(scalar_discrete_stability(a=-.99)['asymptotically_stable'])
  self.assertFalse(scalar_discrete_stability(a=1.01)['asymptotically_stable'])
  self.assertTrue(scalar_discrete_stability(a=1)['marginal_boundary'])
 def test_non_numeric(self):
  with self.assertRaises(ControlInputError):scalar_discrete_stability(a=True)
 def test_controllability(self):
  d=state_rank_2x2(A=[[1,1],[0,1]],B=[.5,1],C=[1,0]);self.assertTrue(d['controllable_at_absolute_det_tol']);self.assertTrue(d['observable_at_absolute_det_tol'])
 def test_no_control(self):
  d=state_rank_2x2(A=[[1,1],[0,1]],B=[0,0],C=[1,0]);self.assertFalse(d['controllable_at_absolute_det_tol'])
 def test_no_observability(self):
  d=state_rank_2x2(A=[[1,1],[0,1]],B=[.5,1],C=[0,0]);self.assertFalse(d['observable_at_absolute_det_tol'])
 def test_bad_matrices(self):
  with self.assertRaises(ControlInputError):state_rank_2x2(A=[[1]],B=[1,0],C=[1,0])
 def test_pi_trace_length(self):
  r=pi_first_order_simulation(kp=1,ki=.2,plant_gain=1,tau_s=5,sample_s=.2,setpoints=[1.]*25,u_min=0,u_max=1)
  self.assertEqual(len(r['trace']),25);self.assertGreater(r['output_final'],0)
 def test_pi_antiwindup_improves_specific_case(self):
  data=casebook()['cases'][4];self.assertTrue(data['passed']);self.assertLess(data['result']['clamp_iae'],data['result']['without_iae'])
 def test_pi_bad_limits(self):
  with self.assertRaises(ControlInputError):pi_first_order_simulation(kp=1,ki=1,plant_gain=1,tau_s=2,sample_s=.1,setpoints=[1],u_min=1,u_max=1)
 def test_pi_bad_mode(self):
  with self.assertRaises(ControlInputError):pi_first_order_simulation(kp=1,ki=1,plant_gain=1,tau_s=2,sample_s=.1,setpoints=[1],u_min=0,u_max=1,antiwindup='foo')
 def test_pi_nan(self):
  with self.assertRaises(ControlInputError):pi_first_order_simulation(kp=1,ki=1,plant_gain=1,tau_s=2,sample_s=.1,setpoints=[math.nan],u_min=0,u_max=1)
 def test_kalman_scalar_posterior(self):
  d=scalar_kalman(a=1,c=1,process_variance=0,measurement_variance=1,initial_estimate=0,initial_variance=1,measurements=[2]);self.assertAlmostEqual(d['final_estimate'],1);self.assertAlmostEqual(d['final_variance'],.5)
 def test_kalman_reduction_with_repeated_measurements(self):
  d=scalar_kalman(a=1,c=1,process_variance=0,measurement_variance=1,initial_estimate=0,initial_variance=1,measurements=[2]*4)
  self.assertAlmostEqual(d['final_estimate'],1.6);self.assertAlmostEqual(d['final_variance'],.2)
 def test_kalman_bad_R(self):
  with self.assertRaises(ControlInputError):scalar_kalman(a=1,c=1,process_variance=0,measurement_variance=0,initial_estimate=0,initial_variance=1,measurements=[1])
 def test_lqr_horizon_one_closed(self):
  d=scalar_finite_lqr(a=2,b=1,q=1,r=1,terminal_q=1,horizon=1,x0=1)
  self.assertAlmostEqual(d['gains'][0],1)
  self.assertAlmostEqual(d['optimal_cost'],3)
 def test_lqr_cost_equality(self):
  d=scalar_finite_lqr(a=1.1,b=1,q=1,r=.2,terminal_q=1,horizon=12,x0=2)
  self.assertAlmostEqual(d['optimal_cost'],d['rollout_cost'],places=10)
 def test_lqr_bad_horizon(self):
  with self.assertRaises(ControlInputError):scalar_finite_lqr(a=1,b=1,q=1,r=1,terminal_q=1,horizon=True,x0=1)
 def test_lqr_bad_r(self):
  with self.assertRaises(ControlInputError):scalar_finite_lqr(a=1,b=1,q=1,r=0,terminal_q=1,horizon=2,x0=1)
 def test_nyquist_boundary(self):
  self.assertFalse(nyquist_information(sample_hz=10,max_signal_frequency_hz=5)['ideal_bandlimit_condition_satisfied'])
  self.assertTrue(nyquist_information(sample_hz=11,max_signal_frequency_hz=5)['ideal_bandlimit_condition_satisfied'])
 def test_small_gain(self):
  self.assertTrue(small_gain_sufficient(forward_norm_bound=.5,feedback_norm_bound=.5)['strict_small_gain_condition'])
  self.assertFalse(small_gain_sufficient(forward_norm_bound=2,feedback_norm_bound=1)['strict_small_gain_condition'])
 def test_small_gain_bad(self):
  with self.assertRaises(ControlInputError):small_gain_sufficient(forward_norm_bound=-1,feedback_norm_bound=1)
 def test_casebook(self):self.assertEqual(casebook()['result'],'passed')
 def test_200_seeded_response_checks(self):
  rng=random.Random(1107)
  for _ in range(200):
   x0=rng.uniform(-4,4);xf=rng.uniform(-4,4);tau=rng.uniform(.05,30);t=rng.uniform(0,50)
   d=first_order_response(initial=x0,final=xf,tau_s=tau,time_s=t)['state']
   self.assertAlmostEqual(d,xf+(x0-xf)*math.exp(-t/tau))

if __name__=='__main__':unittest.main()
