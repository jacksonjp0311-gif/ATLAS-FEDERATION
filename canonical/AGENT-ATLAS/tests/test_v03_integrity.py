import unittest,json
from pathlib import Path
from agent_atlas.v03_cases import casebook_v03
from agent_atlas.models import AgentModelError
from atlas_forge.common import AtlasStore,revision
ROOT=Path(__file__).resolve().parents[1]

class V03Integrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.store=AtlasStore(ROOT/'agent_atlas/resources/common')
  cls.records={r['record_id']:r for r in cls.store.export()}
 def test_new_record_inventory(self):
  self.assertGreaterEqual(len(self.records),128)
  self.assertGreaterEqual(sum(x['type']=='source' for x in self.records.values()),27)
  self.assertGreaterEqual(len(self.store._relations),83)
  self.assertEqual(sum(x['provenance'].get('edition_added')=='0.3.0' for x in self.records.values()),28)
 def test_old_versions_retained(self):
  records=json.loads((ROOT/'evidence/previous_record_revisions_v0.2.0.json').read_text())
  relations=json.loads((ROOT/'evidence/previous_relation_revisions_v0.2.0.json').read_text())
  self.assertEqual(len(records),100);self.assertEqual(len(relations),63)
  for key,v in records.items():self.assertEqual(self.records[key]['revision'],v)
  for key,v in relations.items():self.assertEqual(self.store._relations[key]['revision'],v)
 def test_source_closure_and_revision(self):
  for r in self.records.values():
   self.assertEqual(r['revision'],revision(r))
   self.assertTrue(r['content']['limitations'])
   self.assertFalse(r['provenance']['independent_review'])
   for s in r['sources']:
    self.assertEqual(self.records[s['record_id']]['revision'],s['revision'])
    self.assertEqual(self.records[s['record_id']]['type'],'source')
  for r in self.store._relations.values():
   self.assertEqual(r['revision'],revision(r))
   for part in ('from','to'):
    self.assertEqual(self.records[r[part]['record_id']]['revision'],r[part]['revision'])
 def test_new_source_cards_and_no_mast_rows(self):
  for suffix in ('OTEL-AGENT-2026','OTEL-TOOL-2026','OTEL-PRIVACY-2026','AWS-IDEMPOTENCY','AWS-WA-IDEMPOTENCY'):
   self.assertIn('agent-atlas:source:'+suffix,self.records)
  v=json.loads((ROOT/'evidence/source_scope_v0.3.0.json').read_text())
  self.assertEqual(len(v['sources']),5)
  self.assertEqual(v['MAST_full_rows_read'],0)
  self.assertFalse(v['independent_human_review'])
 def test_context_scientific_limits(self):
  for query in ['otel tool span privacy execution','idempotency unknown external effects operator stop',
                'MAST missing judge labels grouped framework','repeated trial pass all reliability']:
   p=self.store.assemble_context(query,node_ids=['agent-atlas'])
   self.assertTrue(self.store.validate_context(p)['valid'])
   self.assertEqual(p['status'],'context_available')
 def test_casebook_and_reading_path(self):
  self.assertEqual(casebook_v03()['status'],'passed')
  self.assertEqual(casebook_v03()['count'],8)
  self.assertGreaterEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),30)
  self.assertGreaterEqual(len(list((ROOT/'docs/investigations').glob('*.md'))),18)
  guide=(ROOT/'docs/REFERENCE_GUIDE.md').read_text()
  for p in list((ROOT/'docs/chapters').glob('*.md'))+list((ROOT/'docs/investigations').glob('*.md')):
   self.assertIn(p.name,guide)
 def test_single_node_parity(self):
  a=ROOT/'agent_atlas/resources/common/nodes/agent-atlas';b=ROOT.parent/'common/nodes/agent-atlas'
  for p in a.rglob('*'):
   if p.is_file():self.assertEqual(p.read_bytes(),(b/p.relative_to(a)).read_bytes())

if __name__=='__main__':unittest.main()
