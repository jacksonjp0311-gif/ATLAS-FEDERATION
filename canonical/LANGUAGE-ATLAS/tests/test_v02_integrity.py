"""Verify all earlier exact revisions, current docs, source closure and evidence limits."""
import json,unittest
from pathlib import Path
from language_atlas.advanced_cases import advanced_casebook
ROOT=Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0,str(ROOT.parent/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision

class V02Integrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.local=AtlasStore(ROOT/'language_atlas/resources/common')
  cls.full=AtlasStore(ROOT.parent/'common')
  cls.by={r['record_id']:r for r in cls.local.export()}
 def test_records(self):
  self.assertEqual(len(self.by),224)
  self.assertEqual(len(self.local._relations),222)
  self.assertEqual(sum(x['type']=='source' for x in self.by.values()),33)
  self.assertEqual(sum(x['provenance'].get('edition_added')=='0.2.0' for x in self.by.values()),57)
 def test_older_record_revisions(self):
  d=json.loads((ROOT/'evidence/previous_record_revisions_v0.1.0.json').read_text());self.assertEqual(len(d),167)
  for k,v in d.items():self.assertEqual(self.by[k]['revision'],v,k)
 def test_older_relation_revisions(self):
  d=json.loads((ROOT/'evidence/previous_relation_revisions_v0.1.0.json').read_text());self.assertEqual(len(d),167)
  for k,v in d.items():self.assertEqual(self.full._relations[k]['revision'],v,k)
 def test_source_closure(self):
  for r in self.by.values():
   self.assertEqual(r['revision'],revision(r))
   for x in r['sources']:
    self.assertEqual(self.by[x['record_id']]['revision'],x['revision']);self.assertEqual(self.by[x['record_id']]['type'],'source')
  for rel in self.local._relations.values():
   self.assertEqual(rel['revision'],revision(rel))
   for term in ('from','to'):self.assertEqual(rel[term]['revision'],self.by[rel[term]['record_id']]['revision'])
 def test_full_federation(self):
  d=self.full.discover();self.assertEqual(d['records'],1699);self.assertEqual(d['relations'],934)
  self.assertEqual(len(d['nodes']),9)
  self.assertEqual(len([r for r in self.full._relations.values() if r['relation_id'].startswith('language-atlas:')]),227)
 def test_standalone_node_copy(self):
  a=ROOT/'language_atlas/resources/common/nodes/language-atlas'
  b=ROOT.parent/'common/nodes/language-atlas'
  for f in a.rglob('*'):
   if f.is_file() and f.name!='relations.jsonl':
    # Manifests differ intentionally (standalone has no cross-node edges).
    if f.name=='atlas_manifest.json':continue
    self.assertEqual(f.read_bytes(),(b/f.relative_to(a)).read_bytes())
 def test_contexts(self):
  for query in ['corpus BLEU tokenization semantic meaning','PCFG inside Viterbi derivation probability',
                'WALS family sampling genealogical areal','community speaker permission public archive',
                'signed language tier overlap simultaneity','Unicode UAX29 revision 49 grapheme']:
   with self.subTest(query=query):
    p=self.local.assemble_context(query,node_ids=['language-atlas'])
    self.assertTrue(self.local.validate_context(p)['valid'])
    self.assertEqual(p['status'],'context_available')
 def test_manual(self):
  self.assertEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),50)
  self.assertEqual(len(list((ROOT/'docs/investigations').glob('*.md'))),30)
  g=(ROOT/'docs/REFERENCE_GUIDE.md').read_text()
  for f in list((ROOT/'docs/chapters').glob('*.md'))+list((ROOT/'docs/investigations').glob('*.md')):self.assertIn(f.name,g)
  self.assertGreater(len((ROOT/'docs/DEPTH_MANUAL_v0.2.0.md').read_text().split()),30000)
 def test_no_real_corpus(self):
  scope=json.loads((ROOT/'evidence/source_scope_v0.2.0.json').read_text())
  self.assertEqual(len(scope['new_sources']),8)
  self.assertEqual(scope['authentic_corpus_samples_loaded'],0)
  self.assertEqual(scope['community_recordings_or_sign_video_acquired'],0)
  self.assertEqual(scope['human_reviewers'],0)
  for r in self.by.values():
   self.assertFalse(r['provenance'].get('independent_scientific_review',False))
   self.assertTrue(r['content']['limitations'])
 def test_casebook(self):
  self.assertEqual(advanced_casebook()['status'],'passed')
  self.assertEqual(advanced_casebook()['count'],11)
 def test_no_external_command(self):
  txt=(ROOT/'language_atlas/advanced.py').read_text()
  for op in ('import requests','import socket','import subprocess','os.system(', 'eval(', 'exec('):self.assertNotIn(op,txt)

if __name__=='__main__':unittest.main()
