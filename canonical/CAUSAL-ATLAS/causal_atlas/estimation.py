"""Exact, bounded teaching estimators using supplied nuisance predictions.

No propensity or outcome models are fitted here. No interval, hidden-confounding
check, randomized-design authentication or empirical causal verdict is produced.
All rational results are serialized as strings; no weights are silently clipped.
"""
from __future__ import annotations
from fractions import Fraction as F
from typing import Any, Mapping
from .models import ModelError, rational

MAX_ROWS = 10000


def _prob(value: Any, *, open_interval: bool = False) -> F:
    v = rational(value)
    if not (0 < v < 1 if open_interval else 0 <= v <= 1):
        raise ModelError('Probability outside ' + ('(0,1)' if open_interval else '[0,1]'))
    return v


def _name(value: Any) -> str:
    if not isinstance(value, str) or not value.strip() or len(value.encode()) > 128:
        raise ModelError('A nonblank name of at most 128 UTF-8 bytes is required')
    return value


def _number(value: Any) -> F:
    v = rational(value)
    if abs(v) > 10**12 or v.denominator.bit_length() > 128:
        raise ModelError('Number exceeds bounded teaching-tool precision or magnitude')
    return v


def _table(value: Any, keys: set[str], maximum: int) -> list[dict]:
    if not isinstance(value, list) or not 1 <= len(value) <= maximum:
        raise ModelError(f'Expected 1..{maximum} rows')
    if any(not isinstance(r, dict) or set(r) != keys for r in value):
        raise ModelError('Rows must have exactly these fields: ' + ', '.join(sorted(keys)))
    return value


def _sum(xs):
    return sum(xs, F(0))


def _summary_weights(weights: list[F]) -> dict:
    total = _sum(weights)
    return {'observed_rows':len(weights), 'sum_weights':str(total),
            'effective_sample_size':str(total*total/_sum(w*w for w in weights)),
            'max_weight':str(max(weights)), 'largest_normalized_weight':str(max(weights)/total),
            'interpretation':'weight concentration diagnostic, not a count of independent information or a causal validation'}


def supplied_estimates(rows: list[dict], *, nuisance_origin: str) -> dict:
    """Compute OR, HT, Hajek, and residual-form AIPW for a sample ATE target.

    Rows are individual units, not aggregated counts. `x` is one declared numeric
    baseline covariate used ONLY for a balance diagnostic. Other adjustments must
    be documented upstream. Both arms and 0 < e < 1 are required.
    """
    _table(rows, {'id','a','y','e','m0','m1','x'}, MAX_ROWS)
    if nuisance_origin not in {'known_design','external_predictions','out_of_fold','in_sample','synthetic_oracle'}:
        raise ModelError('Declare nuisance_origin: known_design, external_predictions, out_of_fold, in_sample or synthetic_oracle')
    ids = [_name(r['id']) for r in rows]
    if len(set(ids)) != len(ids):
        raise ModelError('Duplicate unit ID; cluster/longitudinal rows need a different design')
    parsed=[]
    for r in rows:
        if type(r['a']) is not int or r['a'] not in (0,1):
            raise ModelError('Treatment must be integer 0 or 1, not boolean')
        parsed.append((r['a'],_number(r['y']),_prob(r['e'],open_interval=True),
                       _number(r['m0']),_number(r['m1']),_number(r['x'])))
    if {r[0] for r in parsed} != {0,1}:
        raise ModelError('Both observed treatment arms are required')
    n=len(parsed); weights={0:[],1:[]};weighted_y={0:F(0),1:F(0)};xw={0:F(0),1:F(0)}
    crude={0:[],1:[]};base_x={0:[],1:[]};scores=[]
    for a,y,e,m0,m1,x in parsed:
        w=1/e if a else 1/(1-e)
        weights[a].append(w);weighted_y[a]+=w*y;xw[a]+=w*x;crude[a].append(y);base_x[a].append(x)
        scores.append(m1-m0+a/e*(y-m1)-(1-a)/(1-e)*(y-m0))
    wt={a:_sum(weights[a]) for a in (0,1)}
    estimates={'crude_difference':_sum(crude[1])/len(crude[1])-_sum(crude[0])/len(crude[0]),
               'outcome_regression':_sum(m1-m0 for a,y,e,m0,m1,x in parsed)/n,
               'ipw_horvitz_thompson':(weighted_y[1]-weighted_y[0])/n,
               'ipw_hajek':weighted_y[1]/wt[1]-weighted_y[0]/wt[0],
               'aipw':_sum(scores)/n}
    return {'schema':'atlas.causal-estimates/1','result':'computed_conditional_on_inputs',
            'target':'sample-covariate-distribution average contrast, binary point exposure',
            'nuisance_origin':nuisance_origin,'observed_rows':n,
            'estimates':{k:str(v) for k,v in estimates.items()},
            'diagnostics':{'arm_weights':{str(a):_summary_weights(weights[a]) for a in (0,1)},
              'minimum_supplied_propensity':str(min(r[2] for r in parsed)),
              'maximum_supplied_propensity':str(max(r[2] for r in parsed)),
              'declared_covariate_mean_difference_unweighted':str(_sum(base_x[1])/len(base_x[1])-_sum(base_x[0])/len(base_x[0])),
              'declared_covariate_mean_difference_weighted':str(xw[1]/wt[1]-xw[0]/wt[0]),
              'weights_clipped':False,'balance_does_not_test_unmeasured_confounding':True},
            'causal_identification_verified':False,'confidence_interval':None,
            'limitations':['Predictions supplied, not fitted or verified by this tool.',
                'Consistency, sufficient baseline adjustment, positivity and suitable sampling must be justified separately.',
                'Weight ESS and one covariate mean are incomplete diagnostics.',
                'No nuisance-fitting, clustering, longitudinal, or sampling-uncertainty correction is implemented.',
                'Double robustness is a conditional population/asymptotic property, not exact sample correctness.']}


