"""Authored engineering regression tests, not scientific/answer-quality evaluation."""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from atlas_forge.cli import main
from atlas_forge.federation import Federation, FederationError, _safe
from atlas_forge.server import make_server

class FederationTests(unittest.TestCase):
    def setUp(self):self.f=Federation()
    def test_three_nodes_only(self):
        d=self.f.discover();self.assertTrue(d['valid']);self.assertEqual({n['id'] for n in d['nodes']},{'signal-atlas','cymatics-atlas','measurement-atlas'})
    def test_exact_node_counts(self):
        d=self.f.discover();self.assertEqual({n['id']:n['record_count'] for n in d['nodes']},{'signal-atlas':232,'cymatics-atlas':132,'measurement-atlas':6})
    def test_upstream_pins(self):
        n=self.f.discover()['nodes'];self.assertEqual(n[0]['upstream']['commit'],'234b65fdb4f64add7fa53d5ea8312a63bcf616b4');self.assertEqual(n[1]['upstream']['commit'],'21fba3ec77225d14ef81a6d761fa0922d8002d56')
    def test_all_six_remote_blobs_match(self):
        d=self.f.discover();files=[f for n in d['nodes'][:2] for f in n['snapshot_files']];self.assertEqual(len(files),6);self.assertTrue(all(f['git_blob_verified'] for f in files))
    def test_federation_membership_not_causality(self):
        self.assertTrue(all(e['relation']=='contains_reference_node' for e in self.f.discover()['edges']))
    def test_no_unbuilt_nodes(self):self.assertNotIn('materials-atlas',json.dumps(self.f.discover()))
    def test_faraday_routes_to_cymatics(self):
        r=self.f.search('Faraday waves');self.assertEqual({x['node_id'] for x in r['results']},{'cymatics-atlas'})
    def test_noaa_routes_to_signal(self):
        r=self.f.search('NOAA GOES');self.assertEqual({x['node_id'] for x in r['results']},{'signal-atlas'})
    def test_cross_atlas_uncertainty(self):
        r=self.f.search('frequency uncertainty');self.assertEqual({x['node_id'] for x in r['results']},{'signal-atlas','cymatics-atlas','measurement-atlas'})
    def test_empty_unresolved(self):self.assertEqual(self.f.search('')['status'],'unresolved')
    def test_stopwords_unresolved(self):self.assertEqual(self.f.search('what is the')['status'],'unresolved')
    def test_unmatched_unresolved(self):self.assertEqual(self.f.search('unicorn teleportation')['status'],'unresolved')
    def test_partial_not_verified(self):
        r=self.f.search('resonance');self.assertEqual(r['status'],'partial');self.assertFalse(r['answer_verified'])
    def test_measurement_now_enabled(self):
        r=self.f.search('uncertainty');self.assertFalse(r['excluded_nodes']);self.assertIn('measurement-atlas',{x['node_id'] for x in r['results']})
    def test_starter_explicit(self):
        r=self.f.search('uncertainty',node_ids=['measurement-atlas'],include_starters=True);self.assertTrue(r['results']);self.assertTrue(all(x['upstream_status']=='editorial_pending_review' for x in r['results'] if x['kind']=='starter_packet'))
    def test_selected_measurement_is_enabled(self):self.assertEqual(self.f.search('uncertainty',node_ids=['measurement-atlas'])['status'],'partial')
    def test_node_filter(self):
        r=self.f.search('frequency',node_ids=['signal-atlas']);self.assertTrue(r['results']);self.assertEqual({x['node_id'] for x in r['results']},{'signal-atlas'})
    def test_unknown_node_rejected(self):
        with self.assertRaises(ValueError):self.f.search('wave',node_ids=['materials-atlas'])
    def test_empty_node_selection_rejected(self):
        with self.assertRaises(ValueError):self.f.search('wave',node_ids=[])
    def test_bad_limits(self):
        for n in [0,51,-1,True,2.5]:
            with self.subTest(n=n),self.assertRaises(ValueError):self.f.search('waves',per_node=n)
    def test_bad_query(self):
        for q in [None,[],'x'*4097]:
            with self.assertRaises(ValueError):self.f.search(q)
    def test_deterministic(self):self.assertEqual(self.f.search('frequency'),self.f.search('frequency'))
    def test_per_node_limit(self):
        r=self.f.search('frequency',per_node=1);self.assertEqual(len(r['results']),2)
    def test_lossless_original_claim(self):
        r=next(r for r in self.f.export(['signal-atlas']) if r['original_id']=='C-001');self.assertEqual(r['text'],r['upstream_record']['claim']);self.assertEqual(r['upstream_status'],'verified');self.assertEqual(r['federation_status'],'imported_reference_not_independently_reviewed')
    def test_citations_and_rights(self):
        r=self.f.search('Faraday waves')['results'];self.assertTrue(all(x['sources'] for x in r));self.assertTrue(all(s['url'].startswith('https://') and s['rights'] for x in r for s in x['sources']))
    def test_record_locator_not_evidence_locator(self):
        r=next(r for r in self.f.export(['cymatics-atlas']) if r['original_id']=='cymatics-definition');self.assertIsNone(r['evidence_locator']);self.assertEqual(r['record_locator']['position'],'/concepts/0')
    def test_audit_locator_preserved(self):
        r=next(r for r in self.f.export(['cymatics-atlas']) if r['original_id']=='a-leissa-survey');self.assertEqual(r['evidence_locator'],r['upstream_record']['source_locator'])
    def test_catalog_is_not_measurement(self):
        r=[r for r in self.f.export(['cymatics-atlas']) if r['kind']=='external_dataset_catalog'];self.assertEqual(len(r),2);self.assertTrue(all(not x['supporting_raw_measurements_bundled'] and not x['upstream_record']['locally_imported'] for x in r))
    def test_shared_citations_not_corroboration(self):
        r=self.f.search('Faraday waves');self.assertTrue(r['shared_source_groups']);self.assertTrue(all('not independent corroboration' in g['meaning'] for g in r['shared_source_groups']))
    def test_namespaced_ids_unique(self):
        r=self.f.export(include_starters=True);self.assertEqual(len(r),len({x['record_uid'] for x in r}))
    def test_export_default_count(self):self.assertEqual(len(self.f.export()),370)
    def test_export_all_count(self):self.assertEqual(len(self.f.export(include_starters=True)),370)
    def test_export_one_node(self):self.assertEqual(len(self.f.export(['cymatics-atlas'])),132)
    def test_data_not_executed(self):
        r=self.f.search('$(touch /tmp/ATLAS_SHOULD_NOT_RUN)');self.assertEqual(r['status'],'unresolved');self.assertFalse(Path('/tmp/ATLAS_SHOULD_NOT_RUN').exists())
    def test_path_traversal_rejected(self):
        for p in ['../x','/etc/passwd','C:/x','raw\\x','']:
            with self.subTest(p=p),self.assertRaises(FederationError):_safe(Path('.'),p)
    def test_symlink_escape_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)
            try: (p/'link').symlink_to(p.parent,target_is_directory=True)
            except (OSError, NotImplementedError): self.skipTest('symlink creation not available on this platform')
            with self.assertRaises(FederationError):_safe(p,'link/anything')
    def test_corrupt_one_node_isolated(self):
        with tempfile.TemporaryDirectory() as t:
            shutil.copytree(self.f.root,Path(t)/'f');f=Federation(Path(t)/'f');p=f.root/'nodes/signal-atlas/1.0/raw/claims.jsonl';p.write_bytes(p.read_bytes()+b' ')
            d=f.discover();self.assertFalse(d['valid']);r=f.search('Faraday waves');self.assertTrue(r['degraded']);self.assertTrue(r['results']);self.assertEqual(r['errors'][0]['node_id'],'signal-atlas')
            with self.assertRaises(FederationError):f.export()
    def test_manifest_tamper_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            shutil.copytree(self.f.root,Path(t)/'f');f=Federation(Path(t)/'f');p=f.root/'nodes/cymatics-atlas/1.0.0/manifest.json';p.write_text('{}');self.assertFalse(f.discover()['valid'])
    def test_registry_tamper_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            shutil.copytree(self.f.root,Path(t)/'f');f=Federation(Path(t)/'f');(f.root/'registry.json').write_text('{}');self.assertFalse(f.discover()['valid'])
            with self.assertRaises(FederationError):f.search('frequency')
    def test_cli_nodes(self):
        s=io.StringIO()
        with contextlib.redirect_stdout(s):code=main(['nodes'])
        self.assertEqual(code,0);self.assertEqual(len(json.loads(s.getvalue())['nodes']),3)
    def test_cli_export_no_overwrite(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'x.jsonl'
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(['export-nodes','--out',str(p)]),0);self.assertEqual(main(['export-nodes','--out',str(p)]),2)
            self.assertEqual(len(p.read_text().splitlines()),370)
    def test_cli_bad_node_error(self):
        with contextlib.redirect_stdout(io.StringIO()):self.assertEqual(main(['search','waves','--node','missing']),2)

