"""Bounded original RC1 Electronics reference checks, no equipment or claims of calibration."""
import unittest, math, random
from electronics_atlas.v1_scoped_models import *

class TestElectronicsScoped(unittest.TestCase):
    def test_oxide_capacitance(self):
        for er in (1.2,3.9,15):
            for t in (1e-9,2e-8,5e-7):
                a=mos_oxide_capacitance(1e-12,t,er)
                self.assertAlmostEqual(a['capacitance_F'], 8.8541878128e-12*er*1e-12/t,delta=1e-27)
    def test_oxide_thickness_monotone(self):
        a=mos_oxide_capacitance(1e-12,1e-8,3.9)['capacitance_F']
        b=mos_oxide_capacitance(1e-12,2e-8,3.9)['capacitance_F']
        self.assertAlmostEqual(a/b,2)
    def test_oxide_invalid(self):
        for args in ((0,1e-9,3.9),(1e-12,0,3.9),(1e-12,1e-9,-1),('x',1e-9,3.9),(True,1e-9,3.9)):
            with self.assertRaises(ValueError):mos_oxide_capacitance(*args)
    def test_body_effect_zero(self):
        self.assertAlmostEqual(mos_body_effect_threshold(.6,.3,.3,0),.6)
    def test_body_effect_monotone(self):
        prev=mos_body_effect_threshold(.6,.3,.3,0)
        for sb in (.1,.4,1,2,4):
            out=mos_body_effect_threshold(.6,.3,.3,sb)
            self.assertGreater(out,prev);prev=out
    def test_body_effect_invalid(self):
        for sb in (-.1,float('nan'),float('inf')):
            with self.assertRaises(ValueError):mos_body_effect_threshold(.5,.3,.4,sb)
    def test_nmos_cutoff(self):
        for vg in (0,.1,.49):self.assertEqual(long_channel_nmos(vg,1,.5,1e-3)['current_A'],0)
    def test_nmos_linear(self):
        v=long_channel_nmos(1,.25,.5,1e-3)
        self.assertEqual(v['region'],'linear');self.assertAlmostEqual(v['current_A'],9.375e-5)
    def test_nmos_saturation(self):
        v=long_channel_nmos(1,2,.5,1e-3)
        self.assertEqual(v['region'],'saturation');self.assertAlmostEqual(v['current_A'],.000125)
    def test_nmos_continuity(self):
        a=long_channel_nmos(1,.5-1e-9,.5,1e-3)['current_A']
        b=long_channel_nmos(1,.5,.5,1e-3)['current_A']
        self.assertAlmostEqual(a,b,delta=1e-12)
    def test_nmos_lambda(self):
        a=long_channel_nmos(1,2,.5,1e-3,.1)['current_A']
        b=long_channel_nmos(1,2,.5,1e-3,0)['current_A']
        self.assertAlmostEqual(a/b,1.2)
    def test_nmos_invalid(self):
        with self.assertRaises(ValueError):long_channel_nmos(1,-.1,.5,1e-3)
        with self.assertRaises(ValueError):long_channel_nmos(1,.1,.5,0)
    def test_thermal_voltage_300K(self):
        self.assertAlmostEqual(thermal_voltage(300),.025851999786435535,places=12)
    def test_thermal_voltage_invalid(self):
        with self.assertRaises(ValueError):thermal_voltage(0)
    def test_diode_zero(self):
        self.assertEqual(ideal_diode_current(0,1e-12,1,300),0)
    def test_diode_reverse(self):
        x=ideal_diode_current(-3,1e-12,1,300)
        self.assertAlmostEqual(x,-1e-12,delta=1e-23)
    def test_diode_forward(self):
        self.assertGreater(ideal_diode_current(.3,1e-12,1.5,300),0)
    def test_diode_expm1_small(self):
        v=1e-12;VT=thermal_voltage(300)
        self.assertAlmostEqual(ideal_diode_current(v,1e-12,1,300),1e-12*v/VT,delta=1e-23)
    def test_diode_overflow_rejection(self):
        with self.assertRaises(ValueError):ideal_diode_current(100,1e-12,1,300)
    def test_diode_positive_slope(self):
        ps=[ideal_diode_current(x,1e-12,1,300) for x in (-.2,0,.1,.2,.4)]
        self.assertEqual(ps,sorted(ps))
    def test_diffusion_surface_peak(self):
        res=half_space_gaussian_dopant(1e16,1e-14,10,0)
        self.assertAlmostEqual(res['volume_density_per_m3'],1e16/math.sqrt(math.pi*1e-13))
    def test_diffusion_dose_conservation(self):
        for x in (0,1e-6,1e-5,1e-4):
            r=half_space_gaussian_dopant(1e16,1e-14,10,x)
            self.assertLessEqual(r['integrated_sheet_dose_per_m2'],r['total_sheet_dose_per_m2'])
    def test_diffusion_mass_ten_sigma(self):
        r=half_space_gaussian_dopant(1e16,1e-14,10,10*math.sqrt(1e-13))
        self.assertAlmostEqual(r['integrated_sheet_dose_per_m2']/1e16,1,delta=1e-10)
    def test_diffusion_invalid(self):
        for args in ((1e16,0,1,1e-7),(1e16,1e-14,0,1e-7),(1e16,1e-14,1,-1)):
            with self.assertRaises(ValueError):half_space_gaussian_dopant(*args)
    def test_sheet_resistance(self):
        self.assertAlmostEqual(four_point_sheet_resistance(0.01,.001),45.32360141827194,places=10)
    def test_sheet_resistance_no_current(self):
        with self.assertRaises(ValueError):four_point_sheet_resistance(.1,0)
    def test_hall_reference(self):
        known_n=1e22;t=1e-3;I=.01;B=.5
        vh=I*B/(ELEMENTARY_CHARGE_C*known_n*t)
        self.assertAlmostEqual(hall_carrier_density(I,B,t,vh)/known_n,1,places=12)
    def test_hall_ambiguous(self):
        with self.assertRaises(ValueError):hall_carrier_density(.01,0,.001,.01)
        with self.assertRaises(ValueError):hall_carrier_density(.01,.5,.001,0)
    def test_thermal_initial(self):
        self.assertAlmostEqual(thermal_rc(0,300,350,2,10,.1),350)
    def test_thermal_limit(self):
        self.assertAlmostEqual(thermal_rc(1000,300,350,2,10,.1),320,places=8)
    def test_thermal_monotone(self):
        arr=[thermal_rc(t,300,300,2,10,.1) for t in (0,.1,.5,1,10)]
        self.assertEqual(arr,sorted(arr))
    def test_dram_refresh_boundary(self):
        x=dram_retention(1e-14,.2e-14,1e-3,0)
        deadline=x['ideal_refresh_deadline_s']
        self.assertTrue(dram_retention(1e-14,.2e-14,1e-3,deadline*.95)['retains_state'])
        self.assertFalse(dram_retention(1e-14,.2e-14,1e-3,deadline*1.05)['retains_state'])
    def test_dram_invalid(self):
        with self.assertRaises(ValueError):dram_retention(1e-14,2e-14,1e-3,0)
    def test_yield_bound(self):
        for d in (0,.01,.1,1,10):
            for a in (0,.01,.1,1):self.assertTrue(0<=poisson_defect_free_yield(d,a)<=1)
    def test_yield_poisson(self):
        self.assertAlmostEqual(poisson_defect_free_yield(.2,3),math.exp(-.6))
    def test_yield_no_defects(self):
        self.assertEqual(poisson_defect_free_yield(0,10),1)
    def test_feature_budget(self):
        x=line_edge_overlay_budget(1,2,3,40)
        self.assertEqual(x['max_absolute_feature_error_nm'],6)
        self.assertAlmostEqual(x['relative_bound'],.15)
    def test_feature_invalid(self):
        with self.assertRaises(ValueError):line_edge_overlay_budget(-1,1,1,20)
    def test_microprogram(self):
        # LDI 5, ADD 7, STORE 0, XOR 3, HALT: 5+7=12, 12 xor 3 =15
        code=bytes([0x10,5,0x20,7,0x40,0,0x30,3,0xf0,0])
        x=EightBitAccumulator(code).run()
        self.assertTrue(x['halted']);self.assertEqual(x['accumulator'],15)
        self.assertEqual(x['ram'][0],12);self.assertEqual(x['steps'],5)
    def test_microprogram_branch(self):
        code=bytes([0x10,1,0x60,6,0x10,99,0x20,6,0xf0,0])
        self.assertEqual(EightBitAccumulator(code).run()['accumulator'],7)
    def test_microprogram_wrap(self):
        code=bytes([0x10,255,0x20,1,0xf0,0])
        self.assertEqual(EightBitAccumulator(code).run()['accumulator'],0)
    def test_microprogram_unsupported(self):
        with self.assertRaises(ValueError):EightBitAccumulator(bytes([0x70,0])).run()
    def test_microprogram_halt_guard(self):
        code=bytes([0x10,1,0x60,0])
        out=EightBitAccumulator(code,max_steps=9).run()
        self.assertFalse(out['halted']);self.assertEqual(out['steps'],9)
    def test_microprogram_address_guard(self):
        with self.assertRaises(ValueError):EightBitAccumulator(bytes([0x40,16,0xf0,0])).run()
    def test_microprogram_alignment(self):
        with self.assertRaises(ValueError):EightBitAccumulator(bytes([0x10,1,0x60,1])).run()
    def test_microprogram_invalid_type(self):
        with self.assertRaises(ValueError):EightBitAccumulator([0x10,1]).run()
    def test_microprogram_determinism(self):
        p=bytes([0x10,33,0x20,71,0x40,4,0x50,4,0xf0,0])
        self.assertEqual(EightBitAccumulator(p).run(),EightBitAccumulator(p).run())
    def test_invalid_bools(self):
        for fn,args in ((thermal_voltage,(True,)),(poisson_defect_free_yield,(False,1)),(long_channel_nmos,(1,1,.1,True))):
            with self.assertRaises(ValueError):fn(*args)
    def test_nan_rejections(self):
        for fn,args in ((thermal_rc,(0,300,300,float('nan'),1,1)),
                        (long_channel_nmos,(float('inf'),1,.1,1)),
                        (half_space_gaussian_dopant,(1,1,1,float('nan')))):
            with self.assertRaises(ValueError):fn(*args)

if __name__=='__main__':unittest.main()
