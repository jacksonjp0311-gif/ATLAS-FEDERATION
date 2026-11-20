import math,random,unittest
from materials_atlas.methods import MaterialsInputError
from materials_atlas.phase_models import R,regular_solution_energy,regular_solution_boundaries,regular_solution_state
from materials_atlas.diffraction import cubic_peak_lattice,cubic_lattice_from_indexed_peaks
from materials_atlas.hahn_diagnostics import hahn1_residual_diagnostics
from materials_atlas.new_cases import expanded_casebook

class TestThermodynamicModel(unittest.TestCase):
 def test_critical(self):
  w=20000;tc=w/(2*R)
  p=regular_solution_boundaries(temperature_k=tc,omega_j_mol=w)
  self.assertEqual(p['phase_regime'],'single_phase_all_compositions')
 def test_no_attractive_case(self):
  with self.assertRaises(MaterialsInputError):regular_solution_boundaries(temperature_k=300,omega_j_mol=-20)
 def test_high_temp(self):
  p=regular_solution_state(temperature_k=1000,omega_j_mol=100,mole_fraction_b=.5)
  self.assertIn('single_phase',p['state'])
 def test_low_temp(self):
  p=regular_solution_state(temperature_k=600,omega_j_mol=20000,mole_fraction_b=.5)
  self.assertEqual(p['state'],'spinodal_unstable_homogeneous_state')
  self.assertGreater(p['free_energy_drop_to_equilibrium_j_mol'],0)
 def test_critical_formula(self):
  p=regular_solution_boundaries(temperature_k=800,omega_j_mol=20000)
  b=p['binodal_mole_fraction_b'];s=p['spinodal_mole_fraction_b']
  self.assertLess(b[0],s[0]);self.assertLess(s[0],.5)
  self.assertAlmostEqual(b[0]+b[1],1);self.assertAlmostEqual(s[0]+s[1],1)
 def test_metastable_not_mistaken_stable(self):
  w=20000;t=800;p=regular_solution_boundaries(temperature_k=t,omega_j_mol=w)
  x=sum([p['binodal_mole_fraction_b'][0],p['spinodal_mole_fraction_b'][0]])/2
  q=regular_solution_state(temperature_k=t,omega_j_mol=w,mole_fraction_b=x)
  self.assertIn('metastable',q['state']);self.assertGreater(q['free_energy_drop_to_equilibrium_j_mol'],0)
 def test_gradient_curvature_numerical(self):
  r=random.Random(318)
  for i in range(150):
   t=250+r.random()*1200;w=r.random()*20000;x=.05+r.random()*.9;eps=1e-5
   m=regular_solution_energy(temperature_k=t,omega_j_mol=w,mole_fraction_b=x)
   lo=regular_solution_energy(temperature_k=t,omega_j_mol=w,mole_fraction_b=x-eps)['gibbs_mixing_j_mol']
   hi=regular_solution_energy(temperature_k=t,omega_j_mol=w,mole_fraction_b=x+eps)['gibbs_mixing_j_mol']
   self.assertAlmostEqual((hi-lo)/(2*eps),m['first_derivative_j_mol'],delta=.01)
   self.assertAlmostEqual((hi-2*m['gibbs_mixing_j_mol']+lo)/eps**2,m['second_derivative_j_mol'],delta=1.)
 def test_state_fraction_conservation(self):
  r=random.Random(351)
  for i in range(120):
   w=15000+r.random()*5000;t=(w/(2*R))*(.3+r.random()*.6)
   p=regular_solution_boundaries(temperature_k=t,omega_j_mol=w)
   a,b=p['binodal_mole_fraction_b'];x=a+(b-a)*(.1+r.random()*.8)
   state=regular_solution_state(temperature_k=t,omega_j_mol=w,mole_fraction_b=x)
   f=state['equilibrium_two_phase_fractions'];self.assertIsNotNone(f)
   self.assertAlmostEqual(f['low_x_phase']+f['high_x_phase'],1)
   self.assertAlmostEqual(f['low_x_phase']*a+f['high_x_phase']*b,x)
   self.assertGreaterEqual(state['free_energy_drop_to_equilibrium_j_mol'],-1e-11)
 def test_invalid(self):
  for x in (0,1,-.1,1.01,float('nan')):
   with self.assertRaises(MaterialsInputError):regular_solution_energy(temperature_k=800,omega_j_mol=20000,mole_fraction_b=x)
 def test_numeric_bound_refusal(self):
  with self.assertRaises(MaterialsInputError):regular_solution_boundaries(temperature_k=.01,omega_j_mol=1e7)

