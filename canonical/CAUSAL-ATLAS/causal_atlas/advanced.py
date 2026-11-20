"""Bounded, dependency-free causal-method arithmetic (reference edition v1).

Every method assumes its data-generating conditions are supplied. Calculations do not
establish a causal graph, randomized assignment, conditional exchangeability or
sampling validity. All results are exact Fractions where practical.
"""
from __future__ import annotations
from fractions import Fraction as F
from statistics import NormalDist
from typing import Any
from .models import ModelError, rational

MAX_STRATA = 256
MAX_COHORTS = 128


def number(x: Any, *, probability: bool = False, positive: bool = False) -> F:
    v = rational(x)
    if abs(v) > 10**12 or v.denominator.bit_length() > 160:
        raise ModelError('Numeric value exceeds precision/magnitude limits')
    if probability and not (0 <= v <= 1):
        raise ModelError('Probability outside [0,1]')
    if positive and v <= 0:
        raise ModelError('A strictly positive value is required')
    return v


def exact_dict(x: Any, keys: set[str], where: str = 'input') -> dict:
    if not isinstance(x, dict) or set(x) != keys:
        raise ModelError(f'{where} requires exactly {sorted(keys)}')
    return x


def exact_rows(x: Any, keys: set[str], maximum: int = MAX_STRATA) -> list[dict]:
    if not isinstance(x, list) or not 1 <= len(x) <= maximum:
        raise ModelError(f'Require 1..{maximum} rows')
    for r in x:
        exact_dict(r, keys, 'row')
    return x


def label(x: Any) -> str:
    if not isinstance(x, str) or not x.strip() or len(x.encode('utf8')) > 96:
        raise ModelError('Invalid empty/long identifier')
    return x


def _fmt(v: F) -> str:
    return str(v)


def longitudinal_gformula(spec: dict) -> dict:
    """Exact two-decision g-formula for *stipulated* binary L1 models.

    The parameters are *interventional* model primitives, not estimates from data.
    Output is conditional on consistency, positivity and sequential exchangeability.
    """
    exact_dict(spec, {'strata', 'compare'}, 'g-formula')
    strata = exact_rows(spec['strata'], {'id','q','p_l1_by_a0','outcome_risks'})
    seen=set(); rows=[]
    for r in strata:
        rid=label(r['id'])
        if rid in seen:raise ModelError('Duplicate baseline stratum')
        seen.add(rid)
        p=exact_dict(r['p_l1_by_a0'], {'0','1'}, 'L1 transition')
        ys=exact_dict(r['outcome_risks'], {f'{a}{b}{l}' for a in range(2) for b in range(2) for l in range(2)}, 'outcome model')
        rows.append((number(r['q'],probability=True),
                     {a:number(p[str(a)],probability=True) for a in range(2)},
                     {k:number(v,probability=True) for k,v in ys.items()}))
    if sum((q for q,p,y in rows),F(0))!=1:raise ModelError('Baseline stratum proportions must sum exactly to 1')
    compare=exact_dict(spec['compare'],{'regime_a','regime_b'}, 'comparison')
    def regime(x):
        if not isinstance(x, list) or len(x)!=2 or any(type(a) is not int or a not in (0,1) for a in x):
            raise ModelError('Regime must be a two-element [0,1] integer list')
        return tuple(x)
    ra, rb = regime(compare['regime_a']),regime(compare['regime_b'])
    risks={}
    for a in range(2):
        for b in range(2):
            risks[f'{a}{b}']=sum((q*((1-p[a])*ys[f'{a}{b}0']+p[a]*ys[f'{a}{b}1']) for q,p,ys in rows),F(0))
    return {
      'schema':'atlas.causal-longitudinal-gformula/1','result':'stipulated_model_calculation',
      'static_regime_risks':{k:_fmt(v) for k,v in risks.items()},
      'regime_a':list(ra),'regime_b':list(rb),'contrast_a_minus_b':_fmt(risks[''.join(map(str,ra))]-risks[''.join(map(str,rb))]),
      'data_origin':'stipulated_binary_transition_and_outcome_probabilities',
      'identification_verified':False,'sample_confidence_interval':None,
      'limitations':['No model fitting or adjustment for observed histories is performed.',
          'Sequential exchangeability, consistency, positivity and outcome/transition model specification must be defended.',
          'Exhaustively enumerates one intermediate binary covariate and two treatment decisions only; not a general longitudinal estimator.']}


