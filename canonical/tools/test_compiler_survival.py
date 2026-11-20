"""Compiler v0.1.0 canonical federation reader acceptance, original priority #18."""
import json,unittest
from pathlib import Path
from tools.atlas_offline import Atlas
R=Path(__file__).resolve().parents[1]
class TestCompilerSurvival(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.a=Atlas(R)
 def test_nodes(self):self.assertEqual(self.a.catalog()['nodes'],24)
 def test_records(self):self.assertEqual(self.a.catalog()['records'],4102)
 def test_relations(self):self.assertEqual(self.a.catalog()['relationships'],3337)
 def test_sources(self):self.assertEqual(self.a.gaps()['bibliographic_source_records_total'],656)
 def test_manifest(self):
  m=self.a.manifest('compiler-design-atlas')
  self.assertEqual(sum(x['records'] for k,x in m['collections'].items() if k!='relations'),54)
  self.assertEqual(m['collections']['relations']['records'],54)
 def test_first(self):self.assertEqual(self.a.record('compiler-design-atlas:chapter-01-concept')['record']['provenance']['edition_added'],'0.1.0')
 def test_last(self):self.assertEqual(self.a.record('compiler-design-atlas:chapter-12-method')['record']['provenance']['edition_added'],'0.1.0')
 def test_source_hold(self):self.assertIs(self.a.record('compiler-design-atlas:source:WASM_CORE_3')['record']['provenance']['publisher_original_authenticated'],False)
 def test_prior_link(self):
  old=self.a.record('computer-architecture-digital-hardware-atlas:chapter-26-claim')['record']
  self.assertEqual(old['revision'],'f86e0d9ad3bdc11917d694db65cb46781e98ab83acddbf398f58865b6c321a13')
 def test_search(self):self.assertGreater(self.a.search('bounded typed Pratt compiler lexical analysis',node='compiler-design-atlas')['matches_total'],0)
 def test_exact_source_context(self):self.assertGreater(len(self.a.trace('compiler-design-atlas:chapter-01-concept',depth=2)['records']),1)
 def test_registry_hashes(self):self.assertEqual(self.a.verify(all_files=False)['node_manifest_hashes_verified'],24)
 def test_original_queue(self):
  q=json.loads((R/'DOMAIN_QUEUE.json').read_text())
  self.assertEqual(len(q['candidates']),30)
  self.assertEqual(next(x['priority'] for x in q['candidates'] if x['node_id']=='compiler-design-atlas'),18)
 def test_no_hardware_claim(self):self.assertEqual(self.a.gaps()['physical_fabrication_verified_in_this_offline_check'],0)
 def test_rights(self):self.assertEqual(self.a.record('compiler-design-atlas:source:COMPCERT_318')['record']['rights']['status'],'local_reference')
