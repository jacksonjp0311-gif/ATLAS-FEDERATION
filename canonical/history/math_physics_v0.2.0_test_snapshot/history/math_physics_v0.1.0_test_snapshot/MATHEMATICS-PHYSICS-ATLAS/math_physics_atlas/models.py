"""Mathematics & Fundamental Physics Atlas 0.1: offline mathematical kernel.

All values are stipulated examples, not calibrated physical measurements.
Finite, bounded deterministic methods for reconstructing computer science and AI.
"""
from __future__ import annotations
from fractions import Fraction
from math import sqrt, sin, cos, exp, log, factorial, pi, fsum, isfinite, comb, floor
from cmath import exp as cexp
from typing import Sequence

C_LIGHT=299792458.0            # exact SI defining value m/s
PLANCK=6.62607015e-34         # exact SI defining value J*s
E_CHARGE=1.602176634e-19      # exact SI defining value C
BOLTZMANN=1.380649e-23        # exact SI defining value J/K

class ModelDomainError(ValueError): pass

def real(value,name,low=None,high=None):
    if type(value) not in (int,float,Fraction) or not isfinite(float(value)):raise ModelDomainError(name+' must be finite real')
    x=float(value)
    if low is not None and x<low:raise ModelDomainError(name+' below allowed range')
    if high is not None and x>high:raise ModelDomainError(name+' above allowed range')
    return x

def positive(value,name):
    x=real(value,name,0)
    if x<=0:raise ModelDomainError(name+' must be positive')
    return x

def finite_vector(v,length=None):
    if not isinstance(v,(list,tuple)) or not 1<=len(v)<=1000:raise ModelDomainError('vector 1..1000 items required')
    if length is not None and len(v)!=length:raise ModelDomainError('vector dimensions differ')
    return [real(t,'vector entry') for t in v]

def finite_matrix(mat,max_size=64):
    if not isinstance(mat,(list,tuple)) or not 1<=len(mat)<=max_size:raise ModelDomainError('bounded matrix rows')
    width=None;rows=[]
    for row in mat:
        values=finite_vector(row)
        if width is None:width=len(values)
        if len(values)!=width or width>max_size:raise ModelDomainError('rectangular bounded matrix')
        rows.append(values)
    return rows

def dot(a,b):
    x=finite_vector(a);y=finite_vector(b,len(x));return fsum(p*q for p,q in zip(x,y))

