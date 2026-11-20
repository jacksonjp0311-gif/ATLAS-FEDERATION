"""ATLAS FORGE AT8/0.1 -- original bounded 8-bit educational ISA.

All opcodes are exactly two bytes [high-nibble opcode|low-nibble register,
8-bit operand]. The AT8 ISA is NOT RISC-V, Beta, Hack, or a commercial ISA.
It is an independently authored, small architectural specification designed
for offline verification and reconstructible teaching experiments.
"""
from __future__ import annotations
from dataclasses import dataclass
import re

OPS = {
    0x0: 'NOP', 0x1: 'LDI', 0x2: 'ADDI', 0x3: 'XORI',
    0x4: 'ANDI', 0x5: 'ORI', 0x6: 'LOAD', 0x7: 'STORE',
    0x8: 'MOV', 0x9: 'JNZ', 0xA: 'JZ', 0xB: 'JMP',
    0xC: 'CMP', 0xD: 'IN', 0xE: 'OUT', 0xF: 'HALT',
}
CODES = {value: key for key,value in OPS.items()}
REGISTER_OPS = frozenset({'LDI','ADDI','XORI','ANDI','ORI','LOAD','STORE','MOV',
                         'JNZ','JZ','CMP','IN','OUT'})
NO_OPERAND = frozenset({'NOP','HALT'})
ONE_OPERAND = frozenset({'JMP'})
BRANCHES = frozenset({'JNZ','JZ','JMP'})
PORTS = frozenset({'IN','OUT'})
IDENT = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')


class AssemblyError(ValueError):
    """Invalid or ambiguous assembly, never silently coerced."""


class DecodeError(ValueError):
    """Invalid machine-code encoding, distinguished from execution traps."""


@dataclass(frozen=True)
class Instruction:
    name: str
    reg: int | None
    operand: int
    pc: int = 0


def _uint8(value: int, what: str) -> int:
    if type(value) is not int or not 0 <= value < 256:
        raise AssemblyError(f'{what}: unsigned byte 0..255 required')
    return value


def _reg(value: int) -> int:
    if type(value) is not int or value not in (0,1,2,3):
        raise AssemblyError('register index must be 0..3')
    return value


def _operand(name: str, reg: int | None, operand: int) -> tuple[int,int]:
    op=name.upper()
    if op not in CODES:
        raise AssemblyError(f'unsupported AT8 mnemonic {op}')
    operand=_uint8(operand,'operand')
    if op in REGISTER_OPS:
        if reg is None:raise AssemblyError(f'{op} requires register')
        reg=_reg(reg)
    else:
        if reg is not None:raise AssemblyError(f'{op} cannot encode register')
        reg=0
    if op in NO_OPERAND and operand!=0:
        raise AssemblyError(f'{op} requires zero reserved operand')
    if op=='MOV' and operand>3:
        raise AssemblyError('MOV source must be R0..R3')
    if op in PORTS and operand>3:
        raise AssemblyError('AT8 abstract input/output port must be 0..3')
    if op in BRANCHES and operand%2:
        raise AssemblyError('branch destination must be 2-byte aligned')
    return reg,operand


def encode(name: str, reg: int | None = None, operand: int = 0) -> bytes:
    op=name.upper()
    r,value=_operand(op,reg,operand)
    return bytes([(CODES[op]<<4) | r,value])


def decode(raw: bytes, pc: int = 0) -> Instruction:
    if not isinstance(raw,bytes) or len(raw)!=2:
        raise DecodeError('fixed-size instruction is exactly two bytes')
    if type(pc) is not int or pc<0 or pc%2:
        raise DecodeError('instruction PC must be nonnegative and aligned')
    high=(raw[0]>>4)&15
    op=OPS.get(high)
    if op is None:raise DecodeError('unsupported opcode')
    reg=raw[0]&15
    if op not in REGISTER_OPS and reg:
        raise DecodeError(f'{op}: reserved low opcode bits must be zero')
    if op in REGISTER_OPS and reg>3:
        raise DecodeError(f'{op}: reserved register encoding')
    try:_operand(op,reg if op in REGISTER_OPS else None,raw[1])
    except AssemblyError as exc:raise DecodeError(str(exc)) from exc
    return Instruction(op,reg if op in REGISTER_OPS else None,raw[1],pc)


