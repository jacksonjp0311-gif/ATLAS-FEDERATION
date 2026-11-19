import unittest,itertools,random
from computer_atlas.gates import nand,nand_xor,full_adder,ripple_add,alu8

class TestGates(unittest.TestCase):
    def test_nand_all(self):
        for a,b in itertools.product((0,1),repeat=2):self.assertEqual(nand(a,b),1-(a&b))
    def test_xor_all(self):
        for a,b in itertools.product((0,1),repeat=2):self.assertEqual(nand_xor(a,b),a^b)
    def test_full_adder_all_eight(self):
        for a,b,c in itertools.product((0,1),repeat=3):
            s,cy=full_adder(a,b,c);self.assertEqual(s+2*cy,a+b+c)
    def test_all_unsigned_4_bit_pairs(self):
        for a,b,c in itertools.product(range(16),range(16),(0,1)):
            x,y=ripple_add(a,b,4,c);self.assertEqual((x,y),((a+b+c)&15,(a+b+c)>>4))
    def test_extreme_32_bit_carry(self):
        self.assertEqual(ripple_add((1<<32)-1,1,32),(0,1))
    def test_random_8_bit_adder(self):
        r=random.Random(42)
        for _ in range(1024):
            a=r.randrange(256);b=r.randrange(256)
            self.assertEqual(ripple_add(a,b),( (a+b)&255, (a+b)>>8 ))
    def test_carry_reversible_complement_subtract(self):
        for a in range(16):
            for b in range(16):
                difference,carry=ripple_add(a,15^b,4,1)
                self.assertEqual((difference,carry),((a-b)&15,int(a>=b)))
    def test_alu_all_cases(self):
        for a,b in itertools.product(range(16),repeat=2):
            for op,expected in [('ADD',(a+b)&255),('XOR',a^b),('AND',a&b),('OR',a|b),('CMP',(a-b)&255)]:
                self.assertEqual(alu8(a,b,op)['value'],expected)
    def test_alu_flags(self):
        self.assertEqual(alu8(127,1,'ADD')['overflow'],1)
        self.assertEqual(alu8(255,1,'ADD')['carry'],1)
        self.assertEqual(alu8(0,0,'CMP')['zero'],1)
        self.assertEqual(alu8(0,1,'CMP')['carry'],0)
    def test_nand_invalid(self):
        for a in (None,2,-1,True,'1'):
            with self.assertRaises(ValueError):nand(a,1)
    def test_add_invalid(self):
        for args in [(1,1,0),(256,1,8),(-1,2,8),(1,1,33),(1,1,8,2)]:
            with self.assertRaises(ValueError):ripple_add(*args)
    def test_alu_invalid(self):
        for args in [(-1,2,'ADD'),(1,256,'ADD'),(1,2,'MUL')]:
            with self.assertRaises(ValueError):alu8(*args)

if __name__=='__main__':unittest.main()
