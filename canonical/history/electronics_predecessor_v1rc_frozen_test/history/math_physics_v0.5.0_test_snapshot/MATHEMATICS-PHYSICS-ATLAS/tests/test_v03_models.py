"""v0.3 bounded reference methods, domain failures, invariants and convergence tests."""
import math
import random
import unittest
from math_physics_atlas.v03_models import (
    jacobi_svd,svd_least_squares,poisson1d_dirichlet,
    implicit_heat1d_dirichlet,tridiagonal_solve,ReferenceDomainError)
from math_physics_atlas.v03_cases import casebook_v03

class V03Models(unittest.TestCase):
    def test_svd_diagonal(self):
        for a,s in [([[4,0],[0,2]],[4,2]),([[0,0,0],[0,0,0]],[0,0]),
                    ([[1,2,3]],[math.sqrt(14)]),([[1],[2],[3]],[math.sqrt(14)])]:
            got=jacobi_svd(a)
            for x,y in zip(got['singular_values'],s):self.assertAlmostEqual(x,y,places=10)
            self.assertLess(got['reconstruction_relative_frobenius'],1e-10)

    def test_svd_orthogonal_and_transpose_invariance(self):
        rng=random.Random(2)
        for m,n in [(3,2),(2,3),(7,4),(4,7),(6,6),(1,1),(8,1),(1,8)]:
            for _ in range(6):
                a=[[rng.uniform(-2,2) for _ in range(n)] for __ in range(m)]
                got=jacobi_svd(a)
                other=jacobi_svd([list(col) for col in zip(*a)])
                self.assertLess(got['reconstruction_relative_frobenius'],1e-10)
                self.assertLess(got['active_left_orthogonality_error'],1e-10)
                self.assertLess(got['active_right_orthogonality_error'],1e-10)
                for v,w in zip(got['singular_values'],other['singular_values']):self.assertAlmostEqual(v,w,places=9)

    def test_svd_rank_deficient_minimum_norm(self):
        a=[[1,2],[2,4],[3,6]]
        fit=svd_least_squares(a,[1,2,3])
        self.assertEqual(fit['rank_estimate'],1)
        self.assertLess(max(abs(x-y) for x,y in zip(fit['solution'],[.2,.4])),1e-9)
        self.assertLess(fit['residual_l2'],1e-11)

    def test_svd_underdetermined_minimum_norm(self):
        r=svd_least_squares([[1,0,0],[0,1,0]],[4,5])
        self.assertLess(max(abs(x-y) for x,y in zip(r['solution'],[4,5,0])),1e-10)
        self.assertEqual(r['rank_estimate'],2)

    def test_svd_overdetermined_noisy_stationarity(self):
        a=[[1,x] for x in range(-3,4)]
        y=[1.2+0.6*x+(0.02 if x%2 else -0.02) for _,x in a]
        r=svd_least_squares(a,y)
        residual=[sum(v*w for v,w in zip(row,r['solution']))-b for row,b in zip(a,y)]
        for j in range(2):self.assertLess(abs(sum(row[j]*err for row,err in zip(a,residual))),1e-10)

    def test_svd_ill_conditioning_flag(self):
        r=jacobi_svd([[1,0],[0,1e-14]],rank_rtol=1e-10)
        self.assertEqual(r['rank_estimate'],1)
        self.assertIsNone(r['condition_2'])

    def test_svd_invalid_shapes_scalars_and_tolerances(self):
        for a in ([],[[1,2],[3]],[[math.nan]],[[math.inf]],[[complex(1,1)]],[[True]],[[1e120]],[[1]*33]):
            with self.subTest(a=str(a)[:25]),self.assertRaises(ReferenceDomainError):jacobi_svd(a)
        for kw in ({'rank_rtol':0},{'pair_tol':0.1},{'max_sweeps':0},{'max_sweeps':True}):
            with self.assertRaises(ReferenceDomainError):jacobi_svd([[1]],**kw)
        with self.assertRaises(ReferenceDomainError):svd_least_squares([[1,2]],[1,2])

    def test_tridiagonal_exact(self):
        x=tridiagonal_solve([-1.,-1.],[2.,2.,2.],[-1.,-1.],[0.,4.,0.])
        for a,b in zip(x,[2.,4.,2.]):self.assertAlmostEqual(a,b)

    def test_tridiagonal_refuses_singular_or_bad_shapes(self):
        for args in [([], [0], [], [1]), ([1],[1,1],[1],[2]), ([1],[0,0],[1],[1,1])]:
            with self.assertRaises(ReferenceDomainError):tridiagonal_solve(*args)

    def test_poisson_constant_charge_matches_quadratic(self):
        for cells in [1,2,4,8,16,32,64,128]:
            p=poisson1d_dirichlet([2.]*cells,1.,1.)
            err=max(abs(v-x*(1-x)) for x,v in zip(p['x_m'],p['potential_volts']))
            self.assertLess(err,1e-10)
            self.assertLess(abs(p['gauss_balance_residual_C_per_m2']),1e-10)

    def test_poisson_nonzero_voltage_boundaries(self):
        p=poisson1d_dirichlet([0.]*10,8.85e-12,0.5,2.,-1.)
        self.assertLess(max(abs(v-(2-3*x/0.5)) for x,v in zip(p['x_m'],p['potential_volts'])),1e-10)

    def test_poisson_sine_second_order_grid_refinement(self):
        errors=[]
        for cells in (15,31,63,127):
            L=1.3;eps=2.4
            rho=[eps*(math.pi/L)**2*math.sin(math.pi*k/(cells+1)) for k in range(1,cells+1)]
            p=poisson1d_dirichlet(rho,eps,L)
            errors.append(max(abs(v-math.sin(math.pi*x/L)) for x,v in zip(p['x_m'],p['potential_volts'])))
        for a,b in zip(errors,errors[1:]):self.assertGreater(a/b,3.8)

    def test_poisson_refusal(self):
        for rho,e,L in [([],1,1),([1],0,1),([1],1,0),([math.nan],1,1),([1],math.inf,1)]:
            with self.assertRaises(ReferenceDomainError):poisson1d_dirichlet(rho,e,L)

    def test_heat_backward_euler_unconditional_decay_mode(self):
        for r in (0.01,0.1,0.5,1,20,100):
            n=30;dx=1/n;alpha=.5;dt=r*dx*dx/alpha
            init=[math.sin(math.pi*k/n) for k in range(n+1)]
            out=implicit_heat1d_dirichlet(init,alpha,dx,dt,9)
            eigenvalue=4*math.sin(math.pi/(2*n))**2
            fac=(1+r*eigenvalue)**(-9)
            self.assertLess(max(abs(v-fac*x) for x,v in zip(init,out['state'])),1e-9)

    def test_heat_crank_nicolson_mode_and_warning(self):
        n=20;r=3.0;dx=1/n;dt=r*dx*dx
        init=[math.sin(math.pi*k/n) for k in range(n+1)]
        out=implicit_heat1d_dirichlet(init,1.,dx,dt,5,method='crank_nicolson')
        eig=4*math.sin(math.pi/(2*n))**2
        fac=((1-r*eig/2)/(1+r*eig/2))**5
        self.assertLess(max(abs(v-fac*x) for x,v in zip(init,out['state'])),1e-9)

    def test_heat_boundary_preservation_and_zero_steps(self):
        initial=[3.,4.,5.,2.,-1.]
        for method in ('backward_euler','crank_nicolson'):
            out=implicit_heat1d_dirichlet(initial,.1,.2,.01,100,method=method)
            self.assertEqual(out['state'][0],3.)
            self.assertEqual(out['state'][-1],-1.)
            self.assertEqual(implicit_heat1d_dirichlet(initial,.1,.2,.01,0,method=method)['state'],initial)

    def test_heat_refusals(self):
        for kw in ({'method':'invalid'},{'method':True},{'method':None}):
            with self.assertRaises(ReferenceDomainError):implicit_heat1d_dirichlet([0,1,0],1,1,.1,3,**kw)
        for init,alpha,dx,dt,steps in [([1,2],1,1,1,1),([0,1,0],0,1,1,1),([0,1,0],1,0,1,1),([0,1,0],1,1,-1,1),([0,1,0],1,1,.1,-1),([0,1,0],1,1,.1,1.5)]:
            with self.assertRaises(ReferenceDomainError):implicit_heat1d_dirichlet(init,alpha,dx,dt,steps)

    def test_casebook(self):
        self.assertEqual(casebook_v03()['count'],4)

if __name__=='__main__':unittest.main()
