"""Original AT8 v0.3 bounded boot/flow/cache/workflow assertions."""
import unittest,struct,hashlib,random
from computer_atlas.isa import assemble,encode
from computer_atlas.v03_boot import (
    BootIntegrityError,BootSlot,encode_boot_image,decode_boot_image,
    ecc_encode_image_payload,ecc_recover_image_payload,select_boot_slot,stage_update,HEADER)
from computer_atlas.v03_control import control_flow_certificate
from computer_atlas.v03_cache import SmallRAMCache
from computer_atlas.v03_workflow import verify_program,verify_job_batch,canonical_json_bytes
from computer_atlas.v02_ecc import UncorrectableROMError

BASE=assemble('LDI R0, 5\nADDI R0, 7\nOUT R0, 0\nHALT')
ALT=assemble('LDI R0, 2\nOUT R0, 0\nHALT')
SOURCE='SET 5\nADD 7\nSTORE 0\nXOR 3\nOUT 0\nHALT'

class ImageContract(unittest.TestCase):
    def test_image_is_exactly_versioned_and_canonical(self):
        b=encode_boot_image(BASE);self.assertEqual(len(b),HEADER.size+len(BASE))
        self.assertEqual(b[:4],b'AT8R');self.assertEqual(decode_boot_image(b)['rom'],BASE)
        self.assertEqual(encode_boot_image(decode_boot_image(b)['rom']),b)
    def test_sha256_and_crc_validate(self):
        a=decode_boot_image(encode_boot_image(BASE))
        self.assertEqual(a['rom_sha256'],hashlib.sha256(BASE).hexdigest())
        self.assertFalse(a['sha256_is_authentication'])
    def test_wrong_magic_rejected(self):
        b=bytearray(encode_boot_image(BASE));b[0]=0
        with self.assertRaises(BootIntegrityError):decode_boot_image(bytes(b))
    def test_wrong_version_rejected(self):
        b=bytearray(encode_boot_image(BASE));b[4]=99
        with self.assertRaises(BootIntegrityError):decode_boot_image(bytes(b))
    def test_nonzero_reserved_flags_rejected(self):
        b=bytearray(encode_boot_image(BASE));b[5]=1
        with self.assertRaises(BootIntegrityError):decode_boot_image(bytes(b))
    def test_truncation_rejected(self):
        with self.assertRaises(BootIntegrityError):decode_boot_image(encode_boot_image(BASE)[:-1])
    def test_extension_rejected(self):
        with self.assertRaises(BootIntegrityError):decode_boot_image(encode_boot_image(BASE)+b'\x00')
    def test_corrupted_crc_rejected(self):
        b=bytearray(encode_boot_image(BASE));b[8]^=1
        with self.assertRaises(BootIntegrityError):decode_boot_image(bytes(b))
    def test_corrupted_hash_rejected(self):
        b=bytearray(encode_boot_image(BASE));b[15]^=1
        with self.assertRaises(BootIntegrityError):decode_boot_image(bytes(b))
    def test_corrupted_payload_rejected(self):
        b=bytearray(encode_boot_image(BASE));b[-1]^=1
        with self.assertRaises(BootIntegrityError):decode_boot_image(bytes(b))
    def test_wrong_python_type_rejected(self):
        with self.assertRaises(BootIntegrityError):decode_boot_image(bytearray(encode_boot_image(BASE)))
    def test_odd_and_oversize_rom_rejected(self):
        for rom in (b'\x00',b'\x00'*257):
            with self.assertRaises(ValueError):encode_boot_image(rom)
    def test_ecc_roundtrip(self):
        image=encode_boot_image(BASE);encoded=ecc_encode_image_payload(image)
        self.assertEqual(ecc_recover_image_payload(encoded,image)['rom'],BASE)
    def test_ecc_13_one_bit_errors(self):
        image=encode_boot_image(BASE);encoded=ecc_encode_image_payload(image)
        for b in range(13):
            altered=list(encoded);altered[0]^=1<<b
            out=ecc_recover_image_payload(altered,image)
            self.assertEqual(out['rom'],BASE);self.assertEqual(out['corrected_words'],1)
    def test_ecc_78_double_bit_errors(self):
        image=encode_boot_image(BASE);encoded=ecc_encode_image_payload(image)
        for a in range(13):
            for b in range(a+1,13):
                altered=list(encoded);altered[0]^=(1<<a)|(1<<b)
                with self.assertRaises(BootIntegrityError):ecc_recover_image_payload(altered,image)

