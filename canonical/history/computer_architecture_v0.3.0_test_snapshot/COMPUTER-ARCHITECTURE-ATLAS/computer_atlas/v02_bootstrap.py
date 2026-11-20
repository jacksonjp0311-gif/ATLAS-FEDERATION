"""ATLAS FORGE Computer Architecture 0.2 — original bounded structured AT8 compiler.

A tiny higher-level language compiles into the UNCHANGED AT8 v0.1 ISA. Its
independent source evaluator provides a separate semantic oracle. This is a
compiler *bootstrap demonstration*, NOT a general compiler, an OS, hardware, or
an authenticity proof of physical execution.

Statements: SET/ADD/XOR/AND/OR <byte>, LOAD/STORE <address>, IN/OUT <port>,
REPEAT <1..255> / END (max three nesting levels), HALT (once, last).
Only R0 is visible; R3..R1 are reserved for loop counters. ROM <=256 bytes.
"""
from __future__ import annotations
from dataclasses import dataclass
import hashlib, json, re
from .isa import assemble

@dataclass(frozen=True)
class Statement:
    op: str
    val: int = 0
    body: tuple['Statement', ...] = ()

_ARITH=frozenset({'SET','ADD','XOR','AND','OR'})
_MEM=frozenset({'STORE','LOAD'})
_PORT=frozenset({'IN','OUT'})
_OPERANDS=_ARITH|_MEM|_PORT|{'REPEAT'}


def parse_source(source: str) -> tuple[Statement,...]:
    if not isinstance(source,str) or not source.strip():raise ValueError('nonempty source text required')
    top=[];frames=[top];counts=[]
    lines=source.splitlines()
    if len(lines)>2000:raise ValueError('source too long')
    for num,raw in enumerate(lines,1):
        line=raw.split('#',1)[0].split(';',1)[0].strip()
        if not line:continue
        tok=line.upper().split()
        op=tok[0]
        if op=='END':
            if len(tok)!=1 or len(frames)==1:raise ValueError(f'line {num}: unmatched END')
            body=tuple(frames.pop());count=counts.pop()
            if not body:raise ValueError('empty repeat block')
            frames[-1].append(Statement('REPEAT',count,body))
        elif op=='REPEAT':
            if len(tok)!=2 or not re.fullmatch(r'\d+',tok[1]):raise ValueError(f'line {num}: repeat requires decimal count')
            n=int(tok[1]);
            if not 1<=n<=255 or len(frames)>3:raise ValueError('repeat count/depth outside bounded range')
            frames.append([]);counts.append(n)
        elif op in _OPERANDS:
            if len(tok)!=2 or not re.fullmatch(r'\d+',tok[1]):raise ValueError(f'line {num}: byte operand expected')
            val=int(tok[1]);limit=3 if op in _PORT else 255
            if val>limit:raise ValueError(f'line {num}: operand out of range')
            frames[-1].append(Statement(op,val))
        elif op=='HALT':
            if len(tok)!=1 or len(frames)!=1:raise ValueError('HALT must occur at top level')
            frames[-1].append(Statement('HALT'))
        else:raise ValueError(f'line {num}: unsupported construct {op}')
    if len(frames)!=1:raise ValueError('unclosed REPEAT block')
    if not top or top[-1].op!='HALT' or any(s.op=='HALT' for s in top[:-1]):
        raise ValueError('exactly one terminal HALT required')
    return tuple(top)


def compile_source(source: str) -> bytes:
    program=parse_source(source);out=[];nonce=0
    def emit(stmts,depth=0):
        nonlocal nonce
        for s in stmts:
            op=s.op;val=s.val
            if op=='REPEAT':
                if depth>=3:raise ValueError('nesting beyond reserved registers')
                r=3-depth;nonce+=1;mark=f'__LOOP_{nonce}'
                out.append(f'LDI R{r}, {val}')
                out.append(f'{mark}:')
                emit(s.body,depth+1)
                out.append(f'ADDI R{r}, 255')
                out.append(f'JNZ R{r}, {mark}')
            elif op=='HALT':out.append('HALT')
            elif op=='SET':out.append(f'LDI R0, {val}')
            elif op in ('ADD','XOR','AND','OR'):
                out.append(f'{op}I R0, {val}')
            else:out.append(f'{op} R0, {val}')
    emit(program)
    if len([s for s in out if not s.endswith(':')])>128:
        raise ValueError('compiled program exceeds AT8 instruction bound')
    return assemble('\n'.join(out))


def evaluate_source(source: str, input_tapes: dict[int,list[int]|tuple[int,...]]|None=None,
                    max_operations: int=100000):
    """Independent AST evaluator with no AT8 machine-code invocation.

    One operation counted per primitive statement, including HALT and each
    REPEAT dispatch, not an equivalent count of AT8 microticks/instructions.
    """
    program=parse_source(source)
    if type(max_operations) is not int or not 1<=max_operations<=100000:
        raise ValueError('operation limit must be bounded')
    if input_tapes is None:input_tapes={}
    if not isinstance(input_tapes,dict) or any(type(k) is not int or k not in range(4) or
      not isinstance(v,(list,tuple)) or any(type(b) is not int or not 0<=b<256 for b in v) for k,v in input_tapes.items()):
        raise ValueError('invalid external input tape')
    tape={k:tuple(input_tapes.get(k,())) for k in range(4)}
    cursor={k:0 for k in range(4)}
    acc=0;ram=[0]*256;output=[];steps=0;halt=False
    def execute(block):
        nonlocal acc,steps,halt
        for s in block:
            steps+=1
            if steps>max_operations:raise ValueError('source execution budget exceeded')
            op=s.op;v=s.val
            if op=='REPEAT':
                for _ in range(v):execute(s.body)
            elif op=='SET':acc=v
            elif op=='ADD':acc=(acc+v)&255
            elif op=='XOR':acc^=v
            elif op=='AND':acc&=v
            elif op=='OR':acc|=v
            elif op=='STORE':ram[v]=acc
            elif op=='LOAD':acc=ram[v]
            elif op=='IN':
                if cursor[v]>=len(tape[v]):raise ValueError('source input exhausted')
                acc=tape[v][cursor[v]];cursor[v]+=1
            elif op=='OUT':output.append((v,acc))
            elif op=='HALT':halt=True
    execute(program)
    return {'accumulator':acc,'ram':tuple(ram),'output':tuple(output),
            'input_cursors':tuple(cursor[i] for i in range(4)),
            'halted':halt,'source_operations':steps,'physical_computer_verified':False}


def compile_receipt(source: str, input_tapes=None, max_operations: int=100000):
    """Source-to-ROM evidence receipt; SHA hashes establish byte identity only."""
    raw=source.encode('utf-8');rom=compile_source(source)
    expected=evaluate_source(source,input_tapes,max_operations)
    return {'schema':'atlas.computer-at8-bootstrap/1','source_sha256':hashlib.sha256(raw).hexdigest(),
      'rom_sha256':hashlib.sha256(rom).hexdigest(),'rom_bytes':len(rom),
      'reference_output':list(map(list,expected['output'])),
      'reference_register_accumulator':expected['accumulator'],
      'source_operations':expected['source_operations'],
      'evidence_grade':'constructed software trace only, not hardware certification'}
