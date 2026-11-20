"""ATLAS compiler-design v0.1.0: typed, bounded expression compiler and VM.

Scientific model only. This language is intentionally not Python, C, Wasm or LLVM IR.
Integer operations use checked signed 32-bit arithmetic; invalid operations trap.
"""
from __future__ import annotations
from dataclasses import dataclass
import hashlib, json, re

MIN_I32=-(1<<31); MAX_I32=(1<<31)-1
MAX_TOKENS=4096; MAX_DEPTH=128; MAX_INSNS=16384; MAX_SLOTS=512
class CompileError(ValueError):pass
class Trap(ArithmeticError):pass

@dataclass(frozen=True)
class Token:
    text:str
    offset:int
@dataclass(frozen=True)
class Lit:
    value:int|bool
@dataclass(frozen=True)
class Var:
    name:str
@dataclass(frozen=True)
class Unary:
    op:str
    arg:object
@dataclass(frozen=True)
class Binary:
    op:str
    lhs:object
    rhs:object
@dataclass(frozen=True)
class If:
    cond:object
    yes:object
    no:object
@dataclass(frozen=True)
class Let:
    name:str
    value:object
@dataclass(frozen=True)
class Program:
    statements:tuple[Let,...]
    result:object
@dataclass(frozen=True)
class Code:
    instructions:tuple[tuple[str,int|str|None],...]
    slots:tuple[str,...]

_IDENT=re.compile(r'[A-Za-z_][A-Za-z_0-9]*\Z')
_NUMBER=re.compile(r'[0-9]+\Z')
_RESERVED={'let','return','if','then','else','true','false'}
_RE=re.compile(r'(?P<ws>\s+)|(?P<comment>//[^\n]*)|(?P<number>[0-9]+)|(?P<word>[A-Za-z_][A-Za-z_0-9]*)|(?P<op>==|[+\-*/<;=()])')

def lex(src:str)->tuple[Token,...]:
    if not isinstance(src,str) or len(src)>32768:raise CompileError('source length limit')
    tokens=[];pos=0
    while pos<len(src):
        m=_RE.match(src,pos)
        if not m:raise CompileError(f'unsupported character at offset {pos}')
        if m.lastgroup not in ('ws','comment'):
            tokens.append(Token(m.group(),pos))
            if len(tokens)>MAX_TOKENS:raise CompileError('token budget exceeded')
        pos=m.end()
    tokens.append(Token('<EOF>',pos));return tuple(tokens)

class Parser:
    def __init__(self,tokens):self.ts=tokens;self.i=0;self.depth=0
    def peek(self):return self.ts[self.i].text
    def take(self,expect=None):
        t=self.ts[self.i]
        if expect is not None and t.text!=expect:raise CompileError(f'expected {expect!r} at {t.offset}, got {t.text!r}')
        self.i+=1;return t.text
    def name(self):
        tok=self.ts[self.i]
        if not _IDENT.fullmatch(tok.text) or tok.text in _RESERVED:raise CompileError(f'invalid name at {tok.offset}')
        return self.take()
    def parse(self)->Program:
        statements=[]
        while self.peek()=='let':
            self.take();name=self.name();self.take('=');value=self.expr();self.take(';')
            statements.append(Let(name,value))
            if len(statements)>MAX_SLOTS:raise CompileError('local budget exceeded')
        self.take('return');result=self.expr();self.take(';');self.take('<EOF>')
        return Program(tuple(statements),result)
    def expr(self,min_bp=0):
        self.depth+=1
        if self.depth>MAX_DEPTH:raise CompileError('expression nesting exceeded')
        try:
            left=self.atom()
            while True:
                op=self.peek()
                if op not in ('==','<','+','-','*','/'):break
                bp={'==':5,'<':5,'+':10,'-':10,'*':20,'/':20}[op]
                if bp<min_bp:break
                self.take();right=self.expr(bp+1);left=Binary(op,left,right)
            return left
        finally:self.depth-=1
    def atom(self):
        op=self.peek()
        if _NUMBER.fullmatch(op):
            n=int(self.take())
            if n>MAX_I32:raise CompileError('integer literal out of i32 range')
            return Lit(n)
        if op in ('true','false'):return Lit(self.take()=='true')
        if op=='(':
            self.take();value=self.expr();self.take(')');return value
        if op=='-':self.take();return Unary('-',self.expr(30))
        if op=='if':
            self.take();cond=self.expr();self.take('then');yes=self.expr();self.take('else');no=self.expr()
            return If(cond,yes,no)
        if _IDENT.fullmatch(op) and op not in _RESERVED:return Var(self.take())
        raise CompileError(f'unexpected token {op!r} at {self.ts[self.i].offset}')

