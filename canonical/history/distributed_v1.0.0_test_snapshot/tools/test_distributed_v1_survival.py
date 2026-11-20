"""Scoped v1 18-node federation acceptance; original v0.1 tests run frozen."""
import json,pathlib,unittest
from tools.atlas_offline import Atlas
R=pathlib.Path(__file__).resolve().parents[1]
class TestDistributedV1Survival(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.a=Atlas(R)
 def test_nodes(self):self.assertEqual(self.a.catalog()['nodes'],18)
 def test_full_counts(self):self.assertEqual((self.a.catalog()['records'],self.a.catalog()['relationships']),(3532,2699))
 def test_sources(self):self.assertEqual(self.a.gaps()['bibliographic_source_records_total'],580)
 def test_first_v01_record_immutable(self):self.assertEqual(self.a.record('distributed-systems-atlas:chapter-01-concept')['record']['revision'],'5013e1e83518f108193fad103344920fd4cc73b6f64b0804fa2ce7fe47f440ad')
 def test_v1_revision(self):self.assertEqual(self.a.record('distributed-systems-atlas:chapter-24-concept')['record']['provenance']['edition_added'],'1.0.0')
 def test_bound_qualifier(self):
  x=self.a.trace('distributed-systems-atlas:chapter-17-method',depth=2)
  self.assertGreaterEqual(len(x['records']),2)
 def test_search(self):self.assertGreater(self.a.search('bounded Paxos agreement proposer crash recovery',node='distributed-systems-atlas')['matches_total'],0)
 def test_queue(self):
  q=json.loads((R/'DOMAIN_QUEUE.json').read_text());self.assertEqual(len(q['candidates']),30)
  self.assertEqual(next(x['priority'] for x in q['candidates'] if x['node_id']=='neural-architectures-atlas'),13)
 def test_manifest(self):self.assertEqual(self.a.verify(all_files=False)['node_manifest_hashes_verified'],18)
 def test_science_hold(self):self.assertEqual(self.a.gaps()['publisher_original_bytes_authenticated_in_this_offline_check'],0)
 def test_domain_totals(self):
  m=self.a.manifest('distributed-systems-atlas')
  self.assertEqual((sum(v['records'] for k,v in m['collections'].items() if k!='relations'),m['collections']['relations']['records']),(113,100))
if __name__=='__main__':unittest.main()
