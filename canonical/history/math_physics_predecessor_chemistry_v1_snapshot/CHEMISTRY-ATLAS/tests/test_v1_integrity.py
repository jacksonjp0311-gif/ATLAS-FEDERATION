"""Scoped Chemistry content-v1 acceptance and exact old record revision retention."""
import unittest,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];COLLECTION=ROOT.parent
sys.path.insert(0,str(COLLECTION/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision
from chemistry_atlas.v1_cases import casebook_v1
class ChemistryV1Integrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.local=AtlasStore(ROOT/'chemistry_atlas/resources/common');cls.full=AtlasStore(COLLECTION/'common')
  cls.by={r['record_id']:r for r in cls.local.export()}
 def test_version(self):
  from chemistry_atlas import __version__
  self.assertEqual(__version__,'1.0.0')
 def test_counts(self):
  self.assertEqual(len(self.by),305)
  self.assertEqual(sum(r['type']=='source' for r in self.by.values()),21)
  self.assertEqual(len(self.local._relations),268)
  self.assertEqual(sum(r['provenance'].get('edition_added')=='1.0.0' for r in self.by.values()),68)
 def test_full(self):
  d=self.full.discover();self.assertEqual(len(d['nodes']),11);self.assertEqual(d['records'],2357);self.assertEqual(d['relations'],1519)
 def test_older_record_revisions_exact(self):
  previous=json.loads((ROOT/'evidence/previous_record_revisions_v0.2.0.json').read_text());self.assertEqual(len(previous),237)
  for k,v in previous.items():self.assertEqual(self.by[k]['revision'],v,k)
 def test_older_full_relations_exact(self):
  previous=json.loads((ROOT/'evidence/previous_full_relations_v0.2.0.json').read_text());self.assertEqual(len(previous),210)
  for k,v in previous.items():self.assertEqual(self.full._relations[k]['revision'],v,k)
 def test_strict_source_closure(self):
  for r in self.by.values():
   self.assertEqual(r['revision'],revision(r));self.assertTrue(r['content']['limitations'])
   for x in r['sources']:
    self.assertEqual(self.by[x['record_id']]['revision'],x['revision'])
    self.assertEqual(self.by[x['record_id']]['type'],'source')
 def test_relation_revisions(self):
  for r in self.local._relations.values():
   self.assertEqual(r['revision'],revision(r))
   for k in ('from','to'):self.assertEqual(self.by[r[k]['record_id']]['revision'],r[k]['revision'])
 def test_no_primary_source_authentication(self):
  for r in self.by.values():
   if r['type']=='source':self.assertFalse(r['provenance'].get('primary_source_bytes_archived',False))
  self.assertEqual(json.loads((ROOT/'evidence/v1_scoped_sources.json').read_text())['authentic_primary_bytes_retained'],0)
 def test_manual(self):
  chap=list((ROOT/'docs/chapters').glob('*.md'));self.assertEqual(len(chap),67)
  text=(ROOT/'docs/DEPTH_MANUAL_v1.0.0.md').read_text()
  self.assertGreater(len(text.split()),35000)
  nav=(ROOT/'docs/REFERENCE_GUIDE.md').read_text()
  for x in chap:self.assertIn(x.name,nav)
 def test_cases(self):
  j=casebook_v1();self.assertEqual(j['status'],'passed');self.assertEqual(j['count'],14)
 def test_frozen_snapshot_exists(self):
  p=COLLECTION/'history/chemistry_v0.2.0_test_snapshot/ORIGINAL_SNAPSHOT_RECEIPT.json';self.assertTrue(p.exists())
  x=json.loads(p.read_text());self.assertTrue(x['old_original_tests_unchanged'])
 def test_queries(self):
  for query in ['Shomate heat capacity enthalpy entropy temperature','band gap semiconductor carriers photonic energy',
      'IUPAC formal electrode potential and electrochemical work',
      'Bragg diffraction crystalline spacing',
      'NIST thermochemistry original source rights provenance']:
   with self.subTest(query=query):
    p=self.local.assemble_context(query,node_ids=['chemistry-atlas'])
    self.assertEqual(p['status'],'context_available');self.assertTrue(self.local.validate_context(p)['valid'])
 def test_no_hardware_or_network(self):
  text=(ROOT/'chemistry_atlas/v1_models.py').read_text()
  for string in ('import requests','import serial','import subprocess','import socket','os.system('):self.assertNotIn(string,text)
if __name__=='__main__':unittest.main()
