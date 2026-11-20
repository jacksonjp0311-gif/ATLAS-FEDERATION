"""v0.3 new assertions; original v0.1/v0.2 release tests remain in exact frozen snapshots."""
import json
import hashlib
from pathlib import Path
import unittest,sys
ROOT=Path(__file__).resolve().parents[1];COL=ROOT.parent
sys.path.insert(0,str(COL/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision
from math_physics_atlas.v03_cases import casebook_v03

class V03Integrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local=AtlasStore(ROOT/'math_physics_atlas/resources/common')
        cls.full=AtlasStore(COL/'common')
        cls.records={x['record_id']:x for x in cls.local.export()}

    def test_federation_inventory(self):
        a=self.full.discover()
        self.assertEqual((len(a['nodes']),a['records'],a['relations']),(12,2581,1735))
        a=self.local.discover()
        self.assertEqual((len(a['nodes']),a['records'],a['relations']),(1,224,208))

    def test_frozen_prefix_data_all_categories(self):
        previous=COL/'history/math_physics_v0.2.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS/data'
        for name in ('concepts','claims','equations','methods','datasets','reviews','sources','relations'):
            with self.subTest(name=name):
                self.assertTrue((ROOT/'data'/f'{name}.jsonl').read_bytes().startswith((previous/f'{name}.jsonl').read_bytes()))

    def test_old_test_suite_byte_identical(self):
        previous=COL/'history/math_physics_v0.2.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS/tests'
        for name in ('test_models.py','test_v02_models.py'):
            with self.subTest(name=name):
                self.assertEqual((ROOT/'tests'/name).read_bytes(),(previous/name).read_bytes())

        # The v0.2 integrity suite itself is preserved in the historical
        # snapshot and checked against its original v0.2 FILE_MANIFEST hash;
        # current tests/test_integrity.py was versioned to the new inventory.
        old_manifest=json.loads((COL/'history/math_physics_v0.2.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS/FILE_MANIFEST.json').read_text())
        old_bytes=(previous/'test_integrity.py').read_bytes()
        self.assertEqual(hashlib.sha256(old_bytes).hexdigest(),old_manifest['files']['tests/test_integrity.py'])

    def test_immutable_revisions(self):
        for record in self.records.values():
            self.assertEqual(record['revision'],revision(record))
            for src in record['sources']:
                self.assertEqual(src['revision'],self.records[src['record_id']]['revision'])
        for rel in self.local._relations.values():
            self.assertEqual(rel['revision'],revision(rel))
            for key in ('from','to'):
                self.assertEqual(rel[key]['revision'],self.records[rel[key]['record_id']]['revision'])

    def test_chapters_and_casebooks(self):
        self.assertEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),52)
        self.assertEqual(casebook_v03()['count'],4)
        self.assertEqual(len(json.loads((ROOT/'evidence/chapter_index.json').read_text())),52)

    def test_sources_scientific_limit(self):
        sources=[r for r in self.records.values() if r['type']=='source']
        self.assertEqual(len(sources),14)
        for s in sources:
            self.assertIs(s['provenance'].get('primary_source_bytes_archived'),False)
        self.assertFalse(any(r['evidence']['review_status']=='independently_reproduced' for r in self.records.values()))

    def test_new_contexts_source_closed(self):
        for question in ('Jacobi rectangular SVD orthogonal rank diagnostic',
                         'pseudoinverse minimum norm least squares',
                         'Poisson electrostatics charge Gauss finite difference',
                         'backward Euler Crank Nicolson diffusion stiffness'):
            with self.subTest(question=question):
                p=self.local.assemble_context(question,node_ids=['mathematics-physics-atlas'])
                self.assertTrue(self.local.validate_context(p)['valid'])
                self.assertNotIn(p['status'],('no_match','evidence_unavailable'))

    def test_no_unintended_router(self):
        p=(ROOT/'math_physics_atlas/v03_models.py').read_text()
        for forbidden in ('import requests','import socket','import subprocess','os.system(','eval(','exec('):
            self.assertNotIn(forbidden,p)
        self.assertFalse(json.loads((COL/'BUILD_POLICY.json').read_text())['Bitwork_router_changes'])

if __name__=='__main__':unittest.main()
