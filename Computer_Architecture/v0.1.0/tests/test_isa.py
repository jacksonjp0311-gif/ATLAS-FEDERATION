import unittest
from computer_atlas.isa import (OPS,CODES,REGISTER_OPS,AssemblyError,DecodeError,
    encode,decode,assemble,disassemble,validate_rom)
from computer_atlas.programs import examples

class TestInstructionContract(unittest.TestCase):
    def test_exact_16_opcodes(self):
        self.assertEqual(len(OPS),16);self.assertEqual(len(CODES),16)
        self.assertEqual(set(CODES),set(OPS.values()))
    def test_all_encodings(self):
        for op in OPS.values():
            for r in range(4) if op in REGISTER_OPS else [None]:
                values=range(4) if op=='MOV' or op in ('IN','OUT') else [0,1,17,200] if op not in ('NOP','HALT') else [0]
                for val in values:
                    if op in ('JMP','JZ','JNZ') and val%2:continue
                    encoded=encode(op,r,val)
                    instr=decode(encoded,0)
                    self.assertEqual((instr.name,instr.reg,instr.operand),(op,r,val))
                    self.assertEqual(len(encoded),2)
    def test_all_reserved_register_bits_rejected(self):
        for top,op in OPS.items():
            for low in range(4,16) if op in REGISTER_OPS else range(1,16):
                with self.subTest(op=op,low=low),self.assertRaises(DecodeError):
                    decode(bytes([top<<4|low,0]))
    def test_reserved_operand_bits_rejected(self):
        for op in ('NOP','HALT'):
            for value in (1,17,255):
                with self.assertRaises(DecodeError):decode(bytes([CODES[op]<<4,value]))
    def test_mov_ports_invalid(self):
        for op in ('MOV','IN','OUT'):
            with self.assertRaises(DecodeError):decode(bytes([CODES[op]<<4,255]))
    def test_branch_alignment(self):
        for op in ('JMP','JZ','JNZ'):
            with self.assertRaises(DecodeError):decode(bytes([CODES[op]<<4,3]))
    def test_nonsense_length_type(self):
        for x in (b'',b'\x00',b'\x00\x00\x00',(0,0),'00'):
            with self.assertRaises(DecodeError):decode(x)
    def test_alignment_pc(self):
        with self.assertRaises(DecodeError):decode(b'\x00\x00',1)
    def test_basic_roundtrip(self):
        for name,blob in examples().items():
            self.assertEqual(assemble(disassemble(blob)),blob,name)
    def test_comments_labels_case(self):
        program='''# comment
START: ldi r0, 2 ; initial
next: OUT R0, 0
ADDI R0, 255
JNZ R0, NEXT
halt
'''
        b=assemble(program)
        self.assertEqual(decode(b[6:8]).name,'JNZ')
        self.assertEqual(decode(b[6:8]).operand,2)
    def test_duplicate_labels(self):
        with self.assertRaises(AssemblyError):assemble('A: NOP\nA: HALT')
    def test_undefined_label(self):
        with self.assertRaises(AssemblyError):assemble('JMP NOT_HERE\nHALT')
    def test_branch_outside_rom(self):
        with self.assertRaises(AssemblyError):assemble('JMP 42\nHALT')
    def test_odd_jump(self):
        with self.assertRaises(AssemblyError):assemble('JMP 3\nHALT')
    def test_bad_register(self):
        for src in ('LDI R4, 0','ADD R0, 2','MOV R0, R1','OUT 0, 0','STORE R-1, 4'):
            with self.subTest(src=src),self.assertRaises(AssemblyError):assemble(src)
    def test_bound_literal(self):
        for src in ('LDI R0, 256','LDI R0, -1','LDI R0, 4.5'):
            with self.assertRaises(AssemblyError):assemble(src)
    def test_256_rom_length(self):
        source='\n'.join(['NOP']*127+['HALT'])
        p=assemble(source)
        self.assertEqual(len(p),256)
        with self.assertRaises(AssemblyError):assemble(source+'\nNOP')
    def test_no_undocumented_extensions(self):
        with self.assertRaises(AssemblyError):assemble('.WORD 5\nHALT')
    def test_empty_program(self):
        with self.assertRaises(AssemblyError):assemble('; comment only')
    def test_rom_has_halt_not_termination_proof(self):
        self.assertTrue(validate_rom(assemble('HALT'))['has_halt'])
        self.assertFalse(validate_rom(assemble('JMP 0'))['has_halt'])
        self.assertIn('not termination proof',validate_rom(assemble('HALT'))['evidence'])
    def test_rom_branch_outside(self):
        with self.assertRaises(DecodeError):validate_rom(bytes([0xB0,0x20,0xF0,0]))

if __name__=='__main__':unittest.main()
