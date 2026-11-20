"""Authored integration regressions; not held-out scientific evaluation."""
import unittest
from atlas_forge.common import AtlasStore
class CoverageContextTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.store=AtlasStore();cls.c=cls.store.assemble_context('Pontius upper bound recomputed handbook',node_ids=['measurement-atlas'],max_context_bytes=32768)
 def test_new_conflict_exposed(self):self.assertEqual(self.c['status'],'conflicting_context')
 def test_both_upper_bounds_retained(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_context_replays_exactly(self):self.assertTrue(self.store.validate_context(self.c)['valid'])
 def test_total_inventory(self):self.assertEqual(self.store.discover()['records'],505)
 def test_model_limitations_retained(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_reference_ids_unique(self):
  rows=list(self.store.export());self.assertEqual(len({r['record_id'] for r in rows}),len(rows))
