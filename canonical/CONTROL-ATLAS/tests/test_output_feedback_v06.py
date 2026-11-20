"""Self-contained regression cases for offline output-feedback interval methods."""
import random,unittest,math
from control_atlas.methods import ControlInputError
from control_atlas.output_feedback import (
    scalar_observer_error_bound,scalar_actuator_step,scalar_output_feedback_tube,
    scalar_measurement_consistency,_lin_interval,_clip_interval)
from control_atlas.output_feedback_cases import casebook

P={'plant_a':.6,'plant_b':.2,'feedback_k':.4,'observer_gain':.55,
   'estimated_initial_state':.1,'initial_state_error_radius':.05,
   'process_disturbance_radius':.01,'sensor_noise_radius':.01,
   'previous_applied_input':0,'actuator_abs_limit':.4,'actuator_max_delta':.1,
   'actuator_response_fraction':.6,'state_abs_limit':1,'steps':12}

class ObserverTests(unittest.TestCase):
    def test_stationary_scalar(self):
        a=scalar_observer_error_bound(plant_a=.8,observer_gain=.6,initial_error_radius=.1,
          process_disturbance_radius=.02,measurement_noise_radius=.01,steps=12)
        self.assertAlmostEqual(a['stationary_sufficient_error_radius'],.0325)
        self.assertEqual(len(a['error_radii']),13)
        self.assertTrue(a['stationary_error_bound_available'])
    def test_nonconvergent(self):
        a=scalar_observer_error_bound(plant_a=1.3,observer_gain=.1,initial_error_radius=.1,
          process_disturbance_radius=.02,measurement_noise_radius=.01,steps=10)
        self.assertFalse(a['stationary_error_bound_available'])
        self.assertIsNone(a['stationary_sufficient_error_radius'])
    def test_observer_noise_increases_bound(self):
        def f(v):return scalar_observer_error_bound(plant_a=.7,observer_gain=.5,initial_error_radius=.1,
          process_disturbance_radius=.02,measurement_noise_radius=v,steps=10)['error_radii'][-1]
        self.assertGreater(f(.2),f(.01))
    def test_invalid_radii(self):
        for val in [-.1,float('nan'),float('inf'),True]:
            with self.subTest(val=val), self.assertRaises(ControlInputError):
                scalar_observer_error_bound(plant_a=.7,observer_gain=.5,initial_error_radius=.1,
                  process_disturbance_radius=.02,measurement_noise_radius=val,steps=10)
    def test_invalid_steps(self):
        for val in [0,257,2.1,True,'10']:
            with self.subTest(val=val), self.assertRaises(ControlInputError):
                scalar_observer_error_bound(plant_a=.7,observer_gain=.5,initial_error_radius=.1,
                  process_disturbance_radius=.02,measurement_noise_radius=.01,steps=val)
    def test_exact_error_extremes_within_bound(self):
        rng=random.Random(615)
        for trial in range(120):
            a=rng.uniform(-.9,.9);L=rng.uniform(-1,1);E=rng.uniform(0,.4)
            W=rng.uniform(0,.1);V=rng.uniform(0,.1)
            r=scalar_observer_error_bound(plant_a=a,observer_gain=L,initial_error_radius=E,
                process_disturbance_radius=W,measurement_noise_radius=V,steps=9)
            e=rng.uniform(-E,E)
            for bound in r['error_radii'][1:]:
                e=(a-L)*e + rng.uniform(-W,W) - L*rng.uniform(-V,V)
                self.assertLessEqual(abs(e),bound+1e-12)

