"""Bounded checks for AT8 v0.4 exact NAND netlists and memory/bus models."""
import unittest,itertools,random,math,json
from computer_atlas.v04_gatelevel import NandCircuit,nand3,ripple_adder_netlist,evaluate_add,certify_at8_arithmetic
from computer_atlas.v04_memory import HarvardBus,ParityByteMemory,RoundRobinArbiter
from computer_atlas.isa import assemble

class NandLogic(unittest.TestCase):
    def test_three_valued_nand_truth(self):
        truth={(0,0):1,(0,1):1,(1,0):1,(1,1):0,(0,None):1,(None,0):1,
               (1,None):None,(None,1):None,(None,None):None}
        for pair,val in truth.items():self.assertEqual(nand3(*pair),val)
    def test_invalid_boolean_types(self):
        for v in (True,False,2,'1',1.0,[],{}):
            with self.assertRaises(ValueError):nand3(v,1)
    def test_adder_one_bit_all_inputs(self):
        for a,b,ci in itertools.product((0,1),repeat=3):
            r=evaluate_add(a,b,1,ci)
            self.assertEqual((r['result'],r['carry']),((a+b+ci)&1,(a+b+ci)>>1))
    def test_four_bit_exhaustive(self):
        for a,b in itertools.product(range(16),repeat=2):
            for ci in (0,1):
                r=evaluate_add(a,b,4,ci)
                self.assertEqual((r['result'],r['carry']),((a+b+ci)&15,(a+b+ci)>>4))
    def test_subtract_four_bit_exhaustive(self):
        for a,b in itertools.product(range(16),repeat=2):
            r=evaluate_add(a,b,4,1,True)
            self.assertEqual(r['result'],(a-b)&15)
            self.assertEqual(r['carry'],int(a>=b))
    def test_subtract_zero(self):
        for w in (1,2,4,8,16):
            self.assertEqual(evaluate_add((1<<w)-1,(1<<w)-1,w,1,True)['result'],0)
    def test_random_8bit(self):
        r=random.Random(20261117)
        for _ in range(1000):
            a=r.randrange(256);b=r.randrange(256)
            got=evaluate_add(a,b,8)
            self.assertEqual(got['result']+256*got['carry'],a+b)
    def test_random_16bit(self):
        r=random.Random(12)
        for _ in range(200):
            a=r.randrange(65536);b=r.randrange(65536)
            got=evaluate_add(a,b,16)
            self.assertEqual(got['result']+65536*got['carry'],a+b)
    def test_gate_counts(self):
        for w in (1,2,4,8,16):
            self.assertEqual(len(ripple_adder_netlist(w).gates),9*w)
            self.assertEqual(len(ripple_adder_netlist(w,True).gates),10*w)
    def test_gate_depth_increases(self):
        arr=[ripple_adder_netlist(w).structural_depth() for w in (1,2,3,4,8)]
        self.assertEqual(arr,sorted(arr))
        self.assertGreater(arr[-1],arr[0])
    def test_deterministic_netlist_hash(self):
        self.assertEqual(ripple_adder_netlist(8).sha256(),ripple_adder_netlist(8).sha256())
        self.assertNotEqual(ripple_adder_netlist(8).sha256(),ripple_adder_netlist(8,True).sha256())
    def test_netlist_time_bound(self):
        a=ripple_adder_netlist(8)
        b=a.gate_delay_bounds(1e-12,3e-12)
        self.assertGreater(b['latest_s'],b['earliest_s'])
        self.assertFalse(b['glitch_and_wire_delays_included'])
    def test_invalid_gate_delay(self):
        a=ripple_adder_netlist(8)
        for vals in [(-1,2),(3,2),(float('nan'),2),(0,float('inf'))]:
            with self.assertRaises(ValueError):a.gate_delay_bounds(*vals)
    def test_netlist_unknown_input(self):
        n=ripple_adder_netlist(1)
        r=n.eval({'a0':0,'b0':None,'c0':0})
        self.assertIsNone(r['s0'])
    def test_mask_known_reduces_unknown(self):
        self.assertEqual(nand3(0,None),1)
    def test_future_wire_rejected(self):
        with self.assertRaises(ValueError):NandCircuit(('a',),(('b','z','a'),),('b',))
    def test_duplicate_wire_rejected(self):
        with self.assertRaises(ValueError):NandCircuit(('a',),(('a','a','a'),),('a',))
    def test_missing_input_rejected(self):
        with self.assertRaises(ValueError):ripple_adder_netlist(1).eval({'a0':0,'b0':1})
    def test_invalid_unsigned_operands(self):
        for a,b,w,ci in ((-1,0,8,0),(256,0,8,0),(0,0,0,0),(0,0,8,2),(1,1,8,True)):
            with self.assertRaises(ValueError):evaluate_add(a,b,w,ci)
    def test_netlist_export_stable(self):
        n=ripple_adder_netlist(4)
        self.assertEqual(n.canonical_netlist()['schema'],'atlas.at8-nand-netlist/1')
        self.assertEqual(len(n.canonical_netlist()['gates']),36)
    def test_gate_isa_refinement(self):
        rom=assemble('LDI R0, 255\nADDI R0, 1\nCMP R0, 0\nHALT')
        x=certify_at8_arithmetic(rom)
        self.assertEqual(x['result'],'passed')
        self.assertEqual(x['exercised_arithmetic_instructions'],2)
    def test_gate_refinement_bounded_loop(self):
        rom=assemble('LDI R0, 1\nLOOP: JMP LOOP')
        x=certify_at8_arithmetic(rom,max_steps=20)
        self.assertEqual(x['result'],'HOLD')
        self.assertFalse(x['physical_hardware_validated'])

