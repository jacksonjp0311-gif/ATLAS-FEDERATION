"""Separate NumPy checks on authored random cases, not empirical validation."""
from pathlib import Path
import argparse,json,platform,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from causal_atlas.estimation import supplied_estimates,population_comparison,binary_missing_bounds

def run():
    try:import numpy as np
    except ImportError:return {'result':'not_run','reason':'optional NumPy missing'}
    rng=np.random.default_rng(12112026);failures=[];max_error=0.0;total=0
    for k in range(250):
        n=int(rng.integers(4,100));a=rng.integers(0,2,n);a[:2]=[0,1]
        y=rng.integers(-20,21,n);e=rng.integers(5,96,n)/100
        m0=rng.integers(-20,21,n)/5;m1=rng.integers(-20,21,n)/5;x=rng.integers(-5,6,n)
        rows=[{'id':str(i),'a':int(a[i]),'y':int(y[i]),'e':str(e[i]),'m0':str(m0[i]),'m1':str(m1[i]),'x':int(x[i])} for i in range(n)]
        got=supplied_estimates(rows,nuisance_origin='external_predictions')
        wt=a/e;wc=(1-a)/(1-e)
        want={'crude_difference':y[a==1].mean()-y[a==0].mean(),'outcome_regression':np.mean(m1-m0),
              'ipw_horvitz_thompson':np.dot(wt-wc,y)/n,'ipw_hajek':np.dot(wt,y)/wt.sum()-np.dot(wc,y)/wc.sum(),
              'aipw':np.mean(m1-m0)+np.dot(wt,y-m1)/n-np.dot(wc,y-m0)/n}
        from fractions import Fraction
        for key,target in want.items():
            err=abs(float(Fraction(got['estimates'][key]))-target)/max(1,abs(target));max_error=max(max_error,err);total+=1
            if err>1e-12:failures.append({'case':k,'quantity':key,'scaled_error':err})
    # Enumerate the complete joint law, rather than the implementation's
    # reduced stratum expectation expression. Working and true models differ.
    for k in range(150):
        strata=[];target=0;expect=0
        q0=int(rng.integers(1,100));qs=[q0/100,1-q0/100]
        for j,q in enumerate(qs):
            e,g,u0,u1,v0,v1=rng.integers(5,96,6)/100
            strata.append(dict(name=str(j),q=str(q0 if j==0 else 100-q0)+'/100',e=str(e),g=str(g),mu0=str(u0),mu1=str(u1),m0=str(v0),m1=str(v1)))
            target+=q*(u1-u0)
            for a in (0,1):
                u=u1 if a else u0
                for y in (0,1):
                    prob=q*(e if a else 1-e)*(u if y else 1-u)
                    score=(v1+a/g*(y-v1))-(v0+(1-a)/(1-g)*(y-v0))
                    expect+=prob*score
        result=population_comparison(strata)
        for key,want in [('aipw',expect),('true_ate',target),('aipw_bias',expect-target)]:
            err=abs(float(Fraction(result[key]))-want)/max(1,abs(want));max_error=max(max_error,err);total+=1
            if err>1e-12:failures.append({'population_case':k,'quantity':key,'scaled_error':err})
    # Exhaust possible missing successes for small binary counted populations.
    bound_cases=0
    for n0 in range(1,5):
        for n1 in range(1,5):
            for o0 in range(n0+1):
                for o1 in range(n1+1):
                    s0=o0//2;s1=(o1+1)//2
                    r=binary_missing_bounds({'0':dict(total=n0,observed=o0,successes=s0),'1':dict(total=n1,observed=o1,successes=s1)})
                    possibilities=[Fraction(s1+t,n1)-Fraction(s0+c,n0) for t in range(n1-o1+1) for c in range(n0-o0+1)]
                    want=[str(min(possibilities)),str(max(possibilities))];bound_cases+=1
                    if r['difference_bounds']!=want:failures.append({'bound_case':bound_cases})
    return {'schema':'atlas.causal-estimation-oracle/1','result':'passed' if not failures else 'failed','seed':12112026,
      'sample_cases':250,'synthetic_population_cases':150,'scalar_numeric_comparisons':total,'exhaustive_missing_bound_cases':bound_cases,
      'scaled_absolute_tolerance':1e-12,'max_scaled_absolute_error':max_error,'failures':failures,'numpy_version':np.__version__,
      'python':platform.python_version(),'independent_numerical_implementation':True,'independent_human_review':False,'empirical_observations':False,
      'limits':'Author-generated test distributions; no fitted-model benchmark, real causal effect, sampling coverage or AI quality evaluation.'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path);args=p.parse_args();r=run();text=json.dumps(r,indent=2)
    if args.out:args.out.write_text(text+'\n')
    print(text);raise SystemExit(0 if r['result']=='passed' else 2)
