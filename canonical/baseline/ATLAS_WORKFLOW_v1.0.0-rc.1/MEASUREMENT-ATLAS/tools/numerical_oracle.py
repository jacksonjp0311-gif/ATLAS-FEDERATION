#!/usr/bin/env python3
"""Optional NumPy comparison of declared first-order calculations; not laboratory evidence."""
from pathlib import Path
import json,sys,math
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import numpy as np
from measurement_atlas.uncertainty import combine_linear
rng=np.random.default_rng(86422);cases=0;max_relative_error=0.0;invalid=0
for n in range(1,9):
 for i in range(15):
  A=rng.normal(size=(n,n));C=A@A.T+np.eye(n)*.1;c=rng.normal(size=n)
  for scale in [1e-120,1e-12,1.,1e12,1e120]:
   scaled=C*scale;expected=float(c@scaled@c);actual=combine_linear(c.tolist(),scaled.tolist())['variance']
   error=abs(actual-expected)/max(abs(expected),1e-300);max_relative_error=max(max_relative_error,error);cases+=1
   if not math.isclose(actual,expected,rel_tol=1e-10,abs_tol=0):raise AssertionError((n,i,scale,error))
for scale in [1e-120,1e-12,1.,1e12,1e120]:
 try:combine_linear([1,-1],[[scale,2*scale],[2*scale,scale]])
 except ValueError:invalid+=1
 else:raise AssertionError('invalid covariance accepted')
print(json.dumps({'kind':'numpy_numerical_crosscheck','result':'passed','seed':86422,'numpy_version':np.__version__,'positive_definite_cases':cases,'invalid_cases_rejected':invalid,'max_relative_error':max_relative_error,'independent_human_review':False,'physical_measurements':False},indent=2))
