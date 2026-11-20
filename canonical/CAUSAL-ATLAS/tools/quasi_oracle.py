"""Separate numerical algorithms on authored cases; not independent human review."""
from pathlib import Path
import argparse, json, platform, sys
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from causal_atlas.quasi import local_linear_jump, iv_population, fuzzy_local_ratio
from causal_atlas.quasi_cases import fuzzy_rd_rows


def run():
    try:
        import numpy as np
    except ImportError:
        return {'result':'not_run','reason':'Optional NumPy not installed'}
    # These tolerances and seeds are declared in code before this check is run.
    seed=3132026; tolerance=1e-10
    rng=np.random.default_rng(seed); failures=[]; count=0; largest=0.0
    def compare(got,want,case,key):
        nonlocal count,largest
        count+=1
        value=float(F(got)); error=abs(value-float(want))/max(1.0,abs(float(want)))
        largest=max(largest,error)
        if not np.isfinite(error) or error>tolerance:
            failures.append({'case':case,'quantity':key,'scaled_absolute_error':error})
    # Weighted least squares via NumPy SVD, rather than the local closed-form
    # 2x2 Fraction normal equations. Vary score origins, scales, asymmetry,
    # outcomes, noise, and kernels. Selected points are strictly in the window.
    for case in range(240):
        nleft=int(rng.integers(5,30)); nright=int(rng.integers(5,30))
        origin=int(rng.integers(-10000,10001)); scale=int(rng.integers(1,20))
        left=-rng.integers(1,101,nleft); right=rng.integers(1,101,nright)
        left[:2]=[-1,-100]; right[:2]=[1,100]
        xs=np.concatenate([left,right]); h=110*scale
        rows=[]
        for i,dx in enumerate(xs):
            base=int(rng.integers(-5,6)); # Independent non-exact-line response
            y=F(3+int(dx),20)+F(int(rng.integers(-30,31)),10)+base+(2 if dx>0 else 0)
            rows.append({'id':str(i),'x':str(origin+int(dx)*scale),'y':str(y)})
        kernel='triangular' if case%2 else 'uniform'
        got=local_linear_jump(rows,cutoff=origin,bandwidth=h,kernel=kernel,data_origin='synthetic_constructed')
        means={}
        for label,condition in [('left',lambda x:x<origin),('right',lambda x:x>=origin)]:
            selected=[r for r in rows if condition(float(F(r['x'])))]
            x=np.array([float(F(r['x'])) for r in selected]); u=(x-origin)/h
            y=np.array([float(F(r['y'])) for r in selected]); w=1-np.abs(u) if kernel=='triangular' else np.ones(len(u))
            design=np.column_stack((np.ones(len(u)),u)); root=np.sqrt(w)
            beta=np.linalg.lstsq(design*root[:,None],y*root,rcond=None)[0]
            rss=np.sum(w*(y-design@beta)**2); means[label]=beta[0]
            side=got['sides'][label]
            compare(side['intercept_at_cutoff'],beta[0],case,label+'_intercept')
            compare(side['slope_per_score_unit'],beta[1]/h,case,label+'_slope')
            compare(side['weighted_rss'],rss,case,label+'_rss')
            compare(side['kernel_weight_ess'],w.sum()**2/(w@w),case,label+'_kernel_ess')
        compare(got['jump'],means['right']-means['left'],case,'jump')
    # Direct enumeration of each synthetic joint potential-type population.
    # This comparison does not estimate individual compliance types from data.
    for case in range(200):
        raw=rng.integers(1,100,4); denominator=int(raw.sum()); types=[]
        masses=raw/denominator
        pairs=[(0,0),(1,1),(0,1),(1,0)]
        yy=rng.integers(-10,11,(4,2))/10; gg=rng.integers(-4,5,4)/100
        for j,(d0,d1) in enumerate(pairs):
            types.append(dict(name=str(j),mass=f'{int(raw[j])}/{denominator}',d0=d0,d1=d1,
                              y0=str(yy[j,0]),y1=str(yy[j,1]),direct_z=str(gg[j])))
        got=iv_population(types)
        ym=[];dm=[]
        for z in (0,1):
            outcome=0.;treatment=0.
            for j,(d0,d1) in enumerate(pairs):
                d=d1 if z else d0
                outcome+=masses[j]*(yy[j,d]+gg[j]*z);treatment+=masses[j]*d
            ym.append(outcome);dm.append(treatment)
        for z in (0,1):
            compare(got['supplied_means']['y_z'+str(z)],ym[z],case,'population_y'+str(z))
            compare(got['supplied_means']['d_z'+str(z)],dm[z],case,'population_d'+str(z))
        compare(got['population_ate'],np.dot(masses,yy[:,1]-yy[:,0]),case,'population_ate')
        compare(got['complier_effect'],yy[2,1]-yy[2,0],case,'complier_effect')
        compare(got['direct_contribution'],np.dot(masses,gg),case,'direct_contribution')
        if raw[2]!=raw[3]:
            compare(got['ratio'],(ym[1]-ym[0])/(dm[1]-dm[0]),case,'wald_ratio')
        elif got['ratio'] is not None:failures.append({'case':case,'quantity':'zero_first_stage_not_refused'})
    # A deterministic fuzzy example is checked using separate least-squares fits.
    rows=fuzzy_rd_rows();fit=fuzzy_local_ratio(rows,cutoff=0,bandwidth=4,kernel='triangular',minimum_first_stage=0,data_origin='synthetic_constructed')
    jumps={}
    for key in ('y','d'):
        intercepts=[]
        for side in (False,True):
            subset=[r for r in rows if (F(r['x'])>=0)==side]
            u=np.array([float(F(r['x']))/4 for r in subset]);values=np.array([float(F(r[key])) for r in subset]);weights=np.sqrt(1-np.abs(u))
            intercepts.append(np.linalg.lstsq(np.column_stack([np.ones(len(u)),u])*weights[:,None],values*weights,rcond=None)[0][0])
        jumps[key]=intercepts[1]-intercepts[0]
    compare(fit['ratio'],jumps['y']/jumps['d'],'fuzzy','ratio')
    return {'schema':'atlas.causal-quasi-oracle/1','result':'passed' if not failures else 'failed',
            'seed':seed,'weighted_line_datasets':240,'weighted_line_fits':480,'stipulated_populations':200,
            'fuzzy_datasets':1,'scalar_numeric_comparisons':count,'scaled_absolute_tolerance':tolerance,
            'max_scaled_absolute_error':largest,'failures':failures,'numpy_version':np.__version__,
            'python':platform.python_version(),'comparison_method':'NumPy SVD least squares and explicit population enumeration',
            'independent_human_review':False,'empirical_observations':False,'causal_assumptions_validated':False,
            'limits':'Author-generated development cases. No participant study, robust interval implementation or AI evaluation.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path);args=parser.parse_args();r=run();text=json.dumps(r,indent=2)
    if args.out:args.out.write_text(text+'\n')
    print(text);raise SystemExit(0 if r['result']=='passed' else 2)
