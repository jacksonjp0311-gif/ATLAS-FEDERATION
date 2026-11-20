"""Energy v1 scoped reference and exact revision preservation checks."""
import unittest,json
from pathlib import Path
from energy_atlas.v1_cases import casebook_v1
ROOT=Path(__file__).resolve().parents[1];COLLECTION=ROOT.parent
from atlas_forge.common import AtlasStore,revision
class EnergyV1(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.s=AtlasStore(ROOT/'energy_atlas/resources/common')
  cls.records={r['record_id']:r for r in cls.s.export()}
 def test_counts(self):
  self.assertEqual(len(self.records),301)
  self.assertEqual(len(self.s._relations),256)
  self.assertEqual(sum(r['type']=='source' for r in self.records.values()),31)
  self.assertEqual(sum(r['provenance'].get('edition_added')=='1.0.0' for r in self.records.values()),60)
 def test_federation(self):
  d=AtlasStore(COLLECTION/'common').discover()
  self.assertEqual(d['records'],2052)
  self.assertEqual(d['relations'],1245)
  self.assertEqual(len(d['nodes']),10)
 def test_old_records_exact(self):
  old=json.loads((ROOT/'evidence/v1_previous_record_revisions.json').read_text());self.assertEqual(len(old),241)
  for key,h in old.items():self.assertEqual(self.records[key]['revision'],h,key)
 def test_old_relations_exact(self):
  old=json.loads((ROOT/'evidence/v1_previous_relation_revisions.json').read_text());self.assertEqual(len(old),205)
  shared=AtlasStore(COLLECTION/'common')
  for key,h in old.items():self.assertEqual(shared._relations[key]['revision'],h,key)
 def test_new_record_revision_and_source_closure(self):
  for r in self.records.values():
   self.assertEqual(r['revision'],revision(r))
   for src in r['sources']:
    self.assertEqual(self.records[src['record_id']]['revision'],src['revision'])
    self.assertEqual(self.records[src['record_id']]['type'],'source')
 def test_relation_closure(self):
  for e in self.s._relations.values():
   self.assertEqual(e['revision'],revision(e))
   for k in ('from','to'):self.assertEqual(self.records[e[k]['record_id']]['revision'],e[k]['revision'])
 def test_version(self):
  from energy_atlas import __version__
  self.assertEqual(__version__,'1.0.0')
 def test_manual(self):
  self.assertEqual(len(list((ROOT/'docs/chapters').glob('*.md'))),64)
  m=(ROOT/'docs/DEPTH_MANUAL_v1.0.0.md').read_text()
  self.assertGreater(len(m.split()),35000)
  guide=(ROOT/'docs/REFERENCE_GUIDE.md').read_text()
  for p in (ROOT/'docs/chapters').glob('*.md'):self.assertIn(p.name,guide)
 def test_cases(self):
  x=casebook_v1();self.assertEqual(x['count'],15);self.assertEqual(x['status'],'passed')
 def test_source_debt_visible(self):
  info=json.loads((ROOT/'evidence/v1_new_source_scope.json').read_text())
  self.assertEqual(info['total_energy_source_count'],31)
  self.assertEqual(info['source_bytes_authenticated'],0)
  for r in self.records.values():
   if r['type']=='source':self.assertFalse(r['provenance'].get('primary_source_bytes_archived',False))
 def test_new_source_labels(self):
  self.assertIn('energy-atlas:source:CDC-FLOODED-WELL',self.records)
  self.assertIn('energy-atlas:source:SANDIA-MICROGRID-TOOLKIT',self.records)
 def test_scoped_context(self):
  for query in ('critical flexible loads and fuel energy conservation ledger','water pumping versus potable water heating safety',
                'blackout grid forming inverter islanding','battery fire protection NFPA 855'):
   c=self.s.assemble_context(query,node_ids=['energy-atlas'])
   self.assertEqual(c['status'],'context_available')
   self.assertTrue(self.s.validate_context(c)['valid'])
 def test_survival_charter(self):
  p=COLLECTION/'docs/HUMAN_KNOWLEDGE_SURVIVAL_CHARTER_v1.md';self.assertTrue(p.is_file())
 def test_nonsafety_status(self):
  from energy_atlas.survival_v1 import water_energy_boundary
  self.assertFalse(water_energy_boundary(2,20,80,1)['potability_verified'])
 def test_previous_snapshot(self):
  q=COLLECTION/'history/energy_v0.2.0_test_snapshot/FILE_CHECKSUMS.json';self.assertTrue(q.is_file())
  self.assertEqual(len(json.loads(q.read_text())['members']),283)
if __name__=='__main__':unittest.main()
