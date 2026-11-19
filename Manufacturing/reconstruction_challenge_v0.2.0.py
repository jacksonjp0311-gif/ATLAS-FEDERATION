#!/usr/bin/env python3
"""ATLAS FORGE: evidence-aware bridge from manufacturing records to a computer.

Runs a bounded authentic *software* Electronics v1rc interpreter and then
reports which *physical manufacturing* evidence is absent. Never claims a
fabricated CPU from the interpreter's success.
"""
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'ELECTRONICS-SEMICONDUCTORS-ATLAS'))
from manufacturing_atlas.v02_models import manufacturing_evidence_gate
from electronics_atlas.v1_scoped_models import EightBitAccumulator


def run():
    program=bytes([0x10,5,0x20,7,0x40,0,0x30,3,0xF0,0])
    result=EightBitAccumulator(program,max_steps=30).run()
    software_passed=(result['halted'] and result['ram'][0]==12 and result['accumulator']==15)
    if not software_passed:raise AssertionError('frozen electronics interpreter failed baseline fixture')
    steps={
      'material_characterization':{'depends_on':[],'inputs':['planned_substrate'],
            'outputs':['characterized_substrate'],'required_evidence':['wafer_batch_assay','traceable_calibration']},
      'dielectric_film':{'depends_on':['material_characterization'],'inputs':['characterized_substrate'],
            'outputs':['oxide_stack'],'required_evidence':['oxide_thickness_measurements','film_leakage_test']},
      'semiconductor_device':{'depends_on':['dielectric_film'],'inputs':['oxide_stack'],
            'outputs':['test_transistor'],'required_evidence':['doping_profile','transistor_IV_CV']},
      'digital_cell':{'depends_on':['semiconductor_device'],'inputs':['test_transistor'],
            'outputs':['physical_gate'],'required_evidence':['gate_transfer_curve','cell_timing_across_corners']},
      'register_and_memory':{'depends_on':['digital_cell'],'inputs':['physical_gate'],
            'outputs':['hardware_register'],'required_evidence':['memory_retention_measurement','clock_setup_hold_measurement']},
      'hardware_program':{'depends_on':['register_and_memory'],'inputs':['hardware_register'],
            'outputs':['demonstrated_physical_computer'],'required_evidence':['independent_hardware_program_trace','external_reviewer_signoff']},
    }
    plan=manufacturing_evidence_gate(steps,['planned_substrate'],{})
    assert not plan['structurally_complete'] and not plan['independently_certified']
    assert len(plan['missing_evidence_ids'])==12
    hypothetical=manufacturing_evidence_gate(steps,['planned_substrate'],{name:'SYNTHTIC_METADATA_NOT_MEASUREMENT' for name in plan['missing_evidence_ids']})
    assert hypothetical['structurally_complete'] and not hypothetical['independently_certified']
    return {'schema':'atlas.original-federation-manufacturing-to-computer-challenge/1',
       'software_electronics_v1rc_interpreter_passed':software_passed,
       'software_program_bytes_hex':program.hex(),'software_result':{'accumulator':result['accumulator'],
           'ram0':result['ram'][0],'steps':result['steps']},
       'physical_manufacturing_status':'HOLD','physical_steps_blocked':sum(x['status'].startswith('HOLD') for x in plan['steps'].values()),
       'missing_physical_evidence_types':plan['missing_evidence_ids'],
       'structurally_ready_with_hypothetical_metadata_only':hypothetical['structurally_complete'],
       'physical_evidence_certified_from_metadata':False,
       'real_fabricated_cpu_demonstrated':False,
       'independent_science_review':False,
       'conclusion':'Software reconstructed the finite program. Physical manufacturing remains unsupported by primary measurement evidence.'}

if __name__=='__main__':
 report=run(); print(json.dumps(report,indent=2))
 if len(sys.argv)>1:Path(sys.argv[1]).write_text(json.dumps(report,indent=2)+'\n')
