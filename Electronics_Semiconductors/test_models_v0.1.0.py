"""Bounded, independently checkable reference invariants."""
import math,unittest
from electronics_atlas.models import *
class TestElectronicsModels(unittest.TestCase):
    def test_exact_si(self):
        self.assertEqual(Q,1.602176634e-19)
        self.assertEqual(K_B,1.380649e-23)
        self.assertGreater(thermal_voltage(300),.025)
        self.assertLess(thermal_voltage(300),.027)
    def test_mass_action_neutrality(self):
        for d in [-1e24,-1e21,-1e18,0,1e18,1e21,1e24]:
            n,p=mass_action_carriers(d,1e16)
            self.assertAlmostEqual(n*p/(1e16**2),1.,places=11)
            self.assertAlmostEqual((n-p)/max(abs(d),1),d/max(abs(d),1),places=11)
    def test_majority_minority_symmetry(self):
        a=mass_action_carriers(1e21,1e16);b=mass_action_carriers(-1e21,1e16)
        self.assertAlmostEqual(a[0],b[1]);self.assertAlmostEqual(a[1],b[0])
    def test_junction(self):
        v=built_in_potential(1e22,1e22,1e16,300)
        self.assertTrue(.6<v<.8)
        w=depletion_width(1e22,1e22,1e16,11.7,300)
        self.assertTrue(0<w<1e-4)
        self.assertGreater(depletion_width(1e22,1e22,1e16,11.7,300,-.1),w)
    def test_diode_inverse(self):
        for v in [-.1,-.01,-1e-9,0,1e-9,.01,.1]:
            i=diode_current(1e-12,v,300)
            self.assertAlmostEqual(diode_voltage_from_current(1e-12,i,300),v,delta=1e-8)
        self.assertEqual(diode_current(1e-12,0.,300),0.)
    def test_depletion_limit(self):
        v=built_in_potential(1e22,1e22,1e16,300)
        with self.assertRaises(ValueError):depletion_width(1e22,1e22,1e16,11.7,300,v)
    def test_mos_capacitance(self):
        c=mos_gate_capacitance(3.9,1e-12,1e-8)
        self.assertAlmostEqual(c,EPSILON_0_APPROX*3.9*1e-4)
    def test_mos_regions_continuity(self):
        k=1e-4; vov=1.
        a=ideal_nmos_current(k,2.,vov,1.)
        b=ideal_nmos_current(k,2.,vov+1e-10,1.)
        self.assertAlmostEqual(a,b,delta=1e-12)
        self.assertAlmostEqual(a,.5*k)
        self.assertEqual(ideal_nmos_current(k,.2,1.,1.),0.)
        for vds in [0.,.2,.4,.7,.9,1.,1.5,2.]:
            self.assertGreaterEqual(ideal_nmos_current(k,2.,vds,1.),0.)
    def test_rc_response(self):
        R,C=1e3,1e-9
        self.assertEqual(rc_step(0,1,R,C,0),0)
        self.assertAlmostEqual(rc_step(0,1,R,C,R*C*math.log(2)),.5)
        self.assertLess(rc_step(0,1,R,C,10*R*C),1.)
    def test_switch_power(self):
        self.assertAlmostEqual(switch_dynamic_power(1e-12,1.,1e9,.5),.0005)
        self.assertEqual(switch_dynamic_power(1e-12,0,1e9,1),0)
    def test_discrete_balance(self):
        edges=[.2,.5,1.5,1.2];dx=.1
        d=current_divergence_1d(edges,dx)
        self.assertAlmostEqual(sum(d)*dx,edges[-1]-edges[0])
    def test_truth_tables(self):
        self.assertEqual([logic_not(x) for x in (0,1)],[1,0])
        self.assertEqual([logic_nand(a,b) for a in (0,1) for b in (0,1)],[1,1,1,0])
        self.assertEqual([logic_nor(a,b) for a in (0,1) for b in (0,1)],[1,0,0,0])
    def test_invalid(self):
        for fn,args in [(thermal_voltage,(0,)),(mass_action_carriers,(0.,0.)),
          (depletion_width,(1e22,1e22,1e16,11.7,0)),(diode_current,(1e-12,20,300)),
          (diode_voltage_from_current,(1e-12,-1e-12,300)),(mos_gate_capacitance,(1.,0,1e-9)),
          (ideal_nmos_current,(1.,1.,-1.,.5)),(rc_step,(0,1,0,1,1)),
          (switch_dynamic_power,(1.,1.,1.,1.2)),(current_divergence_1d,([1.],1.)),
          (logic_not,(3,))]:
            with self.assertRaises(ValueError):fn(*args)
if __name__=='__main__':unittest.main()
