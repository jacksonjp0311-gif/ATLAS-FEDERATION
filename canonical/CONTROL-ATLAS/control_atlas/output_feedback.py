"""Bounded scalar output feedback and actuator dynamics, purely offline.

No hardware interfaces. Interval hulls are sufficient finite-horizon enclosures for
exactly stated LTI and bounded independent noise assumptions, not stochastic
confidence regions or certification of sensor integrity or physical safety.
"""
from __future__ import annotations
from math import isfinite
from .methods import ControlInputError, num


def _finite(name, value, *, nonnegative=False, positive=False):
    return num(value, name, nonnegative=nonnegative, positive=positive)


def _interval(lo, hi, label):
    a, b = _finite(label+' lower', lo), _finite(label+' upper', hi)
    if a > b:
        raise ControlInputError(label+' lower exceeds upper')
    return (a,b)


def _lin_interval(terms, offset=(0.0,0.0)):
    """Linear image of independent interval arguments; output is an enclosure."""
    low,high=offset
    for coefficient, (lo,hi) in terms:
        a,b=coefficient*lo,coefficient*hi
        low+=min(a,b)
        high+=max(a,b)
    if not isfinite(low) or not isfinite(high):
        raise ControlInputError('interval numerical overflow')
    return (low,high)


def _clip_interval(I, low, high):
    if low>high:raise ControlInputError('clip bounds reversed')
    return (max(low,min(high,I[0])),max(low,min(high,I[1])))


def scalar_observer_error_bound(*, plant_a, observer_gain, initial_error_radius,
                                process_disturbance_radius, measurement_noise_radius,
                                steps):
    """e[k+1]=(a-L)e[k]+w[k]-L v[k] for predictor-corrector ordering.

    y[k]=x[k]+v[k] and xhat[k+1]=a*xhat[k]+b*u[k]+L*(y[k]-xhat[k]).
    This assumes the SAME known applied u[k] enters predictor and plant. It does
    not cover unknown actuator state, delayed measurements, bias beyond V, or
    unbounded stochastic noise. Return finite-horizon error radius and, only
    when |a-L|<1, a stationary sufficient scalar bound.
    """
    a=_finite('plant_a',plant_a);L=_finite('observer_gain',observer_gain)
    e0=_finite('initial_error_radius',initial_error_radius,nonnegative=True)
    W=_finite('process_disturbance_radius',process_disturbance_radius,nonnegative=True)
    V=_finite('measurement_noise_radius',measurement_noise_radius,nonnegative=True)
    if type(steps)is not int or not 1<=steps<=256:
        raise ControlInputError('steps must be integer 1..256')
    gain=abs(a-L);forcing=W+abs(L)*V
    if not isfinite(gain) or not isfinite(forcing):raise ControlInputError('observer numerical overflow')
    bounds=[e0]
    for _ in range(steps):
        next_e=gain*bounds[-1]+forcing
        if not isfinite(next_e):raise ControlInputError('observer bound numerical overflow')
        bounds.append(next_e)
    limiting=forcing/(1-gain) if gain<1 else None
    return {'schema':'atlas.control-scalar-observer-error/1',
      'error_dynamics_gain':a-L,'magnitude_gain':gain,'error_radii':bounds,
      'stationary_sufficient_error_radius':limiting,
      'stationary_error_bound_available':gain<1,
      'conditional_model_bound':True,
      'model_assumptions':['Exact known plant a, gain L, same recorded applied actuator input for plant and observer',
        'Scalar discrete LTI, initial error radius and bounded additive process/sensor disturbances',
        'Measurement y[k] is timely, matched to x[k] and bounded by the declared noise radius'],
      'limitations':['No physical sensor fault isolation, unverified noise/bias guarantee or stochastic coverage claim',
        'A finite-horizon bound is not a control-invariant physical safety guarantee',
        'For |a-L|>=1 the function supplies finite-horizon bounds but no finite asymptotic certificate']}


