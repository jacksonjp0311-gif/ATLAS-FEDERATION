"""Bounded, standard-library control theory calculations for declared models.

Outputs are model calculations, not real hardware control, safety proof, stability
of unknown plants, or agent action authorizations. All inputs are supplied.
"""
from __future__ import annotations
from math import exp, isfinite, atan2, sqrt, pi, log

class ControlInputError(ValueError):
    pass

def _n(name, v, positive=False, nonnegative=False):
    if isinstance(v, bool) or not isinstance(v,(int,float)) or not isfinite(v):
        raise ControlInputError(f'{name} must be a finite numeric scalar')
    x=float(v)
    if positive and x<=0: raise ControlInputError(f'{name} must be positive')
    if nonnegative and x<0: raise ControlInputError(f'{name} must be nonnegative')
    return x

def first_order_response(*, initial:float, final:float, time_s:float, tau_s:float):
    x0=_n('initial',initial);xf=_n('final',final)
    t=_n('time_s',time_s,nonnegative=True);tau=_n('tau_s',tau_s,positive=True)
    x=xf+(x0-xf)*exp(-t/tau)
    return {'state':x,'time_s':t,'model':'single continuous stable first-order pole',
        'limitations':['No dead time, saturation or external disturbance','Not an identified plant or uncertainty bound']}

def zoh_first_order(*, gain:float, tau_s:float, sample_s:float):
    g=_n('gain',gain);tau=_n('tau_s',tau_s,positive=True);h=_n('sample_s',sample_s,positive=True)
    a=exp(-h/tau);b=g*(1-a)
    return {'a':a,'b':b,'sample_s':h,'state_equation':'y[k+1]=a*y[k]+b*u[k]',
       'limitations':['Exact for this first-order continuous model with held constant input between samples',
                     'Does not capture actuator delay, quantization or unmodeled modes']}

def scalar_discrete_stability(*, a:float):
    pole=_n('a',a)
    return {'pole':pole,'asymptotically_stable':abs(pole)<1,'marginal_boundary':abs(pole)==1,
        'interpretation':'asymptotic zero-input stability of exactly x[k+1]=a*x[k] only'}

def state_rank_2x2(*, A, B, C, tol:float=1e-10):
    # Kalman rank criterion, restricted to n=2 with one input and one output.
    if not isinstance(A,(list,tuple)) or len(A)!=2 or any(not isinstance(row,(list,tuple)) or len(row)!=2 for row in A):
        raise ControlInputError('A must be 2x2')
    a=[[ _n(f'A{i}{j}',A[i][j]) for j in range(2)] for i in range(2)]
    if not isinstance(B,(list,tuple)) or len(B)!=2 or not isinstance(C,(list,tuple)) or len(C)!=2:
        raise ControlInputError('B and C must be two-element vectors')
    b=[_n('B',x) for x in B];c=[_n('C',x) for x in C]
    tol=_n('tol',tol,positive=True)
    AB=[sum(a[i][j]*b[j] for j in range(2)) for i in range(2)]
    CA=[sum(c[j]*a[j][i] for j in range(2)) for i in range(2)]
    controllability_det=b[0]*AB[1]-b[1]*AB[0]
    observability_det=c[0]*CA[1]-c[1]*CA[0]
    return {'controllability_det':controllability_det,'observability_det':observability_det,
       'controllable_at_absolute_det_tol':abs(controllability_det)>tol,
       'observable_at_absolute_det_tol':abs(observability_det)>tol,
       'limitations':['Only dimension-two, single-input single-output LTI rank calculation',
                      'Absolute determinant tolerance is scale/units dependent, not a robust numerical rank criterion',
                      'Declared matrices are not identified from real plant observations']}

def pi_first_order_simulation(*, kp:float, ki:float, plant_gain:float, tau_s:float,
       sample_s:float, setpoints:list, u_min:float, u_max:float, antiwindup:str='clamp', y0:float=0):
    kp=_n('kp',kp,nonnegative=True);ki=_n('ki',ki,nonnegative=True)
    g=_n('plant_gain',plant_gain);tau=_n('tau_s',tau_s,positive=True);dt=_n('sample_s',sample_s,positive=True)
    lo=_n('u_min',u_min);hi=_n('u_max',u_max)
    if lo>=hi:raise ControlInputError('u_min < u_max required')
    if antiwindup not in ('clamp','none'):raise ControlInputError('antiwindup must be clamp or none')
    if not isinstance(setpoints,list) or not 1<=len(setpoints)<=10000:raise ControlInputError('setpoints length must be 1..10000')
    refs=[_n('setpoint',x) for x in setpoints]
    y=_n('y0',y0);integrator=0.;data=[];a=exp(-dt/tau);b=g*(1-a);abs_error=0.
    for i,ref in enumerate(refs):
        error=ref-y
        proposed=kp*error+integrator
        u=max(lo,min(hi,proposed))
        saturating=(u!=proposed)
        # Conditional integration: stop integration only if error would drive
        # output still farther into the active saturated rail.
        pushing=(proposed>hi and error>0) or (proposed<lo and error<0)
        if not (antiwindup=='clamp' and pushing):
            integrator+=ki*dt*error
        y=a*y+b*u
        if not all(map(isfinite,(integrator,y))):raise ControlInputError('simulation overflow; model inappropriate')
        abs_error+=abs(error)*dt
        data.append({'step':i,'reference':ref,'error':error,'actuator':u,
                     'output_after_step':y,'saturated':saturating,'integrator_after_step':integrator})
    return {'result':'synthetic_simulation','output_final':y,'integrator_final':integrator,
      'integral_absolute_error':abs_error,'saturated_steps':sum(p['saturated'] for p in data),'trace':data,
      'model':{'a':a,'b':b,'antiwindup':antiwindup,'controller':'PI with explicit output limits'},
      'limitations':['Plant and controller are declared synthetic scalars, not identified equipment',
                     'Clamping implementation is one discretized convention and not a proof of closed-loop stability',
                     'No delay, measurement noise, actuator slew, hidden states or safety interlocks']}

