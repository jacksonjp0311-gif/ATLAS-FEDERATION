"""Atomic AT8 architectural semantics (reference model A).

Fetch/decode/execute semantics are committed only on a valid instruction.
Program ROM (immutable bytes) is separate from 256-byte RAM, enforcing a
finite memory model. No physical register, clock, transistor or CPU is asserted.
"""
from __future__ import annotations
from dataclasses import dataclass
from .isa import decode, validate_rom, DecodeError


class AT8Trap(ValueError):
    def __init__(self, code: str, pc: int, detail: str = ''):
        self.code=code
        self.pc=pc
        super().__init__(f'{code} at PC=0x{pc:02X}: {detail}')


def _inputs(input_tapes):
    if input_tapes is None:return {i:() for i in range(4)}
    if not isinstance(input_tapes, dict):raise ValueError('input tapes must be port-to-values mapping')
    result={i:() for i in range(4)}
    for port,values in input_tapes.items():
        if type(port) is not int or port not in range(4):raise ValueError('input port 0..3')
        if not isinstance(values,(list,tuple)) or any(type(b) is not int or not 0<=b<256 for b in values):
            raise ValueError('input values must be byte sequences')
        result[port]=tuple(values)
    return result


def _flags(x: int, carry: int = 0, overflow: int = 0) -> tuple[int,int,int,int]:
    return (int(x==0),int(bool(x&128)),int(carry),int(overflow))


class SpecMachine:
    """Finite 4-register AT8 machine, architecture-level golden semantics.

    GPRs R0..R3 and 256 RAM bytes reset to zero. ROM 2..256 bytes, even.
    PC is an absolute byte address, always even. Register reads are read-before-
    write for each instruction. Output events are a trace, not real electrical I/O.
    """
    def __init__(self,rom:bytes,input_tapes=None):
        validate_rom(rom)
        self.rom=rom
        self.regs=[0]*4
        self.ram=[0]*256
        self.pc=0
        self.flags=(1,0,0,0)  # zero, negative, carry, signed overflow on reset
        self.output=[]
        self.inputs=_inputs(input_tapes)
        self.cursor=[0]*4
        self.cycles=0
        self.halted=False

    def snapshot(self):
        return {'pc':self.pc,'regs':tuple(self.regs),'ram':tuple(self.ram),
                'flags':tuple(self.flags),'output':tuple(self.output),
                'input_cursors':tuple(self.cursor),'cycles':self.cycles,
                'halted':self.halted}

    def step(self) -> dict:
        if self.halted:raise AT8Trap('halted',self.pc,'cannot clock a halted model')
        pc=self.pc
        if pc<0 or pc%2 or pc+1>=len(self.rom):
            raise AT8Trap('program_counter',pc,'ROM fetch outside valid aligned word')
        try:inst=decode(self.rom[pc:pc+2],pc)
        except DecodeError as exc:raise AT8Trap('illegal_instruction',pc,str(exc)) from exc
        op=inst.name;r=inst.reg;imm=inst.operand
        # All mutable effects are staged and committed only at the end.
        next_pc=pc+2
        regs=self.regs[:]
        next_flags=self.flags
        ram_write=None;read_port=None;out_event=None
        halt=False
        if op=='LDI':
            regs[r]=imm;next_flags=_flags(regs[r])
        elif op=='ADDI':
            a=regs[r];total=a+imm;result=total&255
            overflow=int(bool((~(a^imm)&(a^result))&128))
            regs[r]=result;next_flags=_flags(result,int(total>255),overflow)
        elif op=='XORI':regs[r]^=imm;next_flags=_flags(regs[r])
        elif op=='ANDI':regs[r]&=imm;next_flags=_flags(regs[r])
        elif op=='ORI':regs[r]|=imm;next_flags=_flags(regs[r])
        elif op=='LOAD':regs[r]=self.ram[imm];next_flags=_flags(regs[r])
        elif op=='STORE':ram_write=(imm,regs[r])
        elif op=='MOV':regs[r]=self.regs[imm];next_flags=_flags(regs[r])
        elif op=='JNZ':
            if regs[r]!=0:next_pc=imm
        elif op=='JZ':
            if regs[r]==0:next_pc=imm
        elif op=='JMP':next_pc=imm
        elif op=='CMP':
            a=regs[r];delta=(a-imm)&255
            overflow=int(bool(((a^imm)&(a^delta))&128))
            next_flags=_flags(delta,int(a>=imm),overflow)
        elif op=='IN':
            if self.cursor[imm]>=len(self.inputs[imm]):
                raise AT8Trap('input_exhausted',pc,f'port {imm} has no available input')
            read_port=imm
            regs[r]=self.inputs[imm][self.cursor[imm]]
            next_flags=_flags(regs[r])
        elif op=='OUT':out_event=(imm,regs[r])
        elif op=='HALT':halt=True
        elif op=='NOP':pass
        else:raise AT8Trap('illegal_instruction',pc,'unhandled operation')
        # Validate the branch before any memory/IO/register effect is committed.
        if op in ('JMP','JZ','JNZ') and (next_pc%2 or next_pc>=len(self.rom)):
            raise AT8Trap('branch_target',pc,'branch target outside ROM')
        if ram_write is not None:self.ram[ram_write[0]]=ram_write[1]
        if read_port is not None:self.cursor[read_port]+=1
        if out_event is not None:self.output.append(out_event)
        self.regs=regs
        self.flags=next_flags
        self.pc=next_pc
        self.cycles+=1
        self.halted=halt
        return {'pc_before':pc,'pc_after':next_pc,'instruction':op,'reg':r,
                'operand':imm,'registers':tuple(regs),'flags':next_flags,
                'ram_write':ram_write,'output':out_event,'cycles':self.cycles,'halted':halt}

    def run(self,max_steps:int=1000):
        if type(max_steps) is not int or not 1<=max_steps<=100000:
            raise ValueError('max_steps must be bounded integer 1..100000')
        trace=[]
        while not self.halted and len(trace)<max_steps:
            trace.append(self.step())
        return {'halted':self.halted,'stop_reason':'halted' if self.halted else 'bounded_step_budget',
                'steps':len(trace),'trace':trace,'snapshot':self.snapshot(),
                'physical_hardware_verified':False}
