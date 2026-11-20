"""Control Atlas 0.4: bounded 2x2 robustness, control, and diagnostics.

NO live actuation, drivers, network, deployment, safety certification or automatic
causal attribution. All results are conditional on caller-supplied mathematical
models, exact units and scientific assumptions. Runtime stdlib only.
"""
from __future__ import annotations
from itertools import product
from math import sqrt, isfinite, hypot
from typing import Any
from .methods import ControlInputError, num, fit_scalar_arx


def _vec2(x,name):
    if not isinstance(x,(list,tuple)) or len(x)!=2:
        raise ControlInputError(f'{name} requires a length-2 vector')
    return (num(x[0],name),num(x[1],name))


def _mat2(x,name):
    if not isinstance(x,(list,tuple)) or len(x)!=2 or any(not isinstance(y,(list,tuple)) or len(y)!=2 for y in x):
        raise ControlInputError(f'{name} requires a 2x2 matrix')
    return tuple(_vec2(y,name) for y in x)


def _eigs_symmetric_2(m):
    x,y=m[0];z,w=m[1]
    # Callers have verified symmetry.
    mid=(x+w)/2; half=hypot((x-w)/2,(y+z)/2)
    return mid-half,mid+half


def _check_symmetric_psd(m,name,positive=False):
    if abs(m[0][1]-m[1][0])>1e-12*max(1,*[abs(q) for row in m for q in row]):
        raise ControlInputError(f'{name} must be symmetric')
    eig=_eigs_symmetric_2(m)
    threshold=1e-11*max(1,abs(eig[1]))
    if (positive and eig[0]<=threshold) or (not positive and eig[0]<-threshold):
        raise ControlInputError(f'{name} must be {"positive definite" if positive else "positive semidefinite"}')
    return eig


def _transpose(a):return ((a[0][0],a[1][0]),(a[0][1],a[1][1]))
def _mult(a,b):return tuple(tuple(a[i][0]*b[0][j]+a[i][1]*b[1][j] for j in range(2)) for i in range(2))
def _matminus(a,b):return tuple(tuple(a[i][j]-b[i][j] for j in range(2)) for i in range(2))
def _mv(a,x):return tuple(a[i][0]*x[0]+a[i][1]*x[1] for i in range(2))
def _dot(a,b):return a[0]*b[0]+a[1]*b[1]


def mimo_2x2_return_difference(plant_frequency_response, feedback_frequency_response):
    """S=(I+G K)^-1, T=I-S at one real-valued, *declared* point.

    No frequency sweep, complex phase, MIMO Nyquist or internal stability test.
    The calculation is purely algebraic and cannot establish robust stability.
    """
    g=_mat2(plant_frequency_response,'plant'); k=_mat2(feedback_frequency_response,'feedback')
    L=_mult(g,k)
    m=((1+L[0][0],L[0][1]),(L[1][0],1+L[1][1]))
    det=m[0][0]*m[1][1]-m[0][1]*m[1][0]
    # True 2x2 singular values from Gram. The determinant identity avoids
    # catastrophic cancellation for small sigma_min.
    frob2=sum(t*t for row in m for t in row)
    sigma_max=sqrt((frob2+sqrt(max(0,frob2*frob2-4*det*det)))/2)
    sigma_min=abs(det)/sigma_max if sigma_max else 0
    if not all(isfinite(z) for z in (sigma_max,sigma_min,det)) or sigma_min<=1e-12*max(1,sigma_max):
        raise ControlInputError('return-difference matrix singular or numerically unresolved at this point')
    S=((m[1][1]/det,-m[0][1]/det),(-m[1][0]/det,m[0][0]/det))
    T=tuple(tuple((1.0 if i==j else 0.0)-S[i][j] for j in range(2)) for i in range(2))
    residual=max(abs(S[i][j]+T[i][j]-(1.0 if i==j else 0.0)) for i in range(2) for j in range(2))
    return {'kind':'one_point_real_2x2_return_difference', 'loop_matrix':L,'return_difference':m,
      'singular_values':[sigma_max,sigma_min], 'condition_number':sigma_max/sigma_min,
      'S':S,'T':T,'S_plus_T_identity_max_error':residual,
      'limits':['No dynamic plant poles, sampling, actuator saturation or loop-transfer phase is represented',
                'A large sigma_min at one point is NOT proof of internal stability or full-frequency robust margin',
                'Plant and feedback matrices supplied, not system-identified or calibrated; no physical control']}


