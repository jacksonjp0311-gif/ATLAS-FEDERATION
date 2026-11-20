"""Constructed v0.4 experiments; no equipment, simulator sensors or real interventions."""
from .advanced import (mimo_2x2_return_difference,common_lyapunov_box_2x2,
      finite_horizon_lqr_2state,scalar_grid_open_loop_plan,
      normalized_innovation_two_sensor,ambiguous_sensor_state_bias,arx_training_validation_split)

def casebook():
    cases=[]
    def add(name,result,passes,explanation):
        cases.append({'name':name,'origin':'author_constructed_model_not_real_plant',
                      'result':result,'passed':bool(passes),'explanation':explanation})
    g=((1,-1.99),(-1.99,1))
    r=mimo_2x2_return_difference(g,((1,0),(0,1)))
    add('mimo_near_singular_return_difference',r,r['condition_number']>350,
        'A seemingly finite 2x2 loop matrix has one very small return-difference singular direction; no dynamic stability inferred.')
    r=common_lyapunov_box_2x2([[(.5,.6),(-.03,.03)],[(-.03,.03),(.3,.4)]],((1,0),(0,1)))
    add('common_quadratic_box_sufficiency',r,r['common_P_strict_decay_numerically_certified'],
        'One supplied P exhibits strict numeric contraction at every matrix-box vertex, a sufficient model-only certificate.')
    bad=common_lyapunov_box_2x2([[(.8,.8),(1,1)],[(0,0),(.8,.8)]],((1,0),(0,1)))
    add('failed_P_not_instability',bad,not bad['common_P_strict_decay_numerically_certified'],
        'Stable upper triangular matrix with eigenvalues .8 has P=I fail; no inference of instability from failed candidate.')
    opt=finite_horizon_lqr_2state(((1,1),(0,1)),(.5,1),((10,0),(0,1)),.25,((10,0),(0,1)),8,(2,0))
    add('two_state_Riccati_cost_identity',opt,opt['cost_identity_residual']<1e-8,
        'Finite horizon unconstrained Riccati value agrees with model rollout; no hard actuator/state constraints.')
    plan=scalar_grid_open_loop_plan(1,1,1.5,4,[-.75,-.5,0,.5,.75],.75,2,1,.1,4)
    add('grid_plan_not_continuous_MPC',plan,plan['status']=='feasible_grid_candidate',
        'Finds best sequence in a finite explicit grid; does not establish continuous constrained optimum or real-time control.')
    no=scalar_grid_open_loop_plan(1.3,1,1.9,3,[-.1,0,.1],.1,2,1,.1)
    add('grid_no_candidate_not_global_infeasible',no,no['status']=='no_feasible_candidate_on_grid',
        'Grid may contain no feasible candidate; conclusion intentionally does not assert continuous-problem infeasibility.')
    nis=normalized_innovation_two_sensor((2,0),((4,1),(1,1)))
    add('correlated_innovation_squared',nis,abs(nis['NIS']-4/3)<1e-12,
        'Correlation changes normalized residual magnitude; no fault cause can be derived from NIS alone.')
    both=ambiguous_sensor_state_bias(10,[{'hypothesis':'real_state_10','state':10,'sensor_bias':0},
        {'hypothesis':'real_state_8','state':8,'sensor_bias':2}])
    add('sensor_bias_vs_state_ambiguous',both,both['both_hypotheses_match_single_measurement'],
        'Two physically distinct hypotheses produce the same reading; an additional sensor or experiment is needed.')
    controls=[0,2,-1,1,3,-2,1,0,2,-2,3,1,0,-1,1,2,-3,1,0,2,-1,1,2,0,-2,3,1,0,2,-1,1,0]
    x=[.3]
    for i,u in enumerate(controls):x.append((.8 if i<24 else .95)*x[-1]+.2*u)
    idr=arx_training_validation_split(x,controls,24)
    add('time_split_parameter_drift',idr,idr['later_one_step_RMS']>idr['train_one_step_RMS']+1e-4,
        'Training on one scalar model does not validate later samples after a constructed parameter shift.')
    return {'schema':'atlas.control-advanced-v04-casebook/1','status':'passed' if all(z['passed'] for z in cases) else 'failed',
       'count':len(cases),'cases':cases,'real_plant_samples':0,'live_actuation':False,
       'heldout_ai_evaluation':False,'scientific_independent_review':False}
