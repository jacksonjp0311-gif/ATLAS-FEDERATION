#!/usr/bin/env python3
"""Fixed-seed normal-model stress test. Not experimental data or held-out research.

Compare t intervals, the unjustified k=2 shortcut at n=5, and omission of a
shared per-trial random offset. Only the first model meets the iid-normal mean
interval assumptions. Rates are sampled estimates with Monte Carlo uncertainty.
"""
from pathlib import Path
import sys,json,math
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from measurement_atlas.coverage import coverage_factor

def run(trials=20000,seed=7132026):
    try:import numpy as np
    except ImportError:return {'result':'not_run','reason':'NumPy optional developer dependency missing'}
    rng=np.random.default_rng(seed);n=5
    noise=rng.normal(0,1,(trials,n));mean=noise.mean(axis=1);se=noise.std(axis=1,ddof=1)/math.sqrt(n);k=coverage_factor(.95,n-1)
    common=rng.normal(0,.75,trials)
    def report(name,flags):
        count=int(sum(flags));p=count/trials;z=1.959963984540054;den=1+z*z/trials
        ctr=(p+z*z/(2*trials))/den;half=z*math.sqrt(p*(1-p)/trials+z*z/(4*trials**2))/den
        return {'case':name,'covered':count,'trials':trials,'rate':p,'monte_carlo_se':math.sqrt(p*(1-p)/trials),
                'wilson_95_interval_for_simulated_rate':[ctr-half,ctr+half]}
    cases=[report('iid_normal_student_t',np.abs(mean)<=k*se),report('iid_normal_k_equals_2',np.abs(mean)<=2*se),
           report('shared_offset_omitted_from_budget',np.abs(mean+common)<=k*se)]
    expected=.95;ok=abs(cases[0]['rate']-expected)<=.012
    return {'result':'passed' if ok else 'failed','seed':seed,'n':n,'cases':cases,'student_t_factor':k,
       'predeclared_iid_rate_acceptance':[.938,.962],'shared_offset_sd':.75,'numpy_version':np.__version__,
       'synthetic':True,'physical_validation':False,'independent_held_out':False,
       'limitations':['A seeded normal simulation cannot validate real measurement distributions or calibration stability.',
          'Shared bias is deliberately omitted only to demonstrate a violated assumption; no new measurement capability is proved.']}
if __name__=='__main__':
    r=run();print(json.dumps(r,indent=2));sys.exit(0 if r['result']=='passed' else 2)
