"""Finite independently executed v0.2 parser/backend agreement experiment.

The reference AST evaluator is algorithmically separate from both VMs.
The recursive parser is algorithmically separate from the Pratt parser,
but they share the lexical scanner and AST schema. This is differential
software evidence only, not proof of universal semantic preservation.
"""
import json,random
from compiler_atlas.core import parse,compile_program,run,Trap,CompileError
from compiler_atlas.reference_parser import parse_reference
from compiler_atlas.register_ir import (lower,run_registers,RegisterCode,
    verify_registers)
from .independent_oracle import generator, evaluate, normalize

SEED=18022026

def experiment(seed=SEED,count=9000):
    rng=random.Random(seed)
    parser_matches=0;vm_matches=0;trap_cases=0
    examples=['return 7;', 'return -7/2;', 'return if true then 4 else 5/0;',
      'return if false then 5/0 else 4;', 'return 2147483647+1;',
      'return 1/0;', 'return if false then 2147483647+1 else -9;',
      'return (if true then 6 else 7) * (if false then 1 else 2);']
    for _ in range(count):
        source='let x='+str(rng.choice([-200,0,1,7,1024]))+';let y=-3;return '+generator(rng,rng.randrange(1,5))+';'
        examples.append(source)
    for index,source in enumerate(examples):
        core_ast=parse(source)
        ref_ast=parse_reference(source)
        if core_ast!=ref_ast:
            raise AssertionError(json.dumps({'case':index,'source':source,'reason':'parser structural difference'}))
        parser_matches+=1
        reference=normalize(lambda:evaluate(ref_ast))
        if reference[0]=='trap':trap_cases+=1
        for optimized in (False,True):
            stack=normalize(lambda:run(compile_program(source,optimized=optimized)))
            regs=normalize(lambda:run_registers(lower(source,optimized=optimized)))
            if stack!=reference or regs!=reference:
                raise AssertionError(json.dumps({'case':index,'source':source,'optimization':optimized,
                    'expected':reference,'stack':stack,'registers':regs}))
            vm_matches+=2
    malformed_sources=['return;', 'return (3+2;', 'let x=1 return x;',
      'return if true then 1;', 'return 2147483648;', 'return @;',
      'return 1; return 2;', 'return 1 + ;']
    rejected_parser=0
    for source in malformed_sources:
        core_failure=ref_failure=False
        try:parse(source)
        except CompileError:core_failure=True
        try:parse_reference(source)
        except CompileError:ref_failure=True
        if core_failure and ref_failure:rejected_parser+=1
        else:raise AssertionError('malformed grammar accepted by at least one parser')
    malformed_registers=[
      RegisterCode((('RETURN',(0,)),),('i32',),()),
      RegisterCode((('CONST_BOOL',(0,True)),('RETURN',(0,))),('bool',),()),
      RegisterCode((('CONST_I32',(0,3)),('JUMP',(1,)),('RETURN',(0,))),('i32',),()),
      RegisterCode((('CONST_I32',(0,5)),('ADD',(1,0,2)),('RETURN',(1,))),('i32','i32','i32'),()),
      RegisterCode((('CONST_BOOL',(0,True)),('BR_FALSE',(0,3)),('CONST_I32',(1,12)),('RETURN',(1,))),('bool','i32'),())]
    rejected_ir=0
    for code in malformed_registers:
        try:verify_registers(code)
        except CompileError:rejected_ir+=1
        else:raise AssertionError('invalid IR got past register verifier')
    return {'schema':'atlas.compiler-design-v02-independent-multibackend-oracle/1',
      'result':'passed', 'seed':seed,'programs':len(examples),
      'independent_parser_AST_matches':parser_matches,
      'independent_VM_semantic_comparisons':vm_matches,
      'programs_with_expected_trap':trap_cases,
      'malformed_grammar_controls_rejected':rejected_parser,
      'invalid_register_ir_controls_rejected':rejected_ir,
      'notes':'Finite seeded cases, separate parsers share lexer and AST; AST evaluator shares arithmetic specification. Does not establish formal proof or native backend correctness.'}

if __name__=='__main__':
    print(json.dumps(experiment(),sort_keys=True,indent=2))
