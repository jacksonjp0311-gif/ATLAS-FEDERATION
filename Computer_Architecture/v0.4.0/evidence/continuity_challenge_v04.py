#!/usr/bin/env python3
"""ATLAS FORGE v0.4: finite source→boot→NAND trace with physical evidence HOLD.

A successful software check is deliberately NOT treated as manufactured hardware.
"""
import json,hashlib
from computer_atlas.v04_bootstrap import bootstrap_certificate,verify_boot_batch
from computer_atlas.v04_gatelevel import evaluate_add,ripple_adder_netlist
from computer_atlas.v04_memory import ParityByteMemory,RoundRobinArbiter
from computer_atlas.v02_trace import physical_evidence_matrix
from computer_atlas.v03_boot import BootSlot,stage_update,select_boot_slot,encode_boot_image
from computer_atlas.v02_bootstrap import compile_source

SOURCE='SET 5\nADD 7\nSTORE 0\nXOR 3\nOUT 0\nHALT'
SECOND='SET 3\nREPEAT 3\nOUT 0\nADD 255\nEND\nHALT'
INVALID='UNSUPPORTED 9\nHALT'

def run():
    built=bootstrap_certificate(SOURCE)
    assert built['output_events']==[[0,15]]
    assert built['NAND_refinement_checks']>=1
    original=BootSlot(1,encode_boot_image(compile_source(SOURCE)),True)
    staged=stage_update(original,None,compile_source(SECOND),2,'after_data')
    # A simulated interrupted update must keep earlier committed program.
    restored=select_boot_slot(*staged)
    assert restored['rom']==compile_source(SOURCE) and restored['generation']==1
    committed=stage_update(*staged,compile_source(SECOND),2,'after_commit')
    assert select_boot_slot(*committed)['generation']==2
    batch=verify_boot_batch([SOURCE,INVALID,SECOND])
    assert batch['software_batch_passed'] is False
    assert [j['result'] for j in batch['results']]==['passed','failed_closed','passed']
    mem=ParityByteMemory(1);mem.write(0,0);mem.inject_data_flip(0,1)
    single=mem.read(0)
    assert single['status']=='detected_parity_error'
    mem.write(0,0);mem.inject_data_flip(0,3)
    double=mem.read(0)
    assert double['status']=='parity_consistent_not_authentic' and double['value']==3
    arb=RoundRobinArbiter(3)
    assert [arb.tick([1,1,1]) for _ in range(6)]==[0,1,2,0,1,2]
    physics=physical_evidence_matrix({'transistor_iv_cv':True,'clock_reset_integrity':True})
    assert len(physics['required_types'])==12 and len(physics['unverified_types'])==12
    assert physics['physical_manufacturing_acceptance']=='HOLD'
    return {'schema':'atlas.at8-v04-continuity-challenge/1','result':'software_pass_physical_hold',
            'ISA':'AT8/0.1 unchanged','source_receipt_sha256':built['receipt_sha256'],
            'ROM_sha256':built['rom_sha256'],'NAND_netlist_sha256':ripple_adder_netlist(8).sha256(),
            'NAND_instruction_refinements':built['NAND_refinement_checks'],
            'output':built['output_events'],'interrupted_generation':restored['generation'],
            'committed_generation':select_boot_slot(*committed)['generation'],
            'batch_result':[j['result'] for j in batch['results']],
            'memory_single_bit_detection':single['status'],
            'memory_double_bit_blind_spot':double['status'],
            'arbiter_grants':[0,1,2,0,1,2],
            'physical_evidence_types_required':12,'physical_evidence_types_verified':0,
            'physical_stages_blocked':physics['blocked_stages'],
            'physical_cpu_fabricated':False,'firmware_authenticated_by_hardware_root':False,
            'publisher_original_file_authenticated':False,
            'independent_scientific_peer_review':False}

if __name__=='__main__':print(json.dumps(run(),indent=2))
