"""New original Control Atlas v0.5 investigations, entirely mathematical models."""
from .invariance import robust_invariant_box_2x2, scalar_robust_interval, simulate_2x2_state_feedback
from .methods import ControlInputError


def casebook():
    c=[]
    def add(name,r,passes,explanation):
        c.append({'id':name,'origin':'synthetic_authored_mathematical_case','result':r,
          'passed':bool(passes),'explanation':explanation})
    safe=robust_invariant_box_2x2(A_intervals=[[(.3,.4),(-.03,.03)],[(-.02,.02),(.2,.3)]],
       B_intervals=[(.8,.9),(.1,.2)],state_feedback_K=[.1,.1],state_radii=[1,1],disturbance_radii=[.05,.05],
       actuator_limit=.25,full_state_available=True)
    add('conditionally_robust_box',safe,safe['conditional_invariance_and_input_feasibility'] and safe['vertices_checked']==64,
        'Conditional box invariant and input-feasible under declared independent 2x2 model, not qualified hardware.')
    violated=robust_invariant_box_2x2(A_intervals=[[(.95,1.05),(-.03,.03)],[(-.02,.02),(.9,1.1)]],
       B_intervals=[(.8,.9),(.1,.2)],state_feedback_K=[.1,.1],state_radii=[1,1],disturbance_radii=[.1,.1],
       actuator_limit=.25,full_state_available=True)
    add('invariance_candidate_refused',violated,not violated['conditional_invariance_and_input_feasibility'],
        'A selected box fails the mathematical sufficient conditions; it says nothing about actual equipment safety.')
    tight=robust_invariant_box_2x2(A_intervals=[[(.3,.4),(-.03,.03)],[(-.02,.02),(.2,.3)]],
       B_intervals=[(.8,.9),(.1,.2)],state_feedback_K=[.1,.1],state_radii=[1,1],disturbance_radii=[.05,.05],
       actuator_limit=.12,full_state_available=True)
    add('actuator_limit_breaks_certificate',tight,tight['state_box_invariant_for_every_assumed_model'] and not tight['actuator_unsaturated_for_every_state_in_box'],
        'A mathematically invariant closed-loop state model does not imply input commands fit the actuator.')
    scalar=scalar_robust_interval(closed_loop_gain=.7,state_radius=1,disturbance_radius=.2,input_gain=.2,input_limit=.3,state_feedback_exact=True)
    add('scalar_disturbance_box',scalar,scalar['conditional_certificate'] and abs(scalar['worst_one_step_abs_state']-.9)<1e-12,
        'Simple exact scalar interval invariant under a stipulated bounded disturbance.')
    d=[[.05,0],[-.05,0],[0,.05],[0,-.05]]*3
    a=((.6,0),(0,.7));b=(.2,.2);k=(.3,.2)
    sim=simulate_2x2_state_feedback(A=a,B=b,K=k,x0=[.4,.5],disturbances=d,input_limit=.2)
    add('bounded_synthetic_rollout',sim,len(sim['states'])==len(d)+1 and sim['saturated_steps']>=0,
        'An observed finite trajectory is not a universal guarantee over all disturbances and initial states.')
    bias=[[0,0]]*6+[[.5,-.5]]*6
    biased=simulate_2x2_state_feedback(A=a,B=b,K=k,x0=[.4,.5],disturbances=d,input_limit=.2,measurement_biases=bias)
    add('sensor_bias_changes_commands',biased,biased['sensor_bias_applied'] and biased['applied_commands']!=sim['applied_commands'],
        'A controller using biased observations differs from exact state-feedback design; the certificate does not transfer.')
    try:
        robust_invariant_box_2x2(A_intervals=[[(.3,.4),(-.03,.03)],[(-.02,.02),(.2,.3)]],
            B_intervals=[(.8,.9),(.1,.2)],state_feedback_K=[.1,.1],state_radii=[1,1],disturbance_radii=[.05,.05],
            actuator_limit=.25,full_state_available=False)
        refused=False
    except ControlInputError:refused=True
    add('state_not_available_refusal',{'refused':refused},refused,
        'Explicitly reject invocation when the physical state is only estimated; no state-feedback proof is inherited.')
    return {'schema':'atlas.control-invariance-v05-casebook/1','status':'passed' if all(x['passed'] for x in c) else 'failed',
        'count':len(c),'cases':c,'physical_measurements':False,'hardware_actuation':False,'independent_review':False}