def _number(word: str, labels: dict[str,int]) -> int:
    t=word.strip().upper()
    if t in labels:return _uint8(labels[t],f'label {t}')
    if t.startswith(('0X','0B','0O')):
        try:return _uint8(int(t,0),'literal')
        except ValueError as e:raise AssemblyError(f'invalid literal {word}') from e
    if re.fullmatch(r'\d+',t):return _uint8(int(t,10),'literal')
    raise AssemblyError(f'unknown symbol or invalid unsigned constant {word!r}')


def _tokens(text: str) -> list[tuple[int,str]]:
    if not isinstance(text,str):raise AssemblyError('assembly source must be text')
    output=[]
    for line_no,line in enumerate(text.splitlines(),start=1):
        line=line.split(';',1)[0].split('#',1)[0].strip()
        if line:output.append((line_no,line))
    return output


def assemble(text: str) -> bytes:
    """Two-pass, bounded, label-capable assembler. No implicit truncation."""
    labels: dict[str,int]={}
    source=[]
    address=0
    for lineno,line in _tokens(text):
        while ':' in line:
            prefix,tail=line.split(':',1)
            prefix=prefix.strip().upper()
            if not IDENT.fullmatch(prefix):
                raise AssemblyError(f'line {lineno}: invalid label')
            if prefix in labels:raise AssemblyError(f'line {lineno}: duplicate label {prefix}')
            if prefix in CODES:raise AssemblyError(f'line {lineno}: mnemonic used as label')
            labels[prefix]=address
            line=tail.strip()
            if not line:break
        if not line:continue
        source.append((lineno,address,line))
        address+=2
        if address>256:
            raise AssemblyError('AT8 ROM exceeds 256 bytes / 128 instructions')
    if not source:raise AssemblyError('empty program is not runnable')
    code=bytearray()
    for lineno,pc,line in source:
        bits=[p for p in re.split(r'[\s,]+',line.strip()) if p]
        op=bits[0].upper()
        if op not in CODES:raise AssemblyError(f'line {lineno}: unknown opcode {op}')
        if op in NO_OPERAND:
            if len(bits)!=1:raise AssemblyError(f'line {lineno}: {op} takes no arguments')
            code+=encode(op)
        elif op in ONE_OPERAND:
            if len(bits)!=2:raise AssemblyError(f'line {lineno}: {op} takes one target')
            code+=encode(op,None,_number(bits[1],labels))
        else:
            if len(bits)!=3:raise AssemblyError(f'line {lineno}: {op} takes register and operand')
            r=bits[1].upper()
            if not re.fullmatch(r'R[0-3]',r):raise AssemblyError(f'line {lineno}: invalid register {r}')
            value=_number(bits[2],labels)
            code+=encode(op,int(r[1]),value)
    # Reject branches outside the generated image before runtime.
    for pc in range(0,len(code),2):
        inst=decode(bytes(code[pc:pc+2]),pc)
        if inst.name in BRANCHES and inst.operand>=len(code):
            raise AssemblyError(f'branch at PC {pc}: target outside program')
    return bytes(code)


def disassemble(data: bytes) -> str:
    """Canonical assembly with numeric absolute addresses, byte-exact round-trip."""
    if not isinstance(data,bytes) or not data or len(data)>256 or len(data)%2:
        raise DecodeError('AT8 ROM length must be even, 2..256 bytes')
    lines=[]
    for pc in range(0,len(data),2):
        inst=decode(data[pc:pc+2],pc)
        if inst.name in BRANCHES and inst.operand>=len(data):
            raise DecodeError(f'PC {pc}: branch target beyond ROM')
        if inst.name in NO_OPERAND:line=inst.name
        elif inst.name in ONE_OPERAND:line=f'{inst.name} {inst.operand}'
        else:line=f'{inst.name} R{inst.reg}, {inst.operand}'
        lines.append(line)
    return '\n'.join(lines)+'\n'


def validate_rom(data: bytes) -> dict:
    if not isinstance(data,bytes) or len(data)<2 or len(data)%2 or len(data)>256:
        raise DecodeError('ROM size must be an even 2..256 bytes')
    ops=[]
    for i in range(0,len(data),2):
        instr=decode(data[i:i+2],i)
        if instr.name in BRANCHES and instr.operand>=len(data):
            raise DecodeError('absolute branch target outside ROM')
        ops.append(instr.name)
    return {'instructions':len(ops),'bytes':len(data),'opcodes':tuple(ops),
            'has_halt': 'HALT' in ops,'evidence':'byte syntax only, not termination proof'}
