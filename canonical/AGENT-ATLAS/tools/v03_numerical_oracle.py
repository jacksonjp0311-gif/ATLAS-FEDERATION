"""Independent NumPy arithmetic for 0.3 synthetic evidence examples.

Not a model benchmark, external-trace analysis or validation of human labels.
"""
import json,sys,random,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from agent_atlas.evidence_v03 import project_otel_metadata,recovery_decision,grouped_mast_annotations,repeatability_panel
from agent_atlas.trace_science import MAST_CODES
rng=np.random.default_rng(13496)
c={'span_coverage':0,'recovery_transitions':0,'MAST_counts':0,'MAST_unknowns':0,'repeatability':0}
maxerr=0.0

def check(x,y,kind):
 global maxerr
 e=abs(float(x)-float(y));maxerr=max(e,maxerr)
 if e>1e-10*max(1.0,abs(float(y))):raise AssertionError(f'{kind} mismatch {x=} {y=}')
 c[kind]+=1

for rep in range(250):
 root={'trace_id':'a'*32,'span_id':f'{1:016x}','parent_span_id':None,'operation':'invoke_agent','start_ns':0,'end_ns':100000000,
       'status':'ok','tool_call_id':None,'attributes':{'gen_ai.operation.name':'invoke_agent'}}
 items=[root];ranges=[]
 for i in range(2,11):
  start=int(rng.integers(0,94));end=start+int(rng.integers(1,7))
  ranges.append((start,end))
  items.append({'trace_id':'a'*32,'span_id':f'{i:016x}','parent_span_id':f'{1:016x}',
                'operation':'chat','start_ns':start*1000000,'end_ns':end*1000000,
                'status':'ok','tool_call_id':None,'attributes':{'gen_ai.operation.name':'chat'}})
 result=project_otel_metadata(items)
 # Independent discrete millisecond occupancy, not interval merging.
 ticks=np.zeros(100,dtype=np.bool_)
 for start,end in ranges:ticks[start:end]=True
 check(result['overlap_aware_child_covered_ms'],int(np.count_nonzero(ticks)),'span_coverage')

for i in range(1500):
 deps=['ready','blocked'];workers=['pending','failed','reported_success','running']
 sides=['none','prepared','submitted_unknown','reported_confirmed'];vs=['none','pending','host_verified','host_rejected']
 stopped=bool(rng.integers(0,2));parent=bool(rng.integers(0,2));dep=deps[int(rng.integers(0,2))]
 worker=workers[int(rng.integers(0,4))];side=sides[int(rng.integers(0,4))];ver=vs[int(rng.integers(0,4))]
 attempts=int(rng.integers(0,4));max_attempts=3
 x={'task_id':'test','parent_dispatch_recorded':parent,'operator_stopped':stopped,'dependency_state':dep,
    'worker_state':worker,'side_effect_state':side,'verification_state':ver,'attempts':attempts,'max_attempts':max_attempts}
 r=recovery_decision(x)
 # Independent decision table at the observable-explanation level.
 if stopped:e='respect_operator_stop'
 elif side=='submitted_unknown':e='reconcile_provider_before_resubmit'
 elif not parent:e='require_parent_dispatch'
 elif dep=='blocked':e='await_dependency'
 elif ver=='host_verified' and worker!='reported_success':e='escalate_conflicting_receipts'
 elif ver=='host_verified' and worker=='reported_success':e='complete_with_host_evidence'
 elif ver=='host_rejected' and worker=='reported_success':e='escalate_failed_verification'
 elif side=='reported_confirmed' and worker=='failed':e='reconcile_provider_receipt'
 elif worker=='reported_success' or ver=='pending':e='verify_worker_result'
 elif worker in ('running','pending'):e='observe_running_worker'
 elif attempts>=max_attempts:e='escalate_attempt_limit'
 else:e='retry_may_be_considered'
 if r['decision']!=e:raise AssertionError('decision table mismatch')
 c['recovery_transitions']+=1

for batch in range(200):
 rows=[];a=np.empty((5,14),dtype=np.float64)
 for i in range(5):
  codes={k:([None,0,1][int(z)]) for k,z in zip(MAST_CODES,rng.integers(0,3,size=len(MAST_CODES)))}
  rows.append({'mas_name':'A','llm_name':'model','benchmark_name':'demo','trace_id':i+batch*5,'mast_annotation':codes})
  for j,k in enumerate(MAST_CODES):a[i,j]=np.nan if codes[k] is None else codes[k]
 got=grouped_mast_annotations(rows)['groups'][0]['codes']
 positive=np.nansum(a,axis=0);known=np.count_nonzero(~np.isnan(a),axis=0)
 for j,k in enumerate(MAST_CODES):
  check(got[k]['positive'],positive[j],'MAST_counts')
  check(got[k]['unknown'],5-int(known[j]),'MAST_unknowns')

for rep in range(200):
 data=[];success={}
 for tid in ['a','b','c','d']:
  for arm in ['baseline','candidate']:
   vals=rng.integers(0,2,size=4)
   success[(tid,arm)]=bool(np.all(vals==1))
   for idx,z in enumerate(vals):
    data.append({'task_id':tid,'arm':arm,'trial':idx,'reported_success':bool(z),'split':'evaluation',
       'task_version':'v1','evaluator_version':'v1','cost_units':1})
 got=repeatability_panel(data,repeats=4)
 for arm in ['baseline','candidate']:
  expected=sum(success[tid,arm] for tid in ['a','b','c','d'])/4
  check(got['observed_all_pass_task_fraction'][arm],expected,'repeatability')

print(json.dumps({'schema':'atlas.agent-v03-oracle/1','status':'passed','seed':13496,
    'comparisons':sum(c.values()),'categories':c,'max_absolute_difference':maxerr,
    'numpy_version':np.__version__,'actual_MAST_rows_loaded':0,'live_agents_tested':0,
    'independent_human_label_review':False,'source':'author-generated randomized structured fixtures'},indent=2))
