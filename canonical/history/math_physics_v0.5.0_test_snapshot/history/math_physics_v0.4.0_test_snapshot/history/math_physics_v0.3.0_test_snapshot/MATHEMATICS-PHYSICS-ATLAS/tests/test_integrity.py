"""Current v0.3 integrity; exact v0.2 and v0.1 tests are frozen in history."""
import json,unittest,sys,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];COL=ROOT.parent
sys.path.insert(0,str(COL/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision
from math_physics_atlas.cases import casebook
from math_physics_atlas.v02_cases import casebook_v02
from math_physics_atlas.v03_cases import casebook_v03
class MathPhysicsV02Integrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.local=AtlasStore(ROOT/'math_physics_atlas/resources/common');cls.full=AtlasStore(COL/'common')
  cls.records={x['record_id']:x for x in cls.local.export()}
 def test_inventory(self):
  self.assertEqual(len(self.records),207);self.assertEqual(len(self.local._relations),192)
  d=self.full.discover();self.assertEqual((len(d['nodes']),d['records'],d['relations']),(12,2564,1719))
 def test_chapters_cases(self):
  self.assertEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),48)
  self.assertEqual(casebook()['count'],22);self.assertEqual(casebook_v02()['count'],6);self.assertEqual(casebook_v03()['count'],4)
 def test_record_revisions(self):
  for x in self.records.values():
   self.assertEqual(x['revision'],revision(x))
   for s in x['sources']:
    self.assertEqual(self.records[s['record_id']]['revision'],s['revision'])
 def test_relation_revisions(self):
  for rel in self.local._relations.values():
   self.assertEqual(rel['revision'],revision(rel))
   for key in ('from','to'):
    self.assertEqual(self.records[rel[key]['record_id']]['revision'],rel[key]['revision'])
 def test_historical_exact_bytes(self):
  original=COL/'history/math_physics_v0.1.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS/data'
  for cat in ('concepts','claims','equations','methods','sources','relations','reviews','datasets'):
   old=(original/f'{cat}.jsonl').read_bytes();now=(ROOT/'data'/f'{cat}.jsonl').read_bytes()
   self.assertTrue(now.startswith(old),cat)
 def test_context_closure(self):
  for q in ('Householder QR stable least squares rank','radix two FFT aliasing spectral sampling',
            'nonlinear RK4 local error step doubling','heat equation thermal Fourier number stability',
            'wave equation leapfrog CFL physics'):
   p=self.local.assemble_context(q,node_ids=['mathematics-physics-atlas']);self.assertTrue(self.local.validate_context(p)['valid'])
 def test_not_scientific_review(self):
  self.assertEqual(sum(x['type']=='source' for x in self.records.values()),13)
  for x in self.records.values():
   if x['type']=='source':self.assertFalse(x['provenance']['primary_source_bytes_archived'])
 def test_no_runtime_network(self):
  p=(ROOT/'math_physics_atlas/v02_models.py').read_text()
  for bad in ('import requests','import socket','import subprocess','os.system(','eval(','exec('):self.assertNotIn(bad,p)
