"""Authored finite-model and boundary-regression cases; no real observations."""
from fractions import Fraction as F
from .models import ModelError
from .quasi import (iv_population, wald_summary, exclusion_sensitivity,
                    local_linear_jump, fuzzy_local_ratio, bandwidth_sensitivity)


def encouragement_types():
    return [
        dict(name='never',mass='3/10',d0=0,d1=0,y0='3/5',y1='1/2',direct_z=0),
        dict(name='always',mass='1/5',d0=1,d1=1,y0='1/5',y1='3/10',direct_z=0),
        dict(name='complier',mass='1/2',d0=0,d1=1,y0='2/5',y1='7/10',direct_z=0)]


def linear_rd_rows():
    return [{'id':f'r{i}','x':x,'y':1+2*x+(5-3*x if x>=0 else 0)}
            for i,x in enumerate([-3,-2,-1,0,1,2,3])]


def curved_rd_rows():
    xs=[F(i,4) for i in range(-12,13) if i]
    return [{'id':f'r{i}','x':str(x),
             'y':str(2+x+(F(1,10) if x<0 else F(1,2))*x*x+(5 if x>0 else 0))}
            for i,x in enumerate(xs)]


def fuzzy_rd_rows(*, equal_uptake=False):
    out=[]
    for x in [-3,-2,-1,0,1,2,3]:
        for j in range(10):
            d=int(j<(2 if x<0 or equal_uptake else 7))
            out.append(dict(id=f'{x}:{j}',x=x,y=str(2+F(x,10)+3*d),d=d))
    return out


def quasi_casebook():
    cases=[]
    def add(cid, result, expected, **meta):
        checks={key:result[key]==val for key,val in expected.items()}
        cases.append({'id':cid,'origin':'synthetic_constructed','result':result,
                      'expected':expected,'checks':checks,'passed':all(checks.values()),**meta})
    good=iv_population(encouragement_types())
    add('iv-local-not-population',good,{'first_stage':'1/2','reduced_form':'3/20',
        'ratio':'3/10','complier_effect':'3/10','population_ate':'7/50'},
        lesson='A valid local complier effect differs from the whole-population effect in this fully stipulated population.')
    types=encouragement_types()
    for t in types:t['direct_z']='1/20'
    add('iv-exclusion-failure',iv_population(types),{'ratio':'2/5','complier_effect':'3/10',
        'exclusion_in_declared_model':False},lesson='Encouragement directly changes outcomes as well as uptake.')
    defiers=[dict(name='complier',mass='2/5',d0=0,d1=1,y0=0,y1='1/10',direct_z=0),
             dict(name='defier',mass='3/10',d0=1,d1=0,y0=0,y1='9/10',direct_z=0),
             dict(name='never',mass='3/10',d0=0,d1=0,y0=0,y1='1/5',direct_z=0)]
    add('iv-monotonicity-failure',iv_population(defiers),{'ratio':'-23/10','population_ate':'37/100',
        'monotone_in_declared_model':False},lesson='Every type benefits, but the signed ratio is negative when defiers violate monotonicity.')
    weak=dict(y_z0='1/5',y_z1='2003/10000',d_z0='1/5',d_z1='201/1000',
              minimum_first_stage='1/200',data_origin='synthetic_constructed')
    add('iv-small-denominator-refused',wald_summary(**weak),{'result':'unresolved_first_stage','ratio':None})
    ordinary=wald_summary(**dict(weak,minimum_first_stage=0))
    perturbed=wald_summary(**dict(weak,y_z1='2013/10000',minimum_first_stage=0))
    add('iv-small-denominator-amplification',{'initial_ratio':ordinary['ratio'],
        'perturbed_ratio':perturbed['ratio']},{'initial_ratio':'3/10','perturbed_ratio':'13/10'},
        lesson='An outcome-contrast perturbation of 0.001 moves the ratio by one; this is not a statistical weak-IV test.')
    add('iv-direct-effect-sensitivity',exclusion_sensitivity(reduced_form='1/5',first_stage='1/2',
        direct_lower=0,direct_upper='1/20',minimum_first_stage=0,data_origin='synthetic_constructed'),
        {'effect_scenario_bounds':['3/10','2/5'],'is_confidence_interval':False})
    fit=local_linear_jump(linear_rd_rows(),cutoff=0,bandwidth=4,kernel='triangular',data_origin='synthetic_constructed')
    add('sharp-rd-piecewise-linear',fit,{'jump':'5'},
        lesson='Different left/right slopes, with an exactly specified jump of five.')
    add('same-cutoff-two-mechanisms',{'observed_jump':fit['jump'],
        'training_effect_world_A':5,'training_effect_world_B':0,
        'coincident_policy_effect_world_B':5,'observable_tables_identical':True},
        {'observed_jump':'5','observable_tables_identical':True},
        lesson='One world attributes the jump to training; another to a second policy with the same assignment rule. The observed table alone cannot distinguish them.')
    sensitivity=bandwidth_sensitivity(curved_rd_rows(),cutoff=0,bandwidths=[1,2,4],
                                     kernel='triangular',data_origin='synthetic_constructed')
    bias=[abs(F(r['jump'])-5) for r in sensitivity['results']]
    add('rd-curvature-bandwidth',{'grid':sensitivity['results'],
        'known_limit_jump':'5','bias_increases_on_this_grid':bias[0]<bias[1]<bias[2]},
        {'known_limit_jump':'5','bias_increases_on_this_grid':True},
        lesson='Only a chosen synthetic curvature case; no bandwidth is selected for the user and no universal monotone-bias rule is claimed.')
    add('fuzzy-rd-imperfect-uptake',fuzzy_local_ratio(fuzzy_rd_rows(),cutoff=0,bandwidth=4,
        kernel='triangular',minimum_first_stage=0,data_origin='synthetic_constructed'),
        {'first_stage':'1/2','reduced_form':'3/2','ratio':'3'})
    add('fuzzy-rd-no-uptake-change',fuzzy_local_ratio(fuzzy_rd_rows(equal_uptake=True),cutoff=0,bandwidth=4,
        kernel='triangular',minimum_first_stage=0,data_origin='synthetic_constructed'),
        {'result':'unresolved_first_stage','ratio':None})
    sparse=[dict(id=str(i),x=-1 if i<3 else 1,y=i) for i in range(6)]
    try:local_linear_jump(sparse,cutoff=0,bandwidth=2,kernel='uniform',data_origin='synthetic_constructed');refused=False
    except ModelError:refused=True
    add('rd-repeated-score-insufficient',{'refused':refused},{'refused':True},
        lesson='Many observations at one score per side do not identify two separate slopes.')
    return {'schema':'atlas.quasi-casebook/1','result':'passed' if all(c['passed'] for c in cases) else 'failed',
            'cases':cases,'actual_observations':False,'independent_human_review':False,
            'empirical_design_validated':False,'sampling_inference_implemented':False}
