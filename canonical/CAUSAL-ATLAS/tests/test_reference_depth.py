import json,re,unittest
from pathlib import Path
try:
    from atlas_forge.common import AtlasStore
except ImportError:
    AtlasStore = None
R=Path(__file__).resolve().parents[1]
@unittest.skipIf(AtlasStore is None, 'Shared Forge runtime is needed for reference integration tests')
class DepthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.store=AtlasStore(R/'causal_atlas/resources/common');cls.records={x['record_id']:x for x in cls.store.export()}
    def test_old_revisions_preserved(self):
        old=json.loads((R/'evidence/retained_v0.1_record_revisions.json').read_text())
        # The file is a direct record_id to revision mapping.
        for rid,rev in old.items():self.assertEqual(self.records[rid]['revision'],rev)
    def test_inventory_matches(self):
        meta=json.loads((R/'evidence/record_inventory.json').read_text());self.assertEqual(meta['total_records'],len(self.records))
    def test_new_sources_have_inspected_scope(self):
        for r in self.records.values():
            if r['type']=='source' and r['provenance'].get('edition_added')=='0.2.0':
                self.assertTrue(r['provenance']['inspected_scope']);self.assertFalse(r['provenance']['source_bytes_archived'])
    def test_source_closure(self):
        for r in self.records.values():
            for s in r['sources']:self.assertEqual(self.records[s['record_id']]['revision'],s['revision'])
    def test_no_independent_review_invented(self):
        for r in self.records.values():self.assertNotIn(r['evidence']['review_status'],['human_reviewed','independently_reproduced'])
    def test_eight_substantive_chapters(self):
        chapters=list((R/'docs/chapters').glob('*.md'));self.assertGreaterEqual(len(chapters),8)
        for p in chapters:self.assertGreater(len(p.read_text().split()),400)
    def test_three_substantive_investigations(self):
        paths=list((R/'docs/investigations').glob('*.md'));self.assertGreaterEqual(len(paths),3)
        for p in paths:self.assertGreater(len(p.read_text().split()),300)
    def test_rubrics_do_not_claim_heldout(self):
        d=json.loads((R/'evaluations/depth_review_v0.2.0.json').read_text());self.assertEqual(len(d['items']),20)
        self.assertFalse(d['held_out']);self.assertFalse(d['model_evaluation_run'])
        for q in d['items']:self.assertIn(q['expected_record_id'],self.records)
    def test_no_missing_local_document_links(self):
        # Inspect generated nonhistorical reference Markdown, not immutable old snapshots.
        paths=[R/'README.md',R/'docs/REFERENCE_GUIDE.md',* (R/'docs/chapters').glob('*.md'),*(R/'docs/investigations').glob('*.md')]
        for p in paths:
            for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
                if not re.match(r'^(https?:|#)',target):self.assertTrue((p.parent/target.split('#')[0]).exists(),f'{p}: {target}')
    def test_supported_queries_return_context(self):
        for q in ['augmented weighting','missing outcomes bounds','weight concentration','time zero','trend sensitivity']:
            c=self.store.assemble_context(q);self.assertTrue(self.store.validate_context(c)['valid']);self.assertNotEqual(c['status'],'no_match')
if __name__=='__main__':unittest.main()