class TestCubicDiffraction(unittest.TestCase):
 def test_single_peak(self):
  p=cubic_peak_lattice(wavelength_angstrom=1.5406,h=1,k=1,l=1,two_theta_deg=45)
  self.assertAlmostEqual(p['d_spacing_angstrom'],1.5406/(2*math.sin(math.pi/8)))
 def test_roundtrip(self):
  r=random.Random(41)
  for i in range(100):
   wave=.3+r.random()*1.6;a=3.0+r.random()*4;h,k,l=1,1,1
   if wave*math.sqrt(3)/(2*a)>=1:continue
   tw=2*math.degrees(math.asin(wave*math.sqrt(3)/(2*a)))
   v=cubic_peak_lattice(wavelength_angstrom=wave,h=h,k=k,l=l,two_theta_deg=tw)
   self.assertAlmostEqual(v['lattice_parameter_angstrom'],a,places=11)
 def test_ideal_multi(self):
  wave=1.5406;true_a=3.61
  peaks=[]
  for hkl in [(1,1,1),(2,0,0),(2,2,0),(3,1,1)]:
   tw=2*math.degrees(math.asin(wave*math.sqrt(sum(k*k for k in hkl))/(2*true_a)))
   peaks.append(dict(zip(('h','k','l'),hkl),two_theta_deg=tw,u_two_theta_deg=.015))
  r=cubic_lattice_from_indexed_peaks(wavelength_angstrom=wave,wavelength_standard_uncertainty_angstrom=.0001,peaks=peaks)
  self.assertAlmostEqual(r['mean_lattice_parameter_angstrom'],true_a,places=10)
  self.assertLess(r['chi_square'],1e-12)
  self.assertAlmostEqual(r['standard_uncertainty_shared_wavelength_angstrom'],true_a*.0001/wave)
 def test_shared_wavelength_never_shrinks_with_more_peaks(self):
  wave=1.5406;a=4
  all_peaks=[]
  for hkl in [(1,0,0),(1,1,0),(1,1,1),(2,0,0),(2,1,0)]:
   n=sum(k*k for k in hkl)
   tw=2*math.degrees(math.asin(wave*math.sqrt(n)/(2*a)))
   all_peaks.append(dict(zip(('h','k','l'),hkl),two_theta_deg=tw,u_two_theta_deg=.01))
  three=cubic_lattice_from_indexed_peaks(wavelength_angstrom=wave,wavelength_standard_uncertainty_angstrom=.001,peaks=all_peaks[:3])
  five=cubic_lattice_from_indexed_peaks(wavelength_angstrom=wave,wavelength_standard_uncertainty_angstrom=.001,peaks=all_peaks)
  self.assertAlmostEqual(three['standard_uncertainty_shared_wavelength_angstrom'],five['standard_uncertainty_shared_wavelength_angstrom'],places=12)
  self.assertLess(five['standard_uncertainty_angle_angstrom'],three['standard_uncertainty_angle_angstrom'])
 def test_invalid(self):
  for kw in [{'h':0,'k':0,'l':0,'two_theta_deg':30},{'h':1,'k':1,'l':1,'two_theta_deg':180},{'h':1.0,'k':1,'l':1,'two_theta_deg':30}]:
   with self.assertRaises(MaterialsInputError):cubic_peak_lattice(wavelength_angstrom=1.54,**kw)
 def test_repeated_family_rejected(self):
  p=[{'h':1,'k':1,'l':1,'two_theta_deg':30,'u_two_theta_deg':.01}]*3
  with self.assertRaises(MaterialsInputError):cubic_lattice_from_indexed_peaks(wavelength_angstrom=1.5,wavelength_standard_uncertainty_angstrom=0,peaks=p)
 def test_missing_uncertainty_rejected(self):
  p=[{'h':1,'k':1,'l':1,'two_theta_deg':30,'u_two_theta_deg':.01}]*2+[{'h':2,'k':0,'l':0,'two_theta_deg':40}]
  with self.assertRaises(MaterialsInputError):cubic_lattice_from_indexed_peaks(wavelength_angstrom=1.5,wavelength_standard_uncertainty_angstrom=0,peaks=p)
 def test_bad_sigma_rejected(self):
  p=[{'h':1,'k':1,'l':1,'two_theta_deg':30,'u_two_theta_deg':0},{'h':2,'k':0,'l':0,'two_theta_deg':40,'u_two_theta_deg':.01},{'h':2,'k':2,'l':0,'two_theta_deg':50,'u_two_theta_deg':.01}]
  with self.assertRaises(MaterialsInputError):cubic_lattice_from_indexed_peaks(wavelength_angstrom=1.5,wavelength_standard_uncertainty_angstrom=.001,peaks=p)

class TestHahnDiagnostics(unittest.TestCase):
 def test_diagnostics(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_invalid_bin_count(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_casebook(self):self.assertEqual(expanded_casebook()['status'],'passed')
if __name__=='__main__':unittest.main()