def staggered_group_time(spec: dict) -> dict:
    """Descriptive cohort-time difference in changes; not a complete DiD estimator."""
    exact_dict(spec, {'periods','groups','control_policy'}, 'staggered DiD')
    ts=spec['periods']
    if not isinstance(ts,list) or not 3<=len(ts)<=24 or any(type(t)is not int for t in ts) or ts!=sorted(set(ts)):
        raise ModelError('Require 3..24 strictly increasing integer periods')
    policy=spec['control_policy']
    if policy not in {'never','not_yet'}:raise ModelError('control_policy must be never or not_yet')
    rows=exact_rows(spec['groups'], {'id','first_treated','weight','means'}, MAX_COHORTS)
    data=[];seen=set()
    for r in rows:
        k=label(r['id'])
        if k in seen:raise ModelError('Duplicate cohort')
        seen.add(k)
        g=r['first_treated']
        if g is not None and (type(g)is not int or g not in ts or g==ts[0]):
            raise ModelError('Treatment time must follow the first measured period')
        means=exact_dict(r['means'],{str(t) for t in ts},'group-period means')
        data.append((k,g,number(r['weight'],positive=True),{t:number(means[str(t)]) for t in ts}))
    if not any(g is not None for k,g,w,m in data):raise ModelError('At least one treated group required')
    out=[];unavailable=[]
    for k,g,w,m in data:
        if g is None:continue
        prior=ts[ts.index(g)-1]
        for t in ts:
            if t<g:continue
            control=[d for d in data if d[0]!=k and (d[1] is None or (policy=='not_yet' and d[1]>t))]
            if not control:
                unavailable.append({'cohort':k,'period':t,'reason':'no_eligible_untreated_comparison'})
                continue
            wt=sum((z[2] for z in control),F(0))
            cchange=sum((cw*(cm[t]-cm[prior]) for ck,cg,cw,cm in control),F(0))/wt
            contrast=m[t]-m[prior]-cchange
            out.append({'cohort':k,'period':t,'base_period':prior,'comparison_ids':[d[0] for d in control],
                        'observed_difference_in_changes':_fmt(contrast),'is_effect_under_parallel_trends_only':True})
    return {'schema':'atlas.staggered-did-point-contrasts/1','result':'observed_group_time_contrasts',
        'control_policy':policy,'contrasts':out,'unavailable':unavailable,'causal_identification_verified':False,
        'inference':None,'limitations':['Requires no anticipation and plausible group-time parallel trends for a causal ATT(g,t) interpretation.',
         'Input means and group sizes are supplied rather than estimated; no covariate adjustment, inference, censoring adjustment, panel weighting or bootstrap is implemented.',
         'Previously-treated groups are never used as comparison controls.','Avoid interpreting this descriptive tool as the full Callaway–Sant’Anna estimator.']}


def mediation_interventional(spec: dict) -> dict:
    """Two binary exposure/mediator standardizations; not natural cross-world effects."""
    exact_dict(spec,{'mediator_prob','outcome_risk'},'interventional mediation')
    pm=exact_dict(spec['mediator_prob'],{'0','1'},'mediator probability')
    y=exact_dict(spec['outcome_risk'],{'00','01','10','11'},'outcome risk')
    p={a:number(v,probability=True) for a,v in pm.items()}
    mu={k:number(v,probability=True) for k,v in y.items()}
    def v(a,dist):return (1-p[str(dist)])*mu[f'{a}0']+p[str(dist)]*mu[f'{a}1']
    total=v(1,1)-v(0,0)
    direct=v(1,0)-v(0,0)
    indirect=v(1,1)-v(1,0)
    assert total==direct+indirect
    return {'schema':'atlas.interventional-mediation/1','result':'conditional_gformula_illustration',
       'contrast_total':_fmt(total),'interventional_direct_component':_fmt(direct),
       'interventional_indirect_component':_fmt(indirect),'decomposition_exact':True,
       'interpretation':'stochastic mediator-distribution contrast with specified outcome risks, not natural direct/indirect effects',
       'identified_from_observational_data':False,
       'limitations':['No exposure-induced mediator-outcome confounder is represented; identification depends on assumptions and timing.',
       'Does not identify individual natural indirect effects or infer a mediator mechanism from correlations.',
       'All four outcome means and both mediator probabilities are supplied, not learned.']}