def common_lyapunov_box_2x2(a_bounds,P,relative_tolerance=1e-10):
    """Sufficient common P certificate over entire independent 2x2 matrix box.

    P>0 and P-A_i.T P A_i>0 at every box vertex. For P positive definite,
    A.T P A is matrix-convex in A, so P strict at vertices suffices for the
    whole convex box. No parameter correlation, interpolation error, saturation
    or nonlinearity. Floating point == numerical evidence, not formal proof.
    """
    if not isinstance(a_bounds,(list,tuple)) or len(a_bounds)!=2 or any(not isinstance(row,(list,tuple)) or len(row)!=2 for row in a_bounds):
        raise ControlInputError('a_bounds must be a 2x2 matrix of intervals')
    intervals=[]
    for row in a_bounds:
        for pair in row:
            if not isinstance(pair,(tuple,list)) or len(pair)!=2:raise ControlInputError('each interval requires [lo,hi]')
            lo,hi=num(pair[0],'matrix lo'),num(pair[1],'matrix hi')
            if lo>hi:raise ControlInputError('interval lower endpoint exceeds upper')
            intervals.append((lo,hi))
    p=_mat2(P,'P');_check_symmetric_psd(p,'P',positive=True)
    eps=num(relative_tolerance,'relative_tolerance',positive=True)
    if eps>1e-4:raise ControlInputError('excessively loose numerical tolerance')
    vertices=[]
    for vals in product(*intervals):
        a=((vals[0],vals[1]),(vals[2],vals[3]))
        q=_matminus(p,_mult(_transpose(a),_mult(p,a)))
        eig=_eigs_symmetric_2(q)
        if not all(isfinite(x) for x in eig):raise ControlInputError('nonfinite Q eigenvalue')
        vertices.append({'A':a,'minimum_Q_eigenvalue':eig[0]})
    worst=min(v['minimum_Q_eigenvalue'] for v in vertices)
    scale=max(1,*[abs(z) for row in p for z in row])
    ok=worst>eps*scale
    return {'kind':'common_quadratic_vertex_box_2x2', 'vertices_checked':len(vertices),
     'worst_minimum_Q_eigenvalue':worst,'relative_threshold':eps*scale,'vertex_evidence':vertices,
     'common_P_strict_decay_numerically_certified':ok,
     'scope':'Sufficient strict discrete-time quadratic decay for every matrix in supplied independent-entry box, conditional on validated bounds',
     'limits':['P failure is NOT proof any member unstable; another P or nonquadratic certificate may work',
               'Numerical float tests are not rigorous interval-arithmetic mathematical proof',
               'Parameter box and model assumptions not established by equipment observations',
               'No unmodeled delay, saturation, switching reset, nonlinear states, disturbances or real safety inference']}


def finite_horizon_lqr_2state(A,B,Q,R,Q_terminal,horizon,x0):
    """Two states, one input, finite horizon discrete-time quadratic LQR.

    DP recursion, Q and Qf symmetric PSD, R positive. No constraints or model
    uncertainty. The positive semidefiniteness checks are numerical tolerances.
    """
    a=_mat2(A,'A');b=_vec2(B,'B');q=_mat2(Q,'Q');qf=_mat2(Q_terminal,'Qf');r=num(R,'R',positive=True)
    _check_symmetric_psd(q,'Q');_check_symmetric_psd(qf,'Q_terminal')
    if type(horizon) is not int or not 1<=horizon<=128:raise ControlInputError('horizon must be integer 1..128')
    x=_vec2(x0,'x0')
    p=qf;pol=[];ps=[p]
    for step in range(horizon-1,-1,-1):
        pb=_mv(p,b);den=r+_dot(b,pb)
        if den<=0 or not isfinite(den):raise ControlInputError('unstable Riccati denominator')
        pa=_mult(p,a)
        numerator=(pb[0]*a[0][0]+pb[1]*a[1][0],pb[0]*a[0][1]+pb[1]*a[1][1])
        K=(numerator[0]/den,numerator[1]/den)
        apa=_mult(_transpose(a),pa)
        nextp=tuple(tuple(q[i][j]+apa[i][j]-numerator[i]*numerator[j]/den for j in range(2)) for i in range(2))
        nextp=((nextp[0][0],(nextp[0][1]+nextp[1][0])/2),((nextp[0][1]+nextp[1][0])/2,nextp[1][1]))
        if not all(isfinite(v) for row in nextp for v in row):raise ControlInputError('Riccati numerical overflow')
        pol.insert(0,K);ps.insert(0,nextp);p=nextp
    trajectory=[x];us=[];cost=0
    for K in pol:
        u=-_dot(K,x);us.append(u)
        cost+=_dot(x,_mv(q,x))+r*u*u
        ax=_mv(a,x);x=(ax[0]+b[0]*u,ax[1]+b[1]*u)
        trajectory.append(x)
    cost+=_dot(x,_mv(qf,x))
    v0=_dot(trajectory[0],_mv(ps[0],trajectory[0]))
    if not all(isfinite(v) for v in us+[cost,v0]):raise ControlInputError('nonfinite cost or control')
    return {'kind':'two_state_one_input_finite_horizon_unconstrained_LQR',
      'horizon':horizon,'initial_gain':pol[0], 'gains':pol,'Riccati_P0':ps[0],
      'predicted_controls':us,'predicted_states':trajectory,'realized_quadratic_cost':cost,
      'Riccati_value_x0':v0,'cost_identity_residual':abs(cost-v0),
      'limits':['Unconstrained exact two-state single-input linear plant; Q,Qf PSD and R>0',
                'No actuator limits, state constraints, model mismatch, disturbances or noise',
                'Optimization performed on declared model, not a safety-certified controller or physical plant']}


