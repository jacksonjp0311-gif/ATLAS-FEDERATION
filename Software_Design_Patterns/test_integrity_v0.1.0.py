"""Offline standalone patterns node exact-revision graph checks."""
import unittest,json,hashlib
from importlib.resources import files
ROOT=files('patterns_atlas').joinpath('resources/common')
NODE='software-design-patterns-atlas'
def digest(data):return hashlib.sha256(data).hexdigest()
def canonical(data):return json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()

class TestNodeIntegrity(unittest.TestCase):
    def test_local_registry_lock(self):
        raw=ROOT.joinpath('registry.json').read_bytes()
        self.assertEqual(json.loads(ROOT.joinpath('registry.lock.json').read_text())['sha256'],digest(raw))
        self.assertEqual(len(json.loads(raw)['nodes']),1)
    def test_manifest_and_collections(self):
        m=json.loads(ROOT.joinpath('nodes',NODE,'atlas_manifest.json').read_text())
        self.assertEqual(m['software_version'],'0.1.0')
        self.assertEqual(m['node_id'],NODE)
        for kind,c in m['collections'].items():
            raw=ROOT.joinpath('nodes',NODE,c['path']).read_bytes()
            self.assertEqual(c['sha256'],digest(raw),kind)
            self.assertEqual(c['records'],len(raw.splitlines()),kind)
    def test_all_record_revisions(self):
        for p in ('concepts','claims','equations','methods','sources'):
            for line in ROOT.joinpath('nodes',NODE,'data/'+p+'.jsonl').read_bytes().splitlines():
                j=json.loads(line)
                self.assertEqual(j['revision'],digest(canonical({k:v for k,v in j.items() if k!='revision'})))
    def test_local_exact_revision_endpoints(self):
        rows=[json.loads(line) for p in ('concepts','claims','equations','methods','sources')
              for line in ROOT.joinpath('nodes',NODE,'data/'+p+'.jsonl').read_bytes().splitlines()]
        ids={(j['record_id'],j['revision']) for j in rows}
        self.assertEqual(len(ids),105)
        rel=[json.loads(line) for line in ROOT.joinpath('nodes',NODE,'data/relations.jsonl').read_bytes().splitlines()]
        self.assertEqual(len(rel),96)
        for r in rel:
            self.assertIn((r['from']['record_id'],r['from']['revision']),ids)
            self.assertIn((r['to']['record_id'],r['to']['revision']),ids)
    def test_publisher_sources_are_only_bibliography(self):
        lines=ROOT.joinpath('nodes',NODE,'data/sources.jsonl').read_bytes().splitlines()
        self.assertEqual(len(lines),9)
        for line in lines:
            j=json.loads(line)
            self.assertFalse(j['provenance']['original_publisher_bytes_authenticated'])
            self.assertFalse(j['provenance']['scientific_review'])

if __name__=='__main__':unittest.main()
