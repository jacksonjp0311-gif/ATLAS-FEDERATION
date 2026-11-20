"""Constructed numerical investigations, zero physical measurements."""
from math import exp
from math_physics_atlas.v05_models import (equilibrium_problem,solve_equilibrium_1d,
    exponential_fitted_flux,bernoulli_bounded,manufactured_equilibrium_sine)

def casebook_v05():
    cases=[]
    def add(name,passed,metric,notes):cases.append({'name':name,'passed':bool(passed),'metric':float(metric),'qualification':notes})
    g=equilibrium_problem(31,1,1,0.4,0.);r=solve_equilibrium_1d(g)
    add('zero_boundary_equilibrium',r['converged'] and max(abs(v) for v in r['potential_u'])==0.,r['residual_linf'],
        'A manufactured zero state only')
    g=equilibrium_problem(31,1,0.8,0.6,0.6*__import__('math').sinh(0.7),(.7,.7));r=solve_equilibrium_1d(g)
    add('constant_equilibrium',r['converged'] and max(abs(v-0.7) for v in r['potential_u'])<1e-9,
        max(abs(v-0.7) for v in r['potential_u']),'Requires matching source and boundary')
    a=manufactured_equilibrium_sine(15);b=manufactured_equilibrium_sine(31)
    add('nonlinear_manufactured_second_order',a['error_linf']/b['error_linf']>3.9,a['error_linf']/b['error_linf'],
        'Analytic continuous function, not experimental dielectric data')
    f=exponential_fitted_flux(0.,1.,1.,exp(1.),1e-4,0.2)
    add('exponential_equilibrium_edge_flux',abs(f)<1e-15,abs(f),
        'Constant field, Boltzmann ratio; no contacts or recombination')
    d=exponential_fitted_flux(0.,0.,7.,3.,0.1,0.5)
    add('zero_field_Fick',abs(d-0.8)<1e-13,d,
        'A single edge Fick law is not a full transient transport model')
    add('Bernoulli_extreme_reciprocity',abs(bernoulli_bounded(-120.)-bernoulli_bounded(120.)-120)<1e-12,
        bernoulli_bounded(-120.)-bernoulli_bounded(120.),'Stable mathematical identity')
    return {'schema':'atlas.math-v05-casebook/1','status':'passed' if all(c['passed'] for c in cases) else 'failed',
        'count':len(cases),'cases':cases,'physical_measurements':0,'independent_peer_review':False}
