"""Reproducible AT8 software-retirement trace and manufacturing evidence boundary."""
from __future__ import annotations
import hashlib,json
from .spec import SpecMachine,AT8Trap
from .microcoded import MicrocodedMachine
from .isa import validate_rom

PHYSICAL_GATES=(
 'material_identity','wafer_characterization','transistor_iv_cv',
 'dielectric_and_contact_metrology','gate_transfer_curves','gate_timing_pvt',
 'clock_reset_integrity','physical_memory_retention','power_thermal_validation',
 'layout_masks_interconnect','manufacturing_process_receipts','independent_hardware_execution_trace')


def _digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()


def differential_retirement(rom:bytes,input_tapes=None,max_steps:int=1000):
    validate_rom(rom)
    if type(max_steps) is not int or not 1<=max_steps<=100000:raise ValueError('bounded step count required')
    a=SpecMachine(rom,input_tapes);b=MicrocodedMachine(rom,input_tapes);events=[]
    for i in range(max_steps):
        if a.halted and b.halted:break
        if a.halted!=b.halted:raise AssertionError('retirement halt mismatch')
        pre_a=a.snapshot();pre_b=b.snapshot()
        if pre_a!=pre_b:raise AssertionError('pre-retirement divergence')
        err_a=err_b=None
        try:event_a=a.step()
        except AT8Trap as exc:err_a=exc.code
        try:event_b=b.step_instruction()
        except AT8Trap as exc:err_b=exc.code
        if err_a!=err_b:raise AssertionError(f'atomic versus microcycle traps differ {err_a}, {err_b}')
        if err_a:
            if a.snapshot()!=pre_a or b.snapshot()!=pre_b:raise AssertionError('trap changed committed machine state')
            events.append({'retirement':i,'trap':err_a})
            break
        after=a.snapshot()
        if after!=b.snapshot():raise AssertionError(f'retirement {i} disagreement')
        events.append({'retirement':i,'pc_before':event_a['pc_before'],
            'pc_after':event_a['pc_after'],'instruction':event_a['instruction'],
            'state_sha256':_digest(after)})
    return {'schema':'atlas.at8-retirement-trace/1',
      'rom_sha256':hashlib.sha256(rom).hexdigest(),'event_count':len(events),
      'events_sha256':_digest(events),'halted':a.halted and b.halted,
      'trap':events[-1].get('trap') if events else None,
      'atomic_snapshot':a.snapshot(),'microcycle_snapshot':b.snapshot(),
      'models_agree':a.snapshot()==b.snapshot(),
      'hardware_implementation_demonstrated':False}


def physical_evidence_matrix(assertions=None):
    """Claimed metadata is not a physical measurement or external attestation."""
    if assertions is None: assertions={}
    if not isinstance(assertions,dict):raise ValueError('evidence metadata mapping required')
    unknown=sorted(set(assertions)-set(PHYSICAL_GATES))
    if unknown:raise ValueError('unknown evidence class: '+repr(unknown[:3]))
    return {'schema':'atlas.at8-physical-evidence/1',
      'required_types':list(PHYSICAL_GATES),
      'unverified_types':list(PHYSICAL_GATES),
      'claimed_metadata_types':sorted(k for k,v in assertions.items() if v),
      'blocked_stages':6,
      'physical_manufacturing_acceptance':'HOLD',
      'note':'A checksum or user-provided claim is not independently calibrated physical evidence'}
