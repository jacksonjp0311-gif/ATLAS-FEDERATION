"""Reproducible authored control-engineering teaching cases, not field results."""
from __future__ import annotations
from math import exp
from .methods import (zoh_first_order, first_order_step,simulate_zoh_first_order,scalar_closed_loop,
     rank_two_state,eigenvalues_2x2,pid_saturated_demo,fit_scalar_arx,alias_frequency,
     scalar_lqr,scalar_kalman_update,ControlInputError)


def casebook()->dict:
    cases=[]
    def add(case,output,checks,description):
        cases.append({'id':case,'origin':'authored_synthetic_teaching','description':description,
                      'result':output,'checks':checks,'passed':all(checks.values()),
                      'experiment_or_safe_controller':False})
    params=zoh_first_order(2,3,.5)
    sim=simulate_zoh_first_order(2,3,.5,[1]*6)
    analytic=first_order_step(2,3,3)
    add('sampled-exact-first-order',{'a':params['a'],'b':params['b'],'step_y6':sim['states'][-1], 'continuous_y3':analytic['output']},
        {'zoh_matches_continuous_step':abs(sim['states'][-1]-analytic['output'])<1e-13},
        'Exact ZOH can match an ideal continuous response at sample times; no measured plant data.')
    stable=scalar_closed_loop(1.2,.5,1.0)
    unstable=scalar_closed_loop(1.2,.5,0.0)
    add('unstable-plant-nominal-feedback',{'open_loop':unstable,'closed_loop':stable},
        {'open_unstable':not unstable['asymptotically_stable_for_scalar_discrete_linear_model'],
         'closed_stable_nominally':stable['asymptotically_stable_for_scalar_discrete_linear_model']},
        'Nominal feedback pole classification; saturation or delay can break it.')
    plant=rank_two_state([[1,.2],[0,1]],[0,.2],[1,0])
    dead=rank_two_state([[.8,0],[0,.9]],[1,0],[1,0])
    add('two-state-structural-tests',{'double_integrator':plant,'unreachable_unobserved':dead},
        {'reachable':plant['controllability_rank_numerically_full'],
         'observable':plant['observability_rank_numerically_full'],
         'unreachable':not dead['controllability_rank_numerically_full'],
         'unobserved':not dead['observability_rank_numerically_full']},
        'Two-state determinant tests; actuator limits, sensor noise and coordinate scaling omitted.')
    PID=dict(kp=1,ki=.5,kd=0,dt_s=1,setpoints=[10]*8,measurements=[0]*8,minimum_u=-1,maximum_u=1)
    raw=pid_saturated_demo(**PID,clamp_antiwindup=False)
    clamp=pid_saturated_demo(**PID,clamp_antiwindup=True)
    add('pid-clamping-and-windup',{'raw_final_i':raw['final_integral'],'clamped_final_i':clamp['final_integral']},
        {'raw_accumulates':raw['final_integral']>0,'clamped_stops':clamp['final_integral']==0},
        'Controller-only arithmetic demonstrates one antiwindup policy; no closed-loop stability proven.')
    alias=alias_frequency(70,100)
    add('sampled-aliasing',alias,
        {'70_folds_to_30':alias['aliased_frequency_hz']==30,'nyquist_violated':not alias['below_nyquist']},
        'A 70 Hz sinusoid sampled at 100 Hz has 30 Hz alias magnitude, absent bandlimiting prior.')
    inputs=[0,1,0,2,-1,3,0,1,2,-2,2,0]
    x=[.4]
    for u in inputs:x.append(.8*x[-1]+.3*u)
    identified=fit_scalar_arx(x,inputs)
    add('exactly-identified-authored-plant',identified,
        {'a_recovered':abs(identified['a_hat']-.8)<1e-12,'b_recovered':abs(identified['b_hat']-.3)<1e-12,
         'rss_zero':identified['rss']<1e-23},
        'Noiseless synthetic inputs intentionally excite both regressors; not a real system ID study.')
    lqr=scalar_lqr(1.2,1,1,1)
    add('scalar-infinite-horizon-LQR',lqr,
        {'positive_cost':lqr['P']>0,'stabilizing':abs(lqr['closed_loop_pole'])<1},
        'Unconstrained linear-quadratic feedback optimal only for stipulated model and cost.')
    kal=scalar_kalman_update(1,0,1,.25,.25,2)
    add('conditional-scalar-kalman',kal,
        {'gain_between_0_1':0<kal['gain']<1,'posterior_covariance_shrinks':kal['posterior_variance']<kal['predicted_variance']},
        'One known linear noise-model update; not an authenticated sensor estimate.')
    complex_poles=eigenvalues_2x2([[.8,-.1],[.1,.8]])
    add('complex-discrete-poles',complex_poles,
        {'rho_is_sqrtpoint65':abs(complex_poles['spectral_radius']-(.65)**.5)<1e-14,
         'nominal_stable':complex_poles['asymptotically_stable_if_discrete_LTI']},
        'Complex eigenvalue modulus, not real-plant robust stability.')
    return {'schema':'atlas.control-casebook/1','count':len(cases),'status':'passed' if all(c['passed'] for c in cases) else 'failed',
            'cases':cases,'real_physical_measurements':False,'real_controller_actions':False,
            'independently_reviewed_science':False,'live_bitwork_run':False}
