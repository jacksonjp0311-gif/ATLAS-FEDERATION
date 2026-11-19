"""ATLAS FORGE Computer Architecture v0.4: NAND-only AT8 datapath refinement.

This is a symbolic, deterministic finite gate network. It is not transistor RTL,
fabrication evidence, independently characterized delay, silicon timing signoff,
or physical metastability modeling. Unknown inputs use conservative 3-valued NAND.
"""
from __future__ import annotations
from dataclasses import dataclass
import hashlib,json,math


def _bit(value):
    if value is None or (type(value) is int and value in (0,1)):
        return value
    raise ValueError('logic value must be exact 0, 1 or UNKNOWN (None)')


def nand3(a,b):
    a,b=_bit(a),_bit(b)
    if a==0 or b==0:return 1
    if a==1 and b==1:return 0
    return None


def _canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')


@dataclass(frozen=True)
class NandCircuit:
    """Topologically ordered acyclic NAND netlist with named primary inputs."""
    inputs:tuple[str,...]
    gates:tuple[tuple[str,str,str],...]
    outputs:tuple[str,...]
    def __post_init__(self):
        if type(self.inputs) is not tuple or not self.inputs or len(self.inputs)>64:
            raise ValueError('bounded input tuple required')
        if type(self.gates) is not tuple or not (1<=len(self.gates)<=800):
            raise ValueError('bounded nonempty NAND gate list required')
        known=set()
        for n in self.inputs:
            if type(n) is not str or not n or n in known:raise ValueError('duplicate/invalid input')
            known.add(n)
        for gate in self.gates:
            if type(gate) is not tuple or len(gate)!=3:raise ValueError('gate (out,a,b) tuple required')
            out,a,b=gate
            if any(type(n) is not str or not n for n in gate):raise ValueError('named pins required')
            if out in known:raise ValueError('duplicate output/gate alias')
            if a not in known or b not in known:raise ValueError('gate references unknown/future signal')
            known.add(out)
        if type(self.outputs) is not tuple or not self.outputs or any(n not in known for n in self.outputs):
            raise ValueError('output pins absent')
        if len(set(self.outputs))!=len(self.outputs):raise ValueError('duplicate outputs')

    def eval(self,values:dict[str,int|None]):
        if type(values) is not dict or set(values)!=set(self.inputs):raise ValueError('exact primary input set required')
        state={name:_bit(values[name]) for name in self.inputs}
        for out,a,b in self.gates:state[out]=nand3(state[a],state[b])
        return {n:state[n] for n in self.outputs}

    def canonical_netlist(self):
        return {'schema':'atlas.at8-nand-netlist/1','inputs':list(self.inputs),
                'gates':[list(x) for x in self.gates],'outputs':list(self.outputs),
                'physical_cells_characterized':False}

    def sha256(self):return hashlib.sha256(_canonical(self.canonical_netlist())).hexdigest()

    def structural_depth(self):
        """Number of NAND levels. Not time and not a sensitized path proof."""
        depth={n:0 for n in self.inputs}
        for out,a,b in self.gates:depth[out]=1+max(depth[a],depth[b])
        return max(depth[n] for n in self.outputs)

    def gate_delay_bounds(self,min_delay_s,max_delay_s):
        for n,x in [('minimum gate delay',min_delay_s),('maximum gate delay',max_delay_s)]:
            if type(x) not in (int,float) or not math.isfinite(x) or x<0:raise ValueError(n)
        if min_delay_s>max_delay_s:raise ValueError('min exceeds max')
        min_levels={n:0 for n in self.inputs};max_levels={n:0 for n in self.inputs}
        for out,a,b in self.gates:
            min_levels[out]=1+min(min_levels[a],min_levels[b])
            max_levels[out]=1+max(max_levels[a],max_levels[b])
        return {'earliest_s':min(min_levels[n] for n in self.outputs)*min_delay_s,
                'latest_s':max(max_levels[n] for n in self.outputs)*max_delay_s,
                'bounds_are_hypothetical':True,'glitch_and_wire_delays_included':False}


