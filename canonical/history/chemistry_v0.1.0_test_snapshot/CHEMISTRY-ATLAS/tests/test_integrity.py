"""Chemistry Atlas Common Contract, source-closed retrieval and scientific limits."""
import json,unittest
from pathlib import Path
from chemistry_atlas import __version__
from chemistry_atlas.cases import casebook
from atlas_forge.common import AtlasStore,revision
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent

class ChemistryReferenceIntegrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.store=AtlasStore(ROOT/'chemistry_atlas/resources/common');cls.by={r['record_id']:r for r in cls.store.export()}
 def test_version(self):self.assertEqual(__version__,'0.1.0')
 def test_node_count(self):
  d=self.store.discover();self.assertEqual(len(d['nodes']),1);self.assertEqual(d['records'],168);self.assertEqual(d['relations'],140)
 def test_full_federation(self):
  d=AtlasStore(BASE/'common').discover();self.assertEqual(len(d['nodes']),11);self.assertEqual(d['records'],2220);self.assertEqual(d['relations'],1391)
 def test_source_count(self):self.assertEqual(sum(r['type']=='source' for r in self.by.values()),14)
 def test_exact_revision_and_local_sources(self):
  for r in self.by.values():
   self.assertEqual(r['revision'],revision(r));self.assertTrue(r['content']['limitations'])
   for s in r['sources']:
    self.assertIn(s['record_id'],self.by);self.assertEqual(self.by[s['record_id']]['revision'],s['revision']);self.assertEqual(self.by[s['record_id']]['type'],'source')
 def test_local_relations(self):
  for e in self.store._relations.values():
   self.assertEqual(e['revision'],revision(e))
   for k in ('from','to'):self.assertEqual(self.by[e[k]['record_id']]['revision'],e[k]['revision'])
 def test_only_full_qualified_crosslinks(self):
  full=AtlasStore(BASE/'common')
  edges=[x for x in full._relations.values() if x['relation_id'].startswith('chemistry-atlas:')]
  self.assertEqual(len(edges),146);self.assertEqual(len(edges)-len(self.store._relations),6)
 def test_35_original_chapters(self):
  self.assertEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),35)
  self.assertGreater(len((ROOT/'docs/DEPTH_MANUAL_v0.1.0.md').read_text().split()),15000)
 def test_casebook_25(self):self.assertEqual(casebook()['case_count'],25)
 def test_absent_original_source_files(self):
  for r in self.by.values():
   if r['type']=='source':self.assertFalse(r['provenance']['primary_source_bytes_archived'])
   self.assertFalse(r['provenance']['independent_scientific_review'])
 def test_context_assembly(self):
  for query in ['semiconductor carrier conductivity mobility doping','reaction free Gibbs energy chemical equilibrium activity',
                'kinetics Arrhenius activation energy','silicon oxide dielectric chemical purity','mole Avogadro constant SI',
                'Nernst Faraday electrochemistry battery','chemical data machine learning leakage and validation']:
   with self.subTest(q=query):
    p=self.store.assemble_context(query,node_ids=['chemistry-atlas']);self.assertEqual(p['status'],'context_available');self.assertTrue(self.store.validate_context(p)['valid'])
 def test_no_io_automation(self):
  source=(ROOT/'chemistry_atlas/models.py').read_text()
  for part in ('import socket','import requests','import subprocess','os.system(','eval(', 'exec('):self.assertNotIn(part,source)
