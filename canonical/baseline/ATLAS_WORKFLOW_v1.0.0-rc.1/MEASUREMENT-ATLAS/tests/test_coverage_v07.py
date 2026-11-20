import math, json, unittest, subprocess, sys
from pathlib import Path
from decimal import Decimal
from measurement_atlas.coverage import coverage_factor,student_t_survival,effective_df,expanded_interval
from measurement_atlas.intervals import inverse_prediction_interval,regression_interval,reproduce_interval,ERROR_MODEL
from measurement_atlas.calibration import fit_polynomial
from measurement_atlas.published_case import load_case,reproduce

class CoverageTests(unittest.TestCase):
    def test_cauchy_exact(self):
        for p in [.5,.8,.9,.95,.99,.9999]:
            self.assertAlmostEqual(coverage_factor(p,1)/math.tan(math.pi*p/2),1,places=10)
    def test_nist_8df_95(self):self.assertAlmostEqual(coverage_factor(.95,8),2.3060041352,places=9)
    def test_nist_37df(self):self.assertAlmostEqual(coverage_factor(.95,37),2.0261924630,places=9)
    def test_normal_limit_explicit(self):self.assertAlmostEqual(coverage_factor(.95,'inf'),1.95996398454,places=10)
    def test_survival_symmetry(self):
        for df in [1,2,8,37,10000,'inf']:
            for t in [0,.5,2,8]:self.assertAlmostEqual(student_t_survival(t,df)+student_t_survival(-t,df),1,places=12)
    def test_quantile_roundtrip(self):
        for df in [1,2,2.5,8,37,194,10000]:
            for p in [.5,.8,.95,.99,.9999]:self.assertAlmostEqual(2*student_t_survival(coverage_factor(p,df),df),1-p,places=10)
    def test_finite_df_not_silently_normal(self):
        with self.assertRaises(ValueError):coverage_factor(.95,10001)
    def test_bad_df(self):
        for df in [True,False,0,-1,.5,'nan','-inf',None,'bad']:
            with self.subTest(df=df),self.assertRaises(ValueError):coverage_factor(.95,df)
    def test_bad_probability(self):
        for p in [True,.49,1,.99999,-1,'nan','inf',None]:
            with self.subTest(p=p),self.assertRaises(ValueError):coverage_factor(p,8)
    def test_bad_t(self):
        for x in [True,'nan','inf',None]:
            with self.assertRaises(ValueError):student_t_survival(x,8)
    @staticmethod
    def comp(name='a',u=1,c=1,df=10):return dict(name=name,standard_uncertainty=u,sensitivity=c,df=df)
    def test_ws_equal_components(self):
        r=effective_df([self.comp(),self.comp('b')],independent=True)
        self.assertEqual(Decimal(r['effective_df']),20);self.assertAlmostEqual(r['combined_standard_uncertainty'],math.sqrt(2))
    def test_ws_single_component(self):self.assertEqual(Decimal(effective_df([self.comp(df=8)],independent=True)['effective_df']),8)
    def test_ws_infinite_df_is_explicit(self):self.assertEqual(effective_df([self.comp(df='Infinity')],independent=True)['effective_df'],'infinity')
    def test_ws_no_type_b_default(self):
        r=self.comp();del r['df']
        with self.assertRaises(ValueError):effective_df([r],independent=True)
    def test_ws_correlation_refused(self):
        for flag in [False,None,1,'yes']:
            with self.assertRaises(ValueError):effective_df([self.comp()],independent=flag)
    def test_ws_small_scale(self):
        r=effective_df([self.comp(u=1e-150),self.comp('b',u=1e-150)],independent=True)
        self.assertAlmostEqual(float(r['effective_df']),20);self.assertGreater(r['combined_standard_uncertainty'],0)
    def test_ws_scaling(self):
        for scale in [1e-100,1,1e100]:self.assertAlmostEqual(float(effective_df([self.comp(u=scale),self.comp('b',u=scale)],independent=True)['effective_df']),20)
    def test_ws_negative_sensitivity(self):self.assertEqual(effective_df([self.comp(c=-2)],independent=True)['combined_standard_uncertainty'],2)
    def test_ws_zero_combined_invalid(self):
        with self.assertRaises(ValueError):effective_df([self.comp(u=0)],independent=True)
    def test_ws_duplicate_names_invalid(self):
        with self.assertRaises(ValueError):effective_df([self.comp(),self.comp()],independent=True)
    def test_ws_bad_values(self):
        for row in [self.comp(u=-1),self.comp(df=0),self.comp(df='nan'),self.comp(c=True),self.comp(u='inf')]:
            with self.assertRaises(ValueError):effective_df([row],independent=True)
    def test_expansion_names_model(self):
        r=expanded_interval(10,.1,probability=.95,df=8,unit='mm',model='normal_mean_iid')
        self.assertFalse(r['assumptions_checked']);self.assertEqual(r['status'],'conditional_model_interval');self.assertAlmostEqual(r['expanded_uncertainty'],.23060041352,places=9)
    def test_expansion_missing_model_rejected(self):
        with self.assertRaises(ValueError):expanded_interval(10,.1,probability=.95,df=8,unit='mm',model='anything')
    def test_expansion_zero_rejected(self):
        with self.assertRaises(ValueError):expanded_interval(10,0,probability=.95,df=8,unit='mm',model='normal_mean_iid')
    def test_expansion_missing_unit_rejected(self):
        with self.assertRaises(ValueError):expanded_interval(10,.1,probability=.95,df=8,unit='',model='normal_mean_iid')
    def test_json_is_finite(self):json.dumps(expanded_interval(0,.1,probability=.95,df='inf',unit='V',model='normal_mean_iid'),allow_nan=False)

class IntervalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rows,meta,_,_=load_case();cls.fit=fit_polynomial([r['load'] for r in rows],[r['deflection'] for r in rows],degree=2,x_unit='source load',y_unit='source deflection');cls.r=reproduce_interval()
    def test_endpoint_order(self):
        i=self.r['interval'];self.assertLess(Decimal(i['lower']),Decimal(i['estimate']));self.assertLess(Decimal(i['estimate']),Decimal(i['upper']))
    def test_old_discrepancies_preserved(self):self.assertEqual(len(reproduce()['handbook_disagreements']),6)
    def test_one_new_display_disagreement(self):
        checks=self.r['publisher_comparisons'];self.assertEqual([c['quantity'] for c in checks if not c['within_display_tolerance']],['upper']);self.assertFalse(self.r['all_targets_matched'])
    def test_targets_not_relaxed(self):self.assertTrue(all(c['absolute_tolerance']=='0.5' for c in self.r['publisher_comparisons']))
    def test_both_inverse_equations(self):
        i=self.r['interval'];k=Decimal(i['coverage_factor']);y=Decimal(i['response'])
        for side,sign in [('lower',1),('upper',-1)]:
            x=Decimal(i[side]);value=self.fit.predict(x)+sign*k*self.fit.prediction_sd(x,new_observation=True)
            self.assertLess(abs(value-y),Decimal('1e-20'))
    def test_uses_future_not_mean(self):
        a=regression_interval(self.fit,1700000,probability=.95,new_observation=True,error_model=ERROR_MODEL)
        b=regression_interval(self.fit,1700000,probability=.95,new_observation=False,error_model=ERROR_MODEL)
        self.assertGreater(Decimal(a['upper'])-Decimal(a['lower']),Decimal(b['upper'])-Decimal(b['lower']))
    def test_no_normality_inferred(self):
        with self.assertRaises(ValueError):inverse_prediction_interval(self.fit,1.2,probability=.95,error_model='unknown')
    def test_no_new_empirical_observation(self):self.assertIn('hypothetical',self.r['reading_origin']);self.assertFalse(self.r['independent_experiment'])
    def test_monotonicity_bound_positive(self):self.assertGreater(Decimal(self.r['interval']['monotonicity_sufficient_condition']['positive_margin']),0)
    def test_extrapolation_refused(self):
        with self.assertRaises(ValueError):inverse_prediction_interval(self.fit,4,probability=.95,error_model=ERROR_MODEL)
    def test_clipping_requires_permission(self):
        y=self.fit.predict(self.fit.x_min)
        with self.assertRaisesRegex(ValueError,'endpoint outside'):inverse_prediction_interval(self.fit,y,probability=.95,error_model=ERROR_MODEL)
    def test_clipping_declared(self):
        r=inverse_prediction_interval(self.fit,self.fit.predict(self.fit.x_min),probability=.95,error_model=ERROR_MODEL,allow_clipping=True)
        self.assertTrue(r['range_limited']);self.assertEqual(r['clipped_endpoints'],['lower'])
    def test_decreasing_model(self):
        f=fit_polynomial(range(6),[10.1,7.9,6.05,3.95,2.1,-.1],degree=1,x_unit='mm',y_unit='V')
        r=inverse_prediction_interval(f,5,probability=.95,error_model=ERROR_MODEL)
        self.assertLess(Decimal(r['lower']),Decimal(r['estimate']));self.assertLess(Decimal(r['estimate']),Decimal(r['upper']))
    def test_flat_and_nonmonotone_refused(self):
        f=fit_polynomial([-2,-1,0,1,2],[4.1,.9,.1,.9,4.1],degree=2,x_unit='m',y_unit='V')
        with self.assertRaises(ValueError):inverse_prediction_interval(f,1,probability=.95,error_model=ERROR_MODEL)
    def test_weak_band_slope_refused(self):
        f=fit_polynomial(range(6),[1,-1,1,-1,1,0],degree=1,x_unit='m',y_unit='V')
        with self.assertRaisesRegex(ValueError,'sufficient condition'):inverse_prediction_interval(f,f.predict(2.5),probability=.99,error_model=ERROR_MODEL)
    def test_unit_rescaling(self):
        self.skipTest('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')
    def test_zero_variance_rejected(self):
        f=fit_polynomial([0,1,2,3],[0,1,2,3],degree=1,x_unit='m',y_unit='V')
        with self.assertRaises(ValueError):inverse_prediction_interval(f,1.5,probability=.95,error_model=ERROR_MODEL)
    def test_success_does_not_claim_publisher_match(self):self.assertEqual(self.r['result'],'computed_with_publisher_discrepancies')
