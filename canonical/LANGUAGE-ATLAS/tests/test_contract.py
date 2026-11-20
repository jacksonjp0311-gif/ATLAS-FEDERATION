"""Exact Atlas Common Contract, scientific status and manual continuity checks."""
import json,unittest,sys
from pathlib import Path
from importlib.resources import files
from language_atlas.cases import casebook
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision

class ExactReference(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s=AtlasStore(ROOT/'language_atlas/resources/common')
        cls.rs={r['record_id']:r for r in cls.s.export()}
    def test_new_node_counts(self):
        self.assertEqual(len(self.rs),224)
        self.assertEqual(len(self.s._relations),222)
        self.assertEqual(sum(r['type']=='source' for r in self.rs.values()),33)
    def test_node_version(self):
        self.assertEqual(self.s.discover()['nodes'][0]['software_version'],'0.2.0')
    def test_node_one_only(self):
        self.assertEqual(len(self.s.discover()['nodes']),1)
    def test_all_exact_revisions_and_scoped_sources(self):
        for rec in self.rs.values():
            self.assertEqual(rec['revision'],revision(rec))
            self.assertEqual(rec['node_id'],'language-atlas')
            self.assertTrue(rec['content']['limitations'])
            self.assertFalse(rec['provenance'].get('independent_scientific_review',False))
            for sr in rec['sources']:
                self.assertIn(sr['record_id'],self.rs)
                self.assertEqual(self.rs[sr['record_id']]['revision'],sr['revision'])
                self.assertEqual(self.rs[sr['record_id']]['type'],'source')
    def test_relations_exact(self):
        for rel in self.s._relations.values():
            self.assertEqual(rel['revision'],revision(rel))
            for side in ('from','to'):
                self.assertIn(rel[side]['record_id'],self.rs)
                self.assertEqual(rel[side]['revision'],self.rs[rel[side]['record_id']]['revision'])
    def test_contexts_qualifier_and_source_closure(self):
        for q in ['Unicode NFC NFKC compatibility information loss','phonology voicing minimal pair feature','cyk parsing ambiguity derivation','pragmatics implicature indirect request','language endangered documentation rights']:
            with self.subTest(q=q):
                p=self.s.assemble_context(q,node_ids=['language-atlas'])
                self.assertEqual(p['status'],'context_available')
                self.assertTrue(self.s.validate_context(p)['valid'])
    def test_manual_all_chapters(self):
        chapters=list((ROOT/'docs/chapters').glob('*.md'))
        self.assertEqual(len(chapters),50)
        guide=(ROOT/'docs/REFERENCE_GUIDE.md').read_text()
        for f in chapters:self.assertIn(f.name,guide)
        self.assertGreater(len((ROOT/'docs/DEPTH_MANUAL_v0.2.0.md').read_text().split()),23000)
        self.assertEqual(len(list((ROOT/'docs/investigations').glob('*.md'))),30)
    def test_primary_source_absence_explicit(self):
        for rec in self.rs.values():
            if rec['type']=='source':self.assertFalse(rec['provenance']['original_source_bytes_archived'])
    def test_cases_all_constructed(self):
        cb=casebook();self.assertEqual(cb['case_count'],19)
        self.assertTrue(all(c['data_origin']=='original_constructed_fixture' for c in cb['cases']))
        self.assertFalse(cb['real_multilingual_corpus_acquired'])
    def test_full_and_standalone_records_match(self):
        full=AtlasStore(ROOT.parent/'common')
        a={r['record_id']:r['revision'] for r in full.export() if r['node_id']=='language-atlas'}
        self.assertEqual(a,{x:xv['revision'] for x,xv in self.rs.items()})
        self.assertEqual(len(full.discover()['nodes']),9)
    def test_full_cross_links_only(self):
        full=AtlasStore(ROOT.parent/'common')
        all_language=[r for r in full._relations.values() if r['relation_id'].startswith('language-atlas:')]
        self.assertEqual(len(all_language),227)
        self.assertEqual(len(all_language)-len(self.s._relations),5)
    def test_no_language_content_commands(self):
        code=(ROOT/'language_atlas/models.py').read_text()
        for forbidden in ('import subprocess','import socket','import requests','os.system','eval(', 'exec('):
            self.assertNotIn(forbidden,code)

if __name__=='__main__':unittest.main()
