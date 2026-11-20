"""Agent Atlas 0.3: bounded evidence-state and telemetry science.

No network, permissions, external tool effects, model invocations or independent
semantic verification. Input records are untrusted data and never instructions.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from math import isfinite, sqrt
import re
from .models import AgentModelError, _id
from .trace_science import MAST_CODES, analyze_trace

HEX16=re.compile(r'^[0-9a-f]{16}$')
HEX32=re.compile(r'^[0-9a-f]{32}$')
SEMANTIC_ATTRS={'gen_ai.operation.name','gen_ai.tool.name','gen_ai.agent.name','gen_ai.request.model','error.type'}
OPERATIONS={'invoke_agent','invoke_workflow','execute_tool','chat','plan','verification','generate_content'}


def _integer(v, label, minimum=0):
    if type(v) is not int or v < minimum or v > 10**20:
        raise AgentModelError(f'{label} must be a bounded integer')
    return v


def _identifier(v,pattern,label):
    if not isinstance(v,str) or not pattern.fullmatch(v):
        raise AgentModelError(f'{label} must be lowercase hex of correct length')
    return v


def _exact(x,keys,label):
    if not isinstance(x,dict) or set(x)!=keys:raise AgentModelError(f'{label} exact fields required')
    return x


def project_otel_metadata(rows:list[dict])->dict:
    """Validate a narrow subset of OTel GenAI spans, retaining no prompt content.

    All timestamps caller-supplied same epoch nanoseconds; caller data not signed.
    Deliberately rejects fields with prompts, output, tokens and tool arguments.
    """
    if not isinstance(rows,list) or not 1<=len(rows)<=2000:raise AgentModelError('1..2000 spans required')
    keys={'trace_id','span_id','parent_span_id','operation','start_ns','end_ns','status','tool_call_id','attributes'}
    by={};trace=None;canonical=[]
    for r in rows:
        _exact(r,keys,'OTel span')
        tr=_identifier(r['trace_id'],HEX32,'trace_id')
        if trace is None:trace=tr
        if trace!=tr:raise AgentModelError('multiple trace ids')
        sid=_identifier(r['span_id'],HEX16,'span_id')
        if sid in by:raise AgentModelError('duplicate span id')
        par=r['parent_span_id'];par=None if par is None else _identifier(par,HEX16,'parent_span_id')
        if r['operation'] not in OPERATIONS:raise AgentModelError('unknown operation')
        t0=_integer(r['start_ns'],'start_ns');t1=_integer(r['end_ns'],'end_ns')
        if t1<t0:raise AgentModelError('negative duration')
        if r['status'] not in {'ok','error','unset'}:raise AgentModelError('invalid span status')
        call=r['tool_call_id']
        if call is not None:call=_id(call)
        attrs=r['attributes']
        if not isinstance(attrs,dict) or not set(attrs)<=SEMANTIC_ATTRS:
            raise AgentModelError('unapproved/sensitive OTel attribute key')
        for name,value in attrs.items():
            if not isinstance(value,str) or len(value)>128:raise AgentModelError('non-string or oversized metadata attribute')
        if 'gen_ai.operation.name' in attrs and attrs['gen_ai.operation.name']!=r['operation']:
            raise AgentModelError('operation attribute conflicts with span')
        if r['operation']=='execute_tool' and not attrs.get('gen_ai.tool.name'):
            raise AgentModelError('tool span requires a tool name')
        by[sid]=r
        kind=('agent' if r['operation'] in {'invoke_agent','invoke_workflow'} else
              'tool' if r['operation']=='execute_tool' else
              'verification' if r['operation']=='verification' else 'model')
        mapped={'id':'s'+sid,'parent_id':None if par is None else 's'+par,
            'kind':kind,'start_ms':t0/1e6,'end_ms':t1/1e6,
            'status':'success' if r['status']=='ok' else 'failed' if r['status']=='error' else 'incomplete',
            'evidence_ref':None}
        canonical.append(mapped)
    result=analyze_trace(canonical,declared_success=False)
    executed=[r for r in rows if r['operation']=='execute_tool']
    return {'schema':'atlas.agent-otel-metadata/1','trace_id':trace,
        'spans':len(rows),'tool_spans':len(executed),'reported_successful_tool_spans':sum(r['status']=='ok' for r in executed),
        'root_elapsed_ms':result['root_elapsed_ms'],
        'overlap_aware_child_covered_ms':result['overlap_aware_child_covered_ms'],
        'status_counts':result['statuses'],
        'content_fields_retained':False,'external_tool_effects_verified':False,
        'semantic_success_verified':False,'adapter_scope':'narrow_agent_tool_model_span_metadata_subset',
        'limitations':['OTel conventions are evolving; this is not an arbitrary OTLP decoder',
                       'Reported span success is not provider-side effect verification',
                       'Unrecorded operations cannot be detected from this trace',
                       'Text, tool arguments, generated content and private identifiers are not retained']}


def recovery_decision(spec:dict)->dict:
    """Explain a conservative next step without performing it.

    Priority: operator Stop; uncertain externally submitted side effect; dependencies;
    verified goal; verification pending; retry admissibility; exhausted attempts.
    """
    _exact(spec,{'task_id','parent_dispatch_recorded','operator_stopped','dependency_state',
                 'worker_state','side_effect_state','verification_state','attempts','max_attempts'},'recovery')
    _id(spec['task_id'])
    for k in ('parent_dispatch_recorded','operator_stopped'):
        if type(spec[k]) is not bool:raise AgentModelError(k+' requires boolean')
    dep=spec['dependency_state'];worker=spec['worker_state'];eff=spec['side_effect_state'];ver=spec['verification_state']
    if dep not in {'ready','blocked'} or worker not in {'pending','failed','reported_success','running'} or eff not in {'none','prepared','submitted_unknown','reported_confirmed'} or ver not in {'none','pending','host_verified','host_rejected'}:
        raise AgentModelError('invalid state')
    tries=_integer(spec['attempts'],'attempts');limit=_integer(spec['max_attempts'],'max_attempts',1)
    if limit>1000 or tries>limit:raise AgentModelError('bounded attempts must not exceed limit')
    if spec['operator_stopped']:dec='respect_operator_stop'
    elif eff=='submitted_unknown':dec='reconcile_provider_before_resubmit'
    elif not spec['parent_dispatch_recorded']:dec='require_parent_dispatch'
    elif dep=='blocked':dec='await_dependency'
    elif ver=='host_verified' and worker!='reported_success':dec='escalate_conflicting_receipts'
    elif ver=='host_verified' and worker=='reported_success':dec='complete_with_host_evidence'
    elif ver=='host_rejected' and worker=='reported_success':dec='escalate_failed_verification'
    elif eff=='reported_confirmed' and worker=='failed':dec='reconcile_provider_receipt'
    elif worker=='reported_success' or ver=='pending':dec='verify_worker_result'
    elif worker in {'running','pending'}:dec='observe_running_worker'
    elif tries>=limit:dec='escalate_attempt_limit'
    else:dec='retry_may_be_considered'
    return {'schema':'atlas.agent-recovery-decision/1','task_id':spec['task_id'],'decision':dec,
       'executes_retry':False,'authorizes_external_tools':False,
       'provider_effects_proven':False,'host_truth_independently_verified':False,
       'limitations':['A host verification state is caller-reported and not cryptographically authenticated',
        'Retry admissibility is not a command, authorization, or guarantee of idempotency',
        'Unknown submitted external calls require reconciliation; operator Stop prevails']}


def grouped_mast_annotations(rows:list[dict])->dict:
    """Group actual-or-synthetic MAST schema metadata, never interpret text.

    For authentic public rows, supply key,trace_id,... and 14-code mapping; trace
    content is deliberately not accepted, stored, parsed or evaluated here.
    """
    if not isinstance(rows,list) or not 1<=len(rows)<=10000:raise AgentModelError('1..10000 rows required')
    grouped=defaultdict(list);seen=set()
    for row in rows:
        _exact(row,{'mas_name','llm_name','benchmark_name','trace_id','mast_annotation'},'MAST metadata')
        for k in ('mas_name','llm_name','benchmark_name'):_id(row[k])
        tid=row['trace_id'];_integer(tid,'trace_id')
        key=(row['mas_name'],row['llm_name'],row['benchmark_name'],tid)
        if key in seen:raise AgentModelError('duplicate composite trace id')
        seen.add(key)
        ann=row['mast_annotation'];_exact(ann,set(MAST_CODES),'MAST 14 codes')
        for v in ann.values():
            if not (v is None or type(v) is int and v in (0,1)):
                raise AgentModelError('MAST annotations 0, 1, or null')
        grouped[(row['mas_name'],row['benchmark_name'])].append(ann)
    out=[]
    for (framework,benchmark),items in sorted(grouped.items()):
        val={}
        for code in MAST_CODES:
            pos=sum(a[code]==1 for a in items)
            known=sum(a[code] is not None for a in items)
            val[code]={'known':known,'positive':pos,'unknown':len(items)-known,
                      'fraction_of_known':pos/known if known else None}
        out.append({'framework':framework,'benchmark':benchmark,'count':len(items),'codes':val})
    return {'schema':'atlas.agent-mast-grouped/1','rows':len(rows),'groups':out,
       'labels_are_caller_supplied':True,'published_label_origin':'LLM_judge_for_full_MAST_dataset',
       'human_ground_truth_verified':False,'population_failure_probability_estimated':False,
       'limitations':['0, 1 and null represent a model annotation, absence, and missingness respectively; null is not zero',
        'MAST may have unequal model/benchmark composition; conditional group proportions are not causal failure rates',
        'Human annotation rounds use incompatible taxonomy revisions; do not pool their codes with this 14-code schema']}


def repeatability_panel(rows:list[dict],*,repeats:int)->dict:
    """Descriptive pass^k per task, explicit whole-task matched repeats.

    Requires task_id, arm baseline/candidate, trial index, binary *reported* outcome,
    fixed split and metadata hashes, and caller-supplied evaluation validity flag.
    """
    nrep=_integer(repeats,'repeats',1)
    if not 1<=nrep<=20:raise AgentModelError('repeats 1..20')
    if not isinstance(rows,list) or not 2<=len(rows)<=4000:raise AgentModelError('2..4000 trial rows required')
    by=defaultdict(dict);taskmeta={};observed=set()
    fields={'task_id','arm','trial','reported_success','split','task_version','evaluator_version','cost_units'}
    for r in rows:
        _exact(r,fields,'trial record');tid=_id(r['task_id'])
        arm=r['arm'];split=r['split']
        if arm not in {'baseline','candidate'} or split not in {'development','evaluation'}:
            raise AgentModelError('arm/split')
        if type(r['reported_success']) is not bool:raise AgentModelError('reported_success boolean')
        trial=_integer(r['trial'],'trial')
        if trial>=nrep:raise AgentModelError('trial out of expected range')
        task_v=_id(r['task_version']);eval_v=_id(r['evaluator_version'])
        cost=r['cost_units']
        if type(cost) not in (float,int) or not isfinite(cost) or cost<0:raise AgentModelError('cost_units must be finite and nonnegative')
        key=(tid,arm,trial)
        if key in observed:raise AgentModelError('duplicate task/arm/trial')
        observed.add(key)
        meta=(split,task_v,eval_v)
        if tid in taskmeta and taskmeta[tid]!=meta:raise AgentModelError('task/split/evaluator mismatch across arms')
        taskmeta[tid]=meta
        by[(tid,arm)][trial]=(r['reported_success'],cost)
    taskids=sorted(taskmeta)
    for tid in taskids:
        for arm in ['baseline','candidate']:
            if set(by[(tid,arm)])!=set(range(nrep)):raise AgentModelError('incomplete matched repetition set')
    panels=[];group={'baseline':0,'candidate':0};cost_totals={'baseline':0.,'candidate':0.}
    for tid in taskids:
        p={'task_id':tid,'split':taskmeta[tid][0]}
        for arm in ('baseline','candidate'):
            trials=[by[(tid,arm)][i] for i in range(nrep)]
            anypass=any(v[0] for v in trials);allpass=all(v[0] for v in trials)
            p[arm]={'pass_any':anypass,'pass_all':allpass,'successes':sum(v[0] for v in trials),
                    'total_cost_units':sum(v[1] for v in trials)}
            group[arm]+=allpass;cost_totals[arm]+=sum(v[1] for v in trials)
        panels.append(p)
    n=len(taskids)
    return {'schema':'atlas.agent-repeatability/1','tasks':n,'repeats_per_arm':nrep,
        'splits':dict(Counter(x['split'] for x in panels)),
        'observed_all_pass_task_fraction':{arm:group[arm]/n for arm in group},
        'total_cost_units':cost_totals,'tasks_detail':panels,
        'claim_of_model_improvement_verified':False,'paired_evaluation_ground_truth_authenticated':False,
        'limitations':['Outcomes are caller-provided reports; evaluator validity, task correctness, cost, and leakage are unverified',
          'All-pass over repeated trials is not the single-trial pass rate; tasks and seeds must be sampled as designed',
          'Development and evaluation splits cannot be mixed for a clean held-out claim',
          'No causal effect or statistical generalization claim follows without a sampling/evaluation design']}
