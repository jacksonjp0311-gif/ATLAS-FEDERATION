import unittest,itertools,hashlib
from computer_atlas.v02_ecc import encode_byte,decode_word,protect_rom,recover_rom,UncorrectableROMError
from computer_atlas.isa import assemble

class TestHamming138(unittest.TestCase):
    def test_all_clean(self):
        for byte in range(256):
            r=decode_word(encode_byte(byte))
            self.assertEqual(r['byte'],byte)
            self.assertEqual(r['status'],'clean')
    def test_all_single_bit_flips(self):
        for byte in range(256):
            c=encode_byte(byte)
            for i in range(13):
                r=decode_word(c^(1<<i))
                self.assertEqual(r['byte'],byte)
                self.assertEqual(r['corrected_word'],c)
                self.assertTrue(r['status'].startswith('corrected'))
    def test_all_double_bit_flips(self):
        for byte in range(256):
            c=encode_byte(byte)
            for i,j in itertools.combinations(range(13),2):
                r=decode_word(c^(1<<i)^(1<<j))
                self.assertEqual(r['status'],'detected_double')
                self.assertIsNone(r['byte'])
    def test_valid_rom(self):
        raw=assemble('LDI R0,5\nADDI R0,9\nHALT')
        code=protect_rom(raw)
        r=recover_rom(code,hashlib.sha256(raw).hexdigest())
        self.assertEqual(r['rom'],raw)
        self.assertEqual(r['corrected_words'],0)
    def test_correct_rom_single(self):
        raw=assemble('LDI R0,5\nHALT');code=list(protect_rom(raw))
        code[1]^=1<<5
        r=recover_rom(code,hashlib.sha256(raw).hexdigest())
        self.assertEqual(r['rom'],raw)
        self.assertEqual(r['corrected_words'],1)
    def test_refuse_double(self):
        raw=assemble('LDI R0,5\nHALT');code=list(protect_rom(raw))
        code[1]^=(1<<5)|(1<<2)
        with self.assertRaises(UncorrectableROMError):recover_rom(code)
    def test_wrong_sha(self):
        raw=assemble('HALT')
        with self.assertRaises(UncorrectableROMError):recover_rom(protect_rom(raw),'0'*64)
    def test_invalid_codeword(self):
        with self.assertRaises(ValueError):decode_word(8192)
        with self.assertRaises(ValueError):decode_word(True)
    def test_invalid_data(self):
        with self.assertRaises(ValueError):encode_byte(256)
        with self.assertRaises(ValueError):encode_byte(True)
    def test_invalid_rom(self):
        with self.assertRaises(ValueError):protect_rom(b'')
        with self.assertRaises(ValueError):protect_rom(b'abc')
