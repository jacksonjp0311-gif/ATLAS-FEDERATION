"""Versioned evidence and common-context contract tests. Not science certification."""
import json,hashlib,unittest,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
ROOT=R/'control_atlas/resources/common';NODE=ROOT/'nodes/control-atlas'
B=R.parent/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'
sys.path.insert(0,str(B))
from atlas_forge.common import AtlasStore,revision,sha,canonical

class TestControlRecords(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.store=AtlasStore(ROOT);cls.records={r['record_id']:r for r in cls.store.export()}
 def test_node_records(self):
  self.assertGreaterEqual(len(self.records),117)
  self.assertGreaterEqual(sum(r['type']=='source' for r in self.records.values()),27)
  self.assertGreaterEqual(self.store.discover()['records'],117)
 def test_all_revisions_and_links(self):
  for r in self.records.values():
   self.assertEqual(r['revision'],revision(r))
   self.assertEqual(r['node_id'],'control-atlas')
   for s in r['sources']:
    self.assertEqual(self.records[s['record_id']]['revision'],s['revision'])
    self.assertEqual(self.records[s['record_id']]['type'],'source')
 def test_relations(self):
  edges=self.store._relations
  self.assertGreaterEqual(len(edges),64)
  for r in edges.values():
   self.assertEqual(r['revision'],revision(r))
   for k in ('from','to'):
    self.assertEqual(r[k]['revision'],self.records[r[k]['record_id']]['revision'])
 def test_limited_evidence(self):
  for r in self.records.values():
   self.assertFalse(r['provenance']['independent_review'])
   self.assertTrue(r['content']['limitations'])
   self.assertNotIn(r['evidence']['review_status'],('human_reviewed','independently_reproduced'))
 def test_source_cards(self):
  for r in self.records.values():
   if r['type']=='source':
    self.assertTrue(r['provenance']['url'].startswith('https://'))
    self.assertFalse(r['provenance']['source_bytes_archived'])
 def test_source_closure_in_context(self):
  for q in ('scalar discrete stability unit circle','Riccati finite LQR quadratic',
            'saturated integral antiwindup','Kalman covariance sensor noise',
            'sampling aliasing Nyquist delay','controllability observability'):
   with self.subTest(q=q):
    p=self.store.assemble_context(q,node_ids=['control-atlas'])
    self.assertTrue(self.store.validate_context(p)['valid'])
    self.assertEqual(p['status'],'context_available')
 def test_tight_budget_graceful(self):
  p=self.store.assemble_context('anti-windup integrator',node_ids=['control-atlas'],max_context_bytes=512)
  self.assertTrue(self.store.validate_context(p)['valid'])
 def test_module_does_not_require_hardware(self):
  from control_atlas import models
  self.assertFalse(hasattr(models,'connect_hardware'))
 def test_docs_cover_chapters_and_cases(self):
  self.assertGreaterEqual(len(list((R/'docs/chapters').glob('*.md'))),26)
  self.assertGreaterEqual(len(list((R/'docs/investigations').glob('*.md'))),18)
  guide=(R/'docs/REFERENCE_GUIDE.md').read_text()
  for p in (R/'docs/chapters').glob('*.md'):self.assertIn(p.name,guide)
  for p in (R/'docs/investigations').glob('*.md'):self.assertIn(p.name,guide)
 def test_no_false_control_deployment(self):
  readme=(R/'README.md').read_text().lower()
  self.assertIn('no',readme)
  self.assertIn('bitwork',readme)

if __name__=='__main__':unittest.main()
