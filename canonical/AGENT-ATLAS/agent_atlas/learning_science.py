"""Agent Atlas v0.4: proof-qualified learning and evidence comparisons.

Pure Python, offline, deterministic, intentionally does not run agents, access
external tools, authenticate host signatures, or declare LLM improvement.
Caller-supplied evidence and labels are UNTRUSTED until separately reviewed.
"""
from __future__ import annotations
import hashlib
import math
from collections import defaultdict
from math import comb
from .models import AgentModelError, _id, _sha
from .trace_science import MAST_CODES


def _exact(x, keys, name):
    if not isinstance(x, dict) or set(x) != set(keys):
        raise AgentModelError(f'{name} requires exact fields: {sorted(keys)}')
    return x


def _boolean(x, name):
    if type(x) is not bool: raise AgentModelError(name + ' must be Boolean')
    return x


def _sha256(x, name, *, nullable=False):
    if x is None and nullable:return x
    if not isinstance(x, str) or len(x)!=64 or any(c not in '0123456789abcdef' for c in x):
        raise AgentModelError(name+' must be lowercase SHA-256 hex')
    return x


def audit_artifact_proof(packet:dict) -> dict:
    """Check structure/lineage of a *supplied* host artifact receipt.

    Hash equality is not host authentication; caller could forge the entire
    packet. The output states admissibility CONDITIONAL on trusted host facts.
    """
    _exact(packet, {'task_id','goal_revision','observed_goal_revision',
      'parent_dispatch_id','worker_receipt_dispatch_id','worker_reported_complete',
      'operator_stopped','side_effect_state','expected_artifact_sha256',
      'observed_artifact_sha256','evaluator_revision','evaluator_state',
      'evidence_origin'},'artifact evidence packet')
    tid=_id(packet['task_id'])
    for k in ('goal_revision','observed_goal_revision'):
        _sha256(packet[k],k)
    for k in ('parent_dispatch_id','worker_receipt_dispatch_id'):
        if packet[k] is not None:_id(packet[k])
    for k in ('worker_reported_complete','operator_stopped'):_boolean(packet[k],k)
    for k in ('expected_artifact_sha256','observed_artifact_sha256'):
        _sha256(packet[k],k,nullable=True)
    if packet['side_effect_state'] not in {'none','prepared','submitted_unknown','reported_confirmed'}:
        raise AgentModelError('unsupported side_effect_state')
    if packet['evaluator_state'] not in {'none','pending','reported_pass','reported_fail'}:
        raise AgentModelError('unsupported evaluator_state')
    if packet['evidence_origin'] not in {'worker_self_report','reported_host_observation','unknown'}:
        raise AgentModelError('unsupported evidence_origin')
    if packet['evaluator_revision'] is not None:_sha256(packet['evaluator_revision'],'evaluator_revision')
    reasons=[]
    if packet['operator_stopped']:
        status='respect_operator_stop'
    elif packet['side_effect_state']=='submitted_unknown':
        status='reconcile_external_effect_first'
    elif packet['parent_dispatch_id'] is None or packet['parent_dispatch_id']!=packet['worker_receipt_dispatch_id']:
        status='deny_missing_or_mismatched_parent_dispatch'
    elif packet['goal_revision']!=packet['observed_goal_revision']:
        status='deny_foreign_goal_revision'
    elif packet['expected_artifact_sha256'] is None or packet['observed_artifact_sha256'] is None:
        status='require_complete_artifact_evidence'
    elif packet['expected_artifact_sha256']!=packet['observed_artifact_sha256']:
        status='deny_artifact_hash_mismatch'
    elif not packet['worker_reported_complete']:
        status='await_worker_completion'
    elif packet['evaluator_state']=='reported_fail':
        status='escalate_evaluator_failure'
    elif packet['evaluator_revision'] is None or packet['evaluator_state'] in {'none','pending'}:
        status='await_evaluator_evidence'
    elif packet['evidence_origin']!='reported_host_observation':
        status='require_independent_host_observation'
    else:
        status='structurally_eligible_given_trusted_host_facts'
    if packet['expected_artifact_sha256']==packet['observed_artifact_sha256'] and packet['expected_artifact_sha256'] is not None:
        reasons.append('hash_fields_match_but_bytes_and_sender_were_not_authenticated')
    return {'schema':'atlas.agent-artifact-evidence-gate/1','task_id':tid,
      'decision':status,'reasons':reasons,'external_effect_executed':False,
      'artifact_bytes_rehashed_here':False,'host_authority_authenticated':False,
      'semantic_task_success_verified':False,
      'limitations':['Every input is caller-supplied, including claims of independent host observation',
        'SHA-256 fields are compared but original artifact bytes and authentic signatures are not checked',
        'Eligibility is conditional; this code grants no tool permission or scientific acceptance']}


