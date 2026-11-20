import json
import tempfile
import unittest
from pathlib import Path
from atlas_forge.core import init_atlas, validate, query, rank_domains, packet_sha256, check_packet, make_packet

class ForgeTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.path=init_atlas("measurement",self.tmp.name)
    def tearDown(self): self.tmp.cleanup()
    def test_rank_has_ten_distinct(self):
        x=rank_domains();self.assertEqual(len(x),10);self.assertEqual(len({d['slug'] for d in x}),10)
    def test_scaffold_valid(self):self.assertTrue(validate(self.path)['valid'])
    def test_empty_query_abstains(self):self.assertEqual(query(self.path,"what is the uncertainty")['status'],"unresolved")
    def test_does_not_overwrite(self):
        with self.assertRaises(FileExistsError):init_atlas("measurement",self.tmp.name)
    def test_invalid_domain_rejected(self):
        with self.assertRaises(ValueError):init_atlas("invented",self.tmp.name)
    def test_manifest_count_tamper(self):
        p=self.path/'atlas_manifest.json';m=json.loads(p.read_text());m['packet_count']=9;p.write_text(json.dumps(m));self.assertFalse(validate(self.path)['valid'])
    def test_missing_source_registry_fails(self):
        (self.path/'data'/'sources.json').unlink();self.assertFalse(validate(self.path)['valid'])
    def test_hash_detects_changed_claim(self):
        p=self.make_pkt();p['claim']='rewritten';self.assertIn('content_sha256 mismatch',check_packet(p,{'nist'}))
    def test_synthetic_cannot_claim_reproduced(self):
        p=self.make_pkt();p['evidence_kind']='synthetic';p['review_status']='independently_reproduced';p['content_sha256']=packet_sha256(p)
        self.assertTrue(any('synthetic/simulation' in x for x in check_packet(p,{'nist'})))
    def test_measured_requires_instrument(self):
        p=self.make_pkt();p['evidence_kind']='measured';p['content_sha256']=packet_sha256(p)
        self.assertTrue(any('instrument' in x for x in check_packet(p,{'nist'})))
    def test_review_needs_artifact(self):
        p=self.make_pkt();p['review_status']='human_reviewed';p['content_sha256']=packet_sha256(p)
        self.assertTrue(any('review_artifact' in x for x in check_packet(p,{'nist'})))
    def test_source_mismatch_fails(self):
        self.with_pkt();data=self.path/'data'/'sources.json';s=json.loads(data.read_text());s[0]['url']='https://example.org';data.write_text(json.dumps(s));self.assertFalse(validate(self.path)['valid'])
    def test_packet_duplicate_rejected(self):
        self.with_pkt();p=self.path/'data'/'packets.jsonl';p.write_text(p.read_text()*2);m=self.path/'atlas_manifest.json';o=json.loads(m.read_text());o['packet_count']=2;m.write_text(json.dumps(o));self.assertFalse(validate(self.path)['valid'])
    def test_query_hit_carries_provenance(self):
        self.with_pkt();r=query(self.path,'measurement type A')
        self.assertEqual(r['status'],'partial');self.assertEqual(r['results'][0]['source_id'],'nist')
    def test_unrelated_query_abstains(self):
        self.with_pkt();self.assertEqual(query(self.path,'quantum sock treehouse')['status'],'unresolved')
    def test_bad_source_url_type_is_rejected(self):
        p=self.make_pkt();p["source_url"]=100;p["content_sha256"]=packet_sha256(p)
        self.assertTrue(check_packet(p,{"nist"}))
    def test_malformed_source_id_is_rejected_without_exception(self):
        p=self.make_pkt();p["source_id"]=["nist"];p["content_sha256"]=packet_sha256(p)
        self.assertTrue(check_packet(p,{"nist"}))
    def test_packet_hash_deterministic(self):
        a=self.make_pkt();b=dict(reversed(list(a.items())));self.assertEqual(packet_sha256(a),packet_sha256(b))
    def test_example_release_valid(self):
        path=Path(__file__).resolve().parents[1]/'examples'/'MEASUREMENT-ATLAS'
        self.assertTrue(validate(path)['valid'])
    def make_pkt(self):
        return make_packet(packet_id='example-1',claim='NIST has a section on measurement Type A uncertainty',evidence_kind='editorial',review_status='editorial_pending_review',source_id='nist',source_url='https://www.nist.gov/pml/nist-technical-note-1297',source_locator='Table of contents §3',inspected_scope='Section title only',applicability='Document navigation',limitations='Not a full method review',rights='Linked only',version='0.1')
    def with_pkt(self):
        p=self.make_pkt();(self.path/'data'/'packets.jsonl').write_text(json.dumps(p)+'\n');(self.path/'data'/'sources.json').write_text(json.dumps([{'source_id':'nist','url':p['source_url'],'version':'1994 revision','rights':'Link only'}]));m=self.path/'atlas_manifest.json';o=json.loads(m.read_text());o['source_count']=1;o['packet_count']=1;m.write_text(json.dumps(o))
if __name__=='__main__':unittest.main()
