import unittest
from compiler_atlas.core import (lex,parse,infer,typecheck,compile_program,execute,Code,verify,serialize,artifact_digest,CompileError,Trap)

class CompilerCore(unittest.TestCase):
    def test_arithmetic(self):
        for s,answer in [('return 1+2*3;',7),('return (1+2)*3;',9),('return 7-10;',-3),('return -7/2;',-3),('return -7/-2;',3),('return 0*2147483647;',0)]:
            with self.subTest(s=s):self.assertEqual(execute(s),answer)
    def test_branch(self):
        for s,answer in [('return if 2<3 then 4 else 9;',4),('return if false then 1/0 else 12;',12),('return if true then 5 else 4/0;',5),('return if 5==5 then 88 else 99;',88)]:
            with self.subTest(s=s):
                self.assertEqual(execute(s,True),answer)
                self.assertEqual(execute(s,False),answer)
    def test_locals(self):
        self.assertEqual(execute('let x=4;let y=x+5;return y*2;'),18)
        self.assertEqual(execute('let x=3;return if x<7 then x else 9;'),3)
    def test_token_positions(self):
        ts=lex(' let a = 2; // a\nreturn a;')
        self.assertEqual([t.text for t in ts],['let','a','=','2',';','return','a',';','<EOF>'])
        self.assertEqual(ts[0].offset,1)
    def test_compiler_reproducibility(self):
        p='let x=30;return if x<2 then 1 else x*4;'
        self.assertEqual(serialize(compile_program(p)),serialize(compile_program(p)))
        self.assertEqual(len(artifact_digest(compile_program(p))),64)
    def test_optimization_preserves_result(self):
        for v in range(-30,30):
            p=f'let x={v};return if x<0 then 0-x else x+1;'
            self.assertEqual(execute(p,False),execute(p,True))
    def test_overflow(self):
        for source in ('return 2147483647+1;','return 100000*100000;', 'return -2147483647-2;'):
            with self.subTest(source=source):
                for opt in (False,True):
                    with self.assertRaises(Trap):execute(source,opt)
    def test_divide_by_zero(self):
        with self.assertRaises(Trap):execute('return 4/0;')
        with self.assertRaises(Trap):execute('return 4/0;',False)
    def test_bad_grammar(self):
        for p in ('return 1','ret 1;','return 1 2;','return (1+2;','return @;','let x=2;','return 1; let x=2;', 'return 1;return 2;','return é;'):
            with self.subTest(p=p),self.assertRaises(CompileError):compile_program(p)
    def test_ill_typed(self):
        for p in ('return true;','return true+1;','return if 1 then 2 else 3;','return if true then 1 else false;', 'let x=true;return 5;', 'let x=1;let x=2;return x;', 'return z;','return 1 == true;','return 1<true;'):
            with self.subTest(p=p),self.assertRaises(CompileError):compile_program(p)
    def test_bad_literal(self):
        with self.assertRaises(CompileError):compile_program('return 2147483648;')
    def test_deliberately_corrupted_code(self):
        rejected=[Code((('JMP',0),),()),Code((('PUSH_BOOL',True),('RETURN',None)),()),Code((('LOAD',0),('RETURN',None)),('x',)),Code((('PUSH_I32',1),('PUSH_BOOL',True),('ADD',None),('RETURN',None)),()),Code((('PUSH_I32',1),('JMP',200),('RETURN',None)),())]
        for v in rejected:
            with self.subTest(v=v),self.assertRaises(CompileError):verify(v)
    def test_lex_bound(self):
        with self.assertRaises(CompileError):lex('a'*32769)
    def test_max_locals(self):
        with self.assertRaises(CompileError):compile_program(''.join(f'let x{i}={i};' for i in range(513))+'return x0;')
    def test_internals(self):
        self.assertEqual(typecheck(parse('let x=1;return x;'))['x'],'i32')
        self.assertGreaterEqual(verify(compile_program('return 3;')),1)
if __name__=='__main__':unittest.main()
