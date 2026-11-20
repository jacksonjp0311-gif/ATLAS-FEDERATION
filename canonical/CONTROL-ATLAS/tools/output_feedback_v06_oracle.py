"""Independent NumPy/SciPy checks for authored scalar output-feedback bounds.

Models are stipulated. No sensor experiment, measured input limits, real PLC,
independent scientific review, or future-time safety certification is inferred.
"""
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from scipy.optimize import linprog
from control_atlas.output_feedback import (scalar_observer_error_bound,
    scalar_actuator_step,scalar_output_feedback_tube,scalar_measurement_consistency)

rng=np.random.default_rng(601126)
counts={'observer_recurrence':0,'actuator_numpy_clip':0,'tube_trajectory_containment':0,
        'measurement_bound':0,'affine_box_scipy_lp':0}
max_error=0.0

def check_close(a,b,k,atol=1e-9):
    global max_error
    delta=abs(float(a)-float(b));max_error=max(max_error,delta)
    if delta>atol:raise AssertionError(f'{k}: delta {delta} for {a} vs {b}')
    counts[k]+=1

# Independent closed-form geometric series, including g=1.
for _ in range(300):
    a=float(rng.uniform(-1.4,1.4));L=float(rng.uniform(-1,1))
    E=float(rng.uniform(0,.3));W=float(rng.uniform(0,.08));V=float(rng.uniform(0,.05));n=int(rng.integers(1,20))
    r=scalar_observer_error_bound(plant_a=a,observer_gain=L,initial_error_radius=E,
      process_disturbance_radius=W,measurement_noise_radius=V,steps=n)
    g=abs(a-L);q=W+abs(L)*V
    ref=g**n*E+q*float(np.sum(np.power(g,np.arange(n))))
    check_close(r['error_radii'][-1],ref,'observer_recurrence')

for _ in range(400):
    U=float(rng.uniform(.1,8));p=float(rng.uniform(-U,U));req=float(rng.uniform(-10,10));delta=float(rng.uniform(0,4));alpha=float(rng.uniform(.001,1))
    r=scalar_actuator_step(requested_input=req,previous_applied_input=p,max_abs_input=U,
                           max_delta_per_step=delta,response_fraction=alpha)
    cmd=float(np.clip(req,-U,U));slew=float(np.clip(cmd,p-delta,p+delta));applied=p+alpha*(slew-p)
    check_close(r['applied_input_next'],applied,'actuator_numpy_clip')

for _ in range(400):
    h=float(rng.uniform(-1,1));e=float(rng.uniform(0,.3));v=float(rng.uniform(0,.15));y=float(rng.uniform(-2,2))
    o=scalar_measurement_consistency(measured_output=y,estimated_state=h,
      estimated_state_error_radius=e,sensor_noise_radius=v)
    lo=h-e-v;hi=h+e+v
    check_close(o['distance_outside_interval'],float(np.maximum.reduce([lo-y,0,y-hi])),'measurement_bound')

# Full augmented Monte Carlo simulation with an independent implementation of
# command magnitudes, rate limits, actuator lag, plant and observer.
for _ in range(100):
    a=float(rng.uniform(.1,.95));b=float(rng.uniform(.02,.8))
    K=float(rng.uniform(.05,1.5));L=float(rng.uniform(.05,1.0));E=float(rng.uniform(.001,.12))
    W=float(rng.uniform(.001,.04));V=float(rng.uniform(.001,.025))
    h0=float(rng.uniform(-.2,.2));U=float(rng.uniform(.2,1.5));D=float(rng.uniform(.01,.3));alpha=float(rng.uniform(.05,1))
    u0=float(rng.uniform(-U,U));steps=15
    p=dict(plant_a=a,plant_b=b,feedback_k=K,observer_gain=L,estimated_initial_state=h0,
      initial_state_error_radius=E,process_disturbance_radius=W,sensor_noise_radius=V,
      previous_applied_input=u0,actuator_abs_limit=U,actuator_max_delta=D,
      actuator_response_fraction=alpha,state_abs_limit=10,steps=steps)
    tube=scalar_output_feedback_tube(**p)['timeline']
    for rep in range(12):
        x=h0+float(rng.uniform(-E,E));h=h0;u=u0
        for k in range(steps+1):
            for truth,lo,hi in [(x,*tube[k]['physical_state_interval']),
                                (h,*tube[k]['observer_estimate_interval']),
                                (u,*tube[k]['applied_actuator_interval'])]:
                if not lo-1e-10<=truth<=hi+1e-10:
                    raise AssertionError(('tube escape',rep,k,truth,lo,hi,p))
                counts['tube_trajectory_containment']+=1
            if k==steps:break
            w=float(rng.uniform(-W,W));v=float(rng.uniform(-V,V))
            # Actual applied actuator u enters current plant and observer.
            raw=-K*h
            mag=float(np.clip(raw,-U,U))
            cmd=float(np.clip(mag,u-D,u+D))
            unew=(1-alpha)*u+alpha*cmd
            xnew=a*x+b*u+w
            hnew=(a-L)*h +L*x +b*u+L*v
            x,h,u=xnew,hnew,unew

# Independently optimize a generic 2-state affine next-state coordinate over an
# interval box via SciPy linear programming, not the model's own interval helper.
for _ in range(200):
    a=float(rng.uniform(-1,1));b=float(rng.uniform(-1,1));c=float(rng.uniform(-1,1));v=float(rng.uniform(-1,.5))
    lo=np.array([float(rng.uniform(-1,0)),float(rng.uniform(-1,0)),float(rng.uniform(-1,0))])
    hi=lo+rng.uniform(.01,1.5,size=3)
    target=(np.array([a,b,c])*np.where(np.array([a,b,c])>=0,hi,lo)).sum()+v
    result=linprog(-np.array([a,b,c]),bounds=list(zip(lo,hi)),method='highs')
    if not result.success:raise RuntimeError('SciPy LP oracle failed')
    check_close(target,-float(result.fun)+v,'affine_box_scipy_lp',atol=1e-8)

report={'schema':'atlas.control-output-feedback-oracle/1','result':'passed',
 'seed':601126,'numpy_version':np.__version__,'scipy_version':__import__('scipy').__version__,
 'checks':counts,'total_comparisons':sum(counts.values()),'largest_numeric_difference':max_error,
 'validation_scope':'separately_computed_author_synthetic_models_and_random_trajectories',
 'not_verified':['physical actuator model','actual sensor noise envelope','measurement time alignment',
                 'engineering safety','observer integrity under faults','hardware system','unbounded-time robustness']}
print(json.dumps(report,indent=2))
