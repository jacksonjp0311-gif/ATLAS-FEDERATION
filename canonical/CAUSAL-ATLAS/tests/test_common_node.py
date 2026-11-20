import json,unittest
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil
from importlib.resources import files
from atlas_forge.common import AtlasStore,ContractError

class CommonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root=Path(str(files('causal_atlas')/'resources/common'));cls.store=AtlasStore(cls.root)
    def test_load_same_runtime(self):self.assertEqual(len(self.store.discover()['nodes']),1)
    def test_search(self):self.assertTrue(self.store.search('standardization positivity')['results'])
    def test_context(self):
        p=self.store.assemble_context('standardization positivity');self.assertTrue(self.store.validate_context(p)['valid'])
    def test_no_match(self):self.assertEqual(self.store.assemble_context('zxqvupl987')['status'],'no_match')
    def test_empty_refused(self):
        with self.assertRaises(ContractError):self.store.assemble_context('')
    def test_full_qualifiers(self):
        p=self.store.assemble_context('standardization',limit=1)
        self.assertIn('causal-atlas:positivity',p['context_text']);self.assertIn('causal-atlas:exchangeability',p['context_text'])
    def test_budget(self):
        p=self.store.assemble_context('standardization',max_context_bytes=512)
        self.assertLessEqual(len(p['context_text'].encode()),512);self.assertTrue(self.store.validate_context(p)['valid'])
    def test_modified_text_rejected(self):
        p=self.store.assemble_context('standardization');p['context_text']+=' tampered'
        self.assertFalse(self.store.validate_context(p)['valid'])
    def test_sources_present(self):
        p=self.store.assemble_context('standardization');self.assertIn('causal-atlas:source:HR2006',p['context_text'])
    def test_all_records_preserve_labels(self):
        for p in (self.root/'nodes/causal-atlas/data').glob('*.jsonl'):
            if p.name=='relations.jsonl':continue
            for line in p.read_text().splitlines():
                r=json.loads(line);self.assertNotIn(r['evidence']['review_status'],('human_reviewed','independently_reproduced'))
    def test_tampered_node(self):
        with TemporaryDirectory() as d:
            dest=Path(d)/'node';shutil.copytree(self.root,dest)
            p=dest/'nodes/causal-atlas/data/concepts.jsonl';p.write_bytes(p.read_bytes()+b'\n')
            with self.assertRaises(ContractError):AtlasStore(dest)

if __name__=='__main__':unittest.main()
