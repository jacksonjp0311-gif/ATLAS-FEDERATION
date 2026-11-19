"""Finite software-only bootstrap checks; prior AT8 ISA remains unchanged."""
import unittest,hashlib,json
from computer_atlas.v04_bootstrap import bootstrap_certificate,verify_boot_batch,canonical_bytes
from computer_atlas.v04_gatelevel import certify_at8_arithmetic
from computer_atlas.isa import assemble

SAMPLE='SET 5\nADD 7\nSTORE 0\nXOR 3\nOUT 0\nHALT'
class Bootstrap(unittest.TestCase):
    def test_end_to_end(self):
        a=bootstrap_certificate(SAMPLE)
        self.assertEqual(a['register_r0'],15)
        self.assertEqual(a['output_events'],[[0,15]])
        self.assertFalse(a['physical_CPU_demonstrated'])
    def test_reproducible_certificate(self):
        self.assertEqual(bootstrap_certificate(SAMPLE),bootstrap_certificate(SAMPLE))
    def test_source_edit_changes_digest(self):
        a=bootstrap_certificate(SAMPLE)
        b=bootstrap_certificate(SAMPLE.replace('SET 5','SET 6'))
        self.assertNotEqual(a['rom_sha256'],b['rom_sha256'])
    def test_default_boot_untrusted(self):
        self.assertFalse(bootstrap_certificate(SAMPLE)['firmware_origin_authenticated'])
    def test_isa_preserved(self):
        self.assertEqual(bootstrap_certificate(SAMPLE)['ISA'],'AT8/0.1 unchanged')
    def test_addition_gate_check(self):
        self.assertGreater(bootstrap_certificate(SAMPLE)['NAND_refinement_checks'],0)
    def test_canonical_hash_receipt(self):
        x=bootstrap_certificate(SAMPLE)
        d={k:v for k,v in x.items() if k!='receipt_sha256'}
        self.assertEqual(x['receipt_sha256'],hashlib.sha256(canonical_bytes(d)).hexdigest())
    def test_bad_source_refused(self):
        for x in (None,'',3,'  '):
            with self.assertRaises(ValueError):bootstrap_certificate(x)
    def test_step_budget_rejected(self):
        with self.assertRaises(ValueError):bootstrap_certificate(SAMPLE,max_steps=0)
    def test_batch_all_good(self):
        x=verify_boot_batch(['SET 1\nADD 2\nHALT',SAMPLE])
        self.assertTrue(x['software_batch_passed'])
    def test_batch_fail_closed(self):
        x=verify_boot_batch([SAMPLE,'NO_SUCH_OPCODE 4'])
        self.assertFalse(x['software_batch_passed'])
        self.assertEqual(x['results'][1]['result'],'failed_closed')
    def test_batch_empty_rejected(self):
        with self.assertRaises(ValueError):verify_boot_batch([])
    def test_hardware_claim_false(self):
        self.assertFalse(verify_boot_batch([SAMPLE])['actual_hardware_demonstrated'])
    def test_bounded_loop_holds(self):
        rom=assemble('JMP 0')
        x=certify_at8_arithmetic(rom,max_steps=10)
        self.assertEqual(x['result'],'HOLD')
    def test_arithmetic_trap_holds(self):
        rom=assemble('IN R0, 0\nHALT')
        x=certify_at8_arithmetic(rom,max_steps=10)
        self.assertEqual(x['result'],'HOLD')

if __name__=='__main__':unittest.main()
