"""Bounded two-state / two-sensor output-feedback *observer* reference.

All state/noise/input quantities are declared in compatible normalized units.
No actual physical bounds are established. This module does not compute a
robust controller, actuator authority, safe action or real-world certification.
"""
from __future__ import annotations
from math import isfinite
from .methods import ControlInputError


def _scalar(x,name,positive=False,nonnegative=False):
    if type(x) not in (int,float) or not isfinite(x):raise ControlInputError(f'{name} must be finite')
    v=float(x)
    if positive and v<=0:raise ControlInputError(f'{name} must be positive')
    if nonnegative and v<0:raise ControlInputError(f'{name} must be nonnegative')
    return v

def _matrix(m,name):
    if not isinstance(m,(list,tuple)) or len(m)!=2 or any(not isinstance(r,(list,tuple)) or len(r)!=2 for r in m):
        raise ControlInputError(f'{name} must be exactly 2x2')
    return [[_scalar(m[i][j],f'{name}[{i}][{j}]') for j in range(2)] for i in range(2)]

def _vector(v,name,nonnegative=False):
    if not isinstance(v,(list,tuple)) or len(v)!=2:raise ControlInputError(f'{name} must have two entries')
    return [_scalar(v[i],f'{name}[{i}]',nonnegative=nonnegative) for i in range(2)]

def _mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def _mv(A,x):return [sum(A[i][k]*x[k] for k in range(2)) for i in range(2)]

def _finite_vector(v,label):
    if not all(isfinite(q) for q in v):raise ControlInputError(f'{label} overflow')
    return v


def two_by_two_observer_error_tube(*,A,C,L,initial_error_radii,process_error_radii,
                                    measurement_error_radii,steps):
    """Bound |e[k]| given e[k+1]=(A-LC)e[k]+w[k]-L*v[k].

    Assumes the observer uses the SAME known applied plant input as the plant,
    that all samples align and that deterministic componentwise hard bounds W,V
    hold. Noise covariance/standard deviation is NOT a hard bound.
    """
    A=_matrix(A,'A');C=_matrix(C,'C');L=_matrix(L,'L')
    e0=_vector(initial_error_radii,'e0',nonnegative=True)
    W=_vector(process_error_radii,'W',nonnegative=True)
    V=_vector(measurement_error_radii,'V',nonnegative=True)
    if type(steps)is not int or not 1<=steps<=500:raise ControlInputError('steps must be integer 1..500')
    LC=_mm(L,C);F=[[A[i][j]-LC[i][j] for j in range(2)] for i in range(2)]
    absF=[[abs(v) for v in row] for row in F];absL=[[abs(v) for v in row] for row in L]
    forcing=[W[i]+sum(absL[i][j]*V[j] for j in range(2)) for i in range(2)]
    trajectory=[list(e0)];e=list(e0)
    for _ in range(steps):
        e=_finite_vector([sum(absF[i][j]*e[j] for j in range(2))+forcing[i] for i in range(2)],'observer bound')
        trajectory.append(e)
    row_gain=max(sum(row) for row in absF)
    limiting=None
    if row_gain<1:
        # Conservative scalar infinity-norm envelope, not the exact minimal
        # positively invariant error set for the multivariable observer.
        lim=max(forcing)/(1-row_gain)
        if isfinite(lim):limiting=[lim,lim]
    return {'schema':'atlas.control-mimo-observer-error-tube/1','dimension':2,
        'output_dimension':2,'F_observer_error_dynamics':F,
        'absolute_F':absF,'componentwise_forcing':forcing,'error_radii':trajectory,
        'sufficient_row_sum_contraction':row_gain<1,'row_sum_gain':row_gain,
        'conservative_stationary_infinity_norm_envelope':limiting,
        'status':'conditional_mathematical_error_enclosure_only',
        'limitations':['All A,C,L,W,V and initial error limits must be physically justified for this purpose',
          'Both observer and plant must use the same known applied input and aligned current observations',
          'No actuator dynamics, intersample excursions, nonlinearities, correlated interval reduction or physical safety are represented',
          'An observer bound does not certify closed-loop state constraints or actuator feasibility',
          'Failure of the sufficient row-sum test does not prove physical instability']}


def two_sensor_consistency(*,estimate,estimated_error_radii,C,sensor_values,measurement_error_radii):
    """Check whether an observed y is compatible with C xhat and hard bounds.

    Incompatibility does not identify root cause. Independent intervals may be
    conservative; compatible measurements do not authenticate sensors.
    """
    h=_vector(estimate,'h');E=_vector(estimated_error_radii,'E',nonnegative=True)
    C=_matrix(C,'C');y=_vector(sensor_values,'y');V=_vector(measurement_error_radii,'V',nonnegative=True)
    center=_mv(C,h)
    rad=[sum(abs(C[i][j])*E[j] for j in range(2))+V[i] for i in range(2)]
    compatible=[abs(y[i]-center[i])<=rad[i]+1e-12 for i in range(2)]
    return {'schema':'atlas.control-two-sensor-consistency/1',
      'expected_sensor_intervals':[[center[i]-rad[i],center[i]+rad[i]] for i in range(2)],
      'compatible':all(compatible),'sensor_level_compatibility':compatible,
      'root_cause_identified':False,
      'limitations':['Compatible readings do not demonstrate calibration, completeness or sensor integrity',
        'Incompatible readings show a violated set of assumptions, not whether plant, actuator, sensor, timing or model is at fault',
        'Hard bounds must be measured/qualified separately; standard deviations cannot be used as hard envelopes']}
