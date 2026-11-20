import unittest,math,random
from agent_atlas.models import AgentModelError
from agent_atlas.trace_science import (analyze_trace,outbox_reconciliation,compare_memory_claims,paired_eval,
  mast_annotation_summary,MAST_CODES)
from agent_atlas.advanced_cases import advanced_casebook


def span(id='root',parent_id=None,kind='agent',start_ms=0,end_ms=100,status='success',evidence_ref=None):
 return dict(id=id,parent_id=parent_id,kind=kind,start_ms=start_ms,end_ms=end_ms,status=status,evidence_ref=evidence_ref)

class TestTraceStructure(unittest.TestCase):
 def test_root_and_children(self):
  x=[span(),span('a','root','tool',10,80,evidence_ref='sha'),span('b','root','model',20,90)]
  r=analyze_trace(x,declared_success=True)
  self.assertEqual(r['root_elapsed_ms'],100)
  self.assertEqual(r['sum_span_durations_ms'],240)
  self.assertEqual(r['overlap_aware_child_covered_ms'],80)
  self.assertIn('success_claim_without_verification_record',r['diagnostics'])
  self.assertFalse(r['semantically_verified'])
 def test_source_locators_not_truth(self):
  a=analyze_trace([span(),span('verify','root','verification',10,20,evidence_ref='evidence')],declared_success=True)
  self.assertEqual(a['reported_verification_evidence'],1)
  self.assertFalse(a['semantically_verified'])
 def test_missing_tool_ref(self):
  r=analyze_trace([span(),span('tool','root','tool',1,9)],declared_success=False)
  self.assertIn('tool_success_without_evidence_pointer',r['diagnostics'])
 def test_order_independent(self):
  x=[span(),span('tool','root','tool',10,20)]
  self.assertEqual(analyze_trace(x)['spans'],analyze_trace(x[::-1])['spans'])
 def test_missing_root(self):
  with self.assertRaises(AgentModelError):analyze_trace([span('a','b')])
 def test_multiple_roots(self):
  with self.assertRaises(AgentModelError):analyze_trace([span(),span('r2')])
 def test_missing_parent(self):
  with self.assertRaises(AgentModelError):analyze_trace([span(),span('tool','no-parent')])
 def test_parent_time_boundary(self):
  with self.assertRaises(AgentModelError):analyze_trace([span(),span('child','root',start_ms=0,end_ms=101)])
 def test_cycle(self):
  x=[span(),span('child','child')]
  with self.assertRaises(AgentModelError):analyze_trace(x)
 def test_duplicate_ids(self):
  with self.assertRaises(AgentModelError):analyze_trace([span(),span()])
 def test_bad_kind(self):
  with self.assertRaises(AgentModelError):analyze_trace([span(kind='human')])
 def test_bad_clock(self):
  with self.assertRaises(AgentModelError):analyze_trace([span(end_ms=-1)])
 def test_many_concurrent(self):
  x=[span(end_ms=1000)]+[span(f'c{i}','root','tool',5,900,evidence_ref='ev') for i in range(100)]
  r=analyze_trace(x)
  self.assertEqual(r['root_elapsed_ms'],1000)
  self.assertEqual(r['overlap_aware_child_covered_ms'],895)

class TestOutbox(unittest.TestCase):
 @staticmethod
 def ev(phase,request_id='x',idempotency_key='key',provider_receipt=None):
  return dict(phase=phase,request_id=request_id,idempotency_key=idempotency_key,provider_receipt=provider_receipt)
 def test_prepared(self):
  r=outbox_reconciliation([self.ev('prepared')]);self.assertEqual(r['states']['x'],'prepared')
 def test_submitted_without_receipt(self):
  r=outbox_reconciliation([self.ev('prepared'),self.ev('submitted')])
  self.assertEqual(r['needs_provider_reconciliation'],['x']);self.assertFalse(r['safe_to_auto_resubmit'])
 def test_acknowledged(self):
  r=outbox_reconciliation([self.ev('prepared'),self.ev('submitted'),self.ev('confirmed',provider_receipt='provider')])
  self.assertEqual(r['confirmed_by_reported_receipt'],['x']);self.assertFalse(r['provider_effects_verified'])
 def test_rejected_after_submit_unknown(self):
  r=outbox_reconciliation([self.ev('prepared'),self.ev('submitted'),self.ev('rejected')])
  self.assertEqual(r['states']['x'],'unknown_after_submission')
 def test_rejected_without_submit(self):
  r=outbox_reconciliation([self.ev('prepared'),self.ev('rejected')])
  self.assertEqual(r['states']['x'],'rejected')
 def test_duplicate_ack(self):
  r=outbox_reconciliation([self.ev('prepared'),self.ev('submitted'),self.ev('confirmed',provider_receipt='r'),self.ev('confirmed',provider_receipt='r')])
  self.assertEqual(r['duplicate_events'],1)
 def test_duplicate_key_across_requests(self):
  with self.assertRaises(AgentModelError):outbox_reconciliation([self.ev('prepared'),self.ev('prepared',request_id='y')])
 def test_changed_ack(self):
  with self.assertRaises(AgentModelError):outbox_reconciliation([self.ev('prepared'),self.ev('submitted'),self.ev('confirmed',provider_receipt='r'),self.ev('confirmed',provider_receipt='different')])
 def test_confirm_no_send(self):
  with self.assertRaises(AgentModelError):outbox_reconciliation([self.ev('confirmed',provider_receipt='r')])
 def test_new_key_mutation(self):
  with self.assertRaises(AgentModelError):outbox_reconciliation([self.ev('prepared'),self.ev('submitted',idempotency_key='different')])
 def test_invalid_rejected_to_submitted(self):
  with self.assertRaises(AgentModelError):outbox_reconciliation([self.ev('prepared'),self.ev('rejected'),self.ev('submitted')])

