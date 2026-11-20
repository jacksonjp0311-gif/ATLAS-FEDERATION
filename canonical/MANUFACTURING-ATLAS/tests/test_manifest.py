import unittest,json,hashlib
from pathlib import Path
from manufacturing_atlas.cases import casebook
class MetadataTests(unittest.TestCase):
 def test_casebook(self):
  a=casebook();self.assertEqual(a['status'],'passed');self.assertEqual(a['cases'],14)
 def test_manifest(self):
  p=Path(__file__).resolve().parents[1]
  m=json.loads((p/'FILE_MANIFEST.json').read_text())
  self.assertGreater(len(m['files']),30)
  for k,h in m['files'].items():self.assertEqual(hashlib.sha256((p/k).read_bytes()).hexdigest(),h)
