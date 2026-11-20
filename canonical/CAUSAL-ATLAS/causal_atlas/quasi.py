"""Bounded, exact-arithmetic IV and RD teaching calculations.

These are separately invoked domain tools. They do not infer instrument validity,
continuity, monotonicity, or assignment mechanisms from an observed table. RD is
point estimation only: no bandwidth selection, bias-corrected inference, or
confidence interval is implemented. No numerical guard is a statistical test.
"""
from __future__ import annotations
from fractions import Fraction as F
from typing import Any
from .models import ModelError, rational

MAX_RD_ROWS = 512
ORIGINS = {'synthetic_constructed', 'operator_supplied', 'published_transcription'}


def number(value: Any) -> F:
    v = rational(value)
    if abs(v) > 10**12 or v.denominator.bit_length() > 128:
        raise ModelError('Number exceeds magnitude or precision limits')
    return v


def probability(value: Any) -> F:
    v = number(value)
    if not 0 <= v <= 1:
        raise ModelError('Probability must be in [0,1]')
    return v


def origin_label(value: str) -> str:
    if not isinstance(value,str) or value not in ORIGINS:
        raise ModelError('Declare data_origin: ' + ', '.join(sorted(ORIGINS)))
    return value


def ratio_contrast(delta_y, delta_d, *, minimum_first_stage) -> dict:
    """Arithmetic ratio with an explicitly selected operational guard, not an F test."""
    dy, dd, guard = map(number, (delta_y, delta_d, minimum_first_stage))
    if not 0 <= guard < 1:
        raise ModelError('minimum_first_stage must be in [0,1)')
    unresolved = abs(dd) <= guard
    return {
        'result': 'unresolved_first_stage' if unresolved else 'ratio_computed_not_causally_validated',
        'reduced_form': str(dy), 'first_stage': str(dd),
        'ratio': None if unresolved else str(dy / dd),
        'minimum_first_stage': str(guard),
        'guard_interpretation': 'caller-selected numerical/operational threshold, not a weak-IV significance test',
        'causal_identification_verified': False, 'confidence_interval': None,
        'weak_instrument_test_performed': False,
    }


def wald_summary(*, y_z0, y_z1, d_z0, d_z1, minimum_first_stage, data_origin) -> dict:
    """Four supplied means; actual treatment means must be probabilities."""
    y0, y1 = number(y_z0), number(y_z1)
    d0, d1 = probability(d_z0), probability(d_z1)
    out = ratio_contrast(y1-y0, d1-d0, minimum_first_stage=minimum_first_stage)
    out.update(schema='atlas.causal-wald/1', data_origin=origin_label(data_origin),
               supplied_means={'y_z0':str(y0),'y_z1':str(y1),'d_z0':str(d0),'d_z1':str(d1)},
               limitations=[
                   'A binary-instrument ratio is not automatically a population average treatment effect.',
                   'Independence, exclusion, consistency, relevant uptake and monotonicity need separate justification for LATE.',
                   'Four means cannot identify individual compliance types or validate those assumptions.',
                   'No sampling inference, nuisance adjustment or fitted propensity model is supplied.'])
    return out


def exclusion_sensitivity(*, reduced_form, first_stage, direct_lower, direct_upper,
                          minimum_first_stage, data_origin) -> dict:
    """Under assumed DeltaY=theta*DeltaD+gamma, vary gamma over a declared interval.

    This is NOT a confidence region or a generic bound for every IV violation.
    """
    low, high = number(direct_lower), number(direct_upper)
    if low > high:
        raise ModelError('direct_lower must not exceed direct_upper')
    out = ratio_contrast(reduced_form, first_stage, minimum_first_stage=minimum_first_stage)
    dy, dd = number(reduced_form), number(first_stage)
    out.update(schema='atlas.iv-exclusion-sensitivity/1', data_origin=origin_label(data_origin),
               additive_direct_contribution=[str(low),str(high)],
               assumed_equation='reduced_form = theta * first_stage + direct_contribution',
               effect_scenario_bounds=None if out['ratio'] is None else
                   [str(x) for x in sorted(((dy-low)/dd, (dy-high)/dd))],
               is_confidence_interval=False,
               limitations=['Direct-contribution bounds are supplied assumptions, not inferred from data.',
                            'Other identification conditions remain required.',
                            'Negative first stages reverse bound ordering; no bounds are clipped.'])
    return out


