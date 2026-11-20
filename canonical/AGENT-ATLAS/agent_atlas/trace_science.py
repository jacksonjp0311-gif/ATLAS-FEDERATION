"""Bounded, offline agent-trace and evaluation research methods (Agent Atlas 0.2).

These functions DO NOT call tools, run agents, provide host authorization,
validate a model's semantic correctness, or establish real-world generalization.
Inputs are trusted structured research fixtures; raw trace text is untrusted data.
"""
from __future__ import annotations
from collections import Counter,defaultdict
from math import comb,isfinite
from typing import Any
from .models import AgentModelError,_id,_num,_json,_sha

# Codes are a snapshot of the public MAST-Data dataset card's 14-mode schema.
# A separate human-annotation file uses differing taxonomies across rounds.
MAST_CODES=tuple(['1.1','1.2','1.3','1.4','1.5','2.1','2.2','2.3','2.4','2.5','2.6','3.1','3.2','3.3'])
KINDS=('agent','model','tool','verification')
STATUSES=('success','failed','incomplete')

def _nonnegative_real(v,name):
    return _num(v,name,lower=0,upper=1e12)


def analyze_trace(spans:list[dict], *, declared_success:bool=False)->dict:
    """Validate one nested agent trace and calculate descriptive timing and evidence coverage.

    All timestamps are in a caller-declared common monotonic millisecond clock.
    This function never executes spans or reads span content. A successful
    verification span is only a *reported* verification, not proof of truth.
    """
    if type(declared_success) is not bool:raise AgentModelError('declared_success must be boolean')
    if not isinstance(spans,list) or not 1<=len(spans)<=5000:raise AgentModelError('1..5000 trace spans required')
    by={};roots=[]
    for row in spans:
        fields={'id','parent_id','kind','start_ms','end_ms','status','evidence_ref'}
        if not isinstance(row,dict) or set(row)!=fields:raise AgentModelError('malformed trace span')
        sid=_id(row['id']);parent=row['parent_id']
        if parent is not None:parent=_id(parent)
        if sid in by:raise AgentModelError('duplicate span identifier')
        if row['kind'] not in KINDS or row['status'] not in STATUSES:raise AgentModelError('unsupported kind/status')
        t0=_nonnegative_real(row['start_ms'],'start_ms');t1=_nonnegative_real(row['end_ms'],'end_ms')
        if t1<t0:raise AgentModelError('negative duration')
        ev=row['evidence_ref']
        if ev is not None:_id(ev,kind='evidence_ref')
        if parent is None:roots.append(sid)
        by[sid]=dict(id=sid,parent_id=parent,kind=row['kind'],start_ms=t0,end_ms=t1,status=row['status'],evidence_ref=ev)
    if len(roots)!=1 or by[roots[0]]['kind']!='agent':raise AgentModelError('exactly one root agent span required')
    root=roots[0]
    for sid,row in by.items():
        p=row['parent_id']
        if p is None:continue
        if p not in by:raise AgentModelError('missing parent')
        par=by[p]
        if row['start_ms']<par['start_ms'] or row['end_ms']>par['end_ms']:
            raise AgentModelError('child interval outside parent')
        if p==sid:raise AgentModelError('span cannot parent itself')
        seen={sid};q=p
        while q is not None:
            if q in seen:raise AgentModelError('cycle in span lineage')
            seen.add(q);q=by[q]['parent_id']
    # Union of child intervals, rather than incorrectly summing concurrent children.
    children=defaultdict(list)
    for row in by.values():
        if row['parent_id'] is not None:children[row['parent_id']].append(row['id'])
    def covered(parent):
        blocks=sorted((by[x]['start_ms'],by[x]['end_ms']) for x in children[parent]);total=0.0
        if not blocks:return 0.0
        low,high=blocks[0]
        for a,b in blocks[1:]:
            if a>high:total+=high-low;low,high=a,b
            elif b>high:high=b
        return total+high-low
    overlap_aware_child_ms=sum(covered(s) for s in by)
    state_counts=Counter(row['status'] for row in by.values())
    kind_counts=Counter(row['kind'] for row in by.values())
    verified=[row for row in by.values() if row['kind']=='verification' and row['status']=='success' and row['evidence_ref']]
    successful_tools=[row for row in by.values() if row['kind']=='tool' and row['status']=='success']
    tool_evidence=sum(x['evidence_ref'] is not None for x in successful_tools)
    flags=[]
    if declared_success and not verified:flags.append('success_claim_without_verification_record')
    if any(row['status']=='failed' for row in by.values()):flags.append('trace_contains_failed_spans')
    if any(row['status']=='incomplete' for row in by.values()):flags.append('trace_contains_incomplete_spans')
    if len(successful_tools)>tool_evidence:flags.append('tool_success_without_evidence_pointer')
    return {'schema':'atlas.agent-trace-structure/1','root':root,'spans':len(spans),
        'root_elapsed_ms':by[root]['end_ms']-by[root]['start_ms'],
        'sum_span_durations_ms':sum(row['end_ms']-row['start_ms'] for row in by.values()),
        'overlap_aware_child_covered_ms':overlap_aware_child_ms,
        'kinds':{k:kind_counts.get(k,0) for k in KINDS},
        'statuses':{k:state_counts.get(k,0) for k in STATUSES},
        'successful_tool_spans':len(successful_tools),'successful_tool_evidence_pointers':tool_evidence,
        'reported_verification_evidence':len(verified),'declared_success':declared_success,
        'diagnostics':flags,'semantically_verified':False,'live_agent_execution':False,
        'limitations':['Reported verification spans are assertions, not independently verified task outcomes',
          'A complete nested trace cannot detect unrecorded actions, hidden state changes, or lying endpoints',
          'Overlapping child durations are not independent elapsed time or billable token usage']}


