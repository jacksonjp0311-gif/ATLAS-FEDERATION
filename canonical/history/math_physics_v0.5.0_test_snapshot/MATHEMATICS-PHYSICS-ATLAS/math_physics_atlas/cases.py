"""Constructed finite scientific reconstruction exercises, not empirical observations."""
from math import exp,sqrt,log,pi
from .models import *

def casebook():
    entries=[]
    def add(name,result,ok,scope):entries.append({'name':name,'result':result,'passed':bool(ok),'scope':scope,'origin':'original authored mathematical example'})
    a=rational_solve([[2,1],[1,-1]],[5,1]);add('Exact rational 2x2 solution',a,a['solution_fractions']==['2','1'],'Unique square linear system')
    a=matrix_multiply([[1,2]],[[3],[4]]);add('Matrix multiplication',a,a==[[11.]],'Linear maps only; input dimensions matter')
    a=projection([3,4],[1,0]);add('Orthogonal projection',a,a['projected']==[3,0] and abs(a['orthogonality_residual'])<1e-12,'Euclidean inner product')
    a=least_squares([[1,0],[1,1],[1,2]],[1,3,5]);add('Least squares straight line',a,all(abs(x-y)<1e-10 for x,y in zip(a['parameters'],[1,2])),'Full column rank, normal equations only')
    a=polynomial_derivative([2,3,4]);add('Polynomial derivative',a,a==[3,8],'Power rule for polynomials')
    a=central_difference_polynomial([0,0,1],2,1e-4);add('Central finite difference',a,abs(a-4)<1e-7,'Discretization and rounding error')
    a=integrate_polynomial([0,0,1],0,3);add('Exact polynomial integral',a,abs(a-9)<1e-12,'Antiderivative formula')
    a=simpson_polynomial([0,0,0,1],0,2,10);add('Simpson cubic integral',a,abs(a-4)<1e-12,'Uniform even intervals; polynomials of degree up to three')
    a=linear_ode_exact(2,-1,0,1);add('Exponential ODE',a,abs(a-2/exp(1))<1e-12,'Constant coefficient scalar ODE')
    a=rk4_linear(1,-.5,0,1,100);add('RK4 ODE convergence',a,abs(a['numerical_y']-a['analytic_reference'])<1e-9,'Finite step stability not proven for arbitrary ODEs')
    a=spectral_energy([1,0,-1,0]);add('Parseval DFT identity',a,abs(a['time_energy']-a['frequency_energy'])<1e-12,'Finite discrete transform with specified normalization')
    a=shannon_entropy([.5,.5]);add('One bit entropy',a,abs(a-1)<1e-12,'Shannon discrete probabilities, not physical disorder')
    a=bayes_binary(.5,.9,.1);add('Bayesian evidence update',a,abs(a['posterior_H1']-.9)<1e-12,'User-chosen likelihoods, no true outcome inference')
    a=binomial_probability(2,1,.5);add('Binomial count',a,abs(a-.5)<1e-12,'Independent identical Bernoulli trials')
    a=stable_softmax([1000,1000]);add('Stable softmax',a,abs(sum(a)-1)<1e-12 and all(abs(z-.5)<1e-12 for z in a),'Probability transform, not calibrated model confidence')
    a=quadratic_gradient_descent([[2,0],[0,2]],[2,4],.25,60,[0,0]);add('Quadratic gradient descent',a,abs(a['solution'][0]-1)<1e-10 and abs(a['solution'][1]-2)<1e-10,'Strongly convex strictly diagonal dominant Hessian')
    a=newtonian_kinematics(0,1,2,3);add('Constant acceleration kinematics',a,a['position_m']==12 and a['velocity_m_s']==7,'One dimensional classical motion')
    a=harmonic_oscillator_energy(1,4,.5,0);add('Spring potential energy',a,abs(a['energy_J']-.5)<1e-12,'Lossless linear spring within elastic range')
    a=rc_decay(10,1000,.001,1);add('RC exponential decay',a,abs(a['voltage_V']-10/exp(1))<1e-10,'Ideal components, no hardware approval')
    a=photon_energy(500e-9);add('Photon energy',a,2<a['energy_eV']<3,'Vacuum photon, not a measured absorption spectrum')
    a=born_probability([1+0j,1j]);add('Quantum Born probabilities',a,all(abs(z-.5)<1e-12 for z in a['probabilities']),'Abstract normalized two-level state')
    a=uncertainty_product(2,3,.1,.2);add('Product uncertainty',a,abs(a['standard_uncertainty']-.5)<1e-12,'Linear error propagation with zero covariance')
    return {'schema':'atlas.math-physics-reconstruction-cases/1','status':'passed' if all(x['passed'] for x in entries) else 'failed',
      'count':len(entries),'cases':entries,'real_experiments':0,'physical_devices_tested':0,'independent_science_review':False}
