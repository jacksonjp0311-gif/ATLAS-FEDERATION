import unittest
try:
 from atlas_forge.common import AtlasStore
 HAS_FORGE=True
except ImportError:HAS_FORGE=False
from measurement_atlas.reference import open_reference

@unittest.skipUnless(HAS_FORGE,'optional shared Forge runtime not installed')
class ReferenceTests(unittest.TestCase):
 def test_single_node(self):
  d=open_reference().discover();self.assertEqual(d['records'],141);self.assertEqual(len(d['nodes']),1)
 def test_context_valid(self):
  s=open_reference();p=s.assemble_context('expanded uncertainty');self.assertTrue(s.validate_context(p)['valid'])
 def test_known_primary_record(self):
  s=open_reference();r=s.search('uniform bounded uncertainty')['results'][0];self.assertEqual(r['record_id'],'measurement-atlas:method:uniform-bounds')
 def test_no_match(self):self.assertEqual(open_reference().search('zxqv7788')['status'],'no_match')
 def test_budget(self):
  s=open_reference();p=s.assemble_context('uncertainty',max_context_bytes=512);self.assertLessEqual(p['context_bytes'],512);self.assertTrue(s.validate_context(p)['valid'])
 def test_publication_not_replication(self):
  rs=open_reference().export();self.assertFalse(any(r['evidence']['review_status']=='independently_reproduced' for r in rs))