def scalar_actuator_step(*,requested_input,previous_applied_input,max_abs_input,max_delta_per_step,response_fraction):
    """Magnitude clamp -> slew clamp -> first-order actuator response.

    applied_new = prev + alpha*(slewed_target-prev); 0 < alpha <=1.
    This is an authored discrete actuator model, not a device characterization.
    """
    req=_finite('requested_input',requested_input)
    previous=_finite('previous_applied_input',previous_applied_input)
    U=_finite('max_abs_input',max_abs_input,positive=True)
    delta=_finite('max_delta_per_step',max_delta_per_step,nonnegative=True)
    alpha=_finite('response_fraction',response_fraction,positive=True)
    if alpha>1:raise ControlInputError('response_fraction must be <= 1')
    if abs(previous)>U:raise ControlInputError('previous applied input outside declared actuator magnitude bounds')
    clipped=max(-U,min(U,req))
    slew_target=max(previous-delta,min(previous+delta,clipped))
    applied=(1-alpha)*previous+alpha*slew_target
    if not isfinite(applied):raise ControlInputError('actuator numerical overflow')
    return {'schema':'atlas.control-scalar-actuator/1','requested_input':req,
       'magnitude_clamped_target':clipped,'slew_limited_target':slew_target,
       'applied_input_next':applied,
       'command_magnitude_limited':clipped!=req,
       'command_slew_limited':slew_target!=clipped,
       'applied_within_magnitude_limit':abs(applied)<=U+1e-12,
       'applied_change_within_slew_limit':abs(applied-previous)<=delta+1e-12,
       'limitations':['This is a supplied scalar discrete actuator lag/rate model; it is not measured hardware dynamics',
         'No deadband, backlash, hysteresis, transport delay, switching logic or failure detection',
         'A software command bound is not a safety-rated interlock']}


