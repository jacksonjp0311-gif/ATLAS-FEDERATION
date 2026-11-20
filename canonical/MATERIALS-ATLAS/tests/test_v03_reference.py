import unittest,json,hashlib
from pathlib import Path
from materials_atlas.new_cases import expanded_casebook
from materials_atlas.hahn_diagnostics import hahn1_residual_diagnostics
ROOT=Path(__file__).resolve().parents[1]
N=ROOT/'materials_atlas/resources/common/nodes/materials-atlas'

class TestV03EvidenceBoundaries(unittest.TestCase):
 def test_records_and_revisions(self):
  rows={}
  for p in (N/'data').glob('*.jsonl'):
   if p.name!='relations.jsonl':
    for line in p.read_text().splitlines():
     if line:r=json.loads(line);rows[r['record_id']]=r
  self.assertGreaterEqual(len(rows),112)
  self.assertGreaterEqual(sum(r['type']=='source' for r in rows.values()),26)
  self.assertEqual(sum(r['provenance'].get('edition_added')=='0.3.0' for r in rows.values()),23)
  history=json.loads((ROOT/'evidence/baseline_record_revisions_v0.1.0.json').read_text())['records']
  self.assertEqual(len(history),52)
  for k,revis in history.items():self.assertEqual(rows[k]['revision'],revis)
  for r in rows.values():
   for link in r['sources']:
    self.assertEqual(link['revision'],rows[link['record_id']]['revision'])
    self.assertEqual(rows[link['record_id']]['type'],'source')
 def test_relation_versions(self):
  rows={}
  for p in (N/'data').glob('*.jsonl'):
   if p.name!='relations.jsonl':
    for line in p.read_text().splitlines():
     if line:r=json.loads(line);rows[r['record_id']]=r['revision']
  rel=[json.loads(x) for x in (N/'data/relations.jsonl').read_text().splitlines()]
  self.assertGreaterEqual(len(rel),56)
  for r in rel:
   for k in ('from','to'):
    self.assertEqual(rows[r[k]['record_id']],r[k]['revision'])
 def test_source_maturity_labels(self):
  rows=[]
  for p in (N/'data').glob('*.jsonl'):
   if p.name!='relations.jsonl':rows += [json.loads(x) for x in p.read_text().splitlines() if x]
  for r in rows:
   self.assertFalse(r['provenance']['independent_review'])
   self.assertTrue(r['content']['limitations'])
   self.assertNotEqual(r['evidence']['origin'],'laboratory_measured')
 def test_docs_and_casebook(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
if __name__=='__main__':unittest.main()
