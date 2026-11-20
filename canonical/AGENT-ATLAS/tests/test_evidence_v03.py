"""Agent Atlas v0.3 method/negative tests; synthetic fixtures only."""
import copy,math,random,unittest
from agent_atlas.evidence_v03 import (project_otel_metadata,recovery_decision,grouped_mast_annotations,
       repeatability_panel,MAST_CODES)
from agent_atlas.v03_cases import otel_fixture,casebook_v03
from agent_atlas.models import AgentModelError


def recovery(**patch):
    x={'task_id':'T','parent_dispatch_recorded':True,'operator_stopped':False,
         'dependency_state':'ready','worker_state':'failed','side_effect_state':'none',
         'verification_state':'none','attempts':1,'max_attempts':3}
    x.update(patch);return recovery_decision(x)


class OTelSourceBoundary(unittest.TestCase):
    def test_fixture_not_agent_truth(self):
        r=project_otel_metadata(otel_fixture())
        self.assertEqual(r['spans'],4);self.assertEqual(r['tool_spans'],1)
        self.assertFalse(r['external_tool_effects_verified'])
        self.assertFalse(r['content_fields_retained'])
    def test_concurrent_spans_duration(self):
        r=project_otel_metadata(otel_fixture())
        self.assertEqual(r['root_elapsed_ms'],100)
        self.assertEqual(r['overlap_aware_child_covered_ms'],79)
    def test_untrusted_content_key_rejected(self):
        x=otel_fixture();x[1]['attributes']['gen_ai.input.messages']='secret'
        with self.assertRaises(AgentModelError):project_otel_metadata(x)
    def test_content_value_nonstring_refused(self):
        x=otel_fixture();x[1]['attributes']['gen_ai.agent.name']={'injected':'text'}
        with self.assertRaises(AgentModelError):project_otel_metadata(x)
    def test_mismatched_op(self):
        x=otel_fixture();x[1]['attributes']['gen_ai.operation.name']='chat'
        with self.assertRaises(AgentModelError):project_otel_metadata(x)
    def test_duplicate_span(self):
        x=otel_fixture();x.append(copy.deepcopy(x[1]))
        with self.assertRaises(AgentModelError):project_otel_metadata(x)
    def test_missing_root(self):
        x=otel_fixture();x[0]['parent_span_id']='f'*16
        with self.assertRaises(AgentModelError):project_otel_metadata(x)
    def test_invalid_hex(self):
        x=otel_fixture();x[0]['trace_id']='g'*32
        with self.assertRaises(AgentModelError):project_otel_metadata(x)
    def test_clock_overflow(self):
        x=otel_fixture();x[2]['end_ns']=10**22
        with self.assertRaises(AgentModelError):project_otel_metadata(x)
    def test_tool_name_required(self):
        x=otel_fixture();x[2]['attributes'].pop('gen_ai.tool.name')
        with self.assertRaises(AgentModelError):project_otel_metadata(x)
    def test_multiple_traces(self):
        x=otel_fixture();x[2]['trace_id']='b'*32
        with self.assertRaises(AgentModelError):project_otel_metadata(x)
    def test_clock_order(self):
        x=otel_fixture();x[1]['end_ns']=1
        with self.assertRaises(AgentModelError):project_otel_metadata(x)

class RecoveryBoundary(unittest.TestCase):
    def test_stop_overrides_submission(self):self.assertEqual(recovery(operator_stopped=True,side_effect_state='submitted_unknown')['decision'],'respect_operator_stop')
    def test_unknown_effect_overrides_limit(self):self.assertEqual(recovery(side_effect_state='submitted_unknown',attempts=3)['decision'],'reconcile_provider_before_resubmit')
    def test_parent_dispatch_required(self):self.assertEqual(recovery(parent_dispatch_recorded=False)['decision'],'require_parent_dispatch')
    def test_dependency(self):self.assertEqual(recovery(dependency_state='blocked')['decision'],'await_dependency')
    def test_report_requires_verification(self):self.assertEqual(recovery(worker_state='reported_success')['decision'],'verify_worker_result')
    def test_host_verified(self):self.assertEqual(recovery(worker_state='reported_success',verification_state='host_verified')['decision'],'complete_with_host_evidence')
    def test_host_verified_not_worker(self):self.assertNotEqual(recovery(worker_state='failed',verification_state='host_verified')['decision'],'complete_with_host_evidence')
    def test_conflicting_host_receipt(self):self.assertEqual(recovery(worker_state='failed',verification_state='host_verified')['decision'],'escalate_conflicting_receipts')
    def test_failed_verification(self):self.assertEqual(recovery(worker_state='reported_success',verification_state='host_rejected')['decision'],'escalate_failed_verification')
    def test_provider_report_with_failed_worker(self):self.assertEqual(recovery(worker_state='failed',side_effect_state='reported_confirmed')['decision'],'reconcile_provider_receipt')
    def test_pending_not_retry(self):self.assertEqual(recovery(worker_state='pending')['decision'],'observe_running_worker')
    def test_running_not_retry(self):self.assertEqual(recovery(worker_state='running')['decision'],'observe_running_worker')
    def test_limit_refuses(self):self.assertEqual(recovery(attempts=3)['decision'],'escalate_attempt_limit')
    def test_retry_is_not_command(self):
        r=recovery();self.assertEqual(r['decision'],'retry_may_be_considered');self.assertFalse(r['executes_retry'])
    def test_invalid_bool(self):
        with self.assertRaises(AgentModelError):recovery(operator_stopped=1)
    def test_invalid_attempt(self):
        with self.assertRaises(AgentModelError):recovery(attempts=4)
    def test_bad_state(self):
        with self.assertRaises(AgentModelError):recovery(verification_state='verified')

