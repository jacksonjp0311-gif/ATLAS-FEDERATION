"""Bounded offline survival reader tests; fabricated data never scientific claims."""
import contextlib,hashlib,io,json,os,pathlib,sys,tempfile,unittest
from tools.atlas_offline import Atlas,AtlasError,canonical,digest_bytes,strict_json,safe_file,main
ROOT=pathlib.Path(__file__).resolve().parents[1]

def sample_record(node,identity,source=False):
    r={'schema':'atlas.record/1','node_id':node,'record_id':f'{node}:{identity}',
       'original_id':identity,'type':'source' if source else 'concept','title':'Sample resistor physics',
       'content':{'text':'Ohm law V=IR, ideal laboratory fixture only.','tags':['resistor','voltage'],
         'domain':'electrical','equation':'V = I R','assumptions':['constant resistance'],
         'applicability':['linear circuit example'],'limitations':['not a measurement'],
         'units':['V','A','ohm'],'uncertainty':['zero measured calibration']},
       'evidence':{'origin':'constructed','review_status':'not_independently_reviewed',
         'locators':[],'gaps':['no physical experiment'],'upstream_labels':{}},
       'sources':[],'rights':{'status':'local_reference','note':'Original mathematical example'},
       'provenance':{'author':'Test fixture','publisher_original_archived':False},'extensions':{},'status':'active'}
    r['revision']=digest_bytes(canonical(r));return r

def sample_relation(a,b):
    r={'schema':'atlas.relation/1','relation_id':'test-node:related-1','type':'depends_on',
       'from':{'record_id':a['record_id'],'revision':a['revision']},
       'to':{'record_id':b['record_id'],'revision':b['revision']},'provenance':{'origin':'fixture'}}
    r['revision']=digest_bytes(canonical(r));return r