def ripple_adder_netlist(width=8,subtract=False):
    """Nine-NAND-per-bit ripple core (+one input inversion per bit for SUB)."""
    if type(width) is not int or not 1<=width<=16 or type(subtract) is not bool:
        raise ValueError('width 1..16 and Boolean subtract flag')
    primary=tuple(f'a{i}' for i in range(width))+tuple(f'b{i}' for i in range(width))+('c0',)
    gates=[];carry='c0'
    for i in range(width):
        a=f'a{i}';b=f'b{i}'
        if subtract:
            invert=f'bnot{i}'
            gates.append((invert,b,b));b=invert
        n0=f'g{i}_0';n1=f'g{i}_1';n2=f'g{i}_2';x=f'g{i}_x'
        n3=f'g{i}_3';n4=f'g{i}_4';n5=f'g{i}_5';s=f's{i}';ncarry=f'c{i+1}'
        gates.extend(((n0,a,b),(n1,a,n0),(n2,b,n0),(x,n1,n2),
                      (n3,x,carry),(n4,x,n3),(n5,carry,n3),(s,n4,n5),(ncarry,n0,n3)))
        carry=ncarry
    return NandCircuit(primary,tuple(gates),tuple(f's{i}' for i in range(width))+(carry,))


def evaluate_add(a,b,width=8,carry_in=0,subtract=False):
    if type(width) is not int or not 1<=width<=16:raise ValueError('width 1..16 required')
    if type(a) is not int or type(b) is not int or not 0<=a<(1<<width) or not 0<=b<(1<<width):
        raise ValueError('unsigned exact width operands required')
    if type(carry_in) is not int or carry_in not in (0,1):raise ValueError('carry bit 0 or 1')
    if type(subtract) is not bool:raise ValueError('subtract is bool')
    net=ripple_adder_netlist(width,subtract)
    state={f'a{i}':(a>>i)&1 for i in range(width)}
    state.update({f'b{i}':(b>>i)&1 for i in range(width)})
    state['c0']=carry_in
    out=net.eval(state)
    result=sum(out[f's{i}']<<i for i in range(width))
    return {'result':result,'carry':out[f'c{width}'],
            'nand_gates':len(net.gates),'max_gate_levels':net.structural_depth(),
            'netlist_sha256':net.sha256(),'physical_timing_measured':False}


def certify_at8_arithmetic(rom,input_tapes=None,max_steps=1000):
    """Cross-check ISA instruction effects against independent NAND datapath.

    Uses existing atomic and microcycle engines; no ISA extension or true RTL.
    """
    from .spec import SpecMachine,AT8Trap
    from .isa import decode
    from .v02_trace import differential_retirement
    if type(max_steps) is not int or not 1<=max_steps<=10000:
        raise ValueError('step bound 1..10000 required')
    trace=differential_retirement(rom,input_tapes,max_steps=max_steps)
    if not trace['models_agree'] or trace['trap'] or not trace['halted']:
        return {'result':'HOLD','reason':'nonhalt/trap/processor disagreement',
                'physical_hardware_validated':False}
    m=SpecMachine(rom,input_tapes)
    cases=[]
    for index in range(max_steps):
        if m.halted:break
        before=m.snapshot();inst=decode(rom[m.pc:m.pc+2],m.pc)
        event=m.step()
        if inst.name in ('ADDI','CMP'):
            operand=before['regs'][inst.reg]
            sub=inst.name=='CMP'
            got=evaluate_add(operand,inst.operand,8,1 if sub else 0,sub)
            expected=(operand-inst.operand)&255 if sub else (operand+inst.operand)&255
            if got['result']!=expected:raise AssertionError('symbolic adder vs reference integer mismatch')
            actual=event['registers'][inst.reg] if not sub else before['regs'][inst.reg]
            if actual!=(before['regs'][inst.reg] if sub else expected):
                raise AssertionError('AT8 register write/compare mismatch')
            if got['carry']!=event['flags'][2]:raise AssertionError('NAND vs ISA carry differs')
            if event['flags'][0]!=int(expected==0) or event['flags'][1]!=(expected>>7)&1:
                raise AssertionError('NAND vs ISA zero/sign flags differ')
            cases.append({'pc':inst.pc,'op':inst.name,'operand_register':operand,'immediate':inst.operand,
                          'result':expected,'carry':got['carry'],'nand_count':got['nand_gates']})
    return {'schema':'atlas.at8-gate-refinement/1','result':'passed',
            'exercised_arithmetic_instructions':len(cases),'verified_cases':cases,
            'retirement_receipt_sha256':trace['events_sha256'],
            'adder_netlist_sha256':ripple_adder_netlist(8).sha256(),
            'subtractor_netlist_sha256':ripple_adder_netlist(8,True).sha256(),
            'atomic_microcycles_agree':True,'physical_hardware_validated':False}
