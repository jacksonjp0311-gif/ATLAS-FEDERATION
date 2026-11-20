"""Exact source closure and historical no-regression checks for Chemistry v0.2."""
from pathlib import Path
import unittest,sys,json
from chemistry_atlas.advanced_cases import advanced_casebook
ROOT=Path(__file__).resolve().parents[1];COLLECTION=ROOT.parent
sys.path.insert(0,str(COLLECTION/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision
class ChemistryV02Integrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.local=AtlasStore(ROOT/'chemistry_atlas/resources/common')
  cls.full=AtlasStore(COLLECTION/'common')
  cls.by={r['record_id']:r for r in cls.local.export()}
 def test_version(self):
  from chemistry_atlas import __version__
  self.assertEqual(__version__,'0.2.0')
 def test_node_inventory(self):
  self.assertEqual(len(self.by),237)
  self.assertEqual(sum(x['type']=='source' for x in self.by.values()),18)
  self.assertEqual(len(self.local._relations),204)
 def test_federation(self):
  d=self.full.discover();self.assertEqual(len(d['nodes']),11)
  self.assertEqual(d['records'],2289);self.assertEqual(d['relations'],1455)
 def test_original_record_revisions(self):
  old=json.loads((ROOT/'evidence/prior_record_revisions_v0.1.0.json').read_text());self.assertEqual(len(old),168)
  for k,rev in old.items():self.assertEqual(self.by[k]['revision'],rev,k)
 def test_old_relation_revisions(self):
  old=json.loads((ROOT/'evidence/prior_relations_v0.1.0.json').read_text());self.assertEqual(len(old),146)
  for k,rev in old.items():self.assertEqual(self.full._relations[k]['revision'],rev,k)
 def test_source_and_revision_closure(self):
  for rec in self.by.values():
   self.assertEqual(rec['revision'],revision(rec))
   self.assertTrue(rec['content']['limitations'])
   self.assertFalse(rec['provenance'].get('independent_scientific_review',False))
   for ref in rec['sources']:
    self.assertEqual(self.by[ref['record_id']]['revision'],ref['revision'])
    self.assertEqual(self.by[ref['record_id']]['type'],'source')
 def test_standalone_relation_closure(self):
  for rel in self.local._relations.values():
   self.assertEqual(rel['revision'],revision(rel))
   for end in ('from','to'):
    self.assertIn(rel[end]['record_id'],self.by)
    self.assertEqual(rel[end]['revision'],self.by[rel[end]['record_id']]['revision'])
 def test_six_cross_domain_links(self):
  rel=[r for r in self.full._relations.values() if r['relation_id'].startswith('chemistry-atlas:')]
  self.assertEqual(len(rel),210)
  self.assertEqual(len(rel)-len(self.local._relations),6)
 def test_51_chapters_and_manual(self):
  ch=list((ROOT/'docs/chapters').glob('*.md'))
  self.assertEqual(len(ch),51)
  self.assertGreater(len((ROOT/'docs/DEPTH_MANUAL_v0.2.0.md').read_text().split()),26000)
  guide=(ROOT/'docs/REFERENCE_GUIDE.md').read_text()
  for f in ch:self.assertIn(f.name,guide)
 def test_four_additional_sources(self):
  src=json.loads((ROOT/'evidence/source_scope_v02.json').read_text())
  self.assertEqual(len(src['sources']),4)
  self.assertEqual(src['actual_dataset_rows_acquired'],0)
  for s in src['sources']:self.assertFalse(s['authentic_original_bytes_archived'])
 def test_all_source_cards_link_only(self):
  for r in self.by.values():
   if r['type']=='source':self.assertFalse(r['provenance']['primary_source_bytes_archived'])
 def test_casebook(self):
  r=advanced_casebook();self.assertEqual(r['count'],14);self.assertEqual(r['status'],'passed')
 def test_scoped_contexts(self):
  queries=['ionic chemical charge conservation and exact rational balance',
   'chemical activity ionic strength Debye Huckel dilute solution',
   'standard Gibbs reaction enthalpy and vanthoff equilibrium',
   'semiconductor electron hole neutrality intrinsic carriers',
   'Fick diffusion finite volume stable time step',
   'machine learning chemistry dataset provenance leakage',
   'authenticated original publisher source bytes and rights']
  for q in queries:
   with self.subTest(q=q):
    p=self.local.assemble_context(q,node_ids=['chemistry-atlas'])
    self.assertEqual(p['status'],'context_available')
    self.assertTrue(self.local.validate_context(p)['valid'])
 def test_no_actual_external_side_effects(self):
  p=(ROOT/'chemistry_atlas/advanced.py').read_text()
  for token in ('import requests','import subprocess','import socket','os.system(', 'eval(', 'exec('):self.assertNotIn(token,p)
 def test_legacy_tests_retained(self):
  self.assertTrue((ROOT/'legacy_tests_v0.1.0/test_models.py').is_file())
  self.assertTrue((ROOT/'legacy_tests_v0.1.0/test_integrity.py').is_file())
  snap=COLLECTION/'history/chemistry_v0.1.0_test_snapshot/CHEMISTRY-ATLAS/tests/test_integrity.py'
  self.assertEqual((ROOT/'legacy_tests_v0.1.0/test_integrity.py').read_bytes(),snap.read_bytes())
if __name__=='__main__':unittest.main()