def matrix_multiply(A,B):
    a=finite_matrix(A);b=finite_matrix(B)
    if len(a[0])!=len(b):raise ModelDomainError('incompatible matrix dimensions')
    return [[fsum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def transpose(A):
    m=finite_matrix(A);return [list(row) for row in zip(*m)]

def rational_solve(A,b):
    """Exact Gaussian elimination for finite rational inputs; rejects singularity."""
    if not isinstance(A,list) or not 1<=len(A)<=32 or any(not isinstance(row,list) or len(row)!=len(A) for row in A):raise ModelDomainError('square rational matrix required')
    if not isinstance(b,list) or len(b)!=len(A):raise ModelDomainError('matching right hand vector')
    def rational(v):
        if type(v) not in (int,Fraction) or abs(v)>10**12:raise ModelDomainError('exact bounded integer or Fraction required')
        return Fraction(v)
    n=len(A);aug=[[rational(v) for v in row]+[rational(b[i])] for i,row in enumerate(A)]
    for col in range(n):
        pivot=next((r for r in range(col,n) if aug[r][col]!=0),None)
        if pivot is None:raise ModelDomainError('singular or underdetermined rational system')
        aug[col],aug[pivot]=aug[pivot],aug[col];div=aug[col][col]
        aug[col]=[t/div for t in aug[col]]
        for r in range(n):
            if r!=col and aug[r][col]!=0:
                mul=aug[r][col];aug[r]=[v-mul*w for v,w in zip(aug[r],aug[col])]
    x=[row[-1] for row in aug]
    assert all(sum(Fraction(v)*x[j] for j,v in enumerate(row))==Fraction(b[i]) for i,row in enumerate(A))
    return {'solution_fractions':[str(t) for t in x],'solution_floats':[float(t) for t in x],
     'exact_residual_zero':True,'scope':'unique square rational linear system, not general overdetermined fitting'}

def least_squares(A,b):
    """Pedagogical normal-equations method; ill-conditioned systems refused."""
    m=finite_matrix(A);v=finite_vector(b,len(m));n=len(m[0])
    if len(m)<n:raise ModelDomainError('underdetermined least squares not implemented')
    ata=matrix_multiply(transpose(m),m);atb=[dot(row,v) for row in transpose(m)]
    aug=[ata[i]+[atb[i]] for i in range(n)]
    scale=max(abs(a) for row in ata for a in row)
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(aug[i][k]));aug[k],aug[p]=aug[p],aug[k]
        if abs(aug[k][k])<1e-11*max(1,scale):raise ModelDomainError('rank deficient / ill-conditioned normal equations')
        c=aug[k][k]
        for j in range(k,n+1):aug[k][j]/=c
        for i in range(n):
            if i!=k:
                w=aug[i][k]
                for j in range(k,n+1):aug[i][j]-=w*aug[k][j]
    x=[aug[i][-1] for i in range(n)]
    residual=[dot(row,x)-v[i] for i,row in enumerate(m)]
    return {'parameters':x,'squared_residual':dot(residual,residual),'normal_equation_residual':
       [dot(row,residual) for row in transpose(m)],
       'limitations':['Normal equations square the condition number; use stable QR/SVD on real data',
                      'No physical model or independent fitted dataset verified']}

def projection(v,basis):
    v=finite_vector(v);u=finite_vector(basis,len(v));d=dot(u,u)
    if d<=0:raise ModelDomainError('zero projection axis')
    coeff=dot(v,u)/d;proj=[coeff*t for t in u];res=[v[i]-proj[i] for i in range(len(v))]
    return {'projected':proj,'perpendicular_residual':res,'coefficient':coeff,'orthogonality_residual':dot(res,u)}

def polynomial_value(coefficients,x):
    a=finite_vector(coefficients);t=real(x,'x');result=0.
    for c in reversed(a):result=result*t+c
    return result

def polynomial_derivative(coefficients):
    a=finite_vector(coefficients)
    return [i*a[i] for i in range(1,len(a))] if len(a)>1 else [0.]

def central_difference_polynomial(coefficients,x,h):
    step=positive(h,'step');t=real(x,'x');return (polynomial_value(coefficients,t+step)-polynomial_value(coefficients,t-step))/(2*step)

def integrate_polynomial(coefficients,a,b):
    c=finite_vector(coefficients);a=real(a,'a');b=real(b,'b')
    return fsum(co/(j+1)*(b**(j+1)-a**(j+1)) for j,co in enumerate(c))

def simpson_polynomial(coefficients,a,b,n):
    if type(n)!=int or not 2<=n<=20000 or n%2:raise ModelDomainError('positive even number of intervals required')
    a=real(a,'a');b=real(b,'b');dx=(b-a)/n
    vals=[polynomial_value(coefficients,a+i*dx) for i in range(n+1)]
    return dx/3*(vals[0]+vals[-1]+4*fsum(vals[i] for i in range(1,n,2))+2*fsum(vals[i] for i in range(2,n-1,2)))

def linear_ode_exact(y0,a,b,t):
    y=real(y0,'y0');aa=real(a,'a');bb=real(b,'b');tt=real(t,'t',0)
    return y*exp(aa*tt)+bb*tt if aa==0 else (y+bb/aa)*exp(aa*tt)-bb/aa

def rk4_linear(y0,a,b,t,steps):
    y=real(y0,'y0');a=real(a,'a');b=real(b,'b');t=real(t,'duration',0)
    if type(steps)!=int or not 1<=steps<=20000:raise ModelDomainError('bounded positive steps')
    h=t/steps
    for _ in range(steps):
        k1=a*y+b;k2=a*(y+h*k1/2)+b;k3=a*(y+h*k2/2)+b;k4=a*(y+h*k3)+b
        y+=h/6*(k1+2*k2+2*k3+k4)
        if not isfinite(y):raise ModelDomainError('ODE divergence/nonfinite state')
    return {'numerical_y':y,'analytic_reference':linear_ode_exact(y0,a,b,t),'steps':steps,
            'scope':'scalar linear yprime=ay+b with constant a,b, no general ODE guarantees'}

def discrete_fourier(values):
    x=finite_vector(values)
    if len(x)>128:raise ModelDomainError('O(n²) transform resource cap')
    n=len(x);return [sum(v*cexp(-2j*pi*k*t/n) for t,v in enumerate(x)) for k in range(n)]

def spectral_energy(values):
    x=finite_vector(values);X=discrete_fourier(x)
    return {'time_energy':fsum(t*t for t in x),'frequency_energy':fsum(abs(z)**2 for z in X)/len(x),
            'scope':'Parseval energy, unnormalized forward DFT, no physical sampling or aliasing assessment'}

def shannon_entropy(weights):
    w=finite_vector(weights)
    if any(p<0 for p in w) or abs(fsum(w)-1)>1e-10:raise ModelDomainError('probabilities must be nonnegative and total one')
    return -fsum(p*log(p,2) for p in w if p>0)

def bayes_binary(prior,likelihood_positive_H1,likelihood_positive_H0):
    p=real(prior,'prior',0,1);a=real(likelihood_positive_H1,'likelihood_H1',0,1);b=real(likelihood_positive_H0,'likelihood_H0',0,1)
    denom=p*a+(1-p)*b
    if denom==0:raise ModelDomainError('zero probability evidence cannot be conditioned upon')
    return {'posterior_H1':p*a/denom,'evidence_probability':denom,'scope':'chosen prior and likelihood, not real event validation'}

def binomial_probability(n,k,p):
    if type(n)!=int or type(k)!=int or not 0<=k<=n<=1000:raise ModelDomainError('bounded integer n and k')
    p=real(p,'p',0,1)
    return comb(n,k)*p**k*(1-p)**(n-k)

def stable_softmax(logits):
    x=finite_vector(logits)
    shift=max(x);e=[exp(t-shift) for t in x];den=fsum(e)
    return [v/den for v in e]

def quadratic_gradient_descent(A,b,step,iterations,initial):
    mat=finite_matrix(A);n=len(mat)
    if any(len(row)!=n for row in mat):raise ModelDomainError('square matrix needed')
    v=finite_vector(b,n);x=finite_vector(initial,n);eta=positive(step,'learning rate')
    if type(iterations)!=int or not 0<=iterations<=5000:raise ModelDomainError('bounded iterations')
    if any(abs(mat[i][j]-mat[j][i])>1e-12 for i in range(n) for j in range(n)):raise ModelDomainError('symmetric Hessian required')
    # Strict diagonal dominance with positive diagonals gives SPD for this subset.
    if any(mat[i][i]<=fsum(abs(mat[i][j]) for j in range(n) if j!=i) for i in range(n)):
        raise ModelDomainError('positive strictly diagonally dominant Hessian required for this subset')
    # A provably conservative sufficient step bound from infinity norm.
    bound=max(fsum(abs(y) for y in row) for row in mat)
    if eta>=2/bound:raise ModelDomainError('step too large for guaranteed gradient descent convergence subset')
    for _ in range(iterations):
        g=[dot(row,x)-v[i] for i,row in enumerate(mat)]
        x=[xi-eta*gi for xi,gi in zip(x,g)]
        if not all(isfinite(z) for z in x):raise ModelDomainError('nonfinite optimizer state')
    g=[dot(row,x)-v[i] for i,row in enumerate(mat)]
    val=.5*dot(x,[dot(row,x) for row in mat])-dot(v,x)
    return {'solution':x,'objective':val,'gradient_norm':sqrt(dot(g,g)),
     'scope':'strictly diagonally dominant symmetric positive quadratic only; other objectives need separate solvers'}

def newtonian_kinematics(position_m,velocity_m_s,acceleration_m_s2,duration_s):
    x=real(position_m,'position');v=real(velocity_m_s,'velocity');a=real(acceleration_m_s2,'acceleration');t=real(duration_s,'duration',0)
    return {'position_m':x+v*t+.5*a*t*t,'velocity_m_s':v+a*t,
       'scope':'one-dimensional constant acceleration in chosen inertial frame; no air drag or relativistic correction'}

def harmonic_oscillator_energy(mass_kg,spring_N_m,x_m,velocity_m_s):
    m=positive(mass_kg,'mass');k=positive(spring_N_m,'spring stiffness');x=real(x_m,'displacement');v=real(velocity_m_s,'velocity')
    return {'energy_J':.5*m*v*v+.5*k*x*x,'angular_frequency_rad_s':sqrt(k/m),
      'scope':'ideal linear lossless spring, no forced/driven dynamics, validated material stress or safety'}

def rc_decay(voltage_initial_V,resistance_ohm,capacitance_F,time_s):
    v=real(voltage_initial_V,'voltage');r=positive(resistance_ohm,'resistance');c=positive(capacitance_F,'capacitance');t=real(time_s,'time',0)
    return {'voltage_V':v*exp(-t/(r*c)),'time_constant_s':r*c,
      'scope':'ideal RC discharge, lumped model, no actual wiring/voltage safety approval'}

def photon_energy(wavelength_m):
    lam=positive(wavelength_m,'vacuum wavelength')
    return {'energy_J':PLANCK*C_LIGHT/lam,'energy_eV':PLANCK*C_LIGHT/(lam*E_CHARGE),
     'scope':'single photon in vacuum; not a particular material absorption spectrum'}

def born_probability(amplitudes):
    if not isinstance(amplitudes,(list,tuple)) or not 1<=len(amplitudes)<=256:raise ModelDomainError('bounded complex amplitudes')
    vals=[]
    for z in amplitudes:
        if type(z) not in (int,float,complex) or not(isfinite(complex(z).real) and isfinite(complex(z).imag)):
            raise ModelDomainError('finite complex amplitude required')
        vals.append(complex(z))
    norm=fsum(abs(z)**2 for z in vals)
    if norm<=0:raise ModelDomainError('zero quantum state')
    return {'probabilities':[abs(z)**2/norm for z in vals],'original_norm_squared':norm,
      'scope':'finite dimensional pure state Born rule, no claim of quantum computer or measurement'}

def uncertainty_product(a,b,u_a,u_b,cov_ab=0):
    a=real(a,'a');b=real(b,'b');ua=real(u_a,'u_a',0);ub=real(u_b,'u_b',0);cov=real(cov_ab,'covariance')
    if abs(cov)>ua*ub*(1+1e-12):raise ModelDomainError('invalid input covariance')
    var=b*b*ua*ua+a*a*ub*ub+2*a*b*cov
    if var<-1e-9*max(1,b*b*ua*ua+a*a*ub*ub):raise ModelDomainError('negative variance')
    return {'value':a*b,'standard_uncertainty':sqrt(max(0,var)),
      'scope':'first-order uncertainty approximation with caller supplied covariance, no calibrated measurements'}
