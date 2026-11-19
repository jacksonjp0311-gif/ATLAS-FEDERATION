#!/usr/bin/env python3
"""Independent finite AT8 v0.4 verification, not laboratory or expert review."""
import json,hashlib,random,itertools,math
from computer_atlas.v04_gatelevel import evaluate_add,nand3,ripple_adder_netlist,certify_at8_arithmetic
from computer_atlas.v04_memory import HarvardBus,ParityByteMemory,RoundRobinArbiter
from computer_atlas.v04_bootstrap import bootstrap_certificate
from computer_atlas.isa import assemble


def run():
    counts={};seed=20261117; rng=random.Random(seed)
    def check(name,got,ref):
        if got!=ref:raise AssertionError((name,got,ref))
        counts[name]=counts.get(name,0)+1
    # Two independent oracles: Python's arbitrary-precision addition and
    # complement-plus-one subtraction; the DUT traverses its NAND gate network.
    for a in range(256):
        for b in range(256):
            x=evaluate_add(a,b,8)
            check('exhaustive_nand_add_result',(x['result'],x['carry']),((a+b)&255,(a+b)>>8))
            y=evaluate_add(a,b,8,1,True)
            check('exhaustive_nand_sub_result',(y['result'],y['carry']),((a-b)&255,int(a>=b)))
    for a,b,carry in itertools.product((0,1),repeat=3):
        x=evaluate_add(a,b,1,carry)
        check('full_adder_truth',(x['result'],x['carry']),((a+b+carry)&1,(a+b+carry)>>1))
    # Independent strong-Kleene NAND truth reference, including X propagation.
    for a,b in itertools.product((0,1,None),repeat=2):
        expect=1 if 0 in (a,b) else 0 if a==1 and b==1 else None
        check('three_valued_logic',nand3(a,b),expect)
    # Bounded random large widths and netlist canonical stability.
    for w in (4,12,16):
        for i in range(400):
            a=rng.randrange(1<<w);b=rng.randrange(1<<w);carry=i%2
            x=evaluate_add(a,b,w,carry)
            check('mixed_width_arithmetic',x['result']+(x['carry']<<w),a+b+carry)
    # Fault model explicitly demonstrates parity's double-bit blind spot.
    for value in range(256):
        for bit in range(8):
            p=ParityByteMemory(1);p.write(0,value);p.inject_data_flip(0,1<<bit)
            check('parity_single_error_detected',p.read(0)['status'],'detected_parity_error')
        p=ParityByteMemory(1);p.write(0,value);p.inject_data_flip(0,0b11)
        check('parity_double_error_not_guaranteed',p.read(0)['status'],'parity_consistent_not_authentic')
    # Fairness and type safety under independent round robin oracle.
    for n in range(2,12):
        a=RoundRobinArbiter(n)
        for i in range(n*40):
            check('rr_full_load',a.tick([1]*n),i%n)
    for i in range(256):
        m=HarvardBus(assemble('HALT'))
        m.write(i,(i*17)&255)
        check('Harvard_RAM_readback',m.read(i),(i*17)&255)
    # Source to ROM to processor+NAND coverage (two separate source programs).
    programs=['SET 5\nADD 7\nSTORE 0\nXOR 3\nOUT 0\nHALT',
              'SET 3\nREPEAT 3\nADD 1\nEND\nOUT 0\nHALT']
    for src in programs:
        a=bootstrap_certificate(src)
        b=bootstrap_certificate(src)
        check('bootstrap_reproducible_receipts',a['receipt_sha256'],b['receipt_sha256'])
        check('bootstrap_software_checked',a['syntax_assembler_processor_gate_checks'],'passed')
        check('bootstrap_physical_hold',a['physical_CPU_demonstrated'],False)
    total=sum(counts.values())
    return {'schema':'atlas.at8-v04-independent-finite-oracle/1','result':'passed','seed':seed,
       'comparisons':total,'groups':counts,'nand_add_sha256':ripple_adder_netlist(8).sha256(),
       'physical_devices_tested':0,'hardware_signed_firmware_authenticated':False,
       'independent_expert_science_review':False,'note':'independently coded software/numeric checks only'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