def fixture(folder):
    root=pathlib.Path(folder)
    data=root/'common/nodes/test-node/data';data.mkdir(parents=True,exist_ok=True)
    a=sample_record('test-node','a');b=sample_record('test-node','b',True);rel=sample_relation(a,b)
    coll={}
    for cat,rows in [('concept',[a]),('source',[b]),('relations',[rel])]:
        p=data/(cat+'s.jsonl' if cat!='relations' else 'relations.jsonl')
        p.write_bytes(b''.join(canonical(x)+b'\n' for x in rows))
        coll[cat]={'path':'data/'+p.name,'records':len(rows),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    manifest={'schema':'atlas.node-manifest/1','node_id':'test-node','collections':coll}
    mp=data.parent/'atlas_manifest.json';mp.write_bytes(canonical(manifest)+b'\n')
    registry={'schema':'atlas.registry/1','nodes':[{'node_id':'test-node','manifest':'nodes/test-node/atlas_manifest.json','manifest_sha256':hashlib.sha256(mp.read_bytes()).hexdigest()}]}
    rp=root/'common/registry.json';rp.write_bytes(canonical(registry)+b'\n')
    (rp.parent/'registry.lock.json').write_bytes(canonical({'schema':'atlas.registry-lock/1','sha256':hashlib.sha256(rp.read_bytes()).hexdigest()}))
    q=root/'DOMAIN_QUEUE.json';q.write_text('[]\n')
    files={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file()}
    (root/'FILE_MANIFEST.json').write_bytes(canonical({'schema':'atlas.files/1','files':files})+b'\n')
    return root,a,b,rel

class TestContracts(unittest.TestCase):
    def test_canonical_stable(self):
        self.assertEqual(canonical({'b':2,'a':1}),b'{"a":1,"b":2}')
    def test_json_duplicate_fails(self):
        with self.assertRaises(AtlasError):strict_json('{"a":1,"a":2}')
    def test_nonfinite_rejected(self):
        with self.assertRaises(AtlasError):strict_json('{"x":NaN}')
    def test_directory_escape_refused(self):
        for bad in ('../x','/etc/passwd','..\\win','C:/foo','a/../b'):
            with self.subTest(bad=bad),self.assertRaises(AtlasError):safe_file(ROOT,bad)
    def test_symlink_refused(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d);(root/'shortcut').symlink_to('/tmp')
            with self.assertRaises(AtlasError):safe_file(root,'shortcut/data')
    def test_absolute_root_valid(self):self.assertEqual(safe_file(ROOT,'common').name,'common')
    def test_boolean_query_bounds(self):
        with self.assertRaises(AtlasError):Atlas(ROOT).search('t',0)
    def test_record_revision_formula(self):
        r=sample_record('test-node','a')
        self.assertEqual(r['revision'],digest_bytes(canonical({k:v for k,v in r.items() if k!='revision'})))

class TestFixture(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root,self.a,self.b,self.rel=fixture(self.tmp.name)
    def tearDown(self):self.tmp.cleanup()
    def test_fixture_catalog(self):
        m=Atlas(self.root).catalog()
        self.assertEqual((m['nodes'],m['records'],m['relationships']),(1,2,1))
    def test_fixture_verify(self):
        m=Atlas(self.root).verify()
        self.assertEqual((m['source_file_hashes_verified'],m['exact_relation_references_checked']),(7,2))
    def test_untracked_file_reported(self):
        (self.root/'NOT_IN_MANIFEST.txt').write_text('untracked')
        report=Atlas(self.root).verify()
        self.assertEqual(report['untracked_files_count'],1)
        self.assertEqual(report['untracked_files_first_10'],['NOT_IN_MANIFEST.txt'])
    def test_fixture_search(self):
        m=Atlas(self.root).search('resistor')
        self.assertEqual(m['matches_total'],2)
        self.assertFalse(m['rank_is_scientific_confidence'])
    def test_fixture_search_nonexistent(self):self.assertEqual(Atlas(self.root).search('supernovanotfound')['matches_total'],0)
    def test_fixture_gaps_not_qualified(self):
        m=Atlas(self.root).gaps()
        self.assertEqual(m['publisher_original_bytes_authenticated_in_this_offline_check'],0)
        self.assertEqual(m['bibliographic_source_records_total'],1)
    def test_fixture_record(self):self.assertEqual(Atlas(self.root).record(self.a['record_id'])['record']['title'],'Sample resistor physics')
    def test_unknown_record(self):
        with self.assertRaises(AtlasError):Atlas(self.root).record('does-not-exist')
    def test_fixture_trace_upstream(self):
        m=Atlas(self.root).trace(self.a['record_id'])
        self.assertEqual(len(m['records']),2)
    def test_fixture_trace_downstream(self):
        m=Atlas(self.root).trace(self.b['record_id'],'downstream')
        self.assertEqual(len(m['records']),2)
    def test_fixture_trace_both(self):
        m=Atlas(self.root).trace(self.b['record_id'],'both')
        self.assertEqual(len(m['records']),2)
    def test_fixture_trace_depth_zero(self):self.assertEqual(len(Atlas(self.root).trace(self.a['record_id'],depth=0)['records']),1)
    def test_trace_depth_refused(self):
        with self.assertRaises(AtlasError):Atlas(self.root).trace(self.a['record_id'],depth=50)
    def test_tamper_manifest_sha(self):
        (self.root/'common/nodes/test-node/atlas_manifest.json').write_text('{}')
        with self.assertRaises(AtlasError):Atlas(self.root).catalog()
    def test_tamper_source_files(self):
        p=self.root/'common/nodes/test-node/data/concepts.jsonl'
        p.write_bytes(p.read_bytes()+b'CORRUPTION')
        with self.assertRaises(AtlasError):Atlas(self.root).verify()
    def test_tamper_lock(self):
        (self.root/'common/registry.lock.json').write_text('{}')
        with self.assertRaises(AtlasError):Atlas(self.root).verify(all_files=False)
    def test_missing_endpoint(self):
        relpath=self.root/'common/nodes/test-node/data/relations.jsonl'
        m=json.loads(relpath.read_bytes());m['to']['record_id']='test-node:missing'
        m['revision']=digest_bytes(canonical({k:v for k,v in m.items() if k!='revision'}))
        relpath.write_bytes(canonical(m)+b'\n')
        # correctly update immutable checksum manifests so failure tests semantics
        mp=self.root/'common/nodes/test-node/atlas_manifest.json';manifest=json.loads(mp.read_bytes());manifest['collections']['relations']['sha256']=hashlib.sha256(relpath.read_bytes()).hexdigest();mp.write_bytes(canonical(manifest)+b'\n')
        rp=self.root/'common/registry.json';registry=json.loads(rp.read_bytes());registry['nodes'][0]['manifest_sha256']=hashlib.sha256(mp.read_bytes()).hexdigest();rp.write_bytes(canonical(registry)+b'\n')
        with self.assertRaises(AtlasError):Atlas(self.root).record(self.a['record_id'])
    def test_duplicate_record_id(self):
        p=self.root/'common/nodes/test-node/data/concepts.jsonl';p.write_bytes(p.read_bytes()+p.read_bytes())
        mp=self.root/'common/nodes/test-node/atlas_manifest.json';d=json.loads(mp.read_bytes());d['collections']['concept']['records']=2;d['collections']['concept']['sha256']=hashlib.sha256(p.read_bytes()).hexdigest();mp.write_bytes(canonical(d)+b'\n')
        rp=self.root/'common/registry.json';d=json.loads(rp.read_bytes());d['nodes'][0]['manifest_sha256']=hashlib.sha256(mp.read_bytes()).hexdigest();rp.write_bytes(canonical(d)+b'\n')
        with self.assertRaises(AtlasError):Atlas(self.root).record(self.a['record_id'])
    def test_cli_success_and_failclosed(self):
        stdout,stderr=io.StringIO(),io.StringIO()
        with contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):r=main(['--root',str(self.root),'search','resistor'])
        self.assertEqual(r,0);self.assertEqual(json.loads(stdout.getvalue())['matches_total'],2)
        stdout,stderr=io.StringIO(),io.StringIO()
        with contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):r=main(['--root',str(self.root),'record','missing'])
        self.assertEqual(r,2);self.assertEqual(json.loads(stderr.getvalue())['result'],'FAIL_CLOSED')

