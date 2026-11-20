import unittest,math
from bioelectric_atlas.instruments import *
class InstrumentsTest(unittest.TestCase):
 def test_dc_resistive_parallel(self):
  d=electrode_dummy_impedance(100,900,1e-6,0)
  self.assertAlmostEqual(d['real_ohm'],1000)
 def test_hf_limit(self):
  d=electrode_dummy_impedance(100,900,1e-6,1e12)
  self.assertAlmostEqual(d['real_ohm'],100,places=6)
 def test_negative_imaginary(self):
  self.assertLess(electrode_dummy_impedance(100,900,1e-6,100)['imag_ohm'],0)
 def test_infinite_capacitance_not_permitted(self):
  with self.assertRaises(ValueError):electrode_dummy_impedance(1,1,float('inf'),0)
 def test_not_biomedical_stimulation(self):
  self.assertFalse(electrode_dummy_impedance(100,900,1e-6,100)['human_or_animal_connection_authorized'])
 def test_adc_endpoints(self):
  self.assertEqual(adc_ideal_quantize(0,0,1,8)['code'],0)
  self.assertEqual(adc_ideal_quantize(1,0,1,8)['code'],255)
 def test_adc_midpoint(self):
  self.assertEqual(adc_ideal_quantize(0.5,0,1,3)['code'],4)
 def test_adc_clips(self):
  self.assertTrue(adc_ideal_quantize(-1,0,1,8)['clipped'])
  self.assertTrue(adc_ideal_quantize(2,0,1,8)['clipped'])
 def test_adc_no_error_beyond_half_step(self):
  for j in range(1001):
   v=j/1000;y=adc_ideal_quantize(v,0,1,10)
   self.assertLessEqual(abs(v-y['reconstructed_volts']),y['step_volts']/2+1e-12)
 def test_adc_invalid_bits(self):
  for b in (0,25,1.2,True):
   with self.assertRaises(ValueError):adc_ideal_quantize(0,0,1,b)
 def test_sine_aliased_exact_sample(self):
  fs=100
  x=uniform_sample_sine(1,17,fs,200)
  y=uniform_sample_sine(1,117,fs,200)
  self.assertLess(max(abs(a-b) for a,b in zip(x,y)),1e-12)
 def test_sine_sample_count(self):
  self.assertEqual(len(uniform_sample_sine(1,1,10,100)),100)
 def test_noise_deterministic(self):
  self.assertEqual(deterministic_voltage_noise([0.1]*12,0.2,43),deterministic_voltage_noise([0.1]*12,0.2,43))
 def test_noise_seed_changes(self):
  self.assertNotEqual(deterministic_voltage_noise([0.1]*12,0.2,43)['sha256'],deterministic_voltage_noise([0.1]*12,0.2,44)['sha256'])
 def test_rss_error(self):
  self.assertAlmostEqual(root_sum_square_uncertainty([3,4]),5)
 def test_rss_correlation_not_claimed(self):
  self.assertEqual(root_sum_square_uncertainty([0,0,0]),0)
 def test_rss_empty_refused(self):
  with self.assertRaises(ValueError):root_sum_square_uncertainty([])
if __name__=='__main__':unittest.main()