def outbox_reconciliation(events:list[dict])->dict:
    """Classify pre/post-send side effects; uncertainty never triggers automatic re-send.

    Event phases: prepared -> submitted -> confirmed; or prepared -> rejected.
    This is an *offline* replay of supplied events, not crash-safe durable I/O.
    """
    if not isinstance(events,list) or not 1<=len(events)<=5000:raise AgentModelError('1..5000 outbox events')
    phases={};idem={};duplicates=0
    for idx,e in enumerate(events):
        if not isinstance(e,dict) or set(e)!={'request_id','idempotency_key','phase','provider_receipt'}:
            raise AgentModelError('exact outbox fields required')
        rid=_id(e['request_id']);key=_id(e['idempotency_key']);phase=e['phase'];receipt=e['provider_receipt']
        if phase not in {'prepared','submitted','confirmed','rejected'}:raise AgentModelError('invalid outbox phase')
        if receipt is not None:_id(receipt)
        if phase=='confirmed' and receipt is None:raise AgentModelError('confirmation requires provider receipt')
        if phase!='confirmed' and receipt is not None:raise AgentModelError('receipt only for confirmation')
        if key in idem and idem[key]!=rid:raise AgentModelError('same idempotency key across different requests')
        idem[key]=rid
        prev=phases.get(rid)
        if prev is None:
            if phase!='prepared':raise AgentModelError('unprepared request')
            phases[rid]={'idempotency_key':key,'phase':phase,'provider_receipt':None}
        else:
            if prev['idempotency_key']!=key:raise AgentModelError('idempotency key mutation')
            if prev['phase']==phase:
                if prev['provider_receipt']!=receipt:raise AgentModelError('conflicting duplicate event')
                duplicates+=1;continue
            allowed={'prepared':{'submitted','rejected'},'submitted':{'confirmed','rejected'}}
            if phase not in allowed.get(prev['phase'],set()):raise AgentModelError('invalid/out-of-order transition')
            if phase=='rejected' and prev['phase']=='submitted':
                # Provider rejection could be ambiguous; cannot conclude side effects never occurred.
                prev['phase']='unknown_after_submission'
            else:prev['phase']=phase
            prev['provider_receipt']=receipt
    summary={k:v['phase'] for k,v in sorted(phases.items())}
    unknown=[k for k,v in summary.items() if v in {'submitted','unknown_after_submission'}]
    return {'schema':'atlas.agent-outbox-reconciliation/1','requests':len(phases),'duplicate_events':duplicates,
     'states':summary,'needs_provider_reconciliation':unknown,
     'safe_to_auto_resubmit':[], 'confirmed_by_reported_receipt':sorted(k for k,v in summary.items() if v=='confirmed'),
     'durable_persistence_proven':False,'provider_effects_verified':False,
     'limitations':['A submitted call may have executed even when a receipt is missing or later marked rejected',
        'The model never calls an external provider, and the input log is not a signed/durable journal',
        'A reported receipt is not proof of full downstream effect or authorization']}


