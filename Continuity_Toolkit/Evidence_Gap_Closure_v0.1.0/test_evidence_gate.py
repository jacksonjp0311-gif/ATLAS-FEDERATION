import json,hashlib,sys,tempfile,unittest,os
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from atlas_evidence_gate import (canonical,sha,strict_json,safe_child,inspect_proposal,original_domain_plan,
                                 GATE_HOLD,GATE_INVALID,EvidenceError,_record)

class GateCase(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        r=Path(self.temp.name);self.root=r/'atlas';self.workspace=r/'evidence';self.workspace.mkdir();self.root.mkdir()
        node='fixture-atlas';folder=self.root/'common/nodes'/node;data=folder/'data';data.mkdir(parents=True)
        obj={'schema':'atlas.record/1','node_id':node,'record_id':node+':concept:one','original_id':'concept:one',
             'type':'concept','title':'Constructed fixture record','status':'active','content':{'text':'synthetic only'},'evidence':{'gaps':['not authenticated']},'sources':[]}
        obj['revision']=sha(canonical(obj));self.record=obj
        content=canonical(obj)+b'\n';(data/'concepts.jsonl').write_bytes(content)
        manifest={'schema':'atlas.node-manifest/1','node_id':node,'collections':{'concept':{'path':'data/concepts.jsonl','records':1,'sha256':sha(content)}}}
        raw=canonical(manifest)+b'\n';(folder/'atlas_manifest.json').write_bytes(raw)
        reg={'schema':'atlas.registry/1','nodes':[{'node_id':node,'manifest':'nodes/'+node+'/atlas_manifest.json','manifest_sha256':sha(raw)}]}
        rb=canonical(reg)+b'\n';(self.root/'common/registry.json').write_bytes(rb)
        (self.root/'common/registry.lock.json').write_bytes(canonical({'schema':'atlas.registry-lock/1','sha256':sha(rb)}))
        (self.workspace/'real.txt').write_text('constructed reference fixture')
        self.proposal={'schema':'atlas.external-evidence-proposal/1',
          'kind':'source_original','target':{'record_id':obj['record_id'],'revision':obj['revision']},
          'artifact':{'relative_path':'real.txt','sha256':sha((self.workspace/'real.txt').read_bytes())},
          'metadata':{'publisher_url':'https://example.test/sample','publication_edition':'sample-1',
             'source_locator':'page 1','rights_status':'unknown','acquisition_method':'local fixture'}}
    def inspect(self):return inspect_proposal(self.root,self.workspace,self.proposal)
    def test_valid_bytes_still_unverified(self):
        r=self.inspect();self.assertEqual(r['status'],GATE_HOLD)
        self.assertTrue(r['byte_integrity_verified']);self.assertFalse(r['original_publisher_authenticated'])
        self.assertFalse(r['external_scientific_review_accepted'])
    def test_wrong_digest_rejected(self):
        self.proposal['artifact']['sha256']='0'*64
        self.assertEqual(self.inspect()['status'],GATE_INVALID)
    def test_wrong_record_revision_rejected(self):
        self.proposal['target']['revision']='0'*64
        self.assertEqual(self.inspect()['status'],GATE_INVALID)
    def test_missing_record_rejected(self):
        self.proposal['target']['record_id']='fixture-atlas:concept:missing'
        self.assertEqual(self.inspect()['status'],GATE_INVALID)
    def test_unsupported_kind_refused(self):
        self.proposal['kind']='silicon_certified'
        self.assertEqual(self.inspect()['status'],GATE_INVALID)
    def test_missing_provenance_field_refused(self):
        self.proposal['metadata'].pop('publication_edition')
        self.assertEqual(self.inspect()['status'],GATE_INVALID)
    def test_unsupported_rights_approval_refused(self):
        self.proposal['metadata']['rights_status']='licensed_verified'
        self.assertEqual(self.inspect()['status'],GATE_INVALID)
    def test_no_empty_evidence(self):
        (self.workspace/'real.txt').write_bytes(b'')
        self.proposal['artifact']['sha256']=sha(b'')
        self.assertEqual(self.inspect()['status'],GATE_INVALID)
    def test_path_traversal_refused(self):
        self.proposal['artifact']['relative_path']='../another.txt'
        self.assertEqual(self.inspect()['status'],GATE_INVALID)
    def test_symlink_refused(self):
        symlink=self.workspace/'shortcut';symlink.symlink_to(self.workspace/'real.txt')
        self.proposal['artifact']['relative_path']='shortcut'
        self.assertEqual(self.inspect()['status'],GATE_INVALID)
    def test_nonfinite_json_refused(self):
        with self.assertRaises(EvidenceError):strict_json('{"foo":NaN}')
    def test_duplicate_json_key_refused(self):
        with self.assertRaises(EvidenceError):strict_json('{"x":1,"x":2}')
    def test_record_revision_validated(self):
        self.assertEqual(_record(self.root,self.record['record_id'],self.record['revision'])['title'],self.record['title'])
    def test_registry_integrity_enforced(self):
        (self.root/'common/registry.json').write_text('{}')
        self.assertEqual(self.inspect()['status'],GATE_INVALID)
    def test_measurement_metadata_not_certificate(self):
        self.proposal['kind']='physical_measurement'
        self.proposal['metadata']={'sample_identifier':'a','instrument_identifier':'b','calibration_reference':'c',
              'units':'V','measurement_uncertainty':0.002,'method':'synthetic'}
        r=self.inspect();self.assertEqual(r['status'],GATE_HOLD)
        self.assertFalse(r['physical_measurement_validated_by_lab'])
    def test_review_declaration_not_acceptance(self):
        self.proposal['kind']='independent_review'
        self.proposal['metadata']={'reviewer_identifier':'name','independence_declaration':'self-claimed',
             'review_scope':'fixture','conflicts_disclosed':False}
        r=self.inspect();self.assertEqual(r['status'],GATE_HOLD)
        self.assertFalse(r['external_scientific_review_accepted'])
    def test_negative_result_preserved(self):
        self.proposal['kind']='negative_result'
        self.proposal['metadata']={'failure_observation':'did not work','test_conditions':'fixture',
              'expected_result':'one','actual_result':'zero'}
        self.assertEqual(self.inspect()['status'],GATE_HOLD)
    def test_software_reproduction_not_science(self):
        self.proposal['kind']='software_reproduction'
        self.proposal['metadata']={'runtime_version':'3.11','test_command':'pytest fixture',
              'independent_implementation':'sample','input_fixture_digest':'deadbeef'}
        self.assertEqual(self.inspect()['status'],GATE_HOLD)
    def test_structured_queue_requires_original_digest(self):
        (self.root/'DOMAIN_QUEUE.json').write_text('{}')
        with self.assertRaises(EvidenceError):original_domain_plan(self.root)

class ActualAtlas(unittest.TestCase):
    def test_real_atlas_gap_count_if_supplied(self):
        root=os.environ.get('ATLAS_ROOT')
        if not root:self.skipTest('ATLAS_ROOT not specified: synthetic suite remains independently runnable')
        p=original_domain_plan(Path(root))
        self.assertEqual((p['original_queue_count'],p['represented_original_domain_count'],p['missing_original_domain_count']),(30,9,21))
        self.assertEqual(p['next_missing_original_priority']['node'],'bioelectric-atlas')
        self.assertEqual(len(p['additional_enabling_nodes']),6)

if __name__=='__main__':unittest.main()
