import copy,json,subprocess,sys,tempfile,unittest
from fractions import Fraction as F
from pathlib import Path
try:
    from atlas_forge.common import AtlasStore
except ImportError:
    AtlasStore = None
from causal_atlas.models import ModelError
from causal_atlas.quasi import bandwidth_sensitivity,fuzzy_local_ratio,wald_summary
from causal_atlas.quasi_cases import curved_rd_rows
R=Path(__file__).resolve().parents[1]

@unittest.skipIf(AtlasStore is None, 'Shared Forge runtime is needed for reference integration tests')
class QuasiReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.store=AtlasStore(R/'causal_atlas/resources/common')
        cls.records={r['record_id']:r for r in cls.store.export()}
    def test_all_previous_record_revisions_unchanged(self):
        old=json.loads((R/'evidence/retained_v0.2_record_revisions.json').read_text())
        self.assertEqual(len(old),73)
        for rid,rev in old.items():self.assertEqual(self.records[rid]['revision'],rev)
    def test_actual_inventory(self):
        x=json.loads((R/'evidence/record_inventory.json').read_text())
        self.assertEqual(x['total_records'],len(self.records));self.assertGreaterEqual(len(self.records),105)
        self.assertEqual(len(json.loads((R/'evidence/retained_v0.3_record_revisions.json').read_text())),105)
        self.assertGreaterEqual(sum(r['type']=='source' for r in self.records.values()),23)
        self.assertFalse(x['scientific_v1_accepted'])
    def test_twelve_substantive_chapters(self):
        paths=sorted((R/'docs/chapters').glob('*.md'));self.assertGreaterEqual(len(paths),12)
        for p in paths:self.assertGreater(len(p.read_text().split()),400,p.name)
    def test_six_investigations(self):
        paths=sorted((R/'docs/investigations').glob('*.md'));self.assertGreaterEqual(len(paths),6)
        for p in paths:self.assertGreater(len(p.read_text().split()),300,p.name)
    def test_six_blank_templates(self):
        self.assertEqual(len(list((R/'docs/templates').glob('*.md'))),6)
    def test_new_review_questions_are_visible_development_material(self):
        d=json.loads((R/'evaluations/quasi_review_v0.3.0.json').read_text())
        self.assertEqual(len(d['items']),16);self.assertFalse(d['held_out']);self.assertFalse(d['model_evaluation_run'])
        for r in d['items']:self.assertIn(r['expected_record_id'],self.records)
    def test_source_inspections_remain_scoped(self):
        rows=json.loads((R/'evidence/source_inspection_v0.3.0.json').read_text());self.assertEqual(len(rows),7)
        for row in rows:
            self.assertFalse(row['full_text_mirrored']);self.assertFalse(row['independent_review'])
            self.assertTrue(row['portion']);self.assertTrue(row['access']);self.assertIn(row['source_id'],self.records)
    def test_failed_visual_access_is_disclosed(self):
        rows=json.loads((R/'evidence/source_inspection_v0.3.0.json').read_text())
        s=next(x for x in rows if x['source_id'].endswith(':SS1997'))
        self.assertIn('503',s['access']);self.assertIn('No visual',s['access'])
    def test_indexed_abstracts_are_not_labeled_full_review(self):
        rows=json.loads((R/'evidence/source_inspection_v0.3.0.json').read_text())
        for key in ('GI2014','MC2007','IL2007'):
            row=next(x for x in rows if x['source_id'].endswith(':'+key))
            self.assertIn('abstract',(row['portion']+' '+row['access']).lower())
    def test_wald_context_retains_local_target_and_assumptions(self):
        p=self.store.assemble_context('binary instrument Wald ratio',limit=1)
        self.assertTrue(self.store.validate_context(p)['valid'])
        ids={r['record_id'] for r in p['payload']['records']}
        for key in ['iv-wald','iv-identification-conditions','iv-monotonicity','iv-late-target','iv-denominator-guard']:
            self.assertIn('causal-atlas:'+key,ids)
    def test_small_budget_drops_whole_wald_unit(self):
        p=self.store.assemble_context('binary instrument Wald ratio',limit=1,max_context_bytes=2048)
        self.assertTrue(self.store.validate_context(p)['valid']);self.assertEqual(p['status'],'budget_exhausted')
        self.assertEqual(p['payload']['records'],[]);self.assertTrue(p['exclusions'])
    def test_rd_context_reports_inference_boundary(self):
        p=self.store.assemble_context('regression discontinuity local linear')
        self.assertTrue(self.store.validate_context(p)['valid'])
        ids={r['record_id'] for r in p['payload']['records']}
        self.assertIn('causal-atlas:rd-inference-boundary',ids)
    def test_removed_qualifier_invalidates_context(self):
        p=self.store.assemble_context('binary instrument Wald ratio',limit=1)
        p['payload']['records']=[r for r in p['payload']['records'] if not r['record_id'].endswith(':iv-monotonicity')]
        self.assertFalse(self.store.validate_context(p)['valid'])
    def test_source_references_resolve_exactly(self):
        for r in self.records.values():
            for s in r['sources']:
                self.assertIn(s['record_id'],self.records);self.assertEqual(self.records[s['record_id']]['revision'],s['revision'])
    def test_invalid_cutoff_not_misreported_as_insufficient_support(self):
        with self.assertRaises(ModelError):
            bandwidth_sensitivity(curved_rd_rows(),cutoff='nan',bandwidths=[1,2],kernel='uniform',data_origin='synthetic_constructed')
    def test_unhashable_origin_is_domain_error(self):
        with self.assertRaises(ModelError):
            wald_summary(y_z0=0,y_z1=1,d_z0=0,d_z1=1,minimum_first_stage=0,data_origin=[])
    def test_fuzzy_boundary_not_silently_clipped(self):
        rows=[dict(id=str(i),x=x,y=0,d=int(i==0)) for i,x in enumerate([-3,-2,-1,0,1,2])]
        r=fuzzy_local_ratio(rows,cutoff=0,bandwidth=4,kernel='uniform',minimum_first_stage=0,data_origin='synthetic_constructed')
        self.assertTrue(r['treatment_boundary_estimates_outside_unit_interval'])
        self.assertLess(F(r['treatment_fit']['sides']['left']['intercept_at_cutoff']),0)
    def test_example_command_inputs_are_executable(self):
        for command,file in [('wald','iv_wald.json'),('iv-population','iv_training_types.json'),('iv-sensitivity','iv_exclusion_sensitivity.json'),('rd','sharp_rd.json'),('fuzzy-rd','fuzzy_rd.json'),('rd-bandwidths','rd_bandwidths.json')]:
            with self.subTest(command=command):
                p=subprocess.run([sys.executable,'-m','causal_atlas',command,str(R/'examples'/file)],capture_output=True,text=True)
                self.assertEqual(p.returncode,0,p.stderr);self.assertIsInstance(json.loads(p.stdout),dict)
    def test_duplicate_cli_keys_refused(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'bad.json';p.write_text('{"cutoff":0,"cutoff":1}')
            r=subprocess.run([sys.executable,'-m','causal_atlas','rd',str(p)],capture_output=True,text=True)
            self.assertEqual(r.returncode,2);self.assertIn('Duplicate',json.loads(r.stderr)['error'])

if __name__=='__main__':unittest.main()
