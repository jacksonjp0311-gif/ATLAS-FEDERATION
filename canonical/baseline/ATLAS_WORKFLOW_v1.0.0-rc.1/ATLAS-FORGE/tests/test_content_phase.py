from pathlib import Path
import hashlib,json,unittest
ROOT=Path(__file__).resolve().parents[1]
class ContentPhaseTests(unittest.TestCase):
 def test_navigation_runtime_unchanged(self):
  receipt=json.loads((ROOT/'workflow/deferred_navigation.json').read_text())
  self.assertFalse(receipt['new_navigation_features'])
  for row in receipt['files']:self.assertEqual(hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest(),row['sha256'])
 def test_exact_domain_order(self):
  d=json.loads((ROOT/'workflow/domain_roadmap.json').read_text())
  self.assertEqual([r['node_id'] for r in d['domains'][:10]], [x+'-atlas' for x in ['measurement','causal','materials','control','agent','computation','language','energy','bioelectric','manufacturing']])
  q=json.loads((ROOT/'workflow/domain_queue.json').read_text())
  self.assertEqual([r['node_id'] for r in d['domains']],[r['node_id'] for r in q['candidates']])
  self.assertEqual(len(d['domains']),30)
 def test_other_domains_remain_queued(self):
  d=json.loads((ROOT/'workflow/domain_roadmap.json').read_text())
  self.assertTrue(all(r['status']=='queued_not_built' for r in d['domains'][1:]));self.assertFalse(d['next_domain_allowed'])
 def test_navigation_deferred_not_waived(self):
  s=json.loads((ROOT/'workflow/state.json').read_text());self.assertEqual(s['navigation_work'],'deferred_by_owner_not_waived')
  gates=json.loads((ROOT/'workflow/acceptance.json').read_text())['gates'];self.assertIn('G6',gates);self.assertIn('G7',gates)
 def test_history_retained(self):self.assertTrue((ROOT/'history/v0.4.0/common/registry.json').is_file())
