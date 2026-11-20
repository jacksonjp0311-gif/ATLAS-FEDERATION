import copy,json,subprocess,sys,unittest
from fractions import Fraction as F
from causal_atlas.estimation import *
from causal_atlas.investigations import process_rows,process_strata,investigations

class EstimationTests(unittest.TestCase):
    def test_correct_constructed_estimates(self):
        r=supplied_estimates(process_rows(),nuisance_origin='synthetic_oracle')
        for k in ('outcome_regression','ipw_horvitz_thompson','ipw_hajek','aipw'):self.assertEqual(r['estimates'][k],'1/10')
    def test_unweighted_diff(self):self.assertEqual(supplied_estimates(process_rows(),nuisance_origin='synthetic_oracle')['estimates']['crude_difference'],'-13/50')
    def test_balanced_covariate(self):self.assertEqual(supplied_estimates(process_rows(),nuisance_origin='synthetic_oracle')['diagnostics']['declared_covariate_mean_difference_weighted'],'0')
    def test_conservative_labels(self):
        r=supplied_estimates(process_rows(),nuisance_origin='external_predictions');self.assertFalse(r['causal_identification_verified']);self.assertIsNone(r['confidence_interval'])
    def test_rows_unchanged(self):
        x=process_rows();y=copy.deepcopy(x);supplied_estimates(x,nuisance_origin='in_sample');self.assertEqual(x,y)
    def test_flip_treatment_sign(self):
        rows=process_rows();a=supplied_estimates(rows,nuisance_origin='synthetic_oracle')['estimates']
        for r in rows:r['a']=1-r['a'];r['e']=str(1-F(r['e']));r['m0'],r['m1']=r['m1'],r['m0']
        b=supplied_estimates(rows,nuisance_origin='synthetic_oracle')['estimates']
        for k in a:self.assertEqual(F(a[k]),-F(b[k]))
    def test_outcome_shift_invariance_aipw(self):
        x=process_rows();a=supplied_estimates(x,nuisance_origin='synthetic_oracle')['estimates']['aipw']
        for r in x:
            for k in ('y','m0','m1'):r[k]=str(F(r[k])+7)
        self.assertEqual(a,supplied_estimates(x,nuisance_origin='synthetic_oracle')['estimates']['aipw'])
    def test_no_clipping(self):
        x=process_rows()[:];x[0]['e']='999/1000'
        r=supplied_estimates(x,nuisance_origin='external_predictions');self.assertEqual(r['diagnostics']['arm_weights']['0']['max_weight'],'1000');self.assertFalse(r['diagnostics']['weights_clipped'])
    def test_no_inferred_origin(self):
        with self.assertRaises(ModelError):supplied_estimates(process_rows(),nuisance_origin='verified')
    def test_boolean_treatment(self):
        x=process_rows();x[0]['a']=False
        with self.assertRaises(ModelError):supplied_estimates(x,nuisance_origin='external_predictions')
    def test_duplicate_id(self):
        x=process_rows();x[0]['id']=x[1]['id']
        with self.assertRaises(ModelError):supplied_estimates(x,nuisance_origin='external_predictions')
    def test_unknown_fields(self):
        x=process_rows();x[0]['execute']='do not execute'
        with self.assertRaises(ModelError):supplied_estimates(x,nuisance_origin='external_predictions')
    def test_invalid_values(self):
        for v in [0,1,-1,'nan','inf',True,None]:
            with self.subTest(v=v):
                x=process_rows();x[0]['e']=v
                with self.assertRaises(ModelError):supplied_estimates(x,nuisance_origin='external_predictions')
    def test_single_arm(self):
        with self.assertRaises(ModelError):supplied_estimates([r for r in process_rows() if r['a']==1],nuisance_origin='known_design')
    def test_size_and_empty(self):
        for x in [[],{},[{}]*10001]:
            with self.assertRaises(ModelError):supplied_estimates(x,nuisance_origin='in_sample')
    def test_outcome_invalid(self):
        for v in [True,None,'1e999','nan',10**13]:
            x=process_rows();x[0]['y']=v
            with self.assertRaises(ModelError):supplied_estimates(x,nuisance_origin='external_predictions')
    def test_same_constant_outcome_aipw_zero(self):
        x=process_rows()
        for r in x:r.update(y=1,m0=1,m1=1,e='1/3')
        self.assertEqual(supplied_estimates(x,nuisance_origin='in_sample')['estimates']['aipw'],'0')
    def test_distinguish_ht_hajek(self):
        x=process_rows()
        for r in x:r['e']='1/3'
        r=supplied_estimates(x,nuisance_origin='in_sample')['estimates'];self.assertNotEqual(r['ipw_horvitz_thompson'],r['ipw_hajek'])

