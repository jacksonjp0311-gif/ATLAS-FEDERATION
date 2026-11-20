"""No original science manifests or canonical queue may be modified in v0.1."""
import hashlib,json,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class History(unittest.TestCase):
 def test_queue_30(self):
  q=json.loads((R/'DOMAIN_QUEUE.json').read_text());self.assertEqual(len(q['candidates']),30)
 def test_prior_node_count(self):
  a=json.loads((R/'common/registry.json').read_text());self.assertEqual(len(a['nodes']),24)
  prev=json.loads((R/'history/compiler_predecessor_database_v1.0.0_test_snapshot/common/registry.json').read_text());self.assertEqual(len(prev['nodes']),23)
  self.assertEqual([x for x in a['nodes'] if x['node_id']!='compiler-design-atlas'],prev['nodes'])
 def test_exact_prior_manifest(self):
  prior=R/'history/compiler_predecessor_database_v1.0.0_test_snapshot/common/nodes'
  for f in prior.rglob('*'):
   if f.is_file():
    now=R/'common/nodes'/f.relative_to(prior);self.assertEqual(hashlib.sha256(f.read_bytes()).hexdigest(),hashlib.sha256(now.read_bytes()).hexdigest())
