import unittest,random,math
from control_atlas.multivariable import (two_by_two_observer_error_tube,two_sensor_consistency)
from control_atlas.methods import ControlInputError

class TwoSensorObserver(unittest.TestCase):
    def settings(self):
        return {'A':[[.9,.05],[0,.8]],'C':[[1,0],[0,1]],
         'L':[[.45,0],[.0,.40]],'initial_error_radii':[.4,.25],
         'process_error_radii':[.03,.05],'measurement_error_radii':[.1,.12],'steps':25}
    def test_bound(self):
        z=two_by_two_observer_error_tube(**self.settings())
        self.assertEqual(len(z['error_radii']),26)
        self.assertTrue(z['sufficient_row_sum_contraction'])
        self.assertEqual(len(z['conservative_stationary_infinity_norm_envelope']),2)
    def test_random_trajectories_contained(self):
        rng=random.Random(110712)
        p=self.settings();d=two_by_two_observer_error_tube(**p)
        F=d['F_observer_error_dynamics'];L=p['L'];E=p['initial_error_radii'];W=p['process_error_radii'];V=p['measurement_error_radii']
        for _ in range(400):
            e=[rng.uniform(-E[i],E[i]) for i in range(2)]
            for k in range(p['steps']):
                w=[rng.uniform(-W[i],W[i]) for i in range(2)]
                v=[rng.uniform(-V[i],V[i]) for i in range(2)]
                e=[sum(F[i][j]*e[j] for j in range(2))+w[i]-sum(L[i][j]*v[j] for j in range(2)) for i in range(2)]
                for i in range(2):self.assertLessEqual(abs(e[i]),d['error_radii'][k+1][i]+1e-10)
    def test_negative_bounds_refused(self):
        p=self.settings();p['process_error_radii'][0]=-1
        with self.assertRaises(ControlInputError):two_by_two_observer_error_tube(**p)
    def test_dimensions_refused(self):
        p=self.settings();p['L']=[[1,0]]
        with self.assertRaises(ControlInputError):two_by_two_observer_error_tube(**p)
    def test_sensor_consistency(self):
        r=two_sensor_consistency(estimate=[1,2],estimated_error_radii=[.1,.1],C=[[1,0],[0,1]],sensor_values=[1.02,2.05],measurement_error_radii=[.1,.1])
        self.assertTrue(r['compatible']);self.assertFalse(r['root_cause_identified'])
        r=two_sensor_consistency(estimate=[1,2],estimated_error_radii=[.1,.1],C=[[1,0],[0,1]],sensor_values=[10,2],measurement_error_radii=[.1,.1])
        self.assertFalse(r['compatible']);self.assertFalse(r['root_cause_identified'])
    def test_stable_F_but_interval_contraction_fails(self):
        # Magnitude-induced interval conservatism: rotations can be stable
        # despite |F| infinity norm >= 1 (sufficiency is not necessity).
        p=self.settings();p['A']=[[.3,.9],[-.9,.3]];p['L']=[[0,0],[0,0]]
        d=two_by_two_observer_error_tube(**p)
        self.assertFalse(d['sufficient_row_sum_contraction'])
        self.assertIsNone(d['conservative_stationary_infinity_norm_envelope'])
    def test_no_hardware_claim(self):
        r=two_by_two_observer_error_tube(**self.settings())
        self.assertTrue(any('physical safety' in x for x in r['limitations']))

if __name__=='__main__':unittest.main()
