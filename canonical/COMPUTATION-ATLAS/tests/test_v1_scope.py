"""v1 revision/provenance tests; not scientific peer-review."""
import unittest,json,sys
from pathlib import Path
from computation_atlas.v1_cases import casebook_v1
from atlas_forge.common import AtlasStore,revision
R=Path(__file__).resolve().parents[1]
class ScopeV1(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.s=AtlasStore(R/'computation_atlas/resources/common');cls.r={r['record_id']:r for r in cls.s.export()}
 def test_inventory(self):
  self.assertEqual(len(self.r),234);self.assertEqual(len(self.s._relations),251)
  self.assertEqual(sum(r['type']=='source' for r in self.r.values()),21)
 def test_old_revisions(self):
  old=json.loads((R/'evidence/previous_record_revisions_v0.2.0.json').read_text());self.assertEqual(len(old),232)
  for rid,rev in old.items():self.assertEqual(self.r[rid]['revision'],rev)
 def test_old_relations(self):
  old=json.loads((R/'evidence/previous_relation_revisions_v0.2.0.json').read_text());self.assertEqual(len(old),250)
  for rid,rev in old.items():self.assertEqual(self.s._relations[rid]['revision'],rev)
 def test_all_closure(self):
  for r in self.r.values():
   self.assertEqual(r['revision'],revision(r));self.assertTrue(r['content']['limitations'])
   for link in r['sources']:
    self.assertEqual(self.r[link['record_id']]['revision'],link['revision'])
    self.assertEqual(self.r[link['record_id']]['type'],'source')
  for r in self.s._relations.values():
   self.assertEqual(r['revision'],revision(r))
   for key in ['from','to']:self.assertEqual(self.r[r[key]['record_id']]['revision'],r[key]['revision'])
 def test_sources_not_invented(self):
  for r in self.r.values():
   if r['type']=='source':self.assertFalse(r['provenance'].get('primary_source_bytes_archived',True))
 def test_chapters_and_cases(self):
  self.assertEqual(len(list((R/'docs/chapters').glob('*.md'))),50)
  self.assertEqual(casebook_v1()['count'],32)
  self.assertEqual(casebook_v1()['status'],'passed')
 def test_guide_links(self):
  guide=(R/'docs/REFERENCE_GUIDE.md').read_text()
  for p in (R/'docs/chapters').glob('*.md'):self.assertIn(p.name,guide)
 def test_context(self):
  for q in ['maximum flow min cut capacity', 'fft radial convolution padding','vector clock concurrency happens-before','linear equations exact rational solving']:
   p=self.s.assemble_context(q,node_ids=['computation-atlas'])
   self.assertTrue(self.s.validate_context(p)['valid'])
 def test_math_no_live_network(self):
  from computation_atlas import advanced_v02
  self.assertFalse(hasattr(advanced_v02,'call_llm'));self.assertFalse(hasattr(advanced_v02,'send_email'))
 def test_mathematical_methods_in_distribution(self):
  import computation_atlas.advanced_v02 as a
  self.assertEqual(a.gaussian_solve_exact([[2,1],[1,-1]],[5,1])['solution'],['2','1'])
  self.assertEqual(a.kruskal_forest(4,[(0,1,1),(1,2,2),(2,3,1)])['components'],1)
if __name__=='__main__':unittest.main()
