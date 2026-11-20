#!/usr/bin/env python3
"""Original ATLAS FORGE vertical slice: software program and manufacturing evidence gate.

Uses the inherited Electronics and Manufacturing nodes *as installed in the same
canonical collection*, never claims that Python execution fabricates a computer.
"""
import hashlib,json,sys
from pathlib import Path
here=Path(__file__).resolve()
root=here.parents[2]
sys.path.insert(0,str(root/'COMPUTER-ARCHITECTURE-ATLAS'))
sys.path.insert(0,str(root/'MANUFACTURING-ATLAS'))
sys.path.insert(0,str(root/'ELECTRONICS-SEMICONDUCTORS-ATLAS'))
from computer_atlas.isa import assemble
from computer_atlas.spec import SpecMachine
from computer_atlas.microcoded import MicrocodedMachine
from computer_atlas.programs import ARITHMETIC_AND_MEMORY
from electronics_atlas.v1_scoped_models import EightBitAccumulator
from manufacturing_atlas.v02_models import manufacturing_evidence_gate


def run():
    old=EightBitAccumulator(bytes([0x10,5,0x20,7,0x40,0,0x30,3,0xF0,0])).run()
    assert old['halted'] and old['ram'][0]==12 and old['accumulator']==15
    rom=assemble(ARITHMETIC_AND_MEMORY)
    spec=SpecMachine(rom).run(max_steps=30)
    micro=MicrocodedMachine(rom).run(max_instructions=30)
    assert spec['halted'] and micro['halted'] and spec['snapshot']==micro['snapshot']
    assert spec['snapshot']['ram'][0]==12 and spec['snapshot']['output']==((0,15),)
    stages={
      'substrate_and_material':{'depends_on':[], 'inputs':['proposed_materials'],
        'outputs':['verified_substrate'], 'required_evidence':['wafer_assay','traceable_mobility_measurement']},
      'process_geometry':{'depends_on':['substrate_and_material'], 'inputs':['verified_substrate'],
        'outputs':['device_stack'], 'required_evidence':['lithography_overlay_report','oxide_metrology']},
      'transistor_characterization':{'depends_on':['process_geometry'], 'inputs':['device_stack'],
        'outputs':['validated_transistor'], 'required_evidence':['doping_profile','device_IV_CV_sweeps']},
      'cell_library':{'depends_on':['transistor_characterization'], 'inputs':['validated_transistor'],
        'outputs':['validated_gates'], 'required_evidence':['noise_margins_at_PVT','standard_cell_timing_power']},
      'state_and_interconnect':{'depends_on':['cell_library'], 'inputs':['validated_gates'],
        'outputs':['validated_registers_and_RAM'], 'required_evidence':['setup_hold_metastability_tests','memory_retention_ECC_tests']},
      'hardware_program_execution':{'depends_on':['state_and_interconnect'], 'inputs':['validated_registers_and_RAM'],
        'outputs':['physical_AT8_demonstrator'], 'required_evidence':['independently_recorded_hardware_trace','signed_external_reviewer']},
    }
    physical=manufacturing_evidence_gate(stages,['proposed_materials'],{})
    assert not physical['structurally_complete'] and not physical['independently_certified']
    assert len(physical['missing_evidence_ids'])==12
    supplied={name:'UNAUTHENTICATED_METADATA_NOT_PHYSICAL_PROOF' for name in physical['missing_evidence_ids']}
    synthetic=manufacturing_evidence_gate(stages,['proposed_materials'],supplied)
    assert synthetic['structurally_complete'] and not synthetic['independently_certified']
    # Exactly reproducible software trace receipts, not authentication or claims of equipment.
    traceraw=json.dumps(spec['trace'],sort_keys=True,separators=(',',':')).encode()
    return {'schema':'atlas.original-federation-computer-architecture-continuity/1',
      'program_hex':rom.hex(),'rom_sha256':hashlib.sha256(rom).hexdigest(),
      'trace_sha256':hashlib.sha256(traceraw).hexdigest(),
      'prior_electronics_accumulator_halted':old['halted'],'prior_electronics_ram0':old['ram'][0],
      'new_architecture_implementations_agree':True,
      'new_at8_halted':spec['halted'],'new_at8_instruction_steps':spec['steps'],
      'new_at8_microcycles':micro['microcycles'],
      'new_at8_ram0':spec['snapshot']['ram'][0],
      'new_at8_port0_output':list(spec['snapshot']['output']),
      'physical_stages_blocked':sum(v['status'].startswith('HOLD') for v in physical['steps'].values()),
      'missing_physical_evidence_types':physical['missing_evidence_ids'],
      'synthetic_metadata_structurally_complete':synthetic['structurally_complete'],
      'synthetic_metadata_independently_certified':synthetic['independently_certified'],
      'physical_CPU_fabricated':False,'physical_device_measurements':0,
      'independent_hardware_review':False,'publisher_originals_authenticated':0,
      'verdict':'PASS finite reproducible software; HOLD physical technology reconstruction'}

if __name__=='__main__':
    x=run();print(json.dumps(x,indent=2))
    if len(sys.argv)>1:
        out=Path(sys.argv[1]);out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(json.dumps(x,indent=2)+'\n')
