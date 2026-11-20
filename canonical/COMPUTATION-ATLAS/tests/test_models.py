import unittest,random,math,itertools
from fractions import Fraction
from collections import Counter
from computation_atlas.models import *
from computation_atlas.proofs import *
from computation_atlas.cases import casebook
class ComputabilityTests(unittest.TestCase):
 def test_halt(self):self.assertEqual(counter_machine([('halt',)])['status'],'halted')
 def test_budget_one_step(self):self.assertEqual(counter_machine([('inc',0,0)],step_budget=1)['registers'],(1,0))
 def test_budget_zero(self):self.assertEqual(counter_machine([('inc',0,0)],step_budget=0)['status'],'unknown_budget_exhausted')
 def test_branch_zero(self):self.assertEqual(counter_machine([('decjz',0,1,2),('inc',1,2),('halt',)],step_budget=4)['pc'],2)
 def test_branch_positive(self):self.assertEqual(counter_machine([('decjz',0,1,2),('halt',),('halt',)],initial=(3,0))['registers'][0],2)
 def test_reject_bad_register(self):
  with self.assertRaises(InvalidInput):counter_machine([('inc',2,0)])
 def test_reject_bad_target(self):
  with self.assertRaises(InvalidInput):counter_machine([('inc',0,90)])
 def test_unknown_not_nonhalting(self):self.assertNotEqual(counter_machine([('inc',0,0)],step_budget=10)['status'],'nonhalting')
 def test_no_arbitrary_python(self):
  with self.assertRaises(InvalidInput):counter_machine([('eval','anything')])
 def test_negative_counter(self):
  with self.assertRaises(InvalidInput):counter_machine([('halt',)],initial=(-1,0))
class AlgorithmTests(unittest.TestCase):
 def test_stable(self):self.assertEqual(stable_mergesort([('a',1),('b',1),('c',0)],key=lambda v:v[1]),[('c',0),('a',1),('b',1)])
 def test_random_sort(self):
  rng=random.Random(341)
  for _ in range(250):
   a=[rng.randint(-100,100) for _ in range(rng.randint(0,50))]
   self.assertEqual(stable_mergesort(a),sorted(a))
 def test_left_bound_random(self):
  rng=random.Random(123)
  for _ in range(150):
   a=sorted(rng.randint(-20,20) for _ in range(50));target=rng.randint(-22,22)
   idx=lower_bound(a,target);self.assertTrue(all(x<target for x in a[:idx]));self.assertTrue(all(x>=target for x in a[idx:]))
 def test_invalid_graph(self):
  with self.assertRaises(InvalidInput):dijkstra({'a':{'b':1}},'a')
 def test_negative_dijkstra_rejected(self):
  with self.assertRaises(InvalidInput):dijkstra({'a':{'b':-1},'b':{}},'a')
 def test_dijkstra_paths(self):
  g={'A':{'B':10,'C':1},'B':{},'C':{'B':2}}
  ans=dijkstra(g,'A');self.assertEqual(ans['distances']['B'],3);self.assertTrue(shortest_path_certificate(g,'A',ans))
 def test_unreachable(self):
  g={'a':{},'b':{}}
  self.assertEqual(dijkstra(g,'a')['distances']['b'],float('inf'))
  self.assertTrue(shortest_path_certificate(g,'a',dijkstra(g,'a')))
 def test_certificate_tamper(self):
  g={'A':{'B':1},'B':{}}
  ans=dijkstra(g,'A');ans['distances']['B']=0;self.assertFalse(shortest_path_certificate(g,'A',ans))
 def test_certificate_parent_cycle(self):
  g={'a':{'b':0},'b':{'c':0},'c':{'b':0}}
  p=dijkstra(g,'a');p['parents']['b']='c';p['parents']['c']='b'
  self.assertFalse(shortest_path_certificate(g,'a',p))
 def test_bellman_negative_cycle(self):self.assertEqual(bellman_ford({'a':{'b':-1},'b':{'a':0}},'a')['status'],'reachable_negative_cycle')
 def test_bellman_unreachable_cycle(self):self.assertEqual(bellman_ford({'a':{},'b':{'c':-2},'c':{'b':1}},'a')['status'],'finite_shortest_paths')
 def test_bellman_finite(self):self.assertEqual(bellman_ford({'a':{'b':-2},'b':{}} ,'a')['distances']['b'],-2)
 def test_topo(self):
  g={'a':['b','c'],'b':['c'],'c':[]};o=topological_order(g)
  self.assertLess(o.index('a'),o.index('b'));self.assertLess(o.index('b'),o.index('c'))
 def test_topo_cycle(self):
  with self.assertRaises(InvalidInput):topological_order({'a':['b'],'b':['a']})
 def test_edit(self):self.assertEqual(edit_distance('kitten','sitting'),3)
 def test_edit_triangle(self):
  for a,b,c in [('abc','ax','def'),('','a','abc'),('hello','hallo','hullo')]:self.assertLessEqual(edit_distance(a,c),edit_distance(a,b)+edit_distance(b,c))
 def test_edit_symmetry(self):self.assertEqual(edit_distance('abcd','abc'),edit_distance('abc','abcd'))
 def test_knapsack_zero(self):self.assertEqual(knapsack_01([0],[3],0)['value'],3)
 def test_knapsack_solution(self):
  r=knapsack_01([1,2,3],[10,12,17],3);self.assertEqual(r['value'],22)
 def test_knapsack_oracle_bruteforce(self):
  rng=random.Random(344)
  for _ in range(90):
   n=rng.randint(0,8);w=[rng.randint(0,8) for _ in range(n)];v=[rng.randint(-5,15) for _ in range(n)];cap=rng.randint(0,18)
   r=knapsack_01(w,v,cap); optimum=max((sum(v[i] for i in range(n) if mask>>i&1) for mask in range(1<<n) if sum(w[i] for i in range(n) if mask>>i&1)<=cap),default=0)
   self.assertEqual(r['value'],optimum)
 def test_knapsack_resource_refusal(self):
  with self.assertRaises(InvalidInput):knapsack_01([1]*2000,[1]*2000,5000)
 def test_egcd(self):
  for a,b in [(0,0),(0,5),(-34,20),(-34,-20),(14,35),(1,0)]:
   g,x,y=extended_gcd(a,b);self.assertEqual(a*x+b*y,g);self.assertEqual(g,math.gcd(a,b))
 def test_rational_interval(self):self.assertEqual(interval_mul((-1,2),(2,3)),(Fraction(-3),Fraction(6)))
 def test_interval_exact(self):
  rng=random.Random(999)
  for _ in range(100):
   a,b=sorted([rng.randint(-20,20),rng.randint(-20,20)]);c,d=sorted([rng.randint(-10,10),rng.randint(-10,10)])
   lo,hi=interval_mul((a,b),(c,d))
   for x in (a,b,(a+b)/2):
    for y in (c,d,(c+d)/2):self.assertLessEqual(float(lo)-1e-10,x*y);self.assertGreaterEqual(float(hi)+1e-10,x*y)
 def test_bisection(self):
  r=bisection(lambda x:x*x-2,1,2,continuous_confirmed=True,atol=1e-8)
  self.assertLessEqual(r['interval'][0],math.sqrt(2));self.assertGreaterEqual(r['interval'][1],math.sqrt(2))
 def test_bisection_noncontinuous_refusal(self):
  with self.assertRaises(InvalidInput):bisection(lambda x:-1 if x<0 else 1,-1,1)
 def test_bisection_same_sign(self):
  with self.assertRaises(InvalidInput):bisection(lambda x:x*x+1,-1,1,continuous_confirmed=True)
 def test_kahan_reasonable(self):self.assertAlmostEqual(kahan_sum([.1]*100),10.,places=10)
 def test_fsum_counterexample(self):
  nums=[1e16,1.,1.,-1e16];s=0.0
  for n in nums:s+=n
  self.assertEqual(s,0);self.assertEqual(math.fsum(nums),2)
 def test_entropy(self):self.assertAlmostEqual(shannon_entropy([1/4]*4),2)
 def test_entropy_invalid(self):
  with self.assertRaises(InvalidInput):shannon_entropy([.7,.7])
 def test_sort_certificate(self):self.assertTrue(sorted_permutation_certificate([2,3,2],[2,2,3]))
 def test_bad_certificate(self):self.assertFalse(sorted_permutation_certificate([1,2],[1,1]))
 def test_prefix(self):self.assertTrue(prefix_free(['0','100','101','11']))
 def test_prefix_collision(self):self.assertFalse(prefix_free(['0','01']))
 def test_casebook(self):self.assertGreaterEqual(casebook()['count'],16)
