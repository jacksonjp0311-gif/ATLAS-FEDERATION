#!/usr/bin/env python3
"""Optional numerical comparison with mpmath quadrature/CDF at 60 decimal digits.

Independent arithmetic implementation, not independent human review or experiments.
"""
from pathlib import Path
import json,random,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from measurement_atlas.decisions import normal_conformance
try:import mpmath as mp
except ImportError:
    print(json.dumps({'result':'not_run','reason':'optional mpmath unavailable'}));raise SystemExit(2)
mp.mp.dps=60
rng=random.Random(12112026);failures=[];max_abs=0.;max_rel=0.;cases=[]
# z ranges cover both tails, the center, narrow intervals and single limits.
for i in range(320):
    lo=rng.uniform(-10,10);hi=lo+rng.uniform(.001,4)
    cases.append((lo,hi))
cases += [(None,x) for x in (-10,-9,-3,0,3,9,10)] + [(x,None) for x in (-10,-9,-3,0,3,9,10)]
for i,(lo,hi) in enumerate(cases):
    value=rng.uniform(-50,50);scale=10**rng.uniform(-2,2)
    lower=None if lo is None else value+lo*scale;upper=None if hi is None else value+hi*scale
    p=normal_conformance(value,scale,lower=lower,upper=upper,unit='mm',quantity_kind='length',model_basis='synthetic oracle fixture')['conditional_probability']
    # Recompute from exactly the supplied binary-float values, not unrecoverable decimal intent.
    zlo=-mp.inf if lower is None else (mp.mpf(lower)-mp.mpf(value))/mp.mpf(scale)
    zhi=mp.inf if upper is None else (mp.mpf(upper)-mp.mpf(value))/mp.mpf(scale)
    phi=lambda z:mp.erfc(-z/mp.sqrt(2))/2
    oracle=phi(zhi)-phi(zlo);expected=float(oracle)
    err=abs(p-expected);rel=err/max(abs(expected),1e-300);max_abs=max(max_abs,err);max_rel=max(max_rel,rel)
    passed=err<=2e-14 and (expected<1e-30 or rel<=1e-8)
    if not passed:failures.append({'case':i,'expected':expected,'actual':p,'absolute_error':err,'relative_error':rel})
r={'schema':'measurement.practical-oracle/1','result':'failed' if failures else 'passed','cases':len(cases),'seed':12112026,
   'mpmath_version':mp.__version__,'decimal_digits':60,'max_absolute_error':max_abs,'max_relative_error':max_rel,
   'absolute_tolerance':2e-14,'relative_tolerance_when_probability_above_1e_30':1e-8,'failures':failures,
   'independent_human_review':False,'physical_experiments':False}
print(json.dumps(r,indent=2));sys.exit(bool(failures))
