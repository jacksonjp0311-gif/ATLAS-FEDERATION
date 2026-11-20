from pathlib import Path
from decimal import Decimal, localcontext
from importlib.resources import files
import json,shutil,subprocess,sys,tempfile,unittest
from measurement_atlas.calibration import fit_polynomial
from measurement_atlas.published_case import load_case,reproduce,PINS

class CalibrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows,cls.meta,cls.handbook,cls.certified=load_case()
        cls.x=[r['load'] for r in cls.rows]; cls.y=[r['deflection'] for r in cls.rows]
        cls.fit=cls.make(cls.x,cls.y,2); cls.report=reproduce()
    @staticmethod
    def make(x,y,degree=1):
        return fit_polynomial(x,y,degree=degree,x_unit='stated x unit',y_unit='stated y unit')
    def test_40_source_readings(self):self.assertEqual(len(self.rows),40)
    def test_twenty_replicated_levels(self):self.assertEqual(self.fit.distinct_levels,20)
    def test_order_retained(self):self.assertEqual(self.x[:20],self.x[20:])
    def test_units_not_invented(self):self.assertIn('unspecified',self.meta['columns']['load']['unit'])
    def test_raw_bytes_not_claimed(self):self.assertFalse(self.meta['original_file_bytes_included']);self.assertIsNone(self.meta['original_upstream_file_sha256'])
    def test_independent_lab_not_claimed(self):self.assertFalse(self.report['independent_physical_replication'])
    def test_all_11_certified_values(self):self.assertEqual(len(self.report['certified_reference_checks']),11);self.assertTrue(self.report['certified_reference_passed'])
    def test_six_handbook_disagreements_retained(self):self.assertEqual(len(self.report['handbook_disagreements']),6);self.assertFalse(self.report['handbook_all_within_printed_rounding'])
    def test_thresholds_not_relaxed(self):self.assertEqual(self.handbook['quadratic']['residual_sd']['absolute_tolerance'],5e-11)
    def test_reproduction_status_honest(self):self.assertEqual(self.report['result'],'passed_with_source_discrepancies')
    def test_inverse_example_is_hypothetical(self):self.assertIn('hypothetical',self.report['illustrative_inverse']['data_kind'])
    def test_published_interval_not_claimed(self):self.assertFalse(self.report['published_interval_reproduced'])
    def test_capture_tamper_rejected(self):
        self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
    def test_exact_line(self):
        f=self.make([0,1,2,3],[2,5,8,11]);self.assertLess(abs(f.coefficients[0]-2),Decimal('1e-50'));self.assertLess(abs(f.coefficients[1]-3),Decimal('1e-50'))
    def test_exact_quadratic(self):
        f=self.make([0,1,2,3,4],[1,6,17,34,57],2)
        for a,b in zip(f.coefficients,[1,2,3]):self.assertLess(abs(a-b),Decimal('1e-50'))
    def test_reject_bad_degree(self):
        for d in [0,3,True,1.0,2.0,'1',None]:
            with self.subTest(d=d), self.assertRaises(ValueError):self.make([0,1,2,3],[1,2,3,4],d)
    def test_reject_nonfinite(self):
        for x in ['nan','inf','-inf',True, 'bad']:
            with self.subTest(x=x), self.assertRaises(ValueError):self.make([0,1,2,3],[1,2,3,x])
    def test_reject_length_mismatch(self):
        with self.assertRaises(ValueError):self.make([0,1,2,3],[1,2,3])
    def test_reject_insufficient_rows(self):
        with self.assertRaises(ValueError):self.make([0,1],[1,2])
    def test_reject_singular_design(self):
        with self.assertRaises(ValueError):self.make([1,1,1,1],[1,2,3,4])
    def test_reject_missing_units(self):
        with self.assertRaises(ValueError):fit_polynomial([0,1,2,3],[0,1,2,3],degree=1,x_unit='',y_unit='V')
    def test_no_replicates_is_unavailable(self):
        f=self.make([0,1,2,3],[1,2.1,2.9,4]);self.assertIsNone(f.lack_of_fit_F);self.assertEqual(f.as_dict()['lack_of_fit']['status'],'unavailable_no_replicates')
    def test_zero_pure_error_not_a_pass(self):
        f=self.make([0,0,1,1,2,2],[1,1,3,3,6,6]);self.assertIsNone(f.lack_of_fit_F);self.assertEqual(f.as_dict()['lack_of_fit']['status'],'undefined_zero_pure_error')
    def test_degrees_of_freedom(self):self.assertEqual((self.fit.residual_df,self.fit.pure_error_df,self.fit.lack_of_fit_df),(37,20,17))
    def test_partition_sum(self):self.assertLess(abs(self.fit.sse-self.fit.pure_error_ss-self.fit.lack_of_fit_ss),Decimal('1e-30'))
    def test_predict_new_observation_variance(self):
        m=self.fit.prediction_sd('1700000',new_observation=False);n=self.fit.prediction_sd('1700000',new_observation=True)
        self.assertLess(abs((n*n-m*m)-self.fit.residual_sd**2),Decimal('1e-30'))
    def test_future_response_requires_explicit_boolean(self):
        with self.assertRaises(ValueError):self.fit.prediction_sd(1700000,new_observation='yes')
    def test_prediction_outside_range(self):
        with self.assertRaises(ValueError):self.fit.predict(4000000)
    def test_inverse_outside_range(self):
        with self.assertRaises(ValueError):self.fit.invert(5)
    def test_inverse_recovers_load(self):
        y=self.fit.predict('1750000');self.assertLess(abs(self.fit.invert(y)-1750000),Decimal('1e-20'))
    def test_nonmonotonic_inverse_rejected(self):
        f=self.make([-2,-1,0,1,2],[4,1,0,1,4],2)
        with self.assertRaisesRegex(ValueError,'nonmonotone'):f.invert(1)
    def test_negative_slope_inverse(self):
        f=self.make([0,1,2,3],[7,5,3,1]);self.assertLess(abs(f.invert(4)-Decimal('1.5')),Decimal('1e-25'))
    def test_unit_rescaling(self):
        f=self.make([str(Decimal(x)/1000000) for x in self.x],self.y,2)
        with localcontext() as ctx:
            ctx.prec=60
            for i,(small,big) in enumerate(zip(self.fit.coefficients,f.coefficients)):
                self.assertLess(abs(small*Decimal(1000000)**i-big),Decimal('1e-30'))
    def test_residual_r_squared_not_enough(self):
        f=self.make(self.x,self.y,1);self.assertGreater(f.r_squared,Decimal('.999'));self.assertGreater(f.lack_of_fit_F,200)
    def test_cli_success_with_discrepancies(self):
        p=subprocess.run([sys.executable,'-m','measurement_atlas','published-case'],cwd=Path(__file__).resolve().parents[1],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr);self.assertEqual(json.loads(p.stdout)['result'],'passed_with_source_discrepancies')
