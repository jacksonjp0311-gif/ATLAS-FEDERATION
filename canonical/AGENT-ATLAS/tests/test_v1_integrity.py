import unittest,json,hashlib
from pathlib import Path
from atlas_forge.common import AtlasStore, revision
from agent_atlas.v1_cases import casebook_v1
R=Path(__file__).resolve().parents[1]

class ScopedV1Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.s=AtlasStore(R/'agent_atlas/resources/common');cls.records={r['record_id']:r for r in cls.s.export()}
 def test_v1_totals(self):
  self.assertEqual(len(self.records),190)
  self.assertEqual(len([r for r in self.records.values() if r['type']=='source']),34)
  self.assertEqual(len(self.s._relations),122)
  self.assertEqual(sum(r['provenance'].get('edition_added')=='1.0.0' for r in self.records.values()),32)
 def test_prior_record_immutability(self):
  prior=json.loads((R/'evidence/previous_record_revisions_v0.4.0.json').read_text())
  self.assertEqual(len(prior),158)
  for k,v in prior.items():self.assertEqual(self.records[k]['revision'],v,k)
 def test_prior_relation_immutability(self):
  prior=json.loads((R/'evidence/previous_relation_revisions_v0.4.0.json').read_text())
  self.assertEqual(len(prior),101)
  for k,v in prior.items():self.assertEqual(self.s._relations[k]['revision'],v,k)
 def test_source_closure_all(self):
  for r in self.records.values():
   self.assertEqual(r['revision'],revision(r))
   for src in r['sources']:
    self.assertIn(src['record_id'],self.records)
    self.assertEqual(src['revision'],self.records[src['record_id']]['revision'])
    self.assertEqual(self.records[src['record_id']]['type'],'source')
  for e in self.s._relations.values():
   self.assertEqual(e['revision'],revision(e))
   for term in ['from','to']:
    self.assertEqual(e[term]['revision'],self.records[e[term]['record_id']]['revision'])
 def test_source_bodies_not_mirrored(self):
  info=json.loads((R/'evidence/v1_source_scopes.json').read_text())
  self.assertEqual(len(info['new_source_cards']),4)
  self.assertFalse(info['independent_human_review'])
  self.assertEqual(info['real_model_runs'],0)
  for r in self.records.values():
   self.assertFalse(r['provenance'].get('independent_review',False))
   self.assertTrue(r['content']['limitations'])
 def test_content_dimensions(self):
  self.assertEqual(len(list((R/'docs/chapters').glob('*.md'))),50)
  self.assertEqual(len(list((R/'docs/investigations').glob('*.md'))),32)
  self.assertEqual(casebook_v1()['status'],'passed')
 def test_new_reference_context(self):
  for query in ['belief-state Bayes posterior action transition model', 'shortest path heuristic Dijkstra witness',
                'inverse propensity logging weights effective sample size', 'offline knowledge survival source access']:
   with self.subTest(query=query):
    p=self.s.assemble_context(query,node_ids=['agent-atlas'])
    self.assertEqual(p['status'],'context_available')
    self.assertTrue(self.s.validate_context(p)['valid'])
 def test_survivability_charter_exists(self):
  ROOT=R.parent
  self.assertTrue((ROOT/'docs/HUMAN_KNOWLEDGE_SURVIVAL_CHARTER_v1.md').is_file())
  self.assertTrue((ROOT/'docs/OFFLINE_RECONSTRUCTION_RUNBOOK.md').is_file())
 def test_no_executor(self):
  import agent_atlas.foundations_v1 as core
  self.assertFalse(hasattr(core,'run_llm'));self.assertFalse(hasattr(core,'send_tool'))
if __name__=='__main__':unittest.main()
