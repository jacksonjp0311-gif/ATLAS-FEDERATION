import copy,json,subprocess,sys,unittest
from fractions import Fraction as F
from causal_atlas.models import ModelError
from causal_atlas.quasi import *
from causal_atlas.quasi_cases import *

class WaldTests(unittest.TestCase):
    def args(self):return dict(y_z0='1/5',y_z1='7/20',d_z0='1/5',d_z1='7/10',minimum_first_stage=0,data_origin='operator_supplied')
    def test_ratio(self):self.assertEqual(wald_summary(**self.args())['ratio'],'3/10')
    def test_denominator_zero(self):self.assertIsNone(wald_summary(**dict(self.args(),d_z1='1/5'))['ratio'])
    def test_guard_inclusive(self):self.assertIsNone(wald_summary(**dict(self.args(),minimum_first_stage='1/2'))['ratio'])
    def test_guard_not_statistical(self):self.assertFalse(wald_summary(**self.args())['weak_instrument_test_performed'])
    def test_no_interval(self):self.assertIsNone(wald_summary(**self.args())['confidence_interval'])
    def test_no_causal_admission(self):self.assertFalse(wald_summary(**self.args())['causal_identification_verified'])
    def test_reverse_instrument_same_ratio(self):
        a=self.args();a['y_z0'],a['y_z1']=a['y_z1'],a['y_z0'];a['d_z0'],a['d_z1']=a['d_z1'],a['d_z0']
        self.assertEqual(wald_summary(**a)['ratio'],'3/10')
    def test_reverse_outcome_sign(self):self.assertEqual(wald_summary(**dict(self.args(),y_z0='-1/5',y_z1='-7/20'))['ratio'],'-3/10')
    def test_probability_rejection(self):
        for v in [-1,2,True,'nan','inf',None]:
            with self.subTest(v=v),self.assertRaises(ModelError):wald_summary(**dict(self.args(),d_z1=v))
    def test_unknown_origin(self):
        with self.assertRaises(ModelError):wald_summary(**dict(self.args(),data_origin='scientifically_verified'))
    def test_invalid_guards(self):
        for v in [-1,1,True,'nan']:
            with self.subTest(v=v),self.assertRaises(ModelError):wald_summary(**dict(self.args(),minimum_first_stage=v))
    def test_negative_sensitivity_orientation(self):
        out=exclusion_sensitivity(reduced_form='-1/5',first_stage='-1/2',direct_lower='-1/20',direct_upper=0,minimum_first_stage=0,data_origin='synthetic_constructed')
        self.assertEqual(out['effect_scenario_bounds'],['3/10','2/5'])
    def test_sensitivity_reversed_bounds(self):
        with self.assertRaises(ModelError):exclusion_sensitivity(reduced_form=1,first_stage=1,direct_lower=1,direct_upper=0,minimum_first_stage=0,data_origin='operator_supplied')
    def test_sensitivity_no_stage(self):
        out=exclusion_sensitivity(reduced_form=1,first_stage=0,direct_lower=0,direct_upper=1,minimum_first_stage=0,data_origin='operator_supplied');self.assertIsNone(out['effect_scenario_bounds'])

class IVPopulationTests(unittest.TestCase):
    def test_local_not_population(self):
        r=iv_population(encouragement_types());self.assertEqual(r['ratio'],'3/10');self.assertEqual(r['population_ate'],'7/50')
    def test_exact_decomposition(self):self.assertTrue(iv_population(encouragement_types())['decomposition']['equals_reduced_form'])
    def test_no_mutation(self):
        a=encouragement_types();b=copy.deepcopy(a);iv_population(a);self.assertEqual(a,b)
    def test_zero_mass_rejected(self):
        a=encouragement_types();a[0]['mass']=0
        with self.assertRaises(ModelError):iv_population(a)
    def test_mass_must_sum_one(self):
        a=encouragement_types();a[0]['mass']='31/100'
        with self.assertRaises(ModelError):iv_population(a)
    def test_no_boolean_uptake(self):
        a=encouragement_types();a[0]['d0']=False
        with self.assertRaises(ModelError):iv_population(a)
    def test_repeated_name(self):
        a=encouragement_types();a[0]['name']=a[1]['name']
        with self.assertRaises(ModelError):iv_population(a)
    def test_direct_effect_breaks_exclusion(self):
        a=encouragement_types();a[0]['direct_z']=1;self.assertFalse(iv_population(a)['exclusion_in_declared_model'])
    def test_no_compliers_no_ratio(self):
        a=[dict(name='never',mass=1,d0=0,d1=0,y0=0,y1=1,direct_z=0)]
        r=iv_population(a);self.assertIsNone(r['complier_effect']);self.assertIsNone(r['ratio'])
    def test_invalid_unknown_fields(self):
        a=encouragement_types();a[0]['extra']=1
        with self.assertRaises(ModelError):iv_population(a)
    def test_bad_values(self):
        for v in [None,[],[{}]*65]:
            with self.assertRaises(ModelError):iv_population(v)