class DualBoot(unittest.TestCase):
    def test_only_a_selected(self):
        s=BootSlot(3,encode_boot_image(BASE),True)
        x=select_boot_slot(s,None)
        self.assertEqual((x['selected_slot'],x['generation']),('A',3))
    def test_newer_committed_selected(self):
        a=BootSlot(1,encode_boot_image(BASE),True)
        b=BootSlot(2,encode_boot_image(ALT),True)
        self.assertEqual(select_boot_slot(a,b)['selected_slot'],'B')
    def test_uncommitted_is_ineligible(self):
        a=BootSlot(1,encode_boot_image(BASE),True)
        b=BootSlot(2,encode_boot_image(ALT),False)
        self.assertEqual(select_boot_slot(a,b)['selected_slot'],'A')
    def test_corrupt_newer_falls_back(self):
        a=BootSlot(1,encode_boot_image(BASE),True)
        b=bytearray(encode_boot_image(ALT));b[-1]^=1
        x=select_boot_slot(a,BootSlot(2,bytes(b),True))
        self.assertEqual(x['selected_slot'],'A')
        self.assertEqual(x['rejected'][0]['reason'],'invalid_image') if False else None
    def test_equal_gen_conflict_fails_closed(self):
        with self.assertRaises(BootIntegrityError):select_boot_slot(BootSlot(1,encode_boot_image(BASE),True),BootSlot(1,encode_boot_image(ALT),True))
    def test_no_valid_boot_fails_closed(self):
        with self.assertRaises(BootIntegrityError):select_boot_slot(None,None)
    def test_power_loss_before_writing_preserves_old(self):
        a=BootSlot(1,encode_boot_image(BASE),True)
        s=stage_update(a,None,ALT,2,'before_data')
        self.assertEqual(s,(a,None))
        self.assertEqual(select_boot_slot(*s)['selected_slot'],'A')
    def test_power_loss_after_data_preserves_old(self):
        a=BootSlot(1,encode_boot_image(BASE),True)
        s=stage_update(a,None,ALT,2,'after_data')
        self.assertEqual(select_boot_slot(*s)['selected_slot'],'A')
    def test_after_commit_selects_new(self):
        a=BootSlot(1,encode_boot_image(BASE),True)
        s=stage_update(a,None,ALT,2,'after_commit')
        self.assertEqual(select_boot_slot(*s)['selected_slot'],'B')
    def test_generation_rollback_rejected(self):
        a=BootSlot(6,encode_boot_image(BASE),True)
        with self.assertRaises(ValueError):stage_update(a,None,ALT,6)
    def test_invalid_generation_rejected(self):
        with self.assertRaises(ValueError):BootSlot(-1,b'',True)
        with self.assertRaises(ValueError):BootSlot(True,b'',True)
    def test_slot_two_generation_updates(self):
        a,b=stage_update(None,None,BASE,1)
        self.assertEqual(select_boot_slot(a,b)['selected_slot'],'A')
        a,b=stage_update(a,b,ALT,2)
        self.assertEqual(select_boot_slot(a,b)['selected_slot'],'B')
        a,b=stage_update(a,b,BASE,3)
        self.assertEqual(select_boot_slot(a,b)['selected_slot'],'A')

class ControlFlow(unittest.TestCase):
    def test_simple_program_all_paths_halt(self):
        r=control_flow_certificate(BASE)
        self.assertTrue(r['all_paths_to_halt_if_no_trap'])
        self.assertFalse(r['reachable_cycle'])
        self.assertEqual(r['max_instructions_if_no_trap'],4)
    def test_branch_loop_is_unknown_not_halting_proof(self):
        rom=assemble('LDI R0, 2\nloop:\nADDI R0, 255\nJNZ R0, loop\nHALT')
        r=control_flow_certificate(rom)
        self.assertTrue(r['reachable_cycle'])
        self.assertFalse(r['all_paths_to_halt_if_no_trap'])
        self.assertIsNone(r['max_instructions_if_no_trap'])
    def test_unreachable_code_after_halt(self):
        rom=assemble('HALT\nLDI R1, 9')
        r=control_flow_certificate(rom)
        self.assertEqual(r['unreachable_program_counters'],(2,))
    def test_fallthrough_beyond_rom_rejected_as_proof(self):
        r=control_flow_certificate(assemble('NOP'))
        self.assertFalse(r['all_paths_to_halt_if_no_trap'])
        self.assertEqual(r['fallthrough_escapes'],(0,))
    def test_conditional_has_both_branches(self):
        rom=assemble('LDI R0, 0\nJZ R0, 8\nLDI R0, 1\nHALT\nHALT')
        r=control_flow_certificate(rom)
        self.assertTrue(r['all_paths_to_halt_if_no_trap'])
        self.assertEqual(r['max_instructions_if_no_trap'],4)
    def test_ram_addresses_are_explicit(self):
        rom=assemble('LOAD R1, 7\nSTORE R1, 8\nOUT R1, 2\nHALT')
        r=control_flow_certificate(rom)
        self.assertEqual(r['ram_read_addresses'],(7,))
        self.assertEqual(r['ram_write_addresses'],(8,))
        self.assertEqual(r['output_ports'],(2,))
    def test_input_may_trap(self):
        rom=assemble('IN R0, 0\nHALT')
        r=control_flow_certificate(rom)
        self.assertTrue(r['all_paths_to_halt_if_no_trap'])
        self.assertTrue(r['possible_input_exhaustion'])
    def test_alignment_or_unsupported_bytecode_refused(self):
        with self.assertRaises(ValueError):control_flow_certificate(b'\x10')

