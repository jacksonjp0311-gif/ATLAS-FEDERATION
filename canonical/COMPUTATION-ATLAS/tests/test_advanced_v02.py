import unittest,random,math,itertools
from fractions import Fraction
from computation_atlas.advanced_v02 import *
class AdvancedV02(unittest.TestCase):
 def test_union_find(self):
  uf=DisjointSets(6);self.assertTrue(uf.union(0,1));self.assertFalse(uf.union(1,0));self.assertEqual(uf.components,5)
  uf.union(1,2);self.assertTrue(uf.same(0,2));self.assertFalse(uf.same(2,3))
 def test_bad_union(self):
  with self.assertRaises(ComputationError):DisjointSets(0)
 def test_kruskal(self):
  x=kruskal_forest(4,[(0,1,1),(0,2,5),(1,2,2),(2,3,1)]);self.assertEqual(x['total_cost'],4);self.assertEqual(x['components'],1)
 def test_disconnected_forest(self):
  r=kruskal_forest(5,[(0,1,-2),(3,4,0)]);self.assertEqual(r['components'],3);self.assertEqual(r['total_cost'],-2)
 def test_kruskal_multi(self):
  r=kruskal_forest(2,[(0,1,4),(0,1,2),(0,1,1)]);self.assertEqual(r['total_cost'],1)
 def test_bad_kruskal(self):
  with self.assertRaises(ComputationError):kruskal_forest(3,[(0,4,2)])
 def test_maxflow(self):
  e=[(0,1,3),(0,2,2),(1,2,1),(1,3,2),(2,3,4)]
  r=max_flow_min_cut(4,e,0,3);self.assertAlmostEqual(r['max_flow'],5);self.assertAlmostEqual(r['min_cut_capacity'],5)
 def test_maxflow_reverse(self):
  e=[(0,1,2),(1,2,1),(2,3,2),(0,2,1),(1,3,1)]
  r=max_flow_min_cut(4,e,0,3);self.assertEqual(r['max_flow'],3)
 def test_maxflow_parallel(self):
  r=max_flow_min_cut(2,[(0,1,2),(0,1,3)],0,1);self.assertEqual(r['max_flow'],5)
 def test_maxflow_empty(self):
  r=max_flow_min_cut(2,[],0,1);self.assertEqual(r['max_flow'],0);self.assertEqual(r['min_cut_capacity'],0)
 def test_maxflow_bad(self):
  with self.assertRaises(ComputationError):max_flow_min_cut(2,[(0,1,-1)],0,1)
 def test_gaussian(self):
  d=gaussian_solve_exact([[2,1],[1,-1]],[5,1]);self.assertEqual(d['solution'],['2','1']);self.assertTrue(d['exact_residual_zero'])
 def test_rational(self):
  x=gaussian_solve_exact([['1/10','0'],['0','3']],[1,2]);self.assertEqual(x['solution'],['10','2/3'])
 def test_gaussian_pivot(self):
  d=gaussian_solve_exact([[0,1],[1,0]],[3,4]);self.assertEqual(d['solution'],['4','3'])
 def test_singular(self):
  with self.assertRaises(ComputationError):gaussian_solve_exact([[1,2],[2,4]],[3,6])
 def test_fft_simple(self):
  a=fft_radix2([1,2,3,4]);b=fft_radix2(a,inverse=True)
  self.assertTrue(all(abs(v-x)<1e-12 for v,x in zip(b,[1,2,3,4])))
 def test_fft_delta(self):self.assertTrue(all(abs(x-1)<1e-12 for x in fft_radix2([1,0,0,0])))
 def test_fft_bad_length(self):
  with self.assertRaises(ComputationError):fft_radix2([1,2,3])
 def test_convolution(self):
  out=convolution_linear([1,2,3],[2,1]);self.assertEqual(len(out),4)
  self.assertTrue(all(abs(z-w)<1e-10 for z,w in zip(out,[2,5,8,3])))
 def test_fft_complex(self):
  vals=[complex(1,2),complex(-3,2),complex(1,-5),complex(3,1)]
  got=fft_radix2(fft_radix2(vals),inverse=True)
  self.assertTrue(all(abs(x-y)<1e-10 for x,y in zip(vals,got)))
 def test_hoeffding(self):
  r=hoeffding_interval([0,1]*50,.05);self.assertEqual(r['n'],100);self.assertTrue(r['clipped_interval'][0]<.5<r['clipped_interval'][1])
 def test_hoeffding_unknown(self):self.assertFalse(hoeffding_interval([1]*10)['coverage_verified_for_actual_data'])
 def test_hoeffding_bounds(self):
  with self.assertRaises(ComputationError):hoeffding_interval([.2,2])
 def test_clock_before(self):
  a=vector_clock_tick((0,0),0);b=vector_clock_merge((0,0),a,1);self.assertEqual(vector_clock_relation(a,b),'happened_before')
 def test_clock_concurrent(self):self.assertEqual(vector_clock_relation((1,0),(0,1)),'concurrent')
 def test_clock_equal(self):self.assertEqual(vector_clock_relation((1,1),(1,1)),'equal')
 def test_clock_invalid(self):
  with self.assertRaises(ComputationError):vector_clock_merge((1,0),(0,),1)
 def test_canonical(self):self.assertEqual(canonical_json_digest({'b':2,'a':1}),canonical_json_digest({'a':1,'b':2}))
 def test_canonical_nonfinite(self):
  with self.assertRaises(ComputationError):canonical_json_digest({'x':float('nan')})
 def test_random_exact_linear(self):
  rng=random.Random(2026)
  for _ in range(100):
   x=[rng.randint(-8,8) for j in range(3)];A=[[rng.randint(-4,4) for j in range(3)] for i in range(3)]
   rhs=[sum(a*b for a,b in zip(row,x)) for row in A]
   try:r=gaussian_solve_exact(A,rhs)
   except ComputationError:continue
   self.assertEqual([Fraction(z) for z in r['solution']],x)
 def test_monte_carlo_not_proof(self):
  r=hoeffding_interval([.5]*100);self.assertEqual(r['status'],'conditional_iid_bound_only')
 def test_no_causal_order_from_real_clock(self):self.assertEqual(vector_clock_relation((2,0),(1,1)),'concurrent')
if __name__=='__main__':unittest.main()
