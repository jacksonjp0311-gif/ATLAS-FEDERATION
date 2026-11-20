import unittest
from computer_atlas.v02_control import control_flow_analysis
from computer_atlas.isa import assemble

class TestAT8ControlFlow(unittest.TestCase):
    def test_linear_halt(self):
        x=control_flow_analysis(assemble('LDI R0,5\nADDI R0,3\nHALT'))
        self.assertTrue(x['all_structural_paths_terminate_at_halt'])
        self.assertEqual(x['unreachable_pcs'],tuple())
    def test_unconditional_jump_skips_code(self):
        x=control_flow_analysis(assemble('JMP END\nLDI R0,99\nEND: HALT'))
        self.assertEqual(x['unreachable_pcs'],(2,))
        self.assertTrue(x['all_structural_paths_terminate_at_halt'])
    def test_loop_conservative(self):
        x=control_flow_analysis(assemble('LDI R0,3\nL: ADDI R0,255\nJNZ R0,L\nHALT'))
        self.assertTrue(x['reachable_structural_cycles'])
        self.assertFalse(x['all_structural_paths_terminate_at_halt'])
        self.assertIn(6,x['reachable_halts'])
    def test_conditional_acyclic(self):
        x=control_flow_analysis(assemble('LDI R0,0\nJZ R0,DONE\nNOP\nDONE: HALT'))
        self.assertTrue(x['all_structural_paths_terminate_at_halt'])
    def test_falloff_trap(self):
        x=control_flow_analysis(assemble('LDI R0,0\nNOP'))
        self.assertEqual(x['reachable_falloff_traps'],(2,))
        self.assertFalse(x['all_structural_paths_terminate_at_halt'])
    def test_unreachable_loop_does_not_block(self):
        x=control_flow_analysis(assemble('JMP DONE\nLOOP: JMP LOOP\nDONE: HALT'))
        self.assertEqual(x['unreachable_pcs'],(2,))
        self.assertTrue(x['all_structural_paths_terminate_at_halt'])
    def test_only_halt(self):
        x=control_flow_analysis(assemble('HALT'))
        self.assertTrue(x['all_structural_paths_terminate_at_halt'])
    def test_runtime_input_not_proved(self):
        x=control_flow_analysis(assemble('IN R0,1\nHALT'))
        self.assertTrue(x['all_structural_paths_terminate_at_halt'])
        self.assertIn('input exhaustion',x['limitations'])
    def test_input_rom_invalid(self):
        with self.assertRaises(ValueError):control_flow_analysis(b'')
