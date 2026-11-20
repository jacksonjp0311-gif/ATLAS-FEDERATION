"""Network Stacks original domain #16 22-node offline reader acceptance."""
import unittest,json
from pathlib import Path
from tools.atlas_offline import Atlas,AtlasError
R=Path(__file__).resolve().parents[1]
class TestNetworkSurvival(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.a=Atlas(R)
 def test_nodes(self):self.assertEqual(self.a.catalog()['nodes'],22)
 def test_records(self):self.assertEqual(self.a.catalog()['records'],3948)
 def test_relations(self):self.assertEqual(self.a.catalog()['relationships'],3185)
 def test_sources(self):self.assertEqual(self.a.gaps()['bibliographic_source_records_total'],640)
 def test_manifest_count(self):
  m=self.a.manifest('network-stacks-atlas')
  self.assertEqual((sum(v['records'] for k,v in m['collections'].items() if k!='relations'),m['collections']['relations']['records']),(131,156))
 def test_first_chapter(self):self.assertEqual(self.a.record('network-stacks-atlas:chapter-01-concept')['record']['provenance']['edition_added'],'1.0.0')
 def test_last_method(self):self.assertEqual(self.a.record('network-stacks-atlas:chapter-22-method')['record']['provenance']['edition_added'],'1.0.0')
 def test_source_authentication_hold(self):self.assertIs(self.a.record('network-stacks-atlas:source:RFC9846')['record']['provenance']['publisher_original_authenticated'],False)
 def test_prior_os_record(self):self.assertEqual(self.a.record('os-internals-atlas:chapter-22-method')['record']['provenance']['edition_added'],'1.0.0')
 def test_search(self):self.assertGreater(self.a.search('UDP pseudoheader IPv6 zero checksum',node='network-stacks-atlas')['matches_total'],0)
 def test_dependency_trace(self):self.assertGreater(len(self.a.trace('network-stacks-atlas:chapter-22-method',depth=2)['records']),1)
 def test_schema_registry(self):self.assertEqual(self.a.verify(all_files=False)['node_manifest_hashes_verified'],22)
 def test_original_30(self):
  q=json.loads((R/'DOMAIN_QUEUE.json').read_text())
  self.assertEqual(len(q['candidates']),30)
  self.assertEqual(next(x['priority'] for x in q['candidates'] if x['node_id']=='network-stacks-atlas'),16)
 def test_no_physical_claim(self):self.assertEqual(self.a.gaps()['physical_fabrication_verified_in_this_offline_check'],0)
 def test_rights_restrictions(self):self.assertIn(self.a.record('network-stacks-atlas:source:RFC9293')['record']['rights']['status'],('local_reference','unknown','restricted'))
