import unittest,hashlib,json,sys
from pathlib import Path
from importlib.resources import files
from computation_atlas.models import *
from computation_atlas.proofs import *

class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root=Path(__file__).resolve().parents[1]
        cls.bundle=Path(str(files('computation_atlas')/'resources/common'))
    def test_software_version(self):
        from computation_atlas import __version__
        self.assertEqual(__version__,'1.0.0')
    def test_standalone_registry_exists(self):self.assertTrue((self.bundle/'registry.lock.json').exists())
    def test_registry_exact_sha(self):
        registry=(self.bundle/'registry.json').read_bytes()
        self.assertEqual(json.loads((self.bundle/'registry.lock.json').read_text())['sha256'],hashlib.sha256(registry).hexdigest())
    def test_bundle_one_node(self):
        self.assertEqual(len(json.loads((self.bundle/'registry.json').read_text())['nodes']),1)
    def test_bundle_manifest_matches(self):
        entry=json.loads((self.bundle/'registry.json').read_text())['nodes'][0]
        self.assertEqual(hashlib.sha256((self.bundle/entry['manifest']).read_bytes()).hexdigest(),entry['manifest_sha256'])
    def test_bundle_collections_hashes(self):
        node=self.bundle/'nodes/computation-atlas'
        manifest=json.loads((node/'atlas_manifest.json').read_text())
        for kind,meta in manifest['collections'].items():
            path=node/meta['path'];self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),meta['sha256'])
    def test_reference_chapters(self):self.assertGreaterEqual(len(list((self.root/'docs/chapters').glob('*.md'))),34)
    def test_manual_contains_derivation(self):self.assertIn('proof', (self.root/'docs/DEPTH_MANUAL_v0.1.0.md').read_text().lower())
    def test_original_cited_bytes_absent(self):self.assertNotEqual((self.root/'docs/SOURCE_REGISTER.md').read_text().count('original bytes absent'),0)
    def test_nonnetwork_core(self):
        for p in ('models.py','proofs.py','cases.py'):
            text=(self.root/'computation_atlas'/p).read_text()
            self.assertNotIn('import requests',text);self.assertNotIn('import socket',text)
    def test_rights_and_gaps_recorded(self):
        srcs=[json.loads(l) for l in (self.bundle/'nodes/computation-atlas/data/sources.jsonl').read_text().splitlines()]
        self.assertGreaterEqual(len(srcs),15)
        for r in srcs:self.assertEqual(r['provenance']['primary_source_bytes_archived'],False);self.assertTrue(r['evidence']['gaps'])
    def test_all_reference_records_source_linked(self):
        node=self.bundle/'nodes/computation-atlas/data'
        for p in node.glob('*.jsonl'):
            if p.name=='sources.jsonl' or p.name=='relations.jsonl':continue
            for line in p.read_text().splitlines():
                r=json.loads(line);self.assertTrue(r['sources'] or r['evidence']['gaps'],r['record_id'])
    def test_unrelated_manifest_version(self):
        manifest=json.loads((self.bundle/'nodes/computation-atlas/atlas_manifest.json').read_text())
        self.assertEqual(manifest['software_version'],'1.0.0')
