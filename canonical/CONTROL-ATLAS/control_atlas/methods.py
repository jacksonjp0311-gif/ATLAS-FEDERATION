"""Control Atlas bounded *teaching* calculations, not a deployed control loop.

Explicit inputs, finite numeric validation and no physical safety or stability
assurance from simulation. Standard library, no automatic actuation.
"""
from __future__ import annotations
from math import exp, expm1, sqrt, isfinite, log, pi

class ControlInputError(ValueError):
    """Model inputs or intended interpretation unsupported."""


def num(v, name, *, positive=False, nonnegative=False):
    if type(v) not in (float,int) or not isfinite(v):raise ControlInputError(f'{name}: finite real scalar required')
    if abs(v)>1e40:raise ControlInputError(f'{name}: magnitude exceeds bounded numerical model')
    if positive and v<=0:raise ControlInputError(f'{name}: must be positive')
    if nonnegative and v<0:raise ControlInputError(f'{name}: must be nonnegative')
    return float(v)


def zoh_first_order(gain,tau_s,sample_s):
    """Exact scalar zero-order hold of dy/dt=(-y+gain*u)/tau."""
    k=num(gain,'gain');tau=num(tau_s,'tau_s',positive=True);dt=num(sample_s,'sample_s',positive=True)
    if not isfinite(dt/tau):raise ControlInputError('sampling time ratio exceeds finite model limits')
    a=exp(-dt/tau);b=k*(-expm1(-dt/tau))
    return {'a':a,'b':b,'sample_s':dt,'discrete_model':'y[k+1]=a*y[k]+b*u[k]',
            'limits':['linear stable first-order plant, constant u between samples','no deadtime, saturation, unmodeled states, sample jitter or sensor noise']}


def first_order_step(gain,tau_s,time_s,input_step=1.0,y0=0.0):
    k=num(gain,'gain');tau=num(tau_s,'tau_s',positive=True);t=num(time_s,'time_s',nonnegative=True)
    u=num(input_step,'input_step');x=num(y0,'y0');target=k*u
    y=target+(x-target)*exp(-t/tau)
    return {'time_s':t,'output':y,'target_if_held':target,
            'limits':['ideal first-order linear plant, step held from time zero','not experimental system identification or equipment response']}


def simulate_zoh_first_order(gain,tau_s,sample_s,inputs,y0=0.0):
    if not isinstance(inputs,list) or not 1<=len(inputs)<=10000:raise ControlInputError('inputs list length must be 1..10000')
    a=zoh_first_order(gain,tau_s,sample_s)
    x=num(y0,'y0');xs=[x]
    for i,u in enumerate(inputs):
        x=a['a']*x+a['b']*num(u,f'u[{i}]')
        if not isfinite(x):raise ControlInputError('numeric overflow')
        xs.append(x)
    return {'states':xs,'output_after_inputs':xs[1:],'dt_s':a['sample_s'],
            'origin':'synthetic_constant_input_hold','limits':a['limits']}


def scalar_closed_loop(a,b,k):
    aa=num(a,'a');bb=num(b,'b');kk=num(k,'k');pole=aa-bb*kk
    if not isfinite(pole):raise ControlInputError('pole overflow')
    return {'closed_loop_pole':pole,'asymptotically_stable_for_scalar_discrete_linear_model':abs(pole)<1,
            'limits':['linear scalar state feedback u=-k*x; no saturations, disturbances, delay or model uncertainty','pole test is not system safety or robust stability certification']}


def eigenvalues_2x2(A):
    if not isinstance(A,(list,tuple)) or len(A)!=2 or any(not isinstance(x,(list,tuple)) or len(x)!=2 for x in A):
        raise ControlInputError('A must be 2x2')
    a,b,c,d=[num(v,'A element') for row in A for v in row]
    tr=a+d;det=a*d-b*c;discriminant=tr*tr-4*det
    if not all(map(isfinite,[tr,det,discriminant])):raise ControlInputError('matrix outside finite range')
    if discriminant>=0:
        root=sqrt(discriminant);eig=[(tr+root)/2,(tr-root)/2];rho=max(abs(x) for x in eig)
        reprs=[{'real':x,'imag':0.0} for x in eig]
    else:
        real=tr/2;imag=sqrt(-discriminant)/2;rho=(real*real+imag*imag)**.5
        reprs=[{'real':real,'imag':imag},{'real':real,'imag':-imag}]
    return {'eigenvalues':reprs,'spectral_radius':rho,'asymptotically_stable_if_discrete_LTI':rho<1,
            'limits':['real 2x2 linear time-invariant state transition only','no robustness, nonlinear guarantees, saturation or domain identification']}


