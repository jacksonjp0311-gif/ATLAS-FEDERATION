"""Current Energy v0.2 content and exact prior immutable revisions."""
import unittest,json,sys,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];COLLECTION=ROOT.parent
sys.path.insert(0,str(COLLECTION/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision
from energy_atlas.survival_cases import casebook_survival
class EnergyV02Reference(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.store=AtlasStore(ROOT/'energy_atlas/resources/common');cls.by={r['record_id']:r for r in cls.store.export()}
 def test_full_node_counts(self):
  self.assertEqual(len(self.by),241)
  self.assertEqual(sum(r['type']=='source' for r in self.by.values()),28)
  self.assertEqual(len(self.store._relations),200)
 def test_full_federation(self):
  d=AtlasStore(COLLECTION/'common').discover()
  self.assertEqual(d['records'],1992);self.assertEqual(d['relations'],1189);self.assertEqual(len(d['nodes']),10)
 def test_unchanged_prior_records(self):
  data=json.loads((ROOT/'evidence/previous_record_revisions_v0.1.0.json').read_text())
  self.assertEqual(len(data),176)
  for key,old in data.items():self.assertEqual(self.by[key]['revision'],old,key)
 def test_unchanged_prior_relations(self):
  data=json.loads((ROOT/'evidence/previous_relation_revisions_v0.1.0.json').read_text())
  self.assertEqual(len(data),149)
  s=AtlasStore(COLLECTION/'common')
  for key,old in data.items():self.assertEqual(s._relations[key]['revision'],old,key)
 def test_source_revision_closure(self):
  for r in self.by.values():
   self.assertEqual(r['revision'],revision(r))
   for src in r['sources']:
    self.assertIn(src['record_id'],self.by)
    self.assertEqual(self.by[src['record_id']]['revision'],src['revision'])
    self.assertEqual(self.by[src['record_id']]['type'],'source')
  for r in self.store._relations.values():
   self.assertEqual(r['revision'],revision(r))
   for k in ('from','to'):self.assertEqual(self.by[r[k]['record_id']]['revision'],r[k]['revision'])
 def test_full_cross_node_edges(self):
  d=AtlasStore(COLLECTION/'common')
  edges=[x for x in d._relations.values() if x['relation_id'].startswith('energy-atlas:')]
  self.assertEqual(len(edges),205)
  self.assertEqual(sum(not x['to']['record_id'].startswith('energy-atlas:') for x in edges),5)
 def test_no_empirical_inflation(self):
  source=json.loads((ROOT/'evidence/survival_source_register_v0.2.0.json').read_text())
  self.assertEqual(len(source['sources']),8)
  self.assertEqual(source['source_bytes_verified'],0)
  for x in self.by.values():
   self.assertFalse(x['provenance'].get('independent_review',False))
   self.assertTrue(x['content']['limitations'])
   if x['type']=='source':self.assertFalse(x['provenance']['primary_source_bytes_archived'])
 def test_manual_depth_and_index(self):
  chap=list((ROOT/'docs/chapters').glob('*.md'))
  self.assertEqual(len(chap),50)
  index=(ROOT/'docs/REFERENCE_GUIDE.md').read_text()
  for p in chap:self.assertIn(p.name,index)
  manual=(ROOT/'docs/DEPTH_MANUAL_v0.2.0.md').read_text()
  self.assertGreater(len(manual.split()),19000)
 def test_casebook(self):self.assertEqual(casebook_survival()['status'],'passed');self.assertEqual(casebook_survival()['count'],11)
 def test_version(self):
  from energy_atlas import __version__
  self.assertEqual(__version__,'0.2.0')
 def test_contexts(self):
  for query in ['battery reserve energy and multiple cloudy days','water lifting total dynamic pump head and efficiency',
               'microgrid multi interval unserved load thermal energy ledger','portable generator carbon monoxide combustion safety',
               'heating water versus potable drinking water sanitation']:
   p=self.store.assemble_context(query,node_ids=['energy-atlas'])
   self.assertEqual(p['status'],'context_available')
   self.assertTrue(self.store.validate_context(p)['valid'])
 def test_readonly_no_equipment_control(self):
  text=(ROOT/'energy_atlas/survival_models.py').read_text()
  for token in ('import requests','import socket','import subprocess','import serial'):
   self.assertNotIn(token,text)
if __name__=='__main__':unittest.main()