def iv_population(types: list[dict]) -> dict:
    """Exactly integrate a fully stipulated finite population with independent Z.

    Y(d,z)=y0+(y1-y0)*d+direct_z*z. Every potential response and uptake rule is
    known only because this is a synthetic model, not fitted observational data.
    """
    fields={'name','mass','d0','d1','y0','y1','direct_z'}
    if not isinstance(types,list) or not 1 <= len(types) <= 64:
        raise ModelError('Expected 1..64 stipulated population types')
    names=set(); parsed=[]
    for r in types:
        if not isinstance(r,dict) or set(r)!=fields:
            raise ModelError('Each type must contain exactly: '+', '.join(sorted(fields)))
        name=r['name']
        if not isinstance(name,str) or not name.strip() or len(name)>128 or name in names:
            raise ModelError('Type names must be nonblank, bounded and unique')
        names.add(name)
        if any(type(r[k]) is not int or r[k] not in (0,1) for k in ('d0','d1')):
            raise ModelError('d0 and d1 must be integer 0 or 1')
        mass=probability(r['mass'])
        if mass<=0:raise ModelError('Zero-mass types must be omitted explicitly')
        parsed.append((mass,r['d0'],r['d1'],number(r['y0']),number(r['y1']),number(r['direct_z'])))
    if sum((r[0] for r in parsed),F(0)) != 1:
        raise ModelError('Masses must sum exactly to one')
    d={z:sum((q*(d1 if z else d0) for q,d0,d1,y0,y1,g in parsed),F(0)) for z in (0,1)}
    y={z:sum((q*(y0+(y1-y0)*(d1 if z else d0)+g*z)
                for q,d0,d1,y0,y1,g in parsed),F(0)) for z in (0,1)}
    shares={label:sum((q for q,d0,d1,y0,y1,g in parsed if (d0,d1)==pair),F(0))
            for label,pair in [('never',(0,0)),('always',(1,1)),('complier',(0,1)),('defier',(1,0))]}
    total_effect=sum((q*(y1-y0) for q,d0,d1,y0,y1,g in parsed),F(0))
    comp=sum((q*(y1-y0) for q,d0,d1,y0,y1,g in parsed if (d0,d1)==(0,1)),F(0))
    weighted=sum((q*(d1-d0)*(y1-y0) for q,d0,d1,y0,y1,g in parsed),F(0))
    direct=sum((q*g for q,d0,d1,y0,y1,g in parsed),F(0))
    out=wald_summary(y_z0=y[0],y_z1=y[1],d_z0=d[0],d_z1=d[1],
                     minimum_first_stage=0,data_origin='synthetic_constructed')
    out.update(schema='atlas.iv-stipulated-population/1',
               population_ate=str(total_effect),
               complier_effect=None if not shares['complier'] else str(comp/shares['complier']),
               type_masses={k:str(v) for k,v in shares.items()},
               monotone_in_declared_model=not bool(shares['defier']),
               exclusion_in_declared_model=all(g==0 for q,d0,d1,y0,y1,g in parsed),
               instrument_independence='stipulated by using the same type distribution in both Z arms',
               direct_contribution=str(direct),
               decomposition={'signed_type_effect':str(weighted), 'direct_contribution':str(direct),
                              'equals_reduced_form': weighted+direct==y[1]-y[0]},
               actual_observations=False, assumptions_empirically_checked=False)
    return out


def _rows(rows, fields):
    if not isinstance(rows,list) or not 1 <= len(rows) <= MAX_RD_ROWS:
        raise ModelError(f'Expected 1..{MAX_RD_ROWS} rows')
    names=set();parsed=[]
    for r in rows:
        if not isinstance(r,dict) or set(r)!=fields:
            raise ModelError('Rows must contain exactly: '+', '.join(sorted(fields)))
        rid=r['id']
        if not isinstance(rid,str) or not rid.strip() or len(rid)>128 or rid in names:
            raise ModelError('Row IDs must be nonblank, bounded and unique')
        names.add(rid);parsed.append((rid,number(r['x']),number(r['y'])))
    return parsed


def _fit_side(rows, *, cutoff: F, bandwidth: F, kernel: str) -> dict:
    # Weighted normal equations in the bounded coordinate u=(x-c)/h.
    # Fractions make this small teaching calculation exact; no floating-point solver.
    data=[(rid,(x-cutoff)/bandwidth,y,
           1-abs((x-cutoff)/bandwidth) if kernel=='triangular' else F(1))
          for rid,x,y in rows]
    if len(data)<3 or len({r[1] for r in data})<2:
        raise ModelError('Each side needs at least 3 positive-weight rows and 2 distinct scores')
    s0=sum((w for _,u,y,w in data),F(0));s1=sum((w*u for _,u,y,w in data),F(0))
    s2=sum((w*u*u for _,u,y,w in data),F(0))
    sy=sum((w*y for _,u,y,w in data),F(0));suy=sum((w*u*y for _,u,y,w in data),F(0))
    determinant=s0*s2-s1*s1
    if determinant<=0:raise ModelError('Singular weighted line fit')
    a=(s2*sy-s1*suy)/determinant;b=(s0*suy-s1*sy)/determinant
    equivalent=[{'id':rid,'weight':str(w*(s2-s1*u)/determinant)} for rid,u,y,w in data]
    rss=sum((w*(y-a-b*u)**2 for _,u,y,w in data),F(0))
    return {'intercept_at_cutoff':str(a),'slope_per_score_unit':str(b/bandwidth),
            'positive_weight_rows':len(data),'distinct_scores':len({r[1] for r in data}),
            'sum_kernel_weights':str(s0),
            'kernel_weight_ess':str(s0*s0/sum((w*w for _,u,y,w in data),F(0))),
            'weighted_rss':str(rss),'nearest_score_gap':str(min(abs(x-cutoff) for _,x,y in rows)),
            'normalized_weighted_score_variance':str(determinant/(s0*s0)),
            'intercept_equivalent_weights':equivalent,
            'negative_equivalent_weights':sum(F(r['weight'])<0 for r in equivalent),
            'score_range':[str(min(x for _,x,y in rows)),str(max(x for _,x,y in rows))]}


