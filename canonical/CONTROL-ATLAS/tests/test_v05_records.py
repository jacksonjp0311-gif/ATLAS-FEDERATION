import unittest,json
from pathlib import Path
from atlas_forge.common import AtlasStore
from control_atlas.invariance_cases import casebook
ROOT=Path(__file__).resolve().parents[1]
class ContentV05(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.store=AtlasStore(ROOT/'control_atlas/resources/common')
  cls.recs={r['record_id']:r for r in cls.store.export()}
 def test_current_exact(self):
  self.assertGreaterEqual(len(self.recs),191)
  self.assertGreaterEqual(len(self.store._relations),107)
  self.assertGreaterEqual(sum(r['type']=='source' for r in self.recs.values()),42)
 def test_old_record_revisions_preserved(self):
  original=json.loads((ROOT/'evidence/baseline_control_v0.4_revisions.json').read_text())['records']
  self.assertEqual(len(original),173)
  for k,v in original.items():self.assertEqual(self.recs[k]['revision'],v,k)
 def test_old_relation_revisions_preserved(self):
  original=json.loads((ROOT/'evidence/baseline_control_v0.4_relations.json').read_text())['relations']
  self.assertEqual(len(original),96)
  for k,v in original.items():self.assertEqual(self.store._relations[k]['revision'],v,k)
 def test_new_statuses_do_not_claim_physical_safety(self):
  additions=[r for r in self.recs.values() if r['provenance'].get('edition_added')=='0.5.0']
  self.assertEqual(len(additions),18)
  self.assertTrue(all(r['provenance']['independent_review'] is False for r in additions))
  for r in additions:
   self.assertTrue(r['content']['limitations'])
   for s in r['sources']:
    self.assertEqual(self.recs[s['record_id']]['revision'],s['revision'])
 def test_new_contexts(self):
  for q in ['robust 2state box 64 corners','exact state feedback invariant box','bounded actuator feedback','biased observer synthetic rollout']:
   with self.subTest(q=q):
    p=self.store.assemble_context(q,node_ids=['control-atlas'])
    self.assertEqual(p['status'],'context_available')
    self.assertTrue(self.store.validate_context(p)['valid'])
 def test_full_reference_guide(self):
  self.assertGreaterEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),46)
  self.assertGreaterEqual(len(list((ROOT/'docs/investigations').glob('*.md'))),36)
  guide=(ROOT/'docs/REFERENCE_GUIDE.md').read_text()
  for f in list((ROOT/'docs/chapters').glob('*.md'))+list((ROOT/'docs/investigations').glob('*.md')):
   self.assertIn(f.name,guide)
 def test_cases(self):self.assertEqual(casebook()['status'],'passed')
if __name__=='__main__':unittest.main()
