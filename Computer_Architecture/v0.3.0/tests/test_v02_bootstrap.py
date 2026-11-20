import unittest,random,hashlib
from computer_atlas.v02_bootstrap import parse_source,compile_source,evaluate_source,compile_receipt
from computer_atlas.spec import SpecMachine,AT8Trap
from computer_atlas.microcoded import MicrocodedMachine

class TestAT8Bootstrap(unittest.TestCase):
    def compare(self,text,tapes=None,max_ops=100000):
        rom=compile_source(text)
        golden=evaluate_source(text,tapes,max_ops)
        atomic=SpecMachine(rom,tapes).run(max_steps=max_ops)
        micro=MicrocodedMachine(rom,tapes).run(max_instructions=max_ops)
        self.assertTrue(atomic['halted'])
        self.assertTrue(micro['halted'])
        self.assertEqual(atomic['snapshot'],micro['snapshot'])
        last=atomic['snapshot']
        self.assertEqual(last['regs'][0],golden['accumulator'])
        self.assertEqual(last['ram'],golden['ram'])
        self.assertEqual(last['output'],golden['output'])
        self.assertEqual(last['input_cursors'],golden['input_cursors'])
        return rom
    def test_basic_program(self):
        rom=self.compare('SET 5\nADD 7\nSTORE 4\nXOR 3\nOUT 0\nHALT')
        self.assertEqual(len(rom),12)
    def test_repeat_countdown(self):
        self.compare('SET 0\nREPEAT 7\n ADD 1\n OUT 0\nEND\nHALT')
    def test_nested_repeat(self):
        self.compare('SET 0\nREPEAT 2\n REPEAT 3\n  ADD 2\n END\nEND\nHALT')
    def test_three_level_nesting(self):
        self.compare('SET 0\nREPEAT 2\nREPEAT 2\nREPEAT 3\nADD 1\nEND\nEND\nEND\nHALT')
    def test_byte_wrap_and_zero(self):
        self.compare('SET 250\nREPEAT 6\n ADD 1\nEND\nHALT')
    def test_comments_and_case(self):
        self.compare('set 7 # note\nadd 3 ; plus\nhalt')
    def test_load_store(self):
        self.compare('SET 33\nSTORE 10\nSET 0\nLOAD 10\nOUT 2\nHALT')
    def test_input(self):
        self.compare('IN 1\nADD 9\nOUT 2\nHALT',{1:[99]})
    def test_input_twice(self):
        self.compare('IN 0\nOUT 0\nIN 0\nOUT 0\nHALT',{0:[12,3]})
    def test_bitwise_all(self):
        self.compare('SET 7\nAND 3\nOR 16\nXOR 1\nHALT')
    def test_reference_digest(self):
        r=compile_receipt('SET 5\nADD 7\nHALT')
        self.assertEqual(r['source_sha256'],hashlib.sha256(b'SET 5\nADD 7\nHALT').hexdigest())
        self.assertTrue(0<r['rom_bytes']<=256)
    def test_random_straight_line(self):
        rng=random.Random(2218)
        for _ in range(250):
            src=['SET '+str(rng.randrange(256))]
            for k in range(rng.randrange(2,20)):
                op=rng.choice(('ADD','XOR','OR','AND','STORE','LOAD','OUT'))
                v=rng.randrange(4) if op=='OUT' else rng.randrange(256)
                src.append(f'{op} {v}')
            src.append('HALT');self.compare('\n'.join(src))
    def test_random_nested(self):
        rng=random.Random(991)
        for _ in range(150):
            a,b,c=[rng.randrange(1,5) for i in range(3)]
            self.compare(f'SET {rng.randrange(256)}\nREPEAT {a}\nADD {c}\nREPEAT {b}\nXOR 3\nEND\nEND\nHALT')
    def test_rom_overflow_refusal(self):
        with self.assertRaises(ValueError):compile_source('SET 5\n'+'ADD 1\n'*140+'HALT')
    def test_loop_depth_refusal(self):
        with self.assertRaises(ValueError):compile_source('REPEAT 1\n'*4+'SET 1\n'+'END\n'*4+'HALT')
    def test_empty_loop_refusal(self):
        with self.assertRaises(ValueError):parse_source('REPEAT 2\nEND\nHALT')
    def test_loop_zero_refusal(self):
        with self.assertRaises(ValueError):compile_source('REPEAT 0\nSET 2\nEND\nHALT')
    def test_missing_halt_refusal(self):
        with self.assertRaises(ValueError):compile_source('SET 2')
    def test_duplicate_halt_refusal(self):
        with self.assertRaises(ValueError):compile_source('HALT\nHALT')
    def test_early_halt_in_loop_refusal(self):
        with self.assertRaises(ValueError):compile_source('REPEAT 3\nHALT\nEND\nHALT')
    def test_bad_opcode_refusal(self):
        with self.assertRaises(ValueError):compile_source('MULTIPLY 4\nHALT')
    def test_bad_input_port(self):
        with self.assertRaises(ValueError):compile_source('IN 4\nHALT')
    def test_missing_input_refusal(self):
        with self.assertRaises(ValueError):evaluate_source('IN 2\nHALT')
        with self.assertRaises(AT8Trap):SpecMachine(compile_source('IN 2\nHALT')).run()
    def test_operation_budget(self):
        with self.assertRaises(ValueError):evaluate_source('SET 2\nREPEAT 255\nADD 1\nEND\nHALT',max_operations=10)
    def test_noninteger_input(self):
        with self.assertRaises(ValueError):evaluate_source('IN 2\nHALT',{2:[True]})
    def test_bad_end(self):
        with self.assertRaises(ValueError):compile_source('SET 5\nEND\nHALT')
    def test_unclosed(self):
        with self.assertRaises(ValueError):compile_source('REPEAT 1\nSET 2\nHALT')
