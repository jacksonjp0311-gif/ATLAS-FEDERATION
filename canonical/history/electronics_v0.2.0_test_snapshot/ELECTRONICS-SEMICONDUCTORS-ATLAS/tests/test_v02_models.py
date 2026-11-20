import unittest,math,itertools,random
from electronics_atlas.v02_models import *
from electronics_atlas.models import Q
class TestV02Models(unittest.TestCase):
    def test_bernoulli(self):
        for z in [0.,1e-13,1e-6,.1,2,20,50,51,100,400,-1e-10,-.1,-2,-51,-400]:
            self.assertTrue(math.isfinite(bernoulli_stable(z)))
            self.assertAlmostEqual(bernoulli_stable(-z)-bernoulli_stable(z),z,delta=1e-10*max(1,abs(z)))
    def test_bernoulli_limits(self):
        self.assertEqual(bernoulli_stable(0),1.)
        self.assertAlmostEqual(bernoulli_stable(1e-4),0.9999500008333333,places=11)
        self.assertEqual(bernoulli_stable(900),0.)
        self.assertEqual(bernoulli_stable(-900),900.)
    def test_sg_uniform_drift(self):
        n=1e19;E=500;mu=.07
        j=sg_electron_current(n,n,E,1e-6,mu,300.)
        self.assertAlmostEqual(j/(Q*mu*n*E),1,places=12)
    def test_sg_diffusion_zero_e(self):
        l=1e19;r=2e19;L=1e-6;mu=.05;T=300
        d=mu*thermal_voltage(T)
        self.assertAlmostEqual(sg_electron_current(l,r,0,L,mu,T)/(Q*d*(r-l)/L),1,places=13)
    def test_sg_equilibrium(self):
        l=1e19;E=300;L=1e-6;T=300
        Pe=-E*L/thermal_voltage(T)
        r=l*math.exp(Pe)
        self.assertAlmostEqual(sg_electron_current(l,r,E,L,.04,T),0.,delta=.0001)
    def test_sg_reversal(self):
        a=sg_electron_current(1e18,9e18,200,1e-6,.03,300)
        b=sg_electron_current(9e18,1e18,-200,1e-6,.03,300)
        self.assertAlmostEqual(a,-b,delta=1e-8)
    def test_minority_boundaries(self):
        p=minority_diffusion_profile(1e18,0,1e-6,.002,1e-7,20)
        self.assertEqual(p['density_m3'][0],1e18)
        self.assertEqual(p['density_m3'][-1],0)
        self.assertTrue(all(x>=0 for x in p['density_m3']))
        self.assertLess(abs(p['discrete_conservation_residual_m2_s']),1e-13*abs(p['particle_flux_m2_s'][0]))
    def test_minority_refinement(self):
        errs=[]
        for c in (20,40,80):
            p=minority_diffusion_profile(1.,.1,1e-5,.002,1e-7,c)
            truth=[minority_analytic(i*p['dx_m'],1.,.1,1e-5,.002,1e-7) for i in range(c+1)]
            errs.append(max(abs(a-b) for a,b in zip(p['density_m3'],truth)))
        self.assertTrue(errs[0]>errs[1]*3.9 and errs[1]>errs[2]*3.9)
    def test_minority_analytic_limits(self):
        self.assertEqual(minority_analytic(0,1,0,1e-4,.001,1e-8),1.)
        self.assertEqual(minority_analytic(1e-4,1,0,1e-4,.001,1e-8),0.)
    def test_resistor_voltage_divider(self):
        p=resistor_network(3,[(0,1,1000.),(1,2,2000.)],{0:3.,2:0.})
        self.assertAlmostEqual(p['node_voltages_V'][1],2.)
        self.assertAlmostEqual(p['resistive_power_W'],.003)
        self.assertAlmostEqual(p['injected_plus_supply_power_W'],.003)
        self.assertLess(p['unknown_kcl_residual_A'],1e-12)
    def test_resistor_source_injection(self):
        p=resistor_network(2,[(0,1,1000.)],{0:0},{1:.002})
        self.assertAlmostEqual(p['node_voltages_V'][1],2.)
        self.assertAlmostEqual(p['resistive_power_W'],.004)
    def test_resistor_parallel_and_float(self):
        p=resistor_network(2,[(0,1,1e3),(0,1,1e3)],{0:0},{1:.002})
        self.assertAlmostEqual(p['node_voltages_V'][1],1.)
        with self.assertRaises(ValueError):resistor_network(3,[(0,1,10.)],{0:0})
    def test_cmos_endpoints(self):
        params=(1.2,1e-4,1e-4,.3,.3)
        self.assertEqual(ideal_cmos_inverter_output(0,*params),1.2)
        self.assertEqual(ideal_cmos_inverter_output(1.2,*params),0)
        with self.assertRaises(ValueError):ideal_cmos_inverter_output(.6,*params)  # degenerate ideal saturation plateau
    def test_cmos_monotonic(self):
        params=(1.2,1e-4,2e-4,.2,.25)
        vals=[ideal_cmos_inverter_output(x/40*1.2,*params) for x in range(41)]
        self.assertTrue(all(a+1e-9>=b for a,b in zip(vals,vals[1:])))
    def test_cmos_no_both_off(self):
        with self.assertRaises(ValueError):ideal_cmos_inverter_output(.5,.9,1e-4,1e-4,.6,.6)
    def test_noise_margin(self):
        for v in noise_margins_from_characterization(.1,1.1,.4,.8,1.2):self.assertAlmostEqual(v,.3)
        with self.assertRaises(ValueError):noise_margins_from_characterization(.5,1.,.4,.8,1.2)
    def test_adder_exhaustive(self):
        for a,b,c in itertools.product((0,1),repeat=3):
            s,co=full_adder(a,b,c); self.assertEqual(s+2*co,a+b+c)
    def test_ripple_exhaustive(self):
        for a,b,cin in itertools.product(range(8),range(8),(0,1)):
            s,c=ripple_adder_unsigned(a,b,3,cin)
            self.assertEqual(s+8*c,a+b+cin)
    def test_ripple_width(self):
        s,c=ripple_adder_unsigned((1<<64)-1,1,64)
        self.assertEqual((s,c),(0,1))
    def test_uncertainty(self):
        q=diode_current_local_uncertainty(1e-12,.2,300,1.,.001,.2)
        self.assertGreater(q['first_order_sigma_A'],0.)
        h=1e-7; f=lambda v:1e-12*math.expm1(v/thermal_voltage(300))
        self.assertAlmostEqual(q['dI_dV_A_per_V'],(f(.2+h)-f(.2-h))/(2*h),delta=1e-7*q['dI_dV_A_per_V'])
    def test_uncertainty_covariance(self):
        q=diode_current_local_uncertainty(1e-12,.2,300,1.,.001,.2,-.0002)
        self.assertGreaterEqual(q['first_order_sigma_A'],0.)
    def test_refusals(self):
        examples=[(bernoulli_stable,(float('nan'),)),(sg_electron_current,(-1,1,0,1,.1,300)),
          (minority_diffusion_profile,(1,1,1,.1,1,2)),(minority_analytic,(2,1,1,1,.1,1)),
          (resistor_network,(3,[(0,1,-1.)],{0:0})),(resistor_network,(2,[(0,1,1.)],{})),
          (ideal_cmos_inverter_output,(2,1,1,1,.2,.2)),
          (ripple_adder_unsigned,(8,1,3)),(diode_current_local_uncertainty,(1e-12,.1,300,1,1,1,2))]
        for fn,args in examples:
            with self.subTest(fn=fn.__name__):
                with self.assertRaises(ValueError):fn(*args)
if __name__=='__main__':unittest.main()
