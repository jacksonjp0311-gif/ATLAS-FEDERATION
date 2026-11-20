import unittest,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R.parent/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore, revision
from agent_atlas.advanced_cases import advanced_casebook

class V02Integrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.store=AtlasStore(R/'agent_atlas/resources/common')
  cls.by={r['record_id']:r for r in cls.store.export()}
 def test_immutable_v01_record_revisions(self):
  old=json.loads((R/'evidence/previous_record_revisions_v0.1.0.json').read_text())
  self.assertEqual(len(old),73)
  for k,rev in old.items():self.assertEqual(self.by[k]['revision'],rev,k)
 def test_immutable_v01_relation_revisions(self):
  old=json.loads((R/'evidence/previous_relation_revisions_v0.1.0.json').read_text())
  self.assertEqual(len(old),45)
  for k,rev in old.items():self.assertEqual(self.store._relations[k]['revision'],rev,k)
 def test_v02_new_counts(self):
  self.assertGreaterEqual(len(self.by),100)
  self.assertGreaterEqual(len(self.store._relations),63)
  self.assertGreaterEqual(sum(r['type']=='source' for r in self.by.values()),22)
  self.assertGreaterEqual(sum(r['type']=='dataset' for r in self.by.values()),1)
  self.assertEqual(sum(r['provenance'].get('edition_added')=='0.2.0' for r in self.by.values()),27)
 def test_source_closure(self):
  for r in self.by.values():
   self.assertEqual(r['revision'],revision(r))
   for link in r['sources']:
    self.assertEqual(self.by[link['record_id']]['revision'],link['revision'])
    self.assertEqual(self.by[link['record_id']]['type'],'source')
  for rel in self.store._relations.values():
   self.assertEqual(rel['revision'],revision(rel))
   for k in ('from','to'):self.assertEqual(rel[k]['revision'],self.by[rel[k]['record_id']]['revision'])
 def test_no_empirical_fabrication(self):
  d=self.by['agent-atlas:mast-data-public-external']
  self.assertIn('NO dataset rows',d['content']['text'])
  for r in self.by.values():
   self.assertFalse(r['provenance']['independent_review'])
   self.assertTrue(r['content']['limitations'])
 def test_advanced_casebook(self):
  self.assertEqual(advanced_casebook()['status'],'passed')
  self.assertEqual(advanced_casebook()['count'],7)
 def test_contexts(self):
  for q in ('outbox uncertain submission idempotency provider','memory conflict source qualifier expiry',
            'MAST missing annotation null prevalence','paired evaluation discordant matched task sign',
            'agent tracing concurrent span root verification'):
   with self.subTest(query=q):
    p=self.store.assemble_context(q,node_ids=['agent-atlas'])
    self.assertTrue(self.store.validate_context(p)['valid'])
    self.assertEqual(p['status'],'context_available')
 def test_reading_paths(self):
  self.assertGreaterEqual(len(list((R/'docs/chapters').glob('*.md'))),22)
  self.assertGreaterEqual(len(list((R/'docs/investigations').glob('*.md'))),12)
  guide=(R/'docs/REFERENCE_GUIDE.md').read_text()
  for p in (R/'docs/chapters').glob('*.md'):self.assertIn(p.name,guide)
  for p in (R/'docs/investigations').glob('*.md'):self.assertIn(p.name,guide)
 def test_common_source_and_node_parity(self):
  root=R.parent/'common/nodes/agent-atlas'
  single=R/'agent_atlas/resources/common/nodes/agent-atlas'
  for path in single.rglob('*'):
   if path.is_file():self.assertEqual(path.read_bytes(),(root/path.relative_to(single)).read_bytes())

if __name__=='__main__':unittest.main()