def compare_memory_claims(rows:list[dict], *,now_epoch:int)->dict:
    """Preserve revisions and conditional disagreements; never silently pick a winner."""
    if type(now_epoch) is not int or now_epoch<0:raise AgentModelError('now_epoch nonnegative integer')
    if not isinstance(rows,list) or not 1<=len(rows)<=500:raise AgentModelError('memory list must have 1..500 rows')
    by_id={};group=defaultdict(list);expired=[]
    for r in rows:
        fields={'id','subject','predicate','context','value','source_id','source_revision','qualifier','expires_at'}
        if not isinstance(r,dict) or set(r)!=fields:raise AgentModelError('memory claim fields required')
        for x in ('id','subject','predicate','context','source_id','source_revision','qualifier'):_id(r[x],kind=x)
        if r['id'] in by_id:raise AgentModelError('duplicate memory claim identifier')
        if r['expires_at'] is not None and (type(r['expires_at']) is not int or r['expires_at']<0):
            raise AgentModelError('expiry integer or null required')
        _json(r['value'])
        by_id[r['id']]=r
        if r['expires_at'] is not None and r['expires_at']<=now_epoch:expired.append(r['id'])
        else:group[(r['subject'],r['predicate'],r['context'])].append(r)
    conflict=[]
    for (subject,pred,ctx),rs in group.items():
        values={_sha(r['value']) for r in rs}
        if len(values)>1:
            conflict.append({'subject':subject,'predicate':pred,'context':ctx,
                 'claims':[{'id':r['id'],'source_id':r['source_id'],'source_revision':r['source_revision'],
                            'qualifier':r['qualifier'],'value_digest':_sha(r['value'])} for r in rs]})
    return {'schema':'atlas.agent-memory-conflict/1','claims_total':len(rows),
     'expired_ids':sorted(expired),'active_claims':len(rows)-len(expired),
     'unresolved_conflicts':sorted(conflict,key=lambda v:(v['subject'],v['predicate'],v['context'])),
     'auto_resolved':False,'qualifiers_preserved':True,
     'limitations':['Different source values may be compatible under a more precise context not recorded here',
       'No source is independently authenticated and no claim is selected as truth by score',
       'Expiry is a caller-supplied validity policy; it does not delete persisted data']}


