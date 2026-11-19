"""Standard-library finite reference kernels for manufacturing metrology and planning.

Inputs have explicit units. Models are illustrative and NOT equipment certification,
process qualification, safe machine operation instructions, or traceability claims.
"""
from __future__ import annotations
from math import isfinite, sqrt, pi, exp
from collections import deque


def finite(*x):
    if not all(isinstance(z,(int,float)) and not isinstance(z,bool) and isfinite(z) for z in x):
        raise ValueError('finite real inputs required')


def tolerance_fit(hole_min_mm, hole_max_mm, shaft_min_mm, shaft_max_mm):
    """Signed clearance interval: positive means positive clearance."""
    finite(hole_min_mm,hole_max_mm,shaft_min_mm,shaft_max_mm)
    if hole_min_mm>hole_max_mm or shaft_min_mm>shaft_max_mm: raise ValueError('reversed tolerance')
    low=hole_min_mm-shaft_max_mm
    high=hole_max_mm-shaft_min_mm
    kind='clearance' if low>0 else 'interference' if high<0 else 'transition_or_boundary'
    return {'minimum_clearance_mm':low,'maximum_clearance_mm':high,'class':kind}


def interval_stackup(components):
    """Exact extremal interval sum under independent feasible interval constraints.
    A signed component (lo,hi) may have both negative bounds, e.g. an opposing dimension.
    """
    if not components: raise ValueError('at least one component')
    low=high=0.0
    for pair in components:
        if len(pair)!=2: raise ValueError('pair required')
        a,b=pair;finite(a,b)
        if a>b:raise ValueError('reversed component')
        low+=a;high+=b
    return low,high


def covariance_stackup(stds,covariance):
    """Variance of sum; caller must supply valid covariance matrix and justify correlation."""
    n=len(stds)
    if n<1 or len(covariance)!=n or any(len(row)!=n for row in covariance):raise ValueError('dimension mismatch')
    for v in stds: finite(v)
    if any(v<0 for v in stds):raise ValueError('negative standard deviation')
    for i in range(n):
        for j in range(n):
            finite(covariance[i][j]);
            if abs(covariance[i][j]-covariance[j][i])>1e-10*max(1.,abs(covariance[i][j])):raise ValueError('asymmetric covariance')
            if abs(covariance[i][j])>stds[i]*stds[j]+1e-10:raise ValueError('impossible covariance bound')
        if abs(covariance[i][i]-stds[i]**2)>1e-9*max(1, stds[i]**2):raise ValueError('diagonal disagrees with stds')
    variance=sum(sum(row) for row in covariance)
    if variance < -1e-10:raise ValueError('negative aggregate variance')
    return sqrt(max(0.,variance))


def thermal_length(length_m,cte_per_K,temp_change_K):
    """Linear first-order isotropic expansion, bounded small-strain model."""
    finite(length_m,cte_per_K,temp_change_K)
    if length_m<=0 or abs(cte_per_K*temp_change_K)>0.1: raise ValueError('invalid small-strain length/temperature')
    return length_m*(1+cte_per_K*temp_change_K)


def cutting_estimate(diameter_mm, cutting_speed_m_min, teeth, feed_per_tooth_mm, axial_depth_mm, radial_width_mm, specific_cutting_force_N_mm2, efficiency):
    """Rotational machining with a uniform chip-load approximation; no safe setpoint inference."""
    finite(diameter_mm,cutting_speed_m_min,teeth,feed_per_tooth_mm,axial_depth_mm,radial_width_mm,specific_cutting_force_N_mm2,efficiency)
    if min(diameter_mm,cutting_speed_m_min,feed_per_tooth_mm,axial_depth_mm,radial_width_mm,specific_cutting_force_N_mm2)<=0 or not (0<efficiency<=1) or teeth<1 or int(teeth)!=teeth:raise ValueError('invalid process assumptions')
    rpm=1000*cutting_speed_m_min/(pi*diameter_mm)
    feed_mm_min=rpm*teeth*feed_per_tooth_mm
    mrr_mm3_min=feed_mm_min*axial_depth_mm*radial_width_mm
    cut_power_W=specific_cutting_force_N_mm2*mrr_mm3_min/60000.
    return {'rpm':rpm,'feed_mm_min':feed_mm_min,'mrr_mm3_min':mrr_mm3_min,'cutting_W':cut_power_W,'input_W_lower_bound':cut_power_W/efficiency}


def cantilever_deflection(force_N,length_m,youngs_Pa,I_m4):
    finite(force_N,length_m,youngs_Pa,I_m4)
    if length_m<=0 or youngs_Pa<=0 or I_m4<=0:raise ValueError('positive length, E, second moment required')
    return force_N*length_m**3/(3*youngs_Pa*I_m4)


def leadscrew_position(turns,pitch_mm_per_turn,backlash_mm,steps_per_turn):
    finite(turns,pitch_mm_per_turn,backlash_mm,steps_per_turn)
    if pitch_mm_per_turn<=0 or backlash_mm<0 or steps_per_turn<1 or int(steps_per_turn)!=steps_per_turn:raise ValueError('invalid drive')
    ideal=turns*pitch_mm_per_turn
    quant=pitch_mm_per_turn/steps_per_turn
    # Unknown direction/history: interval is conservative, not a predicted point.
    return {'ideal_mm':ideal,'reachable_interval_mm':[ideal-backlash_mm-quant/2,ideal+backlash_mm+quant/2], 'resolution_mm':quant}


