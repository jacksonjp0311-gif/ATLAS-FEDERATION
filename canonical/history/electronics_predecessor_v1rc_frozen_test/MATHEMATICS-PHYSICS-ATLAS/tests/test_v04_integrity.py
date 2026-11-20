"""v0.4 exact-revision, history, source-closure and scope checks."""
import hashlib,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];COL=ROOT.parent
sys.path.insert(0,str(COL/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision
from math_physics_atlas.v04_cases import casebook_v04
class V04Integrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local=AtlasStore(ROOT/'math_physics_atlas/resources/common')
        cls.full=AtlasStore(COL/'common')
        cls.records={x['record_id']:x for x in cls.local.export()}
    def test_federation_counts(self):
        fed=self.full.discover()
        self.assertEqual((len(fed['nodes']),fed['records'],fed['relations']),(12,2581,1735))
        local=self.local.discover()
        self.assertEqual((len(local['nodes']),local['records'],local['relations']),(1,224,208))
    def test_old_v03_exact_record_and_relation_prefix(self):
        old=COL/'history/math_physics_v0.3.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS/data'
        for cat in ('concepts','claims','equations','methods','datasets','reviews','sources','relations'):
            with self.subTest(cat=cat):
                self.assertTrue((ROOT/'data'/f'{cat}.jsonl').read_bytes().startswith((old/f'{cat}.jsonl').read_bytes()))
    def test_historical_v03_tests_original_bytes(self):
        prev=COL/'history/math_physics_v0.3.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS'
        manifest=json.loads((prev/'FILE_MANIFEST.json').read_text())['files']
        for t in ('test_integrity.py','test_models.py','test_v02_models.py','test_v03_models.py','test_v03_integrity.py'):
            path=prev/'tests'/t
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),manifest['tests/'+t])
    def test_chapter_count_and_refs(self):
        self.assertEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),52)
        self.assertEqual(len(json.loads((ROOT/'evidence/chapter_index.json').read_text())),52)
        self.assertEqual(casebook_v04()['count'],6)
    def test_revision_and_exact_source_closure(self):
        for row in self.records.values():
            self.assertEqual(row['revision'],revision(row))
            for src in row['sources']:
                self.assertEqual(self.records[src['record_id']]['revision'],src['revision'])
        for rel in self.local._relations.values():
            self.assertEqual(rel['revision'],revision(rel))
            for side in ('from','to'):
                self.assertEqual(self.records[rel[side]['record_id']]['revision'],rel[side]['revision'])
    def test_new_source_linked_contexts(self):
        for q in ('harmonic 2D dielectric electrostatics conservative Poisson',
                  'matrix free preconditioned conjugate gradient SPD true residual',
                  'manufactured sine convergence spatial discretization',
                  'dielectric interface CODATA vacuum permittivity semiconductor'):
            p=self.local.assemble_context(q,node_ids=['mathematics-physics-atlas'])
            self.assertTrue(self.local.validate_context(p)['valid'])
            self.assertNotIn(p['status'],('evidence_unavailable','no_match'))
    def test_no_primary_source_or_accepted_science(self):
        self.assertEqual(sum(row['type']=='source' for row in self.records.values()),14)
        self.assertFalse(any(row.get('provenance',{}).get('primary_source_bytes_archived') for row in self.records.values()))
        self.assertFalse(any(row['evidence']['review_status']=='independently_reproduced' for row in self.records.values()))
        self.assertFalse(json.loads((COL/'BUILD_POLICY.json').read_text())['Bitwork_router_changes'])
    def test_model_no_network_and_no_dynamic_execution(self):
        model=(ROOT/'math_physics_atlas/v04_models.py').read_text()
        for bad in ('import requests','import socket','os.system(','subprocess','eval(','exec('):
            self.assertNotIn(bad,model)
if __name__=='__main__':unittest.main()
