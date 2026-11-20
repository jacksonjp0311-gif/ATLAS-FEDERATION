"""Original synthetic examples. No empirical data or causal discovery claims."""
from .models import DAG, BinaryModel, standardize_binary, ModelError

ROWS=[
    {'stratum':'easy','treatment':0,'n':80,'successes':64},
    {'stratum':'easy','treatment':1,'n':20,'successes':18},
    {'stratum':'hard','treatment':0,'n':20,'successes':4},
    {'stratum':'hard','treatment':1,'n':80,'successes':24}]

def process_model():
    # Y parent order is alphabetic: A, Z. Z=1 is the difficult-job stratum.
    return BinaryModel(DAG(('Z','A','Y'),(('Z','A'),('Z','Y'),('A','Y'))),
        {'Z':{'':'1/2'},'A':{'0':'1/5','1':'4/5'},
         'Y':{'00':'4/5','01':'1/5','10':'9/10','11':'3/10'}})


def casebook():
    model=process_model(); estimates=standardize_binary(ROWS,{'easy':'1/2','hard':'1/2'})
    observed=model.probability({'Y':1},given={'A':1})-model.probability({'Y':1},given={'A':0})
    effect=model.probability({'Y':1},do={'A':1})-model.probability({'Y':1},do={'A':0})
    collider=BinaryModel(DAG(('A','B','C'),(('A','C'),('B','C'))),
                        {'A':{'':'1/2'},'B':{'':'1/2'},'C':{'00':0,'01':1,'10':1,'11':1}})
    chain=DAG(('A','M','Y'),(('A','M'),('M','Y')))
    hidden=DAG(('U','A','Y'),(('U','A'),('U','Y'),('A','Y')))
    missing=[r.copy() for r in ROWS if not(r['stratum']=='hard' and r['treatment']==0)]
    try:
        standardize_binary(missing,{'easy':'1/2','hard':'1/2'})
        support_rejected=False
    except ModelError:support_rejected=True
    results=[
        {'id':'confounded-process','data_origin':'synthetic_constructed_population',
         'crude_difference':str(observed),'standardized_difference':estimates['standardized_difference'],
         'known_model_intervention_difference':str(effect),
         'expected':{'crude_difference':'-13/50','standardized_difference':'1/10'},
         'passed':str(observed)=='-13/50' and str(effect)=='1/10' and estimates['standardized_difference']=='1/10',
         'limitations':['The generating graph and probabilities are stipulated, not learned from factory data.','No sampling uncertainty is estimated.']},
        {'id':'collider-selection','data_origin':'synthetic_finite_model',
         'marginal_A1_given_B1':str(collider.probability({'A':1},given={'B':1})),
         'A1_given_B0_selected':str(collider.probability({'A':1},given={'B':0,'C':1})),
         'A1_given_B1_selected':str(collider.probability({'A':1},given={'B':1,'C':1})),
         'passed':collider.graph.d_separated(['A'],['B']) and not collider.graph.d_separated(['A'],['B'],['C'])
             and collider.probability({'A':1},given={'B':0,'C':1})==1,
         'limitations':['Selection is explicitly defined as logical OR; other mechanisms can produce different magnitudes.']},
        {'id':'mediator-conditioning','data_origin':'synthetic_graph',
         'chain_blocked_by_M':chain.d_separated(['A'],['Y'],['M']),
         'total_effect_backdoor_adjust_M':chain.backdoor('A','Y',['M']),
         'passed':chain.d_separated(['A'],['Y'],['M']) and not chain.backdoor('A','Y',['M'])['valid_under_supplied_graph'],
         'limitations':['Rejecting M for this sufficient total-effect criterion is not a claim about every direct-effect method.']},
        {'id':'missing-treatment-support','data_origin':'synthetic_grouped_counts',
         'missing_positive_target_stratum_rejected':support_rejected,'passed':support_rejected,
         'limitations':['Empty sample cells alone do not distinguish structural impossibility from finite-sample sparsity.']},
        {'id':'unobserved-common-cause','data_origin':'synthetic_graph',
         'observed_adjustment_sets':hidden.minimal_backdoor_sets('A','Y',['A','Y']),
         'passed':hidden.minimal_backdoor_sets('A','Y',['A','Y'])==[],
         'limitations':['No observed back-door set was found; this is not a complete nonidentifiability proof.']}]
    return {'schema':'atlas.causal-casebook/1','result':'passed' if all(r['passed'] for r in results) else 'failed',
            'cases':results,'physical_observations':False,'independent_review':False,'causal_discovery':False}