def scalar_grid_open_loop_plan(a,b,x0,horizon,input_grid,max_abs_input,max_abs_state,q_state,r_control,q_terminal=0):
    """Exhaustive *grid* search, horizon at most five. NOT globally optimal continuous MPC.

    The method returns either a finite-grid candidate or a failure to find one.
    Failure on the grid does NOT prove the continuous constrained problem infeasible.
    No live/receding-horizon actuation is performed.
    """
    A=num(a,'a');B=num(b,'b');x=num(x0,'x0')
    H=horizon
    if type(H) is not int or not 1<=H<=5:raise ControlInputError('horizon must be 1..5')
    lim=num(max_abs_input,'max_abs_input',positive=True);xlim=num(max_abs_state,'max_abs_state',positive=True)
    q=num(q_state,'q_state',nonnegative=True);rr=num(r_control,'r_control',positive=True);qf=num(q_terminal,'q_terminal',nonnegative=True)
    if not isinstance(input_grid,(list,tuple)) or not 2<=len(input_grid)<=7:raise ControlInputError('2..7 grid controls required')
    grid=[num(t,'input grid') for t in input_grid]
    if len(set(grid))!=len(grid) or any(abs(t)>lim+1e-12 for t in grid):
        raise ControlInputError('grid inputs must be distinct and within supplied bound')
    if abs(x)>xlim:raise ControlInputError('initial state outside declared admissible constraint')
    best=None;visited=0;feasible=0
    for controls in product(sorted(grid),repeat=H):
        visited+=1;now=x;states=[x];cost=0;valid=True
        for u in controls:
            cost+=q*now*now+rr*u*u
            now=A*now+B*u
            if not isfinite(now):raise ControlInputError('nonfinite state rollout')
            states.append(now)
            if abs(now)>xlim+1e-12:valid=False;break
        if not valid:continue
        feasible+=1;cost+=qf*now*now
        if best is None or cost<best['grid_cost']-1e-12:
            best={'controls':list(controls),'states':states,'grid_cost':cost}
    return {'kind':'finite_horizon_open_loop_grid_search_not_continuous_MPC',
      'search_size':visited,'feasible_grid_sequences':feasible,
      'status':'feasible_grid_candidate' if best else 'no_feasible_candidate_on_grid',
      'best':best,'grid_is_exhaustively_enumerated':True,
      'limits':['Not full continuous-input MPC, no guarantee of best real-valued input sequence',
                'No guaranteed recursively feasible real-time feedback; no device commands are generated',
                'No feasible grid candidate does NOT prove continuous optimization infeasible',
                'Plant model, constraint bounds and sample interval are user supplied, not independently verified']}


