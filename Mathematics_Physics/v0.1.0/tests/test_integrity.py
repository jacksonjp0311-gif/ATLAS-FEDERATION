"""New twelfth-node exact source closure, preservation and scientific-boundary checks."""
import unittest,sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];COL=ROOT.parent
sys.path.insert(0,str(COL/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision
from math_physics_atlas.cases import casebook

class MathPhysicsIntegrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.local=AtlasStore(ROOT/'math_physics_atlas/resources/common');cls.shared=AtlasStore(COL/'common')
  cls.records={r['record_id']:r for r in cls.local.export()}
 def test_local_inventory(self):
  self.assertEqual(len(self.records),164);self.assertEqual(len(self.local._relations),152)
  self.assertEqual(sum(r['type']=='source' for r in self.records.values()),10)
 def test_full_federation_counts(self):
  x=self.shared.discover();self.assertEqual(len(x['nodes']),12);self.assertEqual(x['records'],2521);self.assertEqual(x['relations'],1679)
 def test_exact_revision_and_sources(self):
  for r in self.records.values():
   self.assertEqual(r['revision'],revision(r));self.assertTrue(r['content']['limitations'])
   for s in r['sources']:
    self.assertIn(s['record_id'],self.records)
    self.assertEqual(self.records[s['record_id']]['revision'],s['revision'])
    self.assertEqual(self.records[s['record_id']]['type'],'source')
 def test_internal_closed_relationships(self):
  for e in self.local._relations.values():
   self.assertEqual(e['revision'],revision(e))
   for k in ('from','to'):self.assertEqual(self.records[e[k]['record_id']]['revision'],e[k]['revision'])
 def test_crosslinks_only_full(self):
  x=[r for r in self.shared._relations.values() if r['relation_id'].startswith('mathematics-physics-atlas:')]
  self.assertEqual(len(x),160);self.assertEqual(len(x)-len(self.local._relations),8)
 def test_chapters_and_casebook(self):
  self.assertEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),38)
  self.assertEqual(casebook()['status'],'passed');self.assertEqual(casebook()['count'],22)
 def test_scoped_sources_not_primary(self):
  for r in self.records.values():
   if r['type']=='source':self.assertFalse(r['provenance']['primary_source_bytes_archived'])
  self.assertEqual(json.loads((ROOT/'evidence/content_inventory.json').read_text())['original_publisher_bytes_authenticated'],0)
 def test_context_assembly(self):
  for q in ('rational Gaussian elimination linear algebra exact certificates','Runge Kutta differential equation numerical stability',
        'Fourier Parseval sampling signal processing','quantum wavefunction Born probability measurement','AI neural matrix gradient calculus optimization'):
   with self.subTest(query=q):
    p=self.local.assemble_context(q,node_ids=['mathematics-physics-atlas'])
    self.assertEqual(p['status'],'context_available');self.assertTrue(self.local.validate_context(p)['valid'])
 def test_no_runtime_side_effects(self):
  text=(ROOT/'math_physics_atlas/models.py').read_text()
  for bad in ('import requests','import socket','import subprocess','os.system(','eval(','exec('):self.assertNotIn(bad,text)
 def test_previous_chemistry_preserved(self):
  p=COL/'history/math_physics_predecessor_chemistry_v1_snapshot'
  self.assertTrue((p/'HISTORICAL_SCOPE_RECEIPT.json').is_file())
  data=json.loads((p/'HISTORICAL_SCOPE_RECEIPT.json').read_text())
  self.assertEqual(data['prior_federation_records'],2357);self.assertFalse(data['historical_tests_modified'])