class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=make_server(port=0);cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start();cls.base=f'http://127.0.0.1:{cls.server.server_port}'
    @classmethod
    def tearDownClass(cls):cls.server.shutdown();cls.server.server_close();cls.thread.join(3)
    def request(self,path,**kwargs):return urlopen(Request(self.base+path,**kwargs),timeout=4)
    def test_discovery(self):
        with self.request('/api/nodes') as r:self.assertEqual(len(json.load(r)['nodes']),3)
    def test_search(self):
        with self.request('/api/search?q=Faraday') as r:self.assertTrue(json.load(r)['results'])
    def test_empty_search(self):
        with self.request('/api/search?q=') as r:self.assertEqual(json.load(r)['status'],'unresolved')
    def test_invalid_query_parameter(self):
        with self.assertRaises(HTTPError) as c:self.request('/api/search?q=wave&per_node=999')
        self.assertEqual(c.exception.code,400)
    def test_invalid_starter_parameter(self):
        with self.assertRaises(HTTPError) as c:self.request('/api/search?include_starters=maybe')
        self.assertEqual(c.exception.code,400)
    def test_portal_and_resources(self):
        for path,term in [('/','ATLAS FORGE'),('/portal.js','textContent'),('/portal.css',':root')]:
            with self.request(path) as r:self.assertIn(term,r.read().decode())
    def test_csp_and_no_cors(self):
        with self.request('/') as r:self.assertIn("frame-ancestors 'none'",r.headers['Content-Security-Policy']);self.assertIsNone(r.headers.get('Access-Control-Allow-Origin'))
    def test_unknown_path(self):
        with self.assertRaises(HTTPError) as c:self.request('/secrets')
        self.assertEqual(c.exception.code,404)
    def test_writes_rejected(self):
        with self.assertRaises(HTTPError) as c:self.request('/api/nodes',method='POST',data=b'{}')
        self.assertEqual(c.exception.code,405)
    def test_cross_origin_rejected(self):
        with self.assertRaises(HTTPError) as c:self.request('/api/nodes',headers={'Origin':'https://unrelated.invalid'})
        self.assertEqual(c.exception.code,403)
    def test_rebinding_host_rejected(self):
        with self.assertRaises(HTTPError) as c:self.request('/api/nodes',headers={'Host':'evil.example'})
        self.assertEqual(c.exception.code,403)

if __name__=='__main__':unittest.main()