def cluster_interference(spec: dict) -> dict:
    """Two-person cluster effects given 4 fully specified assignment outcomes."""
    exact_dict(spec,{'outcomes_by_assignment'}, 'cluster interference')
    d=exact_dict(spec['outcomes_by_assignment'],{'00','01','10','11'},'assignment response model')
    v={}
    for k,arr in d.items():
        if not isinstance(arr,list) or len(arr)!=2:raise ModelError('Each assignment must include exactly two outcomes')
        v[k]=[number(x,probability=True) for x in arr]
    return {'schema':'atlas.cluster-interference/1','result':'stipulated_two_person_potential_outcomes',
       'direct_effect_focal0_neighbor0':_fmt(v['10'][0]-v['00'][0]),
       'direct_effect_focal0_neighbor1':_fmt(v['11'][0]-v['01'][0]),
       'spillover_focal0_own0':_fmt(v['01'][0]-v['00'][0]),
       'spillover_focal1_own0':_fmt(v['10'][1]-v['00'][1]),
       'no_interference_assumption_verified':False,
       'limitations':['The full assignment map is specified, not inferred.',
        'Interference outside the two-person cluster, selection, randomization and sampling variability are not represented.',
        'The ordinary no-interference potential-outcome simplification cannot be assumed if spillovers are nonzero.']}


def transport_strata(spec: dict) -> dict:
    """Standardize source stratum response functions to a target distribution."""
    exact_dict(spec,{'strata'},'transport')
    rows=exact_rows(spec['strata'],{'id','source_share','target_share','source_mean_0','source_mean_1'})
    seen=set();r=[]
    for x in rows:
        k=label(x['id'])
        if k in seen:raise ModelError('Duplicate stratum')
        seen.add(k)
        ss=number(x['source_share'],probability=True);tt=number(x['target_share'],probability=True)
        if tt>0 and ss==0:raise ModelError('Positive target mass without source support: '+k)
        r.append((ss,tt,number(x['source_mean_0'],probability=True),number(x['source_mean_1'],probability=True)))
    if sum((a for a,b,c,d in r),F(0))!=1 or sum((b for a,b,c,d in r),F(0))!=1:
        raise ModelError('Source and target shares must each sum exactly to one')
    source=sum((ss*(u1-u0) for ss,tt,u0,u1 in r),F(0))
    target=sum((tt*(u1-u0) for ss,tt,u0,u1 in r),F(0))
    return {'schema':'atlas.causal-transport-by-strata/1','result':'conditional_standardization',
      'source_contrast':_fmt(source),'target_contrast':_fmt(target),
      'strata_supported':len([1 for ss,tt,u0,u1 in r if tt>0]),
      'transport_assumptions_verified':False,
      'limitations':['The per-stratum treatment response functions must be identifiable in source and invariant across settings conditional on specified strata.',
          'Observed source associations are not automatically causal response functions.',
          'This is finite stratum reweighting, not a complete graphical transportability algorithm or inference procedure.']}


