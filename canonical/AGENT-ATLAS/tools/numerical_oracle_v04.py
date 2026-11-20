"""Independent NumPy/SciPy checks for offline Agent Atlas 0.4 calculations.

All inputs are author-generated; no original MAST traces or actual agent runs.
"""
import json, random, math, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from scipy.stats import binom
from agent_atlas.learning_science import audit_artifact_proof,paired_learning_audit,compare_label_panels,memory_candidate_review
from agent_atlas.v04_cases import proof_fixture,experiment_fixture,annotations_fixture,memory_fixture
from agent_atlas.trace_science import MAST_CODES
rng=random.Random(3141626)
counts={'proof_precedence':0,'paired_exact_tail':0,'paired_missingness':0,'annotation_confusions':0,'memory_review_precedence':0}

def independent_proof(p):
 if p['operator_stopped']:return 'respect_operator_stop'
 if p['side_effect_state']=='submitted_unknown':return 'reconcile_external_effect_first'
 if not p['parent_dispatch_id'] or p['parent_dispatch_id']!=p['worker_receipt_dispatch_id']:return 'deny_missing_or_mismatched_parent_dispatch'
 if p['goal_revision']!=p['observed_goal_revision']:return 'deny_foreign_goal_revision'
 if not p['expected_artifact_sha256'] or not p['observed_artifact_sha256']:return 'require_complete_artifact_evidence'
 if p['expected_artifact_sha256']!=p['observed_artifact_sha256']:return 'deny_artifact_hash_mismatch'
 if not p['worker_reported_complete']:return 'await_worker_completion'
 if p['evaluator_state']=='reported_fail':return 'escalate_evaluator_failure'
 if not p['evaluator_revision'] or p['evaluator_state'] in ['none','pending']:return 'await_evaluator_evidence'
 if p['evidence_origin']!='reported_host_observation':return 'require_independent_host_observation'
 return 'structurally_eligible_given_trusted_host_facts'

for i in range(1800):
 p=proof_fixture(operator_stopped=bool(rng.getrandbits(1)),
     side_effect_state=rng.choice(['none','prepared','submitted_unknown','reported_confirmed']),
     parent_dispatch_id=rng.choice([None,'dispatch-A','foreign']),
     worker_receipt_dispatch_id=rng.choice([None,'dispatch-A','foreign']),
     observed_goal_revision=rng.choice(['a'*64,'b'*64]),
     observed_artifact_sha256=rng.choice([None,'b'*64,'c'*64]),
     expected_artifact_sha256=rng.choice([None,'b'*64,'c'*64]),
     worker_reported_complete=bool(rng.getrandbits(1)),
     evaluator_state=rng.choice(['none','pending','reported_pass','reported_fail']),
     evaluator_revision=rng.choice([None,'c'*64]),
     evidence_origin=rng.choice(['worker_self_report','reported_host_observation','unknown']))
 r=audit_artifact_proof(p)
 assert r['decision']==independent_proof(p)
 assert not r['host_authority_authenticated'] and not r['external_effect_executed']
 counts['proof_precedence']+=1

for i in range(450):
 n=rng.randint(2,75)
 vals=[(rng.choice([True,False,None]),rng.choice([True,False,None])) for _ in range(n)]
 ex=experiment_fixture();ex['rows']=[{'task_id':'task'+str(j),'split':'evaluation',
    'task_revision':'f'*64,'evaluator_revision':'e'*64,'baseline_pass':a,'candidate_pass':b} for j,(a,b) in enumerate(vals)]
 out=paired_learning_audit(ex)
 known=np.array([(a,b) for a,b in vals if a is not None and b is not None],dtype=np.int8).reshape(-1,2)
 cand=int(np.sum((known[:,0]==0)&(known[:,1]==1)))
 baseline=int(np.sum((known[:,0]==1)&(known[:,1]==0)))
 assert out['paired_outcomes']['candidate_only']==cand
 assert out['paired_outcomes']['baseline_only']==baseline
 assert out['unscored_pairs']==len(vals)-len(known)
 assert out['discordant_pairs']==cand+baseline
 if cand+baseline==0:assert out['one_sided_exact_discordance_p'] is None
 else:
  expected=float(binom.sf(cand-1,cand+baseline,.5))
  assert abs(out['one_sided_exact_discordance_p']-expected)<=2e-13
 counts['paired_exact_tail']+=1;counts['paired_missingness']+=1

for i in range(150):
 n=rng.randint(3,30);rows=[]
 for j in range(n):
  a={k:rng.choice([0,1,None]) for k in MAST_CODES}
  b={k:rng.choice([0,1,None]) for k in MAST_CODES}
  rows.append({'item_id':str(j),'model_labels':b,'annotator_labels':a})
 r=compare_label_panels(rows,taxonomy_version='MAST-14')
 for code in MAST_CODES:
  arr=np.array([[z['annotator_labels'][code] if z['annotator_labels'][code] is not None else -1,
    z['model_labels'][code] if z['model_labels'][code] is not None else -1] for z in rows],dtype=int)
  masks=[(arr[:,0]==1)&(arr[:,1]==1),(arr[:,0]==0)&(arr[:,1]==1),
         (arr[:,0]==1)&(arr[:,1]==0),(arr[:,0]==0)&(arr[:,1]==0),(arr[:,0]<0)|(arr[:,1]<0)]
  values=[int(np.sum(x)) for x in masks]
  d=r['per_code'][code]
  assert values==[d[k] for k in ['tp','fp','fn','tn','missing']]
  counts['annotation_confusions']+=1

for i in range(300):
 rows=memory_fixture()
 for j in range(4):
  r=rows[j]
  r['candidate_state']=rng.choice(['proposed','tested','superseded'])
  r['expiry_state']=rng.choice(['current','expired','unknown'])
  r['evaluation_state']=rng.choice(['none','reported_fail','reported_pass'])
  r['supporting_source_ids']=rng.choice([[],['e1'],['e1','e2']])
  r['contradicting_source_ids']=rng.choice([[],['e3']])
 got=memory_candidate_review(rows)
 for r,d in zip(rows,got['decisions']):
  if r['candidate_state']=='superseded':expect='archive_superseded_revision'
  elif r['expiry_state']!='current':expect='hold_expired_or_unknown_freshness'
  elif r['contradicting_source_ids']:expect='review_conflicting_evidence'
  elif r['evaluation_state']=='reported_fail':expect='preserve_failed_candidate_do_not_adopt'
  elif r['evaluation_state']!='reported_pass' or not r['supporting_source_ids']:expect='requires_tested_support'
  elif r['candidate_state']!='tested':expect='requires_candidate_test'
  else:expect='eligible_for_external_review'
  assert d['decision']==expect
  counts['memory_review_precedence']+=1

result={'schema':'atlas.agent-v04-numeric-oracle/1','status':'passed',
 'comparisons':sum(counts.values()),'categories':counts,
 'seed':3141626,'numpy_version':np.__version__,'scipy_binom_tail':True,
 'MAST_original_rows_imported':0,'agent_invocations':0,'independent_ground_truth':False,
 'causal_improvement_demonstrated':False,
 'limitations':['Deterministic author-generated fixtures, not held-out tasks',
                'Separately implemented precedence and binomial arithmetic is software verification only']}
print(json.dumps(result,indent=2))
