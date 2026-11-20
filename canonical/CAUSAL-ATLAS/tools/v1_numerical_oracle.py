# Public derivative redaction: ucb_admissions_redistribution_unresolved
"""Independent NumPy numerical checks for declared models; not scientific review.

Deterministic generated model inputs, no experimental results or causal discovery.
Run from a source checkout with optional NumPy installed.
"""
import json, random, sys
from fractions import Fraction as F
from pathlib import Path
from causal_atlas.advanced import longitudinal_gformula, mediation_interventional, transport_strata, independent_binary_contrast, berkeley_admissions
from causal_atlas.advanced_cases import CASES


def check():
    try:
        import numpy as np
    except ImportError:
        return {'result':'not_run','reason':'Optional NumPy not installed','independent_science_review':False}
    rng=random.Random(971126)
    counts={'longitudinal':0,'mediation':0,'transport':0,'binomial':0,'berkeley':0}; max_error=0.0
    def compare(got,want):
        nonlocal max_error
        err=abs(float(got)-float(want))
        scale=max(1.0,abs(float(want)))
        max_error=max(max_error,err/scale)
        if err>1e-11*scale:raise AssertionError(f'numerical deviation {got=} {want=} {err=}')
    for _ in range(120):
        qs=[rng.randint(1,20) for _ in range(3)];q_total=sum(qs)
        strata=[];w=[];trans=[];response=[]
        for j,q in enumerate(qs):
            ps=[rng.randint(1,19) for _ in range(2)]
            ys={f'{a}{b}{l}':F(rng.randint(1,19),20) for a in range(2) for b in range(2) for l in range(2)}
            strata.append({'id':f's{j}','q':str(F(q,q_total)), 'p_l1_by_a0':{str(a):str(F(ps[a],20)) for a in range(2)},'outcome_risks':{k:str(v) for k,v in ys.items()}})
            w.append(q/q_total); trans.append([x/20 for x in ps]);response.append([[[float(ys[f'{a}{b}{l}']) for l in range(2)] for b in range(2)] for a in range(2)])
        r=longitudinal_gformula({'strata':strata,'compare':{'regime_a':[1,1],'regime_b':[0,0]}})
        w=np.array(w);trans=np.array(trans);response=np.array(response)
        for a in range(2):
            for b in range(2):
                value=np.sum(w * ((1-trans[:,a])*response[:,a,b,0]+trans[:,a]*response[:,a,b,1]))
                compare(F(r['static_regime_risks'][f'{a}{b}']),float(value));counts['longitudinal']+=1
    for _ in range(120):
        x={'mediator_prob':{str(a):str(F(rng.randint(1,19),20)) for a in range(2)},'outcome_risk':{f'{a}{m}':str(F(rng.randint(1,19),20)) for a in range(2) for m in range(2)}}
        r=mediation_interventional(x)
        p=np.array([float(F(x['mediator_prob'][str(a)])) for a in range(2)])
        y=np.array([[float(F(x['outcome_risk'][f'{a}{m}'])) for m in range(2)] for a in range(2)])
        v=lambda a,d:np.dot(np.array([1-p[d],p[d]]),y[a,:])
        compare(F(r['contrast_total']),v(1,1)-v(0,0))
        compare(F(r['interventional_direct_component']),v(1,0)-v(0,0))
        compare(F(r['interventional_indirect_component']),v(1,1)-v(1,0))
        counts['mediation']+=3
    for _ in range(120):
        sw=[rng.randint(1,15) for _ in range(4)];tw=[rng.randint(1,15) for _ in range(4)]
        rows=[];dif=[]
        for j in range(4):
            p0=F(rng.randint(0,17),20);p1=F(rng.randint(2,20),20)
            rows.append({'id':f'group{j}','source_share':str(F(sw[j],sum(sw))),'target_share':str(F(tw[j],sum(tw))),'source_mean_0':str(p0),'source_mean_1':str(p1)})
            dif.append(float(p1-p0))
        r=transport_strata({'strata':rows})
        compare(F(r['source_contrast']),np.dot(np.array(sw,dtype=float)/sum(sw),np.array(dif)))
        compare(F(r['target_contrast']),np.dot(np.array(tw,dtype=float)/sum(tw),np.array(dif)))
        counts['transport']+=2
    from statistics import NormalDist
    for _ in range(120):
        n0=rng.randint(80,200);n1=rng.randint(80,200)
        x0=rng.randint(n0//4,3*n0//4);x1=rng.randint(n1//4,3*n1//4)
        x={'group_0':{'successes':x0,'total':n0},'group_1':{'successes':x1,'total':n1},'confidence':'0.95'}
        r=independent_binary_contrast(x)
        p0=x0/n0;p1=x1/n1;se=(p0*(1-p0)/n0+p1*(1-p1)/n1)**.5
        expect=(p1-p0, se)
        compare(F(r['difference']),expect[0]);compare(r['standard_error'],expect[1])
        counts['binomial']+=2
    # UCBAdmissions comparisons omitted pending dataset redistribution clearance.
    return {'schema':'atlas.causal-v1-numerical-oracle/1','result':'partial_public_derivative', 'python':sys.version.split()[0], 'numpy_version':np.__version__, 'seed':971126,'comparisons':sum(counts.values()),'methods':counts,'maximum_scaled_absolute_error':max_error,'tolerance':1e-11, 'data_origin':'seeded_synthetic_models_only_public_derivative', 'causal_identification_verified':False,'independent_science_review':False,'held_out_evaluation':False}

if __name__=='__main__':
    print(json.dumps(check(),indent=2))
