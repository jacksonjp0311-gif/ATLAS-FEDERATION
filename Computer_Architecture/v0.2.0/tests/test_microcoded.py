import unittest,random
from computer_atlas.isa import assemble,encode,DecodeError
from computer_atlas.spec import SpecMachine,AT8Trap
from computer_atlas.microcoded import MicrocodedMachine
from computer_atlas.programs import examples

class TestMicrocoded(unittest.TestCase):
    def test_programs_match_architecture(self):
        for name,p in examples().items():
            tape={1:[7]} if name=='input_output' else {}
            a=SpecMachine(p,tape).run(50)
            b=MicrocodedMachine(p,tape).run(50)
            self.assertTrue(a['halted'] and b['halted'])
            self.assertEqual(a['snapshot'],b['snapshot'])
            self.assertEqual(b['microcycles'],4*a['steps'])
    def test_each_stage_explicit(self):
        p=assemble('LDI R0, 5\nHALT')
        m=MicrocodedMachine(p)
        before=m.snapshot()
        stages=[]
        for _ in range(3):
            stages.append(m.tick()['stage'])
            self.assertEqual(m.snapshot(),before,'architectural state cannot change before COMMIT')
        self.assertEqual(stages,['FETCH','DECODE','EXECUTE'])
        self.assertEqual(m.tick()['stage'],'COMMIT')
        self.assertEqual(m.snapshot()['regs'][0],5)
    def test_pipeline_four_phases_per_instr(self):
        m=MicrocodedMachine(assemble('NOP\nHALT'))
        e=m.step_instruction()
        self.assertEqual([x['stage'] for x in e['microcycles']],['FETCH','DECODE','EXECUTE','COMMIT'])
    def test_random_immediate_arithmetic(self):
        rng=random.Random(20261116)
        for i in range(250):
            a,b,c=(rng.randrange(256) for _ in range(3))
            text=f'LDI R0, {a}\nADDI R0, {b}\nXORI R0, {c}\nOUT R0, 2\nHALT'
            code=assemble(text)
            s=SpecMachine(code);m=MicrocodedMachine(code)
            self.assertEqual(s.run()['snapshot'],m.run()['snapshot'])
    def test_random_register_moves(self):
        rng=random.Random(1)
        for i in range(100):
            a=rng.randrange(256);b=rng.randrange(256);r=rng.randrange(4)
            code=assemble(f'LDI R0, {a}\nLDI R{r}, {b}\nMOV R1, {r}\nOUT R1, 1\nHALT')
            s=SpecMachine(code);m=MicrocodedMachine(code)
            self.assertEqual(s.run()['snapshot'],m.run()['snapshot'])
    def test_arbitrary_one_opcode_each(self):
        raw=('LDI R0, 5\nADDI R0, 255\nANDI R0, 128\nORI R0, 3\n'
             'XORI R0, 40\nSTORE R0, 23\nLOAD R2, 23\nMOV R1, 2\n'
             'CMP R0, 3\nOUT R1, 2\nNOP\nHALT')
        p=assemble(raw)
        self.assertEqual(SpecMachine(p).run()['snapshot'],MicrocodedMachine(p).run()['snapshot'])
    def test_branch_take_and_fallthrough(self):
        text='LDI R0, 1\nJNZ R0, END\nLDI R3, 10\nEND: HALT'
        p=assemble(text);a=SpecMachine(p);b=MicrocodedMachine(p)
        self.assertEqual(a.run()['snapshot'],b.run()['snapshot'])
        self.assertEqual(b.regs[3],0)
    def test_conditional_zero(self):
        text='LDI R0, 0\nJZ R0, END\nLDI R3, 10\nEND: HALT'
        p=assemble(text);self.assertEqual(SpecMachine(p).run()['snapshot'],MicrocodedMachine(p).run()['snapshot'])
    def test_compare_no_register_change(self):
        p=assemble('LDI R0, 1\nCMP R0, 255\nHALT')
        a=SpecMachine(p);b=MicrocodedMachine(p)
        self.assertEqual(a.run()['snapshot'],b.run()['snapshot'])
        self.assertEqual(a.regs[0],1)
    def test_micro_input_exhaustion_atomic(self):
        m=MicrocodedMachine(assemble('IN R0, 0\nHALT'))
        original=m.snapshot()
        m.tick();m.tick()
        with self.assertRaises(AT8Trap) as cm:m.tick()
        self.assertEqual(cm.exception.code,'input_exhausted')
        self.assertEqual(m.snapshot(),original)
    def test_input_consumption_exact_once(self):
        p=assemble('IN R0, 0\nIN R1, 0\nOUT R0, 1\nOUT R1, 1\nHALT')
        a=SpecMachine(p,{0:[1,2]});b=MicrocodedMachine(p,{0:[1,2]})
        self.assertEqual(a.run()['snapshot'],b.run()['snapshot'])
        self.assertEqual(b.cursor[0],2)
    def test_invalid_register_encoding(self):
        with self.assertRaises(DecodeError):MicrocodedMachine(bytes([0x14,5,0xF0,0]))
    def test_fallthrough_trap(self):
        p=assemble('NOP')
        m=MicrocodedMachine(p);m.step_instruction()
        with self.assertRaises(AT8Trap):m.step_instruction()
    def test_budget_no_halt(self):
        m=MicrocodedMachine(assemble('JMP 0'))
        out=m.run(11)
        self.assertFalse(out['halted']);self.assertEqual(out['microcycles'],44)
    def test_wrong_microphase_refused(self):
        m=MicrocodedMachine(assemble('NOP'))
        m.tick()
        with self.assertRaises(AT8Trap):m.step_instruction()
    def test_step_halted_refusal(self):
        m=MicrocodedMachine(assemble('HALT'));m.run()
        with self.assertRaises(AT8Trap):m.tick()
    def test_invalid_micro_budget(self):
        for x in (0,True,1.25,100001):
            with self.assertRaises(ValueError):MicrocodedMachine(assemble('HALT')).run(x)
    def test_micro_vs_atomic_flags_for_all_carry_cases(self):
        for a in (0,1,127,128,254,255):
            for b in (0,1,127,128,254,255):
                p=encode('LDI',0,a)+encode('ADDI',0,b)+encode('HALT')
                s=SpecMachine(p);m=MicrocodedMachine(p)
                s.step();s.step();m.step_instruction();m.step_instruction()
                self.assertEqual(s.snapshot(),m.snapshot())

if __name__=='__main__':unittest.main()
