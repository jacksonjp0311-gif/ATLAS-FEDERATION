"""Constructed v0.4 test cases; no physical measurement claims."""
from math import pi,sin
from math_physics_atlas.v04_models import poisson2d_problem,solve_poisson2d_cg,manufactured_sine_refinement


def casebook_v04():
    rows=[]
    def add(name, passed, metric, note):
        rows.append({'case':name,'passed':bool(passed),'metric':float(metric),'limits':note})
    refine=manufactured_sine_refinement()
    add('manufactured_sine_O_h2',min(refine['error_ratios'])>3.9,min(refine['error_ratios']),
        'Constructed exact sine solution; tests a truncation-order prediction, not field data')
    g=poisson2d_problem(8,12,2.0,1.0,8.8541878188e-12,0.,lambda x,y:1+3*x-2*y)
    out=solve_poisson2d_cg(g,rtol=2e-11)
    err=max(abs(out['potential_volts'][j][i]-(1+3*i*g.hx-2*j*g.hy)) for j in range(1,13) for i in range(1,9))
    add('affine_boundary_laplace',out['converged'] and err<1e-9,err,
        'Homogeneous charge with linear Dirichlet boundary; constant dielectric')
    # A dielectric interface is represented only by assigned linear epsilon,
    # not real measured permittivity, contacts, or interface charge.
    g=poisson2d_problem(13,11,1,1,lambda x,y:1e-11*(1 if x<0.5 else 6),
                        0.,lambda x,y:x)
    out=solve_poisson2d_cg(g,rtol=5e-11)
    add('piecewise_linear_dielectric_gauss',out['converged'] and abs(out['gauss_balance_residual_C_per_m'])<1e-17,
        out['gauss_balance_residual_C_per_m'],'Discontinuous linear dielectric and prescribed boundary; no calibrated interface model')
    g=poisson2d_problem(12,10,1,1,2.,lambda x,y:1.0 if x<0.5 else -0.3,0.)
    out=solve_poisson2d_cg(g,rtol=1e-11)
    add('signed_volume_charge_flux',out['converged'] and abs(out['gauss_balance_residual_C_per_m'])<1e-8,
        out['gauss_balance_residual_C_per_m'],'Discrete Gauss law for signed authored charges, 2D per unit depth')
    g=poisson2d_problem(12,9,1.0,1.4,1.0,lambda x,y:sin(3*pi*x)*sin(2*pi*y)+0.2,
                        lambda x,y:0.1*x+0.2*y)
    r=solve_poisson2d_cg(g,rtol=1e-13,maxiter=1)
    add('bounded_nonconvergence_refusal',not r['converged'] and r['status']=='maxiter_exceeded',
        r['residual_l2'],'Underiterated solve is not represented as a converged physical prediction')
    n=g.nx*g.ny
    x=[(k%13-6)*0.13 for k in range(n)]
    y=[((k*5)%11-4)*0.19 for k in range(n)]
    ax=g.matvec(x);ay=g.matvec(y)
    e=sum(p*q for p,q in zip(x,ax))
    sym=abs(sum(p*q for p,q in zip(x,ay))-sum(p*q for p,q in zip(y,ax)))
    add('SPD_symmetry_energy',e>0 and sym<1e-10,sym,
        'Algebraic symmetry and positivity on one finite Dirichlet grid')
    return {'schema':'atlas.math-v04-casebook/1','status':'passed' if all(r['passed'] for r in rows) else 'failed',
            'count':len(rows),'cases':rows,'physical_measurements':0,'scientific_peer_review':False}
