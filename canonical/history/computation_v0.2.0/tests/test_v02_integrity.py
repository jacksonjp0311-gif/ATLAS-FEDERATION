"""Immutable record and source-closure checks for Computation v0.2 content."""
import unittest,json
from pathlib import Path
from computation_atlas.v02_cases import casebook_v02
from atlas_forge.common import AtlasStore,revision
R=Path(__file__).resolve().parents[1]
class V02Integrity(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.s=AtlasStore(R/'computation_atlas/resources/common')
  cls.records={x['record_id']:x for x in cls.s.export()}
 def test_counts(self):
  self.assertEqual(len(self.records),232)
  self.assertEqual(len(self.s._relations),250)
  self.assertEqual(sum(r['type']=='source' for r in self.records.values()),21)
  self.assertEqual(sum(r['provenance'].get('edition_added')=='0.2.0' for r in self.records.values()),70)
 def test_old_records_immutable(self):
  d=json.loads((R/'evidence/previous_record_revisions_v0.1.0.json').read_text());self.assertEqual(len(d),162)
  for k,v in d.items():self.assertEqual(self.records[k]['revision'],v,k)
 def test_old_relations_immutable(self):
  d=json.loads((R/'evidence/previous_relation_revisions_v0.1.0.json').read_text());self.assertEqual(len(d),175)
  for k,v in d.items():
   if k in self.s._relations:self.assertEqual(self.s._relations[k]['revision'],v,k)
  self.assertEqual(len(set(d)-set(self.s._relations)),5)
 def test_source_closure_all(self):
  for r in self.records.values():
   self.assertEqual(r['revision'],revision(r))
   self.assertTrue(r['content']['limitations'])
   for source in r['sources']:
    self.assertEqual(self.records[source['record_id']]['revision'],source['revision'])
    self.assertEqual(self.records[source['record_id']]['type'],'source')
 def test_relationship_closure(self):
  for e in self.s._relations.values():
   self.assertEqual(e['revision'],revision(e))
   for field in ('from','to'):self.assertEqual(self.records[e[field]['record_id']]['revision'],e[field]['revision'])
 def test_casebook(self):
  self.assertEqual(casebook_v02()['status'],'passed');self.assertEqual(casebook_v02()['count'],10)
 def test_docs(self):
  self.assertEqual(len(list((R/'docs/chapters').glob('*.md'))),50)
  self.assertTrue((R/'docs/DEPTH_MANUAL_v0.2.0.md').is_file())
  guide=(R/'docs/REFERENCE_GUIDE.md').read_text()
  for ch in (R/'docs/chapters').glob('*.md'):self.assertIn(ch.name,guide)
 def test_source_rights(self):
  d=json.loads((R/'evidence/source_scope_v0.2.0.json').read_text())
  self.assertEqual(len(d['new_source_cards']),6)
  self.assertEqual(d['authenticated_primary_publisher_bytes_acquired'],0)
  for r in self.records.values():self.assertFalse(r['provenance'].get('original_scientific_review',False))
 def test_new_context_queries(self):
  for q in ('disjoint set union-find equivalence classes',
            'Edmonds Karp maximum flow minimum cut theorem',
            'fft convolution aliasing and zero padding',
            'Lamport vector clocks partial ordering',
            'NP completeness reductions complexity'):
   p=self.s.assemble_context(q,node_ids=['computation-atlas'])
   self.assertEqual(p['status'],'context_available')
   self.assertTrue(self.s.validate_context(p)['valid'])
 def test_standalone_vs_federation(self):
  fed=AtlasStore(R.parent/'common')
  self.assertEqual(fed.discover()['records'],1473)
  self.assertEqual(fed.discover()['relations'],706)
  self.assertEqual(len(fed.discover()['nodes']),8)
  self.assertEqual(fed.discover()['records']-self.s.discover()['records'],1241)
  self.assertEqual(fed.discover()['relations']-self.s.discover()['relations'],456)
if __name__=='__main__':unittest.main()
