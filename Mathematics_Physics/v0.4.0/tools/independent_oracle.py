"""Independent NumPy crosschecks on original invented mathematical examples.

Not physical measurements, actual AI training, primary-source acquisition, or
independent scientific peer review. Counts are per comparison, not experiments.
"""
import sys,json,random,math
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from math_physics_atlas.models import *

rng=random.Random(20261115);count={};biggest=0.
def compare(k,a,b,rtol=1e-8):
 global biggest
 a=float(a);b=float(b);err=abs(a-b);biggest=max(biggest,err)
 if not all(map(math.isfinite,[a,b,err])) or err>rtol*max(1,abs(a),abs(b)):
  raise AssertionError((k,a,b,err))
 count[k]=count.get(k,0)+1
for _ in range(1000):
 x=[rng.uniform(-50,50) for _ in range(5)];y=[rng.uniform(-50,50) for _ in range(5)]
 compare('dot_numpy',dot(x,y),float(np.dot(x,y)))
for _ in range(1000):
 a=[[rng.uniform(-3,3) for _ in range(3)] for _ in range(2)]
 b=[[rng.uniform(-3,3) for _ in range(2)] for _ in range(3)]
 z=matrix_multiply(a,b);ref=np.asarray(a)@np.asarray(b)
 # A cell chosen from independently implemented NumPy matmul per trial
 i=rng.randrange(2);j=rng.randrange(2)
 compare('matrix_numpy',z[i][j],ref[i,j])
for _ in range(1000):
 c=[rng.uniform(-5,5) for _ in range(5)];x=rng.uniform(-2,2)
 compare('polynomial_derivative_numpy',polynomial_value(polynomial_derivative(c),x),float(np.polyval(np.polyder(np.asarray(c)[::-1]),x)))
for _ in range(1000):
 c=[rng.uniform(-3,3) for _ in range(4)];a=rng.uniform(-2,0);b=rng.uniform(0,2)
 exact=integrate_polynomial(c,a,b);approx=simpson_polynomial(c,a,b,12)
 compare('simpson_cubic_numpy',approx,exact)
for _ in range(1000):
 y0=rng.uniform(-5,5);a=rng.uniform(-1,0);b=rng.uniform(-1,1);t=rng.uniform(0,1)
 r=rk4_linear(y0,a,b,t,100)
 compare('rk4_analytic',r['numerical_y'],r['analytic_reference'],rtol=2e-6)
for _ in range(1000):
 vals=[rng.uniform(-2,2) for _ in range(8)]
 ours=discrete_fourier(vals);other=np.fft.fft(np.array(vals))
 k=rng.randrange(len(vals));compare('dft_numpy_complex_magnitude',abs(ours[k]),abs(other[k]))
for _ in range(1000):
 prior=rng.uniform(.01,.99);lik1=rng.uniform(.01,.99);lik0=rng.uniform(.01,.99)
 got=bayes_binary(prior,lik1,lik0)['posterior_H1']
 compare('bayes_numpy',got,float(np.dot([prior,0],[lik1,lik0]))/np.dot([prior,1-prior],[lik1,lik0]))
for _ in range(1000):
 v=[rng.uniform(-1200,1200) for _ in range(7)];x=stable_softmax(v)
 yy=np.asarray(v);yy=np.exp(yy-np.max(yy));yy/=np.sum(yy)
 i=rng.randrange(7);compare('softmax_numpy',x[i],float(yy[i]))
for _ in range(1000):
 # Independent batched Hessian-gradient linear algebra for a valid strictly SPD case.
 q1=rng.uniform(1,4);q2=rng.uniform(1,4);eta=rng.uniform(.01,.15)
 vals=[rng.uniform(-2,2),rng.uniform(-2,2)];ini=[rng.uniform(-2,2),rng.uniform(-2,2)];A=[[q1,0],[0,q2]]
 ours=quadratic_gradient_descent(A,vals,eta,20,ini)['solution']
 x=np.asarray(ini,dtype=float);mat=np.array(A,dtype=float);b=np.asarray(vals,dtype=float)
 for _j in range(20):x=x-eta*(mat@x-b)
 compare('gradient_descent_numpy',ours[0],float(x[0]))
for _ in range(1000):
 x=rng.uniform(-3,3);v=rng.uniform(-3,3);a=rng.uniform(-3,3);t=rng.uniform(0,3)
 r=newtonian_kinematics(x,v,a,t)
 compare('kinematics_numpy',r['position_m'],float(np.polyval([.5*a,v,x],t)))
for _ in range(124):
 a=rng.uniform(-3,3);b=rng.uniform(-3,3);u_a=rng.uniform(.1,.9);u_b=rng.uniform(.1,.9)
 cov=rng.uniform(-.8,.8)*u_a*u_b
 r=uncertainty_product(a,b,u_a,u_b,cov)
 compare('uncertainty_covariance_numpy',r['standard_uncertainty'],math.sqrt(max(0.,b*b*u_a*u_a+a*a*u_b*u_b+2*a*b*cov)))
report={'schema':'atlas.math-physics-independent-oracle/1','result':'passed','comparisons':sum(count.values()),'counts':count,'seed':20261115,
    'max_absolute_difference':biggest,'numpy':np.__version__,'original_material_data_imported':0,
    'real_physical_experiments':0,'independent_scientific_review':False,
    'limitations':['NumPy and analytic arithmetic comparisons test finite math methods under authored inputs, not broad scientific validity',
      'Multiple per-value comparisons are not independent laboratory experiments or AI performance measurements']}
path=Path(__file__).resolve().parents[1]/'evidence/independent_numeric_oracle_v0.1.0.json'
path.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