def scalar_kalman(*, a:float, c:float, process_variance:float, measurement_variance:float,
                  initial_estimate:float, initial_variance:float, measurements:list):
    a=_n('a',a);c=_n('c',c)
    q=_n('process_variance',process_variance,nonnegative=True)
    r=_n('measurement_variance',measurement_variance,positive=True)
    x=_n('initial_estimate',initial_estimate)
    p=_n('initial_variance',initial_variance,nonnegative=True)
    if not isinstance(measurements,list) or not 1<=len(measurements)<=10000:
        raise ControlInputError('measurements length must be 1..10000')
    trace=[]
    for i,v in enumerate(measurements):
        z=_n('measurement',v)
        xp=a*x;pp=a*a*p+q;s=c*c*pp+r
        if s<=0 or not isfinite(s):raise ControlInputError('innovation variance invalid')
        k=pp*c/s
        x=xp+k*(z-c*xp)
        # Joseph covariance formula protects nonnegativity in this scalar case.
        p=(1-k*c)**2*pp+k*k*r
        if not all(map(isfinite,(x,p))):raise ControlInputError('overflow in filter')
        trace.append({'step':i,'estimate':x,'posterior_variance':p,'gain':k,'innovation':z-c*xp})
    return {'result':'stipulated_linear_gaussian_filter','final_estimate':x,'final_variance':p,'trace':trace,
        'limitations':['Input covariance and system parameters are supplied, not estimated or validated',
                       'No control input, non-Gaussian noise, correlated errors or unknown-bias model',
                       'A small variance is conditional on covariance assumptions, not proof of accuracy']}

def scalar_finite_lqr(*, a:float, b:float, q:float, r:float, terminal_q:float,
                      horizon:int, x0:float):
    a=_n('a',a);b=_n('b',b);q=_n('q',q,nonnegative=True);r=_n('r',r,positive=True)
    qf=_n('terminal_q',terminal_q,nonnegative=True);x=_n('x0',x0)
    if type(horizon)!=int or not 1<=horizon<=10000:raise ControlInputError('horizon must be integer 1..10000')
    S=[0.]*(horizon+1);K=[0.]*horizon;S[-1]=qf
    for i in reversed(range(horizon)):
        sn=S[i+1];den=r+b*b*sn
        K[i]=b*sn*a/den
        S[i]=q+a*a*sn-a*b*sn*K[i]
        if not all(map(isfinite,(K[i],S[i]))) or S[i]<-1e-8:raise ControlInputError('invalid Riccati recursion')
    cost=0.;trace=[]
    for i in range(horizon):
        u=-K[i]*x;cost+=q*x*x+r*u*u
        next_x=a*x+b*u
        trace.append({'step':i,'state':x,'action':u,'gain':K[i]})
        x=next_x
    cost+=qf*x*x
    optimal_cost=S[0]*_n('x0',x0)**2
    if abs(cost-optimal_cost)>1e-8*max(1,abs(cost)):
        raise ControlInputError('Riccati and rollout costs disagree')
    return {'result':'unconstrained_scalar_finite_horizon_LQR','gains':K,'riccati':S,
        'optimal_cost':optimal_cost,'rollout_cost':cost,'final_state':x,'trace':trace,
        'limitations':['Unconstrained quadratic regulator, not safe under actuator clipping or state constraints',
                       'Model coefficients and Q/R choice supplied by caller; no identification or real plant validation',
                       'No nonlinearities, delays, noise, saturation or infinite-horizon guarantee']}

def nyquist_information(*, sample_hz:float, max_signal_frequency_hz:float):
    fs=_n('sample_hz',sample_hz,positive=True)
    band=_n('max_signal_frequency_hz',max_signal_frequency_hz,nonnegative=True)
    return {'ideal_bandlimit_condition_satisfied':fs>2*band,'nyquist_limit_hz':fs/2,
       'limitations':['Bandlimited and ideal anti-alias assumptions must be justified',
                      'Nyquist condition alone does NOT establish control-loop sampling adequacy, stability or latency requirements']}

def small_gain_sufficient(*, forward_norm_bound:float, feedback_norm_bound:float):
    a=_n('forward_norm_bound',forward_norm_bound,nonnegative=True)
    b=_n('feedback_norm_bound',feedback_norm_bound,nonnegative=True)
    product=a*b
    if not isfinite(product):raise ControlInputError('product overflow: norm bounds too large')
    return {'norm_bound_product':product,'strict_small_gain_condition':product<1,
       'result':'sufficient_condition_only_under_assumed_stable_operator_norms',
       'limitations':['Operator bounds and individual loop stability are supplied, not measured',
                      'Failure of sufficient bound does not prove an actual loop unstable',
                      'Nonlinear/time-varying/uncertain systems require additional proof and conditions']}
