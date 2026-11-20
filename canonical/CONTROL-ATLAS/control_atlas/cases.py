"""Authored synthetic control-method casebook, never equipment tests."""
from __future__ import annotations
from math import exp
from .models import (first_order_response,zoh_first_order,scalar_discrete_stability,
 state_rank_2x2,pi_first_order_simulation,scalar_kalman,scalar_finite_lqr,
 nyquist_information,small_gain_sufficient)

def casebook():
    cases=[]
    def add(name,result,passed,limitations):
        cases.append({'id':name,'result':result,'passed':bool(passed),
                      'data_origin':'synthetic_authored_test','limitations':limitations})
    x=first_order_response(initial=0,final=1,time_s=10,tau_s=10)
    add('first-order-time-constant',x,abs(x['state']-(1-exp(-1)))<1e-12,'Assumed linear stable system, no actual plant')
    z=zoh_first_order(gain=2,tau_s=5,sample_s=.5)
    add('first-order-zero-order-hold',z,abs(z['a']+z['b']/2-1)<1e-12,'Assumed piecewise-constant input, no hardware sampler')
    y=scalar_discrete_stability(a=1.02)
    add('unstable-discrete-pole',y,not y['asymptotically_stable'],'Only exactly specified scalar LTI')
    ranks=state_rank_2x2(A=[[1,1],[0,1]],B=[.5,1],C=[1,0])
    add('double-integrator-rank',ranks,ranks['controllable_at_absolute_det_tol'] and ranks['observable_at_absolute_det_tol'],
        'Numerical determinant criterion without plant identification')
    setpoints=[3.]*90+[.5]*100
    clamp=pi_first_order_simulation(kp=1.8,ki=1.2,plant_gain=1,tau_s=5,sample_s=.2,
       setpoints=setpoints,u_min=0,u_max=1,antiwindup='clamp')
    none=pi_first_order_simulation(kp=1.8,ki=1.2,plant_gain=1,tau_s=5,sample_s=.2,
       setpoints=setpoints,u_min=0,u_max=1,antiwindup='none')
    add('saturation-antiwindup-comparison',{'clamp_final':clamp['output_final'],
        'without_final':none['output_final'],'clamp_iae':clamp['integral_absolute_error'],
        'without_iae':none['integral_absolute_error'],
        'clamp_integrator':clamp['integrator_final'],'without_integrator':none['integrator_final']},
        clamp['integral_absolute_error']<none['integral_absolute_error'],
        'Only this chosen simulated process; a gain cannot be certified for actual equipment')
    kalman=scalar_kalman(a=1,c=1,process_variance=.01,measurement_variance=.1,
       initial_estimate=0,initial_variance=1,measurements=[.2,.4,.1,.3,.2])
    add('scalar-kalman-recursion',{'final_estimate':kalman['final_estimate'],
        'final_variance':kalman['final_variance'],'gains':[x['gain'] for x in kalman['trace']]},
        kalman['final_variance']>0 and kalman['final_variance']<1,
        'Requires true Gaussian-like model, calibrated covariance and sensor meaning')
    lqr=scalar_finite_lqr(a=1.1,b=1,q=1,r=.1,terminal_q=1,horizon=8,x0=1)
    add('finite-horizon-scalar-lqr',{'cost':lqr['optimal_cost'],'rollout':lqr['rollout_cost'],
        'gain_0':lqr['gains'][0], 'final_state':lqr['final_state']},
        abs(lqr['optimal_cost']-lqr['rollout_cost'])<1e-12,
        'Unconstrained model; no actuator limits or safety guarantee')
    n=nyquist_information(sample_hz=10,max_signal_frequency_hz=5)
    add('nyquist-boundary-refusal',n,not n['ideal_bandlimit_condition_satisfied'],
        'Even sufficient bandlimited sampling does not establish control-loop stability')
    small=small_gain_sufficient(forward_norm_bound=.6,feedback_norm_bound=.7)
    add('small-gain-bound',small,small['strict_small_gain_condition'],
        'True only if stable operator norms and interconnection assumptions hold')
    return {'schema':'atlas.control.casebook/1','cases':cases,'count':len(cases),
            'result':'passed' if all(x['passed'] for x in cases) else 'failed',
            'empirical_control_experiments':0,'real_agent_or_bitwork_interactions':0,
            'independent_scientific_review':False}
