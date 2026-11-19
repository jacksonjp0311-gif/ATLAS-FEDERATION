"""Compiler Design Atlas v0.2.0 — typed, finite register IR and independent VM.

This is a SECOND backend, not an external machine-code compiler or LLVM IR.
Register types are fixed. Control flow is acyclic. Join registers can be
written once on each mutually exclusive path; the verifier checks definite
initialization across every incoming edge by intersection of must-def facts.
Finite agreement does not constitute a universal compiler-correctness proof.
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import deque
from hashlib import sha256
import json
from .core import (parse, infer, typecheck, optimize, calc, MIN_I32, MAX_I32,
    MAX_INSNS, MAX_SLOTS, CompileError, Trap, Lit, Var, Unary, Binary, If)

MAX_REGISTERS=32768
_LANG='atlas-compiler-typed-registers/1'
_OPS={'+':'ADD','-':'SUB','*':'MUL','/':'DIV','<':'LT','==':'EQ'}

@dataclass(frozen=True)
class RegisterCode:
    instructions:tuple[tuple[str,tuple],...]
    register_types:tuple[str,...]
    slots:tuple[str,...]

def lower(source:str,optimized:bool=False)->RegisterCode:
    """Pratt AST -> typed three-address register VM.

    The backend performs only bounded lowering; errors/traps have the same
    declared observable meaning as the first backend for well-typed programs.
    """
    program=parse(source)
    types=typecheck(program)
    register_types=[];ops=[];slots={}
    def fresh(t):
        if t not in ('i32','bool') or len(register_types)>=MAX_REGISTERS:
            raise CompileError('register type/count bound')
        i=len(register_types);register_types.append(t);return i
    def emit(name,*args):
        if len(ops)>=MAX_INSNS:raise CompileError('register program length budget')
        ops.append((name,tuple(args)))
        return len(ops)-1
    def patch(i,argument):
        name,args=ops[i];assert name in ('BR_FALSE','JUMP')
        ops[i]=(name,args[:-1]+(argument,))
    def compile_expr(e):
        if isinstance(e,Lit):
            r=fresh('bool' if type(e.value) is bool else 'i32')
            emit('CONST_BOOL' if type(e.value) is bool else 'CONST_I32',r,e.value)
            return r
        if isinstance(e,Var):
            if e.name not in slots:raise CompileError('undefined backend local')
            r=fresh('i32');emit('LOAD_LOCAL',r,slots[e.name]);return r
        if isinstance(e,Unary):
            a=compile_expr(e.arg);r=fresh('i32');emit('NEG',r,a);return r
        if isinstance(e,Binary):
            a=compile_expr(e.lhs);b=compile_expr(e.rhs)
            t='bool' if e.op in ('<','==') else 'i32'
            r=fresh(t);emit(_OPS[e.op],r,a,b);return r
        if isinstance(e,If):
            cond=compile_expr(e.cond)
            out=fresh(infer(e,types))
            i_branch=emit('BR_FALSE',cond,-1)
            y=compile_expr(e.yes)
            emit('COPY',out,y)
            i_end=emit('JUMP',-1)
            patch(i_branch,len(ops))
            n=compile_expr(e.no)
            emit('COPY',out,n)
            patch(i_end,len(ops))
            return out
        raise CompileError('unknown expression in register backend')
    for stmt in program.statements:
        slots[stmt.name]=len(slots)
        if len(slots)>MAX_SLOTS:raise CompileError('too many locals')
        value=compile_expr(optimize(stmt.value) if optimized else stmt.value)
        emit('STORE_LOCAL',slots[stmt.name],value)
    output=compile_expr(optimize(program.result) if optimized else program.result)
    emit('RETURN',output)
    code=RegisterCode(tuple(ops),tuple(register_types),tuple(slots))
    verify_registers(code)
    return code

def verify_registers(code:RegisterCode)->dict:
    """Independent forward must-definite analysis for forward-only control flow.

    At a CFG join: initialized=intersection(incoming initialized sets).
    This rejects register use that is defined on only one predecessor path.
    """
    if not isinstance(code,RegisterCode):raise CompileError('register code required')
    ins=code.instructions;n=len(ins);rtypes=code.register_types;slots=code.slots
    if not (0<n<=MAX_INSNS and len(rtypes)<=MAX_REGISTERS and len(slots)<=MAX_SLOTS):
        raise CompileError('bad register program shape')
    if any(t not in ('i32','bool') for t in rtypes):raise CompileError('bad register type')
    if len(set(slots))!=len(slots):raise CompileError('duplicate slot names')
    from .core import _IDENT, _RESERVED
    if any(not _IDENT.fullmatch(s) or s in _RESERVED for s in slots):
        raise CompileError('invalid slot names')
    states={0:(frozenset(),frozenset())}
    pending=deque([0]);returns=0;reachable=set()
    def reg_id(v):
        if type(v)!=int or v<0 or v>=len(rtypes):raise CompileError('bad register id')
        return v
    def local_id(v):
        if type(v)!=int or v<0 or v>=len(slots):raise CompileError('bad local index')
        return v
    def target(v,pc):
        if type(v)!=int or v<=pc or v>=n:raise CompileError('jump must be within code and forward')
        return v
    while pending:
        pc=pending.popleft()
        if pc<0 or pc>=n:raise CompileError('register control-flow escapes')
        defs,local_defs=states[pc]
        defined=set(defs);locals_ready=set(local_defs)
        item=ins[pc]
        if not isinstance(item,tuple) or len(item)!=2 or not isinstance(item[0],str) or not isinstance(item[1],tuple):
            raise CompileError('bad register opcode shape')
        op,args=item
        reachable.add(pc)
        def arity(k):
            if len(args)!=k:raise CompileError('wrong register operand count')
        def read(i,t=None):
            i=reg_id(i)
            if i not in defined:raise CompileError('read of register not defined on all paths')
            if t is not None and rtypes[i]!=t:raise CompileError('register operand type mismatch')
            return rtypes[i]
        def write(i,t):
            i=reg_id(i)
            if i in defined:raise CompileError('register redefined along a single path')
            if rtypes[i]!=t:raise CompileError('register result type mismatch')
            defined.add(i)
        successors=[]
        if op=='CONST_I32':
            arity(2)
            if type(args[1])!=int or not MIN_I32<=args[1]<=MAX_I32:raise CompileError('invalid constant i32')
            write(args[0],'i32')
        elif op=='CONST_BOOL':
            arity(2)
            if type(args[1])!=bool:raise CompileError('invalid bool')
            write(args[0],'bool')
        elif op=='LOAD_LOCAL':
            arity(2);dest,index=args;index=local_id(index)
            if index not in locals_ready:raise CompileError('load of uninitialized local')
            write(dest,'i32')
        elif op=='STORE_LOCAL':
            arity(2);index,source=args;index=local_id(index);read(source,'i32')
            locals_ready.add(index)
        elif op=='NEG':
            arity(2);dest,src=args;read(src,'i32');write(dest,'i32')
        elif op in ('ADD','SUB','MUL','DIV','LT','EQ'):
            arity(3);dest,a,b=args
            ta=read(a);tb=read(b)
            if op=='EQ':
                if ta!=tb:raise CompileError('equality operand types differ')
            elif (ta,tb)!=('i32','i32'):raise CompileError('numeric operation needs i32 operands')
            write(dest,'bool' if op in ('LT','EQ') else 'i32')
        elif op=='COPY':
            arity(2);dest,src=args;write(dest,read(src))
        elif op=='BR_FALSE':
            arity(2);cond,to=args;read(cond,'bool')
            successors.append(target(to,pc))
        elif op=='JUMP':
            arity(1);successors.append(target(args[0],pc))
        elif op=='RETURN':
            arity(1);read(args[0],'i32');returns+=1
        else:raise CompileError(f'unknown register instruction {op!r}')
        if op not in ('JUMP','RETURN'):successors.append(pc+1)
        for to in successors:
            if not 0<=to<n:raise CompileError('fallthrough escapes register program')
            new=(frozenset(defined),frozenset(locals_ready))
            previous=states.get(to)
            if previous is not None:
                new=(previous[0]&new[0], previous[1]&new[1])
            if new!=previous:
                states[to]=new;pending.append(to)
    if not returns:raise CompileError('missing reachable RETURN')
    if len(reachable)!=n:raise CompileError('unreachable register instructions')
    return {'registers':len(rtypes),'instructions':n,'reachable':len(reachable),'returns':returns}

def run_registers(code:RegisterCode)->int:
    verify_registers(code)
    registers=[None]*len(code.register_types)
    locals_=[None]*len(code.slots)
    pc=0;steps=0
    while True:
        steps+=1
        if steps>MAX_INSNS*2:raise Trap('register VM step budget')
        op,a=code.instructions[pc];pc+=1
        if op in ('CONST_I32','CONST_BOOL'):registers[a[0]]=a[1]
        elif op=='LOAD_LOCAL':registers[a[0]]=locals_[a[1]]
        elif op=='STORE_LOCAL':locals_[a[0]]=registers[a[1]]
        elif op=='NEG':registers[a[0]]=calc('NEG',registers[a[1]])
        elif op in ('ADD','SUB','MUL','DIV','LT','EQ'):
            registers[a[0]]=calc(op,registers[a[1]],registers[a[2]])
        elif op=='COPY':registers[a[0]]=registers[a[1]]
        elif op=='BR_FALSE':
            if not registers[a[0]]:pc=a[1]
        elif op=='JUMP':pc=a[0]
        elif op=='RETURN':return registers[a[0]]
        else:raise CompileError('unrecognized register opcode')

def execute_registers(source:str,optimized:bool=False)->int:
    return run_registers(lower(source,optimized=optimized))

def serialize_registers(code:RegisterCode)->bytes:
    verify_registers(code)
    doc={'language':_LANG,'register_types':list(code.register_types),'slots':list(code.slots),
         'instructions':[[op,*args] for op,args in code.instructions]}
    return (json.dumps(doc,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode('utf8')

def register_artifact_sha256(code:RegisterCode)->str:
    return sha256(serialize_registers(code)).hexdigest()
