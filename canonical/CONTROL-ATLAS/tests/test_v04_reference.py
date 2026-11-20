"""Release-bound evidence checks; passing is not independent science or hardware proof."""
import json,unittest,hashlib,re
from pathlib import Path
from control_atlas.advanced_cases import casebook
from atlas_forge.common import AtlasStore
ROOT=Path(__file__).resolve().parents[1]

class ReferenceV04(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.store=AtlasStore(ROOT/'control_atlas/resources/common')
  cls.records={x['record_id']:x for x in cls.store.export()}
 def test_current_record_counts(self):
  self.assertGreaterEqual(len(self.records),173)
  self.assertGreaterEqual(len(self.store._relations),96)
  self.assertGreaterEqual(sum(x['type']=='source' for x in self.records.values()),39)
 def test_old_record_revisions_unchanged(self):
  old=json.loads((ROOT/'evidence/baseline_control_v0.3_revisions.json').read_text())['records']
  self.assertEqual(len(old),145)
  for rid,v in old.items():self.assertEqual(self.records[rid]['revision'],v,rid)
 def test_old_relation_revisions_unchanged(self):
  old=json.loads((ROOT/'evidence/baseline_control_v0.3_relations.json').read_text())['relations']
  self.assertEqual(len(old),81)
  for rid,v in old.items():self.assertEqual(self.store._relations[rid]['revision'],v,rid)
 def test_all_sources_closed_and_maturity_explicit(self):
  for r in self.records.values():
   self.assertFalse(r['provenance']['independent_review'])
   self.assertTrue(r['content']['limitations'])
   for s in r['sources']:
    self.assertEqual(self.records[s['record_id']]['type'],'source')
    self.assertEqual(self.records[s['record_id']]['revision'],s['revision'])
 def test_new_records_are_separately_attributed(self):
  new=[x for x in self.records.values() if x['provenance'].get('edition_added')=='0.4.0']
  self.assertEqual(len(new),28)
  for r in new:
   self.assertNotEqual(r['evidence']['review_status'],'independently_reproduced')
   self.assertNotEqual(r['evidence']['review_status'],'human_reviewed')
 def test_new_docs_and_casebook(self):
  self.assertGreaterEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),40)
  self.assertGreaterEqual(len(list((ROOT/'docs/investigations').glob('*.md'))),31)
  self.assertEqual(casebook()['count'],9)
  self.assertEqual(casebook()['status'],'passed')
 def test_guide_contains_each_chapter_and_case(self):
  s=(ROOT/'docs/REFERENCE_GUIDE.md').read_text()
  for p in list((ROOT/'docs/chapters').glob('*.md'))+list((ROOT/'docs/investigations').glob('*.md')):
   self.assertIn(p.name,s)
 def test_context_new_terms_preserve_source_closure(self):
  queries=['common Lyapunov box vertex','multivariable singular return difference',
           'two sensor innovation covariance','model predictive control finite grid',
           'NIST OT rev4 initial public draft']
  for query in queries:
   with self.subTest(query=query):
    ctx=self.store.assemble_context(query,node_ids=['control-atlas'])
    self.assertTrue(self.store.validate_context(ctx)['valid'])
    self.assertEqual(ctx['status'],'context_available')
 def test_source_current_draft_not_final(self):
  text=(ROOT/'docs/chapters/40_ot_governance_and_scientific_release_gates.md').read_text()
  self.assertIn('Initial Public Draft',text)
  self.assertIn('not a final standard',text)
  self.assertIn('routing',text.lower())
 def test_limits_no_fabricated_actuation(self):
  readme=(ROOT/'README.md').read_text().lower()
  self.assertIn('no actuator drivers',readme)
  self.assertIn('30',readme)
  self.assertIn('no real equipment',readme)

if __name__=='__main__':unittest.main()
