"""Release-candidate tests; no laboratory or independent expert certification."""
import math,unittest
from math_physics_atlas.v1_models import (DomainError,device_problem,solve_device,
 manufactured_equilibrium,physical_scaling,solve_carriers,carrier_linear_system,thomas,defects,edge_fluxes)

class TestDimensionalModel(unittest.TestCase):
 def test_exact_constants(self):
  x=physical_scaling(300,1e-6,1.04e-10,1e21)
  self.assertAlmostEqual(x['thermal_voltage_V'],0.025851999786435535,delta=1e-12)
  self.assertAlmostEqual(x['charge_C'],1.602176634e-19,delta=0)
  self.assertAlmostEqual(x['boltzmann_J_per_K'],1.380649e-23,delta=0)
  self.assertGreater(x['lambda_sq'],0)
 def test_length_scaling(self):
  a=physical_scaling(300,1e-6,1e-10,1e21);b=physical_scaling(300,2e-6,1e-10,1e21)
  self.assertAlmostEqual(a['lambda_sq']/b['lambda_sq'],4)
 def test_temperature_scaling(self):
  a=physical_scaling(200,1e-6,1e-10,1e21);b=physical_scaling(400,1e-6,1e-10,1e21)
  self.assertAlmostEqual(b['thermal_voltage_V']/a['thermal_voltage_V'],2)
 def test_invalid_physical(self):
  for args in ((0,1e-6,1e-10,1e21),(300,-1e-6,1e-10,1e21),(300,1e-6,-1e-10,1e21),(300,1e-6,1e-10,0)):
   with self.subTest(args=args),self.assertRaises(DomainError):physical_scaling(*args)

class TestExactManufactured(unittest.TestCase):
 def test_zero_current_equilibrium(self):
  for cells in (2,3,4,8,16,32,64):
   for slope in (-0.7,0,0.4,1.1):
    with self.subTest(cells=cells,slope=slope):
     problem,u,n,p=manufactured_equilibrium(cells,slope=slope)
     result=solve_device(problem,tol=1e-9)
     self.assertTrue(result.converged)
     self.assertLess(max(abs(x-y) for x,y in zip(result.potential,u)),1e-11)
     self.assertLess(max(abs(x-y) for x,y in zip(result.electrons,n)),2e-10)
     self.assertLess(max(abs(x-y) for x,y in zip(result.holes,p)),2e-10)
     self.assertLess(max(abs(v) for v in result.residuals['electron_flux']),3e-11)
     self.assertLess(max(abs(v) for v in result.residuals['hole_flux']),3e-11)
     self.assertLess(result.residuals['charge_gauss_balance'],1e-9)
 def test_uniform_zero(self):
  for cells in (2,5,30):
   s=solve_device(device_problem(cells,1.0))
   self.assertEqual(tuple([0.0]*(cells+2)),s.potential)
   self.assertLess(max(abs(x-1) for x in s.electrons),1e-12)
   self.assertLess(max(abs(x-1) for x in s.holes),1e-12)
 def test_biased_conservation(self):
  for cells in (3,8,16,32,64):
   with self.subTest(cells=cells):
    prob=device_problem(cells,1.0,doping=0.2,voltage=(0,0.4),electrons=(0.5,0.7),holes=(0.8,0.9))
    s=solve_device(prob)
    self.assertLess(s.residuals['poisson'],2e-9)
    self.assertLess(s.residuals['electron_conservation'],1e-10)
    self.assertLess(s.residuals['hole_conservation'],1e-10)
    self.assertLess(s.residuals['charge_gauss_balance'],2e-8)
    self.assertTrue(all(v>0 for v in s.electrons+s.holes))
    self.assertGreater(max(s.residuals['electron_flux']),0)
    self.assertLess(max(s.residuals['hole_flux']),0)
 def test_reversal_symmetry(self):
  pa=device_problem(13,1.,doping=(0.1,)*13,voltage=(-0.1,0.3),electrons=(0.7,1.2),holes=(1.0,.8))
  pb=device_problem(13,1.,doping=(-0.1,)*13,voltage=(0.1,-0.3),electrons=pa.holes,holes=pa.electrons)
  a=solve_device(pa);b=solve_device(pb)
  for aa,bb in zip(a.potential,b.potential):self.assertAlmostEqual(aa,-bb,delta=2e-10)
  for aa,bb in zip(a.electrons,b.holes):self.assertAlmostEqual(aa,bb,delta=2e-10)
  for aa,bb in zip(a.holes,b.electrons):self.assertAlmostEqual(aa,bb,delta=2e-10)
  for aa,bb in zip(a.residuals['electron_flux'],b.residuals['hole_flux']):self.assertAlmostEqual(aa,bb,delta=3e-9)

class TestLinearAlgebra(unittest.TestCase):
 def test_mmatrix_positive_carriers(self):
  u=[-0.9+2.0*i/26 for i in range(27)]
  for sign in (-1,1):
   n=solve_carriers(u,(0.1,1.9),sign)
   self.assertTrue(all(x>0 for x in n))
   f=edge_fluxes(u,n,1.,sign,1/26)
   self.assertLess(max(f)-min(f),1e-10)
 def test_diagonal_dominance(self):
  u=[0,.1,.3,.4,.6,1.]
  for sign in (-1,1):
   lower,diag,upper,rhs=carrier_linear_system(u,(1,2),charge_sign=sign)
   for i in range(len(diag)):
    self.assertGreater(diag[i],0)
    self.assertLessEqual(lower[i],0)
    self.assertLessEqual(upper[i],0)
 def test_thomas_known(self):
  a=thomas([0.,-1.,-1.],[2.,2.,2.],[-1.,-1.,0.],[0.,0.,4.])
  self.assertTrue(all(abs(x-y)<1e-12 for x,y in zip(a,[1.,2.,3.])))
 def test_singular_rejection(self):
  with self.assertRaises(DomainError):thomas([0.,0.],[0.,1.],[0.,0.],[1.,2.])

class TestFailureDisclosure(unittest.TestCase):
 def test_solver_nonconverged(self):
  p=device_problem(16,1.0,doping=.1,voltage=(0,.7),electrons=(1,1.3),holes=(.7,.9))
  with self.assertRaisesRegex(DomainError,'nonconvergence'):solve_device(p,maxiter=1,relax=.2)
 def test_bad_counts(self):
  for n in (0,1,129,3.4,True):
   with self.subTest(n=n),self.assertRaises(DomainError):device_problem(n,1.)
 def test_invalid_contacts(self):
  for contacts in ((0,1),(-1,1),(float('nan'),1),(1,)):
   with self.subTest(contacts=contacts),self.assertRaises(DomainError):device_problem(3,1.,electrons=contacts)
 def test_invalid_doping(self):
  for dop in (float('inf'),[0.,float('nan'),0.],1e8,[],[0.,0.]):
   with self.subTest(dop=dop),self.assertRaises(DomainError):device_problem(3,1.,doping=dop)
 def test_invalid_parameters(self):
  p=device_problem(4,1.)
  for kw in ({'tol':1.},{'maxiter':0},{'relax':0},{'relax':1.5}):
   with self.subTest(kw=kw),self.assertRaises(DomainError):solve_device(p,**kw)
 def test_malformed_system(self):
  with self.assertRaises(DomainError):thomas([],[],[],[])
  with self.assertRaises(DomainError):carrier_linear_system([0.]*3,(1.,1.))

if __name__=='__main__':unittest.main()
