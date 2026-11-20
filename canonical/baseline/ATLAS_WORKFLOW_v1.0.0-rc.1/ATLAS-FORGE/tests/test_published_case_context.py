"""Authored corpus regressions, not an independently blinded evaluation."""
import json
from pathlib import Path
import unittest
from atlas_forge.common import AtlasStore

class PublishedContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.store = AtlasStore()
        cls.context = cls.store.assemble_context('Pontius certified intercept', node_ids=['measurement-atlas'], max_context_bytes=32768)
    def test_published_disagreement_is_visible(self):
        self.assertEqual(self.context['status'], 'conflicting_context')
        self.assertTrue(self.context['conflicts'])
    def test_conflicting_claims_preserved(self):
        self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
    def test_source_closure_and_replay(self):
        self.assertTrue(self.store.validate_context(self.context)['valid'])
    def test_no_evidence_promotion(self):
        for r in self.context['payload']['records']:
            self.assertNotEqual(r['evidence']['review_status'], 'independently_reproduced')
    def test_new_node_inventory(self):
        rows = [r for r in self.store.export() if r['node_id'] == 'measurement-atlas']
        self.assertEqual(len(rows), 141)
    def test_thirty_domain_registry_keeps_measurement_active(self):
        root = Path(__file__).resolve().parents[1]
        queue = json.loads((root/'workflow/domain_queue.json').read_text())
        self.assertEqual(len(queue['candidates']), 30)
        self.assertEqual(queue['current_domain'], 'measurement-atlas')
