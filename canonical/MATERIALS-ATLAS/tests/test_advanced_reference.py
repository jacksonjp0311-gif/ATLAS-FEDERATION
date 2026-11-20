import unittest,json,hashlib
from pathlib import Path
from materials_atlas.advanced_cases import advanced_casebook
from materials_atlas.advanced import published_hahn1_replay
M=Path(__file__).resolve().parents[1]
N=M/'materials_atlas/resources/common/nodes/materials-atlas'

class TestAdvancedScientificRecordIntegrity(unittest.TestCase):
 def test_historical_revisions_unchanged(self):
  old=json.loads((M/'evidence/baseline_record_revisions_v0.1.0.json').read_text())['records']
  rows={}
  for p in (N/'data').glob('*.jsonl'):
   if p.name=='relations.jsonl':continue
   for line in p.read_text().splitlines():
    if line: r=json.loads(line);rows[r['record_id']]=r['revision']
  self.assertEqual(len(old),52)
  self.assertEqual({k:rows[k] for k in old},old)
  self.assertGreaterEqual(len(rows),89)
 def test_source_closure_and_evidence_types(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_release_reference_scope(self):
  self.assertGreaterEqual(len(list((M/'docs/chapters').glob('*.md'))),19)
  self.assertGreaterEqual(len(list((M/'docs/investigations').glob('*.md'))),8)
  self.assertIn('original-byte', (M/'docs/chapters/13_source_data_and_reproduction.md').read_text())
  self.assertIn('routing', (M/'docs/chapters/18_evidence_bound_decisions.md').read_text().lower())
 def test_replay_and_new_casebook(self):
     self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
 def test_legacy_casebook_still_passes(self):
  from materials_atlas.cases import casebook
  self.assertEqual(casebook()['status'],'passed')

if __name__=='__main__':unittest.main()
