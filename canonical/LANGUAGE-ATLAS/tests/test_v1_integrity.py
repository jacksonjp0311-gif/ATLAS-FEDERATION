"""v1 scope acceptance and preservation of prior version hashes."""
import unittest,json,sys,unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision
from language_atlas.v1_cases import casebook_v1

class LanguageV1Integrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.local=AtlasStore(ROOT/'language_atlas/resources/common');cls.full=AtlasStore(ROOT.parent/'common')
  cls.by={r['record_id']:r for r in cls.local.export()}
 def test_inventory(self):
  self.assertEqual(len(self.by),276);self.assertEqual(sum(r['type']=='source' for r in self.by.values()),39)
  self.assertEqual(len(self.local._relations),272);self.assertEqual(self.full.discover()['records'],1751)
  self.assertEqual(self.full.discover()['relations'],984);self.assertEqual(len(self.full.discover()['nodes']),9)
 def test_older_revisions_preserved(self):
  olds=json.loads((ROOT/'evidence/previous_record_revisions_v0.2.0.json').read_text())
  self.assertEqual(len(olds),224)
  for k,v in olds.items():self.assertEqual(self.by[k]['revision'],v,k)
  re=json.loads((ROOT/'evidence/previous_relation_revisions_v0.2.0.json').read_text())
  self.assertEqual(len(re),227)
  for k,v in re.items():self.assertEqual(self.full._relations[k]['revision'],v,k)
 def test_source_closure(self):
  for r in self.by.values():
   self.assertEqual(r['revision'],revision(r))
   self.assertTrue(r['content']['limitations'])
   self.assertFalse(r['provenance'].get('independent_scientific_review',False))
   for s in r['sources']:
    self.assertEqual(self.by[s['record_id']]['revision'],s['revision']);self.assertEqual(self.by[s['record_id']]['type'],'source')
 def test_edges(self):
  for r in self.local._relations.values():
   self.assertEqual(r['revision'],revision(r))
   for side in ('from','to'):self.assertEqual(self.by[r[side]['record_id']]['revision'],r[side]['revision'])
 def test_39_sources_absent(self):
  for r in self.by.values():
   if r['type']=='source':self.assertFalse(r['provenance'].get('original_source_bytes_archived',False))
 def test_contexts(self):
  for query in ('quantifier scope Strong Kleene unknown','weighted segment alignment phonetic similarity',
   'Unicode 18 normalization grapheme revised','CARE community authority control language documentation','finite-state acceptor epsilon grammar'):
   with self.subTest(query=query):
    p=self.local.assemble_context(query,node_ids=['language-atlas'])
    self.assertTrue(self.local.validate_context(p)['valid'])
    self.assertEqual(p['status'],'context_available')
 def test_manual(self):
  ch=list((ROOT/'docs/chapters').glob('*.md'));inv=list((ROOT/'docs/investigations').glob('*.md'))
  self.assertEqual(len(ch),65);self.assertEqual(len(inv),40)
  guide=(ROOT/'docs/REFERENCE_GUIDE.md').read_text()
  for f in ch+inv:self.assertIn(f.name,guide)
  self.assertGreater(len((ROOT/'docs/DEPTH_MANUAL_v1.0.0.md').read_text().split()),35000)
 def test_casebook(self):
  r=casebook_v1();self.assertEqual(r['count'],11);self.assertEqual(r['status'],'passed')
  self.assertFalse(r['community_permissions_authenticated'])
 def test_unicode_version_honesty(self):
  data=json.loads((ROOT/'evidence/v1_unicode_runtime.json').read_text())
  self.assertEqual(data['python_unicodedata_version'],unicodedata.unidata_version)
  self.assertFalse(data['full_uax29_conformance_proven'])
  self.assertFalse(data['unicode18_normative_test_file_acquired'])
 def test_full_local_projection(self):
  full={r['record_id']:r for r in self.full.export() if r['node_id']=='language-atlas'}
  self.assertEqual({k:v['revision'] for k,v in full.items()},{k:v['revision'] for k,v in self.by.items()})
  self.assertEqual(len([r for r in self.full._relations.values() if r['relation_id'].startswith('language-atlas:')]),277)
 def test_no_live_tool_calls(self):
  code=(ROOT/'language_atlas/v1_models.py').read_text()
  for forbidden in ('import requests','import subprocess','import socket','os.system','eval(', 'exec('):self.assertNotIn(forbidden,code)
 def test_rights_and_survival(self):
  self.assertTrue((ROOT.parent/'docs/HUMAN_KNOWLEDGE_SURVIVAL_CHARTER_v1.md').is_file())
  s=json.loads((ROOT/'evidence/v1_source_scopes.json').read_text())
  self.assertEqual(s['raw_original_bytes_acquired'],0)
  self.assertEqual(s['community_permissions_verified'],0)

if __name__=='__main__':unittest.main()
