#!/usr/bin/env python3
"""ATLAS FORGE Computer v0.3 deterministic software-to-physical evidence challenge."""
import json,hashlib
from pathlib import Path
from computer_atlas.v03_workflow import verify_program,verify_job_batch,canonical_json_bytes
from computer_atlas.v03_boot import BootSlot,encode_boot_image,stage_update,select_boot_slot
from computer_atlas.v02_bootstrap import compile_source
from computer_atlas.v02_trace import physical_evidence_matrix

SOURCE='SET 5\nADD 7\nSTORE 0\nXOR 3\nOUT 0\nHALT'
SECOND='SET 3\nREPEAT 3\nOUT 0\nADD 255\nEND\nHALT'
FAIL='IN 1\nHALT'

def run():
    valid=verify_program(SOURCE,max_steps=100)
    assert valid['output_events']==[[0,15]]
    first=BootSlot(1,encode_boot_image(compile_source(SOURCE)),True)
    pending=stage_update(first,None,compile_source(SECOND),2,'after_data')
    recovered=select_boot_slot(*pending)
    assert recovered['rom']==compile_source(SOURCE) and recovered['generation']==1
    committed=stage_update(*pending,compile_source(SECOND),2,'after_commit')
    selected=select_boot_slot(*committed)
    assert selected['rom']==compile_source(SECOND) and selected['generation']==2
    batch=verify_job_batch([{'source':SOURCE},{'source':FAIL},{'source':SECOND}],max_steps=None) if False else verify_job_batch([{'source':SOURCE},{'source':FAIL},{'source':SECOND}])
    assert not batch['software_acceptance']
    assert [x['result'] for x in batch['jobs']]==['verified_software','failed_closed','verified_software']
    physics=physical_evidence_matrix({p:True for p in physical_evidence_matrix()['required_types']})
    assert physics['blocked_stages']==6 and len(physics['unverified_types'])==12
    return {'schema':'atlas.computer-v03-reconstruction-challenge/1','result':'passed_software_reference_physical_hold',
       'ISA':'AT8/0.1 unchanged','boot_image_format':'AT8R/3',
       'main_program_receipt_sha256':valid['receipt_sha256'],
       'main_program_rom_sha256':valid['rom_sha256'],
       'software_main_output':valid['output_events'],
       'interrupted_slot_still_selected_generation':recovered['generation'],
       'committed_slot_selected_generation':selected['generation'],
       'separate_jobs':[{'index':x['job_index'],'result':x['result']} for x in batch['jobs']],
       'batch_is_successful':batch['software_acceptance'],
       'physical_evidence_required':len(physics['required_types']),
       'physical_evidence_verified':0,'physical_stages_blocked':physics['blocked_stages'],
       'hardware_cpu_fabricated':False,'authenticated_secure_boot':False,
       'publisher_original_source_transport_authentication':False,
       'independent_scientific_peer_review':False}
if __name__=='__main__':print(json.dumps(run(),indent=2))
