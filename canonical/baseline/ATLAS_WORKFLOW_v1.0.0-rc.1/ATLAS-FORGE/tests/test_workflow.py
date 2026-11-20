from pathlib import Path
import json,shutil,tempfile,unittest
from atlas_forge.workflow import gate_report,authorize_next_domain,subject_digest
from atlas_forge.common import ContractError,canonical,sha
from atlas_forge.core import init_atlas
ROOT=Path(__file__).resolve().parents[1]
class WorkflowTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);shutil.copytree(ROOT/'workflow',self.root/'workflow');(self.root/'src').mkdir();(self.root/'src/a.py').write_text('x=1')
  d={'schema':'atlas.gate-decisions/1','gates':{g:{'status':'not_run','evidence':[],'remaining':[]} for g in ['G1','G2','G3','G4','G5','G6','G7','G8']}}
  self.write(d)
 def tearDown(self):self.tmp.cleanup()
 def write(self,d):(self.root/'workflow/gate_decisions.json').write_text(json.dumps(d))
 def decision(self):return json.loads((self.root/'workflow/gate_decisions.json').read_text())
 def test_default_no_promotion(self):self.assertFalse(gate_report(self.root)['v1_ready'])
 def test_next_domain_refused(self):
  with self.assertRaises(ContractError):authorize_next_domain(self.root,'causal-atlas')
 def test_active_domain_allowed(self):self.assertTrue(authorize_next_domain(self.root,'measurement-atlas')['allowed'])
 def test_legacy_generator_obeys_active_domain(self):
  with self.assertRaises(ValueError):init_atlas('causal',self.root)
 def test_pass_without_evidence_invalid(self):
  d=self.decision();d['gates']['G6']['status']='passed';self.write(d);r=gate_report(self.root);self.assertEqual(next(x for x in r['gates'] if x['gate']=='G6')['status'],'invalid')
 def test_missing_gate_rejected(self):
  d=self.decision();del d['gates']['G7'];self.write(d)
  with self.assertRaises(ContractError):gate_report(self.root)
 def test_subject_changes_with_source(self):
  before=subject_digest(self.root);(self.root/'src/a.py').write_text('x=2');self.assertNotEqual(before,subject_digest(self.root))
 def test_receipts_do_not_change_subject(self):
  before=subject_digest(self.root);(self.root/'docs/receipts').mkdir(parents=True);(self.root/'docs/receipts/x.json').write_text('{}');self.assertEqual(before,subject_digest(self.root))
 def test_fake_runtime_fixture_cannot_pass(self):
  self.add_receipt('G6','bitwork_live','test_fixture');r=gate_report(self.root);self.assertEqual(next(x for x in r['gates'] if x['gate']=='G6')['status'],'invalid')
 def test_wrong_kind_cannot_pass(self):
  self.add_receipt('G6','common_conformance','local_actual');r=gate_report(self.root);self.assertEqual(next(x for x in r['gates'] if x['gate']=='G6')['status'],'invalid')
 def test_valid_conformance_receipt(self):
  self.add_receipt('G4','common_conformance','local_actual');r=gate_report(self.root);self.assertEqual(next(x for x in r['gates'] if x['gate']=='G4')['status'],'passed');self.assertFalse(r['v1_ready'])
 def test_gate_invalidates_on_source_change(self):
  self.add_receipt('G4','common_conformance','local_actual');(self.root/'src/a.py').write_text('changed');r=gate_report(self.root);self.assertEqual(next(x for x in r['gates'] if x['gate']=='G4')['status'],'invalid')
 def test_evidence_tamper_rejected(self):
  self.add_receipt('G4','common_conformance','local_actual');(self.root/'docs/receipts/test.json').write_text('{}');r=gate_report(self.root);self.assertEqual(next(x for x in r['gates'] if x['gate']=='G4')['status'],'invalid')
 def add_receipt(self,gate,kind,execution):
  subject=subject_digest(self.root);p=self.root/'docs/receipts/test.json';p.parent.mkdir(parents=True,exist_ok=True)
  p.write_text(json.dumps({'kind':kind,'execution_kind':execution,'result':'passed','subject_sha256':subject}))
  d=self.decision();criteria=json.loads((self.root/'workflow/acceptance.json').read_text())
  d['gates'][gate]={'status':'passed','evidence':[{'path':'docs/receipts/test.json','sha256':sha(p.read_bytes())}],
     'subject_sha256':subject,'criteria_sha256':sha(canonical(criteria)),'reviewed_by':'unit-test fixture','reviewed_at':'2026-11-12','remaining':[]};self.write(d)
