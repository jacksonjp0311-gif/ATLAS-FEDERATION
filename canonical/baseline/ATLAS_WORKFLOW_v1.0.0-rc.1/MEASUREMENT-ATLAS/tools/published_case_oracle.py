#!/usr/bin/env python3
"""Compare the local Decimal implementation with NumPy least squares.
Not an independent human review, laboratory replication or held-out study.
"""
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from measurement_atlas.published_case import load_case
from measurement_atlas.calibration import fit_polynomial
try:
 import numpy as np
except ImportError:
 print(json.dumps({'result':'not_run','reason':'Optional NumPy not installed'}));sys.exit(3)
rows,_,_,_=load_case();x=np.array([float(r['load']) for r in rows]);y=np.array([float(r['deflection']) for r in rows]);checks=[]
for degree in (1,2):
 f=fit_polynomial(x.tolist(),y.tolist(),degree=degree,x_unit='unspecified source unit',y_unit='unspecified source unit')
 z=(x-float(f.center))/float(f.scale);design=np.column_stack([z**i for i in range(degree+1)])
 coef=np.linalg.lstsq(design,y,rcond=None)[0];residual=y-design@coef;s=float(np.sqrt(residual@residual/(len(x)-degree-1)))
 checks.append({'degree':degree,'numpy_residual_sd':s,'decimal_residual_sd':str(f.residual_sd),
 'scaled_coefficients_max_abs_difference':float(max(abs(coef-np.array([float(c) for c in f.scaled_coefficients])))),
 'passed':bool(np.allclose(coef,[float(c) for c in f.scaled_coefficients],rtol=1e-10,atol=1e-12) and abs(s-float(f.residual_sd))<1e-13)})
r={'result':'passed' if all(c['passed'] for c in checks) else 'failed','numpy_version':np.__version__,'checks':checks,'independent_human_review':False,'physical_replication':False}
print(json.dumps(r,indent=2));sys.exit(0 if r['result']=='passed' else 2)