class RDTests(unittest.TestCase):
    def args(self):return dict(cutoff=0,bandwidth=4,kernel='triangular',data_origin='synthetic_constructed')
    def fit(self,rows=None,**opts):return local_linear_jump(linear_rd_rows() if rows is None else rows,**dict(self.args(),**opts))
    def test_exact_affine_fit(self):self.assertEqual(self.fit()['jump'],'5')
    def test_uniform_kernel(self):self.assertEqual(self.fit(kernel='uniform')['jump'],'5')
    def test_unequal_slopes(self):
        r=self.fit();self.assertEqual(r['sides']['left']['slope_per_score_unit'],'2');self.assertEqual(r['sides']['right']['slope_per_score_unit'],'-1')
    def test_cutoff_on_right(self):self.assertEqual(self.fit()['sides']['right']['positive_weight_rows'],4)
    def test_equivalent_weights(self):
        r=self.fit();rows={r['id']:r for r in linear_rd_rows()}
        for s in r['sides'].values():
            self.assertEqual(sum(F(w['weight']) for w in s['intercept_equivalent_weights']),1)
            self.assertEqual(sum(F(w['weight'])*rows[w['id']]['x'] for w in s['intercept_equivalent_weights']),0)
            self.assertEqual(sum(F(w['weight'])*rows[w['id']]['y'] for w in s['intercept_equivalent_weights']),F(s['intercept_at_cutoff']))
    def test_negative_weights_not_clipped(self):self.assertGreater(self.fit()['sides']['left']['negative_equivalent_weights'],0)
    def test_no_inference(self):
        r=self.fit();self.assertIsNone(r['standard_error']);self.assertIsNone(r['confidence_interval']);self.assertFalse(r['causal_identification_verified'])
    def test_outcome_offset_invariance(self):
        rows=linear_rd_rows()
        for r in rows:r['y']+=100
        self.assertEqual(self.fit(rows)['jump'],'5')
    def test_outcome_rescale(self):
        rows=linear_rd_rows()
        for r in rows:r['y']*=-2
        self.assertEqual(self.fit(rows)['jump'],'-10')
    def test_score_shift_and_scale(self):
        rows=linear_rd_rows()
        for r in rows:r['x']=1000+20*r['x']
        self.assertEqual(self.fit(rows,cutoff=1000,bandwidth=80)['jump'],'5')
    def test_boundary_excluded(self):
        rows=linear_rd_rows()+[dict(id='boundary',x=4,y=999999)]
        for kernel in ('uniform','triangular'):
            r=self.fit(rows,kernel=kernel);self.assertEqual(r['excluded_row_ids'],['boundary']);self.assertEqual(r['jump'],'5')
    def test_no_mutation(self):
        rows=linear_rd_rows();old=copy.deepcopy(rows);self.fit(rows);self.assertEqual(rows,old)
    def test_unknown_fields(self):
        rows=linear_rd_rows();rows[0]['weight']=1
        with self.assertRaises(ModelError):self.fit(rows)
    def test_duplicate_ids(self):
        rows=linear_rd_rows();rows[0]['id']=rows[1]['id']
        with self.assertRaises(ModelError):self.fit(rows)
    def test_nonfinite_even_excluded(self):
        rows=linear_rd_rows()+[dict(id='bad',x=999,y='nan')]
        with self.assertRaises(ModelError):self.fit(rows)
    def test_invalid_parameters(self):
        for opts in [dict(bandwidth=0),dict(bandwidth=-1),dict(kernel='gaussian'),dict(cutoff=True),dict(data_origin='verified')]:
            with self.subTest(opts=opts),self.assertRaises(ModelError):self.fit(**opts)
    def test_no_left_rows(self):
        with self.assertRaises(ModelError):self.fit([r for r in linear_rd_rows() if r['x']>=0])
    def test_one_distinct_score_per_side(self):
        with self.assertRaises(ModelError):self.fit([dict(id=str(i),x=-1 if i<3 else 1,y=i) for i in range(6)])
    def test_only_two_rows_side(self):
        with self.assertRaises(ModelError):self.fit(linear_rd_rows()[1:])
    def test_size_refusal(self):
        with self.assertRaises(ModelError):self.fit([{}]*513)
    def test_grid_preserves_unsupported_windows(self):
        r=bandwidth_sensitivity(curved_rd_rows(),cutoff=0,bandwidths=['1/10',1],kernel='triangular',data_origin='synthetic_constructed')
        self.assertEqual(r['results'][0]['result'],'unsupported');self.assertEqual(r['results'][1]['result'],'computed');self.assertIsNone(r['selected_bandwidth'])
    def test_invalid_grid(self):
        for values in [[],[1,1],[0],list(range(1,14))]:
            with self.assertRaises(ModelError):bandwidth_sensitivity(curved_rd_rows(),cutoff=0,bandwidths=values,kernel='uniform',data_origin='synthetic_constructed')
    def test_fuzzy(self):
        r=fuzzy_local_ratio(fuzzy_rd_rows(),**self.args(),minimum_first_stage=0)
        self.assertEqual(r['ratio'],'3');self.assertEqual(r['first_stage'],'1/2')
    def test_fuzzy_zero_denominator(self):
        r=fuzzy_local_ratio(fuzzy_rd_rows(equal_uptake=True),**self.args(),minimum_first_stage=0);self.assertIsNone(r['ratio'])
    def test_fuzzy_nonbinary_treatment(self):
        rows=fuzzy_rd_rows();rows[0]['d']=0.5
        with self.assertRaises(ModelError):fuzzy_local_ratio(rows,**self.args(),minimum_first_stage=0)
    def test_cases_pass_without_empirical_promotion(self):
        r=quasi_casebook();self.assertEqual(r['result'],'passed');self.assertEqual(len(r['cases']),12);self.assertFalse(r['actual_observations'])
    def test_cli_casebook(self):
        r=subprocess.run([sys.executable,'-m','causal_atlas','quasi-casebook'],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr);self.assertEqual(json.loads(r.stdout)['result'],'passed')

if __name__=='__main__':unittest.main()
