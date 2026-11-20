"""Independent AST big-step semantics vs compiled VM. Bounded finite software evidence."""
import ast, itertools, json, random
from compiler_atlas.core import (parse,compile_program,run,Trap,CompileError,execute,
    Lit,Var,Unary,Binary,If,MAX_I32,MIN_I32,Code,verify)

def independent_value(node,env):
    if isinstance(node,Lit):return node.value
    if isinstance(node,Var):return env[node.name]
    if isinstance(node,Unary):return checked(-independent_value(node.arg,env))
    if isinstance(node,If):
        cond=independent_value(node.cond,env)
        return independent_value(node.yes if cond else node.no,env)
    if isinstance(node,Binary):
        lhs=independent_value(node.lhs,env);rhs=independent_value(node.rhs,env)
        if node.op=='+':return checked(lhs+rhs)
        if node.op=='-':return checked(lhs-rhs)
        if node.op=='*':return checked(lhs*rhs)
        if node.op=='/':
            if rhs==0:raise ZeroDivisionError('zero denominator')
            result=abs(lhs)//abs(rhs)
            return checked(-result if (lhs<0) ^ (rhs<0) else result)
        if node.op=='<':return lhs<rhs
        if node.op=='==':return lhs==rhs
    raise AssertionError('invalid independent AST')

def checked(x):
    if type(x)!=int or not MIN_I32<=x<=MAX_I32:raise OverflowError('checked i32')
    return x

def evaluate(program):
    env={}
    for statement in program.statements:
        env[statement.name]=independent_value(statement.value,env)
    return independent_value(program.result,env)

def normalize(call):
    try:return ('value',call())
    except (ZeroDivisionError,OverflowError,Trap):return ('trap',None)

def generator(rng,depth,kind='i32'):
    if depth<=0:
        if kind=='bool':return rng.choice(['true','false','0 < 1','2 == 1'])
        return rng.choice(['0','1','7','-12','1024','2147483647','x','y'])
    if kind=='bool':
        if rng.random()<0.25:return rng.choice(['true','false'])
        l=generator(rng,depth-1);r=generator(rng,depth-1)
        return '('+l+rng.choice([' < ',' == '])+r+')'
    choice=rng.randrange(6)
    if choice==0:return generator(rng,0)
    if choice==1:return '-('+generator(rng,depth-1)+')'
    if choice in (2,3,4):
        l=generator(rng,depth-1);r=generator(rng,depth-1)
        return '('+l+rng.choice([' + ',' - ',' * ',' / '])+r+')'
    return '(if '+generator(rng,depth-1,'bool')+' then '+generator(rng,depth-1)+' else '+generator(rng,depth-1)+')'

def execute_oracle(seed=18317,iterations=12000):
    rng=random.Random(seed);count=0;traps=0
    cases=['return 7;','return -7/2;','return if false then 1/0 else 14;',
        'return if true then 1 else 2/0;',
        'let x=3;let y=x*9; return if y<30 then y else y/0;',
        'return (2147483647+1);', 'return 1/0;']
    for _ in range(iterations):
        body=generator(rng,rng.randrange(1,5))
        cases.append('let x='+str(rng.choice([0,1,7,1024]))+';let y=-3;return '+body+';')
    for source in cases:
        prog=parse(source)
        expected=normalize(lambda:evaluate(prog))
        for opt in (False,True):
            actual=normalize(lambda:run(compile_program(source,optimized=opt)))
            if expected!=actual:raise AssertionError(json.dumps({'source':source,'expected':expected,'observed':actual,'optimization':opt}))
            count+=1
            if expected[0]=='trap':traps+=1
    # independent host-language arithmetic oracle, no compiler parser on the expected side
    for a,b in itertools.product(range(-13,14),repeat=2):
        for op in ['+','-','*']:
            source=f'return ({a}) {op} ({b});'
            exp={'+' :a+b,'-':a-b,'*':a*b}[op]
            if execute(source)!=exp:raise AssertionError('host arithmetic mismatch')
            count+=1
    # Negative controls: reject corrupted opcode CFG/stack types.
    negative=[Code((('PUSH_I32',1),('JMP',0),('RETURN',None)),()),
              Code((('PUSH_BOOL',True),('RETURN',None)),()),
              Code((('LOAD',0),('RETURN',None)),('x',)),
              Code((('PUSH_I32',1),('PUSH_BOOL',True),('ADD',None),('RETURN',None)),())]
    rejected=0
    for sample in negative:
        try:verify(sample)
        except CompileError:rejected+=1
        else:raise AssertionError('negative bytecode control falsely accepted')
    return {'schema':'atlas.compiler-design-v01-independent-finite-oracle/1','seed':seed,
            'comparison_count':count,'trapped_comparisons':traps,
            'negative_controls_rejected':rejected,'result':'passed',
            'limitations':'Finite independent AST and arithmetic oracles only. No verified compiler proof, native binary ABI, concurrency or formal semantics for C/LLVM/Wasm.'}

if __name__=='__main__':print(json.dumps(execute_oracle(),indent=2))
