"""Auditable constructed agent reliability cases, no LLM runs or user data."""
from copy import deepcopy
from .models import *

def casebook():
    cases=[]
    def add(name, passed, expected, observation):
        cases.append({'id':name,'origin':'author_constructed_offline','passed':bool(passed),
                      'expected':expected,'observation':observation,'live_agent_or_external_model_test':False})
    tasks=[{'id':'collect','depends_on':[],'priority':5,'estimated_cost':2},
           {'id':'analyze','depends_on':['collect'],'priority':9,'estimated_cost':4},
           {'id':'audit','depends_on':['collect'],'priority':6,'estimated_cost':3},
           {'id':'publish','depends_on':['analyze','audit'],'priority':1,'estimated_cost':1}]
    p=validate_graph(tasks)
    add('dag_and_critical_path',p['order']==['collect','analyze','audit','publish'] and p['critical_path_cost']==7,
        'dependency graph is acyclic, critical path 7 in user supplied cost units',{'order':p['order'],'critical_path_cost':p['critical_path_cost']})
    w=ready_tasks(tasks,completed=['collect'],max_workers=2,budget=4)
    add('admit_only_affordable_work',w['admitted']==['analyze'] and 'audit' in w['ready_candidates'],
        'does not launch workers or silently overspend budget',w)
    b=ready_tasks(tasks,failed=['collect'])
    add('failed_dependency_blocks_descendants',set(b['blocked_due_to_failure'])=={'analyze','audit','publish'},
        'failed required dependency blocks dependent goals',b['blocked_due_to_failure'])
    try:
        validate_graph([{'id':'a','depends_on':['b'],'priority':1,'estimated_cost':1},
                        {'id':'b','depends_on':['a'],'priority':1,'estimated_cost':1}]); rejected=False
    except AgentModelError:rejected=True
    add('cycle_rejection',rejected,'cyclic task plans fail closed',{'rejected':rejected})
    catalog={'read':{'capabilities':['read'],'resources':['report'],'mutating':False},
             'send':{'capabilities':['write'],'resources':['approved-mail'],'mutating':True}}
    req={'tool':'send','capability':'write','resource':'approved-mail','request_id':'user-approval-001'}
    refused=tool_request_gate(req,catalog);allowed=tool_request_gate(req,catalog,approvals=['user-approval-001'])
    add('host_owned_approval',not refused['admitted'] and allowed['admitted'] and refused['reason']=='operator_approval_required',
        'mutating action requires host approval',{'without_approval':refused,'with_declared_approval':allowed})
    unauthorized=tool_request_gate({**req,'resource':'private-vault'},catalog,approvals=['user-approval-001'])
    add('scope_not_expandable_by_approval',not unauthorized['admitted'],
        'approval does not grant a resource absent from catalog',unauthorized)
    journal=append_event([],{'run_id':'r1','actor':'parent','action':'dispatch','payload':{'task':'collect'}})
    journal=append_event(journal,{'run_id':'r1','actor':'worker','action':'worker_result','payload':{'status':'complete'}})
    journal=append_event(journal,{'run_id':'r1','actor':'operator','action':'stop','payload':{'reason':'operator'}})
    try:append_event(journal,{'run_id':'r1','actor':'parent','action':'retry','payload':{}});stopped=False
    except AgentModelError:stopped=True
    add('explicit_stop_is_final',stopped and terminal_status(journal)['state']=='stop',
        'operator stop is different from tool error and is terminal',terminal_status(journal))
    corrupted=deepcopy(journal);corrupted[1]['payload']={'status':'forged'}
    try:verify_ledger(corrupted);tampered=False
    except AgentModelError:tampered=True
    add('journal_detects_mutation',tampered,'content hash chain detects edited bytes, not proof of authorship',{'tamper_detected':tampered})
    rec=verified_worker_receipt('task42','child-abc',{'evidence':'hash-on-files','status':'done'})
    res=reconcile_worker_receipt(rec,'task42','child-abc')
    add('receipt_content_integrity',res['admitted'] and len(res['receipt_digest'])==64,
        'local hash and task linkage verified, external truth not asserted',res)
    try:reconcile_worker_receipt(rec,'other','child-abc');foreign=False
    except AgentModelError:foreign=True
    add('foreign_child_receipt_rejected',foreign,'worker result of a different task not accepted',{'rejected':foreign})
    memory=[{'id':'m1','source_id':'s1','relevance':.9,'recency':.8,'importance':1,'tokens':6,'qualifier':'source not expert reviewed'},
            {'id':'m2','source_id':'s2','relevance':.8,'recency':.6,'importance':.8,'tokens':7,'qualifier':'assumption: toy run'}]
    ctx=select_qualified_memories(memory,budget_tokens=6)
    add('memory_qualifier_remains_attached',len(ctx['admitted'])==1 and ctx['admitted'][0]['qualifier']=='source not expert reviewed',
        'context selection does not drop attached limitation to fit budget',ctx)
    trials=[[True,True,False],[True,True,True],[False,True,False]]
    rel=reliability_metrics(trials)
    add('pass_all_vs_pass_any',rel['observed_pass_all_k']==1/3 and rel['observed_pass_any_k']==1,
        'pass all 3 vs any 3 are different reliability metrics',rel)
    open_journal=append_event([],{'run_id':'recover','actor':'parent','action':'dispatch','payload':{'task':'task42','child_run_id':'child-abc'}})
    rr=receipt_survival(open_journal,rec,'task42','child-abc')
    add('content_verified_result_not_automatically_committed',rr['status']=='eligible_for_parent_verification',
        'retained result can be considered on restart; no final answer or real persistence occurred',rr)
    return {'schema':'agent.atlas.casebook/1','version':'0.1.0','status':'passed' if all(c['passed'] for c in cases) else 'failed',
            'cases':cases,'case_count':len(cases),'live_agent_runs':0,'external_model_benchmarks':0,
            'independent_human_scientific_review':False}