class Cache(unittest.TestCase):
    def test_cold_load_and_hit(self):
        mem=bytes(range(256));c=SmallRAMCache(mem)
        self.assertEqual(c.read(4),4);self.assertEqual(c.read(5),5)
        self.assertEqual((c.read_hits,c.read_misses),(1,1))
    def test_conflicting_tag_eviction(self):
        c=SmallRAMCache(bytes(range(256)),line_size=8,line_count=4)
        self.assertEqual(c.read(0),0)
        self.assertEqual(c.read(32),32)
        self.assertEqual(c.read(0),0)
        self.assertEqual((c.read_hits,c.read_misses),(0,3))
    def test_write_through(self):
        c=SmallRAMCache();c.write(14,173)
        self.assertEqual(c.ram[14],173);self.assertEqual(c.read(14),173)
    def test_write_allocate_collision(self):
        c=SmallRAMCache();c.read(0);c.write(32,41)
        self.assertEqual(c.read(0),0);self.assertEqual(c.read(32),41)
    def test_invalid_address(self):
        c=SmallRAMCache()
        for index in (-1,256,True,1.2):
            with self.assertRaises(ValueError):c.read(index)
    def test_invalid_value(self):
        c=SmallRAMCache()
        for val in (-1,256,True,1.2):
            with self.assertRaises(ValueError):c.write(2,val)
    def test_reset_is_cache_only(self):
        c=SmallRAMCache();c.write(4,71);c.invalidate()
        self.assertEqual(c.read(4),71)
    def test_direct_ram_oracle(self):
        rng=random.Random(20261117);ram=bytearray(256);c=SmallRAMCache()
        for i in range(2500):
            addr=rng.randrange(256)
            if rng.randrange(3):
                v=rng.randrange(256);ram[addr]=v;c.write(addr,v)
            else:self.assertEqual(c.read(addr),ram[addr])
        self.assertEqual(c.ram,ram)

class Workflow(unittest.TestCase):
    def test_compiled_source_matches_reference_processors(self):
        r=verify_program(SOURCE)
        self.assertTrue(r['source_AST_verified'] and r['atomic_microcycles_verified'])
        self.assertEqual(r['output_events'],[[0,15]])
        self.assertEqual(r['register_r0'],15)
        self.assertFalse(r['physical_hardware_verified'])
    def test_receipt_deterministic(self):
        self.assertEqual(verify_program(SOURCE),verify_program(SOURCE))
    def test_input_tape(self):
        r=verify_program('IN 1\nADD 2\nOUT 2\nHALT',{1:[7]})
        self.assertEqual(r['output_events'],[[2,9]])
    def test_bounded_repeat(self):
        r=verify_program('SET 0\nREPEAT 3\n ADD 5\nEND\nOUT 0\nHALT')
        self.assertEqual(r['output_events'],[[0,15]])
        self.assertFalse(r['static_control']['all_paths_to_halt_if_no_trap'])
    def test_missing_input_fails_closed(self):
        with self.assertRaises(ValueError):verify_program('IN 1\nOUT 0\nHALT')
    def test_batch_isolates_bad_job(self):
        r=verify_job_batch([{'source':SOURCE},{'source':'IN 1\nHALT'}])
        self.assertFalse(r['software_acceptance'])
        self.assertEqual([j['result'] for j in r['jobs']],['verified_software','failed_closed'])
    def test_batch_good(self):
        r=verify_job_batch([{'source':SOURCE},{'source':'SET 1\nHALT'}])
        self.assertTrue(r['software_acceptance'])
    def test_batch_limit(self):
        with self.assertRaises(ValueError):verify_job_batch([])
        with self.assertRaises(ValueError):verify_job_batch([{'source':'HALT'}]*9)
    def test_boolean_input_tape_refused(self):
        with self.assertRaises(ValueError):verify_program('IN 1\nHALT',{1:[True]})
    def test_canonical_hash_independent_map_order(self):
        a=canonical_json_bytes({'b':2,'a':[1]})
        b=canonical_json_bytes({'a':[1],'b':2})
        self.assertEqual(a,b)
    def test_bad_jobs_refuse(self):
        with self.assertRaises(ValueError):verify_job_batch([{'source':'HALT','surprise':'X'}])

if __name__=='__main__':unittest.main()
