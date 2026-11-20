"""Exact source/identity tests; passing does not establish agent capability."""
import unittest,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
FORGE=R.parent/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'
sys.path.insert(0,str(FORGE))
from atlas_forge.common import AtlasStore,revision

class ReferenceIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.store=AtlasStore(R/'agent_atlas/resources/common')
        cls.recs={r['record_id']:r for r in cls.store.export()}
    def test_record_count_and_provenance(self):
        self.assertGreaterEqual(len(self.recs),100)
        self.assertGreaterEqual(sum(r['type']=='source' for r in self.recs.values()),22)
        self.assertGreaterEqual(len(self.store._relations),63)
        self.assertGreaterEqual(sum(r['type']=='concept' for r in self.recs.values()),42)
    def test_all_exact_revisions(self):
        for r in self.recs.values():
            self.assertEqual(r['revision'],revision(r))
            self.assertEqual(r['node_id'],'agent-atlas')
            for s in r['sources']:
                self.assertEqual(s['revision'],self.recs[s['record_id']]['revision'])
                self.assertEqual(self.recs[s['record_id']]['type'],'source')
    def test_edges_exact(self):
        for rel in self.store._relations.values():
            self.assertEqual(rel['revision'],revision(rel))
            for k in ['from','to']:
                self.assertEqual(rel[k]['revision'],self.recs[rel[k]['record_id']]['revision'])
    def test_no_experiment_fabricated(self):
        for r in self.recs.values():
            self.assertFalse(r['provenance']['independent_review'])
            self.assertTrue(r['content']['limitations'])
            self.assertNotIn(r['evidence']['review_status'],['human_reviewed','independently_reproduced'])
        for r in self.recs.values():
            if r['type']=='source':self.assertFalse(r['provenance']['source_bytes_archived'])
    def test_context_qualifiers(self):
        for query in ['tool error operator stop terminal final commit','agent task graph dependencies budget','pass all repeated benchmark','memory reflection provenance','prompt injection host tool consent','worker receipt parent resume']:
            with self.subTest(query=query):
                p=self.store.assemble_context(query,node_ids=['agent-atlas'])
                self.assertEqual(p['status'],'context_available')
                self.assertTrue(self.store.validate_context(p)['valid'])
    def test_minimal_budget_integrity(self):
        p=self.store.assemble_context('worker audit task',node_ids=['agent-atlas'],max_context_bytes=512)
        self.assertTrue(self.store.validate_context(p)['valid'])
    def test_docs_complete(self):
        chapters=list((R/'docs/chapters').glob('*.md'));cases=list((R/'docs/investigations').glob('*.md'))
        self.assertGreaterEqual(len(chapters),22);self.assertGreaterEqual(len(cases),12)
        guide=(R/'docs/REFERENCE_GUIDE.md').read_text()
        for p in chapters+cases:self.assertIn(p.name,guide)
        self.assertIn('30', (R/'README.md').read_text())
        self.assertIn('not a live', (R/'README.md').read_text().lower())
    def test_no_live_api(self):
        from agent_atlas import models
        self.assertFalse(hasattr(models,'call_llm'))
        self.assertFalse(hasattr(models,'connect_tools'))
    def test_single_node_and_full_node_parity(self):
        root=R.parent/'common/nodes/agent-atlas';single=R/'agent_atlas/resources/common/nodes/agent-atlas'
        for path in single.rglob('*'):
            if path.is_file():self.assertEqual(path.read_bytes(),(root/path.relative_to(single)).read_bytes())

if __name__=='__main__':unittest.main()