def independent_binary_contrast(spec: dict) -> dict:
    """Approximate descriptive risk difference interval from independent binomials."""
    exact_dict(spec,{'group_0','group_1','confidence'},'binomial contrast')
    groups=[]
    for name in ('group_0','group_1'):
        r=exact_dict(spec[name],{'successes','total'},name)
        x,n=r['successes'],r['total']
        if type(x)is not int or type(n)is not int or not(0<=x<=n and 30<=n<=10**9):raise ModelError('Integer counts, at least 30 per group, required')
        p=F(x,n)
        if not F(1,20)<p<F(19,20):raise ModelError('Near-boundary event proportion; use appropriate non-Wald method')
        groups.append((p,n))
    conf=float(number(spec['confidence'],probability=True))
    if not 0.8<=conf<=0.999:raise ModelError('Confidence nominal level must be 0.8 through 0.999')
    p0,n0=groups[0];p1,n1=groups[1];diff=p1-p0
    z=NormalDist().inv_cdf((1+conf)/2)
    variance=float(p0*(1-p0)/n0+p1*(1-p1)/n1)
    se=variance**0.5
    return {'schema':'atlas.independent-binomial-risk-difference/1','result':'approximate_descriptive_interval',
      'difference':_fmt(diff),'difference_decimal':float(diff),'standard_error':se,'z_multiplier':z,
      'nominal_confidence':conf,'normal_interval':[float(diff)-z*se,float(diff)+z*se],
      'causal_identification_verified':False,
      'limitations':['Assumes independent observations within and between groups; no clustering or observational confounding correction.',
        'Large-sample Wald approximation can undercover, especially near limits; interval can extend beyond the natural difference range.',
        'A confidence interval describes sample variability under its assumptions, not identification or a causal claim.']}


def berkeley_admissions(rows: list[dict]) -> dict:
    """Descriptive, actual published aggregate counts; never a causal sex effect."""
    exact_rows(rows,{'department','male_admitted','male_rejected','female_admitted','female_rejected'},6)
    if sorted(r['department'] for r in rows)!=list('ABCDEF'):
        raise ModelError('All six R UCBAdmissions departments must appear once')
    parsed=[]
    for r in rows:
        xs=[r[k] for k in ('male_admitted','male_rejected','female_admitted','female_rejected')]
        if any(type(x)is not int or not 0<=x<=10**7 for x in xs):raise ModelError('Counts must be nonnegative integers')
        ma,mr,fa,fr=xs
        if ma+mr==0 or fa+fr==0:raise ModelError('Each comparison arm needs observations')
        parsed.append((r['department'],ma,mr,fa,fr))
    mt=sum((ma+mr for k,ma,mr,fa,fr in parsed));ft=sum((fa+fr for k,ma,mr,fa,fr in parsed))
    mad=sum((ma for k,ma,mr,fa,fr in parsed));fad=sum((fa for k,ma,mr,fa,fr in parsed))
    pooled={k:F(ma+mr+fa+fr,mt+ft) for k,ma,mr,fa,fr in parsed}
    mstd=sum((pooled[k]*F(ma,ma+mr) for k,ma,mr,fa,fr in parsed),F(0))
    fstd=sum((pooled[k]*F(fa,fa+fr) for k,ma,mr,fa,fr in parsed),F(0))
    return {'schema':'atlas.ucb-admissions-descriptive/1','result':'observed_aggregate_table_descriptive',
       'total_applications':mt+ft,
       'male':{'total':mt,'admitted':mad,'crude_rate':_fmt(F(mad,mt)),'department_standardized_rate':_fmt(mstd)},
       'female':{'total':ft,'admitted':fad,'crude_rate':_fmt(F(fad,ft)),'department_standardized_rate':_fmt(fstd)},
       'crude_female_minus_male':_fmt(F(fad,ft)-F(mad,mt)),
       'department_standardized_female_minus_male':_fmt(fstd-mstd),
       'target':'pooled six-department application mix',
       'causal_identification_verified':False,'data_origin':'published historical aggregated application counts',
       'limitations':['Association after standardization is not a causal intervention effect of sex or a complete discrimination assessment.',
        'Department selection can be associated with applicant characteristics and other unobserved processes.',
        'The dataset covers the six largest departments, not all applications, and is observational/historical.',
        'These counts are an attributed transcription of public R documentation; original publisher table bytes are not mirrored.']}
