import unittest,random,math
from fractions import Fraction
from math_physics_atlas.models import *
from math_physics_atlas.cases import casebook

class MathPhysicsTests(unittest.TestCase):
 def test_casebook(self):self.assertEqual(casebook()['status'],'passed');self.assertEqual(casebook()['count'],22)
 def test_dot(self):self.assertEqual(dot([1,2],[3,4]),11)
 def test_dot_shape(self):
  with self.assertRaises(ModelDomainError):dot([1],[1,2])
 def test_matrix_multiply(self):self.assertEqual(matrix_multiply([[1,2]],[[3],[4]]),[[11.]])
 def test_matrix_shape(self):
  with self.assertRaises(ModelDomainError):matrix_multiply([[1,2]],[[1]])
 def test_transpose(self):self.assertEqual(transpose([[1,2],[3,4]]),[[1,3],[2,4]])
 def test_rational(self):self.assertEqual(rational_solve([[2,1],[1,-1]],[5,1])['solution_fractions'],['2','1'])
 def test_rational_fraction(self):self.assertEqual(rational_solve([[3]],[1])['solution_fractions'],['1/3'])
 def test_rational_singular(self):
  with self.assertRaises(ModelDomainError):rational_solve([[1,2],[2,4]],[1,2])
 def test_rational_no_approx(self):
  with self.assertRaises(ModelDomainError):rational_solve([[.1]],[.2])
 def test_least_squares(self):self.assertAlmostEqual(least_squares([[1,0],[1,1],[1,2]],[1,3,5])['parameters'][1],2)
 def test_least_rank(self):
  with self.assertRaises(ModelDomainError):least_squares([[1,1],[2,2]],[1,2])
 def test_projection(self):self.assertEqual(projection([3,4],[1,0])['projected'],[3,0])
 def test_projection_zero(self):
  with self.assertRaises(ModelDomainError):projection([1,1],[0,0])
 def test_polynomial(self):self.assertEqual(polynomial_value([1,2,3],2),17)
 def test_derivative(self):self.assertEqual(polynomial_derivative([1,2,3]),[2,6])
 def test_constant_derivative(self):self.assertEqual(polynomial_derivative([4]),[0.])
 def test_center(self):self.assertAlmostEqual(central_difference_polynomial([0,0,1],2,.01),4,places=10)
 def test_center_invalid_step(self):
  with self.assertRaises(ModelDomainError):central_difference_polynomial([1,2],2,0)
 def test_integral(self):self.assertAlmostEqual(integrate_polynomial([0,0,1],0,3),9)
 def test_integral_reverse(self):self.assertAlmostEqual(integrate_polynomial([0,0,1],3,0),-9)
 def test_simpson(self):self.assertAlmostEqual(simpson_polynomial([0,0,0,1],0,2,20),4)
 def test_simpson_odd(self):
  with self.assertRaises(ModelDomainError):simpson_polynomial([1],0,1,3)
 def test_ode_exact(self):self.assertAlmostEqual(linear_ode_exact(1,-1,0,1),math.exp(-1))
 def test_ode_zero_a(self):self.assertEqual(linear_ode_exact(1,0,2,3),7)
 def test_rk4(self):self.assertLess(abs(rk4_linear(1,-1,0,1,20)['numerical_y']-math.exp(-1)),1e-7)
 def test_rk4_zero_time(self):self.assertEqual(rk4_linear(5,2,1,0,1)['numerical_y'],5)
 def test_rk4_invalid_steps(self):
  with self.assertRaises(ModelDomainError):rk4_linear(1,1,0,1,0)
 def test_fourier_energy(self):self.assertAlmostEqual(spectral_energy([1,0,-1,0])['time_energy'],spectral_energy([1,0,-1,0])['frequency_energy'])
 def test_fourier_constant(self):self.assertAlmostEqual(discrete_fourier([2,2,2,2])[0].real,8)
 def test_entropy_one(self):self.assertEqual(shannon_entropy([1,0]),0)
 def test_entropy_two(self):self.assertAlmostEqual(shannon_entropy([.5,.5]),1)
 def test_entropy_not_normalized(self):
  with self.assertRaises(ModelDomainError):shannon_entropy([.5,.4])
 def test_bayes(self):self.assertAlmostEqual(bayes_binary(.5,.9,.1)['posterior_H1'],.9)
 def test_bayes_zero_evidence(self):
  with self.assertRaises(ModelDomainError):bayes_binary(.5,0,0)
 def test_binomial(self):self.assertAlmostEqual(binomial_probability(2,1,.5),.5)
 def test_binomial_bad(self):
  with self.assertRaises(ModelDomainError):binomial_probability(2,3,.5)
 def test_softmax(self):self.assertAlmostEqual(sum(stable_softmax([1000,1001,999])),1)
 def test_softmax_shift(self):
  a=stable_softmax([1,2,3]);b=stable_softmax([1001,1002,1003]);self.assertTrue(all(abs(x-y)<1e-12 for x,y in zip(a,b)))
 def test_gradient_descent(self):
  a=quadratic_gradient_descent([[2,0],[0,2]],[2,4],.25,100,[0,0]);self.assertAlmostEqual(a['solution'][0],1,places=10)
 def test_gd_bad_hessian(self):
  with self.assertRaises(ModelDomainError):quadratic_gradient_descent([[1,2],[2,1]],[1,1],.1,10,[0,0])
 def test_gd_bad_step(self):
  with self.assertRaises(ModelDomainError):quadratic_gradient_descent([[2]],[2],1,10,[0])
 def test_kinematics(self):self.assertEqual(newtonian_kinematics(0,1,2,3)['position_m'],12)
 def test_kinematics_negative_duration(self):
  with self.assertRaises(ModelDomainError):newtonian_kinematics(0,1,2,-3)
 def test_oscillator(self):self.assertAlmostEqual(harmonic_oscillator_energy(1,4,.5,0)['energy_J'],.5)
 def test_rc(self):self.assertAlmostEqual(rc_decay(10,1000,.001,1)['voltage_V'],10/math.e)
 def test_rc_invalid_resistance(self):
  with self.assertRaises(ModelDomainError):rc_decay(1,-1,.1,1)
 def test_photon(self):self.assertGreater(photon_energy(400e-9)['energy_eV'],photon_energy(800e-9)['energy_eV'])
 def test_born(self):self.assertEqual(born_probability([0,1])['probabilities'],[0,1])
 def test_born_zero(self):
  with self.assertRaises(ModelDomainError):born_probability([0,0])
 def test_uncertainty(self):self.assertAlmostEqual(uncertainty_product(2,3,.1,.2)['standard_uncertainty'],.5)
 def test_uncertainty_covariance(self):
  with self.assertRaises(ModelDomainError):uncertainty_product(2,3,.1,.2,.1)
 def test_nan(self):
  with self.assertRaises(ModelDomainError):dot([float('nan')],[2])
 def test_random_exact_rationals(self):
  rng=random.Random(314)
  for _ in range(50):
   a=rng.randint(1,50);b=rng.randint(-10,10)
   out=rational_solve([[a,0],[0,1]],[b,2]);self.assertEqual(Fraction(out['solution_fractions'][0]),Fraction(b,a))
