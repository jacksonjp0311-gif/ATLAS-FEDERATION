"""Finite v0.4 electronic reference tests. No hardware acceptance implied."""
import unittest, math, random, itertools
from electronics_atlas.v04_models import (
 digital_noise_margins,input_logic_level,logic_dag_arrival,
 synchronous_setup_hold,synchronizer_mtbf_log10,primitive_alu,
 bounded_memory_cycle,four_phase_handshake_step,rc_midpoint_delay_uncertainty)

class LogicThresholds(unittest.TestCase):
    def test_margins(self):
        x=digital_noise_margins(3.3,1.0,2.1,.4,2.9)
        self.assertAlmostEqual(x['noise_margin_low_V'],.6)
        self.assertAlmostEqual(x['noise_margin_high_V'],.8)
    def test_boundary_logic(self):
        self.assertEqual([input_logic_level(x,1.,2.) for x in (0.,1.,1.5,2.,3.)],[0,0,None,1,1])
    def test_zero_margin_permitted(self):
        self.assertEqual(digital_noise_margins(1.0,.3,.6,.3,.6)['worst_static_noise_margin_V'],0)
    def test_inconsistent_thresholds_reject(self):
        with self.assertRaises(ValueError):digital_noise_margins(1.,.8,.7,.3,.9)
    def test_nan_reject(self):
        with self.assertRaises(ValueError):input_logic_level(float('nan'),.2,.8)
    def test_negative_supply_reject(self):
        with self.assertRaises(ValueError):digital_noise_margins(-1,.3,.7,.1,.9)

class GatePath(unittest.TestCase):
    def test_serial_paths(self):
        g=[('n1',('a',),1.,3.),('n2',('n1',),2.,5.)]
        res=logic_dag_arrival(g,{'a':(0.,1.)},['n2'])['n2']
        self.assertEqual((res['earliest_s'],res['latest_s']),(3.,9.))
        self.assertEqual(res['latest_path'],('a','n1','n2'))
    def test_fanout_latest_path(self):
        g=[('low',('a',),1.,1.),('high',('b',),2.,4.),('out',('low','high'),1.,2.)]
        x=logic_dag_arrival(g,{'a':(0.,1.),'b':(0.,2.)},['out'])['out']
        self.assertEqual(x['earliest_s'],2.)
        self.assertEqual(x['latest_s'],8.)
        self.assertEqual(x['latest_path'],('b','high','out'))
    def test_undriven_reject(self):
        with self.assertRaises(ValueError):logic_dag_arrival([('x',('missing',),1,2)],{'a':(0,0)},['x'])
    def test_cycle_reject(self):
        with self.assertRaises(ValueError):logic_dag_arrival([('x',('y',),1,2),('y',('x',),1,2)],{'a':(0,0)},['x'])
    def test_duplicate_reject(self):
        with self.assertRaises(ValueError):logic_dag_arrival([('x',('a',),1,2),('x',('a',),1,2)],{'a':(0,0)},['x'])
    def test_negative_delay_reject(self):
        with self.assertRaises(ValueError):logic_dag_arrival([('x',('a',),-1,2)],{'a':(0,0)},['x'])
    def test_max_less_than_min_reject(self):
        with self.assertRaises(ValueError):logic_dag_arrival([('x',('a',),3,2)],{'a':(0,0)},['x'])

