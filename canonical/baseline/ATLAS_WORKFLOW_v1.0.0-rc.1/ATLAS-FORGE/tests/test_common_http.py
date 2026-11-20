import json,unittest,threading
from urllib.request import urlopen
from urllib.error import HTTPError
from atlas_forge.server import make_server
from atlas_forge.common import AtlasStore
class CommonHTTPTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.s=make_server(port=0);cls.t=threading.Thread(target=cls.s.serve_forever,daemon=True);cls.t.start();cls.url=f'http://127.0.0.1:{cls.s.server_port}'
 @classmethod
 def tearDownClass(cls):cls.s.shutdown();cls.s.server_close();cls.t.join()
 def get(self,path):
  with urlopen(self.url+path) as r:return json.load(r)
 def test_common_discovery(self):self.assertEqual(self.get('/api/common/nodes')['records'],505)
 def test_common_search(self):self.assertTrue(self.get('/api/common/search?q=expanded%20uncertainty&node=measurement-atlas')['results'])
 def test_common_context_valid(self):self.assertTrue(AtlasStore().validate_context(self.get('/api/common/context?q=expanded%20uncertainty'))['valid'])
 def test_common_budget(self):self.assertEqual(self.get('/api/common/context?q=expanded%20uncertainty&max_bytes=512')['status'],'budget_exhausted')
 def test_unknown_parameter_rejected(self):
  with self.assertRaises(HTTPError) as e:self.get('/api/common/context?q=uncertainty&execute=true')
  self.assertEqual(e.exception.code,400)
 def test_duplicate_query_rejected(self):
  with self.assertRaises(HTTPError) as e:self.get('/api/common/search?q=a&q=b')
  self.assertEqual(e.exception.code,400)
 def test_common_unknown_endpoint(self):
  with self.assertRaises(HTTPError) as e:self.get('/api/common/execute')
  self.assertEqual(e.exception.code,404)
 def test_common_portal_assets(self):
  for path in ['/','/common_portal.js','/common_portal.css','/hero.png','/legacy']:
   with urlopen(self.url+path) as r:self.assertEqual(r.status,200)
