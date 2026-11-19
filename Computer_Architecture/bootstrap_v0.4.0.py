"""ATLAS FORGE v0.4: verified *software* bootstrapping to NAND datapath.

Checks canonical assembly, AT8 boot checksum, differential microcycle execution,
and independently generated finite gate netlist for retired arithmetic. No
signatures/secure boot, measured silicon, physical update-atomicity or CPU clock.
"""
from __future__ import annotations
import json,hashlib
from .isa import assemble,disassemble
from .v02_bootstrap import compile_source
from .v03_boot import encode_boot_image,decode_boot_image,BootSlot,select_boot_slot
from .v03_workflow import verify_program
from .v04_gatelevel import certify_at8_arithmetic,ripple_adder_netlist


def canonical_bytes(obj):
    return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')


def bootstrap_certificate(source,input_tapes=None,max_steps=5000):
    """Prove finite executable source→ISA→ROM→boot→retire→NAND agreement.

    This is a reproducible *software consistency* certificate, not an attestation
    of boot firmware origin, code safety, timing, silicon or all possible inputs.
    """
    if type(source) is not str or not source.strip() or len(source)>16000:
        raise ValueError('bounded nonempty source text required')
    if type(max_steps) is not int or not 1<=max_steps<=5000:raise ValueError('bounded 1..5000 steps')
    rom=compile_source(source)
    # ISA/assembler bijection for canonical byte encoding
    canonical_asm=disassemble(rom)
    if assemble(canonical_asm)!=rom:raise AssertionError('round-trip assembler mismatch')
    image=encode_boot_image(rom)
    decoded=decode_boot_image(image)
    chosen=select_boot_slot(BootSlot(1,image,True),None)
    if chosen['rom']!=rom or decoded['rom']!=rom:raise AssertionError('boot selection differed')
    receipt=verify_program(source,input_tapes,max_steps)
    gate=certify_at8_arithmetic(rom,input_tapes,max_steps)
    if gate['result']!='passed' or not receipt['source_AST_verified'] or not receipt['atomic_microcycles_verified']:
        raise AssertionError('finite computer reconstruction mismatch')
    data={'schema':'atlas.at8-v04-bootstrap-certificate/1','ISA':'AT8/0.1 unchanged',
          'source_sha256':hashlib.sha256(source.encode()).hexdigest(),
          'canonical_assembly_sha256':hashlib.sha256(canonical_asm.encode()).hexdigest(),
          'rom_sha256':hashlib.sha256(rom).hexdigest(),
          'boot_image_sha256':hashlib.sha256(image).hexdigest(),
          'output_events':receipt['output_events'],
          'output_events_sha256':receipt['output_event_sha256'],
          'register_r0':receipt['register_r0'],'RAM_sha256':receipt['RAM_sha256'],
          'reconstruction_receipt_sha256':receipt['receipt_sha256'],
          'NAND_refinement_checks':gate['exercised_arithmetic_instructions'],
          'NAND_netlist_sha256':ripple_adder_netlist(8).sha256(),
          'syntax_assembler_processor_gate_checks':'passed',
          'firmware_origin_authenticated':False,'secure_boot_hardware_verified':False,
          'physical_CPU_demonstrated':False}
    data['receipt_sha256']=hashlib.sha256(canonical_bytes(data)).hexdigest()
    return data


def verify_boot_batch(programs,max_steps=5000):
    if type(programs) not in (tuple,list) or not 1<=len(programs)<=16:
        raise ValueError('bounded 1..16 program list required')
    results=[]
    for index,src in enumerate(programs):
        try:
            c=bootstrap_certificate(src,None,max_steps)
            results.append({'index':index,'result':'passed','receipt_sha256':c['receipt_sha256']})
        except (ValueError,AssertionError) as exc:
            results.append({'index':index,'result':'failed_closed','exception':type(exc).__name__,
                            'message':str(exc)[:200]})
    return {'schema':'atlas.at8-v04-bootstrap-batch/1','software_batch_passed':all(x['result']=='passed' for x in results),
            'results':results,'actual_hardware_demonstrated':False}