def scalar_output_feedback_tube(*, plant_a, plant_b, feedback_k, observer_gain,
       estimated_initial_state,initial_state_error_radius, process_disturbance_radius,
       sensor_noise_radius,previous_applied_input, actuator_abs_limit,
       actuator_max_delta,actuator_response_fraction,state_abs_limit,steps):
    """Conservative finite-step interval enclosure with estimated-state controller.

    x[k+1] = a*x[k] + b*u_applied[k] + w[k]
    y[k] = x[k] + v[k]
    h[k+1] = (a-L)*h[k]+L*x[k]+b*u_applied[k]+L*v[k]
    cmd[k] = -K*h[k]
    u_applied[k+1] = (1-alpha)*u_applied[k] + alpha*clamp_rate(clamp_abs(cmd[k]))

    The plant uses u_applied[k], and the actuator's update supplies k+1.
    All intervals are sound *over-approximations*, not exact reachable sets;
    independent interval products overcount state-estimate correlation.
    Only checked steps and sampled instants are covered, not invariant time.
    """
    a=_finite('plant_a',plant_a);b=_finite('plant_b',plant_b)
    K=_finite('feedback_k',feedback_k);L=_finite('observer_gain',observer_gain)
    h0=_finite('estimated_initial_state',estimated_initial_state)
    E=_finite('initial_state_error_radius',initial_state_error_radius,nonnegative=True)
    W=_finite('process_disturbance_radius',process_disturbance_radius,nonnegative=True)
    V=_finite('sensor_noise_radius',sensor_noise_radius,nonnegative=True)
    u0=_finite('previous_applied_input',previous_applied_input)
    U=_finite('actuator_abs_limit',actuator_abs_limit,positive=True)
    D=_finite('actuator_max_delta',actuator_max_delta,nonnegative=True)
    alpha=_finite('actuator_response_fraction',actuator_response_fraction,positive=True)
    X=_finite('state_abs_limit',state_abs_limit,positive=True)
    if alpha>1:raise ControlInputError('actuator_response_fraction must be <= 1')
    if abs(u0)>U:raise ControlInputError('previous input exceeds declared hardware bound')
    if type(steps)is not int or not 1<=steps<=100:
        raise ControlInputError('steps must be integer in 1..100')
    xx=(h0-E,h0+E);hh=(h0,h0);uu=(u0,u0)
    timeline=[];all_sampled_safe=True
    for k in range(steps+1):
        bounded=max(abs(xx[0]),abs(xx[1]))<=X
        all_sampled_safe=all_sampled_safe and bounded
        entry={'sample':k,'physical_state_interval':list(xx),'observer_estimate_interval':list(hh),
            'applied_actuator_interval':list(uu),'sampled_state_within_declared_limit':bounded}
        if k==steps:
            timeline.append(entry)
            break
        # Requested controller command; clipped to declared +/-U.
        requested=_lin_interval([(-K,hh)])
        mag=_clip_interval(requested,-U,U)
        # Slew target = clamp(mag, u_previous-D, u_previous+D). The clamp
        # is monotone in both args; interval endpoint hulls are valid.
        low_target=max(uu[0]-D,min(uu[0]+D,mag[0]))
        high_target=max(uu[1]-D,min(uu[1]+D,mag[1]))
        target=(low_target,high_target)
        unext=_lin_interval([((1-alpha),uu),(alpha,target)])
        unext=_clip_interval(unext,-U,U)  # bound guaranteed since prev and target within limits
        nx=_lin_interval([(a,xx),(b,uu)],(-W,W))
        nh=_lin_interval([((a-L),hh),(L,xx),(b,uu)],(-abs(L)*V,abs(L)*V))
        entry['requested_command_interval']=list(requested)
        entry['magnitude_clamped_command_interval']=list(mag)
        entry['slew_target_interval']=list(target)
        timeline.append(entry)
        xx,hh,uu=nx,nh,unext
    return {'schema':'atlas.control-output-feedback-tube/1','result':'finite_horizon_interval_enclosure',
      'timeline':timeline,'steps':steps,'all_sampled_states_within_limit_under_assumed_model':all_sampled_safe,
      'applied_inputs_within_assumed_magnitude_rate_envelope':True,
      'origin':'derived_scalar_plant_estimator_actuator_interval_arithmetic',
      'limits':['Not an invariant certificate; nothing guaranteed after the checked finite horizon or between sampling instants',
        'This conservative interval propagation ignores correlations and may report a false infeasibility',
        'No data establish the assumed plant, sensor bias/noise, disturbance, actuator rate or response parameters',
        'Observer uses the known applied input and current measurement; no timing jitter, stale packets or separate actuator observation latency',
        'Mathematical bound only; no real actuator, interlock, qualified safety or physical deployment']}


def scalar_measurement_consistency(*,measured_output,estimated_state,estimated_state_error_radius,
                                  sensor_noise_radius):
    """Only checks whether a sensor reading is compatible with assumed bounds.

    y=x+v, x in [estimated-E,estimated+E], |v|<=V. A reading outside
    interval is a model/measurement contradiction, not a sensor diagnosis.
    """
    y=_finite('measured_output',measured_output)
    h=_finite('estimated_state',estimated_state)
    e=_finite('estimated_state_error_radius',estimated_state_error_radius,nonnegative=True)
    v=_finite('sensor_noise_radius',sensor_noise_radius,nonnegative=True)
    lo=h-e-v;hi=h+e+v
    consistent=lo<=y<=hi
    return {'schema':'atlas.control-measurement-consistency/1',
      'expected_measurement_interval':[lo,hi],'reading':y,'consistent_given_bounds':consistent,
      'distance_outside_interval':max(lo-y,0.0,y-hi),
      'status':'consistent_under_assumptions' if consistent else 'inconsistent_not_root_cause_isolated',
      'not_identified':['sensor fault','plant-model error','unmodeled disturbance','time synchronization','process change'],
      'limitations':['Bound consistency does not imply trustworthy sensor or known plant',
        'Inconsistency alone does not identify which physical component failed',
        'No alarms, actuator commands, hardware inspection or diagnosis performed']}
