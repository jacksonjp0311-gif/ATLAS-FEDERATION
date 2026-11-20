"""Secondary NumPy/SciPy oracle for constructed Agent Atlas 0.2 methods.

Not a real agent trace, not a live-model benchmark and not independent human
scientific review. Random seed, exact fixture schemas and tolerances recorded.
"""
from pathlib import Path
import sys, json, random, math
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from agent_atlas.trace_science import analyze_trace,paired_eval,mast_annotation_summary,MAST_CODES
try:
    import numpy as np
    from scipy.stats import binomtest
except ImportError as ex:
    print(json.dumps({'status':'not_run','reason':'optional numpy/scipy unavailable','detail':str(ex)}));raise SystemExit(3)
seed=391126; rng=random.Random(seed)
counts={'trace_union':0,'paired_outcomes':0,'paired_exact_p':0,'mast_code_counts':0}
worst=0.0

def check(kind,a,b,tol=1e-12):
    global worst
    err=abs(float(a)-float(b));worst=max(worst,err)
    if not math.isfinite(err) or err>tol:raise AssertionError(f'{kind}: {a=} vs {b=} {err=}')
    counts[kind]+=1

# Independent mask over integer millisecond slots, rather than interval merge.
for j in range(350):
    children=[];x=[{'id':'root','parent_id':None,'kind':'agent','start_ms':0,'end_ms':100,'status':'success','evidence_ref':None}]
    for i in range(rng.randint(2,12)):
        start=rng.randrange(0,100);stop=rng.randrange(start,101)
        children.append((start,stop))
        x.append({'id':f'c{i}','parent_id':'root','kind':'tool','start_ms':start,'end_ms':stop,'status':'success','evidence_ref':'evidence'})
    r=analyze_trace(x)
    slots=np.zeros(100,dtype=bool)
    for lo,hi in children:slots[lo:hi]=True
    check('trace_union',r['overlap_aware_child_covered_ms'],int(np.count_nonzero(slots)))

# Published paired McNemar/sign logic compared with independently written scipy calculation.
for j in range(400):
    n=rng.randrange(1,50)
    b=np.array([rng.random()<.45 for _ in range(n)])
    c=np.array([rng.random()<.55 for _ in range(n)])
    tasks=[dict(task_id=f't{i}',baseline_success=bool(u),candidate_success=bool(v),
        baseline_cost=float(i),candidate_cost=float(i+1),split='evaluation') for i,(u,v) in enumerate(zip(b,c))]
    r=paired_eval(tasks)
    improved=int(np.count_nonzero(~b & c));regressed=int(np.count_nonzero(b & ~c));discord=improved+regressed
    check('paired_outcomes',r['observed_success_difference'],float(np.mean(c.astype(int)-b.astype(int))))
    expected=float(binomtest(improved,discord,.5,alternative='two-sided').pvalue) if discord else 1.0
    check('paired_exact_p',r['exact_two_sided_sign_p'],expected)

for j in range(140):
    n=rng.randrange(1,20)
    rows=[];matrix=np.empty((n,len(MAST_CODES)),dtype=float)
    for i in range(n):
        ann={}
        for c,k in enumerate(MAST_CODES):
            val=rng.choice([None,None,0,1])
            ann[k]=val;matrix[i,c]=np.nan if val is None else val
        rows.append(dict(trace_id=f'{i}',framework='synthetic',benchmark='none',annotation=ann))
    out=mast_annotation_summary(rows)
    for c,k in enumerate(MAST_CODES):
        check('mast_code_counts',out['codes'][k]['known'],int(np.count_nonzero(~np.isnan(matrix[:,c]))))
        check('mast_code_counts',out['codes'][k]['positive'],int(np.nansum(matrix[:,c])))

out={'schema':'atlas.agent-advanced-numerical-oracle/1','version':'0.2.0','status':'passed',
 'seed':seed,'comparisons':sum(counts.values()),'categories':counts,'largest_abs_error':worst,
 'numpy_version':np.__version__,'scipy_available':True,
 'actual_model_calls':0,'external_MAST_rows_read':0,'independent_human_review':False,
 'description':'Secondary algorithms for author-generated deterministic and randomized metadata examples; not a language-model improvement benchmark.'}
(Path(__file__).resolve().parents[1]/'evidence/numerical_oracle_v0.2.0.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
