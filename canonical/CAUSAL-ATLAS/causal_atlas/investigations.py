"""Executable original investigations, never external observational data."""
from copy import deepcopy
from fractions import Fraction as F
from .models import DAG, BinaryModel
from .estimation import population_comparison, supplied_estimates, binary_missing_bounds, two_period_contrast


def process_strata():
    return [dict(name='easy',q='1/2',e='1/5',mu0='4/5',mu1='9/10',g='1/5',m0='4/5',m1='9/10'),
            dict(name='difficult',q='1/2',e='4/5',mu0='1/5',mu1='3/10',g='4/5',m0='1/5',m1='3/10')]


def process_rows():
    # Original v0.1 count table, expanded deterministically to 200 synthetic units.
    rows=[]
    for difficulty,a,n,s,e,m0,m1 in [(0,0,80,64,'1/5','4/5','9/10'),(0,1,20,18,'1/5','4/5','9/10'),
                                    (1,0,20,4,'4/5','1/5','3/10'),(1,1,80,24,'4/5','1/5','3/10')]:
        for i in range(n):rows.append(dict(id=f'{difficulty}-{a}-{i}',a=a,y=int(i<s),e=e,m0=m0,m1=m1,x=difficulty))
    return rows


def investigations():
    cases=[]
    def put(id,result,expected,explanation):
        checks={k:result[k]==v for k,v in expected.items()}
        cases.append(dict(id=id,data_origin='original_constructed_example',result=result,expected=expected,
                          checks=checks,passed=all(checks.values()),interpretation=explanation))
    for name,wrong_g,wrong_m in [('both_correct',False,False),('propensity_only_correct',False,True),
                                ('outcome_only_correct',True,False),('both_wrong',True,True)]:
        s=process_strata()
        for r in s:
            if wrong_g:r['g']='1/2'
            if wrong_m:r['m0']='1/2';r['m1']='3/5'
        result=population_comparison(s)
        put(name,result,{'true_ate':'1/10','aipw':'-13/50' if wrong_g and wrong_m else '1/10'},
            'Exact synthetic population expectation. One correct nuisance family removes this model bias; two wrong families can fail.')
    # Holding means constant while changing target weights changes the estimand.
    s=process_strata();s[0].update(mu1='9/10',mu0='4/5');s[1].update(mu1='3/5',mu0='1/5')
    s[0]['q']='4/5';s[1]['q']='1/5'
    for r in s:r['m0']=r['mu0'];r['m1']=r['mu1']
    put('target_easy_heavy',population_comparison(s),{'true_ate':'4/25'},'Effect heterogeneity plus target composition changes the average being asked for.')
    s[0]['q']='1/5';s[1]['q']='4/5'
    put('target_difficult_heavy',population_comparison(s),{'true_ate':'17/50'},'Same conditional effects, different target: not a contradiction.')
    sampled=supplied_estimates(process_rows(),nuisance_origin='synthetic_oracle')
    put('supplied_models_on_constructed_counts',sampled['estimates'],{'crude_difference':'-13/50','ipw_hajek':'1/10','aipw':'1/10'},
        'Exact agreement here follows from deliberately chosen counts; arbitrary finite samples need not agree.')
    missing=binary_missing_bounds({'1':dict(total=100,observed=60,successes=48),'0':dict(total=100,observed=90,successes=54)})
    put('missing_outcomes_bounds',missing,{'difference_bounds':['-4/25','17/50']},
        'Observed-case pass rates 0.80 and 0.60 do not determine the full-cohort difference; admissible assignments can reverse its sign.')
    did=two_period_contrast('4/5','9/10','7/10','3/4')
    put('parallel_trend_scenario',did,{'observed_two_period_contrast':'1/20','effect_under_stated_trend_scenario':'1/20'},
        'The contrast is causal only under an appropriate untreated-trend assumption and design conditions.')
    did=two_period_contrast('4/5','9/10','7/10','3/4',untreated_trend_difference='2/25')
    put('trend_violation_scenario',did,{'observed_two_period_contrast':'1/20','effect_under_stated_trend_scenario':'-3/100'},
        'The identical observations permit a harmful effect under this explicit untreated-trend difference.')
    rows=[dict(id=str(i),a=1 if i<3 else 0,y=1 if i==0 else 0,e='1/1000' if i==0 else '1/2',m0=0,m1=0,x=0) for i in range(6)]
    r=supplied_estimates(rows,nuisance_origin='external_predictions')
    put('extreme_weight_dominance',r['diagnostics']['arm_weights']['1'],{'largest_normalized_weight':'250/251','effective_sample_size':'126002/125001'},
        'Three treated observations have weight-concentration ESS near one; finite positive propensities alone do not mean a stable estimate.')
    # The SAME observed joint law can come from different intervention mechanisms.
    ma=BinaryModel(DAG(('U','A','Y'),(('U','A'),('U','Y'))),
                   {'U':{'':'1/2'},'A':{'0':0,'1':1},'Y':{'0':0,'1':1}})
    mb=BinaryModel(DAG(('A','Y'),(('A','Y'),)),{'A':{'':'1/2'},'Y':{'0':0,'1':1}})
    equal=all(ma.probability({'A':a,'Y':y})==mb.probability({'A':a,'Y':y}) for a in (0,1) for y in (0,1))
    out={'same_observed_joint':equal,
         'observed_difference':str(ma.probability({'Y':1},given={'A':1})-ma.probability({'Y':1},given={'A':0})),
         'model_A_effect':str(ma.probability({'Y':1},do={'A':1})-ma.probability({'Y':1},do={'A':0})),
         'model_B_effect':str(mb.probability({'Y':1},do={'A':1})-mb.probability({'Y':1},do={'A':0}))}
    put('observational_ambiguity',out,{'same_observed_joint':True,'observed_difference':'1','model_A_effect':'0','model_B_effect':'1'},
        'Two constructed mechanisms agree on every observed A,Y cell but disagree after intervention. Additional information is necessary.')
    return {'schema':'atlas.causal-investigations/1','result':'passed' if all(c['passed'] for c in cases) else 'failed',
            'cases':cases,'physical_observations':False,'independent_scientific_review':False,
            'data_origin':'synthetic_only','causal_discovery':False}
