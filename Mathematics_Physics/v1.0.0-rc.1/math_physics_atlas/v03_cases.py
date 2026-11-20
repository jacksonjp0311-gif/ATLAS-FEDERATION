"""v0.3.0 constructed casebook; synthetic calculations are not laboratory evidence."""
from math import pi,sin
from .v03_models import (jacobi_svd,svd_least_squares,poisson1d_dirichlet,
                         implicit_heat1d_dirichlet)

def casebook_v03():
    a=[[1,2],[2,4],[3,6]]
    s=jacobi_svd(a);assert s['rank_estimate']==1
    fit=svd_least_squares(a,[1,2,3]);assert max(abs(x-y) for x,y in zip(fit['solution'],[0.2,0.4]))<1e-9
    charge=[2.]*19
    p=poisson1d_dirichlet(charge,1.,1.)
    assert max(abs(v-x*(1-x)) for x,v in zip(p['x_m'],p['potential_volts']))<1e-11
    mesh=[sin(pi*k/40) for k in range(41)]
    h=implicit_heat1d_dirichlet(mesh,0.25,1/40,0.01,12)
    assert max(map(abs,h['state']))<max(mesh)
    return {'status':'passed','count':4,'evidence':'synthetic finite mathematical problems; no physical or AI experiment'}
