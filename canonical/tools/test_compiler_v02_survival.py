"""New current Compiler v0.2 node acceptance; historical v0.1 kept frozen."""
import json,unittest
from pathlib import Path
from tools.atlas_offline import Atlas
R=Path(__file__).resolve().parents[1]
class TestCompilerV02Survival(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.a=Atlas(R)
 def test_node_count(self):self.assertEqual(self.a.catalog()['nodes'],24)
 def test_record_count(self):self.assertEqual(self.a.catalog()['records'],4120)
 def test_relation_count(self):self.assertEqual(self.a.catalog()['relationships'],3357)
 def test_source_count(self):self.assertEqual(self.a.gaps()['bibliographic_source_records_total'],657)
 def test_new_manifest(self):
  m=self.a.manifest('compiler-design-atlas')
  self.assertEqual(m['software_version'],'0.2.0')
  self.assertEqual(sum(v['records'] for k,v in m['collections'].items() if k!='relations'),72)
  self.assertEqual(m['collections']['relations']['records'],74)
 def test_old_exact_record(self):
  item=self.a.record('compiler-design-atlas:chapter-03-concept')['record']
  self.assertEqual(item['provenance']['edition_added'],'0.1.0')
  prior=R/'history/compiler_design_v0.1.0_source/data/concepts.jsonl'
  old=next(json.loads(x) for x in prior.read_text().splitlines() if x and json.loads(x)['record_id']==item['record_id'])
  self.assertEqual(item,old)
 def test_new_exact_record(self):
  item=self.a.record('compiler-design-atlas:chapter-15-concept')['record']
  self.assertEqual(item['provenance']['edition_added'],'0.2.0')
 def test_new_source_hold(self):
  item=self.a.record('compiler-design-atlas:source:LLVM_CODEGEN_TUTORIAL')['record']
  self.assertIs(item['provenance']['publisher_original_authenticated'],False)
 def test_oracle_receipt(self):
  x=json.loads((R/'COMPILER-DESIGN-ATLAS/evidence/INDEPENDENT_ORACLE_RECEIPT_v0.2.0.json').read_text())
  self.assertEqual(x['independent_VM_semantic_comparisons'],36032)
  self.assertEqual(x['result'],'passed')
 def test_no_original_30_change(self):
  q=json.loads((R/'DOMAIN_QUEUE.json').read_text())
  self.assertEqual(len(q['candidates']),30)
  self.assertEqual(next(x['priority'] for x in q['candidates'] if x['node_id']=='compiler-design-atlas'),18)