class ParityAndBus(unittest.TestCase):
    def test_ram_store_and_load(self):
        b=HarvardBus(assemble('LDI R0, 1\nHALT'))
        b.write(0,255);self.assertEqual(b.read(0),255)
    def test_fetch_aligned(self):
        rom=assemble('LDI R0, 1\nHALT')
        self.assertEqual(HarvardBus(rom).fetch(0),rom[:2])
    def test_rom_write_refused(self):
        b=HarvardBus(assemble('HALT'))
        with self.assertRaises(PermissionError):b.write_rom(0,10)
    def test_bad_ram_address_atomic(self):
        b=HarvardBus(assemble('HALT'))
        with self.assertRaises(ValueError):b.write(256,22)
        self.assertEqual(len(b.transcript),0)
    def test_rom_odd_pc_refused(self):
        with self.assertRaises(ValueError):HarvardBus(assemble('HALT')).fetch(1)
    def test_byte_typed_refusal(self):
        b=HarvardBus(assemble('HALT'))
        for x in (-1,256,True,3.2):
            with self.assertRaises(ValueError):b.write(1,x)
    def test_bus_receipt_deterministic(self):
        a=HarvardBus(assemble('HALT'));b=HarvardBus(assemble('HALT'))
        for x in (a,b):x.write(7,3);x.read(7)
        self.assertEqual(a.transcript_receipt(),b.transcript_receipt())
    def test_parity_roundtrip(self):
        m=ParityByteMemory()
        for x in range(256):m.write(3,x);self.assertEqual(m.read(3)['value'],x)
    def test_parity_one_bit_fault(self):
        for j in range(8):
            m=ParityByteMemory();m.write(2,0xAA);m.inject_data_flip(2,1<<j)
            self.assertEqual(m.read(2)['status'],'detected_parity_error')
    def test_parity_double_fault_not_detected(self):
        m=ParityByteMemory();m.write(2,0);m.inject_data_flip(2,3)
        x=m.read(2)
        self.assertNotEqual(x['value'],0)
        self.assertEqual(x['status'],'parity_consistent_not_authentic')
        self.assertFalse(m.receipt()['parity_detects_all_double_bit_errors'])
    def test_parity_bit_fault_detected(self):
        m=ParityByteMemory();m.inject_parity_flip(0)
        self.assertIsNone(m.read(0)['value'])
    def test_parity_recovery_by_rewrite(self):
        m=ParityByteMemory();m.inject_data_flip(0,1)
        self.assertIsNone(m.read(0)['value']);m.write(0,15)
        self.assertEqual(m.read(0)['value'],15)
    def test_parity_bounds(self):
        with self.assertRaises(ValueError):ParityByteMemory(257)
        with self.assertRaises(ValueError):ParityByteMemory().inject_data_flip(0,0)
    def test_round_robin_three(self):
        a=RoundRobinArbiter(3)
        self.assertEqual([a.tick([1,1,1]) for _ in range(9)],[0,1,2]*3)
    def test_round_robin_sparse(self):
        a=RoundRobinArbiter(3)
        self.assertEqual(a.tick([0,1,0]),1)
        self.assertEqual(a.tick([0,1,0]),1)
        self.assertIsNone(a.tick([0,0,0]))
    def test_round_robin_fairness(self):
        for n in range(2,9):
            a=RoundRobinArbiter(n)
            grants=[a.tick([1]*n) for _ in range(n*3)]
            self.assertEqual(grants[:n],list(range(n)))
    def test_arbiter_invalid_requests(self):
        a=RoundRobinArbiter(2)
        with self.assertRaises(ValueError):a.tick([True,0])
        with self.assertRaises(ValueError):a.tick([1])
    def test_arbiter_receipt_no_physical_claim(self):
        a=RoundRobinArbiter(2);a.tick([1,0])
        self.assertFalse(a.receipt()['independently_characterized_hardware'])

if __name__=='__main__':unittest.main()
