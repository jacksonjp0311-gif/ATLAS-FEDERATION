import unittest
from measurement_atlas.uncertainty import combine_linear, expanded_uncertainty, type_a
from measurement_atlas.traceability import audit_chain

class ScaleInvarianceTests(unittest.TestCase):
    def test_small_invalid_correlation_rejected(self):
        with self.assertRaises(ValueError):combine_linear([1,-1],[[1e-12,2e-12],[2e-12,1e-12]])
    def test_tiny_negative_variance_rejected(self):
        with self.assertRaises(ValueError):combine_linear([1],[[-1e-25]])
    def test_small_valid_covariance(self):self.assertAlmostEqual(combine_linear([1,-1],[[1e-12,0],[0,1e-12]])['variance']/1e-12,2)
    def test_scaling_preserves_decision(self):
        for scale in [1e-120,1e-12,1,1e12,1e120]:
            with self.subTest(scale=scale):
                c=[[2*scale,.5*scale],[.5*scale,3*scale]]
                self.assertAlmostEqual(combine_linear([1,-1],c)['variance']/scale,4)
    def test_invalid_at_all_scales(self):
        for scale in [1e-120,1e-12,1,1e12,1e120]:
            with self.subTest(scale=scale):
                with self.assertRaises(ValueError):combine_linear([1,-1],[[scale,2*scale],[2*scale,scale]])
    def test_pairwise_valid_but_global_invalid(self):
        with self.assertRaises(ValueError):combine_linear([1,1,1],[[1,-.9,-.9],[-.9,1,-.9],[-.9,-.9,1]])
    def test_zero_variance_covariance_invalid(self):
        with self.assertRaises(ValueError):combine_linear([1,1],[[0,1e-25],[1e-25,1]])
    def test_singular_valid(self):self.assertEqual(combine_linear([1,-1],[[1e-12,1e-12],[1e-12,1e-12]])['variance'],0)
    def test_different_unit_scales(self):self.assertAlmostEqual(combine_linear([1e6,1e-6],[[1e-12,.5],[.5,1e12]])['variance'],3)
    def test_tiny_asymmetry_rejected(self):
        with self.assertRaises(ValueError):combine_linear([1,1],[[1e-20,1e-21],[2e-21,1e-20]])
    def test_expansion_overflow_rejected(self):
        with self.assertRaises(ValueError):expanded_uncertainty(1e308,10)
    def test_propagation_overflow_rejected(self):
        with self.assertRaises(ValueError):combine_linear([1e308],[[1e308]])
    def test_explicit_audit_date(self):
        nodes=[{'id':'m','kind':'measurement','description':'synthetic','source_url':'https://example.invalid','valid_through':'2020-01-01'},
               {'id':'r','kind':'reference_standard','description':'synthetic','source_url':'https://example.invalid','valid_through':None}]
        r=audit_chain(nodes,[{'child':'m','parent':'r'}],measurement_id='m',as_of='2019-01-01');self.assertFalse(r['expired_documentation']);self.assertEqual(r['as_of'],'2019-01-01')
    def test_explicit_audit_date_expiry(self):
        r=audit_chain([{'id':'r','kind':'reference_standard','description':'fixture','source_url':'https://example.invalid','valid_through':'2020-01-01'}],[],measurement_id='r',as_of='2021-01-01');self.assertEqual(r['expired_documentation'],['r'])
    def test_invalid_audit_date(self):
        with self.assertRaises(ValueError):audit_chain([],[],measurement_id='x',as_of='yesterday')

class OverflowTests(unittest.TestCase):
 def test_difference_overflow_rejected(self):
  from measurement_atlas.uncertainty import compare_difference
  with self.assertRaises(ValueError):compare_difference(1e308,-1e308,1,1)
 def test_huge_int_rejected(self):
  from measurement_atlas.uncertainty import expanded_uncertainty
  with self.assertRaises(ValueError):expanded_uncertainty(10**1000,2)
 def test_budget_huge_int_rejected(self):
  from measurement_atlas.budget import type_b
  with self.assertRaises(ValueError):type_b(10**1000,'uniform')
