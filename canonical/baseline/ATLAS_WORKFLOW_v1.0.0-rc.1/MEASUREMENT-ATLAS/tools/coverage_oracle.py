#!/usr/bin/env python3
"""Optional independent-algorithm numerical comparison; SciPy is developer-only.

Not independent human review and not a metrology certification. Tolerances are
written in this script, not expanded after a comparison failure.
"""
from pathlib import Path
import sys,json,math,platform
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))

def run():
    try:
        import numpy as np
        import scipy
        from scipy.stats import t
        from scipy.optimize import brentq
    except ImportError:
        return {'result':'not_run','reason':'NumPy/SciPy developer dependencies unavailable'}
    from measurement_atlas.coverage import coverage_factor,student_t_survival
    from measurement_atlas.intervals import reproduce_interval
    from measurement_atlas.published_case import load_case
    df_values=[1,1.25,2,2.5,4,8,10.75,37,194,1000,10000]
    probabilities=[.5,.6827,.8,.9,.95,.9545,.975,.99,.9973,.9999]
    diffs=[];max_error=0.;checks=0
    for df in df_values:
        for p in probabilities:
            actual=coverage_factor(p,df);expected=float(t.ppf((1+p)/2,df));error=abs(actual-expected)/max(1,abs(expected))
            max_error=max(max_error,error);checks+=1
            if error>2e-9:diffs.append({'df':df,'p':p,'actual':actual,'expected':expected,'relative_error':error})
    # SRD140_PUBLIC_WITHHELD: Pontius inverse comparisons unavailable.
    return {'result':'partial_rights_withheld' if not diffs else 'failed',
        'kind':'independent_numerical_algorithms_not_independent_review','scipy_version':scipy.__version__,'numpy_version':np.__version__,
        'python':platform.python_version(),'quantile_cases':checks,'quantile_max_scaled_absolute_error':max_error,
        'quantile_tolerance':2e-9,'quantile_failures':diffs,'numpy_scipy_inverse':None,
        'inverse_absolute_errors_source_units':None,'inverse_absolute_tolerance':1e-5,
        'publisher_agreement':None,'public_edition_notice':'Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.','independent_human_review':False}
if __name__=='__main__':
    r=run();print(json.dumps(r,indent=2));sys.exit(0 if r['result']=='passed' else 2)
