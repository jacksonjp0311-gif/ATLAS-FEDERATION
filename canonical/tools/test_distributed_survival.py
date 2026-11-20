"""Current 18-node exact revision offline reader acceptance; old 17-node assertions frozen."""
import json,pathlib,unittest
from tools.atlas_offline import Atlas
R=pathlib.Path(__file__).resolve().parents[1]
class TestDistributedSurvival(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.a=Atlas(R)
 def test_eighteen_nodes(self):self.assertEqual(self.a.catalog()['nodes'],18)
 def test_exact_counts(self):self.assertEqual((self.a.catalog()['records'],self.a.catalog()['relationships']),(3495,2667))
 def test_sources(self):self.assertEqual(self.a.gaps()['bibliographic_source_records_total'],575)
 def test_search(self):self.assertGreater(self.a.search('Paxos accepted value majority',node='distributed-systems-atlas')['matches_total'],0)
 def test_record_revision(self):self.assertTrue(self.a.record('distributed-systems-atlas:chapter-08-concept')['record']['revision'])
 def test_cross_revision_dependency(self):
  x=self.a.trace('distributed-systems-atlas:chapter-01-concept',depth=2)
  self.assertGreaterEqual(len(x['records']),2)
 def test_queue_unmodified(self):
  q=json.loads((R/'DOMAIN_QUEUE.json').read_text());self.assertEqual(len(q['candidates']),30)
  self.assertEqual(next(x['priority'] for x in q['candidates'] if x['node_id']=='distributed-systems-atlas'),12)
 def test_manual(self):self.assertTrue(any(x['domain']=='DISTRIBUTED-SYSTEMS-ATLAS' for x in self.a.manuals()['items']))
 def test_manifests(self):self.assertEqual(self.a.verify(all_files=False)['node_manifest_hashes_verified'],18)
 def test_source_science_hold(self):self.assertEqual(self.a.gaps()['publisher_original_bytes_authenticated_in_this_offline_check'],0)
 def test_records_are_new(self):
  m=self.a.manifest('distributed-systems-atlas')
  self.assertEqual((sum(v['records'] for k,v in m['collections'].items() if k!='relations'),m['collections']['relations']['records']),(76,68))
if __name__=='__main__':unittest.main()
