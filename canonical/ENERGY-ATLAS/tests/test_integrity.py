import unittest,json,sys,hashlib
from pathlib import Path
from energy_atlas.cases import casebook
ROOT=Path(__file__).resolve().parents[1]
COLLECTION=ROOT.parent
sys.path.insert(0,str(COLLECTION/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,revision
class EnergyAtlasIntegrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.s=AtlasStore(ROOT/'energy_atlas/resources/common')
  cls.rec={x['record_id']:x for x in cls.s.export()}
 def test_record_inventory(self):
  self.assertEqual(len(self.rec),176)
  self.assertEqual(sum(x['type']=='source' for x in self.rec.values()),20)
  self.assertEqual(len(self.s._relations),144)
 def test_full_federation(self):
  f=AtlasStore(COLLECTION/'common').discover()
  self.assertEqual(f['records'],1927)
  self.assertEqual(f['relations'],1133)
  self.assertEqual(len(f['nodes']),10)
 def test_standalone_source_closure(self):
  for r in self.rec.values():
   self.assertEqual(r['revision'],revision(r))
   for src in r['sources']:
    self.assertIn(src['record_id'],self.rec)
    self.assertEqual(src['revision'],self.rec[src['record_id']]['revision'])
  for e in self.s._relations.values():
   self.assertEqual(e['revision'],revision(e))
   for direction in ('from','to'):
    self.assertIn(e[direction]['record_id'],self.rec)
    self.assertEqual(e[direction]['revision'],self.rec[e[direction]['record_id']]['revision'])
 def test_full_cross_domain_edges(self):
  full=AtlasStore(COLLECTION/'common')
  x=[v for v in full._relations.values() if v['relation_id'].startswith('energy-atlas:')]
  self.assertEqual(len(x),149)
  self.assertEqual(sum(not t['to']['record_id'].startswith('energy-atlas:') for t in x),5)
 def test_all_source_entries_link_only(self):
  for r in self.rec.values():
   self.assertFalse(r['provenance']['independent_review'])
   self.assertTrue(r['content']['limitations'])
   if r['type']=='source':
    self.assertFalse(r['provenance']['primary_source_bytes_archived'])
    self.assertEqual(r['rights']['status'],'local_reference')
 def test_manual_and_casebook(self):
  self.assertEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),36)
  self.assertEqual(casebook()['status'],'passed')
  self.assertEqual(casebook()['count'],25)
 def test_all_chapters_linked(self):
  g=(ROOT/'docs/REFERENCE_GUIDE.md').read_text()
  for p in (ROOT/'docs/chapters').glob('*.md'):
   self.assertIn(p.name,g)
 def test_readable_and_reconstructible(self):
  m=(ROOT/'docs/DEPTH_MANUAL_v0.1.0.md').read_text()
  self.assertIn('Derivation',m)
  self.assertIn('Reconstruct',m)
  self.assertIn('Counterexample',m)
  self.assertGreater(len(m.split()),15000)
 def test_no_operational_control(self):
  p=(ROOT/'energy_atlas/models.py').read_text()
  for token in ['requests','socket','subprocess','webbrowser']:
   self.assertNotIn('import '+token,p)
 def test_contexts(self):
  for q in ['Carnot heat pump coefficient engine reversible','battery state of charge charging efficiency storage',
            'solar photovoltaic irradiance temperature correction','wind Betz rotor aerodynamic power',
            'electrical three phase reactive power transformer', 'thermal heat convection conduction radiation']:
   with self.subTest(query=q):
    p=self.s.assemble_context(q,node_ids=['energy-atlas'])
    self.assertEqual(p['status'],'context_available')
    self.assertTrue(self.s.validate_context(p)['valid'])
 def test_derived_constant_note(self):
  p=ROOT/'evidence/physical_constants_reference.json'
  data=json.loads(p.read_text())
  self.assertFalse(data['primary_publisher_source_bytes_archived'])
  self.assertEqual(data['constants']['c']['value'],299792458)
  self.assertEqual(data['constants']['h']['value'],6.62607015e-34)
if __name__=='__main__':unittest.main()
