"""Bounded, standard-library offline models for agent reliability studies.

Not a deployed agent runtime, tool executor, memory router, authorization provider,
or independently validated improvement to language models.
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import defaultdict
from heapq import heappush, heappop
from math import sqrt
from typing import Any
import hashlib, json, math

class AgentModelError(ValueError):
    """Invalid scientific/model input, ambiguous evidence or prohibited transition."""

def _num(x, name, *, lower=0, upper=1e12) -> float:
    if type(x) not in (float, int) or not math.isfinite(x) or not lower <= x <= upper:
        raise AgentModelError(f'{name} must be finite and in [{lower}, {upper}]')
    return float(x)

def _id(x, *, kind='identifier') -> str:
    if not isinstance(x,str) or not x.strip() or len(x.encode('utf8'))>120 or any(ord(c)<32 for c in x):
        raise AgentModelError('invalid '+kind)
    return x

def _json(x):
    try:return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
    except (ValueError,TypeError,UnicodeError) as ex:raise AgentModelError('noncanonical JSON') from ex

def _sha(obj) -> str:return hashlib.sha256(_json(obj)).hexdigest()

def validate_graph(tasks:list[dict]) -> dict:
    """Deterministic DAG ordering with AND dependencies and no fixed worker count.

    Does not execute tasks. Priority breaks ties among currently available nodes;
    it is not an optimal makespan solver or a validated planning heuristic.
    """
    if not isinstance(tasks,list) or not 1<=len(tasks)<=256:raise AgentModelError('1..256 tasks required')
    nodes={};dependencies={};children=defaultdict(list);indegree={}
    for t in tasks:
        if not isinstance(t,dict) or set(t)!={'id','depends_on','priority','estimated_cost'}:raise AgentModelError('task requires id, depends_on, priority, estimated_cost')
        key=_id(t['id']);deps=t['depends_on']
        if key in nodes:raise AgentModelError('duplicate task')
        if not isinstance(deps,list) or len(set(deps))!=len(deps) or any(not isinstance(d,str) for d in deps):raise AgentModelError('invalid dependencies')
        priority=_num(t['priority'],'priority',lower=-1000,upper=1000)
        cost=_num(t['estimated_cost'],'estimated_cost')
        nodes[key]={'priority':priority,'estimated_cost':cost}
        dependencies[key]=tuple(deps)
    for key,deps in dependencies.items():
        for dep in deps:
            if dep not in nodes:raise AgentModelError(f'unknown dependency: {dep}')
            if dep==key:raise AgentModelError('self-dependency')
            children[dep].append(key)
        indegree[key]=len(deps)
    heap=[]
    for key,n in indegree.items():
        if n==0:heappush(heap,(-nodes[key]['priority'],key))
    order=[];depth={};critical_cost={}
    while heap:
        _,key=heappop(heap);order.append(key)
        depth[key]=1+max((depth[d] for d in dependencies[key]),default=0)
        critical_cost[key]=nodes[key]['estimated_cost']+max((critical_cost[d] for d in dependencies[key]),default=0)
        for child in children[key]:
            indegree[child]-=1
            if indegree[child]==0:heappush(heap,(-nodes[child]['priority'],child))
    if len(order)!=len(nodes):raise AgentModelError('cycle detected; no feasible topological order')
    return {'order':order,'dependencies':{k:list(dependencies[k]) for k in sorted(dependencies)},
            'critical_path_cost':max(critical_cost.values()),'depth':max(depth.values()),
            'task_count':len(nodes),'execution_occurred':False,
            'limitations':['Tie-broken topological ordering is not an optimal constrained scheduler',
                           'Cost values are supplied estimates; no model invocation or tool call occurred']}

def ready_tasks(tasks, *, completed=(), failed=(), max_workers=4, budget=1e9):
    """Admission under submitted task costs; completed/failed are external receipts.

    A failed dependency blocks descendants rather than silently retrying them.
    """
    plan=validate_graph(tasks)
    done={_id(x) for x in completed};fails={_id(x) for x in failed};allids=set(plan['order'])
    if (done|fails)-allids or done & fails:raise AgentModelError('unknown or contradictory statuses')
    if any(not set(plan['dependencies'][k])<=done for k in done):
        raise AgentModelError('completed task missing admitted dependency completion')
    if type(max_workers) is not int or not 1<=max_workers<=256:raise AgentModelError('invalid max_workers')
    remaining=_num(budget,'budget')
    costs={t['id']:t['estimated_cost'] for t in tasks}
    blocked=set(fails)
    changed=True
    while changed:
        old=len(blocked)
        blocked.update(k for k,deps in plan['dependencies'].items() if any(d in blocked for d in deps))
        changed=len(blocked)!=old
    candidates=[k for k in plan['order'] if k not in done|blocked and set(plan['dependencies'][k])<=done]
    admitted=[]
    for k in candidates:
        if len(admitted)>=max_workers:break
        if costs[k]<=remaining:
            remaining-=costs[k];admitted.append(k)
    return {'ready_candidates':candidates,'admitted':admitted,'blocked_due_to_failure':sorted(blocked-fails),
            'explicitly_failed':sorted(fails),'budget_remaining':remaining,
            'not_yet_ready':sorted(allids-done-fails-blocked-set(candidates)),
            'not_executed':True,'limitations':['External results must be admitted by a separate evidence verifier',
                  'No worker is spawned; estimates are input assumptions']}

def tool_request_gate(request:dict, catalog:dict, approvals=()) -> dict:
    """Simulation of host-owned authorization rules, never a real security boundary.

    No tool description string may grant authority. Only host-specified catalog
    capabilities and explicit operator approvals govern this offline decision.
    """
    if not isinstance(request,dict) or set(request)!={'tool','capability','resource','request_id'}:
        raise AgentModelError('invalid tool request')
    tool=_id(request['tool']);cap=_id(request['capability']);res=_id(request['resource']);rid=_id(request['request_id'])
    if not isinstance(catalog,dict):raise AgentModelError('host catalog required')
    meta=catalog.get(tool)
    if meta is None:return {'admitted':False,'reason':'tool_unknown','request_id':rid}
    if not isinstance(meta,dict) or set(meta)!={'capabilities','resources','mutating'} or type(meta['mutating']) is not bool:
        raise AgentModelError('malformed trusted catalog')
    if not isinstance(meta['capabilities'],list) or not isinstance(meta['resources'],list):raise AgentModelError('invalid catalog lists')
    if cap not in meta['capabilities'] or res not in meta['resources']:
        return {'admitted':False,'reason':'capability_or_resource_not_authorized','request_id':rid}
    if meta['mutating'] and rid not in approvals:
        return {'admitted':False,'reason':'operator_approval_required','request_id':rid}
    return {'admitted':True,'reason':'static_host_policy_satisfied','request_id':rid,
            'limitations':['Simulation only; host must enforce identity, consent, and actual authorization']}

ALLOWED_ACTORS={'operator','parent','worker','supervisor','tool','host'}
ALLOWED_ACTIONS={'dispatch','tool_error','worker_result','retry','checkpoint','final_commit','stop','cancel'}

def append_event(ledger:list[dict], event:dict) -> list[dict]:
    """Append-only content hash chain, not cryptographic signing or durable I/O."""
    verify_ledger(ledger)
    if not isinstance(event,dict) or set(event)!={'actor','action','run_id','payload'}:raise AgentModelError('event fields')
    actor=event['actor'];action=event['action']
    if actor not in ALLOWED_ACTORS or action not in ALLOWED_ACTIONS:raise AgentModelError('actor/action not declared')
    run_id=_id(event['run_id']);payload=event['payload'];_json(payload)
    if not isinstance(payload,dict):raise AgentModelError('payload object required')
    if len(ledger)>0 and any(e['run_id']!=run_id for e in ledger):raise AgentModelError('different run id')
    if any(e['action'] in {'stop','cancel','final_commit'} for e in ledger):raise AgentModelError('terminal run: no further event')
    if action in {'stop','cancel'} and actor not in {'operator','host'}:raise AgentModelError('only operator/host terminal stop/cancel permitted')
    if action=='final_commit' and actor not in {'parent','host'}:raise AgentModelError('final commit must be parent/host')
    if action=='worker_result' and actor!='worker':raise AgentModelError('worker_result must be worker actor')
    prev=ledger[-1]['hash'] if ledger else '0'*64
    record={'sequence':len(ledger),'prev_hash':prev,'run_id':run_id,'actor':actor,'action':action,'payload':payload}
    record['hash']=_sha(record)
    return [*ledger, record]

def verify_ledger(ledger:list[dict]) -> bool:
    if not isinstance(ledger,list) or len(ledger)>10000:raise AgentModelError('ledger length invalid')
    prev='0'*64;run=None;final=False
    for i,e in enumerate(ledger):
        if not isinstance(e,dict) or set(e)!={'sequence','prev_hash','run_id','actor','action','payload','hash'}:raise AgentModelError('ledger row malformed')
        if final or type(e['sequence']) is not int or e['sequence']!=i or e['prev_hash']!=prev:raise AgentModelError('ledger linkage/terminal inconsistency')
        if run is not None and e['run_id']!=run:raise AgentModelError('ledger run inconsistency')
        run=_id(e['run_id'])
        if e['actor'] not in ALLOWED_ACTORS or e['action'] not in ALLOWED_ACTIONS:raise AgentModelError('invalid event action')
        if e['action'] in {'stop','cancel'} and e['actor'] not in {'operator','host'}:raise AgentModelError('invalid stop/cancel actor')
        if e['action']=='final_commit' and e['actor'] not in {'parent','host'}:raise AgentModelError('invalid commit actor')
        if e['action']=='worker_result' and e['actor']!='worker':raise AgentModelError('invalid result actor')
        if not isinstance(e['payload'],dict) or e['hash']!=_sha({k:v for k,v in e.items() if k!='hash'}):raise AgentModelError('content hash mismatch')
        final=e['action'] in {'stop','cancel','final_commit'}
        prev=e['hash']
    return True

def terminal_status(ledger):
    verify_ledger(ledger)
    return {'state':ledger[-1]['action'] if ledger and ledger[-1]['action'] in {'stop','cancel','final_commit'} else 'open',
            'entries':len(ledger),'tip_hash':ledger[-1]['hash'] if ledger else '0'*64}

def verified_worker_receipt(task_id:str,child_run_id:str,output:dict) -> dict:
    """Local content-hash check only. No remote attestation or cryptographic signature."""
    _id(task_id);_id(child_run_id)
    if not isinstance(output,dict):raise AgentModelError('output object required')
    raw={'task_id':task_id,'child_run_id':child_run_id,'output':output}
    return {**raw,'content_sha256':_sha(raw),'admission':'locally_content_verifiable_not_externally_attested'}

def reconcile_worker_receipt(receipt:dict, task_id:str, child_run_id:str) -> dict:
    if not isinstance(receipt,dict) or set(receipt)!={'task_id','child_run_id','output','content_sha256','admission'}:
        raise AgentModelError('malformed receipt')
    if receipt['task_id']!=task_id or receipt['child_run_id']!=child_run_id:
        raise AgentModelError('foreign task/child receipt')
    if receipt['content_sha256']!=_sha({k:receipt[k] for k in ('task_id','child_run_id','output')}):
        raise AgentModelError('mutated receipt')
    return {'admitted':True,'task_id':task_id,'receipt_digest':receipt['content_sha256'],
            'limitations':['Content hash proves local bytes and identifiers only; not truth of a worker claim',
                           'Parent must check required evidence and consequences before final commitment']}

def select_qualified_memories(memories:list[dict], *, budget_tokens:int, weights=(.5,.3,.2)) -> dict:
    """Original budgeted memory illustration, NOT Atlas cross-domain routing."""
    if type(budget_tokens) is not int or not 0<=budget_tokens<=100000:raise AgentModelError('budget must be nonnegative int')
    if len(weights)!=3 or any(type(w) not in (float,int) or not 0<=w<=1 for w in weights) or abs(sum(weights)-1)>1e-12:
        raise AgentModelError('weights must sum to one')
    if not isinstance(memories,list) or len(memories)>500:raise AgentModelError('memory list limit')
    ranked=[];ids=set()
    for m in memories:
        if not isinstance(m,dict) or set(m)!={'id','relevance','recency','importance','tokens','qualifier','source_id'}:
            raise AgentModelError('memory must include qualifier and source')
        name=_id(m['id']);_id(m['source_id']);_id(m['qualifier'],kind='qualifier')
        if name in ids:raise AgentModelError('duplicate memory ID')
        ids.add(name)
        values=[_num(m[k],k,lower=0,upper=1) for k in ('relevance','recency','importance')]
        if type(m['tokens']) is not int or not 1<=m['tokens']<=100000:raise AgentModelError('invalid memory token size')
        score=sum(a*b for a,b in zip(weights,values))
        ranked.append((score,name,m))
    ranked.sort(key=lambda x:(-x[0],x[1]))
    chosen=[];remaining=budget_tokens
    for score,name,m in ranked:
        if m['tokens']<=remaining:
            chosen.append({'id':name,'score':score,'source_id':m['source_id'],'qualifier':m['qualifier'],'tokens':m['tokens']})
            remaining-=m['tokens']
    return {'admitted':chosen,'remaining':remaining,'excluded':[n for _,n,_ in ranked if n not in {x['id'] for x in chosen}],
            'status':'illustrative_scored_memory_selection','limitations':['Rank scores are not scientific confidence','All qualifiers are retained in chosen units','This is not the deferred Atlas or Bitwork router']}

def reliability_metrics(trials:list[list[bool]]) -> dict:
    """Empirical repeated-trial pass^k vs pass@k, no i.i.d. assumption needed for counts."""
    if not isinstance(trials,list) or not 1<=len(trials)<=10000 or not isinstance(trials[0],list):raise AgentModelError('trial matrix required')
    k=len(trials[0])
    if not 1<=k<=128 or any(not isinstance(row,list) or len(row)!=k or any(type(x) is not bool for x in row) for row in trials):
        raise AgentModelError('consistent boolean k-trials required')
    n=len(trials)
    return {'tasks':n,'repeats_per_task':k,
       'observed_pass_all_k':sum(all(row) for row in trials)/n,
       'observed_pass_any_k':sum(any(row) for row in trials)/n,
       'per_trial_mean':sum(sum(row) for row in trials)/(n*k),
       'estimated_independent_pass_all_k':(sum(sum(row) for row in trials)/(n*k))**k,
       'limitations':['Observed pass-all and pass-any are finite empirical fractions, not confidence intervals',
                      'The p^k estimate assumes independent identically distributed repeated trials; correlated failures invalidate that extrapolation',
                      'Do not compare different task distributions or equate repeated trial success with factual correctness']}

def receipt_survival(ledger:list[dict],receipt:dict,task_id:str,child_run_id:str) -> dict:
    """Join retained child receipt to a nonterminal parent journal, not run a restart."""
    state=terminal_status(ledger)
    if state['state']!='open':raise AgentModelError('parent already terminal')
    if not any(e['action']=='dispatch' and e['actor'] in {'parent','host'} and e['payload'].get('task')==task_id and e['payload'].get('child_run_id')==child_run_id for e in ledger):
        raise AgentModelError('no matching parent dispatch task/child lineage')
    admitted=reconcile_worker_receipt(receipt,task_id,child_run_id)
    return {'status':'eligible_for_parent_verification','run_tip_hash':state['tip_hash'],
            'receipt_digest':admitted['receipt_digest'],
            'missing':['actual parent restart/reconciliation not executed','claim/evidence truth not independently reviewed']}
