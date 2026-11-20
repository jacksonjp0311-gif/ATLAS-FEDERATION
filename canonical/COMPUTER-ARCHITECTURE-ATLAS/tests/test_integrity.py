"""Standalone archive wire-integrity tests using only Python standard library."""
import unittest,hashlib,json,re
from importlib.resources import files
from computer_atlas.isa import assemble
from computer_atlas.programs import examples

ROOT=files('computer_atlas').joinpath('resources/common')
NODE='computer-architecture-digital-hardware-atlas'


def canonical(obj):return json.dumps(obj,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode('utf-8')


def digest(data):return hashlib.sha256(data).hexdigest()


class TestArchivedNode(unittest.TestCase):
    def test_registry_lock(self):
        raw=ROOT.joinpath('registry.json').read_bytes()
        lock=json.loads(ROOT.joinpath('registry.lock.json').read_text())
        self.assertEqual(lock['sha256'],digest(raw))
        self.assertEqual(len(json.loads(raw)['nodes']),1)
    def test_node_manifest_integrity(self):
        path=ROOT.joinpath('nodes',NODE,'atlas_manifest.json')
        meta=json.loads(path.read_text())
        self.assertEqual(meta['node_id'],NODE)
        self.assertEqual(meta['software_version'],'0.1.0')
        for typ,collection in meta['collections'].items():
            raw=ROOT.joinpath('nodes',NODE,collection['path']).read_bytes()
            self.assertEqual(digest(raw),collection['sha256'],typ)
            self.assertEqual(len(raw.splitlines()),collection['records'],typ)
    def test_revision_integrity(self):
        node=ROOT.joinpath('nodes',NODE)
        for name in ('concepts','claims','equations','methods','sources','relations'):
            for line in node.joinpath('data',name+'.jsonl').read_bytes().splitlines():
                x=json.loads(line)
                self.assertEqual(x['revision'],digest(canonical({k:v for k,v in x.items() if k!='revision'})))
    def test_exact_local_reference_endpoints(self):
        node=ROOT.joinpath('nodes',NODE,'data')
        rows=[json.loads(l) for category in ('concepts','claims','equations','methods','sources')
              for l in node.joinpath(category+'.jsonl').read_bytes().splitlines()]
        index={(x['record_id'],x['revision']) for x in rows}
        self.assertEqual(len(index),102)
        relations=[json.loads(l) for l in node.joinpath('relations.jsonl').read_bytes().splitlines()]
        self.assertEqual(len(relations),96)
        for r in relations:
            self.assertIn((r['from']['record_id'],r['from']['revision']),index)
            self.assertIn((r['to']['record_id'],r['to']['revision']),index)
    def test_source_gaps_honest(self):
        lines=ROOT.joinpath('nodes',NODE,'data/sources.jsonl').read_bytes().splitlines()
        self.assertEqual(len(lines),6)
        for l in lines:
            x=json.loads(l)
            self.assertFalse(x['provenance']['original_publisher_bytes_authenticated'])
            self.assertFalse(x['provenance']['independent_review'])
    def test_reproducible_program_lengths(self):
        for blob in examples().values():
            self.assertTrue(2<=len(blob)<=256)
            self.assertEqual(len(blob)%2,0)

if __name__=='__main__':unittest.main()
