"""Original v0.3 bounded reference assertions; frozen v0.2 tests remain unchanged."""
import unittest,itertools,math,random
from electronics_atlas.v03_models import (
    rc_nodal_backward_euler,charge_supply_energy,nand,nand_xor,nand_full_adder,
    nand_ripple_add,register_path_timing,EdgeRegister,hamming84_encode,
    hamming84_decode,register_bank_step)

class ElectronicsV03(unittest.TestCase):
    def test_rc_one_cap_analytic_implicit(self):
        dt=1e-3;C=1e-6;G=1e-3
        r=rc_nodal_backward_euler([C],[(0,-1,G)],[2.],{}, {},dt)
        self.assertAlmostEqual(r['node_voltages_V'][0],1.,places=13)
        self.assertLess(r['kcl_residual_A'],1e-13)
    def test_rc_fixed_voltage_source(self):
        r=rc_nodal_backward_euler([1e-6,1e-6],[(0,1,1e-3)], [0.,1.],{1:1.},{},1e-3)
        self.assertAlmostEqual(r['node_voltages_V'][0],0.5,places=13)
        self.assertEqual(r['node_voltages_V'][1],1.)
    def test_rc_current_injection(self):
        r=rc_nodal_backward_euler([1e-3],[(0,-1,1e-3)],[0.],{}, {0:.001},1.)
        self.assertAlmostEqual(r['node_voltages_V'][0],.5,places=12)
    def test_rc_steady_decay(self):
        v=1.
        for k in range(20):
            r=rc_nodal_backward_euler([1e-6],[(0,-1,1e-3)],[v],{}, {},1e-3);v=r['node_voltages_V'][0]
            self.assertGreaterEqual(v,0.)
        self.assertAlmostEqual(v,2**-20,delta=1e-11)
    def test_rc_symmetry(self):
        r=rc_nodal_backward_euler([1,1],[(0,1,1),(0,-1,2),(1,-1,2)],[1,1],{}, {},1)
        self.assertAlmostEqual(r['node_voltages_V'][0],r['node_voltages_V'][1],places=13)
    def test_rc_discrete_kcl(self):
        for seed in range(40):
            rng=random.Random(seed)
            c=[rng.uniform(.02,2) for _ in range(4)]
            ed=[(0,1,2.),(1,2,3.),(2,3,1.),(3,-1,1.)]
            r=rc_nodal_backward_euler(c,ed,[rng.uniform(-2,2) for _ in c],{0:1.5},{3:.08},.04)
            self.assertLess(r['relative_kcl_residual'],2e-14)
    def test_rc_rejects_nonfinite(self):
        with self.assertRaises(ValueError):rc_nodal_backward_euler([float('nan')],[],[0],{}, {},1)
    def test_rc_rejects_invalid_connection(self):
        with self.assertRaises(ValueError):rc_nodal_backward_euler([1],[(0,2,1)],[0],{}, {},1)
    def test_rc_rejects_unknown_fixed_injection(self):
        with self.assertRaises(ValueError):rc_nodal_backward_euler([1],[],[0],{0:0},{0:1},1)
    def test_charge_energy_conservation(self):
        r=charge_supply_energy(2e-12,1.5,100,1000,1e9)
        self.assertAlmostEqual(r['supply_energy_J'],4.5e-10)
        self.assertAlmostEqual(r['mean_dynamic_power_W'],.00045)
    def test_energy_fraction_not_transitions(self):
        self.assertEqual(charge_supply_energy(1e-12,0,0,10,1e6)['supply_energy_J'],0.)
        with self.assertRaises(ValueError):charge_supply_energy(1,1,2,1,1)
    def test_nand_truth_table(self):
        for a,b in itertools.product((0,1),repeat=2):self.assertEqual(nand(a,b),1-(a&b))
    def test_xor_truth_table(self):
        for a,b in itertools.product((0,1),repeat=2):self.assertEqual(nand_xor(a,b),a^b)
    def test_full_adder_truth_table(self):
        for a,b,c in itertools.product((0,1),repeat=3):
            s,carry=nand_full_adder(a,b,c)
            self.assertEqual(s+2*carry,a+b+c)
    def test_ripple_exhaustive_4bits(self):
        for a,b,c in itertools.product(range(16),range(16),(0,1)):
            s,carry=nand_ripple_add(a,b,4,c)
            self.assertEqual(s+16*carry,a+b+c)
    def test_ripple_large_width(self):
        self.assertEqual(nand_ripple_add((1<<64)-1,1,64),(0,1))
    def test_ripple_refusals(self):
        for x in [(-1,1,4),(1,16,4),(1,1,0),(1,1,129)]:
            with self.subTest(x=x),self.assertRaises(ValueError):nand_ripple_add(*x)
    def test_timing_safe(self):
        a=register_path_timing(10,1,2,2,3,1,2)
        self.assertTrue(a['guaranteed_timing']);self.assertAlmostEqual(a['setup_margin_s'],4)
    def test_timing_skew(self):
        a=register_path_timing(10,1,2,2,3,1,2,2)
        self.assertLess(a['hold_margin_s'],0)
        self.assertFalse(a['hold_pass'])
        self.assertGreater(a['setup_margin_s'],0)
    def test_timing_frequency_not_hold_fix(self):
        for t in [1,100,1e5]:
            r=register_path_timing(t,.1,.2,.1,.3,.1,1)
            self.assertFalse(r['hold_pass'])
    def test_timing_rejects_pd_before_cd(self):
        with self.assertRaises(ValueError):register_path_timing(2,0,0,2,1,0,0)
    def test_register_nominal(self):
        r=EdgeRegister(.2,.1)
        self.assertEqual(r.capture(1,1,transition_times_s=[.5]),1)
        self.assertEqual(r.capture(0,2,transition_times_s=[1.6]),0)
    def test_register_unknown_at_setup(self):
        r=EdgeRegister(.2,.1)
        self.assertIsNone(r.capture(1,1,transition_times_s=[.9]))
        self.assertEqual(r.capture(0,2,transition_times_s=[1.4]),0)
    def test_register_unknown_at_hold(self):
        r=EdgeRegister(.2,.1)
        self.assertIsNone(r.capture(1,1,transition_times_s=[1.05]))
    def test_register_reject_edge_order(self):
        r=EdgeRegister(0,0);r.capture(0,1)
        with self.assertRaises(ValueError):r.capture(1,1)
    def test_register_reject_transition_order(self):
        with self.assertRaises(ValueError):EdgeRegister(0,0).capture(0,1,[.2,.1])
    def test_codeword_all_single_errors(self):
        for m in range(16):
            word=hamming84_encode(m)
            self.assertEqual(hamming84_decode(word)['data'],m)
            for b in range(8):
                d=hamming84_decode(word^(1<<b))
                self.assertEqual(d['data'],m)
                self.assertEqual(d['status'],'corrected_single')
    def test_codeword_all_double_errors(self):
        for m in range(16):
            word=hamming84_encode(m)
            for i,j in itertools.combinations(range(8),2):
                d=hamming84_decode(word^(1<<i)^(1<<j))
                self.assertEqual(d['status'],'detected_double')
                self.assertIsNone(d['data'])
    def test_codeword_encode_parity(self):
        for m in range(16):
            self.assertEqual(hamming84_decode(hamming84_encode(m))['status'],'clean')
    def test_codeword_refuses_invalid(self):
        for v in [-1,256,1.1,True]:
            with self.assertRaises(ValueError):hamming84_decode(v)
    def test_bank_write_read(self):
        a,q=register_bank_step([0,1,2],1,254,True)
        self.assertEqual(a,(0,254,2));self.assertEqual(q,254)
    def test_bank_propagates_unknown(self):
        a,q=register_bank_step([0,1,2],1,None,True)
        self.assertIsNone(q);self.assertIsNone(a[1])
        b,z=register_bank_step(a,1,3,False)
        self.assertIsNone(z)
    def test_bank_reject_bad_values(self):
        with self.assertRaises(ValueError):register_bank_step([0,1],2,1,True)

if __name__=='__main__':unittest.main()