def capability(lsl,usl,mean,sigma,stable_process=False,distribution_assessed=False):
    """Capability ratios are undefined when process stability/distribution not evidenced."""
    finite(lsl,usl,mean,sigma)
    if lsl>=usl or sigma<=0:raise ValueError('invalid limits/sigma')
    if not stable_process or not distribution_assessed:
        return {'cp':None,'cpk':None,'status':'not_qualified_assumptions'}
    return {'cp':(usl-lsl)/(6*sigma),'cpk':min(usl-mean,mean-lsl)/(3*sigma),'status':'conditional_on_supplied_assumptions'}


def control_chart_flags(values,center,sigma):
    finite(center,sigma)
    if sigma<=0:raise ValueError('sigma positive')
    results=[]
    for idx,z in enumerate(values):
        finite(z)
        if abs(z-center)>3*sigma: results.append(idx)
    return results


def guardband_verdict(reading,lsl,usl,expanded_uncertainty):
    finite(reading,lsl,usl,expanded_uncertainty)
    if lsl>=usl or expanded_uncertainty<0:raise ValueError('limits and uncertainty')
    a,b=reading-expanded_uncertainty,reading+expanded_uncertainty
    if a>=lsl and b<=usl:return 'accepted_under_declared_uncertainty'
    if b<lsl or a>usl:return 'rejected_under_declared_uncertainty'
    return 'indeterminate_measure_again'


def linear_calibration(reference,indication):
    """Fit indication = intercept + gain*reference; not a traceability certificate."""
    if len(reference)!=len(indication) or len(reference)<3:raise ValueError('need >=3 matched observations')
    for x,y in zip(reference,indication):finite(x,y)
    mx=sum(reference)/len(reference);my=sum(indication)/len(indication)
    sxx=sum((x-mx)**2 for x in reference)
    if sxx<=1e-25:raise ValueError('no calibration span')
    gain=sum((x-mx)*(y-my) for x,y in zip(reference,indication))/sxx
    offset=my-gain*mx
    residuals=[y-offset-gain*x for x,y in zip(reference,indication)]
    sigma=sqrt(sum(r*r for r in residuals)/(len(reference)-2))
    return {'gain':gain,'offset':offset,'residual_sigma_indication_units':sigma,'samples':len(reference)}


def critical_path(operations):
    """DAG precedence; durations are deterministic and resource conflicts excluded."""
    if not operations:raise ValueError('no operations')
    ids=set(operations)
    indegree={n:0 for n in ids};followers={n:[] for n in ids}
    for k,row in operations.items():
        duration=row['duration_min'];finite(duration)
        if duration<0:raise ValueError('negative duration')
        deps=list(row.get('requires',[]))
        if len(set(deps))!=len(deps) or k in deps or not set(deps)<=ids:raise ValueError('invalid dependency')
        indegree[k]=len(deps)
        for dep in deps:followers[dep].append(k)
    queue=deque(sorted(k for k in ids if indegree[k]==0))
    order=[];end={}
    while queue:
        k=queue.popleft();order.append(k)
        end[k]=float(operations[k]['duration_min'])+max([end[x] for x in operations[k].get('requires',[])],default=0.)
        for ch in sorted(followers[k]):
            indegree[ch]-=1
            if indegree[ch]==0:queue.append(ch)
    if len(order)!=len(ids):raise ValueError('cyclic routing')
    return {'order':order,'earliest_completion_min':end,'makespan_min':max(end.values()),'resource_capacity_not_modeled':True}


def cast_dimension_from_pattern(pattern_mm,linear_shrink_fraction):
    finite(pattern_mm,linear_shrink_fraction)
    if pattern_mm<=0 or not (0<=linear_shrink_fraction<0.2):raise ValueError('invalid hypothetical shrinkage')
    return pattern_mm*(1-linear_shrink_fraction)


def deposited_height(layers,layer_mm,scale_error_fraction=0.0):
    finite(layers,layer_mm,scale_error_fraction)
    if layers<1 or int(layers)!=layers or layer_mm<=0 or abs(scale_error_fraction)>0.2:raise ValueError('invalid deposition geometry')
    return layers*layer_mm*(1+scale_error_fraction)


def roughness_ra(profile_m):
    """Discrete equally spaced departures from the sample mean, not ISO-certified Ra metrology."""
    if len(profile_m)<2:raise ValueError('insufficient samples')
    for z in profile_m:finite(z)
    avg=sum(profile_m)/len(profile_m)
    return sum(abs(z-avg) for z in profile_m)/len(profile_m)


def first_order_thermal_state(initial_K,ambient_K,power_W,resistance_K_W,heat_capacity_J_K,time_s):
    finite(initial_K,ambient_K,power_W,resistance_K_W,heat_capacity_J_K,time_s)
    if min(initial_K,ambient_K)>1e6 or min(initial_K,ambient_K)<0 or resistance_K_W<=0 or heat_capacity_J_K<=0 or time_s<0:raise ValueError('invalid thermal lumped model')
    target=ambient_K+power_W*resistance_K_W
    tau=resistance_K_W*heat_capacity_J_K
    return target+(initial_K-target)*exp(-time_s/tau)