def parse(src:str)->Program:return Parser(lex(src)).parse()

def infer(expr,env:dict[str,str])->str:
    if isinstance(expr,Lit):return 'bool' if type(expr.value) is bool else 'i32'
    if isinstance(expr,Var):
        if expr.name not in env:raise CompileError(f'unknown local {expr.name}')
        return env[expr.name]
    if isinstance(expr,Unary):
        if infer(expr.arg,env)!='i32':raise CompileError('unary minus requires i32')
        return 'i32'
    if isinstance(expr,Binary):
        lt,rt=infer(expr.lhs,env),infer(expr.rhs,env)
        if expr.op in ('+','-','*','/','<'):
            if (lt,rt)!=('i32','i32'):raise CompileError('numeric operator needs i32 pair')
            return 'bool' if expr.op=='<' else 'i32'
        if expr.op=='==':
            if lt!=rt:raise CompileError('equality needs matching types')
            return 'bool'
    if isinstance(expr,If):
        if infer(expr.cond,env)!='bool':raise CompileError('condition requires bool')
        a,b=infer(expr.yes,env),infer(expr.no,env)
        if a!=b:raise CompileError('branch type mismatch')
        return a
    raise CompileError('unknown AST expression')

def typecheck(prog:Program)->dict[str,str]:
    env={}
    for s in prog.statements:
        if s.name in env:raise CompileError('duplicate local')
        if infer(s.value,env)!='i32':raise CompileError('only i32 locals in v0.1')
        env[s.name]='i32'
    if infer(prog.result,env)!='i32':raise CompileError('return must be i32')
    return env

def i32(n:int)->int:
    if type(n) is not int or not MIN_I32<=n<=MAX_I32:raise Trap('signed i32 overflow')
    return n