def normalized_innovation_two_sensor(innovation,covariance):
    """Numeric innovation squared nu.T S^-1 nu for 2 sensors with SPD S.

    Under correct Gaussian assumptions NIS has chi-square(2) sampling law, but
    this function does no distributional test, p-value or fault attribution.
    """
    nu=_vec2(innovation,'innovation');S=_mat2(covariance,'covariance')
    _check_symmetric_psd(S,'covariance',positive=True)
    det=S[0][0]*S[1][1]-S[0][1]*S[1][0]
    if det<=1e-15*max(1,abs(S[0][0]*S[1][1])):raise ControlInputError('covariance nearly singular')
    Sinv=((S[1][1]/det,-S[0][1]/det),(-S[1][0]/det,S[0][0]/det))
    nis=_dot(nu,_mv(Sinv,nu))
    if not isfinite(nis):raise ControlInputError('nonfinite normalized squared innovation')
    return {'kind':'two_sensor_normalized_innovation_squared','NIS':nis,'measurement_dimensions':2,
      'origin':'caller_supplied_innovation_and_covariance',
      'limits':['No claimed chi-square goodness of fit without correct jointly Gaussian model and covariance',
                'NIS alone is not a cause-specific sensor fault detector or physical safety interlock',
                'Covariance and innovation supplied; no live sensors, model validation, or timestamps checked']}


def ambiguous_sensor_state_bias(measurement,interpretations):
    """Show x+b observational ambiguity in one scalar reading (counterexample)."""
    y=num(measurement,'measurement')
    if not isinstance(interpretations,(list,tuple)) or len(interpretations)!=2:
        raise ControlInputError('exactly two hypotheses required')
    pairs=[]
    for item in interpretations:
        if not isinstance(item,dict) or set(item)!= {'hypothesis','state','sensor_bias'}:
            raise ControlInputError('each hypothesis requires hypothesis,state,sensor_bias')
        label=item['hypothesis']
        if not isinstance(label,str) or not label.strip() or len(label)>100:raise ControlInputError('hypothesis label invalid')
        state=num(item['state'],'state');bias=num(item['sensor_bias'],'bias')
        pred=state+bias
        if not isfinite(pred):raise ControlInputError('prediction overflow')
        pairs.append({'hypothesis':label,'predicted_measurement':pred,'residual':y-pred})
    same=all(abs(t['residual'])<=1e-12*max(1,abs(y)) for t in pairs) and (interpretations[0]['state']!=interpretations[1]['state'] or interpretations[0]['sensor_bias']!=interpretations[1]['sensor_bias'])
    return {'kind':'sensor_state_bias_identifiability_counterexample',
      'both_hypotheses_match_single_measurement':same,
      'result':'not_identified_by_this_measurement' if same else 'hypotheses_do_not_both_match',
      'hypothesis_checks':pairs,
      'limits':['Two chosen hypotheses only; cannot select true root cause, fault location, or mitigation',
                'Need independent calibrated measurement, temporal excitation or additional physically discriminating observations',
                'No sensors sampled and no real-world fault diagnosed']}


def arx_training_validation_split(states,inputs,train_steps):
    """Separate training and later prediction residuals for supplied scalar ARX.

    This is *developer* evaluation on input data, not independent held-out AI
    evaluation; no stationarity/causal excitation is established.
    """
    if not isinstance(states,(list,tuple)) or not isinstance(inputs,(list,tuple)) or len(states)!=len(inputs)+1:
        raise ControlInputError('states must have exactly one more sample than inputs')
    if type(train_steps) is not int or train_steps<5 or len(inputs)-train_steps<3:
        raise ControlInputError('at least five training steps and three later validation steps')
    xs=[num(x,'state') for x in states];us=[num(u,'input') for u in inputs]
    fit=fit_scalar_arx(xs[:train_steps+1],us[:train_steps])
    a,b=fit['a_hat'],fit['b_hat']
    # One-step held-later prediction conditional on each observed predecessor;
    # NOT multi-step feedback rollout or independent external dataset.
    validation=[xs[t+1]-a*xs[t]-b*us[t] for t in range(train_steps,len(us))]
    training=[xs[t+1]-a*xs[t]-b*us[t] for t in range(train_steps)]
    from math import sqrt
    train_rms=sqrt(sum(x*x for x in training)/len(training))
    val_rms=sqrt(sum(x*x for x in validation)/len(validation))
    return {'kind':'scalar_arx_time_ordered_one_step_validation','fitted_a':a,'fitted_b':b,
      'train_count':len(training),'later_validation_count':len(validation),
      'train_one_step_RMS':train_rms,'later_one_step_RMS':val_rms,
      'validation_to_training_ratio':(val_rms/train_rms if train_rms>1e-12 else None),
      'limits':['Time-ordered split alone does not establish independence, causal identification or absence of drift',
                'One-step predictions use the observed previous state, not unconstrained multi-step forecasting',
                'No real plant measurements, noise model, input calibration or excitation guarantee is supplied']}
