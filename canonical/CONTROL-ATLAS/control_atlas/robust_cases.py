"""Authored robustness and diagnostic counterexamples, not physical experiments."""
from .robust import (robust_scalar_feedback_interval,delay_one_sample_scalar,discrete_lyapunov_2x2,
                     first_order_proportional_sensitivity,residual_lag1_diagnostic,watchdog_policy_trace)
from .methods import ControlInputError


def casebook():
    cases=[]
    def check(key,output,passed,source_assumption):
        cases.append({'id':key,'origin':'author_constructed_mathematical_model',
          'result':output,'passed':bool(passed),'assumed_model':source_assumption,
          'physical_controller_deployed':False,'independent_physical_validation':False})
    r=robust_scalar_feedback_interval([.9,1.1],[.25,.45],1)
    check('robust_scalar_interval',r,r['strict_uniform_asymptotic_stability_within_assumed_model'],
          'exact affine scalar pole a-b*k for user-declared interval rectangle')
    r=robust_scalar_feedback_interval([1.35,1.8],[.05,.25],1)
    check('uncertain_scalar_instability_detected',r,not r['strict_uniform_asymptotic_stability_within_assumed_model'],
          'an admissible coefficient corner fails the strict pole condition; no real actuator judged')
    r=delay_one_sample_scalar(1.5,1,1.2)
    check('delay_breaks_nominal_stability',r,r['zero_delay_stable'] and not r['one_sample_delayed_model_stable'],
          'one exact sample of state-feedback delay, input saturations excluded')
    r=discrete_lyapunov_2x2([[.7,0],[0,.9]],[[1,0],[0,1]])
    check('strict_nominal_Lyapunov_candidate',r,r['numerically_positive_definite_P_and_Q'],
          'A stable diagonal mathematical state matrix and P=I')
    r=discrete_lyapunov_2x2([[.5,4],[0,.5]],[[1,0],[0,1]])
    check('failed_P_not_proof_of_instability',r,not r['numerically_positive_definite_P_and_Q'],
          'Nonnormal but stable A with P=I whose Q fails; another P may be valid')
    r=first_order_proportional_sensitivity(2,3,1,.5)
    check('sensitivity_complementarity',r,r['S_plus_T_identity_residual']<1e-14,
          'first-order no-delay model with a proportional controller')
    r=residual_lag1_diagnostic([1,-1,1,-1,1,-1,1,-1])
    check('residual_alternation_not_whiteness',r,r['descriptive_lag1_correlation']<-.8,
          'authored residual sequence, no sampling or significance model')
    trace=[{'now_s':0,'measurement_timestamp_s':0,'measurement_valid':True,'innovation':.1,'requested_output':5},
           {'now_s':1,'measurement_timestamp_s':0,'measurement_valid':True,'innovation':.1,'requested_output':5},
           {'now_s':2,'measurement_timestamp_s':2,'measurement_valid':False,'innovation':.1,'requested_output':5},
           {'now_s':3,'measurement_timestamp_s':3,'measurement_valid':True,'innovation':3,'requested_output':5},
           {'now_s':4,'measurement_timestamp_s':4,'measurement_valid':True,'innovation':.1,'requested_output':5}]
    r=watchdog_policy_trace(trace,max_age_s=.5,maximum_abs_innovation=1,safe_output=0)
    check('illustrative_fault_gate',r,r['blocked_count']==3 and r['accepted_count']==2 and r['trace'][-1]['output']==5,
          'no hardware actuation; user-specified safe output not physically validated')
    return {'schema':'atlas.control-robust-casebook/1','version':'0.3.0','status':'passed' if all(c['passed'] for c in cases) else 'failed',
         'count':len(cases),'cases':cases,'new_real_control_experiments':0,
         'actual_hardware_and_actuators_connected':False,'independent_human_review':False,
         'scientific_v1_accepted':False}
