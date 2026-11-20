"""Control Atlas 0.3.0: bounded stability, robustness and monitoring calculations.

Reference arithmetic ONLY. No drivers, networking, hardware or automatic actuation.
All stability claims are conditional on an exactly specified mathematical model.
"""
from __future__ import annotations
from cmath import sqrt as csqrt
from math import atan2, degrees, hypot, isfinite, sqrt, pi
from .methods import ControlInputError, num


def robust_scalar_feedback_interval(a_bounds, b_bounds, k):
    """Exact robust pole bound over *independent* scalar coefficient intervals.

    x[k+1]=a*x[k]+b*u[k], u[k]=-k*x[k]. For a,b in rectangles,
    p=a-b*k is affine and worst |p| is at a vertex. No delays/saturation.
    """
    def iv(bound,name):
        if not isinstance(bound,(tuple,list)) or len(bound)!=2:
            raise ControlInputError(f'{name} must be a two-element interval')
        lo,hi=[num(v,name) for v in bound]
        if lo>hi:raise ControlInputError(f'{name} endpoints not ordered')
        return lo,hi
    aa=iv(a_bounds,'a');bb=iv(b_bounds,'b');K=num(k,'state_feedback_k')
    vertices=[{'a':a,'b':b,'pole':a-b*K} for a in aa for b in bb]
    for v in vertices:
        if not isfinite(v['pole']):raise ControlInputError('nonfinite closed-loop pole')
    worst=max(vertices,key=lambda v:abs(v['pole']))
    return {'model':'scalar_discrete_state_feedback_interval_box',
      'worst_case_abs_pole':abs(worst['pole']), 'worst_case_vertex':worst,
      'every_vertex':vertices, 'strict_uniform_asymptotic_stability_within_assumed_model':abs(worst['pole'])<1,
      'limits':['Exact for specified independent scalar a,b rectangle, fixed k, LTI discrete plant',
                'No unmodeled delays, actuator saturation, hysteresis, nonlinear states or changes outside the coefficient intervals',
                'Input parameter bounds are supplied rather than inferred or experimentally validated',
                'Failure to meet this criterion is instability for at least one included scalar model, not evidence of actual equipment instability']}


def delay_one_sample_scalar(a,b,k):
    """u[k] = -k*x[k-1]; augmented state characteristic z^2-a*z+b*k.

    Nominal zero-delay pole a-b*k. This shows why nominal stability need not
    survive delay; no robust/distributed delay guarantees.
    """
    A=num(a,'a');B=num(b,'b');K=num(k,'k')
    zero=A-B*K
    product=B*K
    discr=A*A-4*product
    if not isfinite(discr):raise ControlInputError('discriminant overflow')
    z=csqrt(discr)
    roots=((A+z)/2,(A-z)/2)
    spectral=max(abs(x) for x in roots)
    if not isfinite(spectral):raise ControlInputError('nonfinite spectral radius')
    return {'zero_delay_pole':zero,'zero_delay_stable':abs(zero)<1,
            'one_sample_delay_roots':[{'real':x.real,'imag':x.imag} for x in roots],
            'one_sample_delay_spectral_radius':spectral,'one_sample_delayed_model_stable':spectral<1,
            'model':'scalar_discrete_exact_one_sample_state_feedback_delay',
            'limits':['One EXACT sample of measurement-to-actuation feedback delay, no other delays',
                     'Constant gains and perfect state measurement, no saturation or disturbance',
                     'A simulated unstable delayed pole is not a prediction that any real machine will fail']}


def discrete_lyapunov_2x2(A,P,relative_tolerance=1e-10):
    """Check if a user-supplied P proves strict quadratic decay for 2x2 x+=Ax.

    Conditions: symmetric positive definite P, Q=P-A^T P A positive definite.
    A failed candidate does NOT prove instability. Numeric strictness threshold
    is heuristic, not a formal verified interval-arithmetic certificate.
    """
    def mat(m,label):
        if not isinstance(m,(tuple,list)) or len(m)!=2 or any(not isinstance(z,(tuple,list)) or len(z)!=2 for z in m):
            raise ControlInputError(label+' must be 2x2')
        return [[num(v,label) for v in r] for r in m]
    a=mat(A,'A');p=mat(P,'P');tol=num(relative_tolerance,'relative_tolerance',positive=True)
    if tol>=1e-2:raise ControlInputError('relative tolerance too large')
    if abs(p[0][1]-p[1][0])>tol*max(1,*(abs(z) for row in p for z in row)):
        raise ControlInputError('P must be symmetric')
    p=[[p[0][0],(p[0][1]+p[1][0])/2],[(p[0][1]+p[1][0])/2,p[1][1]]]
    ap=[[p[i][0]*a[0][j]+p[i][1]*a[1][j] for j in range(2)] for i in range(2)]
    apa=[[a[0][i]*ap[0][j]+a[1][i]*ap[1][j] for j in range(2)] for i in range(2)]
    q=[[p[i][j]-apa[i][j] for j in range(2)] for i in range(2)]
    q=[[q[0][0],(q[0][1]+q[1][0])/2],[(q[0][1]+q[1][0])/2,q[1][1]]]
    def eig(m):
        av,bv,dv=m[0][0],m[0][1],m[1][1]
        delta=hypot(av-dv,2*bv)
        return ((av+dv-delta)/2,(av+dv+delta)/2)
    pe=eig(p);qe=eig(q)
    vals=[*pe,*qe]
    if not all(isfinite(z) for z in vals):raise ControlInputError('nonfinite eigenvalues')
    scale=max(1,*(abs(z) for row in p for z in row),*(abs(z) for row in q for z in row))
    cert=pe[0]>tol*scale and qe[0]>tol*scale
    return {'P_eigenvalues':list(pe),'Q':q,'Q_eigenvalues':list(qe),'numerically_positive_definite_P_and_Q':cert,
     'interpretation':'sufficient_nominal_2x2_quadratic_Lyapunov_candidate' if cert else 'candidate_not_certified',
     'limits':['Applies to exact autonomous real 2x2 discrete-time LTI dynamics, not a complete feedback loop with constraints',
               'Failed P candidate does not imply plant instability: a different P may work',
               'Floating-point eigentest is not formal interval proof or physical robustness validation']}


