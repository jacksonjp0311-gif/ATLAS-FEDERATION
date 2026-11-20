"""Offline bounded state-feedback invariance and diagnostic simulations.

No actuator drivers, safety systems, network access, inferred physical parameters
or plant commissioning. Results apply only to the exact supplied linear models.
"""
from __future__ import annotations
from itertools import product
from math import isfinite
from .methods import ControlInputError, num


def _pair(values, label, *, nonnegative=False):
    if not isinstance(values,(tuple,list)) or len(values)!=2:
        raise ControlInputError(label+' must be length-two')
    return [num(z,label,nonnegative=nonnegative) for z in values]


def _mat2(a, label):
    if not isinstance(a,(tuple,list)) or len(a)!=2:
        raise ControlInputError(label+' must be 2x2')
    return [_pair(r,label) for r in a]


def _interval(v,label):
    lo,hi=_pair(v,label)
    if lo>hi:raise ControlInputError(label+' interval reversed')
    return lo,hi


def robust_invariant_box_2x2(*, A_intervals, B_intervals, state_feedback_K, state_radii,
                             disturbance_radii, actuator_limit, full_state_available:bool):
    """Exact corner-enumerated invariant axis-aligned box for independent param intervals.

    Plant x'=Ax+B*u+w; policy u=-(K0*x0+K1*x1). A is 2x2, B is 2x1.
    For EACH of 64 parameter vertices, check sum_j |Aij-Bi*Kj| rj + wi <= ri.
    Because induced row deviation is convex in independent parameters, corners
    bound all affine interior A,B choices, provided the intervals are sound.
    This is a model-only *sufficient* robust invariant-box certificate. It is
    not a safety interlock, and does not cover delayed or noisy state feedback.
    """
    if type(full_state_available) is not bool or not full_state_available:
        raise ControlInputError('true full state feedback explicitly required; sensor estimates do not inherit certificate')
    if not isinstance(A_intervals,(tuple,list)) or len(A_intervals)!=2:
        raise ControlInputError('A_intervals must be 2x2 nested intervals')
    a=[]
    for row in A_intervals:
        if not isinstance(row,(tuple,list)) or len(row)!=2:raise ControlInputError('A row has two intervals')
        a.append([_interval(v,'A interval') for v in row])
    if not isinstance(B_intervals,(tuple,list)) or len(B_intervals)!=2:
        raise ControlInputError('B_intervals must be two intervals')
    b=[_interval(x,'B interval') for x in B_intervals]
    k=_pair(state_feedback_K,'K')
    radii=_pair(state_radii,'r',nonnegative=True)
    w=_pair(disturbance_radii,'w',nonnegative=True)
    limit=num(actuator_limit,'actuator_limit',nonnegative=True)
    if any(v<=0 for v in radii):raise ControlInputError('box radii must be positive')
    # Reject numeric overflow rather than fabricating an inequality.
    worst=[(-1,None),(-1,None)]
    for bits in product((0,1),repeat=6):
        vals=[a[0][0][bits[0]],a[0][1][bits[1]],a[1][0][bits[2]],a[1][1][bits[3]],b[0][bits[4]],b[1][bits[5]]]
        for i in range(2):
            bi=vals[4+i];j=2*i
            bound=abs(vals[j]-bi*k[0])*radii[0]+abs(vals[j+1]-bi*k[1])*radii[1]+w[i]
            if not isfinite(bound):raise ControlInputError('numerical bound overflow')
            if bound>worst[i][0]:worst[i]=(bound,bits)
    u_bound=abs(k[0])*radii[0]+abs(k[1])*radii[1]
    if not isfinite(u_bound):raise ControlInputError('numerical input bound overflow')
    state_ok=all(worst[i][0]<=radii[i] for i in range(2))
    actuator_ok=u_bound<=limit
    return {'schema':'atlas.control-robust-box/1','model':'independent_intervals_2x2_one_input_exact_vertices',
        'vertices_checked':64,'max_successor_abs_bound':[z[0] for z in worst],
        'worst_vertex_bits':[list(z[1]) for z in worst],
        'state_radii':radii,'disturbance_radii':w,'input_max_abs_bound':u_bound,
        'state_box_invariant_for_every_assumed_model':state_ok,
        'actuator_unsaturated_for_every_state_in_box':actuator_ok,
        'conditional_invariance_and_input_feasibility':state_ok and actuator_ok,
        'status':'sufficient_mathematical_certificate' if state_ok and actuator_ok else 'candidate_not_certified',
        'limits':['Inputs/intervals supplied rather than experimentally bounded; independent 2x2 plant parameter rectangles only',
            'Exact one-step state box inequalities for given static linear feedback; no unknown nonlinearities or delays',
            'Assumes true full state x: no sensor error, bias, timing jitter, saturation, disturbance outside bounds or changing controller',
            'Failed candidate does not establish that a real plant will become unsafe; model-only statement',
            'No PLC/safety-system integration, deployment permission or physical state safety certification']}


