"""Authored failure modes for Agent Atlas 0.4. No live agent invocation."""
from .learning_science import (audit_artifact_proof,paired_learning_audit,
                               compare_label_panels,memory_candidate_review)
from .trace_science import MAST_CODES

def proof_fixture(**updates):
    d={'task_id':'task-A','goal_revision':'a'*64,'observed_goal_revision':'a'*64,
        'parent_dispatch_id':'dispatch-A','worker_receipt_dispatch_id':'dispatch-A',
        'worker_reported_complete':True,'operator_stopped':False,'side_effect_state':'none',
        'expected_artifact_sha256':'b'*64,'observed_artifact_sha256':'b'*64,
        'evaluator_revision':'c'*64,'evaluator_state':'reported_pass',
        'evidence_origin':'reported_host_observation'}
    d.update(updates);return d

def experiment_fixture():
    scores=[('one',False,True),('two',False,True),('three',False,True),
            ('four',True,False),('five',True,True),('six',False,False)]
    return {'experiment_id':'expt-1','baseline_revision':'a'*64,'candidate_revision':'b'*64,
            'evaluator_revision':'e'*64,'candidate_precommitted':True,
            'train_task_ids':['train-1'],
            'rows':[{'task_id':name,'split':'evaluation','task_revision':'f'*64,'evaluator_revision':'e'*64,
                    'baseline_pass':a,'candidate_pass':b} for name,a,b in scores]}

def annotations_fixture():
    zeros={key:0 for key in MAST_CODES}
    m1=dict(zeros);a1=dict(zeros);m1['3.1']=1;a1['3.1']=1
    m2=dict(zeros);a2=dict(zeros);m2['3.1']=1;a2['3.1']=0
    m3=dict(zeros);a3=dict(zeros);m3['3.1']=None;a3['3.1']=1
    return [{'item_id':'case-1','model_labels':m1,'annotator_labels':a1},
            {'item_id':'case-2','model_labels':m2,'annotator_labels':a2},
            {'item_id':'case-3','model_labels':m3,'annotator_labels':a3}]

def memory_fixture():
    return [
    {'memory_id':'m01','claim_revision':'a'*64,'scope_id':'run1','supporting_source_ids':['e1'],
     'contradicting_source_ids':[],'evaluation_state':'reported_pass','candidate_state':'tested','expiry_state':'current'},
    {'memory_id':'m02','claim_revision':'b'*64,'scope_id':'run1','supporting_source_ids':['e1'],
     'contradicting_source_ids':['e2'],'evaluation_state':'reported_pass','candidate_state':'tested','expiry_state':'current'},
    {'memory_id':'m03','claim_revision':'c'*64,'scope_id':'run1','supporting_source_ids':['e3'],
     'contradicting_source_ids':[],'evaluation_state':'reported_fail','candidate_state':'tested','expiry_state':'current'},
    {'memory_id':'m04','claim_revision':'d'*64,'scope_id':'run1','supporting_source_ids':['e4'],
     'contradicting_source_ids':[],'evaluation_state':'reported_pass','candidate_state':'tested','expiry_state':'expired'}]

def casebook_v04():
    cases=[]
    def add(name,calc,success):
        cases.append({'id':name,'result':calc,'passed':success,'origin':'author_constructed_offline_fixture'})
    p=audit_artifact_proof(proof_fixture())
    add('structural_hash_not_true_authentication',p,p['decision']=='structurally_eligible_given_trusted_host_facts' and not p['host_authority_authenticated'])
    p=audit_artifact_proof(proof_fixture(parent_dispatch_id='wrong'))
    add('parent_dispatch_conflict',p,p['decision']=='deny_missing_or_mismatched_parent_dispatch')
    p=audit_artifact_proof(proof_fixture(side_effect_state='submitted_unknown',operator_stopped=True))
    add('stop_dominates_uncertain_submission',p,p['decision']=='respect_operator_stop')
    p=audit_artifact_proof(proof_fixture(side_effect_state='submitted_unknown'))
    add('unknown_external_effect_reconciliation',p,p['decision']=='reconcile_external_effect_first')
    p=paired_learning_audit(experiment_fixture())
    add('paired_discordance_not_improvement',p,p['discordant_pairs']==4 and p['one_sided_exact_discordance_p']==5/16 and not p['agent_improvement_demonstrated'])
    e=experiment_fixture();e['rows'][0]['baseline_pass']=None
    p=paired_learning_audit(e)
    add('missing_evaluation_not_failure',p,p['unscored_pairs']==1 and not p['design_requirements_met_on_supplied_metadata'])
    e=experiment_fixture();e['train_task_ids']=['one','train-1']
    p=paired_learning_audit(e)
    add('training_evaluation_contamination_detected',p,p['contaminated_task_ids']==['one'] and not p['design_requirements_met_on_supplied_metadata'])
    p=compare_label_panels(annotations_fixture(),taxonomy_version='MAST-14')
    add('annotation_missingness_not_negative',p,p['per_code']['3.1']['missing']==1 and p['per_code']['3.1']['fp']==1)
    p=memory_candidate_review(memory_fixture())
    answers=[r['decision'] for r in p['decisions']]
    add('contradictions_survive_memory_review',p,answers==['eligible_for_external_review','review_conflicting_evidence','preserve_failed_candidate_do_not_adopt','hold_expired_or_unknown_freshness'])
    return {'schema':'atlas.agent-v04-casebook/1','status':'passed' if all(x['passed'] for x in cases) else 'failed',
        'count':len(cases),'cases':cases,
        'MAST_original_rows_loaded':0,'independently_verified_agent_outcomes':0,
        'real_agent_invocations':0,'persistent_memory_writes':0,'router_changes':False}
