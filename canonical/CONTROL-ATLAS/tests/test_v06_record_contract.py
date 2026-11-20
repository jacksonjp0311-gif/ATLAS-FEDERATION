import json,unittest
from pathlib import Path
from atlas_forge.common import AtlasStore
from control_atlas.output_feedback_cases import casebook
R=Path(__file__).resolve().parents[1]

class ContentV06(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.store=AtlasStore(R/'control_atlas/resources/common')
        cls.recs={r['record_id']:r for r in cls.store.export()}
    def test_inventory_exact(self):
        self.assertGreaterEqual(len(self.recs),214)
        self.assertGreaterEqual(sum(r['type']=='source' for r in self.recs.values()),45)
        self.assertGreaterEqual(len(self.store._relations),124)
        self.assertEqual(sum(r['provenance'].get('edition_added')=='0.6.0' for r in self.recs.values()),23)
        self.assertGreaterEqual(self.store.discover()['records'],214)
    def test_old_v05_revisions_exact(self):
        old=json.loads((R/'evidence/old_control_v0.5_revisions.json').read_text())['records']
        self.assertEqual(len(old),191)
        for k,v in old.items():self.assertEqual(self.recs[k]['revision'],v,k)
    def test_old_v05_relations_exact(self):
        old=json.loads((R/'evidence/old_control_v0.5_relations.json').read_text())['relations']
        self.assertEqual(len(old),107)
        for k,v in old.items():self.assertEqual(self.store._relations[k]['revision'],v,k)
    def test_links_ref_and_limited_source_scope(self):
        for r in self.recs.values():
            for link in r['sources']:
                self.assertEqual(link['revision'],self.recs[link['record_id']]['revision'])
                self.assertEqual(self.recs[link['record_id']]['type'],'source')
            if r['provenance'].get('edition_added')=='0.6.0':
                self.assertFalse(r['provenance']['independent_review'])
                self.assertTrue(r['content']['limitations'])
    def test_new_sources_limited(self):
        ss=[r for r in self.recs.values() if r['type']=='source' and r['provenance'].get('edition_added')=='0.6.0']
        self.assertEqual(len(ss),3)
        for r in ss:
            self.assertIn('abstract',r['provenance']['inspected_scope'].lower())
            self.assertFalse(r['provenance']['source_bytes_archived'])
    def test_exact_qualifier_context(self):
        for q in ['bounded scalar observer error noise','actuator rate lag saturation','finite horizon output feedback reachable tube','measurement consistency fault ambiguity']:
            with self.subTest(q=q):
                p=self.store.assemble_context(q,node_ids=['control-atlas'])
                self.assertEqual(p['status'],'context_available',q)
                self.assertTrue(self.store.validate_context(p)['valid'])
    def test_complete_reference_and_links(self):
        chapters=list((R/'docs/chapters').glob('*.md')); inv=list((R/'docs/investigations').glob('*.md'))
        self.assertGreaterEqual(len(chapters),52);self.assertGreaterEqual(len(inv),42)
        guide=(R/'docs/REFERENCE_GUIDE.md').read_text()
        for p in chapters+inv:
            with self.subTest(f=p.name):self.assertIn(p.name,guide)
    def test_new_casebook(self):
        self.assertEqual(casebook()['count'],12)
        self.assertEqual(casebook()['result'],'passed')
        self.assertEqual(casebook()['real_hardware_tests'],0)
    def test_package_no_actuation(self):
        import control_atlas.output_feedback as module
        self.assertFalse(hasattr(module,'connect_plc'))
        self.assertFalse(hasattr(module,'command_actuator'))
        self.assertIn('30 domain', (R/'README.md').read_text())

if __name__=='__main__':unittest.main()
