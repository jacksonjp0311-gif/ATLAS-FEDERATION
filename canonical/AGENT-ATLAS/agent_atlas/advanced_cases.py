"""Executable v0.2 research cases. All traces and labels here are AUTHOR-CONSTRUCTED."""
from .trace_science import (analyze_trace,outbox_reconciliation,compare_memory_claims,
                           paired_eval,mast_annotation_summary,MAST_CODES)
from .models import AgentModelError

def advanced_casebook():
    cases=[]
    def add(name,output,ok,origin='constructed_fixture'):
        cases.append({'id':name,'result':output,'passed':bool(ok),'origin':origin})
    rows=[
        dict(id='root',parent_id=None,kind='agent',start_ms=0,end_ms=250,status='success',evidence_ref=None),
        dict(id='subA',parent_id='root',kind='agent',start_ms=20,end_ms=160,status='success',evidence_ref=None),
        dict(id='subB',parent_id='root',kind='agent',start_ms=40,end_ms=145,status='success',evidence_ref=None),
        dict(id='toolA',parent_id='subA',kind='tool',start_ms=35,end_ms=70,status='success',evidence_ref='tool-response-sha1'),
        dict(id='modelB',parent_id='subB',kind='model',start_ms=50,end_ms=100,status='success',evidence_ref=None),
        dict(id='verify',parent_id='root',kind='verification',start_ms=165,end_ms=200,status='incomplete',evidence_ref=None)]
    a=analyze_trace(rows,declared_success=True)
    add('overlap-versus-evidence',a,a['root_elapsed_ms']==250 and 'success_claim_without_verification_record' in a['diagnostics'])
    r=outbox_reconciliation([
        {'request_id':'r1','idempotency_key':'k1','phase':'prepared','provider_receipt':None},
        {'request_id':'r1','idempotency_key':'k1','phase':'submitted','provider_receipt':None},
        {'request_id':'r1','idempotency_key':'k1','phase':'submitted','provider_receipt':None}])
    add('unknown-external-call-not-auto-retried',r,r['needs_provider_reconciliation']==['r1'] and r['duplicate_events']==1)
    confirmed=outbox_reconciliation([
        {'request_id':'r1','idempotency_key':'k1','phase':'prepared','provider_receipt':None},
        {'request_id':'r1','idempotency_key':'k1','phase':'submitted','provider_receipt':None},
        {'request_id':'r1','idempotency_key':'k1','phase':'confirmed','provider_receipt':'provider-receipt'}])
    add('provider-receipt-not-task-truth',confirmed,confirmed['confirmed_by_reported_receipt']==['r1'] and not confirmed['provider_effects_verified'])
    mem=[dict(id='a',subject='machine',predicate='status',context='2026-Q4',value='ready',source_id='src-a',source_revision='r1',qualifier='operator report',expires_at=None),
         dict(id='b',subject='machine',predicate='status',context='2026-Q4',value='fault',source_id='src-b',source_revision='r2',qualifier='sensor feed disputed',expires_at=None),
         dict(id='c',subject='machine',predicate='status',context='2024-Q1',value='ready',source_id='src-c',source_revision='r3',qualifier='old log',expires_at=1730000000)]
    conflict=compare_memory_claims(mem,now_epoch=1790000000)
    add('memory-contradiction-not-overwritten',conflict,len(conflict['unresolved_conflicts'])==1 and conflict['expired_ids']==['c'])
    tasks=[]
    for i,(b,c) in enumerate([(1,1),(1,0),(0,1),(1,1),(0,1),(0,0),(0,1),(1,0)]):
        tasks.append({'task_id':f't{i}','baseline_success':bool(b),'candidate_success':bool(c),'baseline_cost':10+i,'candidate_cost':12+i,'split':'evaluation'})
    paired=paired_eval(tasks)
    add('paired-eval-discordances',paired,paired['improved_pairs']==3 and paired['regressed_pairs']==2 and not paired['held_out_proven'])
    demo=[]
    for idx in range(3):
        ann={k:None for k in MAST_CODES}
        ann['1.3']=1 if idx==0 else 0
        if idx<2:ann['3.2']=1
        demo.append({'trace_id':f'trace-{idx}','framework':'author_fixture','benchmark':'none','annotation':ann})
    mast=mast_annotation_summary(demo)
    add('missing-annotation-not-negative',mast,mast['codes']['1.3']['known']==3 and mast['codes']['2.1']['known']==0 and mast['codes']['2.1']['fraction_positive_among_known'] is None)
    # Explicit invalid transitions and unverified success cases
    def rejects(fn,*args,**kwargs):
        try:fn(*args,**kwargs)
        except AgentModelError:return True
        return False
    errors={'duplicate_trace_spans':rejects(analyze_trace,[rows[0],rows[0]]),
      'outbox_confirmation_without_send':rejects(outbox_reconciliation,[{'request_id':'r','idempotency_key':'k','phase':'confirmed','provider_receipt':'yes'}]),
      'negative_as_unknown_maST':rejects(mast_annotation_summary,[{'trace_id':'t','framework':'f','benchmark':'b','annotation':dict.fromkeys(MAST_CODES,-1)}])}
    add('invalid-claim-refusals',errors,all(errors.values()))
    return {'schema':'atlas.agent-advanced-casebook/1','version':'0.2.0',
      'cases':cases,'count':len(cases),'status':'passed' if all(x['passed'] for x in cases) else 'failed',
      'actual_live_agents_run':False,'real_MAST_data_rows_loaded':0,'independent_evaluator_review':False}
