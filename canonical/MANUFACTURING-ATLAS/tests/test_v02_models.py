import unittest, math, itertools, random
from manufacturing_atlas.v02_models import (
 covariance_budget_psd,wilson_yield_interval,normal_inspection_acceptance_risk,
 stable_process_capability,resource_bounded_schedule,datum_rigid_transform_xy,
 traceability_chain_audit,manufacturing_evidence_gate)

class ManufacturingV02Tests(unittest.TestCase):
 def test_covariance_diagonal(self):
  a=covariance_budget_psd([[9,0],[0,16]])
  self.assertAlmostEqual(a['standard_uncertainty'],5)
 def test_covariance_positive(self):
  self.assertAlmostEqual(covariance_budget_psd([[1,.5],[.5,1]])['standard_uncertainty'],math.sqrt(3))
 def test_covariance_negative_correlation(self):
  self.assertAlmostEqual(covariance_budget_psd([[1,-.5],[-.5,1]])['standard_uncertainty'],1)
 def test_covariance_zero(self):
  self.assertEqual(covariance_budget_psd([[0,0],[0,0]])['standard_uncertainty'],0)
 def test_covariance_singular(self):
  self.assertAlmostEqual(covariance_budget_psd([[1,1],[1,1]],(1,-1))['standard_uncertainty'],0,places=6)
 def test_covariance_non_psd_even_pairwise_bounds(self):
  # All |Covij|<=σi σj but eigenvalue -0.8 -> reject.
  with self.assertRaises(ValueError):covariance_budget_psd([[1,.9,.9],[.9,1,-.9],[.9,-.9,1]])
 def test_covariance_asymmetric(self):
  with self.assertRaises(ValueError):covariance_budget_psd([[1,.1],[.5,1]])
 def test_covariance_negative_diagonal(self):
  with self.assertRaises(ValueError):covariance_budget_psd([[-1]])
 def test_covariance_sensitivity(self):
  self.assertAlmostEqual(covariance_budget_psd([[4,0],[0,9]],(2,3))['standard_uncertainty'],math.sqrt(97))
 def test_covariance_dimensions(self):
  with self.assertRaises(ValueError):covariance_budget_psd([[1,2],[2]])
 def test_wilson_all_successes_not_certainty(self):
  r=wilson_yield_interval(100,100)
  self.assertEqual(r['estimated_pass_fraction'],1.)
  self.assertLess(r['lower'],1.)
  self.assertGreater(r['lower'],.95)
 def test_wilson_zero_successes(self):
  r=wilson_yield_interval(0,100)
  self.assertEqual(r['lower'],0.)
  self.assertGreater(r['upper'],0.)
 def test_wilson_symmetry(self):
  a=wilson_yield_interval(20,100);b=wilson_yield_interval(80,100)
  self.assertAlmostEqual(a['lower'],1-b['upper'])
 def test_wilson_invalid(self):
  for args in ((101,100),(0,0),(-1,100),(10,9),(1,10,1)):
   with self.assertRaises(ValueError):wilson_yield_interval(*args)
 def test_normal_inspection_symmetry(self):
  p=normal_inspection_acceptance_risk(0,1,-1,1,0)
  self.assertAlmostEqual(p['accept_given_true_value_probability'],.6826894921370859)
 def test_normal_inspection_guard_reduces_acceptance(self):
  a=normal_inspection_acceptance_risk(0,.2,-1,1,.1)
  b=normal_inspection_acceptance_risk(0,.2,-1,1,.3)
  self.assertGreater(a['accept_given_true_value_probability'],b['accept_given_true_value_probability'])
 def test_normal_inspection_false_accept_outside_spec(self):
  p=normal_inspection_acceptance_risk(1.5,.2,-1,1,.1)
  self.assertFalse(p['true_value_within_spec']);self.assertGreaterEqual(p['accept_given_true_value_probability'],0)
 def test_normal_inspection_invalid(self):
  with self.assertRaises(ValueError):normal_inspection_acceptance_risk(0,0,-1,1,0)
  with self.assertRaises(ValueError):normal_inspection_acceptance_risk(0,1,-1,1,1.1)
 def test_process_capability_holds_until_flags(self):
  v=[10+math.sin(i)*.1 for i in range(20)]
  out=stable_process_capability(v,9,11,False,False)
  self.assertIsNone(out['cpk'])
 def test_process_capability_formula_conditional(self):
  v=[10+math.sin(i)*.1 for i in range(20)]
  out=stable_process_capability(v,9,11,True,True)
  self.assertAlmostEqual(out['cpk'],min(11-out['mean'],out['mean']-9)/(3*out['sample_sigma']))
  self.assertIn('not_authenticated',out['status'])
 def test_process_capability_zero_spread(self):
  with self.assertRaises(ValueError):stable_process_capability([5]*20,4,6,True,True)
 def test_process_capability_too_few(self):
  with self.assertRaises(ValueError):stable_process_capability([5]*7,4,6,True,True)
 def test_schedule_simple(self):
  ops={'A':{'duration_min':3,'resource':'cut'},'B':{'duration_min':5,'resource':'drill','depends_on':['A']},'C':{'duration_min':7,'resource':'cut'},'D':{'duration_min':2,'resource':'inspect','depends_on':['B','C']}}
  out=resource_bounded_schedule(ops)
  self.assertEqual(out['resource_conflicts'],0)
  self.assertEqual(out['dependencies_violated'],0)
  self.assertGreaterEqual(out['makespan_min'],10)
 def test_schedule_resource_sequential(self):
  ops={'A':{'duration_min':3,'resource':'one'},'B':{'duration_min':4,'resource':'one'}}
  out=resource_bounded_schedule(ops)['schedule']
  self.assertEqual(out['B']['start_min'],3)
 def test_schedule_invalid_resource(self):
  with self.assertRaises(ValueError):resource_bounded_schedule({'A':{'duration_min':3,'resource':''}})
 def test_schedule_cycle(self):
  with self.assertRaises(ValueError):resource_bounded_schedule({'A':{'duration_min':2,'resource':'a','depends_on':['B']},'B':{'duration_min':1,'resource':'b','depends_on':['A']}})
 def test_schedule_unknown(self):
  with self.assertRaises(ValueError):resource_bounded_schedule({'A':{'duration_min':2,'resource':'a','depends_on':['B']}})
 def test_datum_rotation(self):
  p=datum_rigid_transform_xy((1,0),(3,5),math.pi/2)
  self.assertAlmostEqual(p[0],3)
  self.assertAlmostEqual(p[1],6)
 def test_datum_invertible(self):
  rng=random.Random(5)
  for i in range(60):
   p=(rng.uniform(-2,2),rng.uniform(-2,2));o=(rng.random(),rng.random());t=rng.uniform(-3,3);sc=rng.uniform(.2,4)
   q=datum_rigid_transform_xy(p,o,t,sc)
   r=datum_rigid_transform_xy((q[0]-o[0],q[1]-o[1]),(0,0),-t,1/sc)
   self.assertAlmostEqual(r[0],p[0],places=12);self.assertAlmostEqual(r[1],p[1],places=12)
 def test_datum_invalid(self):
  with self.assertRaises(ValueError):datum_rigid_transform_xy((0,1),(2,3),0,0)
 def test_traceability_claim_not_authenticity(self):
  good={'gauge':{'parent':'lab','unit':'mm','standard_uncertainty':.01,'valid_through':20271231,'sha256':'a'*64},
        'lab':{'parent':None,'unit':'mm','standard_uncertainty':.001,'valid_through':20271231,'sha256':'b'*64}}
  result=traceability_chain_audit(good,'gauge',20261116)
  self.assertEqual(result['status'],'documentation_present_not_source_authenticated')
  self.assertFalse(result['original_source_bytes_authenticated'])
 def test_traceability_expiry(self):
  g={'g':{'parent':None,'unit':'mm','standard_uncertainty':.01,'valid_through':20250101,'sha256':'a'*64}}
  self.assertTrue(traceability_chain_audit(g,'g',20261116)['issues'])
 def test_traceability_missing_parent(self):
  g={'g':{'parent':'missing','unit':'mm','standard_uncertainty':.01,'valid_through':20270101,'sha256':'a'*64}}
  self.assertIn('missing record missing',traceability_chain_audit(g,'g',20261116)['issues'])
 def test_traceability_cycle(self):
  g={'a':{'parent':'b'},'b':{'parent':'a'}}
  with self.assertRaises(ValueError):traceability_chain_audit(g,'a',20261116)
 def test_gate_missing_evidence(self):
  steps={'inspect':{'depends_on':[],'inputs':['part'],'outputs':['accepted'],'required_evidence':['calibration','measurements']}}
  out=manufacturing_evidence_gate(steps,['part'],{'calibration':'sha256hex'})
  self.assertFalse(out['structurally_complete']);self.assertIn('measurements',out['missing_evidence_ids'])
 def test_gate_recorded_not_certified(self):
  steps={'inspect':{'depends_on':[],'inputs':['part'],'outputs':['accepted'],'required_evidence':['calibration']}}
  out=manufacturing_evidence_gate(steps,['part'],{'calibration':'metadata'})
  self.assertTrue(out['structurally_complete']);self.assertFalse(out['independently_certified'])
 def test_gate_dependency_hold_propagates(self):
  steps={'A':{'depends_on':[],'inputs':['stock'],'outputs':['part'],'required_evidence':['material']},
         'B':{'depends_on':['A'],'inputs':['part'],'outputs':['finished'],'required_evidence':['measurement']}}
  out=manufacturing_evidence_gate(steps,['stock'],{'measurement':1})
  self.assertFalse(out['structurally_complete'])
  self.assertEqual(out['steps']['B']['status'],'HOLD_missing_inputs_or_evidence')
 def test_gate_cycle(self):
  with self.assertRaises(ValueError):manufacturing_evidence_gate({'A':{'depends_on':['B']},'B':{'depends_on':['A']}},[],{})
 def test_gate_duplicate_output(self):
  steps={'A':{'depends_on':[],'inputs':['stock'],'outputs':['part'],'required_evidence':[]},
         'B':{'depends_on':['A'],'inputs':['part'],'outputs':['part'],'required_evidence':[]}}
  with self.assertRaises(ValueError):manufacturing_evidence_gate(steps,['stock'],{})

if __name__=='__main__':unittest.main()
