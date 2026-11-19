#!/usr/bin/env python3
"""ATLAS FORGE computer v0.3 independent finite reference-oracle campaign.

Runs exact byte-field checks with independent struct/CRC/SHA calculations,
RAM reference arithmetic rather than cache internals, independent integer
source math, and finite power-loss cases. Not a hardware security test.
"""
from __future__ import annotations
import itertools,hashlib,json,random,struct,zlib
from computer_atlas.isa import assemble,encode
from computer_atlas.v03_boot import (encode_boot_image,decode_boot_image,
   ecc_encode_image_payload,ecc_recover_image_payload,BootSlot,select_boot_slot,
   stage_update,BootIntegrityError)
from computer_atlas.v03_cache import SmallRAMCache
from computer_atlas.v03_control import control_flow_certificate
from computer_atlas.v03_workflow import verify_program


def run(seed=20261117):
    rng=random.Random(seed)
    counts={}
    def count(name,n=1):counts[name]=counts.get(name,0)+n
    # Independent decoder for exact 44-byte immutable boot-image specification.
    for _ in range(1000):
        a=rng.randrange(256);b=rng.randrange(256);c=rng.randrange(256)
        rom=assemble(f'LDI R0, {a}\nADDI R0, {b}\nXORI R0, {c}\nHALT')
        img=encode_boot_image(rom)
        magic,version,flags,n,crc,digest=struct.unpack('>4sBBHI32s',img[:44])
        assert magic==b'AT8R' and version==3 and flags==0 and n==len(rom)
        assert crc==zlib.crc32(rom) and digest==hashlib.sha256(rom).digest()
        assert decode_boot_image(img)['rom_sha256']==digest.hex()
        count('boot_header_crosschecked',5)
        # Separate integer-only oracle, independent of AT8 CPU internals.
        expected=((a+b)&255)^c
        p=f'SET {a}\nADD {b}\nXOR {c}\nOUT 0\nHALT'
        r=verify_program(p)
        assert r['register_r0']==expected and r['output_events']==[[0,expected]]
        count('source_to_architectural_execution',2)
    # Exhaustively inject all single/double bit faults at one codeword.
    for _ in range(12):
        a=rng.randrange(256)
        rom=assemble(f'LDI R0, {a}\nHALT');img=encode_boot_image(rom)
        encoded=ecc_encode_image_payload(img)
        for bit in range(13):
            corrupted=list(encoded);corrupted[0]^=1<<bit
            assert ecc_recover_image_payload(corrupted,img)['rom']==rom
            count('ecc_single_correction')
        for i,j in itertools.combinations(range(13),2):
            corrupted=list(encoded);corrupted[0]^=(1<<i)|(1<<j)
            try:ecc_recover_image_payload(corrupted,img)
            except BootIntegrityError:count('ecc_double_detection')
            else:raise AssertionError('ECC double fault was accepted')
    # Power-loss/staged updates are a symbolic process, not flash programming.
    for _ in range(700):
        a=rng.randrange(256);b=rng.randrange(256)
        old=BootSlot(1,encode_boot_image(assemble(f'LDI R0, {a}\nHALT')),True)
        new=assemble(f'LDI R0, {b}\nHALT')
        t=rng.choice(('none','before_data','after_data','after_commit'))
        x,y=stage_update(old,None,new,2,t)
        chosen=select_boot_slot(x,y)
        assert chosen['generation']==(1 if t in ('before_data','after_data') else 2)
        count('two_slot_interruption_selection')
    # Write-through cache equivalence against separate 256-byte RAM state.
    for _ in range(12):
        initial=bytes(rng.randrange(256) for i in range(256))
        ram=bytearray(initial)
        cache=SmallRAMCache(initial,line_size=rng.choice((4,8,16)),line_count=rng.choice((2,4,8)))
        for step in range(1000):
            addr=rng.randrange(256)
            if rng.randrange(3):
                val=rng.randrange(256)
                ram[addr]=val;cache.write(addr,val)
                count('write_through_ram_oracle')
            else:
                assert cache.read(addr)==ram[addr]
                count('cache_load_reference')
        assert cache.ram==ram
        count('whole_ram_equal_after_cache_run')
    # Independent graph reference for 2-byte straight-line programs.
    for _ in range(450):
        count_ops=rng.randint(1,20)
        text='\n'.join(f'LDI R0, {rng.randrange(256)}' for _ in range(count_ops))+'\nHALT'
        rom=assemble(text)
        r=control_flow_certificate(rom)
        assert r['all_paths_to_halt_if_no_trap'] and r['max_instructions_if_no_trap']==count_ops+1
        assert r['reachable_program_counters']==tuple(range(0,len(rom),2))
        count('static_dag_certificate_reference',3)
    return {'schema':'atlas.computer-v03-independent-finite-oracle/1','status':'passed',
       'seed':seed,'comparisons':sum(counts.values()),'groups':counts,
       'isa_unchanged':True,'publisher_source_originals_authenticated':0,
       'external_scientific_review':False,'physical_cpu_fabricated':False,
       'boot_checksum_is_not_signature':True}

if __name__=='__main__':
    receipt=run()
    print(json.dumps(receipt,indent=2))