def first_order_proportional_sensitivity(plant_gain, plant_tau_seconds, proportional_gain, frequency_rad_s):
    """S=1/(1+L), T=L/(1+L), L=Kp*kg/(1+j*w*tau)."""
    kg=num(plant_gain,'plant_gain');tau=num(plant_tau_seconds,'tau',positive=True)
    k=num(proportional_gain,'proportional_gain');w=num(frequency_rad_s,'frequency_rad_s',nonnegative=True)
    L=k*kg/complex(1,w*tau)
    if abs(1+L)<1e-13:raise ControlInputError('singular sensitivity 1+L near zero')
    S=1/(1+L);T=L/(1+L)
    return {'open_loop_magnitude':abs(L),'open_loop_phase_degrees':degrees(atan2(L.imag,L.real)),
       'sensitivity_magnitude':abs(S),'complementary_sensitivity_magnitude':abs(T),
       'sensitivity_complex':{'real':S.real,'imag':S.imag},
       'complementary_complex':{'real':T.real,'imag':T.imag},
       'S_plus_T_identity_residual':abs(S+T-1),
       'limits':['Analytic frequency response of exactly one stable first-order plant with proportional feedback',
                 'Individual frequency response is not a full gain/phase/disk margin, robust stability test, or noisy closed-loop experiment',
                 'Actuator limits, delay, sensor filtering, nonlinearities and additional dynamics absent']}


def residual_lag1_diagnostic(residuals):
    """Descriptive residual mean/RMS and lag-one centered correlation.

    No p-value, significant-whiteness claim or system identification validity.
    """
    if not isinstance(residuals,(list,tuple)) or not 5<=len(residuals)<=30000:
        raise ControlInputError('5..30000 residuals required')
    data=[num(v,'residual') for v in residuals]
    mean=sum(data)/len(data)
    centered=[v-mean for v in data]
    den=sum(v*v for v in centered)
    if den<=1e-22:raise ControlInputError('near-zero centered residual energy: correlation undefined')
    ac=sum(centered[i]*centered[i+1] for i in range(len(centered)-1))/den
    rms=sqrt(sum(v*v for v in data)/len(data))
    return {'sample_count':len(data),'mean':mean,'rms':rms,'descriptive_lag1_correlation':ac,
      'data_origin':'caller_supplied_residual_series',
      'limits':['No test of independence, white noise, normality, or statistical significance',
                'Lag one alone can miss drift, nonlinear dynamics, hidden delays and correlated noise',
                'A perfectly fitted training record can still be biased or useless for prediction']}


def watchdog_policy_trace(samples, max_age_s, maximum_abs_innovation, safe_output=0):
    """Offline illustrative command gate; NEVER talks to devices.

    Each dict has now_s, measurement_timestamp_s, measurement_valid,
    innovation, requested_output. A stale/invalid/implausible sensor sample
    yields the supplied SAFE OUTPUT; the safe output itself isn't certified.
    """
    age=num(max_age_s,'max_age_s',nonnegative=True)
    threshold=num(maximum_abs_innovation,'maximum_abs_innovation',nonnegative=True)
    safe=num(safe_output,'safe_output')
    if not isinstance(samples,list) or not 1<=len(samples)<=10000:
        raise ControlInputError('1..10000 samples required')
    keys={'now_s','measurement_timestamp_s','measurement_valid','innovation','requested_output'}
    trace=[];last_time=None
    for i,item in enumerate(samples):
        if not isinstance(item,dict) or set(item)!=keys:
            raise ControlInputError('each sample requires exact timestamp, validity, innovation and request fields')
        now=num(item['now_s'],'now_s');stamp=num(item['measurement_timestamp_s'],'measurement_timestamp_s')
        valid=item['measurement_valid']
        if type(valid) is not bool:raise ControlInputError('measurement_valid must be Boolean')
        diff=num(item['innovation'],'innovation');request=num(item['requested_output'],'requested_output')
        if last_time is not None and now<=last_time:raise ControlInputError('strictly increasing sampled clock required')
        if stamp>now:raise ControlInputError('future-dated sensor timestamp refused')
        stale=now-stamp>age
        reasons=[]
        if not valid:reasons.append('sensor_marked_invalid')
        if stale:reasons.append('stale_measurement')
        if abs(diff)>threshold:reasons.append('innovation_exceeds_declared_threshold')
        trace.append({'sample':i,'output':safe if reasons else request,
                      'accepted_request':not bool(reasons),'refusal_reasons':reasons,
                      'age_s':now-stamp})
        last_time=now
    return {'trace':trace,'accepted_count':sum(x['accepted_request'] for x in trace),
      'blocked_count':sum(not x['accepted_request'] for x in trace),
      'limits':['Illustrative supervisor calculation only: no physical sensors, actuators, interlocks or safety-rated logic',
               'The safe_output setting is caller-supplied and NOT verified safe for a physical process',
               'A plausible sensor innovation is not independent evidence the measurement is physically correct',
               'Policy does not certify timing deadlines, emergency stop, fault detection coverage or hardware fail-safe behavior']}