class TestActualFederation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.a=Atlas(ROOT)
    def test_15_nodes(self):self.assertEqual(self.a.catalog()['nodes'],15)
    def test_unchanged_record_and_relation_counts(self):
        m=self.a.catalog();self.assertEqual((m['records'],m['relationships']),(3235,2415))
    def test_547_source_cards(self):self.assertEqual(self.a.gaps()['bibliographic_source_records_total'],547)
    def test_search_electronics(self):self.assertGreater(self.a.search('semiconductor transport')['matches_total'],1)
    def test_search_computing(self):self.assertGreater(self.a.search('boot machine code')['matches_total'],1)
    def test_docs_present(self):self.assertGreaterEqual(len(self.a.manuals()['items']),8)
    def test_exact_revision_trace(self):
        x='computer-architecture-digital-hardware-atlas:chapter-60-method'
        self.assertGreater(len(self.a.trace(x)['records']),1)
    def test_no_scientific_certification(self):self.assertEqual(self.a.gaps()['physical_fabrication_verified_in_this_offline_check'],0)
    def test_bootstrap_challenge(self):
        x=self.a.challenge();self.assertEqual(x['output_events'],[[0,15]])
        self.assertEqual(x['result'],'software_reconstruction_passed')
    def test_entire_file_manifest(self):
        x=self.a.verify();self.assertGreaterEqual(x['source_file_hashes_verified'],9345)
        self.assertEqual(x['node_manifest_hashes_verified'],15)

if __name__=='__main__':unittest.main()
