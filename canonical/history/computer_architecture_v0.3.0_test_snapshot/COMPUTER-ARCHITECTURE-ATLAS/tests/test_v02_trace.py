import unittest,random
from computer_atlas.v02_trace import differential_retirement,physical_evidence_matrix,PHYSICAL_GATES
from computer_atlas.programs import examples
from computer_atlas.isa import assemble
class TestRetirementAndEvidence(unittest.TestCase):
    def test_arithmetic(self):
        p=differential_retirement(examples()['arithmetic_memory'])
        self.assertTrue(p['halted']);self.assertTrue(p['models_agree'])
        self.assertEqual(p['atomic_snapshot']['regs'][0],15)
    def test_countdown(self):
        p=differential_retirement(examples()['countdown'])
        self.assertTrue(p['halted']);self.assertEqual(p['atomic_snapshot']['output'],((0,3),(0,2),(0,1)))
    def test_io(self):
        p=differential_retirement(examples()['input_output'],{1:[11]})
        self.assertTrue(p['halted']);self.assertEqual(p['atomic_snapshot']['output'],((2,13),))
    def test_exhausted_input(self):
        p=differential_retirement(assemble('IN R0,1\nHALT'))
        self.assertFalse(p['halted']);self.assertEqual(p['trap'],'input_exhausted')
    def test_loop_step_bound(self):
        p=differential_retirement(assemble('L: JMP L'),max_steps=10)
        self.assertFalse(p['halted']);self.assertTrue(p['models_agree'])
    def test_trace_hash_repro(self):
        rom=assemble('LDI R0,3\nADDI R0,1\nHALT')
        self.assertEqual(differential_retirement(rom)['events_sha256'],differential_retirement(rom)['events_sha256'])
    def test_trace_rom_mutation_hash(self):
        a=differential_retirement(assemble('LDI R0,3\nHALT'))
        b=differential_retirement(assemble('LDI R0,4\nHALT'))
        self.assertNotEqual(a['rom_sha256'],b['rom_sha256'])
    def test_evidence_default(self):
        x=physical_evidence_matrix()
        self.assertEqual(len(x['unverified_types']),12)
        self.assertEqual(x['physical_manufacturing_acceptance'],'HOLD')
    def test_evidence_claims_not_certified(self):
        x=physical_evidence_matrix({k:{'asserted':True,'sha256':'deadbeef'} for k in PHYSICAL_GATES})
        self.assertEqual(len(x['claimed_metadata_types']),12)
        self.assertEqual(len(x['unverified_types']),12)
        self.assertEqual(x['physical_manufacturing_acceptance'],'HOLD')
    def test_unknown_claim_refused(self):
        with self.assertRaises(ValueError):physical_evidence_matrix({'magical_free_chip':True})
