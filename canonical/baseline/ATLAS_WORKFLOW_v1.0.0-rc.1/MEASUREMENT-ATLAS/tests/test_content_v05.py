from pathlib import Path
import importlib.util,json,math,unittest
ROOT=Path(__file__).resolve().parents[1]
def module(name):
 spec=importlib.util.spec_from_file_location(name,ROOT/'tools'/f'{name}.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class ContentTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.data=json.loads((ROOT/'evidence/primary_reference_additions.json').read_text());cls.records={r['id']:r for r in cls.data['records']};cls.casebook=module('content_casebook').run();cls.cases={c['id']:c for c in cls.casebook['cases']}
 def test_inventory(self):self.assertEqual(len(self.records),92);self.assertEqual(len(self.data['sources']),43)
 def test_content_link_audit(self):self.assertTrue(module('check_content').check()['valid'])
 def test_prior_source_material_retained(self):
  old=json.loads((ROOT/'history/v0.4.0/primary_reference_additions.json').read_text())
  for r in old['records']:
   n=self.records[r['id']]
   for field in ['id','title','text','source','locator','origin','equation']:self.assertEqual(r[field],n[field])
 def test_all_records_have_qualifiers(self):self.assertTrue(all(r['assumptions'] and r['limitations'] for r in self.records.values()))
 def test_all_sources_https(self):self.assertTrue(all(s['url'].startswith('https://') for s in self.data['sources']))
 def test_archived_source_warning(self):self.assertIn('no-longer-updated',next(s for s in self.data['sources'] if s['id']=='TN7')['freshness_note'])
 def test_chapters_exist(self):self.assertEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),8)
 def test_templates_are_explicit(self):self.assertEqual(len(list((ROOT/'templates').glob('*.md'))),4)
 def test_authored_questions_not_held_out(self):
  q=json.loads((ROOT/'evaluations/content_review_questions.json').read_text());self.assertFalse(q['independently_held_out']);self.assertEqual(len(q['cases']),30)
 def test_content_v1_not_promoted(self):self.assertFalse(json.loads((ROOT/'evaluations/content_coverage.json').read_text())['scientific_v1_ready'])
 def test_twelve_new_examples_pass(self):self.assertEqual(self.casebook['case_count'],12);self.assertTrue(all(c['passed'] for c in self.cases.values()))
 def test_all_examples_explicitly_synthetic(self):self.assertTrue(all(c['data_origin']=='synthetic_teaching_example' for c in self.cases.values()));self.assertFalse(self.casebook['actual_measurements'])
 def test_casebook_references_resolve(self):
  for c in self.cases.values():self.assertFalse(set(c['reference_ids'])-self.records.keys())
 def test_temperature_uncertainty_not_offset(self):self.assertEqual(self.cases['temperature-offset']['results']['u_K'],.3)
 def test_common_offset_remains(self):self.assertGreater(self.cases['shared-offset']['results']['u_mm'],.2)
 def test_correlated_difference(self):self.assertAlmostEqual(self.cases['difference-covariance']['results']['u_mm'],math.sqrt(.07))
 def test_calibration_coefficient_covariance(self):self.assertAlmostEqual(self.cases['inverse-calibration']['results']['variance'],.00325)
 def test_nonlinearity_counterexample(self):
  r=self.cases['nonlinear-counterexample']['results'];self.assertEqual(r['first_order_variance'],0);self.assertGreater(r['exact_variance'],0)
 def test_derived_records_labeled(self):
  for rid in ['correlated-mean','shared-offset-average','quantization-assumption','linearization-counterexample','inverse-calibration-sensitivities']:self.assertEqual(self.records[rid]['origin'],'formal_derivation')
 def test_effective_dof_not_probability(self):self.assertEqual(self.cases['effective-dof']['results']['nu_eff'],20);self.assertIn('No t quantile',self.cases['effective-dof']['limitations'][0])