class VerificationTests(unittest.TestCase):
 def test_reachability_path(self):self.assertEqual(finite_reachability(0,{0:[1],1:[2],2:[]},lambda s:s==2)['path'],[0,1,2])
 def test_reachability_unreachable(self):self.assertEqual(finite_reachability(0,{0:[1],1:[]},lambda s:s==2)['status'],'not_reachable_in_declared_finite_graph')
 def test_reachability_budget_unknown(self):self.assertEqual(finite_reachability(0,{0:[1],1:[2],2:[]},lambda s:s==2,limit=1)['status'],'unknown_budget_exhausted')
 def test_reachability_invalid_edge(self):
  with self.assertRaises(InvalidInput):finite_reachability(0,{0:[99]},lambda s:False)
 def test_invariant_valid(self):
  r=inductive_invariant(range(4),0,lambda x:[min(x+1,3)],lambda x:0<=x<=3)
  self.assertEqual(r['status'],'inductive_in_declared_universe')
 def test_invariant_counterexample(self):self.assertEqual(inductive_invariant([0,1],0,lambda x:[1],lambda x:x==0)['status'],'counterexample_step')
 def test_invariant_missing_universe(self):
  with self.assertRaises(InvalidInput):inductive_invariant([0,1],0,lambda x:[2],lambda x:True)
 def test_ranking(self):
  r=witness_rank_decrease(range(5),lambda x:[x-1] if x>0 else [],lambda x:x,lambda x:x==0)
  self.assertEqual(r['status'],'ranking_certificate_for_declared_finite_system')
 def test_ranking_loop(self):self.assertEqual(witness_rank_decrease([0],lambda x:[0],lambda x:x,lambda x:False)['status'],'rank_not_decreasing')
 def test_amdahl(self):self.assertAlmostEqual(amdahl_speedup(.9,10),1/(.1+.09))
 def test_amdahl_overhead(self):self.assertLess(amdahl_speedup(.9,8,.1),amdahl_speedup(.9,8,0))
 def test_amdahl_invalid(self):
  with self.assertRaises(InvalidInput):amdahl_speedup(1.2,4)
 def test_wilson(self):self.assertAlmostEqual(wilson_interval(5,10)[0],.23659,places=4)
 def test_wilson_boundary(self):
  a,b=wilson_interval(0,10);self.assertEqual(a,0);self.assertGreater(b,0)
 def test_wilson_invalid(self):
  with self.assertRaises(InvalidInput):wilson_interval(0,0)
 def test_operations(self):self.assertEqual(estimate_operation_budget(2,2,3)['nodes'],15)
 def test_operations_caps(self):
  with self.assertRaises(InvalidInput):estimate_operation_budget(10,2,300)
