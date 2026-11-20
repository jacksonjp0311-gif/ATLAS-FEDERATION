# SRD69_PUBLIC_DERIVATIVE
import unittest, json,hashlib
from pathlib import Path
from materials_atlas.v1_cases import v1_casebook
R=Path(__file__).resolve().parents[1]
N=R/'materials_atlas/resources/common/nodes/materials-atlas'
def rows(kind):return [json.loads(x) for x in (N/'data'/f'{kind}.jsonl').read_text().splitlines() if x]

class V1ScientificContent(unittest.TestCase):
 def test_v1_record_counts_and_preserved_revisions(self):
  allrecords=[r for kind in ['sources','concepts','methods','equations','datasets','claims','reviews'] for r in rows(kind)]
  self.assertEqual(len(allrecords),148)
  self.assertEqual(sum(r['type']=='source' for r in allrecords),29)
  self.assertEqual(sum(r['provenance'].get('edition_added')=='1.0.0' for r in allrecords),36)
  earlier=json.loads((R/'evidence/baseline_record_revisions_v0.3.0.json').read_text())['records']
  self.assertEqual(len(earlier),112)
  by={x['record_id']:x for x in allrecords}
  self.assertEqual(len(by),len(allrecords))
  for k,v in earlier.items():self.assertEqual(by[k]['revision'],v,k)
 def test_v1_relationships_preserve_existing(self):
  relations=rows('relations')
  self.assertEqual(len(relations),84)
  self.assertEqual(len({r['relation_id'] for r in relations}),84)
  by={r['record_id']:r for kind in ['sources','concepts','methods','equations','datasets','claims','reviews'] for r in rows(kind)}
  for r in relations:
   for part in ['from','to']:
    self.assertEqual(r[part]['revision'],by[r[part]['record_id']]['revision'])
 def test_source_provenance_and_rights(self):
  src=json.loads((R/'evidence/source_register.json').read_text())['sources']
  self.assertEqual(len(src),29)
  for s in src:
   self.assertTrue(s['url'].startswith('https://'))
   self.assertFalse(s['independent_review'])
  copper=next(x for x in src if x['id']=='NIST-CU-SHOMATE')
  self.assertIn('copyright',copper['rights'])
  pdf=next(x for x in src if x['id']=='NIST-CORROSION-MASSLOSS')
  self.assertIn('screenshot_failed',pdf['access'])
 def test_no_false_origin(self):
  for kind in ['sources','concepts','methods','equations','datasets','claims','reviews']:
   for r in rows(kind):
    self.assertFalse(r['provenance']['independent_review'])
    self.assertNotEqual(r['evidence']['origin'],'laboratory_measured')
    self.assertTrue(r['content']['limitations'])
 def test_docs_and_cases(self):
  self.assertEqual(len(list((R/'docs/chapters').glob('*.md'))),32)
  self.assertEqual(len(list((R/'docs/investigations').glob('*.md'))),19)
  self.assertEqual(v1_casebook()['count'],8)
  self.assertEqual(v1_casebook()['status'],'partial_rights_withheld')
 def test_named_refusals(self):
  t=(R/'docs/chapters/29_weakest_link_statistics_not_automatic_reliability.md').read_text()
  self.assertIn('ordinary',t.lower())
  t=(R/'docs/chapters/25_corrosion_penetration_and_localized_failure.md').read_text()
  self.assertIn('pit',t.lower())
  t=(R/'docs/chapters/28_creep_rates_versus_life_prediction.md').read_text()
  self.assertIn('rupture',t.lower())

if __name__=='__main__':unittest.main()