class ClockAnalysis(unittest.TestCase):
    def test_both_pass(self):
        x=synchronous_setup_hold(10.,1.,2.,2.,4.,1.,.5)
        self.assertEqual((x['setup_slack_s'],x['hold_slack_s']),(3.,2.5))
    def test_skew_tradeoff(self):
        a=synchronous_setup_hold(10.,1.,2.,2.,4.,1.,.5)
        b=synchronous_setup_hold(10.,1.,2.,2.,4.,1.,.5,2.)
        self.assertAlmostEqual(b['setup_slack_s']-a['setup_slack_s'],2.)
        self.assertAlmostEqual(b['hold_slack_s']-a['hold_slack_s'],-2.)
    def test_setup_violation(self):
        x=synchronous_setup_hold(4.,1.,2.,2.,4.,1.,.5)
        self.assertFalse(x['setup_pass'])
    def test_hold_violation(self):
        x=synchronous_setup_hold(10.,0.,0.,0.,0.,1.,.5)
        self.assertFalse(x['hold_pass'])
    def test_uncertainties_reduce_slack(self):
        a=synchronous_setup_hold(10.,1.,2.,2.,4.,1.,.5)
        b=synchronous_setup_hold(10.,1.,2.,2.,4.,1.,.5,0.,.7,.8)
        self.assertAlmostEqual(a['setup_slack_s']-b['setup_slack_s'],.7)
        self.assertAlmostEqual(a['hold_slack_s']-b['hold_slack_s'],.8)
    def test_wrong_delay_bounds(self):
        with self.assertRaises(ValueError):synchronous_setup_hold(10.,3.,2.,1.,2.,1.,1.)
    def test_negative_clock_period(self):
        with self.assertRaises(ValueError):synchronous_setup_hold(-1.,1.,2.,1.,2.,1.,1.)
    def test_mtbf_increases_with_resolution(self):
        a=synchronizer_mtbf_log10(10e6,1e6,1e-9,30e-12,1e-9)
        b=synchronizer_mtbf_log10(10e6,1e6,1e-9,30e-12,2e-9)
        self.assertAlmostEqual(b['log10_mtbf_seconds']-a['log10_mtbf_seconds'],1e-9/(30e-12*math.log(10)))
        self.assertFalse(a['hardware_certified'])
    def test_mtbf_needs_calibration(self):
        with self.assertRaises(ValueError):synchronizer_mtbf_log10(10e6,1e6,0.,30e-12,1e-9)

class ALU(unittest.TestCase):
    def test_add_exhaustive_width_4(self):
        for a in range(16):
          for b in range(16):
            r=primitive_alu(a,b,4,'ADD')
            self.assertEqual((r['result'],r['carry']),((a+b)&15,(a+b)>>4))
    def test_sub_exhaustive_width_4(self):
        for a in range(16):
          for b in range(16):
            r=primitive_alu(a,b,4,'SUB')
            self.assertEqual((r['result'],r['carry']),((a-b)&15,int(a>=b)))
    def test_boolean_exhaustive_width_4(self):
        for a in range(16):
          for b in range(16):
            for op,fn in [('AND',lambda a,b:a&b),('OR',lambda a,b:a|b),('XOR',lambda a,b:a^b)]:
              self.assertEqual(primitive_alu(a,b,4,op)['result'],fn(a,b))
    def test_shift_exhaustive_width_4(self):
        for a in range(16):
            self.assertEqual(primitive_alu(a,0,4,'SHL')['result'],(a<<1)&15)
            self.assertEqual(primitive_alu(a,0,4,'SHR')['result'],a>>1)
    def test_add_overflow(self):
        self.assertEqual(primitive_alu(7,1,4,'ADD')['overflow'],1)
        self.assertEqual(primitive_alu(15,1,4,'ADD')['overflow'],0)
    def test_sub_overflow(self):
        self.assertEqual(primitive_alu(8,1,4,'SUB')['overflow'],1)
    def test_zero_negative(self):
        self.assertEqual(primitive_alu(8,8,4,'SUB')['zero'],1)
        self.assertEqual(primitive_alu(8,0,4,'AND')['negative'],0)
    def test_invalid_operator(self):
        with self.assertRaises(ValueError):primitive_alu(1,2,4,'MUL')
    def test_invalid_word(self):
        with self.assertRaises(ValueError):primitive_alu(-1,2,4,'ADD')
    def test_random_16bit(self):
        rng=random.Random(42)
        for _ in range(200):
            a=rng.randrange(65536);b=rng.randrange(65536)
            self.assertEqual(primitive_alu(a,b,16,'ADD')['result'],(a+b)&65535)