def paired_learning_audit(experiment:dict)->dict:
    """Paired benchmark metrics with contamination and uncertain-label refusal.

    Labels are caller-supplied reports and do NOT become independently verified
    success even if a p value is small. Exact McNemar sign tail for discordance.
    """
    _exact(experiment,{'experiment_id','baseline_revision','candidate_revision','evaluator_revision',
      'candidate_precommitted','train_task_ids','rows'},'paired learning experiment')
    ident=_id(experiment['experiment_id'])
    for key in ('baseline_revision','candidate_revision','evaluator_revision'):_sha256(experiment[key],key)
    _boolean(experiment['candidate_precommitted'],'candidate_precommitted')
    trained=experiment['train_task_ids']
    if not isinstance(trained,list) or len(trained)>10000:raise AgentModelError('train_task_ids list max 10000')
    train={_id(x) for x in trained}
    if len(train)!=len(trained):raise AgentModelError('duplicate training id')
    rows=experiment['rows']
    if not isinstance(rows,list) or not 2<=len(rows)<=1000:raise AgentModelError('2..1000 paired evaluation rows')
    seen=set();group={'candidate_only':0,'baseline_only':0,'both_pass':0,'both_fail':0,'unscored':0}
    heldout=0;dev=0;collisions=[]
    for row in rows:
        _exact(row,{'task_id','split','task_revision','evaluator_revision','baseline_pass','candidate_pass'},'paired row')
        tid=_id(row['task_id'])
        if tid in seen:raise AgentModelError('duplicate paired task id')
        seen.add(tid)
        if row['split'] not in ('development','evaluation'):raise AgentModelError('invalid split')
        _sha256(row['task_revision'],'task_revision')
        _sha256(row['evaluator_revision'],'row.evaluator_revision')
        if row['evaluator_revision']!=experiment['evaluator_revision']:raise AgentModelError('mixed evaluator version')
        for k in ('baseline_pass','candidate_pass'):
            if row[k] is not None and type(row[k]) is not bool:raise AgentModelError('outcome must be bool or null')
        if tid in train and row['split']=='evaluation':collisions.append(tid)
        if row['split']=='evaluation':heldout+=1
        else:dev+=1
        a,b=row['baseline_pass'],row['candidate_pass']
        if a is None or b is None:group['unscored']+=1
        elif a and b:group['both_pass']+=1
        elif not a and not b:group['both_fail']+=1
        elif b:group['candidate_only']+=1
        else:group['baseline_only']+=1
    n=group['candidate_only']+group['baseline_only']
    # H0 discordant-direction symmetry; one-sided P(X >= candidate-only | n, .5)
    p=None if n==0 else sum(comb(n,k) for k in range(group['candidate_only'],n+1))/2**n
    defensible=bool(experiment['candidate_precommitted'] and dev==0 and heldout>0 and not collisions and group['unscored']==0)
    return {'schema':'atlas.agent-paired-learning-audit/1','experiment_id':ident,
        'tasks':len(rows),'evaluation_tasks':heldout,'development_tasks':dev,
        'unscored_pairs':group['unscored'],'contaminated_task_ids':sorted(collisions),
        'discordant_pairs':n,'paired_outcomes':group,'one_sided_exact_discordance_p':p,
        'candidate_precommitted':experiment['candidate_precommitted'],
        'design_requirements_met_on_supplied_metadata':defensible,
        'independent_outcomes_authenticated':False,'agent_improvement_demonstrated':False,
        'limitations':['Paired outcomes and training membership are caller-reported and not validated against original tasks',
            'A small p value is not causal proof, benchmark cleanliness, an independent evaluator, or real-world generalization',
            'Development trials and null outcomes cannot be relabeled as held-out failures',
            'Repeated seeds, costs and clustering require an additional prespecified statistical design']}


