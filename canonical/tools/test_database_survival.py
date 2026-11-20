"""Database Optimization original #17: 23-node offline federation reader acceptance."""
import json,unittest
from pathlib import Path
from tools.atlas_offline import Atlas
ROOT=Path(__file__).resolve().parents[1]
class TestDatabaseSurvival(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.a=Atlas(ROOT)
 def test_nodes(self):self.assertEqual(self.a.catalog()['nodes'],23)
 def test_records(self):self.assertEqual(self.a.catalog()['records'],4048)
 def test_relations(self):self.assertEqual(self.a.catalog()['relationships'],3283)
 def test_sources(self):self.assertEqual(self.a.gaps()['bibliographic_source_records_total'],651)
 def test_new_manifest(self):
  m=self.a.manifest('database-optimization-atlas')
  self.assertEqual((sum(x['records'] for k,x in m['collections'].items() if k!='relations'),m['collections']['relations']['records']),(100,98))
 def test_first_chapter(self):self.assertEqual(self.a.record('database-optimization-atlas:chapter-01-concept')['record']['provenance']['edition_added'],'1.0.0')
 def test_last_method(self):self.assertEqual(self.a.record('database-optimization-atlas:chapter-22-method')['record']['provenance']['edition_added'],'1.0.0')
 def test_publisher_source_auth_hold(self):self.assertIs(self.a.record('database-optimization-atlas:source:PG_INDEX_ONLY')['record']['provenance']['publisher_original_authenticated'],False)
 def test_old_network_record_unchanged(self):self.assertEqual(self.a.record('network-stacks-atlas:chapter-22-concept')['record']['provenance']['edition_added'],'1.0.0')
 def test_search(self):self.assertGreater(self.a.search('index-only heap visibility checks MVCC',node='database-optimization-atlas')['matches_total'],0)
 def test_dependency_trace(self):self.assertGreater(len(self.a.trace('database-optimization-atlas:chapter-22-concept',depth=2)['records']),1)
 def test_schema_registry(self):self.assertEqual(self.a.verify(all_files=False)['node_manifest_hashes_verified'],23)
 def test_original_30(self):
  q=json.loads((ROOT/'DOMAIN_QUEUE.json').read_text())
  self.assertEqual(len(q['candidates']),30)
  self.assertEqual(next(x['priority'] for x in q['candidates'] if x['node_id']=='database-optimization-atlas'),17)
 def test_no_physical_claim(self):self.assertEqual(self.a.gaps()['physical_fabrication_verified_in_this_offline_check'],0)
 def test_rights(self):self.assertIn(self.a.record('database-optimization-atlas:source:SQLITE_EQP')['record']['rights']['status'],('local_reference','unknown','restricted'))
