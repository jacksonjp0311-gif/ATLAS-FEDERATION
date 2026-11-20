"""Control v0.4 new model checks and adversarial refusal tests, stdlib unittest."""
import math,unittest,copy
from control_atlas.advanced import (
    mimo_2x2_return_difference,common_lyapunov_box_2x2,
    finite_horizon_lqr_2state,scalar_grid_open_loop_plan,
    normalized_innovation_two_sensor,ambiguous_sensor_state_bias,
    arx_training_validation_split)
from control_atlas.advanced_cases import casebook
from control_atlas.methods import ControlInputError

class MimoTests(unittest.TestCase):
 def test_identity(self):
  d=mimo_2x2_return_difference([[1,2],[0,1]],[[1,0],[0,1]])
  self.assertLess(d['S_plus_T_identity_max_error'],1e-12)
  self.assertGreater(d['singular_values'][0],d['singular_values'][1])
 def test_near_singular_direction(self):
  d=mimo_2x2_return_difference([[1,-1.99],[-1.99,1]],[[1,0],[0,1]])
  self.assertGreater(d['condition_number'],350)
 def test_singular_rejected(self):
  with self.assertRaises(ControlInputError):mimo_2x2_return_difference([[-1,0],[0,0]],[[1,0],[0,1]])
 def test_bad_shapes(self):
  with self.assertRaises(ControlInputError):mimo_2x2_return_difference([[1,2]],[[1,0],[0,1]])
 def test_nan(self):
  with self.assertRaises(ControlInputError):mimo_2x2_return_difference([[1,float('nan')],[0,1]],[[1,0],[0,1]])

class LyapunovTests(unittest.TestCase):
 def test_common_certificate(self):
  d=common_lyapunov_box_2x2([[[.5,.6],[-.03,.03]],[[-.03,.03],[.3,.4]]],[[1,0],[0,1]])
  self.assertEqual(d['vertices_checked'],16)
  self.assertTrue(d['common_P_strict_decay_numerically_certified'])
 def test_failed_candidate_does_not_label_unstable(self):
  d=common_lyapunov_box_2x2([[[.8,.8],[1,1]],[[0,0],[.8,.8]]],[[1,0],[0,1]])
  self.assertFalse(d['common_P_strict_decay_numerically_certified'])
  self.assertIn('NOT proof',d['limits'][0])
 def test_non_pd_P(self):
  with self.assertRaises(ControlInputError):common_lyapunov_box_2x2([[[.5,.6],[0,0]],[[0,0],[.3,.4]]],[[0,0],[0,-1]])
 def test_unordered_bounds(self):
  with self.assertRaises(ControlInputError):common_lyapunov_box_2x2([[[.6,.5],[0,0]],[[0,0],[.3,.4]]],[[1,0],[0,1]])
 def test_nonsymmetric_P(self):
  with self.assertRaises(ControlInputError):common_lyapunov_box_2x2([[[.5,.6],[0,0]],[[0,0],[.3,.4]]],[[1,1],[0,1]])

class LqrTests(unittest.TestCase):
 def test_riccati_value_identity(self):
  d=finite_horizon_lqr_2state([[1,1],[0,1]],[.5,1],[[10,0],[0,1]],.25,[[10,0],[0,1]],8,[2,0])
  self.assertLess(d['cost_identity_residual'],1e-9)
  self.assertEqual(len(d['predicted_states']),9)
  self.assertEqual(len(d['gains']),8)
 def test_zero_initial_state(self):
  d=finite_horizon_lqr_2state([[1,1],[0,1]],[.5,1],[[1,0],[0,1]],1,[[1,0],[0,1]],4,[0,0])
  self.assertEqual(d['realized_quadratic_cost'],0)
 def test_indefinite_cost_rejected(self):
  with self.assertRaises(ControlInputError):finite_horizon_lqr_2state([[1,0],[0,1]],[1,0],[[1,0],[0,-1]],1,[[1,0],[0,1]],4,[1,0])
 def test_unsymmetric_cost_rejected(self):
  with self.assertRaises(ControlInputError):finite_horizon_lqr_2state([[1,0],[0,1]],[1,0],[[1,2],[0,1]],1,[[1,0],[0,1]],4,[1,0])
 def test_horizon_guard(self):
  with self.assertRaises(ControlInputError):finite_horizon_lqr_2state([[1,0],[0,1]],[1,0],[[1,0],[0,1]],1,[[1,0],[0,1]],0,[1,0])
 def test_input_cost_positive(self):
  with self.assertRaises(ControlInputError):finite_horizon_lqr_2state([[1,0],[0,1]],[1,0],[[1,0],[0,1]],0,[[1,0],[0,1]],2,[1,0])

