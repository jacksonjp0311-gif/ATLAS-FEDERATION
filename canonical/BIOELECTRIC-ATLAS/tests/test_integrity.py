"""Standalone v0.1 exact local Bioelectric node schema and rights honesty."""
import unittest,json,hashlib
from importlib.resources import files

N='bioelectric-atlas'
ROOT=files('bioelectric_atlas').joinpath('resources/common')
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()

class TestIntegrity(unittest.TestCase):
 def test_standalone_registry_lock(self):
  raw=ROOT.joinpath('registry.json').read_bytes()
  self.assertEqual(sha(raw),json.loads(ROOT.joinpath('registry.lock.json').read_text())['sha256'])
 def test_exact_one_node(self):
  nodes=json.loads(ROOT.joinpath('registry.json').read_text())['nodes']
  self.assertEqual(len(nodes),1);self.assertEqual(nodes[0]['node_id'],N)
 def test_manifest_subcollections(self):
  meta=json.loads(ROOT.joinpath('nodes',N,'atlas_manifest.json').read_text())
  self.assertEqual(meta['software_version'],'0.1.0')
  counts={'concept':18,'claim':18,'equation':18,'method':18,'source':7,'relations':72,'dataset':0,'review':0}
  for k,v in counts.items():
   d=meta['collections'][k]
   b=ROOT.joinpath('nodes',N,d['path']).read_bytes()
   self.assertEqual((d['records'],d['sha256']),(v,sha(b)))
 def test_original_record_hashes(self):
  data=ROOT.joinpath('nodes',N,'data')
  for name in ['concepts','claims','equations','methods','sources','relations']:
   for l in data.joinpath(name+'.jsonl').read_bytes().splitlines():
    a=json.loads(l);self.assertEqual(a['revision'],sha(canonical({k:v for k,v in a.items() if k!='revision'})))
 def test_all_local_relations_exact(self):
  data=ROOT.joinpath('nodes',N,'data')
  idx={(a['record_id'],a['revision']) for name in ['concepts','claims','equations','methods','sources'] for l in data.joinpath(name+'.jsonl').read_bytes().splitlines() for a in [json.loads(l)]}
  self.assertEqual(len(idx),79)
  for l in data.joinpath('relations.jsonl').read_bytes().splitlines():
   a=json.loads(l)
   for k in ['from','to']:self.assertIn((a[k]['record_id'],a[k]['revision']),idx)
 def test_original_source_not_authenticated(self):
  p=ROOT.joinpath('nodes',N,'data/sources.jsonl')
  for l in p.read_bytes().splitlines():
   x=json.loads(l);self.assertFalse(x['provenance']['original_full_source_authenticated'])
 def test_nonclinical_scope_present(self):
  p=ROOT.joinpath('nodes',N,'atlas_manifest.json')
  j=json.loads(p.read_text());self.assertIn('No body experimentation',j['scope'])
if __name__=='__main__':unittest.main()
