"""Current reader check: original cryptographic protocols #14."""
import json,pathlib,unittest
from tools.atlas_offline import Atlas
R=pathlib.Path(__file__).resolve().parents[1]
class TestCryptoSurvival(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.a=Atlas(R)
 def test_node_count(self): self.assertEqual(self.a.catalog()['nodes'],20)
 def test_records(self): self.assertEqual(self.a.catalog()['records'],3689)
 def test_relations(self): self.assertEqual(self.a.catalog()['relationships'],2875)
 def test_sources(self): self.assertEqual(self.a.gaps()['bibliographic_source_records_total'],601)
 def test_neural_record_preserved(self): self.assertEqual(self.a.record('neural-architectures-atlas:chapter-01-concept')['record']['provenance']['edition_added'],'1.0.0')
 def test_first_new(self): self.assertEqual(self.a.record('cryptographic-protocols-atlas:chapter-01-concept')['record']['provenance']['edition_added'],'1.0.0')
 def test_last_new(self): self.assertEqual(self.a.record('cryptographic-protocols-atlas:chapter-18-method')['record']['provenance']['edition_added'],'1.0.0')
 def test_source_revision(self): self.assertEqual(self.a.record('cryptographic-protocols-atlas:source:RFC9846')['record']['provenance']['publisher_original_authenticated'],False)
 def test_retrieve(self):self.assertGreater(self.a.search('HMAC SHA-256 key message authentication RFC 4231',node='cryptographic-protocols-atlas')['matches_total'],0)
 def test_qualified_graph(self):self.assertGreaterEqual(len(self.a.trace('cryptographic-protocols-atlas:chapter-12-method',depth=2)['records']),2)
 def test_node_manifest_count(self):
  m=self.a.manifest('cryptographic-protocols-atlas')
  self.assertEqual((sum(v['records'] for k,v in m['collections'].items() if k!='relations'),m['collections']['relations']['records']),(87,108))
 def test_all_manifests(self):self.assertEqual(self.a.verify(all_files=False)['node_manifest_hashes_verified'],20)
 def test_roadmap(self):
  q=json.loads((R/'DOMAIN_QUEUE.json').read_text());self.assertEqual(len(q['candidates']),30)
  self.assertEqual(next(c['priority'] for c in q['candidates'] if c['node_id']=='cryptographic-protocols-atlas'),14)
 def test_science_hold(self):self.assertEqual(self.a.gaps()['publisher_original_bytes_authenticated_in_this_offline_check'],0)