class TestMemory(unittest.TestCase):
 def claim(self,id,value,context='same',expires_at=None):
  return dict(id=id,subject='machine',predicate='status',context=context,value=value,source_id='source-'+id,source_revision='rev-'+id,qualifier='unknown accuracy',expires_at=expires_at)
 def test_disagreement_not_resolved(self):
  r=compare_memory_claims([self.claim('a','on'),self.claim('b','off')],now_epoch=100)
  self.assertEqual(len(r['unresolved_conflicts']),1)
  self.assertFalse(r['auto_resolved'])
  self.assertEqual({x['source_id'] for x in r['unresolved_conflicts'][0]['claims']},{'source-a','source-b'})
 def test_context_separates(self):
  r=compare_memory_claims([self.claim('a','on','day'),self.claim('b','off','night')],now_epoch=100)
  self.assertEqual(len(r['unresolved_conflicts']),0)
 def test_same_value_no_conflict(self):
  r=compare_memory_claims([self.claim('a',{'v':1,'w':2}),self.claim('b',{'w':2,'v':1})],now_epoch=100)
  self.assertEqual(len(r['unresolved_conflicts']),0)
 def test_expired_still_accounted(self):
  r=compare_memory_claims([self.claim('a','on',expires_at=100),self.claim('b','off')],now_epoch=100)
  self.assertEqual(r['expired_ids'],['a']);self.assertEqual(r['claims_total'],2)
 def test_dupe_id_rejects(self):
  with self.assertRaises(AgentModelError):compare_memory_claims([self.claim('a','on'),self.claim('a','off')],now_epoch=100)
 def test_float_nan_rejects(self):
  with self.assertRaises(AgentModelError):compare_memory_claims([self.claim('a',float('nan'))],now_epoch=100)

class TestPairedEvaluation(unittest.TestCase):
 def task(self,i,b,c,split='evaluation'):
  return dict(task_id=str(i),baseline_success=b,candidate_success=c,baseline_cost=1,candidate_cost=2,split=split)
 def test_equal(self):
  r=paired_eval([self.task(1,True,True),self.task(2,False,False)])
  self.assertEqual(r['exact_two_sided_sign_p'],1)
  self.assertEqual(r['observed_success_difference'],0)
 def test_one_direction(self):
  r=paired_eval([self.task(i,False,True) for i in range(10)])
  self.assertAlmostEqual(r['exact_two_sided_sign_p'],2/2**10)
  self.assertEqual(r['observed_success_difference'],1)
 def test_half_discordant(self):
  r=paired_eval([self.task(1,False,True),self.task(2,True,False)])
  self.assertEqual(r['exact_two_sided_sign_p'],1)
 def test_label_not_ground_truth(self):
  r=paired_eval([self.task(1,False,True,'development')])
  self.assertFalse(r['held_out_proven'])
  self.assertEqual(r['splits']['development'],1)
 def test_bad_task(self):
  with self.assertRaises(AgentModelError):paired_eval([dict(task_id='0',baseline_success=1,candidate_success=False,baseline_cost=1,candidate_cost=1,split='evaluation')])
 def test_duplicate_tasks(self):
  with self.assertRaises(AgentModelError):paired_eval([self.task(1,False,True),self.task(1,False,True)])
 def test_bad_cost(self):
  with self.assertRaises(AgentModelError):paired_eval([dict(self.task(1,False,True),baseline_cost=-1)])

class TestMAST(unittest.TestCase):
 def row(self,idx,a=None):
  return dict(trace_id=str(idx),framework='mock',benchmark='mock',annotation=a or {k:None for k in MAST_CODES})
 def test_unknown_not_zero(self):
  r=mast_annotation_summary([self.row(1)])
  self.assertIsNone(r['codes']['1.1']['fraction_positive_among_known'])
  self.assertEqual(r['codes']['1.1']['unknown'],1)
 def test_three_categories(self):
  r=self.row(1);r['annotation']['1.1']=1;r['annotation']['2.6']=0;r['annotation']['3.3']=None
  o=mast_annotation_summary([r]);self.assertEqual(o['codes']['1.1']['fraction_positive_among_known'],1)
  self.assertEqual(o['codes']['2.6']['fraction_positive_among_known'],0)
 def test_wrong_code(self):
  x=self.row(1);x['annotation']['4.1']=1
  with self.assertRaises(AgentModelError):mast_annotation_summary([x])
 def test_nonbinary(self):
  x=self.row(1);x['annotation']['1.1']='yes'
  with self.assertRaises(AgentModelError):mast_annotation_summary([x])
 def test_duplicate_id(self):
  with self.assertRaises(AgentModelError):mast_annotation_summary([self.row(1),self.row(1)])
 def test_advanced_casebook(self):
  self.assertEqual(advanced_casebook()['count'],7)
  self.assertEqual(advanced_casebook()['status'],'passed')

if __name__=='__main__':unittest.main()
