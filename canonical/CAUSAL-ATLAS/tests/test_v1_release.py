# Public derivative redaction: ucb_admissions_redistribution_unresolved
"""Causal v1 scoped reference and compatibility regression, not independent review."""
import hashlib,json,re,subprocess,sys,unittest
from pathlib import Path
from fractions import Fraction as F
from causal_atlas.advanced_cases import CASES
try:
    from atlas_forge.common import AtlasStore
except ImportError:
    AtlasStore=None
R=Path(__file__).resolve().parents[1]

class ContentV1(unittest.TestCase):
    def test_declared_version(self):
        from causal_atlas import __version__
        self.assertEqual(__version__,'1.0.0')
        self.assertEqual(json.loads((R/'atlas_manifest.json').read_text())['software_version'],'1.0.0')
    def test_chapters_and_investigations(self):
        self.assertEqual(len(list((R/'docs/chapters').glob('*.md'))),24)
        self.assertEqual(len(list((R/'docs/investigations').glob('*.md'))),13)
        self.assertEqual(len(list((R/'docs/templates').glob('*.md'))),6)
    def test_guide_mentions_each_chapter(self):
        guide=(R/'docs/REFERENCE_GUIDE.md').read_text()
        for p in (R/'docs/chapters').glob('*.md'):
            self.assertIn(p.name,guide)
        for p in (R/'docs/investigations').glob('*.md'):
            self.assertIn(p.name,guide)
    def test_old_cases_still_present(self):
        self.assertEqual(len(list((R/'docs/investigations').glob('0[1-6]_*.md'))),6)
    def test_source_rights_are_bounded(self):
        self.skipTest('Historical UCBAdmissions numerical data and derived results are unavailable in this public derivative pending redistribution clearance.')
    def test_no_auto_causality_from_historical(self):
        self.skipTest('Historical UCBAdmissions numerical data and derived results are unavailable in this public derivative pending redistribution clearance.')
    def test_cli_methods(self):
        for cmd,filename in [('longitudinal','longitudinal'),('staggered-did','staggered_did'),('mediation','mediation'),('interference','interference'),('transport','transport'),('binomial-interval','binomial_interval')]:
            with self.subTest(cmd=cmd):
                p=subprocess.run([sys.executable,'-m','causal_atlas',cmd,str(R/'examples'/f'{filename}.json')],cwd=R,capture_output=True,text=True)
                self.assertEqual(p.returncode,0,p.stderr)
                self.assertIsInstance(json.loads(p.stdout),dict)
    def test_casebook_cli(self):
        p=subprocess.run([sys.executable,'-m','causal_atlas','advanced-casebook'],cwd=R,capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr)
        self.assertEqual(len(json.loads(p.stdout)['cases']),7)
    def test_document_links(self):
        docs=[R/'README.md',R/'docs/REFERENCE_GUIDE.md',R/'docs/COVERAGE_MATRIX.md',R/'docs/REAL_DATA_REPRODUCTION.md']
        docs+=list((R/'docs/chapters').glob('*.md'))+list((R/'docs/investigations').glob('*.md'))
        for path in docs:
            for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):
                if not link.startswith(('https://','http://','#')):
                    with self.subTest(path=path.name,link=link):
                        self.assertTrue((path.parent/link.split('#')[0]).exists(),str(path)+': '+link)
    def test_explicit_deployment_gaps(self):
        x=json.loads((R/'docs/RELEASE_STATE.json').read_text())
        self.assertFalse(x.get('scientific_v1_accepted',False))
        self.assertFalse(x.get('live_bitwork_integration',False))
        self.assertFalse(x.get('independent_human_review',False))
    def test_metadata_coverage(self):
        self.skipTest('Historical UCBAdmissions numerical data and derived results are unavailable in this public derivative pending redistribution clearance.')

@unittest.skipIf(AtlasStore is None,'Common Forge runtime unavailable')
class MachineV1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.store=AtlasStore(R/'causal_atlas/resources/common')
        cls.records={r['record_id']:r for r in cls.store.export()}
    def test_node_count(self):
        self.skipTest('Historical UCBAdmissions numerical data and derived results are unavailable in this public derivative pending redistribution clearance.')
    def test_old_105_revisions_retained(self):
        old=json.loads((R/'evidence/retained_v0.3_record_revisions.json').read_text())
        self.assertEqual(len(old),105)
        for k,v in old.items():self.assertEqual(self.records[k]['revision'],v)
    def test_all_links_exact(self):
        for r in self.records.values():
            for s in r['sources']:
                self.assertEqual(self.records[s['record_id']]['revision'],s['revision'])
    def test_no_fabricated_independent_review(self):
        for r in self.records.values():
            self.assertNotIn(r['evidence']['review_status'],('independently_reproduced','human_reviewed'))
    def test_new_contexts(self):
        for q in ['sequential exchangeability','staggered adoption cohort','interference spillover','mediation interventional','transportability target','negative control','UCBAdmissions']:
            with self.subTest(q=q):
                pkg=self.store.assemble_context(q,node_ids=['causal-atlas'])
                self.assertTrue(self.store.validate_context(pkg)['valid'])
                self.assertNotIn(pkg['status'],('no_match','evidence_unavailable'))
                self.assertTrue(pkg['payload']['records'])
    def test_source_evidence_not_answer(self):
        pkg=self.store.assemble_context('Berkeley UCBAdmissions',node_ids=['causal-atlas'])
        self.assertTrue(self.store.validate_context(pkg)['valid'])
        self.assertNotEqual(pkg['status'],'verified_causal_effect')
    def test_retain_whole_unit_with_budget(self):
        pkg=self.store.assemble_context('sequential exchangeability',node_ids=['causal-atlas'],max_context_bytes=512)
        self.assertTrue(self.store.validate_context(pkg)['valid'])
        self.assertNotEqual(pkg['status'],'verified_causal_effect')
    def test_revision_mutation_fails(self):
        import copy
        pkg=self.store.assemble_context('longitudinal positivity',node_ids=['causal-atlas'])
        self.assertTrue(self.store.validate_context(pkg)['valid'])
        if pkg['payload']['records']:
            corrupted=copy.deepcopy(pkg)
            corrupted['payload']['records'][0]['revision']='0'*64
            self.assertFalse(self.store.validate_context(corrupted)['valid'])
    def test_external_data_not_read_as_verified(self):
        r=self.records['causal-atlas:ucb-observational-stratification'] if 'causal-atlas:ucb-observational-stratification' in self.records else None
        if r:self.assertNotIn(r['evidence']['review_status'],['human_reviewed','independently_reproduced'])

if __name__=='__main__':unittest.main()