class MemoryBus(unittest.TestCase):
    def test_read_only(self):
        x=bounded_memory_cycle([1,2,3],1,8,1,0)
        self.assertEqual(x['read_word'],2)
        self.assertEqual(x['next_words'],(1,2,3))
    def test_write_only(self):
        x=bounded_memory_cycle([1,2,3],1,8,0,1,9)
        self.assertIsNone(x['read_word'])
        self.assertEqual(x['next_words'],(1,9,3))
    def test_read_first_collision(self):
        x=bounded_memory_cycle([1,2,3],1,8,1,1,9,'read_first')
        self.assertEqual(x['read_word'],2)
        self.assertEqual(x['next_words'],(1,9,3))
    def test_write_first_collision(self):
        x=bounded_memory_cycle([1,2,3],1,8,1,1,9,'write_first')
        self.assertEqual(x['read_word'],9)
    def test_undefined_collision(self):
        x=bounded_memory_cycle([1,2,3],1,8,1,1,9)
        self.assertIsNone(x['read_word']);self.assertTrue(x['read_unknown'])
    def test_unknown_propagated(self):
        x=bounded_memory_cycle([1,None,3],1,8,1,0)
        self.assertIsNone(x['read_word'])
    def test_bad_address(self):
        with self.assertRaises(ValueError):bounded_memory_cycle([1,2,3],3,8,1,0)
    def test_bad_word(self):
        with self.assertRaises(ValueError):bounded_memory_cycle([1,2,3],1,8,1,1,256)
    def test_bad_collision_policy(self):
        with self.assertRaises(ValueError):bounded_memory_cycle([1,2,3],1,8,1,0,collision_policy='ambiguous')

class FourPhaseHandshake(unittest.TestCase):
    def test_valid_cycle(self):
        state='IDLE'
        for req,ack in ((0,0),(1,0),(1,1),(0,1),(0,0)):
            state=four_phase_handshake_step(state,req,ack)
        self.assertEqual(state,'IDLE')
    def test_stable_state_hold(self):
        self.assertEqual(four_phase_handshake_step('REQUESTED',1,0),'REQUESTED')
    def test_invalid_bypass(self):
        with self.assertRaises(ValueError):four_phase_handshake_step('IDLE',1,1)
    def test_invalid_release(self):
        with self.assertRaises(ValueError):four_phase_handshake_step('ACKNOWLEDGED',1,0)
    def test_invalid_bit_type(self):
        with self.assertRaises(ValueError):four_phase_handshake_step('IDLE',True,0)

class Measurement(unittest.TestCase):
    def test_nominal(self):
        x=rc_midpoint_delay_uncertainty(1000.,1e-9,10.,1e-11)
        self.assertAlmostEqual(x['nominal_t50_s'],math.log(2)*1e-6)
    def test_quadrature_independent(self):
        x=rc_midpoint_delay_uncertainty(1000.,1e-9,10.,1e-11)
        self.assertAlmostEqual(x['linearized_sigma_t50_s'],math.log(2)*math.sqrt((1e-9*10)**2+(1000.*1e-11)**2))
    def test_correlation_effect(self):
        pos=rc_midpoint_delay_uncertainty(1000.,1e-9,10.,1e-11,1e-10)
        neg=rc_midpoint_delay_uncertainty(1000.,1e-9,10.,1e-11,-1e-10)
        self.assertGreater(pos['linearized_sigma_t50_s'],neg['linearized_sigma_t50_s'])
    def test_invalid_covariance(self):
        with self.assertRaises(ValueError):rc_midpoint_delay_uncertainty(1000.,1e-9,10.,1e-11,2e-10)
    def test_negative_sigma(self):
        with self.assertRaises(ValueError):rc_midpoint_delay_uncertainty(1000.,1e-9,-1.,1e-11)

if __name__=='__main__':unittest.main()