class ActuatorTests(unittest.TestCase):
    def test_saturation_slew_lag(self):
        r=scalar_actuator_step(requested_input=10,previous_applied_input=0,
            max_abs_input=1,max_delta_per_step=.2,response_fraction=.5)
        self.assertEqual(r['magnitude_clamped_target'],1)
        self.assertEqual(r['slew_limited_target'],.2)
        self.assertAlmostEqual(r['applied_input_next'],.1)
    def test_lag_endpoints(self):
        for alpha in [.00001,1]:
            r=scalar_actuator_step(requested_input=1,previous_applied_input=0,
                max_abs_input=2,max_delta_per_step=2,response_fraction=alpha)
            self.assertAlmostEqual(r['applied_input_next'],alpha)
    def test_zero_rate_does_not_move(self):
        r=scalar_actuator_step(requested_input=-1,previous_applied_input=.2,
           max_abs_input=1,max_delta_per_step=0,response_fraction=.5)
        self.assertEqual(r['applied_input_next'],.2)
    def test_bad_old_command(self):
        with self.assertRaises(ControlInputError):scalar_actuator_step(requested_input=0,previous_applied_input=2,
           max_abs_input=1,max_delta_per_step=.1,response_fraction=.5)
    def test_invalid_lag(self):
        for alpha in [0,1.1,-1,float('nan')]:
            with self.subTest(alpha=alpha),self.assertRaises(ControlInputError):
                scalar_actuator_step(requested_input=1,previous_applied_input=0,
                max_abs_input=1,max_delta_per_step=.1,response_fraction=alpha)
    def test_random_magnitude_and_rate(self):
        rng=random.Random(13)
        for _ in range(500):
            U=rng.uniform(.1,10);D=rng.uniform(0,2*U);prev=rng.uniform(-U,U)
            req=rng.uniform(-10*U,10*U);alpha=rng.uniform(.001,1)
            r=scalar_actuator_step(requested_input=req,previous_applied_input=prev,
              max_abs_input=U,max_delta_per_step=D,response_fraction=alpha)
            self.assertLessEqual(abs(r['applied_input_next']),U+1e-12)
            self.assertLessEqual(abs(r['applied_input_next']-prev),D+1e-12)

