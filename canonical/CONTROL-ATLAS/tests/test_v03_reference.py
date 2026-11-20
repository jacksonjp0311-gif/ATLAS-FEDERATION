"""Control 0.3 revision-preservation, exact closure and release-scope tests."""
import json,hashlib,unittest
from pathlib import Path
from atlas_forge.common import AtlasStore
from control_atlas.robust_cases import casebook
R=Path(__file__).resolve().parents[1]

class V03ScientificContent(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.store=AtlasStore(R/'control_atlas/resources/common')
  cls.records={r['record_id']:r for r in cls.store.export()}
 def test_total(self):
  self.assertGreaterEqual(len(self.records),145)
  self.assertGreaterEqual(sum(r['type']=='source' for r in self.records.values()),32)
  self.assertGreaterEqual(len(self.store._relations),81)
 def test_prior_117_and_64_revisions_unchanged(self):
  old=json.loads((R/'evidence/baseline_control_v0.2_revisions.json').read_text())['records']
  rel=json.loads((R/'evidence/baseline_control_v0.2_relations.json').read_text())['relations']
  self.assertEqual(len(old),117);self.assertEqual(len(rel),64)
  for rid,h in old.items():self.assertEqual(self.records[rid]['revision'],h,rid)
  for rid,h in rel.items():self.assertEqual(self.store._relations[rid]['revision'],h,rid)
 def test_new_record_maturity(self):
  new=[r for r in self.records.values() if r['provenance'].get('edition_added')=='0.3.0']
  self.assertEqual(len(new),28)
  for r in new:
   self.assertFalse(r['provenance']['independent_review'])
   self.assertTrue(r['content']['limitations'])
   for s in r['sources']:
    self.assertEqual(self.records[s['record_id']]['type'],'source')
    self.assertEqual(self.records[s['record_id']]['revision'],s['revision'])
 def test_source_cards_inspected_scope(self):
  src=json.loads((R/'evidence/source_inspection_v0.3.0.json').read_text())
  self.assertEqual(len(src),5)
  self.assertTrue(all(not x['source_bytes_archived'] and not x['independent_human_review'] for x in src))
 def test_robust_cases(self):
  self.assertEqual(casebook()['status'],'passed')
  self.assertEqual(casebook()['count'],8)
 def test_manual_and_chapters(self):
  self.assertGreaterEqual(len(list((R/'docs/chapters').glob('*.md'))),33)
  self.assertGreaterEqual(len(list((R/'docs/investigations').glob('*.md'))),24)
  self.assertIn('one sample', (R/'docs/DEPTH_MANUAL_v0.3.0.md').read_text().lower())
 def test_source_closure_and_context(self):
  for q in ['robust scalar pole interval box', 'Lyapunov P candidate','feedback delay one sample',
            'model residual whiteness not proven','stale sensor offline watchdog']:
   with self.subTest(q=q):
    p=self.store.assemble_context(q,node_ids=['control-atlas'])
    self.assertTrue(self.store.validate_context(p)['valid'])
    self.assertEqual(p['status'],'context_available')
if __name__=='__main__':unittest.main()
