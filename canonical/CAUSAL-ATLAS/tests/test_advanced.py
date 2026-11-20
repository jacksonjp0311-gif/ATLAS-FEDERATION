# Public derivative redaction: ucb_admissions_redistribution_unresolved
"""Input-bound release tests for new v1 reference methods. Scientific truth is NOT verified."""
from __future__ import annotations
import copy,json,unittest
from fractions import Fraction as F
from pathlib import Path
from causal_atlas.advanced import (longitudinal_gformula,staggered_group_time,mediation_interventional,
    cluster_interference,transport_strata,independent_binary_contrast,berkeley_admissions)
from causal_atlas.advanced_cases import CASES,advanced_casebook
from causal_atlas.models import ModelError

class AdvancedCausalMethods(unittest.TestCase):
    def test_all_cases(self):
        result=advanced_casebook()
        self.assertEqual(result['result'],'partial_public_derivative')
        self.assertEqual(len(result['cases']),7)
        self.assertFalse(result['causal_effects_claimed_from_real_data'])

    def test_longitudinal_exact(self):
        out=longitudinal_gformula(CASES['longitudinal'])
        self.assertEqual(out['contrast_a_minus_b'],'17/50')
        self.assertEqual(F(out['static_regime_risks']['00']),F(3,25))
        self.assertEqual(F(out['static_regime_risks']['11']),F(23,50))
        self.assertFalse(out['identification_verified'])
        for a in out['limitations']:self.assertTrue(a)
    def test_longitudinal_swap_regimes(self):
        x=copy.deepcopy(CASES['longitudinal']);x['compare']={'regime_a':[0,0],'regime_b':[1,1]}
        self.assertEqual(longitudinal_gformula(x)['contrast_a_minus_b'],'-17/50')
    def test_longitudinal_rejects(self):
        f=CASES['longitudinal']
        variations=[]
        x=copy.deepcopy(f);x['strata'][0]['q']='2';variations.append(x)
        x=copy.deepcopy(f);x['strata'][0]['p_l1_by_a0']['0']='-1/4';variations.append(x)
        x=copy.deepcopy(f);x['compare']['regime_a']=[True,1];variations.append(x)
        x=copy.deepcopy(f);x['strata'][0]['outcome_risks'].pop('101');variations.append(x)
        x=copy.deepcopy(f);x['strata'].append(copy.deepcopy(x['strata'][0]));variations.append(x)
        for x in variations:
            with self.subTest(x=x),self.assertRaises(ModelError):longitudinal_gformula(x)
    def test_staggered_expected_cohorts(self):
        o=staggered_group_time(CASES['staggered_did'])
        self.assertEqual(len(o['contrasts']),3)
        self.assertEqual([x['observed_difference_in_changes'] for x in o['contrasts']],['2','3','3'])
        self.assertEqual(o['contrasts'][0]['comparison_ids'],['never','late'])
        self.assertFalse(o['causal_identification_verified'])
    def test_staggered_never_control(self):
        x=copy.deepcopy(CASES['staggered_did']);x['control_policy']='never'
        self.assertEqual(len(staggered_group_time(x)['contrasts']),3)
        self.assertEqual(staggered_group_time(x)['contrasts'][0]['comparison_ids'],['never'])
    def test_staggered_no_valid_controls(self):
        x=copy.deepcopy(CASES['staggered_did']);x['groups']=[r for r in x['groups'] if r['id']!='never']
        o=staggered_group_time(x)
        self.assertTrue(o['unavailable']);self.assertEqual(len(o['contrasts']),1)
    def test_staggered_rejects(self):
        x=copy.deepcopy(CASES['staggered_did']);x['periods']=[0,2,1]
        with self.assertRaises(ModelError):staggered_group_time(x)
        x=copy.deepcopy(CASES['staggered_did']);x['groups'][0]['means'].pop('2')
        with self.assertRaises(ModelError):staggered_group_time(x)
        x=copy.deepcopy(CASES['staggered_did']);x['groups'][1]['weight']=0
        with self.assertRaises(ModelError):staggered_group_time(x)
    def test_mediation_decomposition(self):
        o=mediation_interventional(CASES['mediation'])
        self.assertEqual(o['contrast_total'],'6/25')
        self.assertEqual(o['interventional_direct_component'],'3/25')
        self.assertEqual(o['interventional_indirect_component'],'3/25')
        self.assertTrue(o['decomposition_exact'])
        self.assertFalse(o['identified_from_observational_data'])
    def test_mediation_different_models(self):
        x=copy.deepcopy(CASES['mediation']);x['mediator_prob']['1']=x['mediator_prob']['0']
        self.assertEqual(mediation_interventional(x)['interventional_indirect_component'],'0')
        x['outcome_risk']['10']='2'
        with self.assertRaises(ModelError):mediation_interventional(x)
    def test_interference(self):
        o=cluster_interference(CASES['interference'])
        self.assertEqual(o['direct_effect_focal0_neighbor0'],'3/10')
        self.assertEqual(o['spillover_focal0_own0'],'1/5')
        self.assertEqual(o['spillover_focal1_own0'],'1/5')
        self.assertFalse(o['no_interference_assumption_verified'])
    def test_interference_requires_full_potential_outcomes(self):
        x=copy.deepcopy(CASES['interference']);x['outcomes_by_assignment'].pop('11')
        with self.assertRaises(ModelError):cluster_interference(x)
    def test_transport(self):
        o=transport_strata(CASES['transport'])
        self.assertEqual(o['source_contrast'],'3/20')
        self.assertEqual(o['target_contrast'],'1/4')
        self.assertFalse(o['transport_assumptions_verified'])
    def test_transport_support_rejection(self):
        x=copy.deepcopy(CASES['transport']);x['strata'][0]['source_share']='0';x['strata'][1]['source_share']='1'
        with self.assertRaises(ModelError):transport_strata(x)
    def test_transport_normalization(self):
        x=copy.deepcopy(CASES['transport']);x['strata'][0]['target_share']='1'
        with self.assertRaises(ModelError):transport_strata(x)
    def test_binomial_approx(self):
        o=independent_binary_contrast(CASES['binomial_interval'])
        self.assertEqual(o['difference'],'3/20')
        self.assertLess(o['normal_interval'][0],.15)
        self.assertGreater(o['normal_interval'][1],.15)
        self.assertFalse(o['causal_identification_verified'])
    def test_binomial_guard(self):
        x=copy.deepcopy(CASES['binomial_interval']);x['group_0']['successes']=1
        with self.assertRaises(ModelError):independent_binary_contrast(x)
        x=copy.deepcopy(CASES['binomial_interval']);x['group_1']['total']=20
        with self.assertRaises(ModelError):independent_binary_contrast(x)
    def test_berkeley_reanalysis(self):
        self.skipTest('Historical UCBAdmissions numerical data and derived results are unavailable in this public derivative pending redistribution clearance.')
    def test_berkeley_rejects(self):
        self.skipTest('Historical UCBAdmissions numerical data and derived results are unavailable in this public derivative pending redistribution clearance.')
    def test_case_serialization(self):
        r=Path(__file__).parents[1]
        mapping={'longitudinal':'longitudinal','staggered_did':'staggered_did','mediation':'mediation',
                 'interference':'interference','transport':'transport','binomial_interval':'binomial_interval'}
        for key,fname in mapping.items():
            with self.subTest(key=key):self.assertEqual(json.loads((r/'examples'/f'{fname}.json').read_text()),CASES[key])
        # Historical dataset serialization is unavailable in this derivative.

if __name__=='__main__':unittest.main()
