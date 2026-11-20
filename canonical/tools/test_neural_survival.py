"""Original domain #13 current-reader tests. Distributed v1 test remains frozen."""
import json,pathlib,unittest
from tools.atlas_offline import Atlas
R=pathlib.Path(__file__).resolve().parents[1]
class TestNeuralSurvival(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.a=Atlas(R)
 def test_node_count(self):self.assertEqual(self.a.catalog()['nodes'],19)
 def test_records(self):self.assertEqual(self.a.catalog()['records'],3602)
 def test_relations(self):self.assertEqual(self.a.catalog()['relationships'],2767)
 def test_source_cards(self):self.assertEqual(self.a.gaps()['bibliographic_source_records_total'],586)
 def test_revision_preserved(self):self.assertEqual(self.a.record('distributed-systems-atlas:chapter-01-concept')['record']['revision'],'5013e1e83518f108193fad103344920fd4cc73b6f64b0804fa2ce7fe47f440ad')
 def test_first_new(self):self.assertEqual(self.a.record('neural-architectures-atlas:chapter-01-concept')['record']['provenance']['edition_added'],'1.0.0')
 def test_last_new(self):self.assertEqual(self.a.record('neural-architectures-atlas:chapter-16-concept')['record']['provenance']['edition_added'],'1.0.0')
 def test_neural_search(self):self.assertGreater(self.a.search('gradient backpropagation chain rule finite difference',node='neural-architectures-atlas')['matches_total'],0)
 def test_qualified_method(self):self.assertGreaterEqual(len(self.a.trace('neural-architectures-atlas:chapter-05-method',depth=2)['records']),2)
 def test_manifest_hashes(self):self.assertEqual(self.a.verify(all_files=False)['node_manifest_hashes_verified'],19)
 def test_node_manifest(self):
  m=self.a.manifest('neural-architectures-atlas')
  self.assertEqual((sum(v['records'] for k,v in m['collections'].items() if k!='relations'),m['collections']['relations']['records']),(70,68))
 def test_original_roadmap(self):
  x=json.loads((R/'DOMAIN_QUEUE.json').read_text());self.assertEqual(len(x['candidates']),30)
  self.assertEqual(next(c['priority'] for c in x['candidates'] if c['node_id']=='neural-architectures-atlas'),13)
 def test_science_hold(self):self.assertEqual(self.a.gaps()['publisher_original_bytes_authenticated_in_this_offline_check'],0)