def scalar_robust_interval(*, closed_loop_gain:float, state_radius:float,
                           disturbance_radius:float, input_gain:float, input_limit:float,
                           state_feedback_exact:bool):
    """Necessary/sufficient for invariance of symmetric interval in stated scalar model.

    x' = closed_loop_gain * x + w, |w| <=W, |x|<=R, |u|=|input_gain*x| <=U.
    """
    if state_feedback_exact is not True:
        raise ControlInputError('exact state feedback required')
    g=num(closed_loop_gain,'g');r=num(state_radius,'r',positive=True)
    w=num(disturbance_radius,'w',nonnegative=True);k=num(input_gain,'k')
    U=num(input_limit,'U',nonnegative=True)
    reach=abs(g)*r+w;maxu=abs(k)*r
    if not all(isfinite(z) for z in (reach,maxu)):raise ControlInputError('numeric overflow')
    valid=reach<=r and maxu<=U
    return {'model':'exact_discrete_scalar_symmetric_box','worst_one_step_abs_state':reach,
            'worst_input_abs':maxu,'state_invariant':reach<=r,'input_feasible':maxu<=U,
            'conditional_certificate':valid,'status':'sufficient_mathematical_certificate' if valid else 'candidate_not_certified',
            'limits':['Exact scalar additive disturbance interval model only','Certificate does not cover measurement error, delay or dynamic saturation',
                'No physical validation, hardware safety interlock or reliability qualification']}


def simulate_2x2_state_feedback(*,A,B,K,x0,disturbances,input_limit,measurement_biases=None):
    """Illustrate a trajectory with/without an explicitly biased measurement.

    y=x+bias; u=clip(-K@y, +/-limit). No real controller or physical sensor.
    """
    a=_mat2(A,'A');b=_pair(B,'B');k=_pair(K,'K');x=_pair(x0,'x0')
    U=num(input_limit,'input_limit',nonnegative=True)
    if not isinstance(disturbances,list) or not 1<=len(disturbances)<=1000:
        raise ControlInputError('disturbances must be a list of length 1..1000')
    ds=[_pair(w,'disturbance') for w in disturbances]
    biases=[_pair(w,'sensor_bias') for w in measurement_biases] if measurement_biases is not None else [[0.0,0.0] for _ in ds]
    if len(biases)!=len(ds):raise ControlInputError('measurement bias length mismatch')
    history=[list(x)];actions=[];flags=[]
    for w,bias in zip(ds,biases):
        measured=[x[i]+bias[i] for i in range(2)]
        requested=-sum(k[j]*measured[j] for j in range(2))
        u=max(-U,min(U,requested))
        sat=u!=requested
        nxt=[a[i][0]*x[0]+a[i][1]*x[1]+b[i]*u+w[i] for i in range(2)]
        if not all(isfinite(z) for z in nxt):raise ControlInputError('simulated state overflow')
        actions.append(u);flags.append(sat);history.append(nxt);x=nxt
    return {'origin':'authored_synthetic_2x2_trajectory','states':history,'applied_commands':actions,
        'saturated_steps':sum(flags),'sensor_bias_applied':measurement_biases is not None,
        'limits':['A simulated trajectory does not establish robust invariance or safe hardware behavior',
                  'The sensor-bias series is authored input, not diagnosed from any measurements',
                  'No physical process, actuator device or safety-rated controller used']}