def rank_two_state(A,B,C,relative_determinant_cutoff=1e-10):
    """2-state SISO determinant tests; warns on numerical rank uncertainty.

    Wc=[B, AB], Wo=[C; CA]. Returns a *classification* with explicit
    numerical tolerance, not a proof for ill-scaled physical coordinates.
    """
    eig=eigenvalues_2x2(A)
    if not isinstance(B,(list,tuple)) or len(B)!=2 or not isinstance(C,(list,tuple)) or len(C)!=2:
        raise ControlInputError('B and C must each have two entries')
    b0,b1=num(B[0],'B0'),num(B[1],'B1');c0,c1=num(C[0],'C0'),num(C[1],'C1')
    a00,a01=A[0];a10,a11=A[1]
    ab0=a00*b0+a01*b1;ab1=a10*b0+a11*b1
    ca0=c0*a00+c1*a10;ca1=c0*a01+c1*a11
    detc=b0*ab1-b1*ab0;deto=c0*ca1-c1*ca0
    tol=num(relative_determinant_cutoff,'relative_determinant_cutoff',positive=True)
    if tol>=1:raise ControlInputError('cutoff must be less than 1')
    sc=max(1.0,abs(b0),abs(b1),abs(ab0),abs(ab1))
    so=max(1.0,abs(c0),abs(c1),abs(ca0),abs(ca1))
    return {'controllability_determinant':detc,'observability_determinant':deto,
      'controllability_matrix':[[b0,ab0],[b1,ab1]],'observability_matrix':[[c0,c1],[ca0,ca1]],
      'controllability_rank_numerically_full':abs(detc)>tol*sc*sc,
      'observability_rank_numerically_full':abs(deto)>tol*so*so,
      'relative_determinant_cutoff':tol,'eigenvalue_check':eig,
      'limits':['SISO two-state only; coordinate scaling can affect numerical determinant threshold','rank does not imply safe actuation or a correctly identified physical plant']}


def pid_saturated_demo(kp,ki,kd,dt_s,setpoints,measurements,minimum_u,maximum_u,*,clamp_antiwindup=True):
    """Finite input-trace, derivative-on-measurement PID *calculation*, no actuation.

    Candidate I_next=I + ki*error*dt; when clamped, freeze if candidate
    would push an already saturated output further into saturation. No
    plant/closed-loop stability claim is implied by the returned trace.
    """
    if not isinstance(setpoints,list) or not isinstance(measurements,list) or not 1<=len(setpoints)==len(measurements)<=10000:
        raise ControlInputError('setpoint and measurement lists must have 1..10000 equal samples')
    Kp=num(kp,'kp');Ki=num(ki,'ki');Kd=num(kd,'kd');dt=num(dt_s,'dt_s',positive=True)
    lo=num(minimum_u,'minimum_u');hi=num(maximum_u,'maximum_u')
    if not lo<hi:raise ControlInputError('actuator limits must be ordered')
    if type(clamp_antiwindup) is not bool:raise ControlInputError('clamp_antiwindup must be Boolean')
    rows=[];I=0.0;prev=None
    for j,(sp,meas) in enumerate(zip(setpoints,measurements)):
        r=num(sp,f'setpoint[{j}]');y=num(meas,f'measurement[{j}]');e=r-y
        D=0.0 if prev is None else -Kd*(y-prev)/dt
        next_I=I+Ki*e*dt
        proposed=Kp*e+next_I+D
        if clamp_antiwindup and ((proposed>hi and Ki*e>0) or (proposed<lo and Ki*e<0)):
            next_I=I
        raw=Kp*e+next_I+D;u=min(hi,max(lo,raw))
        if not all(map(isfinite,[I,next_I,D,raw,u])):raise ControlInputError('numerical overflow in PID trace')
        rows.append({'sample':j,'error':e,'P':Kp*e,'I':next_I,'D_on_measurement':D,'raw_u':raw,'clamped_u':u,'saturated':u!=raw})
        I=next_I;prev=y
    return {'trace':rows,'final_integral':I,'controller_only':True,'antiwindup':'conditional_integration_clamping' if clamp_antiwindup else 'none',
            'limits':['no physical plant or device is controlled','derivative filtering and plant saturation dynamics absent','clamping is one illustrative antiwindup policy, not independently tuned robust PID']}