class MASTCohorts(unittest.TestCase):
    def row(self,framework='A',benchmark='B',trace_id=1,codes=None):
        return {'mas_name':framework,'llm_name':'testmodel','benchmark_name':benchmark,'trace_id':trace_id,
                'mast_annotation':dict(codes or {k:None for k in MAST_CODES})}
    def test_null_denominator(self):
        x=self.row();d=grouped_mast_annotations([x]);z=d['groups'][0]['codes']['1.1']
        self.assertEqual(z['unknown'],1);self.assertIsNone(z['fraction_of_known'])
    def test_grouping_and_composite_key(self):
        a=self.row('one','bench',1);b=self.row('two','bench',1)
        d=grouped_mast_annotations([a,b]);self.assertEqual(len(d['groups']),2)
    def test_nonbinary_refusal(self):
        a=self.row();a['mast_annotation']['1.1']=True
        with self.assertRaises(AgentModelError):grouped_mast_annotations([a])
    def test_duplicate_refusal(self):
        a=self.row();
        with self.assertRaises(AgentModelError):grouped_mast_annotations([a,a])
    def test_nonexistent_code(self):
        a=self.row();a['mast_annotation']['9.9']=0
        with self.assertRaises(AgentModelError):grouped_mast_annotations([a])
    def test_actual_data_not_implied(self):
        a=self.row();r=grouped_mast_annotations([a]);self.assertFalse(r['human_ground_truth_verified'])

class RepeatedTasks(unittest.TestCase):
    def fixture(self,taskids=('X','Y'),reps=3):
        return [{'task_id':tid,'arm':arm,'trial':j,'reported_success':arm=='candidate',
                 'split':'evaluation','task_version':'source-v1','evaluator_version':'eval-v1','cost_units':j+1}
             for tid in taskids for arm in ('baseline','candidate') for j in range(reps)]
    def test_paired_repeats(self):
        r=repeatability_panel(self.fixture(),repeats=3)
        self.assertEqual(r['observed_all_pass_task_fraction'],{'baseline':0,'candidate':1})
        self.assertFalse(r['claim_of_model_improvement_verified'])
    def test_task_split_mismatch(self):
        x=self.fixture();x[0]['split']='development'
        with self.assertRaises(AgentModelError):repeatability_panel(x,repeats=3)
    def test_evaluator_mismatch(self):
        x=self.fixture();x[0]['evaluator_version']='new'
        with self.assertRaises(AgentModelError):repeatability_panel(x,repeats=3)
    def test_missing_repeat(self):
        x=self.fixture();x.pop()
        with self.assertRaises(AgentModelError):repeatability_panel(x,repeats=3)
    def test_duplicate_repeat(self):
        x=self.fixture();x.append(x[0])
        with self.assertRaises(AgentModelError):repeatability_panel(x,repeats=3)
    def test_reported_bool_must_be_bool(self):
        x=self.fixture();x[0]['reported_success']=1
        with self.assertRaises(AgentModelError):repeatability_panel(x,repeats=3)
    def test_negative_cost(self):
        x=self.fixture();x[0]['cost_units']=-1
        with self.assertRaises(AgentModelError):repeatability_panel(x,repeats=3)
    def test_no_misleading_holdout(self):
        r=repeatability_panel(self.fixture(),repeats=3)
        self.assertFalse(r['paired_evaluation_ground_truth_authenticated'])
    def test_v03_cases(self):
        d=casebook_v03();self.assertEqual(d['status'],'passed');self.assertEqual(d['count'],8)

if __name__=='__main__':unittest.main()