class PopulationTests(unittest.TestCase):
    def test_exact(self):self.assertEqual(population_comparison(process_strata())['aipw'],'1/10')
    def test_propensity_correct(self):
        x=process_strata()
        for r in x:r['m0']='1/3';r['m1']='1/4'
        self.assertEqual(population_comparison(x)['aipw_bias'],'0')
    def test_outcome_correct(self):
        x=process_strata()
        for r in x:r['g']='2/3'
        self.assertEqual(population_comparison(x)['aipw_bias'],'0')
    def test_both_wrong(self):
        x=process_strata()
        for r in x:r.update(g='1/2',m0='1/2',m1='3/5')
        self.assertEqual(population_comparison(x)['aipw_bias'],'-9/25')
    def test_total_mass(self):
        x=process_strata();x[0]['q']='3/4'
        with self.assertRaises(ModelError):population_comparison(x)
    def test_zero_mass(self):
        x=process_strata();x[0]['q']=0;x[1]['q']=1
        with self.assertRaises(ModelError):population_comparison(x)
    def test_duplicate_stratum(self):
        x=process_strata();x[0]['name']=x[1]['name']
        with self.assertRaises(ModelError):population_comparison(x)
    def test_true_support_zero(self):
        x=process_strata();x[0]['e']=0
        with self.assertRaises(ModelError):population_comparison(x)
    def test_invalid_mean(self):
        x=process_strata();x[0]['mu0']=2
        with self.assertRaises(ModelError):population_comparison(x)
    def test_no_mutation(self):
        x=process_strata();y=copy.deepcopy(x);population_comparison(x);self.assertEqual(x,y)

class BoundsTests(unittest.TestCase):
    def test_missing_bounds(self):self.assertEqual(binary_missing_bounds({'0':dict(total=100,observed=90,successes=54),'1':dict(total=100,observed=60,successes=48)})['difference_bounds'],['-4/25','17/50'])
    def test_none_observed(self):self.assertEqual(binary_missing_bounds({'0':dict(total=10,observed=0,successes=0),'1':dict(total=10,observed=0,successes=0)})['difference_bounds'],['-1','1'])
    def test_complete(self):self.assertEqual(binary_missing_bounds({'0':dict(total=10,observed=10,successes=5),'1':dict(total=10,observed=10,successes=8)})['difference_bounds'],['3/10','3/10'])
    def test_inconsistent(self):
        for d in [dict(total=0,observed=0,successes=0),dict(total=1,observed=2,successes=1),dict(total=10,observed=5,successes=6),dict(total=10,observed=True,successes=0)]:
            with self.assertRaises(ModelError):binary_missing_bounds({'0':d,'1':dict(total=10,observed=5,successes=2)})
    def test_unknown_fields(self):
        with self.assertRaises(ModelError):binary_missing_bounds({'0':{},'1':{},'2':{}})
    def test_did(self):self.assertEqual(two_period_contrast('.8','.9','.7','.75')['observed_two_period_contrast'],'1/20')
    def test_did_bias(self):self.assertEqual(two_period_contrast('.8','.9','.7','.75',untreated_trend_difference='.08')['effect_under_stated_trend_scenario'],'-3/100')
    def test_scenarios(self):
        x=investigations();self.assertEqual(x['result'],'passed');self.assertEqual(len(x['cases']),12)
    def test_cli_cases(self):
        r=subprocess.run([sys.executable,'-m','causal_atlas','investigations'],capture_output=True,text=True);self.assertEqual(r.returncode,0,r.stderr);self.assertEqual(len(json.loads(r.stdout)['cases']),12)

if __name__=='__main__':unittest.main()
