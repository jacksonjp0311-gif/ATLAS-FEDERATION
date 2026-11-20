"""Author-created arithmetic and adversarial cases; not evidence of live agents."""
import math,unittest,random
from agent_atlas.foundations_v1 import *
from agent_atlas.v1_cases import casebook_v1
class FoundationV1(unittest.TestCase):
 def test_cases(self):self.assertEqual(casebook_v1()['status'],'passed');self.assertEqual(casebook_v1()['count'],8)
 def test_belief(self):
  v=belief_update([.6,.4],[[.9,.1],[.3,.7]],[[.8,.2],[.1,.9]],0)
  self.assertAlmostEqual(sum(v['posterior']),1);self.assertAlmostEqual(v['posterior'][0],.528/.562)
 def test_prior_must_normalize(self):
  with self.assertRaises(ReferenceModelError):belief_update([.1,.1],[[1,0],[0,1]],[[1,0],[0,1]],0)
 def test_observation_belief_missing(self):
  with self.assertRaises(ReferenceModelError):belief_update([.5,.5],[[1,0],[0,1]],[[0,1],[0,1]],0)
 def test_no_boolean_probabilities(self):
  with self.assertRaises(ReferenceModelError):belief_update([True,0],[[1,0],[0,1]],[[1,0],[0,1]],0)
 def test_mdp_one_step(self):
  p=[[[1,0],[0,1]],[[1,0],[0,1]]]
  r=[[[0,0],[0,5]],[[0,0],[1,1]]]
  v=finite_horizon_mdp(p,r,[0,0],1,.9)
  self.assertAlmostEqual(v['start_values'][0],5);self.assertEqual(v['first_action'][0],1)
 def test_mdp_discount(self):
  r=finite_horizon_mdp([[[1]]],[[[0]]],[10],2,.5)
  self.assertAlmostEqual(r['start_values'][0],2.5)
 def test_mdp_bad_probability(self):
  with self.assertRaises(ReferenceModelError):finite_horizon_mdp([[[.5]]],[[[1]]],[0],2)
 def test_mdp_discount_reject(self):
  with self.assertRaises(ReferenceModelError):finite_horizon_mdp([[[1]]],[[[1]]],[0],2,1.1)
 def test_astar_bad_h(self):
  g={'S':{'A':1,'B':1},'A':{'G':1},'B':{'G':4},'G':{}}
  r=shortest_path_reference(g,'S','G',{'S':0,'A':100,'B':0,'G':0})
  self.assertEqual(r['heuristic_candidate']['cost'],5);self.assertEqual(r['dijkstra_witness']['cost'],2)
  self.assertFalse(r['heuristic_admissible_for_complete_graph'])
 def test_astar_zero_is_dijkstra(self):
  g={'a':{'b':1,'c':4},'b':{'c':1},'c':{}}
  r=shortest_path_reference(g,'a','c');self.assertEqual(r['dijkstra_witness']['cost'],2);self.assertTrue(r['candidate_matches_witness'])
 def test_astar_negative_reject(self):
  with self.assertRaises(ReferenceModelError):shortest_path_reference({'a':{'b':-1},'b':{}},'a','b')
 def test_astar_unknown_node_reject(self):
  with self.assertRaises(ReferenceModelError):shortest_path_reference({'a':{'b':1}},'a','a')
 def test_astar_unreachable(self):
  r=shortest_path_reference({'a':{},'b':{}},'a','b')
  self.assertIsNone(r['dijkstra_witness']['path']);self.assertTrue(r['candidate_matches_witness'])
 def test_importance(self):
  d=[{'logged_action':'X','target_action':'X','logging_probability':.5,'reward':1},
     {'logged_action':'Y','target_action':'X','logging_probability':.5,'reward':0}]
  v=offline_importance_value(d);self.assertEqual(v['ips_mean'],1);self.assertEqual(v['effective_sample_size'],1)
 def test_no_target_observed(self):
  with self.assertRaises(ReferenceModelError):offline_importance_value([{'logged_action':'Y','target_action':'X','logging_probability':.5,'reward':1}]*2)
 def test_importance_cap(self):
  with self.assertRaises(ReferenceModelError):offline_importance_value([{'logged_action':'X','target_action':'X','logging_probability':.001,'reward':1}]*2,max_weight=99)
 def test_bad_reward(self):
  with self.assertRaises(ReferenceModelError):offline_importance_value([{'logged_action':'X','target_action':'X','logging_probability':.5,'reward':100}]*2)
 def test_random_belief_sums(self):
  r=random.Random(1103)
  for j in range(200):
   a=r.random();b=r.random();c=r.random()
   p=belief_update([a,1-a],[[b,1-b],[c,1-c]],[[.2,.8],[.75,.25]],j%2)
   self.assertAlmostEqual(sum(p['posterior']),1,places=12)
 def test_dynamic_programming_backward(self):
  p=[[[1]]];r=[[[1]]]
  for h in range(1,10):
   v=finite_horizon_mdp(p,r,[0],h,1)
   self.assertEqual(v['start_values'][0],h)
 def test_a_star_random_dijkstra(self):
  rng=random.Random(999)
  for _ in range(80):
   n=5;nodes=[str(i) for i in range(n)]
   graph={s:{t:rng.randint(1,9) for t in nodes if t!=s and rng.random()<.5} for s in nodes}
   v=shortest_path_reference(graph,'0','4')
   self.assertTrue(v['candidate_matches_witness'])
if __name__=='__main__':unittest.main()