def fit_scalar_arx(xs,us,*,det_tolerance=1e-12):
    """Estimate a,b for x[k+1]=a*x[k]+b*u[k] by batch in-sample LS.

    Refuse insufficiently excited two-column regressors. Does not handle
    closed-loop noise bias, exogenous disturbances, delay or varying time step.
    """
    if not isinstance(xs,list) or not isinstance(us,list) or len(xs)!=len(us)+1 or not 5<=len(us)<=20000:
        raise ControlInputError('observed states len=n+1, inputs len=n, n=5..20000')
    x=[num(v,'state') for v in xs];u=[num(v,'input') for v in us]
    sx2=sum(v*v for v in x[:-1]);su2=sum(v*v for v in u);sxu=sum(a*b for a,b in zip(x[:-1],u))
    sxy=sum(a*b for a,b in zip(x[:-1],x[1:]));suy=sum(a*b for a,b in zip(u,x[1:]))
    det=sx2*su2-sxu*sxu;scale=max(1.,abs(sx2*su2),abs(sxu*sxu))
    if not all(map(isfinite,[det,scale,sx2,su2,sxu,sxy,suy])):raise ControlInputError('regression sums overflow')
    eps=num(det_tolerance,'det_tolerance',positive=True)
    if det<=eps*scale:raise ControlInputError('regression unidentifiable or poorly excited; no estimator result')
    a=(sxy*su2-suy*sxu)/det;b=(suy*sx2-sxy*sxu)/det
    residuals=[x[i+1]-a*x[i]-b*u[i] for i in range(len(u))]
    rss=sum(v*v for v in residuals)
    return {'a_hat':a,'b_hat':b,'rss':rss,'n':len(u),'regression_determinant':det,
            'in_sample_fit_only':True,'scientific_identification_verified':False,
            'limits':['state x observed directly and perfectly in this teaching tool',
                      'no offsets, noise model, process delay, time-varying parameters, instrumental variables, validation split or uncertainty intervals',
                      'closed-loop data may bias least squares; excitation and measurement provenance need independent review']}


def alias_frequency(f_hz,sampling_hz):
    f=num(f_hz,'f_hz',nonnegative=True);fs=num(sampling_hz,'sampling_hz',positive=True)
    folded=f % fs;alias=min(folded,fs-folded)
    return {'input_frequency_hz':f,'sampling_hz':fs,'aliased_frequency_hz':alias,
            'below_nyquist':f<fs/2,'at_nyquist':f==fs/2,
            'limits':['ideal uniformly sampled sinusoid only','aliases cannot be disambiguated from samples without extra bandlimit/prior','jitter, leakage, finite-window noise and anti-alias filtering not assessed']}


def scalar_lqr(a,b,q,r):
    """Infinite-horizon scalar discrete LQR stabilizing positive DARE solution."""
    A=num(a,'a');B=num(b,'b');Q=num(q,'q',positive=True);RR=num(r,'r',positive=True)
    if B==0:raise ControlInputError('unactuated scalar: stabilizing feedback unavailable here')
    coeff=RR*(1-A*A)-Q*B*B
    disc=coeff*coeff+4*B*B*Q*RR
    if not isfinite(disc):raise ControlInputError('DARE numerical overflow')
    root=sqrt(disc)
    P=(2*Q*RR/(coeff+root)) if coeff>=0 else (-coeff+root)/(2*B*B)
    K=A*B*P/(RR+B*B*P)
    pole=A-B*K
    if not (isfinite(P) and isfinite(K) and abs(pole)<1):raise ControlInputError('DARE did not yield stabilizing scalar solution')
    return {'P':P,'feedback_gain':K,'closed_loop_pole':pole,'stabilizing_scalar_model':True,
            'limits':['unconstrained infinite-horizon scalar linear-quadratic problem','Q,R and plant dynamics supplied, not inferred','no actuator limits, state constraints, nonlinearity, uncertainty or safety guarantee']}


def scalar_kalman_update(a,prior_mean,prior_variance,q_process,r_measurement,measurement):
    """One scalar Kalman measurement update after one known linear prediction.

    Dynamics x_next=a*x, process variance Q; y=x+v, noise variance R.
    """
    A=num(a,'a');mu=num(prior_mean,'prior_mean');P=num(prior_variance,'prior_variance',nonnegative=True)
    Q=num(q_process,'q_process',nonnegative=True);R=num(r_measurement,'r_measurement',positive=True);y=num(measurement,'measurement')
    pred=A*mu;pp=A*A*P+Q;gain=pp/(pp+R)
    post=pred+gain*(y-pred);var=(1-gain)*pp
    return {'predicted_mean':pred,'predicted_variance':pp,'gain':gain,'posterior_mean':post,'posterior_variance':var,
            'limits':['linear scalar Gaussian/second-moment noise assumptions with specified Q and R','measurement directly observes state without bias','no state-constraint, non-Gaussian, outlier, unknown noise covariance or timing audit']}
