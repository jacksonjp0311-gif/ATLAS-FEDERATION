"""New bounded constructed investigation cases; preserve v0.1 casebook untouched."""
from math import sin,pi,exp
from .v02_models import qr_least_squares,svd2_diagnostics,fft_radix2,nonlinear_rk4_adaptive,heat1d_dirichlet,wave1d_dirichlet

def casebook_v02():
    x=qr_least_squares([[1,1],[1,2],[1,3],[1,4]],[3,5,7,9])
    assert abs(x['solution'][0]-1)<1e-12 and abs(x['solution'][1]-2)<1e-12
    s=svd2_diagnostics([[5,0],[0,2]])
    assert max(abs(v-w) for v,w in zip(s['singular_values'],[5,2]))<1e-12
    samples=fft_radix2([0,1,0,0]);assert max(abs(z-w) for z,w in zip(samples,[1,-1j,-1,1j]))<1e-12
    logistic=nonlinear_rk4_adaptive(lambda t,y:y*(1-y),0,0.1,2)
    assert abs(logistic['state']-1/(1+9*exp(-2)))<1e-6
    initial=[sin(pi*i/40) for i in range(41)]
    heat=heat1d_dirichlet(initial,0.1,1/40,0.001,60)
    assert max(heat)<max(initial)
    wave=wave1d_dirichlet(initial,1,1/40,0.01,40)
    assert max(map(abs,wave))<=1.01
    return {'status':'passed','count':6,'evidence':'six constructed finite cases, no laboratory observations'}
