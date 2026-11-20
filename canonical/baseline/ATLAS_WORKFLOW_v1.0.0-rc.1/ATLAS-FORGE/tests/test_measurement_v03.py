import unittest
from atlas_forge.federation import Federation

class MeasurementNodeTests(unittest.TestCase):
    def test_discover_v03(self):
        d=Federation().discover()
        self.assertTrue(d['valid'], d['errors'])
        m=next(x for x in d['nodes'] if x['id']=='measurement-atlas')
        self.assertEqual(m['version'],'0.3.0')
        self.assertTrue(m['enabled_by_default'])
    def test_default_search(self):
        d=Federation().search('Type A evaluation of standard uncertainty')
        groups=[x for x in d['groups'] if x['node_id']=='measurement-atlas']
        self.assertEqual(len(groups),1)
        self.assertGreater(groups[0]['total_matches'],0)
    def test_original_limited(self):
        d=Federation().search('Type A evaluation of standard uncertainty',node_ids=['measurement-atlas'])
        self.assertTrue(all(x['federation_status']=='imported_reference_not_independently_reviewed' for x in d['results']))
