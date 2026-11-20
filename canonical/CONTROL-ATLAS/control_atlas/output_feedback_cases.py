"""Twelve authored uncertainty/actuator/fault counterexamples, no field observations."""
from .output_feedback import (scalar_observer_error_bound, scalar_actuator_step,
                              scalar_output_feedback_tube, scalar_measurement_consistency)
from .methods import ControlInputError


def casebook():
    cases=[]
    def add(key,result,ok,point):
        cases.append({'case':key,'passed':bool(ok),'model_output':result,
              'origin':'authored_synthetic_mathematical_example','reason':point})

    e=scalar_observer_error_bound(plant_a=.8,observer_gain=.6,initial_error_radius=.1,
      process_disturbance_radius=.02,measurement_noise_radius=.01,steps=12)
    add('bounded_observer_with_stationary_error',e,e['stationary_error_bound_available']
      and abs(e['stationary_sufficient_error_radius']-.0325)<1e-12,
      'Under a known scalar model, disturbances/noise leave nonzero error even when observer dynamics are stable.')
    unstable=scalar_observer_error_bound(plant_a=1.4,observer_gain=.2,initial_error_radius=.1,
      process_disturbance_radius=.02,measurement_noise_radius=.01,steps=10)
    add('observer_does_not_converge',unstable,unstable['stationary_sufficient_error_radius'] is None,
      'An observer that cannot damp the model error has no finite stationary certificate.')

    actuator=scalar_actuator_step(requested_input=10,previous_applied_input=0,
      max_abs_input=1,max_delta_per_step=.2,response_fraction=.5)
    add('saturation_slew_and_lag_distinct',actuator,
      actuator['magnitude_clamped_target']==1 and actuator['slew_limited_target']==.2
      and abs(actuator['applied_input_next']-.1)<1e-12,
      'Requested 10, allowed target 1, rate-clamped target 0.2, lagged applied 0.1; controller intention is not plant input.')
    parked=scalar_actuator_step(requested_input=-.6,previous_applied_input=.1,
      max_abs_input=1,max_delta_per_step=0,response_fraction=.8)
    add('rate_zero_prevents_motion',parked,abs(parked['applied_input_next']-.1)<1e-12,
      'Even if the control command changes, an actuator with zero allowed step change does not follow it.')

    params={'plant_a':.6,'plant_b':.2,'feedback_k':.4,'observer_gain':.55,
       'estimated_initial_state':.1,'initial_state_error_radius':.05,
       'process_disturbance_radius':.01,'sensor_noise_radius':.01,
       'previous_applied_input':0,'actuator_abs_limit':.4,'actuator_max_delta':.1,
       'actuator_response_fraction':.6,'state_abs_limit':1.0,'steps':12}
    safe=scalar_output_feedback_tube(**params)
    add('finite_horizon_tube_with_rate_limit',{'end':safe['timeline'][-1],
      'samples':len(safe['timeline']),'all_checked_safe':safe['all_sampled_states_within_limit_under_assumed_model']},
      safe['all_sampled_states_within_limit_under_assumed_model'] and len(safe['timeline'])==13,
      'A sampled finite-horizon interval enclosure, not a universal invariant proof or certified plant.')
    unsafe=scalar_output_feedback_tube(**{**params,'state_abs_limit':.04})
    add('state_limit_candidate_not_satisfied',{'end':unsafe['timeline'][-1],
       'all_checked_safe':unsafe['all_sampled_states_within_limit_under_assumed_model']},
       not unsafe['all_sampled_states_within_limit_under_assumed_model'],
       'Declared state bound is violated by the interval enclosure; proof fails, physical failure is not inferred.')
    slow=scalar_output_feedback_tube(**{**params,'actuator_response_fraction':.01})
    add('lag_changes_reachable_tube',{'lagged_end':slow['timeline'][-1]['physical_state_interval'],
      'baseline_end':safe['timeline'][-1]['physical_state_interval']},
      slow['timeline'][-1]['physical_state_interval']!=safe['timeline'][-1]['physical_state_interval'],
      'Actuator speed matters to the reachable state set; a nominal command trajectory is insufficient.')

    reading=scalar_measurement_consistency(measured_output=.13,estimated_state=.1,
      estimated_state_error_radius=.04,sensor_noise_radius=.02)
    add('measurement_in_bounds',reading,reading['consistent_given_bounds'],
      'Bound agreement is not sensor authentication.')
    outside=scalar_measurement_consistency(measured_output=.3,estimated_state=.1,
      estimated_state_error_radius=.04,sensor_noise_radius=.02)
    add('measurement_contradiction_not_fault_isolation',outside,
      outside['status']=='inconsistent_not_root_cause_isolated',
      'An out-of-bound sensor reading can arise from multiple physical causes and does not isolate a failed sensor.')
    try:
      scalar_observer_error_bound(plant_a=.8,observer_gain=.6,initial_error_radius=.1,
        process_disturbance_radius=.02,measurement_noise_radius=-.01,steps=10)
      rejected=False
    except ControlInputError:rejected=True
    add('negative_sensor_noise_refused',{'rejected':rejected},rejected,
      'Invalid uncertainty radius is rejected rather than recoded as zero.')
    try:
      scalar_actuator_step(requested_input=2,previous_applied_input=2,
         max_abs_input=1,max_delta_per_step=.2,response_fraction=.8)
      rejected=False
    except ControlInputError:rejected=True
    add('initial_actuator_limit_refused',{'rejected':rejected},rejected,
      "An initial applied actuator state outside its declared bound voids the model's stated constraint premise.")
    try:
      scalar_output_feedback_tube(**{**params,'steps':101})
      rejected=False
    except ControlInputError:rejected=True
    add('unbounded_horizon_request_refused',{'rejected':rejected},rejected,
      'No extrapolation from a bounded finite horizon to all future time.')
    return {'schema':'atlas.control-output-feedback-v06-casebook/1',
      'result':'passed' if all(x['passed'] for x in cases) else 'failed','count':len(cases),
      'cases':cases,'origin':'authored_synthetic_models','real_hardware_tests':0,
      'independent_human_review':False,'actual_sensor_root_cause_diagnosis':False}
