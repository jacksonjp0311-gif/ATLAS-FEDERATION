"""Agent v0.4 bounded evidence and eval regression; synthetic fixtures only."""
import copy,math,random,unittest
from agent_atlas.learning_science import (audit_artifact_proof,paired_learning_audit,compare_label_panels,memory_candidate_review)
from agent_atlas.v04_cases import proof_fixture,experiment_fixture,annotations_fixture,memory_fixture,casebook_v04
from agent_atlas.models import AgentModelError
from agent_atlas.trace_science import MAST_CODES

class ProofPacket(unittest.TestCase):
    def check(self,expected,**kwargs):self.assertEqual(audit_artifact_proof(proof_fixture(**kwargs))['decision'],expected)
    def test_structural_pass_is_not_truth(self):
        r=audit_artifact_proof(proof_fixture());self.assertEqual(r['decision'],'structurally_eligible_given_trusted_host_facts')
        self.assertFalse(r['host_authority_authenticated']);self.assertFalse(r['artifact_bytes_rehashed_here']);self.assertFalse(r['semantic_task_success_verified'])
    def test_stop_priority(self):self.check('respect_operator_stop',operator_stopped=True,side_effect_state='submitted_unknown',parent_dispatch_id='wrong')
    def test_side_effect_priority(self):self.check('reconcile_external_effect_first',side_effect_state='submitted_unknown',parent_dispatch_id='wrong')
    def test_missing_dispatch(self):self.check('deny_missing_or_mismatched_parent_dispatch',parent_dispatch_id=None)
    def test_mismatched_dispatch(self):self.check('deny_missing_or_mismatched_parent_dispatch',worker_receipt_dispatch_id='foreign')
    def test_foreign_goal(self):self.check('deny_foreign_goal_revision',observed_goal_revision='d'*64)
    def test_no_observed_hash(self):self.check('require_complete_artifact_evidence',observed_artifact_sha256=None)
    def test_hash_conflict(self):self.check('deny_artifact_hash_mismatch',observed_artifact_sha256='c'*64)
    def test_worker_not_done(self):self.check('await_worker_completion',worker_reported_complete=False)
    def test_evaluator_failed(self):self.check('escalate_evaluator_failure',evaluator_state='reported_fail')
    def test_no_eval(self):self.check('await_evaluator_evidence',evaluator_revision=None)
    def test_eval_pending(self):self.check('await_evaluator_evidence',evaluator_state='pending')
    def test_self_report_is_not_independent(self):self.check('require_independent_host_observation',evidence_origin='worker_self_report')
    def test_extra_fields_rejected(self):
        v=proof_fixture();v['tool_arguments']='send money'
        with self.assertRaises(AgentModelError):audit_artifact_proof(v)
    def test_boolean_guard(self):
        with self.assertRaises(AgentModelError):audit_artifact_proof(proof_fixture(operator_stopped=0))
    def test_hash_guard(self):
        with self.assertRaises(AgentModelError):audit_artifact_proof(proof_fixture(goal_revision='not-a-hash'))
    def test_unknown_side_effect(self):
        with self.assertRaises(AgentModelError):audit_artifact_proof(proof_fixture(side_effect_state='unconfirmed'))

class PairedScientificEvaluation(unittest.TestCase):
    def test_exact_tail(self):
        v=paired_learning_audit(experiment_fixture());self.assertEqual(v['one_sided_exact_discordance_p'],5/16)
        self.assertEqual(v['discordant_pairs'],4);self.assertTrue(v['design_requirements_met_on_supplied_metadata'])
        self.assertFalse(v['agent_improvement_demonstrated'])
    def test_null_not_false(self):
        x=experiment_fixture();x['rows'][0]['candidate_pass']=None
        r=paired_learning_audit(x);self.assertEqual(r['unscored_pairs'],1)
        self.assertEqual(r['paired_outcomes']['unscored'],1)
        self.assertFalse(r['design_requirements_met_on_supplied_metadata'])
    def test_train_leak(self):
        x=experiment_fixture();x['train_task_ids'].append('one')
        r=paired_learning_audit(x);self.assertEqual(r['contaminated_task_ids'],['one']);self.assertFalse(r['design_requirements_met_on_supplied_metadata'])
    def test_precommit_needed(self):
        x=experiment_fixture();x['candidate_precommitted']=False
        self.assertFalse(paired_learning_audit(x)['design_requirements_met_on_supplied_metadata'])
    def test_development_not_holdout(self):
        x=experiment_fixture();x['rows'][0]['split']='development'
        self.assertFalse(paired_learning_audit(x)['design_requirements_met_on_supplied_metadata'])
    def test_duplicate_rejected(self):
        x=experiment_fixture();x['rows'][1]['task_id']='one'
        with self.assertRaises(AgentModelError):paired_learning_audit(x)
    def test_evaluator_drift_rejected(self):
        x=experiment_fixture();x['rows'][2]['evaluator_revision']='e'*63+'d'
        with self.assertRaises(AgentModelError):paired_learning_audit(x)
    def test_boolean_not_integer(self):
        x=experiment_fixture();x['rows'][0]['baseline_pass']=0
        with self.assertRaises(AgentModelError):paired_learning_audit(x)
    def test_training_duplicate(self):
        x=experiment_fixture();x['train_task_ids'].append('train-1')
        with self.assertRaises(AgentModelError):paired_learning_audit(x)
    def test_no_discordance(self):
        x=experiment_fixture()
        for r in x['rows']:r['candidate_pass']=r['baseline_pass']
        self.assertIsNone(paired_learning_audit(x)['one_sided_exact_discordance_p'])
    def test_one_sided_tail_extremes(self):
        x=experiment_fixture()
        for r in x['rows']:r['baseline_pass']=False;r['candidate_pass']=True
        self.assertEqual(paired_learning_audit(x)['one_sided_exact_discordance_p'],1/64)
    def test_no_source_attestation(self):
        x=paired_learning_audit(experiment_fixture());self.assertFalse(x['independent_outcomes_authenticated'])
    def test_historical_task_version_required(self):
        x=experiment_fixture();x['rows'][0]['task_revision']='old'
        with self.assertRaises(AgentModelError):paired_learning_audit(x)

