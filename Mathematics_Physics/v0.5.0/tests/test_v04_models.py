"""v0.4 constructed finite numerical tests; previous test files stay retained."""
import math,random,unittest
from math_physics_atlas.v04_models import (ReferenceDomainError,poisson2d_problem,
    solve_poisson2d_cg,manufactured_sine_refinement)
from math_physics_atlas.v04_cases import casebook_v04

class V04Poisson(unittest.TestCase):
    def test_manufactured_sine_second_order(self):
        result=manufactured_sine_refinement()
        self.assertGreater(min(result['error_ratios']),3.9)
        self.assertLess(result['cases'][-1]['error_linf_volts'],0.001)

    def test_affine_exact_anisotropic_grid(self):
        for nx,ny,Lx,Ly in ((2,3,1.,2.),(11,4,3.,0.7),(5,21,0.3,5.)):
            g=poisson2d_problem(nx,ny,Lx,Ly,8.8541878188e-12,0.,lambda x,y:1.3+2*x-3*y)
            o=solve_poisson2d_cg(g,rtol=2e-12)
            self.assertTrue(o['converged'])
            self.assertLess(max(abs(o['potential_volts'][j][i]-(1.3+2*i*g.hx-3*j*g.hy))
                   for j in range(1,ny+1) for i in range(1,nx+1)),2e-9)
            self.assertLess(abs(o['gauss_balance_residual_C_per_m']),1e-19)

    def test_variable_epsilon_gauss(self):
        for epsilon in (lambda x,y:2*(1+0.3*x+0.2*y),
                        lambda x,y:8e-12*(1 if x<0.5 else 5)):
            g=poisson2d_problem(15,13,1,1,epsilon,lambda x,y:1e-11*(x-0.3),lambda x,y:3*x-y)
            o=solve_poisson2d_cg(g,rtol=1e-11)
            self.assertTrue(o['converged'])
            self.assertLess(abs(o['gauss_balance_residual_C_per_m']),1e-10)

    def test_symmetry_positive_definite_energy(self):
        g=poisson2d_problem(7,5,1,0.3,lambda x,y:1+0.1*x+0.2*y,0.)
        rng=random.Random(404)
        for _ in range(12):
            x=[rng.uniform(-1,1) for _ in g.rhs]
            y=[rng.uniform(-1,1) for _ in g.rhs]
            ax=g.matvec(x);ay=g.matvec(y)
            self.assertGreater(sum(a*b for a,b in zip(x,ax)),0.)
            self.assertLess(abs(sum(a*b for a,b in zip(x,ay))-sum(a*b for a,b in zip(y,ax))),1e-10)

    def test_gauss_charge_matches_boundary_flux(self):
        g=poisson2d_problem(14,10,0.4,2.0,2.,lambda x,y:x-0.1,lambda x,y:x*x+2*y)
        o=solve_poisson2d_cg(g,rtol=1e-12)
        self.assertTrue(o['converged'])
        self.assertLess(abs(o['charge_per_depth_C_per_m']-o['boundary_flux_per_depth_C_per_m']),1e-8)

    def test_zero_source_zero_boundary(self):
        g=poisson2d_problem(4,3,1,1,2.,0.,0.)
        s=solve_poisson2d_cg(g)
        self.assertEqual(s['iterations'],0)
        self.assertTrue(s['converged'])
        self.assertEqual(s['residual_l2'],0.)

    def test_scalar_and_arrays_equivalent(self):
        eps=[[1.1]*7 for _ in range(6)]
        rho=[[0.2]*5 for _ in range(4)]
        ga=poisson2d_problem(5,4,1,2,eps,rho,0.5)
        gb=poisson2d_problem(5,4,1,2,1.1,0.2,0.5)
        self.assertEqual(ga.rhs,gb.rhs)
        self.assertEqual(ga.diagonal,gb.diagonal)

    def test_explicit_nonconvergence(self):
        g=poisson2d_problem(14,11,1,1,1.,lambda x,y:math.sin(3*x+8*y)+0.1)
        s=solve_poisson2d_cg(g,maxiter=1,rtol=1e-14)
        self.assertFalse(s['converged'])
        self.assertEqual(s['status'],'maxiter_exceeded')
        self.assertGreater(s['residual_l2'],s['threshold'])

    def test_invalid_grid_geometry_and_inputs(self):
        invalid=[(True,2,1,1,1,0),(2,0,1,1,1,0),(65,2,1,1,1,0),(2,2,0,1,1,0),
                 (2,2,1,1,-1,0),(2,2,1,1,math.inf,0),(2,2,1,1,1,math.nan),
                 (2,2,1,1,1e-30,0),(2,2,1,1,1e30,0),(2,2,1,1,1,lambda x,y:math.nan)]
        for args in invalid:
            with self.subTest(args=str(args)),self.assertRaises(ReferenceDomainError):
                poisson2d_problem(*args)

    def test_invalid_shapes(self):
        for ep,charge,bd in (([[1.]],0,0),(1,[[0]],0),(1,0,[[0]]),
                             ([[1]*4 for _ in range(4)],0,0)):
            with self.subTest(ep=str(ep)[:12],charge=str(charge)[:12]),self.assertRaises(ReferenceDomainError):
                poisson2d_problem(3,3,1,1,ep,charge,bd)

    def test_solver_input_guards(self):
        g=poisson2d_problem(3,3,1,1,1,1)
        for kw in ({'rtol':0,'atol':0},{'rtol':math.nan},{'maxiter':0},{'maxiter':True},{'maxiter':40001}):
            with self.subTest(kw=kw),self.assertRaises(ReferenceDomainError):solve_poisson2d_cg(g,**kw)
        with self.assertRaises(ReferenceDomainError):g.matvec([0])

    def test_cases(self):
        self.assertEqual(casebook_v04()['status'],'passed')
        self.assertEqual(casebook_v04()['count'],6)

if __name__=='__main__':unittest.main()
