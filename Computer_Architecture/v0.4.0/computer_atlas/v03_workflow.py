"""ATLAS FORGE AT8/0.3 bounded, source-verified educational boot workflow.

Combines independent source-language, architectural, and microcycle references.
No executable hardware, secure boot key, authenticated firmware signer, or OS.
"""
from __future__ import annotations
import hashlib,json
from .v02_bootstrap import compile_source,evaluate_source
from .v02_trace import differential_retirement,physical_evidence_matrix
from .v03_boot import (encode_boot_image,decode_boot_image,select_boot_slot,
                        stage_update,BootSlot,BootIntegrityError)
from .v03_control import control_flow_certificate


def canonical_json_bytes(value):
    """Return a deterministic model-data encoding, not a digital signature."""
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False).encode('utf-8')


def _tapes(inputs):
    if inputs is None:return {}
    if type(inputs) is not dict:raise ValueError('input_tapes must be a mapping of 0..3 to finite byte tapes')
    out={}
    for k,v in inputs.items():
        if type(k) is not int or k not in (0,1,2,3) or type(v) not in (list,tuple):
            raise ValueError('port to finite list/tuple tape required')
        if len(v)>10000 or any(type(x) is not int or x<0 or x>255 for x in v):
            raise ValueError('input tape bytes 0..255; max 10000 elements')
        out[k]=tuple(v)
    return out


def verify_program(source:str,input_tapes=None,max_steps:int=20000):
    if type(source) is not str or not source.strip() or len(source.encode('utf-8'))>16000:
        raise ValueError('bounded nonempty program source required')
    if type(max_steps) is not int or not 1<=max_steps<=100000:
        raise ValueError('bounded instruction budget 1..100000 required')
    tapes=_tapes(input_tapes)
    rom=compile_source(source)
    image=encode_boot_image(rom)
    parsed=decode_boot_image(image)
    selected=select_boot_slot(BootSlot(1,image,True),None)
    if parsed['rom']!=selected['rom']:raise AssertionError('selected image differs from original')
    struct=control_flow_certificate(rom)
    reference=evaluate_source(source,tapes,max_operations=max_steps)
    actual=differential_retirement(rom,tapes,max_steps=max_steps)
    if not actual['models_agree'] or not actual['halted'] or actual['trap'] is not None:
        raise ValueError('AT8 reference processors disagree, trap, or do not halt under stated budget')
    state=actual['atomic_snapshot']
    if not reference['halted'] or state['regs'][0]!=reference['accumulator'] or tuple(state['ram'])!=reference['ram'] or tuple(state['output'])!=reference['output'] or tuple(state['input_cursors'])!=reference['input_cursors']:
        raise AssertionError('independent AST vs hardware-abstraction model mismatch')
    data={'schema':'atlas.computer-v03-checked-program/1',
      'source_sha256':hashlib.sha256(source.encode('utf-8')).hexdigest(),
      'rom_sha256':parsed['rom_sha256'],'image_sha256':parsed['image_sha256'],
      'input_tapes_sha256':hashlib.sha256(canonical_json_bytes({str(k):list(v) for k,v in tapes.items()})).hexdigest(),
      'architecture':'AT8/0.1 fixed unchanged ISA','boot_image_format':'AT8R/3',
      'rom_bytes':len(rom),'instructions_retired':state['cycles'],
      'source_AST_verified':True,'atomic_microcycles_verified':True,
      'halted':True,'register_r0':state['regs'][0],
      'RAM_sha256':hashlib.sha256(bytes(state['ram'])).hexdigest(),
      'output_events':list(map(list,state['output'])),
      'output_event_sha256':hashlib.sha256(canonical_json_bytes(state['output'])).hexdigest(),
      'source_reconstruction_evidence':'finite deterministic software only',
      'static_control':struct,
      'manufacturing_physical_evidence_HOLD':physical_evidence_matrix()['physical_manufacturing_acceptance'],
      'physical_hardware_verified':False,'source_bytes_authenticated_to_publisher':False,
      'secure_boot_signature_verified':False}
    data['receipt_sha256']=hashlib.sha256(canonical_json_bytes(data)).hexdigest()
    return data


def verify_job_batch(jobs):
    if type(jobs) not in (tuple,list) or not 1<=len(jobs)<=8:
        raise ValueError('job batch length must be 1..8')
    receipts=[]
    for index,job in enumerate(jobs):
        if type(job) is not dict or set(job)-{'source','input_tapes','max_steps'} or 'source' not in job:
            raise ValueError('each job must have only source, input_tapes, max_steps')
        try:
            receipt=verify_program(job['source'],job.get('input_tapes'),job.get('max_steps',20000))
            receipts.append({'job_index':index,'result':'verified_software','receipt_sha256':receipt['receipt_sha256'],
                'output_events':receipt['output_events'],'steps':receipt['instructions_retired']})
        except (ValueError,AssertionError,BootIntegrityError) as exc:
            # Isolate failure and make omission visible. Do not report batch success.
            receipts.append({'job_index':index,'result':'failed_closed',
                             'exception_type':type(exc).__name__,'detail':str(exc)[:200]})
    valid=all(item['result']=='verified_software' for item in receipts)
    return {'schema':'atlas.computer-v03-job-batch/1','software_acceptance':valid,
            'jobs':receipts,'hardware_operating_system':False,
            'physical_reliability':False,
            'evidence':'bounded deterministic simulation; not true OS scheduling or silicon'}
