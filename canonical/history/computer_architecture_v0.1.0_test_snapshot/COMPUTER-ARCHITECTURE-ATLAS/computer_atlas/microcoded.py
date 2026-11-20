"""AT8 independent microcycle execution implementation B.

Four symbolic stages per instruction: FETCH -> DECODE -> EXECUTE -> COMMIT.
The execute stage uses NAND-only arithmetic in `gates.alu8`; unlike the atomic
specification, this decomposes clocked behavior. It is NOT transistor RTL,
verified timing closure or a physical CPU.
"""
from __future__ import annotations
from .isa import validate_rom, OPS
from .gates import alu8
from .spec import AT8Trap, _inputs


class MicrocodedMachine:
    def __init__(self,rom:bytes,input_tapes=None):
        validate_rom(rom)
        self.rom=rom
        self.regs=[0]*4
        self.ram=[0]*256
        self.pc=0
        self.flags=(1,0,0,0)
        self.output=[]
        self.inputs=_inputs(input_tapes)
        self.cursor=[0]*4
        self.halted=False
        self.cycles=0
        self.microticks=0
        self.phase='FETCH'
        self.latch=None
        self.pending=None

    def snapshot(self):
        return {'pc':self.pc,'regs':tuple(self.regs),'ram':tuple(self.ram),
                'flags':tuple(self.flags),'output':tuple(self.output),
                'input_cursors':tuple(self.cursor),'cycles':self.cycles,
                'halted':self.halted}

    def tick(self):
        if self.halted:raise AT8Trap('halted',self.pc,'microcycle on halted machine')
        pc=self.pc
        if self.phase=='FETCH':
            if pc<0 or pc%2 or pc+1>=len(self.rom):
                raise AT8Trap('program_counter',pc,'invalid program address')
            self.latch=(self.rom[pc],self.rom[pc+1])
            self.phase='DECODE'
            result={'stage':'FETCH','pc':pc,'data':self.latch}
        elif self.phase=='DECODE':
            top,imm=self.latch
            op=OPS.get(top>>4)
            reg=top&15
            if op is None or (op in ('NOP','JMP','HALT') and reg!=0) or (op not in ('NOP','JMP','HALT') and reg>3):
                raise AT8Trap('illegal_instruction',pc,'reserved bits')
            if op in ('NOP','HALT') and imm!=0:raise AT8Trap('illegal_instruction',pc,'nonzero reserved operand')
            if op=='MOV' and imm>3:raise AT8Trap('illegal_instruction',pc,'MOV source R0..R3')
            if op in ('IN','OUT') and imm>3:raise AT8Trap('illegal_instruction',pc,'port 0..3')
            if op in ('JMP','JZ','JNZ') and (imm%2 or imm>=len(self.rom)):
                raise AT8Trap('branch_target',pc,'target invalid')
            self.latch=(op,reg,imm)
            self.phase='EXECUTE'
            result={'stage':'DECODE','pc':pc,'operation':op,'reg':reg,'operand':imm}
        elif self.phase=='EXECUTE':
            op,r,imm=self.latch
            old=self.regs
            regs=old[:]
            flags=self.flags
            nextpc=pc+2
            memwrite=None;inport=None;output=None;halt=False
            if op=='NOP':pass
            elif op=='LDI':regs[r]=imm
            elif op=='ADDI':
                alu=alu8(old[r],imm,'ADD')
                regs[r]=alu['value']
                flags=tuple(alu[k] for k in ('zero','negative','carry','overflow'))
            elif op in ('ANDI','ORI','XORI'):
                alu=alu8(old[r],imm,{'ANDI':'AND','ORI':'OR','XORI':'XOR'}[op]);regs[r]=alu['value']
            elif op=='LOAD':regs[r]=self.ram[imm]
            elif op=='STORE':memwrite=(imm,old[r])
            elif op=='MOV':regs[r]=old[imm]
            elif op=='JNZ':
                if old[r]:nextpc=imm
            elif op=='JZ':
                if not old[r]:nextpc=imm
            elif op=='JMP':nextpc=imm
            elif op=='CMP':
                flags_alu=alu8(old[r],imm,'CMP')
                flags=tuple(flags_alu[k] for k in ('zero','negative','carry','overflow'))
            elif op=='IN':
                if self.cursor[imm]>=len(self.inputs[imm]):
                    raise AT8Trap('input_exhausted',pc,f'input port {imm}')
                regs[r]=self.inputs[imm][self.cursor[imm]];inport=imm
            elif op=='OUT':output=(imm,old[r])
            elif op=='HALT':halt=True
            else:raise AT8Trap('illegal_instruction',pc,op)
            if op in ('LDI','ANDI','ORI','XORI','LOAD','MOV','IN'):
                x=regs[r];flags=(int(x==0),int(bool(x&128)),0,0)
            self.pending={'regs':regs,'flags':flags,'pc':nextpc,'memwrite':memwrite,
                          'inport':inport,'output':output,'halt':halt,'name':op,'reg':r,'imm':imm}
            self.phase='COMMIT'
            result={'stage':'EXECUTE','pc':pc,'pending_op':op}
        elif self.phase=='COMMIT':
            p=self.pending
            # All effects become architecturally visible together.
            if p['memwrite'] is not None:self.ram[p['memwrite'][0]]=p['memwrite'][1]
            if p['inport'] is not None:self.cursor[p['inport']]+=1
            if p['output'] is not None:self.output.append(p['output'])
            self.regs=p['regs']
            self.flags=p['flags']
            self.pc=p['pc']
            self.cycles+=1
            self.halted=p['halt']
            result={'stage':'COMMIT','pc':pc,'operation':p['name'],
                    'registers':tuple(self.regs),'flags':self.flags,
                    'ram_write':p['memwrite'],'output':p['output'],'halted':self.halted}
            self.phase='FETCH'
            self.latch=None
            self.pending=None
        else:raise AT8Trap('microstage_invalid',pc,'invalid microcycle state')
        self.microticks+=1
        return result

    def step_instruction(self):
        if self.halted:raise AT8Trap('halted',self.pc)
        if self.phase!='FETCH':raise AT8Trap('uncommitted',self.pc,'must begin at FETCH')
        sequence=[]
        for _ in range(4):sequence.append(self.tick())
        if sequence[-1]['stage']!='COMMIT':raise AT8Trap('microstage_invalid',self.pc)
        return {'microcycles':sequence,'snapshot':self.snapshot()}

    def run(self,max_instructions:int=1000):
        if type(max_instructions) is not int or not 1<=max_instructions<=100000:
            raise ValueError('bounded positive instruction budget required')
        events=[]
        while not self.halted and len(events)<max_instructions:
            events.append(self.step_instruction())
        return {'halted':self.halted,'stop_reason':'halted' if self.halted else 'bounded_instruction_budget',
                'steps':len(events),'microcycles':self.microticks,'events':events,
                'snapshot':self.snapshot(),'fabricated_cpu':False}