class TubeTests(unittest.TestCase):
    def test_sampled_tube(self):
        t=scalar_output_feedback_tube(**P)
        self.assertEqual(len(t['timeline']),13)
        self.assertTrue(t['all_sampled_states_within_limit_under_assumed_model'])
        self.assertEqual(t['origin'],'derived_scalar_plant_estimator_actuator_interval_arithmetic')
    def test_tight_limit_veto(self):
        t=scalar_output_feedback_tube(**{**P,'state_abs_limit':.04})
        self.assertFalse(t['all_sampled_states_within_limit_under_assumed_model'])
    def test_lag_changes_tube(self):
        t=scalar_output_feedback_tube(**{**P,'actuator_response_fraction':.01})
        p=scalar_output_feedback_tube(**P)
        self.assertNotEqual(t['timeline'][-1]['physical_state_interval'],p['timeline'][-1]['physical_state_interval'])
    def test_zero_disturbance_zero_interval(self):
        p={**P,'initial_state_error_radius':0,'process_disturbance_radius':0,'sensor_noise_radius':0}
        t=scalar_output_feedback_tube(**p)
        for d in t['timeline']:
            self.assertAlmostEqual(d['physical_state_interval'][0],d['physical_state_interval'][1])
            self.assertAlmostEqual(d['observer_estimate_interval'][0],d['observer_estimate_interval'][1])
    def test_lag_and_slew_bound(self):
        p={**P,'actuator_response_fraction':.2,'actuator_max_delta':.01}
        t=scalar_output_feedback_tube(**p)
        for j,d in enumerate(t['timeline']):
            self.assertTrue(all(abs(z)<=p['actuator_abs_limit']+1e-10 for z in d['applied_actuator_interval']))
    def test_bad_initial_actuator(self):
        with self.assertRaises(ControlInputError):scalar_output_feedback_tube(**{**P,'previous_applied_input':1})
    def test_step_count_bounds(self):
        for steps in [0,101,1.1,True]:
            with self.subTest(steps=steps),self.assertRaises(ControlInputError):scalar_output_feedback_tube(**{**P,'steps':steps})
    def test_invalid_noise(self):
        with self.assertRaises(ControlInputError):scalar_output_feedback_tube(**{**P,'sensor_noise_radius':-.0001})
    def test_independently_generated_trajectories_are_enclosed(self):
        # This is a stochastic check of a *logically derived conservative interval*;
        # it is not a Monte Carlo proof of any real physical system.
        rng=random.Random(610622)
        for case in range(60):
            p={**P,'plant_a':rng.uniform(.2,.9),'plant_b':rng.uniform(.05,.7),
                 'feedback_k':rng.uniform(.1,2),'observer_gain':rng.uniform(.1,.9),
                 'estimated_initial_state':rng.uniform(-.25,.25),
                 'initial_state_error_radius':rng.uniform(0,.1),
                 'process_disturbance_radius':rng.uniform(0,.035),
                 'sensor_noise_radius':rng.uniform(0,.02),
                 'actuator_response_fraction':rng.uniform(.05,1),
                 'actuator_max_delta':rng.uniform(.01,.25),'actuator_abs_limit':.9,
                 'previous_applied_input':rng.uniform(-.1,.1),'steps':15,'state_abs_limit':3.}
            t=scalar_output_feedback_tube(**p)['timeline']
            for _ in range(5):
                x=p['estimated_initial_state']+rng.uniform(-p['initial_state_error_radius'],p['initial_state_error_radius'])
                h=p['estimated_initial_state'];u=p['previous_applied_input']
                for k in range(16):
                    self.assertLessEqual(t[k]['physical_state_interval'][0]-1e-10,x)
                    self.assertLessEqual(x,t[k]['physical_state_interval'][1]+1e-10)
                    self.assertLessEqual(t[k]['observer_estimate_interval'][0]-1e-10,h)
                    self.assertLessEqual(h,t[k]['observer_estimate_interval'][1]+1e-10)
                    self.assertLessEqual(t[k]['applied_actuator_interval'][0]-1e-10,u)
                    self.assertLessEqual(u,t[k]['applied_actuator_interval'][1]+1e-10)
                    if k==15:break
                    w=rng.uniform(-p['process_disturbance_radius'],p['process_disturbance_radius'])
                    v=rng.uniform(-p['sensor_noise_radius'],p['sensor_noise_radius'])
                    u_new=scalar_actuator_step(requested_input=-p['feedback_k']*h,previous_applied_input=u,
                      max_abs_input=p['actuator_abs_limit'],max_delta_per_step=p['actuator_max_delta'],
                      response_fraction=p['actuator_response_fraction'])['applied_input_next']
                    h_new=p['plant_a']*h+p['plant_b']*u+p['observer_gain']*(x+v-h)
                    x_new=p['plant_a']*x+p['plant_b']*u+w
                    x,h,u=x_new,h_new,u_new

class FaultEvidenceTests(unittest.TestCase):
    def test_consistent(self):
        r=scalar_measurement_consistency(measured_output=.1,estimated_state=.1,
           estimated_state_error_radius=.05,sensor_noise_radius=.01)
        self.assertTrue(r['consistent_given_bounds'])
    def test_contradiction_does_not_isolate_fault(self):
        r=scalar_measurement_consistency(measured_output=.4,estimated_state=.1,
           estimated_state_error_radius=.05,sensor_noise_radius=.01)
        self.assertEqual(r['status'],'inconsistent_not_root_cause_isolated')
        self.assertIn('plant-model error',r['not_identified'])
    def test_edge_inclusive(self):
        r=scalar_measurement_consistency(measured_output=.16,estimated_state=.1,
           estimated_state_error_radius=.05,sensor_noise_radius=.01)
        self.assertTrue(r['consistent_given_bounds'])
    def test_invalid_noise(self):
        with self.assertRaises(ControlInputError):scalar_measurement_consistency(measured_output=.1,estimated_state=.1,
           estimated_state_error_radius=-.1,sensor_noise_radius=.01)
    def test_casebook(self):
        r=casebook();self.assertEqual(r['result'],'passed');self.assertEqual(r['count'],12)
        self.assertTrue(all(x['passed'] for x in r['cases']))

if __name__=='__main__':unittest.main()
