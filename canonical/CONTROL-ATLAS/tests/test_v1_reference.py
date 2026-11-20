"""Source and revision integrity of Control v1 candidate; tests do not certify science."""
import unittest,json,hashlib
from pathlib import Path
from control_atlas.v1_cases import v1_casebook
from atlas_forge.common import AtlasStore
R=Path(__file__).resolve().parents[1]

class ControlV1Reference(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.store=AtlasStore(R/'control_atlas/resources/common')
  cls.recs={r['record_id']:r for r in cls.store.export()}
 def test_inventory_and_history_exact(self):
  self.assertEqual(len(self.recs),249)
  self.assertEqual(sum(r['type']=='source' for r in self.recs.values()),51)
  self.assertEqual(len(self.store._relations),147)
  old=json.loads((R/'evidence/old_control_v0.6_revisions.json').read_text())['records']
  self.assertEqual(len(old),214)
  for k,rev in old.items():self.assertEqual(self.recs[k]['revision'],rev,k)
  relations=json.loads((R/'evidence/old_control_v0.6_relations.json').read_text())['relations']
  self.assertEqual(len(relations),124)
  for k,rev in relations.items():self.assertEqual(self.store._relations[k]['revision'],rev,k)
 def test_source_links_closed(self):
  for r in self.recs.values():
   for s in r['sources']:
    self.assertEqual(s['revision'],self.recs[s['record_id']]['revision'])
    self.assertEqual(self.recs[s['record_id']]['type'],'source')
  self.assertEqual(sum(r['provenance'].get('edition_added')=='1.0.0' for r in self.recs.values()),35)
 def test_source_maturity(self):
  for r in self.recs.values():
   if r['provenance'].get('edition_added')=='1.0.0':
    self.assertFalse(r['provenance']['independent_review'])
    self.assertTrue(r['content']['limitations'])
  for suffix in ('OPENMCT-MENDELEY-V2','GITHUB-MOTOR-PWM30','GITHUB-MOTOR-PWM50','GITHUB-MOTOR-PWM70'):
   r=self.recs['control-atlas:source:'+suffix]
   self.assertFalse(r['provenance']['source_bytes_archived'])
 def test_rpm_summaries_no_false_input(self):
  p=R/'evidence/v1_sources/public_motor_rpm_summary.json'
  o=json.loads(p.read_text())
  self.assertEqual([s['n'] for s in o['series']],[49,49,49])
  self.assertFalse(o['analysis']['plant_transfer_function_identified'])
  self.assertFalse(o['raw_bytes_archived'])
  self.assertTrue(o['analysis']['PWM_30_50_70_are_filename_labels'])
 def test_reading_path_and_refusal(self):
  chapters=list((R/'docs/chapters').glob('*.md'))
  investigations=list((R/'docs/investigations').glob('*.md'))
  self.assertEqual(len(chapters),61)
  self.assertEqual(len(investigations),49)
  guide=(R/'docs/REFERENCE_GUIDE.md').read_text()
  for x in chapters+investigations:
   with self.subTest(file=x.name):self.assertIn(x.name,guide)
  self.assertIn('raw', (R/'docs/COVERAGE_MATRIX.md').read_text().lower())
 def test_casebook(self):
  result=v1_casebook()
  self.assertEqual(result['status'],'passed')
  self.assertEqual(result['count'],6)
  self.assertFalse(result['openmct_publisher_raw_data_analyzed'])
  self.assertFalse(result['safety_certified'])
 def test_forge_context_with_new_evidence(self):
  for query in ('OpenMCT source dataset PWM REF','motor constant input','two sensor observer error bound','DMM duplicate asynchronous'):
   with self.subTest(query=query):
    p=self.store.assemble_context(query,node_ids=['control-atlas'])
    self.assertEqual(p['status'],'context_available',query)
    self.assertTrue(self.store.validate_context(p)['valid'])
 def test_installed_api_does_not_actuate(self):
  import control_atlas.empirical as e
  import control_atlas.multivariable as m
  self.assertFalse(hasattr(e,'connect_plc'))
  self.assertFalse(hasattr(m,'command_motor'))
  self.assertIn('30 domain', (R/'README.md').read_text())
if __name__=='__main__':unittest.main()
