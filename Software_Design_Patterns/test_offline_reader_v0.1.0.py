"""Current 17-node offline reader acceptance; 16-node fixtures remain frozen."""
import json,pathlib,unittest
from tools.atlas_offline import Atlas
R=pathlib.Path(__file__).resolve().parents[1]

class TestPatternsSurvival(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.a=Atlas(R)
    def test_seventeen_nodes(self):self.assertEqual(self.a.catalog()['nodes'],17)
    def test_exact_counts(self):
        c=self.a.catalog();self.assertEqual((c['records'],c['relationships']),(3419,2599))
    def test_source_cards(self):self.assertEqual(self.a.gaps()['bibliographic_source_records_total'],563)
    def test_search_sqlite_recovery(self):
        self.assertGreater(self.a.search('SQLite command journal idempotent',node='software-design-patterns-atlas')['matches_total'],0)
    def test_exact_revision_record(self):
        p=self.a.record('software-design-patterns-atlas:chapter-15-concept')['record']
        self.assertEqual(p['node_id'],'software-design-patterns-atlas');self.assertTrue(p['revision'])
    def test_relationship_context(self):
        x=self.a.trace('software-design-patterns-atlas:chapter-24-method',depth=2)
        self.assertGreaterEqual(len(x['records']),2)
    def test_original_queue_unchanged(self):
        q=json.loads((R/'DOMAIN_QUEUE.json').read_text())
        self.assertEqual(len(q['candidates']),30)
        self.assertEqual(next(x for x in q['candidates'] if x['node_id']=='software-design-patterns-atlas')['priority'],11)
    def test_new_manual(self):
        x=self.a.manuals()['items']
        self.assertTrue(any(z['domain']=='SOFTWARE-DESIGN-PATTERNS-ATLAS' for z in x))
    def test_all_17_node_manifests(self):
        self.assertEqual(self.a.verify(all_files=False)['node_manifest_hashes_verified'],17)
    def test_offline_portal_present(self):
        p=R/'SURVIVAL/ATLAS_SOFTWARE_PATTERNS_PORTAL_v0.1.0.html'
        self.assertIn('Software Design Patterns v0.1.0',p.read_text())

if __name__=='__main__':unittest.main()
