from pathlib import Path
import importlib.util
import json
import unittest
from atlas_forge.common import AtlasStore

ROOT=Path(__file__).resolve().parents[1]
class PracticalContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.store=AtlasStore()
    def test_current_inventory(self):self.assertEqual(self.store.discover()['records'],505)
    def test_probability_keeps_model(self):
        p=self.store.assemble_context('normal two-sided conformance probability',node_ids=['measurement-atlas'],max_context_bytes=32768)
        self.assertTrue(self.store.validate_context(p)['valid']);self.assertIn('normal-conformance-model',p['context_text'])
        self.assertIn('source:J106',p['context_text']);self.assertIn('an uncertainty number alone is insufficient to select that distribution.',p['context_text'].lower())
    def test_certificate_keeps_later_use_qualification(self):
        p=self.store.assemble_context('A missing certificate factor is unresolved',node_ids=['measurement-atlas'],max_context_bytes=32768)
        self.assertTrue(self.store.validate_context(p)['valid']);self.assertIn('certificate-use-effects',p['context_text'])
    def test_explicit_pdf_inspection_scope(self):
        rows=[r for r in self.store.export() if r['record_id']=='measurement-atlas:equation:normal-conformance-two-sided']
        self.assertEqual(len(rows),1);self.assertIn('PDF',rows[0]['evidence']['locators'][0]['inspected_scope'])
        self.assertNotEqual(rows[0]['evidence']['review_status'],'independently_verified')
    def test_tiny_budget_remains_valid(self):
        p=self.store.assemble_context('normal two-sided conformance probability',node_ids=['measurement-atlas'],max_context_bytes=512)
        self.assertTrue(self.store.validate_context(p)['valid']);self.assertLessEqual(p['context_bytes'],512)
    def test_candidate_is_not_final(self):
        workspace=ROOT.parent;candidate=json.loads((workspace/'RELEASE_CANDIDATE.json').read_text())
        self.assertEqual(candidate['target_version'],'1.0.0');self.assertFalse(candidate['scientific_v1_accepted']);self.assertFalse(candidate['next_domain_allowed'])
        spec=importlib.util.spec_from_file_location('candidate_readiness',workspace/'tools/v1_readiness.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        r=module.report(workspace);self.assertFalse(r['v1_ready']);self.assertEqual(len(r['subjects']['measurement_sha256']),64)
if __name__=='__main__':unittest.main()