def local_linear_jump(rows: list[dict], *, cutoff, bandwidth, kernel, data_origin) -> dict:
    """Separate weighted lines; estimates an observed boundary discontinuity only.

    Common bandwidth and strict open window abs(x-c)<h. x=c is right. Records at
    the boundary are excluded for both kernels so comparisons use equal support.
    """
    parsed=_rows(rows,{'id','x','y'})
    c,h=number(cutoff),number(bandwidth)
    if h<=0:raise ModelError('Bandwidth must be positive')
    if kernel not in {'triangular','uniform'}:raise ModelError('Supported kernels: triangular, uniform')
    origin=origin_label(data_origin)
    kept=[r for r in parsed if abs(r[1]-c)<h]
    sides={label:_fit_side([r for r in kept if (r[1]<c)==(label=='left')],
                          cutoff=c,bandwidth=h,kernel=kernel) for label in ('left','right')}
    jump=F(sides['right']['intercept_at_cutoff'])-F(sides['left']['intercept_at_cutoff'])
    ids={r[0] for r in kept}
    return {'schema':'atlas.rd-local-linear/1','result':'point_estimate_not_causally_validated',
            'data_origin':origin,'cutoff':str(c),'bandwidth':str(h),'kernel':kernel,
            'window':'abs(x-cutoff)<bandwidth; cutoff belongs to right side',
            'jump':str(jump),'sides':sides,
            'excluded_row_ids':[r[0] for r in parsed if r[0] not in ids],
            'causal_identification_verified':False,'standard_error':None,'confidence_interval':None,
            'limitations':['Point-only fit: no bias correction, sampling interval or automatic bandwidth selection.',
              'Continuity, treatment-assignment rule, no coincident intervention and sorting require external evidence.',
              'Repeated score values do not create additional distinct support near the cutoff.',
              'Equivalent interpolation weights may be negative; kernel ESS is not inferential information.',
              'No population-wide effect is established by a cutoff estimate.']}


def fuzzy_local_ratio(rows: list[dict], *, cutoff, bandwidth, kernel,
                      minimum_first_stage, data_origin) -> dict:
    _rows(rows,{'id','x','y','d'})
    if any(type(r['d']) is not int or r['d'] not in (0,1) for r in rows):
        raise ModelError('Actual treatment d must be integer 0 or 1')
    y=local_linear_jump([{k:r[k] for k in ('id','x','y')} for r in rows],
                       cutoff=cutoff,bandwidth=bandwidth,kernel=kernel,data_origin=data_origin)
    d=local_linear_jump([{'id':r['id'],'x':r['x'],'y':r['d']} for r in rows],
                       cutoff=cutoff,bandwidth=bandwidth,kernel=kernel,data_origin=data_origin)
    out=ratio_contrast(y['jump'],d['jump'],minimum_first_stage=minimum_first_stage)
    out.update(schema='atlas.fuzzy-rd-ratio/1',data_origin=origin_label(data_origin),
               outcome_fit=y,treatment_fit=d,
               treatment_boundary_estimates_outside_unit_interval=any(
                   not 0<=F(side['intercept_at_cutoff'])<=1 for side in d['sides'].values()),
               limitations=['Ratio of estimated jumps, not a certified local complier effect.',
                 'Same window and kernel are used for both fits; fitted treatment boundaries are never clipped.',
                 'Exclusion, local monotonicity, continuity and a relevant treatment jump require justification.',
                 'No uncertainty estimate or weak-identification-robust inference is implemented.'])
    return out


def bandwidth_sensitivity(rows, *, cutoff, bandwidths, kernel, data_origin):
    if not isinstance(bandwidths,list) or not 1<=len(bandwidths)<=12:
        raise ModelError('Expected 1..12 explicitly selected bandwidths')
    values=[number(x) for x in bandwidths]
    if any(x<=0 for x in values) or len(set(values))!=len(values):
        raise ModelError('Bandwidths must be positive and unique')
    _rows(rows,{'id','x','y'});origin_label(data_origin);cutoff=number(cutoff)
    if kernel not in {'triangular','uniform'}:raise ModelError('Unknown kernel')
    result=[]
    for h in values:
        try:
            fit=local_linear_jump(rows,cutoff=cutoff,bandwidth=h,kernel=kernel,data_origin=data_origin)
            result.append({'bandwidth':str(h),'result':'computed','jump':fit['jump'],
                           'left_rows':fit['sides']['left']['positive_weight_rows'],
                           'right_rows':fit['sides']['right']['positive_weight_rows']})
        except ModelError as e:result.append({'bandwidth':str(h),'result':'unsupported','reason':str(e)})
    return {'schema':'atlas.rd-bandwidth-sensitivity/1','results':result,
            'selected_bandwidth':None,'causal_identification_verified':False,
            'limitation':'All requested windows reported; stability is not proof of valid design or an uncertainty interval.'}
