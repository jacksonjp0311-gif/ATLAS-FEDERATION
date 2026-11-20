"""New current-state offline Atlas search and fixity tests; old v0.5 cases untouched.

The 10 original 15-node expected-count tests remain in the immutable v0.5
historical release; their 27 generic tests run unmodified on the current
fingerprint-only reader. These 10 v0.1 tests validate new 16-node state.
"""
import unittest, pathlib, json
from tools.atlas_offline import Atlas
ROOT=pathlib.Path(__file__).resolve().parents[1]
class TestBioelectricSurvival(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.a=Atlas(ROOT)
 def test_sixteen_nodes(self):self.assertEqual(self.a.catalog()['nodes'],16)
 def test_new_record_and_relation_counts(self):
  c=self.a.catalog();self.assertEqual((c['records'],c['relationships']),(3314,2495))
 def test_554_source_cards(self):self.assertEqual(self.a.gaps()['bibliographic_source_records_total'],554)
 def test_bioelectric_source_search(self):
  self.assertGreater(self.a.search('Hodgkin Huxley membrane voltage',node='bioelectric-atlas')['matches_total'],0)
 def test_full_bioelectric_record_exact_revision(self):
  t=self.a.record('bioelectric-atlas:chapter-03-concept')['record'];self.assertTrue(t['revision'])
 def test_numerical_method_trace(self):
  x=self.a.trace('bioelectric-atlas:chapter-07-method',depth=2)
  self.assertGreater(len(x['records']),1)
 def test_science_remains_unaccepted(self):
  gaps=self.a.gaps();self.assertEqual(gaps['publisher_original_bytes_authenticated_in_this_offline_check'],0)
  self.assertEqual(gaps['physical_fabrication_verified_in_this_offline_check'],0)
 def test_manual_discovery(self):
  manuals=self.a.manuals()['items'];self.assertTrue(any(x['domain']=='BIOELECTRIC-ATLAS' for x in manuals))
 def test_common_audit_16_nodes(self):
  result=self.a.verify(all_files=False)
  self.assertEqual(result['node_manifest_hashes_verified'],16)
 def test_whole_source_inventory_when_sealed(self):
  result=self.a.verify(all_files=True)
  self.assertGreaterEqual(result['source_file_hashes_verified'],9364)
if __name__=='__main__':unittest.main()
