# Public derivative redaction: ucb_admissions_redistribution_unresolved
"""Small transparent regression cases for declared causal assumptions."""
from .advanced import (longitudinal_gformula,staggered_group_time,mediation_interventional,
                       cluster_interference,transport_strata,independent_binary_contrast,berkeley_admissions)
from .models import ModelError
CASES = {'longitudinal': {'strata': [{'id': 'one_baseline_group', 'q': '1', 'p_l1_by_a0': {'0': '1/5', '1': '3/5'}, 'outcome_risks': {'000': '1/10', '001': '1/5', '010': '3/10', '011': '2/5', '100': '1/5', '101': '3/10', '110': '2/5', '111': '1/2'}}], 'compare': {'regime_a': [1, 1], 'regime_b': [0, 0]}}, 'staggered_did': {'periods': [0, 1, 2], 'groups': [{'id': 'never', 'first_treated': None, 'weight': '1', 'means': {'0': '0', '1': '1', '2': '2'}}, {'id': 'early', 'first_treated': 1, 'weight': '1', 'means': {'0': '0', '1': '3', '2': '5'}}, {'id': 'late', 'first_treated': 2, 'weight': '1', 'means': {'0': '1', '1': '2', '2': '6'}}], 'control_policy': 'not_yet'}, 'mediation': {'mediator_prob': {'0': '1/5', '1': '3/5'}, 'outcome_risk': {'00': '1/10', '01': '3/10', '10': '1/5', '11': '1/2'}}, 'interference': {'outcomes_by_assignment': {'00': ['1/10', '1/10'], '01': ['3/10', '2/5'], '10': ['2/5', '3/10'], '11': ['3/5', '3/5']}}, 'transport': {'strata': [{'id': 'easy', 'source_share': '3/4', 'target_share': '1/4', 'source_mean_0': '1/5', 'source_mean_1': '3/10'}, {'id': 'difficult', 'source_share': '1/4', 'target_share': '3/4', 'source_mean_0': '1/10', 'source_mean_1': '2/5'}]}, 'binomial_interval': {'group_0': {'successes': 60, 'total': 100}, 'group_1': {'successes': 75, 'total': 100}, 'confidence': '0.95'}, 'ucb_admissions': None}
FUNCTIONS={'longitudinal':longitudinal_gformula,'staggered_did':staggered_group_time,
           'mediation':mediation_interventional,'interference':cluster_interference,
           'transport':transport_strata,'binomial_interval':independent_binary_contrast,
           'ucb_admissions':berkeley_admissions}
def advanced_casebook():
    results=[]
    for key,spec in CASES.items():
        if spec is None:
            results.append({'id':key,'result':{'status':'unavailable_pending_dataset_redistribution_clearance','reason':'ucb_admissions_redistribution_unresolved'}})
            continue
        result=FUNCTIONS[key](spec)
        results.append({'id':key,'result':result})
    return {'schema':'atlas.causal-advanced-casebook/1','result':'partial_public_derivative','cases':results,
            'historical_public_data':[],
            'causal_effects_claimed_from_real_data':False,
            'scientific_human_review':False}
