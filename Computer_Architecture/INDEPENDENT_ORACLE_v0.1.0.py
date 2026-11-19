#!/usr/bin/env python3
"""Third independent AT8 interpreter and finite differential evidence generator.

Original ATLAS FORGE computer architecture. Does not call the architectural
machine's step(), the microcoded tick(), or NAND ALU to compute expected values.
Constructed software comparison only, not fabricated hardware or peer review.
"""
import json,random,itertools,hashlib,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from computer_atlas.isa import assemble,disassemble,encode
from computer_atlas.spec import SpecMachine
from computer_atlas.microcoded import MicrocodedMachine
from computer_atlas.gates import alu8
from computer_atlas.programs import examples


def independent_machine(code,inputs=None,budget=256):
    """Separate byte-by-byte interpreter, with independent flag arithmetic.

    The machine source is intentionally short and NOT shared with either DUT.
    The input is a valid, bounded AT8 ROM; traps are tested separately.
    """
    regs=[0,0,0,0];ram=[0]*256;flags=(1,0,0,0);pc=0;out=[]
    tapes={i:tuple((inputs or {}).get(i,())) for i in range(4)}
    cursors=[0,0,0,0];cycles=0;halt=False
    while cycles<budget and not halt:
        if pc<0 or pc+1>=len(code) or pc%2:raise ValueError('reference ROM fell off')
        hi=code[pc];b=code[pc+1]
        op=hi>>4;r=hi&15
        nextpc=pc+2
        if op==0:
            if r or b:raise ValueError('bad NOP')
        elif op==1:regs[r]=b;flags=(int(b==0),b>>7,0,0)
        elif op==2:
            before=regs[r];z=(before+b)&255
            flags=(int(z==0),z>>7,int(before+b>255),int(bool((~(before^b)&(before^z))&128)))
            regs[r]=z
        elif op in (3,4,5):
            z={3:lambda:regs[r]^b,4:lambda:regs[r]&b,5:lambda:regs[r]|b}[op]()
            regs[r]=z;flags=(int(z==0),z>>7,0,0)
        elif op==6:
            z=ram[b];regs[r]=z;flags=(int(z==0),z>>7,0,0)
        elif op==7:ram[b]=regs[r]
        elif op==8:
            if b>3:raise ValueError('bad MOV')
            z=regs[b];regs[r]=z;flags=(int(z==0),z>>7,0,0)
        elif op==9:
            if regs[r]:nextpc=b
        elif op==10:
            if not regs[r]:nextpc=b
        elif op==11:
            if r:raise ValueError('bad JMP')
            nextpc=b
        elif op==12:
            a=regs[r];z=(a-b)&255
            flags=(int(z==0),z>>7,int(a>=b),int(bool(((a^b)&(a^z))&128)))
        elif op==13:
            if cursors[b]>=len(tapes[b]):raise ValueError('missing oracle input')
            z=tapes[b][cursors[b]];regs[r]=z;cursors[b]+=1
            flags=(int(z==0),z>>7,0,0)
        elif op==14:out.append((b,regs[r]))
        elif op==15:
            if r or b:raise ValueError('bad HALT')
            halt=True
        else:raise ValueError('invalid machine opcode')
        pc=nextpc;cycles+=1
    return {'pc':pc,'regs':tuple(regs),'ram':tuple(ram),'flags':flags,
            'output':tuple(out),'input_cursors':tuple(cursors),'cycles':cycles,'halted':halt}


def run():
    rng=random.Random(20261117)
    tally={};errors=[]
    def verify(name,test,detail=None):
        if not test:raise AssertionError(f'{name}: {detail}')
        tally[name]=tally.get(name,0)+1

    # Exact gate calculation vs independent arithmetic across full 8-bit space.
    for a in range(256):
        for b in range(256):
            g=alu8(a,b,'ADD')
            z=a+b
            verify('exhaustive_gate_8bit_add',g['value']==(z&255) and g['carry']==int(z>255), (a,b,g))
            verify('exhaustive_gate_signed_overflow',g['overflow']==int(bool((~(a^b)&(a^(z&255)))&128)),(a,b))
    # Third interpreter vs atomic spec vs four-stage microcycles, hundreds of
    # randomly generated instruction streams and IO events, deterministic seeds.
    choices=['LDI','ADDI','XORI','ANDI','ORI','LOAD','STORE','MOV','CMP','OUT','IN']
    for i in range(700):
        program=[];ports={p:[rng.randrange(256) for _ in range(12)] for p in range(4)}
        for _ in range(rng.randrange(3,18)):
            op=rng.choice(choices)
            r=rng.randrange(4)
            imm=rng.randrange(4) if op in ('MOV','IN','OUT') else rng.randrange(256)
            program.append(encode(op,r,imm))
        program.append(encode('HALT'))
        blob=b''.join(program)
        if len(blob)>256:raise AssertionError('program exceeded ROM')
        spec=SpecMachine(blob,ports).run(100)
        micro=MicrocodedMachine(blob,ports).run(100)
        oracle=independent_machine(blob,ports,100)
        verify('third_oracle_vs_architecture',spec['snapshot']==oracle,(i,'spec mismatch'))
        verify('third_oracle_vs_microcoded',micro['snapshot']==oracle,(i,'micro mismatch'))
        verify('roundtrip_disassembly',assemble(disassemble(blob))==blob,i)
        verify('four_microcycles_per_instruction',micro['microcycles']==4*spec['steps'],i)
    # Control-flow programs exercise branches and bounded loops.
    for p in [examples()['countdown'],examples()['arithmetic_memory'],examples()['input_output']]:
        input_tapes={1:[7]} if p==examples()['input_output'] else {}
        s=SpecMachine(p,input_tapes).run(100)
        m=MicrocodedMachine(p,input_tapes).run(100)
        v=independent_machine(p,input_tapes)
        verify('branch_control_execution_three_way',s['snapshot']==m['snapshot']==v)
        verify('program_halts',v['halted'])
    # Exhaustive one-instruction immediate+state spec from actual machine execution.
    for a in range(256):
        for b in (0,1,127,128,254,255):
            program=bytes((0x10,a,0x20,b,0xf0,0))
            s=SpecMachine(program)
            s.step();s.step()
            verify('atomic_addi_reg_and_carry',s.regs[0]==((a+b)&255) and s.flags[2]==int(a+b>255))
    # Invalid cases must be refused before any state/port/memory effect.
    p=assemble('IN R0, 0\nHALT')
    s=SpecMachine(p);before=s.snapshot()
    try:s.step()
    except Exception:verify('input_exhaustion_atomic',s.snapshot()==before)
    else:raise AssertionError('missing input not refused')
    return {'schema':'atlas.at8-independent-oracle/1','status':'passed',
            'seed':20261117,'groups':tally,'compared_cases':sum(tally.values()),
            'microcoded_distinct_from_atomic_spec':True,
            'third_interpreter_separate':True,'physical_cpu_demonstrated':False,
            'manufacturing_characterization_supplied':False,
            'source_originals_authenticated':0,'independent_human_review':False,
            'claims':'finite software and constructed oracle evidence, not physically calibrated devices'}

if __name__=='__main__':
    receipt=run()
    print(json.dumps(receipt,indent=2))
    if len(sys.argv)>1:
        p=Path(sys.argv[1]);p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(receipt,indent=2)+'\n')
