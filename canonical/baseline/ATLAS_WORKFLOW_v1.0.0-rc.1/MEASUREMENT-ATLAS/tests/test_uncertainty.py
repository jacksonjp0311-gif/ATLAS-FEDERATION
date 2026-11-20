import math, unittest
from measurement_atlas.uncertainty import type_a, combine_linear, expanded_uncertainty, compare_difference
class Tests(unittest.TestCase):
    def test_type_a(self):self.assertAlmostEqual(type_a([10,12,14])['standard_uncertainty_mean'],2/math.sqrt(3))
    def test_type_a_reject_one(self):
        with self.assertRaises(ValueError):type_a([1])
    def test_type_a_reject_nan(self):
        with self.assertRaises(ValueError):type_a([1,float('nan')])
    def test_uncorrelated(self):self.assertAlmostEqual(combine_linear([1,1],[[4,0],[0,9]])['combined_standard_uncertainty'],math.sqrt(13))
    def test_perfect_correlation(self):self.assertAlmostEqual(combine_linear([1,-1],[[1,1],[1,1]])['combined_standard_uncertainty'],0)
    def test_zero_covariance(self):self.assertEqual(combine_linear([1],[[0]])['variance'],0)
    def test_reject_bad_correlation(self):
        with self.assertRaises(ValueError):combine_linear([1,1],[[1,2],[2,1]])
    def test_reject_nonsymmetric(self):
        with self.assertRaises(ValueError):combine_linear([1,1],[[1,0],[1,1]])
    def test_reject_negative(self):
        with self.assertRaises(ValueError):combine_linear([1],[[-1]])
    def test_reject_dimension(self):
        with self.assertRaises(ValueError):combine_linear([1,1],[[1,0]])
    def test_non_linearized_no_auto(self):self.assertIn('first-order',combine_linear([1],[[1]])['model'])
    def test_expand(self):self.assertAlmostEqual(expanded_uncertainty(.5,2)['expanded_uncertainty'],1)
    def test_expand_reject_factor(self):
        with self.assertRaises(ValueError):expanded_uncertainty(1,0)
    def test_compare(self):self.assertAlmostEqual(compare_difference(2,1,1,1)['standard_uncertainty_difference'],math.sqrt(2))
    def test_compare_covariance(self):self.assertEqual(compare_difference(2,1,1,1,1)['standard_uncertainty_difference'],0)
if __name__=='__main__':unittest.main()