def population_comparison(strata: list[dict]) -> dict:
    """Exactly evaluate expectations in a FULLY STIPULATED synthetic population.

    q sums to one; e is the declared generating propensity; g is a deliberately
    chosen working propensity. mu0/mu1 and m0/m1 are true/working binary means.
    This routine is not an estimator from actual observations.
    """
    _table(strata,{'name','q','e','mu0','mu1','g','m0','m1'},128)
    names=[_name(r['name']) for r in strata]
    if len(set(names))!=len(names):raise ModelError('Duplicate stratum')
    ps=[]
    for r in strata:
        q=_prob(r['q']);e=_prob(r['e'],open_interval=True);g=_prob(r['g'],open_interval=True)
        if q<=0:raise ModelError('Zero-mass strata must be explicitly excluded, not included')
        ps.append((q,e,_prob(r['mu0']),_prob(r['mu1']),g,_prob(r['m0']),_prob(r['m1'])))
    if _sum(r[0] for r in ps)!=1:raise ModelError('Target masses must sum exactly to one')
    truth=_sum(q*(u1-u0) for q,e,u0,u1,g,m0,m1 in ps)
    p1=_sum(q*e for q,e,u0,u1,g,m0,m1 in ps)
    crude1=_sum(q*e*u1 for q,e,u0,u1,g,m0,m1 in ps)/p1
    crude0=_sum(q*(1-e)*u0 for q,e,u0,u1,g,m0,m1 in ps)/(1-p1)
    ht1=_sum(q*e*u1/g for q,e,u0,u1,g,m0,m1 in ps)
    ht0=_sum(q*(1-e)*u0/(1-g) for q,e,u0,u1,g,m0,m1 in ps)
    a=_sum(q*(m1-m0+e/g*(u1-m1)-(1-e)/(1-g)*(u0-m0)) for q,e,u0,u1,g,m0,m1 in ps)
    bias=_sum(q*(e-g)*((u1-m1)/g+(u0-m0)/(1-g)) for q,e,u0,u1,g,m0,m1 in ps)
    assert a-truth==bias
    return {'schema':'atlas.causal-population-comparison/1','data_origin':'synthetic_stipulated_population',
      'true_ate':str(truth),'crude_difference':str(crude1-crude0),
      'outcome_regression':str(_sum(q*(m1-m0) for q,e,u0,u1,g,m0,m1 in ps)),
      'ipw_horvitz_thompson':str(ht1-ht0),
      'ipw_hajek':str(ht1/_sum(q*e/g for q,e,u0,u1,g,m0,m1 in ps)-ht0/_sum(q*(1-e)/(1-g) for q,e,u0,u1,g,m0,m1 in ps)),
      'aipw':str(a),'aipw_bias':str(bias),'algebraic_bias_identity_checked':True,
      'propensity_exact':all(e==g for q,e,u0,u1,g,m0,m1 in ps),
      'outcome_means_exact':all(u0==m0 and u1==m1 for q,e,u0,u1,g,m0,m1 in ps),
      'limitation':'Expectation over a completely declared model; not a fitted-data, sampling or empirical validation result.'}


def binary_missing_bounds(arms: dict) -> dict:
    """Sharp arithmetic bounds for binary arm risks from fully counted populations.

    No MAR, missing-zero or treatment exchangeability assumption is invented.
    These are bounds, not confidence intervals; causal interpretation is external.
    """
    if not isinstance(arms,dict) or set(arms)!={'0','1'}:raise ModelError('Expected arms 0 and 1')
    bounds={}
    for a,d in arms.items():
        if not isinstance(d,dict) or set(d)!={'total','observed','successes'}:raise ModelError('Expected total, observed and successes')
        if any(type(x)is not int for x in d.values()):raise ModelError('Counts must be integers, not booleans')
        n,o,s=d['total'],d['observed'],d['successes']
        if not 0<=s<=o<=n or not 1<=n<=10**9:raise ModelError('Counts outside 0 <= successes <= observed <= total')
        bounds[a]=(F(s,n),F(s+n-o,n))
    return {'result':'bounded_not_identified','data_interpretation':'binary arm risks for supplied counted units',
      'risks':{a:[str(lo),str(hi)] for a,(lo,hi) in bounds.items()},
      'difference_bounds':[str(bounds['1'][0]-bounds['0'][1]),str(bounds['1'][1]-bounds['0'][0])],
      'is_confidence_interval':False,'causal_identification_verified':False,
      'limitations':['Unknown binary outcomes may take either value.', 'Does not correct treatment confounding or sampling uncertainty.']}


def two_period_contrast(treated_pre,treated_post,control_pre,control_post,*,untreated_trend_difference=0):
    """A four-mean contrast and an explicit sensitivity scenario, not a DiD study."""
    tp,ta,cp,ca,d=map(_number,[treated_pre,treated_post,control_pre,control_post,untreated_trend_difference])
    contrast=(ta-tp)-(ca-cp)
    return {'observed_two_period_contrast':str(contrast),'assumed_untreated_trend_difference':str(d),
      'effect_under_stated_trend_scenario':str(contrast-d),
      'identification_verified':False,'sampling_interval':None,
      'limitations':['Trend difference is assumed, not estimated from the four means.',
        'Requires no anticipation and a defensible untreated comparison for causal interpretation.',
        'Not a staggered-adoption estimator, time-series model, or clustered inference procedure.']}
