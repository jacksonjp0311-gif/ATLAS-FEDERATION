import json, unittest, hashlib
from pathlib import Path
M=Path(__file__).resolve().parents[1]
NODE=M/'materials_atlas/resources/common/nodes/materials-atlas'

def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(o):return json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def load():
  result=[]
  for p in (NODE/'data').glob('*.jsonl'):
    if p.name!='relations.jsonl':result.extend(json.loads(row) for row in p.read_text().splitlines() if row)
  return result

class TestScientificRecords(unittest.TestCase):
  def test_manifest_file_digest(self):
    m=json.loads((NODE/'atlas_manifest.json').read_text())
    self.assertEqual(m['node_id'],'materials-atlas')
    for k,v in m['collections'].items():
      raw=(NODE/v['path']).read_bytes()
      self.assertEqual(v['sha256'],sha(raw))
      self.assertEqual(v['records'],len(raw.splitlines()))
  def test_record_identity_and_revisions(self):
    rows=load();self.assertGreaterEqual(len(rows),112)
    ids=set()
    for r in rows:
      self.assertNotIn(r['record_id'],ids);ids.add(r['record_id'])
      self.assertEqual(r['revision'],sha(canonical({k:v for k,v in r.items() if k!='revision'})))
      self.assertEqual(r['node_id'],'materials-atlas')
      self.assertFalse(r['provenance']['independent_review'])
  def test_exact_source_closure(self):
    rows=load();by={x['record_id']:x for x in rows}
    for r in rows:
      for ref in r['sources']:
        self.assertIn(ref['record_id'],by);self.assertEqual(by[ref['record_id']]['revision'],ref['revision'])
        self.assertEqual(by[ref['record_id']]['type'],'source')
  def test_no_fake_measurement(self):
    rows=load()
    for r in rows:
      self.assertNotIn(r['evidence']['review_status'],('independently_reproduced','human_reviewed'))
      self.assertNotEqual(r['evidence']['origin'],'laboratory_measured')
      self.assertTrue(r['content']['limitations'])
  def test_source_provider_metadata(self):
    sources=[x for x in load() if x['type']=='source'];self.assertGreaterEqual(len(sources),26)
    for s in sources:
      self.assertTrue(s['provenance']['url'].startswith('https://'))
      self.assertFalse(s['provenance']['source_bytes_archived'])
  def test_competition_closure(self):
    relations=[json.loads(q) for q in (NODE/'data/relations.jsonl').read_text().splitlines()]
    by={x['record_id']:x for x in load()}
    self.assertGreaterEqual(len(relations),56)
    for r in relations:
      self.assertEqual(r['revision'],sha(canonical({k:v for k,v in r.items() if k!='revision'})))
      for k in ('from','to'):
        self.assertIn(r[k]['record_id'],by)
        self.assertEqual(r[k]['revision'],by[r[k]['record_id']]['revision'])
  def test_manual_and_source_register(self):
    docs=(M/'docs/DEPTH_MANUAL_v0.1.0.md').read_text()
    self.assertGreaterEqual(docs.count('# Chapter '),12)
    self.assertTrue((M/'docs/SOURCE_REGISTER.md').is_file())
  def test_pkg_and_root_node_equivalence(self):
    R=M.parent/'common/nodes/materials-atlas'
    if not R.exists():return
    for p in NODE.rglob('*'):
      if p.is_file():self.assertEqual(p.read_bytes(),(R/p.relative_to(NODE)).read_bytes())
if __name__=='__main__':unittest.main()
