"""Additive v1 candidate record/federation invariants, preserving v0.5 tests unchanged."""
import hashlib,json,unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];COL=ROOT.parent
sys.path.insert(0,str(COL/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision
from math_physics_atlas.v1_cases import casebook_v1
class V1Integrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.local=AtlasStore(ROOT/'math_physics_atlas/resources/common')
  cls.full=AtlasStore(COL/'common')
  cls.records={r['record_id']:r for r in cls.local.export()}
 def test_federation_inventory(self):
  a=self.full.discover();self.assertEqual((len(a['nodes']),a['records'],a['relations']),(12,2625,1774))
  b=self.local.discover();self.assertEqual((len(b['nodes']),b['records'],b['relations']),(1,268,247))
 def test_prior_exact_jsonl_prefix(self):
  prev=COL/'history/math_physics_v0.5.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS/data'
  for cat in ('concepts','claims','equations','methods','datasets','reviews','sources','relations'):
   with self.subTest(category=cat):
    self.assertTrue((ROOT/'data'/f'{cat}.jsonl').read_bytes().startswith((prev/f'{cat}.jsonl').read_bytes()))
 def test_previous_federation_relations_retained(self):
  old=(COL/'history/math_physics_v0.5.0_test_snapshot/common/nodes/mathematics-physics-atlas/data/relations.jsonl').read_bytes()
  new=(COL/'common/nodes/mathematics-physics-atlas/data/relations.jsonl').read_bytes()
  self.assertTrue(new.startswith(old));self.assertEqual(len(new.splitlines())-len(old.splitlines()),24)
 def test_prior_tests_byte_identical(self):
  prev=COL/'history/math_physics_v0.5.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS'
  filehash=json.loads((prev/'FILE_MANIFEST.json').read_text())['files']
  for rel in ('tests/test_v05_models.py','tests/test_v05_integrity.py'):
   self.assertEqual(hashlib.sha256((prev/rel).read_bytes()).hexdigest(),filehash[rel])
 def test_revisions_exact(self):
  for r in self.records.values():
   self.assertEqual(r['revision'],revision(r))
   for s in r['sources']:
    self.assertEqual(self.records[s['record_id']]['revision'],s['revision'])
  for rel in self.local._relations.values():
   self.assertEqual(rel['revision'],revision(rel))
   for k in ('from','to'):
    self.assertEqual(rel[k]['revision'],self.records[rel[k]['record_id']]['revision'])
 def test_new_closure(self):
  for q in ('Poisson electron hole charge continuity', 'Gummel bounded steady solver',
            'Scharfetter Gummel M matrix positive flux','BIPM SI thermal voltage metrology',
            'manufactured equilibria independent dense root'):
   p=self.local.assemble_context(q,node_ids=['mathematics-physics-atlas'])
   self.assertTrue(self.local.validate_context(p)['valid'])
   self.assertNotIn(p['status'],('no_match','evidence_unavailable'))
 def test_scope_and_cases(self):
  self.assertEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),62)
  self.assertEqual(len(json.loads((ROOT/'evidence/chapter_index.json').read_text())),62)
  self.assertEqual(casebook_v1()['count'],11);self.assertEqual(casebook_v1()['status'],'passed')
 def test_no_unearned_evidence(self):
  self.assertEqual(sum(r['type']=='source' for r in self.records.values()),18)
  self.assertFalse(any(r['provenance'].get('primary_source_bytes_archived',False) for r in self.records.values()))
  self.assertFalse(any(r['evidence']['review_status']=='independently_reproduced' for r in self.records.values()))
  self.assertFalse(json.loads((COL/'BUILD_POLICY.json').read_text())['Bitwork_router_changes'])
if __name__=='__main__':unittest.main()
