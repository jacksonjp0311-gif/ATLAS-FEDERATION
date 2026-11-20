"""Current 21-node survival reader acceptance for OS Internals #15."""
import json,pathlib,unittest
from tools.atlas_offline import Atlas
R=pathlib.Path(__file__).resolve().parents[1]
class TestOSSurvival(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.a=Atlas(R)
 def test_node_count(self):self.assertEqual(self.a.catalog()['nodes'],21)
 def test_records(self):self.assertEqual(self.a.catalog()['records'],3817)
 def test_relations(self):self.assertEqual(self.a.catalog()['relationships'],3029)
 def test_sources(self):self.assertEqual(self.a.gaps()['bibliographic_source_records_total'],619)
 def test_crypto_record(self):self.assertEqual(self.a.record('cryptographic-protocols-atlas:chapter-01-concept')['record']['provenance']['edition_added'],'1.0.0')
 def test_os_first(self):self.assertEqual(self.a.record('os-internals-atlas:chapter-01-concept')['record']['provenance']['edition_added'],'1.0.0')
 def test_os_last(self):self.assertEqual(self.a.record('os-internals-atlas:chapter-22-method')['record']['provenance']['edition_added'],'1.0.0')
 def test_source_link(self):self.assertEqual(self.a.record('os-internals-atlas:source:KERNEL_EEVDF')['record']['provenance']['publisher_original_authenticated'],False)
 def test_search(self):self.assertGreater(self.a.search('OS page table TLB shootdown privilege memory',node='os-internals-atlas')['matches_total'],0)
 def test_qualified_dependencies(self):self.assertGreaterEqual(len(self.a.trace('os-internals-atlas:chapter-06-method',depth=2)['records']),2)
 def test_node_manifest_count(self):
  m=self.a.manifest('os-internals-atlas')
  self.assertEqual((sum(v['records'] for k,v in m['collections'].items() if k!='relations'),m['collections']['relations']['records']),(128,154))
 def test_all_manifests(self):self.assertEqual(self.a.verify(all_files=False)['node_manifest_hashes_verified'],21)
 def test_roadmap(self):
  q=json.loads((R/'DOMAIN_QUEUE.json').read_text())
  self.assertEqual(len(q['candidates']),30)
  self.assertEqual(next(c['priority'] for c in q['candidates'] if c['node_id']=='os-internals-atlas'),15)
 def test_held_science(self):self.assertEqual(self.a.gaps()['publisher_original_bytes_authenticated_in_this_offline_check'],0)
