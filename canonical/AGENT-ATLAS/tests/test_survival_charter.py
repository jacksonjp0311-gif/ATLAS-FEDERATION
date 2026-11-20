"""Engineering survival archive invariants, not claims of scientific completeness."""
from pathlib import Path
import unittest,sys,importlib.util,io,contextlib,tempfile,json
ROOT=Path(__file__).resolve().parents[2]
AUDIT=ROOT/'tools/survival_audit.py'
class ArchiveV1(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  sp=importlib.util.spec_from_file_location('survival_audit',AUDIT)
  mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
  cls.audit_module=mod
 def test_offline_documents(self):
  for name in ('docs/HUMAN_KNOWLEDGE_SURVIVAL_CHARTER_v1.md','docs/OFFLINE_RECONSTRUCTION_RUNBOOK.md',
               'docs/CROSS_DOMAIN_SCIENTIFIC_CONTRACT.md','knowledge_preservation/SOURCE_ACQUISITION_LEDGER.json'):
   self.assertTrue((ROOT/name).is_file(),name)
 def test_structure_not_science(self):
  r=self.audit_module.audit_archive(ROOT)
  self.assertEqual(r['result'],'passed_structural_only',r['errors'][:4])
  self.assertEqual(r['nodes'],7)
  self.assertGreaterEqual(r['record_count'],1209)
  self.assertFalse(r['full_human_knowledge_preserved'])
  self.assertFalse(r['scientific_validity_independently_verified'])
 def test_primary_source_debt_not_hidden(self):
  r=self.audit_module.audit_archive(ROOT)
  self.assertGreater(r['source_cards'],0)
  self.assertLess(r['verified_local_primary_source_files'],r['source_cards'])
  self.assertFalse(r['all_primary_sources_available_offline'])
 def test_catalog_has_30_domains(self):
  data=json.loads((ROOT/'DOMAIN_QUEUE.json').read_text())
  self.assertEqual(len(data['candidates']),30)
 def test_citation_rule(self):
  a=(ROOT/'docs/HUMAN_KNOWLEDGE_SURVIVAL_CHARTER_v1.md').read_text()
  for term in ('L0','L1','L2','L3','L4','routing','source','UTF-8'):
   self.assertIn(term,a)
if __name__=='__main__':unittest.main()
