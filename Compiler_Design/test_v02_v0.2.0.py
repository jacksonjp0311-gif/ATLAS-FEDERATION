"""Compiler Atlas v0.2 reference parser + register IR tests."""
import unittest, random
from compiler_atlas.core import parse,execute,CompileError,Trap
from compiler_atlas.reference_parser import parse_reference
from compiler_atlas.register_ir import (RegisterCode, lower,run_registers,execute_registers,
    verify_registers,serialize_registers,register_artifact_sha256)

class CompilerV02(unittest.TestCase):
    def test_parser_different_precedence_path(self):
        cases=['return 2+3*4;', 'return (2+3)*4;', 'return -2*3+5;',
           'return if 1<2 then 3*4 else 1/0;',
           'return if true then 4 else if false then 7 else 8;',
           'let x=2; let y=x+3;return if y<7 then y*y else 8;',
           'return -(-(12));','return 3<4==true;',
           'return if 0==1 then 7 else (if true then 9 else 10);',
           'return (if false then 14 else 7)+9;']
        for source in cases:
            with self.subTest(source=source):self.assertEqual(parse_reference(source),parse(source))
    def test_parser_rejects_bad_inputs(self):
        for source in ['return 1', 'return 4+;', 'let x=2 return x;', 'return @;',
          'return if true then 1;', 'return (-(-(-(-(', 'return 2147483648;',
          'return 1;return 2;', 'return true else 5;', 'let x=1; return x + ;']:
            with self.subTest(source=source),self.assertRaises(CompileError):parse_reference(source)
    def test_very_deep_prefix_bounded(self):
        with self.assertRaises(CompileError):parse_reference('return '+('-'*2000)+'1;')
    def test_register_arithmetic(self):
        for s,v in [('return 1+2*3;',7),('return (1+2)*3;',9),('return -7/2;',-3),
           ('return -7/-2;',3),('let x=8;let y=x*2;return y-5;',11)]:
           with self.subTest(source=s):
                self.assertEqual(execute_registers(s),v)
                self.assertEqual(execute_registers(s,optimized=True),v)
    def test_register_conditional_trap_laziness(self):
        cases=[('return if false then 1/0 else 17;',17),
           ('return if true then 21 else 1/0;',21),
           ('let x=9;return if x<5 then 1/0 else x+1;',10),
           ('return (if true then 2 else 1/0)+(if false then 1/0 else 4);',6)]
        for s,v in cases:
            with self.subTest(source=s):
                self.assertEqual(execute_registers(s),v)
                self.assertEqual(execute_registers(s,True),v)
    def test_register_traps(self):
        for s in ('return 1/0;','return 2147483647+1;', 'return 100000*100000;'):
            for optimized in (False,True):
                with self.subTest(s=s,optimized=optimized),self.assertRaises(Trap):
                    execute_registers(s,optimized=optimized)
    def test_register_semantic_differential(self):
        rng=random.Random(1802)
        for _ in range(300):
            x=rng.randint(-1000,1000); y=rng.randint(-1000,1000)
            source=f'let x={x};let y={y};return if x<y then (x+y)*2 else x-y;'
            for opt in (False,True):
                self.assertEqual(execute_registers(source,opt),execute(source,opt))
    def test_register_same_artifact(self):
        s='let x=2;return if x<4 then x*3 else 8;'
        a=lower(s);b=lower(s)
        self.assertEqual(serialize_registers(a),serialize_registers(b))
        self.assertEqual(len(register_artifact_sha256(a)),64)
    def test_register_verifier_rejects_bad_register(self):
        negative=[
          RegisterCode((('RETURN',(0,)),),('i32',),()),
          RegisterCode((('CONST_BOOL',(0,True)),('RETURN',(0,))),('bool',),()),
          RegisterCode((('CONST_I32',(0,3)),('JUMP',(1,)),('RETURN',(0,))),('i32',),()),
          RegisterCode((('JUMP',(1,)),('RETURN',(0,))),('i32',),()),
          RegisterCode((('CONST_I32',(0,5)),('CONST_I32',(0,6)),('RETURN',(0,))),('i32',),()),
          RegisterCode((('CONST_I32',(0,5)),('ADD',(1,0,2)),('RETURN',(1,))),('i32','i32','i32'),()),
          RegisterCode((('LOAD_LOCAL',(0,0)),('RETURN',(0,))),('i32',),('x',)),
          RegisterCode((('CONST_I32',(0,2)),('BAD',(0,)),('RETURN',(0,))),('i32',),())]
        for obj in negative:
            with self.subTest(ins=obj.instructions),self.assertRaises(CompileError):verify_registers(obj)
    def test_register_join_definite_assignment(self):
        # A path skipping register definition must not be able to return it.
        bad=RegisterCode((('CONST_BOOL',(0,True)),('BR_FALSE',(0,3)),
             ('CONST_I32',(1,12)),('RETURN',(1,))),('bool','i32'),())
        with self.assertRaises(CompileError):verify_registers(bad)
    def test_register_valid_type_result(self):
        p=lower('let n=21;return if n<5 then n else n/3;')
        detail=verify_registers(p)
        self.assertEqual(detail['instructions'],len(p.instructions))
        self.assertEqual(detail['reachable'],len(p.instructions))

if __name__=='__main__':unittest.main()