def paired_eval(tasks:list[dict])->dict:
    """Paired descriptive evaluation and exact discordance sign test.

    The exact two-sided test conditions on discordant *independent task pairs*,
    not on model calls or restarts; randomized task sampling is NOT established.
    """
    if not isinstance(tasks,list) or not 1<=len(tasks)<=256:raise AgentModelError('1..256 paired tasks')
    seen=set();a=b=improved=regressed=both_pass=both_fail=0;dcost=[]
    for t in tasks:
        if not isinstance(t,dict) or set(t)!={'task_id','baseline_success','candidate_success','baseline_cost','candidate_cost','split'}:
            raise AgentModelError('paired task fields')
        key=_id(t['task_id'])
        if key in seen:raise AgentModelError('duplicate task ID')
        seen.add(key)
        if t['split'] not in {'development','evaluation'}:raise AgentModelError('split must be declared')
        if type(t['baseline_success']) is not bool or type(t['candidate_success']) is not bool:
            raise AgentModelError('success must be boolean')
        c0=_num(t['baseline_cost'],'baseline_cost');c1=_num(t['candidate_cost'],'candidate_cost')
        dc=c1-c0;dcost.append(dc)
        x,y=t['baseline_success'],t['candidate_success']
        a+=x;b+=y
        if x and y:both_pass+=1
        elif not x and not y:both_fail+=1
        elif not x and y:improved+=1
        else:regressed+=1
    n=len(tasks);discord=improved+regressed
    # exact two-sided binomial sign test for discordant pairs under p=.5
    exact_p=min(1.0,2*sum(comb(discord,i) for i in range(min(improved,regressed)+1))/(2**discord)) if discord else 1.0
    splits=Counter(t['split'] for t in tasks)
    return {'schema':'atlas.agent-paired-evaluation/1','tasks':n,'splits':dict(splits),
       'baseline_observed_success_rate':a/n,'candidate_observed_success_rate':b/n,
       'observed_success_difference':(b-a)/n,'improved_pairs':improved,'regressed_pairs':regressed,
       'both_pass':both_pass,'both_fail':both_fail,'discordant_pairs':discord,
       'exact_two_sided_sign_p':exact_p,'mean_candidate_minus_baseline_cost':sum(dcost)/n,
       'benchmark_improvement_established':False,'held_out_proven':False,
       'limitations':['The p value assumes independent exchangeable task pairs and equal discordance probabilities under its null',
           'Task sampling, evaluation validity, outcome correctness, model leakage, seeds and system costs are not authenticated',
           'Development and evaluation splits may not be pooled as an unbiased final benchmark',
           'Results are descriptive counts, not a demonstrated model or agent improvement']}


def mast_annotation_summary(rows:list[dict])->dict:
    """Faithfully summarize public MAST-style 14-code annotations, with null != 0."""
    if not isinstance(rows,list) or not 1<=len(rows)<=10000:raise AgentModelError('1..10000 annotation rows required')
    found=Counter();nonmissing=Counter();missing=Counter();seen=set()
    for r in rows:
        if not isinstance(r,dict) or set(r)!={'trace_id','framework','benchmark','annotation'}:
            raise AgentModelError('MAST row metadata and annotation required')
        key=_id(r['trace_id']);_id(r['framework']);_id(r['benchmark'])
        if key in seen:raise AgentModelError('duplicate trace identifier in supplied sample')
        seen.add(key)
        x=r['annotation']
        if not isinstance(x,dict) or set(x)!=set(MAST_CODES):raise AgentModelError('exact 14-code MAST schema required')
        for k,v in x.items():
            if v is None:missing[k]+=1
            elif type(v) is int and v in (0,1):nonmissing[k]+=1;found[k]+=v
            else:raise AgentModelError('labels require 0, 1 or null')
    return {'schema':'atlas.agent-mast-annotation-summary/1',
        'supplied_traces':len(rows), 'codes':{k:{'positive':found[k],'known':nonmissing[k],
                      'unknown':missing[k], 'fraction_positive_among_known':found[k]/nonmissing[k] if nonmissing[k] else None} for k in MAST_CODES},
        'label_origin':'caller_supplied_annotations_unverified',
        'task_ground_truth_verified':False,'independent_human_annotation_verified':False,
        'limitations':['Null labels are unavailable, not negative examples',
          'The published full MAST-Data annotations are LLM-judge labels and are not task ground truth',
          'A small sample or framework mixture cannot establish population failure rates or causal mechanisms']}
