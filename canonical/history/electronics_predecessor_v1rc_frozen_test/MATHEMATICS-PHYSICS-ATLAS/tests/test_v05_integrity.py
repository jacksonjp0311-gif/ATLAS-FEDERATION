"""v0.5 additive exact revision, frozen prior release and source-status checks."""
import hashlib,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];COL=ROOT.parent
sys.path.insert(0,str(COL/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision
from math_physics_atlas.v05_cases import casebook_v05
class V05Integrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local=AtlasStore(ROOT/'math_physics_atlas/resources/common')
        cls.full=AtlasStore(COL/'common')
        cls.records={r['record_id']:r for r in cls.local.export()}
    def test_federation_inventory(self):
        a=self.full.discover(); self.assertEqual((len(a['nodes']),a['records'],a['relations']),(12,2599,1750))
        b=self.local.discover();self.assertEqual((len(b['nodes']),b['records'],b['relations']),(1,242,223))
    def test_exact_previous_data_prefix(self):
        prev=COL/'history/math_physics_v0.4.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS/data'
        for cat in ('concepts','claims','equations','methods','datasets','reviews','sources','relations'):
            with self.subTest(cat=cat):
                self.assertTrue((ROOT/'data'/f'{cat}.jsonl').read_bytes().startswith((prev/f'{cat}.jsonl').read_bytes()))
    def test_federated_previous_cross_links_preserved(self):
        root=COL/'common/nodes/mathematics-physics-atlas/data/relations.jsonl'
        full=[json.loads(x) for x in root.read_text().splitlines()]
        self.assertEqual(len(full),231)
        self.assertEqual(len({r['relation_id'] for r in full}),231)
        self.assertEqual(len([r for r in full if r['relation_id'].split(':')[1].startswith('v05-')]),15)
        old=COL/'history/math_physics_v0.4.0_test_snapshot/common/nodes/mathematics-physics-atlas/data/relations.jsonl'
        self.assertTrue(root.read_bytes().startswith(old.read_bytes()))
    def test_original_frozen_prior_v04_test_bytes(self):
        prev=COL/'history/math_physics_v0.4.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS'
        inventory=json.loads((prev/'FILE_MANIFEST.json').read_text())['files']
        for t in ('test_v04_models.py','test_v04_integrity.py'):
            self.assertEqual(hashlib.sha256((prev/'tests'/t).read_bytes()).hexdigest(),inventory['tests/'+t])
    def test_revisions_and_source_closure(self):
        for r in self.records.values():
            self.assertEqual(r['revision'],revision(r))
            for s in r['sources']:
                self.assertEqual(self.records[s['record_id']]['revision'],s['revision'])
        for rel in self.local._relations.values():
            self.assertEqual(rel['revision'],revision(rel))
            for k in ('from','to'):
                self.assertEqual(rel[k]['revision'],self.records[rel[k]['record_id']]['revision'])
    def test_contexts(self):
        for q in ('nonlinear elliptic equilibrium damped Newton sinh',
                  'thermal voltage Boltzmann dimensionless Poisson carriers',
                  'Scharfetter Gummel Bernoulli exponential flux',
                  'manufactured solution nonlinear residual spatial truncation'):
            p=self.local.assemble_context(q,node_ids=['mathematics-physics-atlas'])
            self.assertTrue(self.local.validate_context(p)['valid'])
            self.assertNotIn(p['status'],('no_match','evidence_unavailable'))
    def test_chapters_cases(self):
        self.assertEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),56)
        self.assertEqual(len(json.loads((ROOT/'evidence/chapter_index.json').read_text())),56)
        self.assertEqual(casebook_v05()['count'],6);self.assertEqual(casebook_v05()['status'],'passed')
    def test_evidence_gates_and_router_deferral(self):
        self.assertEqual(sum(r['type']=='source' for r in self.records.values()),16)
        self.assertFalse(any(r['provenance'].get('primary_source_bytes_archived',False) for r in self.records.values()))
        self.assertFalse(any(r['evidence']['review_status']=='independently_reproduced' for r in self.records.values()))
        self.assertFalse(json.loads((COL/'BUILD_POLICY.json').read_text())['Bitwork_router_changes'])
    def test_invalid_execution_paths_absent(self):
        source=(ROOT/'math_physics_atlas/v05_models.py').read_text()
        for bad in ('import requests','import socket','os.system(', 'subprocess', 'eval(', 'exec('):
            self.assertNotIn(bad,source)
if __name__=='__main__':unittest.main()