def compare_label_panels(rows:list[dict], *,taxonomy_version:str) -> dict:
    """Compare supplied 14-code model-vs-annotator labels, preserving missingness.

    Human labels are annotator opinions, not independent task truth; code IDs
    must refer to the SAME revision. Earlier MAST rounds cannot be pooled here.
    """
    if taxonomy_version!='MAST-14':raise AgentModelError('incompatible taxonomy revision; no crosswalk defined')
    if not isinstance(rows,list) or not 1<=len(rows)<=1000:raise AgentModelError('1..1000 annotation rows required')
    seen=set();matrices={c:[0,0,0,0,0] for c in MAST_CODES}
    # matrix order TP,FP,FN,TN,unknown (relative to annotator, not actual truth)
    for row in rows:
        _exact(row,{'item_id','model_labels','annotator_labels'},'annotation pair')
        rid=_id(row['item_id'])
        if rid in seen:raise AgentModelError('duplicate item_id')
        seen.add(rid)
        for key in ('model_labels','annotator_labels'):
            if not isinstance(row[key],dict) or set(row[key])!=set(MAST_CODES):
                raise AgentModelError('must have exact 14-code MAST map')
        for code in MAST_CODES:
            a,b=row['annotator_labels'][code],row['model_labels'][code]
            if a is not None and type(a) is not int:raise AgentModelError('invalid annotator label')
            if b is not None and type(b) is not int:raise AgentModelError('invalid model label')
            if a not in (0,1,None) or b not in (0,1,None):raise AgentModelError('labels must be 0/1/null')
            idx=4 if a is None or b is None else 0 if a==b==1 else 1 if b==1 else 2 if a==1 else 3
            matrices[code][idx]+=1
    per={}
    for code,(tp,fp,fn,tn,unknown) in matrices.items():
        known=tp+fp+fn+tn
        precision=tp/(tp+fp) if tp+fp else None
        recall=tp/(tp+fn) if tp+fn else None
        accuracy=(tp+tn)/known if known else None
        # Cohen's kappa for two labelers. Degenerate perfect agreement with
        # no label prevalence distinction gets kappa null, not 1.
        if known:
            pa=(tp+fn)/known;pb=(tp+fp)/known
            pe=pa*pb+(1-pa)*(1-pb)
            kappa=(accuracy-pe)/(1-pe) if pe<1 else None
        else:kappa=None
        per[code]={'known':known,'missing':unknown,'model_positive':tp+fp,'annotator_positive':tp+fn,
          'tp':tp,'fp':fp,'fn':fn,'tn':tn,'precision_wrt_annotator':precision,
          'recall_wrt_annotator':recall,'observed_agreement':accuracy,'cohen_kappa':kappa}
    return {'schema':'atlas.agent-annotation-panel/1','items':len(rows),'taxonomy_version':taxonomy_version,
       'per_code':per,'all_codes':len(per),'source':'caller_supplied_annotation_pairs',
       'independent_ground_truth_verified':False,
       'limitations':['MAST human annotation rounds with 18, 17, 17 and 14 codes cannot be pooled without a validated crosswalk',
         'Agreement measures labels, not correctness of agent action or human-verified task outcome',
         'Missing labels never count as negative; null statistics are not zero',
         'This function reads only bounded label maps, not prompt/trace text']}


def memory_candidate_review(records:list[dict])->dict:
    """Test evidence qualifiers for proposed persistent learning; no writes.

    A memory only becomes `eligible_for_external_review`, never silently
    admitted into a live memory store. Contradictory sources stay visible.
    """
    if not isinstance(records,list) or not 1<=len(records)<=300:raise AgentModelError('1..300 memory candidates')
    seen=set();out=[]
    for row in records:
        _exact(row,{'memory_id','claim_revision','scope_id','supporting_source_ids',
           'contradicting_source_ids','evaluation_state','candidate_state','expiry_state'},'memory candidate')
        mid=_id(row['memory_id']);_id(row['scope_id']);_sha256(row['claim_revision'],'claim_revision')
        if mid in seen:raise AgentModelError('duplicate memory_id')
        seen.add(mid)
        support=row['supporting_source_ids'];contrary=row['contradicting_source_ids']
        for field,items in [('support',support),('contradict',contrary)]:
            if not isinstance(items,list) or len(items)>64:raise AgentModelError('bounded source id list required')
            if len(items)!=len({_id(x) for x in items}):raise AgentModelError('duplicate source reference')
        if set(support)&set(contrary):raise AgentModelError('one source cannot simultaneously be assigned opposite roles without separate claims')
        if row['evaluation_state'] not in ('none','reported_pass','reported_fail'):
            raise AgentModelError('invalid evaluation state')
        if row['candidate_state'] not in ('proposed','tested','superseded'):
            raise AgentModelError('invalid candidate state')
        if row['expiry_state'] not in ('current','expired','unknown'):
            raise AgentModelError('invalid expiry state')
        if row['candidate_state']=='superseded':decision='archive_superseded_revision'
        elif row['expiry_state']!='current':decision='hold_expired_or_unknown_freshness'
        elif contrary:decision='review_conflicting_evidence'
        elif row['evaluation_state']=='reported_fail':decision='preserve_failed_candidate_do_not_adopt'
        elif row['evaluation_state']!='reported_pass' or not support:decision='requires_tested_support'
        elif row['candidate_state']!='tested':decision='requires_candidate_test'
        else:decision='eligible_for_external_review'
        out.append({'memory_id':mid,'decision':decision,'support_ids':support,'contradict_ids':contrary,
                    'source_count':len(support)+len(contrary)})
    return {'schema':'atlas.agent-memory-review/1','candidates':len(records),'decisions':out,
      'persistent_store_mutated':False,'source_independence_authenticated':False,'real_transfer_learning_demonstrated':False,
      'limitations':['Even an eligible record needs external reviewer, trusted source provenance and rollback/expiration policy',
        'Contradicting evidence is retained, not averaged away or silently replaced',
        'Reported evaluation outcome and source IDs are caller-supplied, not authenticated',
        'The memory system is not linked to PEGASUS, SYMBIOTE or a live model']}
