import unittest,random,itertools
from computer_atlas.isa import assemble, encode, DecodeError,AssemblyError
from computer_atlas.spec import SpecMachine, AT8Trap
from computer_atlas.programs import examples

class TestSpec(unittest.TestCase):
    def test_hello_program(self):
        r=SpecMachine(examples()['arithmetic_memory']).run()
        self.assertTrue(r['halted'])
        self.assertEqual(r['snapshot']['ram'][0],12)
        self.assertEqual(r['snapshot']['regs'][0],15)
        self.assertEqual(r['snapshot']['output'],((0,15),))
    def test_countdown(self):
        r=SpecMachine(examples()['countdown']).run()
        self.assertEqual(r['snapshot']['output'],((0,3),(0,2),(0,1)))
        self.assertTrue(r['halted'])
    def test_input_tape(self):
        r=SpecMachine(examples()['input_output'],{1:[7]}).run()
        self.assertEqual(r['snapshot']['output'],((2,9),))
        self.assertEqual(r['snapshot']['ram'][4],9)
        self.assertEqual(r['snapshot']['input_cursors'][1],1)
    def test_exhaustive_addi(self):
        for a in range(256):
            for b in range(256):
                machine=SpecMachine(encode('LDI',0,a)+encode('ADDI',0,b)+encode('HALT'))
                machine.step();machine.step()
                self.assertEqual(machine.regs[0],(a+b)&255)
                self.assertEqual(machine.flags[2],int(a+b>255))
    def test_flags_zero(self):
        m=SpecMachine(assemble('LDI R0, 255\nADDI R0, 1\nHALT'))
        m.step();m.step()
        self.assertEqual(m.flags,(1,0,1,0))
    def test_flags_signed_overflow(self):
        m=SpecMachine(assemble('LDI R0, 127\nADDI R0, 1\nHALT'))
        m.step();m.step()
        self.assertEqual(m.flags,(0,1,0,1))
    def test_load_store(self):
        m=SpecMachine(assemble('LDI R3, 77\nSTORE R3, 200\nLOAD R2, 200\nHALT'))
        self.assertEqual(m.run()['snapshot']['regs'][2],77)
    def test_mov_old_register(self):
        m=SpecMachine(assemble('LDI R0, 255\nMOV R1, 0\nHALT'))
        self.assertEqual(m.run()['snapshot']['regs'][1],255)
    def test_cmp_signed_difference(self):
        m=SpecMachine(assemble('LDI R0, 127\nCMP R0, 255\nHALT'))
        m.step();m.step()
        self.assertEqual(m.flags[3],1)
        self.assertEqual(m.regs[0],127)
    def test_branch_zero_uses_reg_not_flags(self):
        program=assemble('LDI R0, 1\nCMP R0, 1\nJZ R0, SKIP\nOUT R0, 0\nSKIP: HALT')
        m=SpecMachine(program)
        self.assertEqual(m.run()['snapshot']['output'],((0,1),))
    def test_branch_take_zero(self):
        m=SpecMachine(assemble('LDI R0, 0\nJZ R0, TARGET\nLDI R1, 99\nTARGET: HALT'))
        self.assertEqual(m.run()['snapshot']['regs'][1],0)
    def test_branch_jnz(self):
        m=SpecMachine(assemble('LDI R0, 1\nJNZ R0, TARGET\nLDI R1, 99\nTARGET: HALT'))
        self.assertEqual(m.run()['snapshot']['regs'][1],0)
    def test_bounded_loop(self):
        m=SpecMachine(assemble('JMP 0'))
        r=m.run(max_steps=19)
        self.assertFalse(r['halted']);self.assertEqual(r['steps'],19)
        self.assertEqual(r['stop_reason'],'bounded_step_budget')
    def test_fallthrough_traps(self):
        m=SpecMachine(assemble('NOP'))
        m.step()
        with self.assertRaises(AT8Trap) as cm:m.step()
        self.assertEqual(cm.exception.code,'program_counter')
    def test_empty_input_atomic_trap(self):
        m=SpecMachine(assemble('IN R0, 1\nHALT'))
        before=m.snapshot()
        with self.assertRaises(AT8Trap) as cm:m.step()
        self.assertEqual(cm.exception.code,'input_exhausted')
        self.assertEqual(m.snapshot(),before)
    def test_no_trap_flag_side_effect(self):
        m=SpecMachine(assemble('LDI R0, 99\nIN R1, 0\nHALT'))
        m.step();before=m.snapshot()
        with self.assertRaises(AT8Trap):m.step()
        self.assertEqual(m.snapshot(),before)
    def test_output_doesnt_mutate_flags(self):
        m=SpecMachine(assemble('LDI R0, 128\nOUT R0, 1\nHALT'))
        m.step();f=m.flags;m.step();self.assertEqual(m.flags,f)
    def test_reset_zero_state(self):
        m=SpecMachine(assemble('HALT'))
        self.assertEqual(m.snapshot()['regs'],(0,0,0,0))
        self.assertEqual(sum(m.snapshot()['ram']),0)
        self.assertEqual(m.flags,(1,0,0,0))
    def test_halt_no_step(self):
        m=SpecMachine(assemble('HALT'));m.run()
        with self.assertRaises(AT8Trap):m.step()
    def test_rom_invalid_before_execution(self):
        with self.assertRaises(DecodeError):SpecMachine(b'\xF0\x01')
    def test_bad_inputs(self):
        for t in [{8:[1]},{0:[256]},{0:[True]},[1,2],{0:'abc'}]:
            with self.assertRaises(ValueError):SpecMachine(assemble('HALT'),t)
    def test_run_budget_bad(self):
        for budget in (0,1.5,True,100001):
            with self.assertRaises(ValueError):SpecMachine(assemble('HALT')).run(budget)
    def test_io_port_order(self):
        p=assemble('IN R0, 0\nOUT R0, 1\nIN R0, 0\nOUT R0, 2\nHALT')
        r=SpecMachine(p,{0:[10,11]}).run()
        self.assertEqual(r['snapshot']['output'],((1,10),(2,11)))
    def test_compare_carry(self):
        m=SpecMachine(assemble('LDI R0, 3\nCMP R0, 4\nHALT'))
        m.step();m.step();self.assertEqual(m.flags[2],0)

if __name__=='__main__':unittest.main()
