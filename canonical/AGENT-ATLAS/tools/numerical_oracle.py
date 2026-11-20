"""Independent numeric/graph comparisons, original synthetic inputs only.

Optional NumPy and NetworkX, not benchmark performance or science validation.
"""
import json,sys,random,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
try:
    import numpy as np
    import networkx as nx
except ImportError as e:
    print(json.dumps({'result':'not_run','reason':str(e)}));raise SystemExit(2)
from agent_atlas.models import validate_graph,reliability_metrics,append_event,verify_ledger,select_qualified_memories
rng=random.Random(20261113)
counts={'graph_critical_cost':0,'topology_constraints':0,'pass_all':0,'pass_any':0,'per_trial':0,'memory_budget':0,'journal_digest':0}
for i in range(400):
    n=rng.randint(1,35);tasks=[];g=nx.DiGraph();g.add_node('START')
    for j in range(n):
        key=f't{j}';deps=[f't{k}' for k in range(j) if rng.random()<.085];cost=rng.randint(1,20)
        tasks.append({'id':key,'depends_on':deps,'priority':rng.uniform(-20,20),'estimated_cost':cost})
        g.add_edge('START',key,weight=cost)
        for d in deps:g.add_edge(d,key,weight=cost)
    p=validate_graph(tasks)
    expected=float(nx.dag_longest_path_length(g,weight='weight'))
    if abs(p['critical_path_cost']-expected)>1e-9:raise AssertionError('critical path mismatch')
    counts['graph_critical_cost']+=1
    order={name:j for j,name in enumerate(p['order'])}
    if any(order[dep]>=order[t['id']] for t in tasks for dep in t['depends_on']):raise AssertionError('bad topological order')
    counts['topology_constraints']+=1
for i in range(500):
    n=rng.randint(1,100);k=rng.randint(1,12)
    rows=[[rng.random()>.2 for j in range(k)] for t in range(n)]
    result=reliability_metrics(rows);arr=np.array(rows,dtype=np.bool_)
    goals=[('pass_all',float(np.mean(np.all(arr,axis=1))),result['observed_pass_all_k']),
           ('pass_any',float(np.mean(np.any(arr,axis=1))),result['observed_pass_any_k']),
           ('per_trial',float(np.mean(arr)),result['per_trial_mean'])]
    for name,expected,actual in goals:
        if abs(expected-actual)>1e-12:raise AssertionError(name)
        counts[name]+=1
for i in range(400):
    mem=[{'id':f'm{j}','source_id':f's{j}','relevance':rng.random(),'recency':rng.random(),
          'importance':rng.random(),'tokens':rng.randint(1,15),'qualifier':'not independently reviewed'} for j in range(rng.randint(0,25))]
    budget=rng.randint(0,35);result=select_qualified_memories(mem,budget_tokens=budget)
    cost=sum(item['tokens'] for item in result['admitted'])
    if cost>budget or cost+result['remaining']!=budget:raise AssertionError('budget miscount')
    if any(item['qualifier']!='not independently reviewed' for item in result['admitted']):raise AssertionError('qualifier stripped')
    counts['memory_budget']+=1
for i in range(500):
    entry={'actor':'parent','action':'checkpoint','run_id':f'r{i}','payload':{'x':i,'y':'observed'}}
    e=append_event([],entry)[0]
    body={k:e[k] for k in ('sequence','prev_hash','run_id','actor','action','payload')}
    digest=hashlib.sha256(json.dumps(body,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf8')).hexdigest()
    if digest!=e['hash'] or not verify_ledger([e]):raise AssertionError('sha mismatch')
    counts['journal_digest']+=1
out={'schema':'atlas.agent-model-oracle/1','result':'passed','seed':20261113,'total_checks':sum(counts.values()),
     'counts':counts,'numpy_version':np.__version__,'networkx_version':nx.__version__,
     'origin':'independent_numeric_and_graph_algorithms_on_author_generated_data',
     'real_llm_calls':0,'real_tool_calls':0,'independent_scientific_review':False,
     'limitations':['No performance benchmark or real external task evaluation','NetworkX check validates supplied cost graph, not a live scheduler']}
(ROOT/'evidence/numerical_oracle_v0.1.0.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
