import math,random,unittest
from math_physics_atlas.v05_models import (ReferenceDomainError,bernoulli_bounded,exponential_fitted_flux,
    equilibrium_problem,solve_equilibrium_1d,manufactured_equilibrium_sine)
from math_physics_atlas.v05_cases import casebook_v05
class V05Models(unittest.TestCase):
    def test_bernoulli_zero_and_reciprocity(self):
        self.assertEqual(bernoulli_bounded(0),1.)
        for z in (1e-10,1e-5,1e-2,1,5,35,75,149):
            self.assertAlmostEqual(bernoulli_bounded(-z)-bernoulli_bounded(z),z,delta=2e-13*max(1,z))
    def test_small_bernoulli_accuracy(self):
        for z in (1e-12,1e-8,1e-4,-1e-4):
            if abs(z)>=1e-10:
                self.assertAlmostEqual(bernoulli_bounded(z),z/math.expm1(z),delta=2e-12)
    def test_edge_fick_law(self):
        self.assertAlmostEqual(exponential_fitted_flux(0,0,5,2,0.5,0.3),5.)
    def test_edge_equilibrium(self):
        for d in (-15.,-3.,-1.,0.,1.,3.,15.):
            self.assertAlmostEqual(exponential_fitted_flux(0,d,2.,2*math.exp(d),0.01,1),0.,delta=2e-8)
    def test_edge_antisyms(self):
        rng=random.Random(20261116)
        for _ in range(150):
            a,b=rng.uniform(-9,9),rng.uniform(-9,9)
            n,m=rng.random()*100,rng.random()*100
            f=exponential_fitted_flux(a,b,n,m,0.2,0.1)
            rev=exponential_fitted_flux(b,a,m,n,0.2,0.1)
            self.assertAlmostEqual(f,-rev,delta=1e-10)
    def test_uniform_zero(self):
        g=equilibrium_problem(31,1,1,0.2,0.);r=solve_equilibrium_1d(g)
        self.assertTrue(r['converged']);self.assertEqual(r['iterations'],0)
        self.assertEqual(max(abs(v) for v in r['potential_u']),0.)
    def test_affine_beta_zero(self):
        g=equilibrium_problem(31,2,0.7,0.,0.,(-0.4,0.6));r=solve_equilibrium_1d(g)
        self.assertTrue(r['converged'])
        self.assertLess(max(abs(r['potential_u'][i]-(-.4+i/32)) for i in range(33)),1e-12)
    def test_constant_nonlinear(self):
        s=0.67;g=equilibrium_problem(31,1,1.2,.35,.35*math.sinh(s),(s,s))
        r=solve_equilibrium_1d(g)
        self.assertTrue(r['converged']);self.assertLess(max(abs(v-s) for v in r['potential_u']),1e-11)
    def test_manufactured_convergence(self):
        a=manufactured_equilibrium_sine(15);b=manufactured_equilibrium_sine(31);c=manufactured_equilibrium_sine(63)
        self.assertGreater(a['error_linf']/b['error_linf'],3.8)
        self.assertGreater(b['error_linf']/c['error_linf'],3.8)
    def test_nonzero_charge_balance(self):
        g=equilibrium_problem(63,2.0,.8,.35,lambda x:math.sin(x)+.1,(-.2,.3));r=solve_equilibrium_1d(g)
        self.assertTrue(r['converged']);self.assertLess(abs(r['charge_flux_balance']),r['threshold']*g.length*1.2)
    def test_exhaustion_reports_failure(self):
        g=equilibrium_problem(31,1,1,.6,lambda x:math.sin(7*x)+1)
        r=solve_equilibrium_1d(g,maxiter=1,rtol=1e-15,atol=1e-15)
        self.assertFalse(r['converged']);self.assertEqual(r['status'],'maxiter_exceeded')
    def test_invalid_inputs(self):
        for v in (True,float('nan'),float('inf'),'2',200):
            with self.subTest(v=v),self.assertRaises(ReferenceDomainError):bernoulli_bounded(v)
        for vals in ((0,0,1,-1,1,1),(0,0,1,1,-2,1),(0,0,1,1,1,0),(0,1000,1,1,1,1)):
            with self.subTest(vals=vals),self.assertRaises(ReferenceDomainError):exponential_fitted_flux(*vals)
        for vals in ((True,1,1,1,0),(1,1,1,1,0),(3,0,1,1,0),(4,1,-1,1,0),(4,1,1,-1,0),(4,1,1,1,float('nan'))):
            with self.subTest(vals=vals),self.assertRaises(ReferenceDomainError):equilibrium_problem(*vals)
    def test_cases(self):
        self.assertEqual(casebook_v05()['status'],'passed')
        self.assertEqual(casebook_v05()['count'],6)
if __name__=='__main__':unittest.main()
