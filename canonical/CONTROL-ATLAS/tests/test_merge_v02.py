"""Independent lineage preservation tests; these do not certify hardware control."""
import json,hashlib,unittest
from pathlib import Path
from atlas_forge.common import AtlasStore
from control_atlas.cases import casebook
from control_atlas.extended_cases import casebook as extended_casebook
from control_atlas import models, methods
R=Path(__file__).resolve().parents[1]
class TestMergedScientificData(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.store=AtlasStore(R/'control_atlas/resources/common')
  cls.records={r['record_id']:r for r in cls.store.export()}
 def test_counts(self):
  self.assertGreaterEqual(len(self.records),117)
  self.assertGreaterEqual(sum(r['type']=='source' for r in self.records.values()),27)
  self.assertGreaterEqual(len(self.store._relations),64)
 def test_old_revisions(self):
  old=json.loads((R/'evidence/retained_old_control_v0.1.0_revisions.json').read_text())
  self.assertEqual(len(old),60)
  self.assertTrue(all(self.records[k]['revision']==v for k,v in old.items()))
 def test_old_edges(self):
  old=json.loads((R/'evidence/old_control_v0.1.0_relations.json').read_text())
  self.assertEqual(len(old),36)
  self.assertTrue(all(self.store._relations[k]['revision']==v for k,v in old.items()))
 def test_mapped_additions(self):
  additions=json.loads((R/'evidence/addition_v0.2_record_map.json').read_text())
  self.assertEqual(len(additions),57)
  self.assertEqual(sum(k!=v['merged_record_id'] for k,v in additions.items()),2)
  for k,v in additions.items():self.assertEqual(self.records[v['merged_record_id']]['revision'],v['revision'])
 def test_sources_closed_and_distinct(self):
  self.assertIn('control-atlas:source:MIT-LQR',self.records)
  self.assertIn('control-atlas:v02-source:MIT-LQR',self.records)
  for r in self.records.values():
   for link in r['sources']:
    src=self.records[link['record_id']]
    self.assertEqual(src['type'],'source')
    self.assertEqual(link['revision'],src['revision'])
 def test_both_casebooks_pass(self):
  self.assertEqual(casebook()['result'],'passed')
  self.assertEqual(extended_casebook()['status'],'passed')
 def test_both_tools_not_equated(self):
  self.assertTrue(callable(models.scalar_finite_lqr))
  self.assertTrue(callable(methods.scalar_lqr))
  self.assertTrue(callable(models.pi_first_order_simulation))
  self.assertTrue(callable(methods.pid_saturated_demo))
 def test_no_hardware(self):
  self.assertFalse(hasattr(models,'connect_hardware'))
  self.assertFalse(hasattr(methods,'connect_hardware'))
 def test_context(self):
  for q in ['scalar Riccati LQR optimal model','saturated PI antiwindup model','scalar ARX identification input excitation']:
   p=self.store.assemble_context(q,node_ids=['control-atlas'])
   self.assertTrue(self.store.validate_context(p)['valid'])
   self.assertEqual(p['status'],'context_available')
 def test_manual_archive(self):
  self.assertGreaterEqual(len(list((R/'docs/chapters').glob('*.md'))),26)
  self.assertGreaterEqual(len(list((R/'docs/investigations').glob('*.md'))),18)
  self.assertTrue((R/'docs/legacy_v0.1.0/DEPTH_MANUAL_v0.1.0.md').exists())
if __name__=='__main__':unittest.main()
