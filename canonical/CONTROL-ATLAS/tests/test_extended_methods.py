import unittest,math,random,json,subprocess,sys
from control_atlas.methods import *
from control_atlas.extended_cases import casebook
class CoreControlTests(unittest.TestCase):
    def test_casebook_all(self):self.assertEqual(casebook()['status'],'passed')
    def test_zoh_simple(self):
        d=zoh_first_order(2,3,.5);self.assertAlmostEqual(d['a'],math.exp(-1/6));self.assertAlmostEqual(d['b'],2*(1-math.exp(-1/6)))
    def test_zoh_vs_analytic(self):
        x=simulate_zoh_first_order(2,3,.5,[1]*6)['states'][-1]
        self.assertAlmostEqual(x,first_order_step(2,3,3)['output'])
    def test_zoh_no_negative_tau(self):
        with self.assertRaises(ControlInputError):zoh_first_order(2,-1,.5)
    def test_zoh_no_negative_dt(self):
        with self.assertRaises(ControlInputError):zoh_first_order(1,1,0)
    def test_first_order_at_zero(self):self.assertEqual(first_order_step(2,3,0,1,3)['output'],3)
    def test_first_order_limit(self):self.assertAlmostEqual(first_order_step(2,3,300)['output'],2)
    def test_first_order_negative_time_reject(self):
        with self.assertRaises(ControlInputError):first_order_step(2,3,-1)
    def test_sim_input_length(self):
        with self.assertRaises(ControlInputError):simulate_zoh_first_order(2,3,.5,[])
    def test_sim_nan(self):
        with self.assertRaises(ControlInputError):simulate_zoh_first_order(2,3,.5,[float('nan')])
    def test_scalar_stability(self):self.assertTrue(scalar_closed_loop(1.2,.5,1)['asymptotically_stable_for_scalar_discrete_linear_model'])
    def test_scalar_open_unstable(self):self.assertFalse(scalar_closed_loop(1.2,.5,0)['asymptotically_stable_for_scalar_discrete_linear_model'])
    def test_scalar_boundary_not_asymptotic(self):self.assertFalse(scalar_closed_loop(1,1,0)['asymptotically_stable_for_scalar_discrete_linear_model'])
    def test_eigen_complex(self):self.assertAlmostEqual(eigenvalues_2x2([[.8,-.1],[.1,.8]])['spectral_radius'],math.sqrt(.65))
    def test_eigen_real(self):self.assertAlmostEqual(eigenvalues_2x2([[.6,0],[0,.9]])['spectral_radius'],.9)
    def test_eigen_dimensions_reject(self):
        with self.assertRaises(ControlInputError):eigenvalues_2x2([[.5]])
    def test_controllable_observable(self):
        d=rank_two_state([[1,.2],[0,1]],[0,.2],[1,0]);self.assertTrue(d['controllability_rank_numerically_full']);self.assertTrue(d['observability_rank_numerically_full'])
    def test_unreachable(self):self.assertFalse(rank_two_state([[.8,0],[0,.9]],[1,0],[1,0])['controllability_rank_numerically_full'])
    def test_unobserved(self):self.assertFalse(rank_two_state([[.8,0],[0,.9]],[1,0],[1,0])['observability_rank_numerically_full'])
    def test_controllability_bad_input(self):
        with self.assertRaises(ControlInputError):rank_two_state([[1,0],[0,1]],[1],[1,0])
    def test_controllability_tol(self):
        with self.assertRaises(ControlInputError):rank_two_state([[1,0],[0,1]],[1,1],[1,1],1)
    def test_pid_output_clamped(self):
        d=pid_saturated_demo(1,1,0,1,[10]*3,[0]*3,-1,1)
        self.assertTrue(all(abs(x['clamped_u'])<=1 for x in d['trace']))
    def test_pid_antiwindup(self):
        args=[1,.5,0,1,[10]*8,[0]*8,-1,1]
        a=pid_saturated_demo(*args,clamp_antiwindup=True);b=pid_saturated_demo(*args,clamp_antiwindup=False)
        self.assertLess(a['final_integral'],b['final_integral'])
    def test_pid_bad_actuator_limits(self):
        with self.assertRaises(ControlInputError):pid_saturated_demo(1,1,0,1,[1],[0],1,-1)
    def test_pid_mismatch_list(self):
        with self.assertRaises(ControlInputError):pid_saturated_demo(1,1,0,1,[1,1],[0],-1,1)
    def test_pid_measured_derivative(self):
        d=pid_saturated_demo(1,0,1,.5,[1,1],[0,.5],-10,10)
        self.assertEqual(d['trace'][1]['D_on_measurement'],-1)
    def test_id_recover_noise_free(self):
        u=[0,1,0,2,-1,3,0,1,2,-2,2,0];x=[.4]
        for v in u:x.append(.8*x[-1]+.3*v)
        d=fit_scalar_arx(x,u)
        self.assertAlmostEqual(d['a_hat'],.8);self.assertAlmostEqual(d['b_hat'],.3);self.assertLess(d['rss'],1e-25)
    def test_id_no_excitation(self):
        with self.assertRaises(ControlInputError):fit_scalar_arx([0]*8,[0]*7)
    def test_id_short(self):
        with self.assertRaises(ControlInputError):fit_scalar_arx([1,1,1],[0,0])
    def test_id_malformed(self):
        with self.assertRaises(ControlInputError):fit_scalar_arx([0]*8,[0]*6)
    def test_alias_70_100(self):self.assertEqual(alias_frequency(70,100)['aliased_frequency_hz'],30)
    def test_alias_no_f(self):self.assertEqual(alias_frequency(0,100)['aliased_frequency_hz'],0)
    def test_alias_negative(self):
        with self.assertRaises(ControlInputError):alias_frequency(-1,100)
    def test_lqr_stabilizing(self):
        d=scalar_lqr(1.2,1,1,1);self.assertTrue(d['stabilizing_scalar_model']);self.assertLess(abs(d['closed_loop_pole']),1)
    def test_lqr_no_actuation(self):
        with self.assertRaises(ControlInputError):scalar_lqr(1,0,1,1)
    def test_lqr_bad_weights(self):
        with self.assertRaises(ControlInputError):scalar_lqr(1,1,-1,1)
    def test_kalman_one_step(self):
        d=scalar_kalman_update(1,0,1,.25,.25,2);self.assertAlmostEqual(d['gain'],5/6)
        self.assertAlmostEqual(d['posterior_variance'],5/24)
    def test_kalman_bad_sensor_variance(self):
        with self.assertRaises(ControlInputError):scalar_kalman_update(1,0,1,.25,0,2)
    def test_kalman_shrinks_variance(self):
        d=scalar_kalman_update(.8,0,1,.3,.2,1);self.assertLess(d['posterior_variance'],d['predicted_variance'])
    def test_scalar_overlarge_magnitude_rejected(self):
        with self.assertRaises(ControlInputError):scalar_closed_loop(1e50,1,1)
    def test_very_small_tau_ratio_refused(self):
        with self.assertRaises(ControlInputError):zoh_first_order(1,1e-300,1e10)
    def test_bool_as_number_rejected(self):
        with self.assertRaises(ControlInputError):zoh_first_order(True,1,.1)
    def test_cli_casebook(self):
        out=subprocess.run([sys.executable,'-m','control_atlas','extended-casebook'],capture_output=True,text=True)
        self.assertEqual(out.returncode,0,out.stderr)
        self.assertEqual(json.loads(out.stdout)['status'],'passed')
    def test_cli_invalid(self):
        out=subprocess.run([sys.executable,'-m','control_atlas','unknown'],capture_output=True,text=True)
        self.assertNotEqual(out.returncode,0)

if __name__=='__main__':unittest.main()