class AnnotationAgreement(unittest.TestCase):
    def test_count(self):
        v=compare_label_panels(annotations_fixture(),taxonomy_version='MAST-14')
        x=v['per_code']['3.1'];self.assertEqual((x['tp'],x['fp'],x['fn'],x['tn'],x['missing']),(1,1,0,0,1))
        self.assertAlmostEqual(x['precision_wrt_annotator'],.5)
        self.assertFalse(v['independent_ground_truth_verified'])
    def test_other_code_all_zero_kappa_null(self):
        r=compare_label_panels(annotations_fixture(),taxonomy_version='MAST-14')
        self.assertIsNone(r['per_code']['1.1']['cohen_kappa'])
    def test_all_missing(self):
        z={c:None for c in MAST_CODES};r=compare_label_panels([{'item_id':'x','annotator_labels':z,'model_labels':z}],taxonomy_version='MAST-14')
        self.assertIsNone(r['per_code']['1.1']['observed_agreement'])
    def test_round_incompatible(self):
        with self.assertRaises(AgentModelError):compare_label_panels(annotations_fixture(),taxonomy_version='MAST-18')
    def test_extra_text_rejected(self):
        x=annotations_fixture();x[0]['trace']='sensitive text'
        with self.assertRaises(AgentModelError):compare_label_panels(x,taxonomy_version='MAST-14')
    def test_mixed_codes(self):
        x=annotations_fixture();x[0]['model_labels'].pop('1.1')
        with self.assertRaises(AgentModelError):compare_label_panels(x,taxonomy_version='MAST-14')
    def test_missing_not_zero(self):
        x=annotations_fixture();x[0]['model_labels']['3.1']=None
        r=compare_label_panels(x,taxonomy_version='MAST-14')
        self.assertEqual(r['per_code']['3.1']['missing'],2)
    def test_bool_invalid(self):
        x=annotations_fixture();x[0]['model_labels']['1.1']=False
        with self.assertRaises(AgentModelError):compare_label_panels(x,taxonomy_version='MAST-14')
    def test_duplicate_id(self):
        x=annotations_fixture();x[1]['item_id']='case-1'
        with self.assertRaises(AgentModelError):compare_label_panels(x,taxonomy_version='MAST-14')

class MemorySurvival(unittest.TestCase):
    def test_all_states(self):
        r=memory_candidate_review(memory_fixture())
        self.assertEqual([x['decision'] for x in r['decisions']],['eligible_for_external_review','review_conflicting_evidence',
                         'preserve_failed_candidate_do_not_adopt','hold_expired_or_unknown_freshness'])
        self.assertFalse(r['persistent_store_mutated'])
    def test_superseded_high_priority(self):
        x=memory_fixture();x[1]['candidate_state']='superseded'
        self.assertEqual(memory_candidate_review(x)['decisions'][1]['decision'],'archive_superseded_revision')
    def test_untested(self):
        x=memory_fixture();x[0]['candidate_state']='proposed'
        self.assertEqual(memory_candidate_review(x)['decisions'][0]['decision'],'requires_candidate_test')
    def test_unknown_expiry(self):
        x=memory_fixture();x[0]['expiry_state']='unknown'
        self.assertEqual(memory_candidate_review(x)['decisions'][0]['decision'],'hold_expired_or_unknown_freshness')
    def test_no_source(self):
        x=memory_fixture();x[0]['supporting_source_ids']=[]
        self.assertEqual(memory_candidate_review(x)['decisions'][0]['decision'],'requires_tested_support')
    def test_duplicate_source(self):
        x=memory_fixture();x[0]['supporting_source_ids']=['x','x']
        with self.assertRaises(AgentModelError):memory_candidate_review(x)
    def test_conflicting_one_source(self):
        x=memory_fixture();x[0]['contradicting_source_ids']=['e1']
        with self.assertRaises(AgentModelError):memory_candidate_review(x)
    def test_content_not_allowed(self):
        x=memory_fixture();x[0]['claim_text']='data exfiltrate'
        with self.assertRaises(AgentModelError):memory_candidate_review(x)
    def test_duplicate_memory(self):
        x=memory_fixture();x[1]['memory_id']='m01'
        with self.assertRaises(AgentModelError):memory_candidate_review(x)
    def test_casebook(self):self.assertEqual(casebook_v04()['status'],'passed')

if __name__=='__main__':unittest.main()
