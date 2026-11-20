"""Mathematics/Physics v0.2 direct finite-problem kernel tests.

Independent numerical comparisons also exist in tools/independent_oracle_v02.py.
"""
import math
import random
import unittest

from math_physics_atlas.v02_models import (
    NumericalDomainError, qr_least_squares, svd2_diagnostics, fft_radix2,
    nonlinear_rk4_adaptive, heat1d_dirichlet, wave1d_dirichlet)


class V02ReferenceAlgorithms(unittest.TestCase):
    def test_qr_exact_overdetermined(self):
        res=qr_least_squares([[1,1],[1,2],[1,3],[1,4]],[3,5,7,9])
        for x,e in zip(res['solution'],[1,2]):self.assertAlmostEqual(x,e,places=11)
        self.assertLess(res['residual_l2'],1e-12)

    def test_qr_noisy_least_squares_optimality(self):
        a=[[1,x] for x in (-3,-2,-1,0,1,2,3)]
        b=[1.2+0.9*row[1]+(0.01 if i%2 else -0.01) for i,row in enumerate(a)]
        r=qr_least_squares(a,b)
        residual=[sum(x*y for x,y in zip(row,r['solution']))-target for row,target in zip(a,b)]
        for j in range(2):
            self.assertLess(abs(sum(row[j]*e for row,e in zip(a,residual))),1e-11)

    def test_qr_rank_failure(self):
        for a in [[[1,2],[2,4],[3,6]],[[0,0],[0,0]]]:
            with self.assertRaises(NumericalDomainError):qr_least_squares(a,[1]*len(a))
        with self.assertRaises(NumericalDomainError):qr_least_squares([[1,0,0],[0,1,0]],[1,2])
        with self.assertRaises(NumericalDomainError):qr_least_squares([[1,1],[1,2]],[1])

    def test_singular_values_diagonal_rotation(self):
        for a,s in [([[5,0],[0,2]],[5,2]),([[0,2],[-5,0]],[5,2]),([[1,1],[1,1]],[2,0])]:
            r=svd2_diagnostics(a)
            for x,y in zip(r['singular_values'],s):self.assertAlmostEqual(x,y,places=12)
        self.assertEqual(svd2_diagnostics([[0,0],[0,0]])['rank_estimate'],0)
        with self.assertRaises(NumericalDomainError):svd2_diagnostics([[1,2,3],[1,2,3]])

    def test_fft_fourier_basis_and_roundtrip(self):
        for n in (1,2,4,8,16,32,64):
            seq=[complex(math.cos(2*math.pi*3*k/n),math.sin(2*math.pi*3*k/n)) for k in range(n)]
            f=fft_radix2(seq)
            self.assertAlmostEqual(abs(f[3%n]),n,places=9)
            self.assertLess(max(abs(f[k]) for k in range(n) if k!=3%n) if n>1 else 0,1e-10)
            inv=fft_radix2(f,True)
            self.assertLess(max(abs(x-y) for x,y in zip(inv,seq)),1e-11)

    def test_fft_reject_non_power_and_nonfinite(self):
        with self.assertRaises(NumericalDomainError):fft_radix2([1,2,3])
        with self.assertRaises(NumericalDomainError):fft_radix2([0,float('nan')])
        with self.assertRaises(NumericalDomainError):fft_radix2([])

    def test_logistic_adaptive_rk(self):
        for y0 in (0.05,0.1,0.3,0.6,0.9):
            for horizon in (0.1,1.,3.,6.):
                result=nonlinear_rk4_adaptive(lambda t,y:y*(1-y),0,y0,horizon,step=0.3)
                ref=1/(1+(1/y0-1)*math.exp(-horizon))
                self.assertAlmostEqual(result['state'],ref,delta=2e-6)
                self.assertEqual(result['time'],horizon)
        with self.assertRaises(NumericalDomainError):nonlinear_rk4_adaptive(lambda t,y:y,1,1,0)
        with self.assertRaises(NumericalDomainError):nonlinear_rk4_adaptive(lambda t,y:float('nan'),0,1,1)

    def test_heat_fourier_number_and_eigenmode(self):
        n=40;dx=1/n;alpha=0.08;dt=0.25*dx*dx/alpha;steps=60
        u=[math.sin(math.pi*i/n) for i in range(n+1)]
        x=heat1d_dirichlet(u,alpha,dx,dt,steps)
        expected=math.exp(-alpha*math.pi**2*dt*steps)
        self.assertLess(max(abs(x[i]-expected*u[i]) for i in range(n+1)),0.001)
        self.assertLess(max(x),max(u))
        with self.assertRaises(NumericalDomainError):heat1d_dirichlet(u,alpha,dx,1.1*dx*dx/alpha,2)

    def test_wave_cfl_and_eigenmode(self):
        n=40;dx=1/n;speed=0.8;dt=0.5*dx/speed;steps=40
        u=[math.sin(math.pi*i/n) for i in range(n+1)]
        out=wave1d_dirichlet(u,speed,dx,dt,steps)
        ref=math.cos(speed*math.pi*steps*dt)
        self.assertLess(max(abs(out[i]-ref*u[i]) for i in range(n+1)),0.005)
        with self.assertRaises(NumericalDomainError):wave1d_dirichlet(u,speed,dx,1.1*dx/speed,1)

    def test_bounded_reject_unphysical_shapes(self):
        with self.assertRaises(NumericalDomainError):heat1d_dirichlet([1,2,0],1,1,0.1,1)
        with self.assertRaises(NumericalDomainError):wave1d_dirichlet([0,1,2],1,1,0.1,1)
        with self.assertRaises(NumericalDomainError):svd2_diagnostics([[1,2],[3,4]],-1)
        with self.assertRaises(NumericalDomainError):qr_least_squares([[float('inf')]],[1])

if __name__=='__main__':unittest.main()