def calc(op,a,b=None):
    if op=='NEG':return i32(-a)
    if op=='ADD':return i32(a+b)
    if op=='SUB':return i32(a-b)
    if op=='MUL':return i32(a*b)
    if op=='DIV':
        if b==0:raise Trap('division by zero')
        return i32((abs(a)//abs(b)) * (-1 if (a<0) != (b<0) else 1))
    if op=='LT':return a<b
    if op=='EQ':return a==b
    raise CompileError('unknown operation')
_MAP={'+':'ADD','-':'SUB','*':'MUL','/':'DIV','<':'LT','==':'EQ'}

def optimize(expr):
    """Conservative defined-operation constant folding; overflow stays a runtime trap."""
    if isinstance(expr,(Lit,Var)):return expr
    if isinstance(expr,Unary):
        a=optimize(expr.arg)
        if isinstance(a,Lit):
            try:return Lit(calc('NEG',a.value))
            except Trap:pass
        return Unary(expr.op,a)
    if isinstance(expr,Binary):
        a,b=optimize(expr.lhs),optimize(expr.rhs)
        if isinstance(a,Lit) and isinstance(b,Lit):
            try:return Lit(calc(_MAP[expr.op],a.value,b.value))
            except Trap:pass
        return Binary(expr.op,a,b)
    if isinstance(expr,If):
        c=optimize(expr.cond)
        if isinstance(c,Lit) and type(c.value) is bool:
            return optimize(expr.yes if c.value else expr.no)
        return If(c,optimize(expr.yes),optimize(expr.no))
    raise CompileError('unsupported AST during optimization')

def compile_program(src:str,optimized:bool=True)->Code:
    prog=parse(src);typecheck(prog)
    ins=[];slot={}
    def emit(op,arg=None):
        if len(ins)>=MAX_INSNS:raise CompileError('bytecode budget exceeded')
        ins.append((op,arg));return len(ins)-1
    def expr(e):
        if isinstance(e,Lit):emit('PUSH_BOOL' if type(e.value) is bool else 'PUSH_I32',e.value);return
        if isinstance(e,Var):emit('LOAD',slot[e.name]);return
        if isinstance(e,Unary):expr(e.arg);emit('NEG');return
        if isinstance(e,Binary):expr(e.lhs);expr(e.rhs);emit(_MAP[e.op]);return
        if isinstance(e,If):
            expr(e.cond);fj=emit('JMP_IF_FALSE',-1)
            expr(e.yes);end=emit('JMP',-1)
            ins[fj]=('JMP_IF_FALSE',len(ins))
            expr(e.no);ins[end]=('JMP',len(ins));return
        raise CompileError('unknown expression in generator')
    for s in prog.statements:
        slot[s.name]=len(slot)
        expr(optimize(s.value) if optimized else s.value)
        emit('STORE',slot[s.name])
    expr(optimize(prog.result) if optimized else prog.result);emit('RETURN')
    obj=Code(tuple(ins),tuple(slot));verify(obj);return obj

def verify(code:Code)->int:
    """Forward CFG abstract interpreter: stack types and definite local initialization."""
    if not isinstance(code,Code) or not 0<len(code.instructions)<=MAX_INSNS or len(code.slots)>MAX_SLOTS:
        raise CompileError('invalid code shape')
    if len(code.slots)!=len(set(code.slots)):raise CompileError('duplicate slots')
    for name in code.slots:
        if not _IDENT.fullmatch(name) or name in _RESERVED:raise CompileError('invalid slot')
    cfg={(0,(),frozenset())};seen={};returned=0;max_stack=0
    while cfg:
        pc,stack,init=cfg.pop()
        if pc<0 or pc>=len(code.instructions):raise CompileError('control flow escapes code')
        old=seen.get(pc)
        if old is not None:
            if old!=(stack,init):raise CompileError('incompatible stack or initialization at merge')
            continue
        seen[pc]=(stack,init);op,arg=code.instructions[pc];st=list(stack);ini=set(init)
        if op=='PUSH_I32':
            if type(arg) is not int or not MIN_I32<=arg<=MAX_I32:raise CompileError('bad i32 immediate')
            st.append('i32')
        elif op=='PUSH_BOOL':
            if type(arg) is not bool:raise CompileError('bad bool immediate')
            st.append('bool')
        elif op in ('LOAD','STORE'):
            if type(arg) is not int or not 0<=arg<len(code.slots):raise CompileError('bad slot index')
            if op=='LOAD':
                if arg not in ini:raise CompileError('uninitialized local')
                st.append('i32')
            else:
                if not st or st.pop()!='i32':raise CompileError('STORE type/underflow')
                ini.add(arg)
        elif op=='NEG':
            if not st or st.pop()!='i32':raise CompileError('NEG underflow/type')
            st.append('i32')
        elif op in ('ADD','SUB','MUL','DIV','LT','EQ'):
            if len(st)<2:raise CompileError('binary underflow')
            r,l=st.pop(),st.pop()
            if op=='EQ':
                if l!=r:raise CompileError('equality stack mismatch')
            elif l!='i32' or r!='i32':raise CompileError('numeric stack mismatch')
            st.append('bool' if op in ('LT','EQ') else 'i32')
        elif op=='JMP_IF_FALSE':
            if not st or st.pop()!='bool':raise CompileError('branch condition type')
            if type(arg) is not int or not pc<arg<len(code.instructions):raise CompileError('bad conditional jump')
            cfg.add((arg,tuple(st),frozenset(ini)))
        elif op=='JMP':
            if type(arg) is not int or not pc<arg<len(code.instructions):raise CompileError('bad jump')
            cfg.add((arg,tuple(st),frozenset(ini)))
            max_stack=max(max_stack,len(st));continue
        elif op=='RETURN':
            if st!=['i32']:raise CompileError('RETURN requires one i32')
            returned+=1;max_stack=max(max_stack,len(st));continue
        else:raise CompileError(f'unknown opcode {op}')
        max_stack=max(max_stack,len(st))
        cfg.add((pc+1,tuple(st),frozenset(ini)))
        if max_stack>4096:raise CompileError('stack bound exceeded')
    if not returned:raise CompileError('no RETURN reachable')
    return max_stack

def run(code:Code)->int:
    verify(code);pc=0;stack=[];loc=[None]*len(code.slots);step=0
    while True:
        step+=1
        if step>MAX_INSNS*2:raise Trap('VM step budget exhausted')
        op,arg=code.instructions[pc];pc+=1
        if op in ('PUSH_I32','PUSH_BOOL'):stack.append(arg)
        elif op=='LOAD':stack.append(loc[arg])
        elif op=='STORE':loc[arg]=stack.pop()
        elif op=='NEG':stack.append(calc('NEG',stack.pop()))
        elif op in ('ADD','SUB','MUL','DIV','LT','EQ'):
            b=stack.pop();a=stack.pop();stack.append(calc(op,a,b))
        elif op=='JMP_IF_FALSE':
            if not stack.pop():pc=arg
        elif op=='JMP':pc=arg
        elif op=='RETURN':return stack.pop()
        else:raise CompileError('unknown opcode in VM')

def execute(src:str,optimized:bool=True)->int:return run(compile_program(src,optimized=optimized))

def serialize(code:Code)->bytes:
    return (json.dumps({'language':'atlas-compiler-tiny-i32/1','slots':list(code.slots),
        'instructions':[list(i) for i in code.instructions]},sort_keys=True,separators=(',',':'))+'\n').encode()

def artifact_digest(code:Code)->str:return hashlib.sha256(serialize(code)).hexdigest()
