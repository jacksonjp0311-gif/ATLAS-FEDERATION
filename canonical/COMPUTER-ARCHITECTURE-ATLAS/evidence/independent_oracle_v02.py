#!/usr/bin/env python3
"""Independent software verification suite for ATLAS v0.2 bootstrap/ROM integrity.

Finite program executions, independent parity-matrix encoding, reference
interpreter, atomic ISA and microcycle retirement. NOT fabricated hardware.
"""
import hashlib,itertools,json,random
from computer_atlas.isa import assemble
from computer_atlas.v02_bootstrap import compile_source,evaluate_source
from computer_atlas.v02_ecc import encode_byte,decode_word
from computer_atlas.v02_control import control_flow_analysis
from computer_atlas.v02_trace import differential_retirement,physical_evidence_matrix,PHYSICAL_GATES
from computer_atlas.spec import SpecMachine
from computer_atlas.microcoded import MicrocodedMachine

# Independent GF(2) generator from linear parity incidence (not copied byte encoding).
_PARITY=(1,2,4,8)
_DATA=(3,5,6,7,9,10,11,12)

def independent_hamming(byte):
    slots={p:(byte>>i)&1 for i,p in enumerate(_DATA)}
    for p in _PARITY:
        slots[p]=0
        slots[p]=sum(v for j,v in slots.items() if j<=12 and j&p)&1
    slots[13]=sum(slots.values())&1
    return sum(v<<(j-1) for j,v in slots.items())


def reference_run(rom,input_tapes=None,max_steps=1000):
    """Use ISA machine's separate atomic model, not v02 trace helpers."""
    m=SpecMachine(rom,input_tapes)
    return m.run(max_steps=max_steps)


def run(seed=20261116):
    rng=random.Random(seed)
    counter={};samples=[]
    def check(cat,yes):
        if not yes:raise AssertionError('mismatch: '+cat)
        counter[cat]=counter.get(cat,0)+1

    for data in range(256):
        code=encode_byte(data)
        check('independent_13_8_generator',code==independent_hamming(data))
        check('clean_13_8_decoder',decode_word(code)['byte']==data)
        for p in range(13):
            a=decode_word(code^(1<<p))
            check('one_bit_error_correction',a['byte']==data and a['corrected_word']==code)
        for i,j in itertools.combinations(range(13),2):
            a=decode_word(code^(1<<i)^(1<<j))
            check('two_bit_error_detection',a['status']=='detected_double' and a['byte'] is None)

    # Exhaustive finite input/output sequences in a small structured language.
    for initial in range(256):
        for inc in range(256):
            src=f'SET {initial}\nADD {inc}\nXOR 165\nSTORE 3\nOUT 0\nHALT'
            rom=compile_source(src)
            expected=(initial+inc)&255
            result=reference_run(rom)
            output=expected^165
            check('bootstrap_exhaustive_8bit_add',result['snapshot']['ram'][3]==output and
                  result['snapshot']['output']==((0,output),))
            if initial%71==0 and inc%71==0:
                trace=differential_retirement(rom)
                check('bootstrap_full_trace_sample',trace['models_agree'] and trace['halted'])

    # Random structured source, compare AST evaluator, atomic ISA, microcycle stages.
    for index in range(850):
        init=rng.randrange(256);a=rng.randrange(256);b=rng.randrange(256)
        depth=rng.randrange(1,4)
        src=[f'SET {init}']
        for i in range(depth):src.append(f'REPEAT {rng.randrange(1,5)}')
        src.extend([f'ADD {a}',f'XOR {b}','STORE 17','OUT 2'])
        for i in range(depth):src.append('END')
        src.append('HALT')
        script='\n'.join(src)
        rom=compile_source(script)
        oracle=evaluate_source(script)
        a_run=reference_run(rom)
        m_run=MicrocodedMachine(rom).run()
        ac=a_run['snapshot'];mi=m_run['snapshot']
        check('ast_vs_atomic_accumulator',ac['regs'][0]==oracle['accumulator'])
        check('ast_vs_atomic_output',ac['output']==oracle['output'])
        check('ast_vs_atomic_ram',ac['ram']==oracle['ram'])
        check('atomic_vs_microcycle',ac==mi)
        report=control_flow_analysis(rom)
        check('source_halt_reachable',bool(report['reachable_halts']))
        if index<6:
            samples.append({'source_sha256':hashlib.sha256(script.encode()).hexdigest(),
              'rom_sha256':hashlib.sha256(rom).hexdigest(),
              'accumulator':ac['regs'][0], 'output_events':len(ac['output']),
              'microcycle_state_match':ac==mi})

    # Bounded conservative graph property and asserted metadata non-certification.
    for n in range(1,51):
        rom=assemble('LDI R0,7\n'+'NOP\n'*n+'HALT')
        report=control_flow_analysis(rom)
        check('acyclic_must_halt_structural',report['all_structural_paths_terminate_at_halt'])
    report=physical_evidence_matrix({k:{'claimed':True} for k in PHYSICAL_GATES})
    check('metadata_not_physical_certification',len(report['unverified_types'])==12 and
          report['physical_manufacturing_acceptance']=='HOLD')
    return {'schema':'atlas.at8-v02-independent-finite-oracle/1','status':'passed',
      'seed':seed,'comparisons':sum(counter.values()),'groups':counter,
      'bootstrap_samples':samples,'physical_evidence_types_missing':12,
      'human_scientific_review':False,'physical_cpu_fabricated':False,
      'publisher_original_transport_authenticated':0,
      'scope':'finite independent software models, not silicon fabrication or hardware validation'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