class GridPlanTests(unittest.TestCase):
 def test_feasible(self):
  d=scalar_grid_open_loop_plan(1,1,1.5,4,[-.75,-.5,0,.5,.75],.75,2,1,.1,4)
  self.assertEqual(d['status'],'feasible_grid_candidate')
  self.assertTrue(all(abs(x)<=2 for x in d['best']['states']))
  self.assertTrue(all(abs(u)<=.75 for u in d['best']['controls']))
 def test_no_candidate_not_global_proof(self):
  d=scalar_grid_open_loop_plan(1.3,1,1.9,3,[-.1,0,.1],.1,2,1,.1)
  self.assertEqual(d['status'],'no_feasible_candidate_on_grid')
  self.assertIn('NOT prove',d['limits'][2])
 def test_duplicate_grid_refused(self):
  with self.assertRaises(ControlInputError):scalar_grid_open_loop_plan(1,1,0,2,[0,0],1,2,1,.1)
 def test_input_bound_refusal(self):
  with self.assertRaises(ControlInputError):scalar_grid_open_loop_plan(1,1,0,2,[-2,0,2],1,2,1,.1)
 def test_horizon_guard(self):
  with self.assertRaises(ControlInputError):scalar_grid_open_loop_plan(1,1,0,6,[-1,0,1],1,2,1,.1)

class SensorTests(unittest.TestCase):
 def test_correlated_nis(self):
  d=normalized_innovation_two_sensor([2,0],[[4,1],[1,1]])
  self.assertAlmostEqual(d['NIS'],4/3)
 def test_covariance_not_psd(self):
  with self.assertRaises(ControlInputError):normalized_innovation_two_sensor([1,1],[[1,3],[3,1]])
 def test_covariance_singular(self):
  with self.assertRaises(ControlInputError):normalized_innovation_two_sensor([1,1],[[1,1],[1,1]])
 def test_ambiguity(self):
  r=ambiguous_sensor_state_bias(10,[{'hypothesis':'state10','state':10,'sensor_bias':0},
          {'hypothesis':'state8','state':8,'sensor_bias':2}])
  self.assertTrue(r['both_hypotheses_match_single_measurement'])
 def test_wrong_hypotheses(self):
  r=ambiguous_sensor_state_bias(10,[{'hypothesis':'state10','state':10,'sensor_bias':0},
          {'hypothesis':'state8','state':8,'sensor_bias':1}])
  self.assertFalse(r['both_hypotheses_match_single_measurement'])
 def test_bad_label(self):
  with self.assertRaises(ControlInputError):ambiguous_sensor_state_bias(10,[{'hypothesis':'','state':10,'sensor_bias':0},
          {'hypothesis':'state8','state':8,'sensor_bias':2}])

class IdentificationTests(unittest.TestCase):
 def test_drift(self):
  c=casebook()
  result=next(x for x in c['cases'] if x['name']=='time_split_parameter_drift')['result']
  self.assertGreater(result['later_one_step_RMS'],.1)
  self.assertLess(result['train_one_step_RMS'],1e-10)
 def test_weak_excitation_rejected(self):
  x=[1]*12;u=[0]*11
  with self.assertRaises(ControlInputError):arx_training_validation_split(x,u,7)
 def test_wrong_lengths(self):
  with self.assertRaises(ControlInputError):arx_training_validation_split([1,2,3],[1,2,3],5)
 def test_all_casebook(self):
  r=casebook();self.assertEqual(r['status'],'passed');self.assertEqual(r['count'],9)

if __name__=='__main__':unittest.main()
