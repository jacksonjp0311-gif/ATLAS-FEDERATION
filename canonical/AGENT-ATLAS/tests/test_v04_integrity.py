"""v0.4 corpus, source-closure and release-scope checks (not scientific review)."""
import unittest,json,hashlib
from pathlib import Path
from atlas_forge.common import AtlasStore,revision
from agent_atlas.v04_cases import casebook_v04
R=Path(__file__).resolve().parents[1]
class AgentV04Integrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.s=AtlasStore(R/'agent_atlas/resources/common')
  cls.r={r['record_id']:r for r in cls.s.export()}
 def test_counts(self):
  self.assertGreaterEqual(len(self.r),158)
  self.assertGreaterEqual(sum(r['type']=='source' for r in self.r.values()),30)
  self.assertGreaterEqual(len(self.s._relations),101)
  self.assertEqual(sum(r['provenance'].get('edition_added')=='0.4.0' for r in self.r.values()),30)
 def test_old_record_revisions(self):
  d=json.loads((R/'evidence/previous_record_revisions_v0.3.0.json').read_text())
  self.assertEqual(len(d),128)
  for name,revision_id in d.items():self.assertEqual(self.r[name]['revision'],revision_id)
 def test_old_relation_revisions(self):
  d=json.loads((R/'evidence/previous_relation_revisions_v0.3.0.json').read_text())
  self.assertEqual(len(d),83)
  for name,revision_id in d.items():self.assertEqual(self.s._relations[name]['revision'],revision_id)
 def test_full_source_closure(self):
  for r in self.r.values():
   self.assertEqual(r['revision'],revision(r))
   for src in r['sources']:
    self.assertEqual(self.r[src['record_id']]['revision'],src['revision'])
    self.assertEqual(self.r[src['record_id']]['type'],'source')
  for rel in self.s._relations.values():
   self.assertEqual(rel['revision'],revision(rel))
   for direction in ('from','to'):
    self.assertEqual(self.r[rel[direction]['record_id']]['revision'],rel[direction]['revision'])
 def test_source_scope(self):
  scope=json.loads((R/'evidence/source_scope_v0.4.0.json').read_text())
  self.assertEqual(len(scope['sources']),3)
  self.assertEqual(scope['MAST_full_rows_loaded'],0)
  self.assertEqual(scope['MAST_human_rows_loaded'],0)
  self.assertEqual(scope['actual_agent_runs'],0)
  self.assertFalse(scope['independent_human_review'])
 def test_context(self):
  for query in ['paired benchmark contamination evaluator precommitment',
        'host dispatch SHA256 artifact conditional proof evidence',
        'mast label cohen kappa unknown annotation',
        'memory evidence contradictions expiry review']:
   with self.subTest(query=query):
    p=self.s.assemble_context(query,node_ids=['agent-atlas'])
    self.assertEqual(p['status'],'context_available')
    self.assertTrue(self.s.validate_context(p)['valid'])
 def test_manual_and_cases(self):
  self.assertGreaterEqual(len(list((R/'docs/chapters').glob('*.md'))),38)
  self.assertGreaterEqual(len(list((R/'docs/investigations').glob('*.md'))),24)
  self.assertEqual(casebook_v04()['count'],9)
  self.assertEqual(casebook_v04()['status'],'passed')
 def test_no_fabricated_live_evidence(self):
  for x in self.r.values():
   self.assertFalse(x['provenance']['independent_review'])
   self.assertTrue(x['content']['limitations'])
  self.assertIn('not a live agent',(R/'README.md').read_text().lower())
 def test_exact_node_copy(self):
  a=R/'agent_atlas/resources/common/nodes/agent-atlas';b=R.parent/'common/nodes/agent-atlas'
  for path in a.rglob('*'):
   if path.is_file():self.assertEqual(path.read_bytes(),(b/path.relative_to(a)).read_bytes())
 def test_guide_links(self):
  guide=(R/'docs/REFERENCE_GUIDE.md').read_text()
  for p in list((R/'docs/chapters').glob('*.md'))+list((R/'docs/investigations').glob('*.md')):
   self.assertIn(p.name,guide)
 def test_no_content_hijack(self):
  from agent_atlas import learning_science
  self.assertFalse(hasattr(learning_science,'execute_llm'))
  self.assertFalse(hasattr(learning_science,'send_tool'))
if __name__=='__main__':unittest.main()
