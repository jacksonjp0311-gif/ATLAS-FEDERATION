import math,unittest,itertools,random
from control_atlas.invariance import (robust_invariant_box_2x2,scalar_robust_interval,
                                     simulate_2x2_state_feedback,ControlInputError)
from control_atlas.invariance_cases import casebook

base={'A_intervals':[[(.3,.4),(-.03,.03)],[(-.02,.02),(.2,.3)]],
       'B_intervals':[(.8,.9),(.1,.2)],'state_feedback_K':[.1,.1],
       'state_radii':[1,1],'disturbance_radii':[.05,.05],
       'actuator_limit':.25,'full_state_available':True}
class TestInvariantModel(unittest.TestCase):
 def test_exact_box_corners(self):
  x=robust_invariant_box_2x2(**base)
  self.assertEqual(x['vertices_checked'],64)
  self.assertTrue(x['conditional_invariance_and_input_feasibility'])
  self.assertLess(x['max_successor_abs_bound'][0],1)
 def test_actuator_limit_veto(self):
  x=robust_invariant_box_2x2(**{**base,'actuator_limit':.1})
  self.assertTrue(x['state_box_invariant_for_every_assumed_model'])
  self.assertFalse(x['conditional_invariance_and_input_feasibility'])
  self.assertEqual(x['status'],'candidate_not_certified')
 def test_interval_independence_veto(self):
  with self.assertRaises(ControlInputError):robust_invariant_box_2x2(**{**base,'full_state_available':False})
 def test_invalid_parameters(self):
  for changes in ({'state_radii':[0,1]}, {'A_intervals':[[(.7,.5),(-.03,.03)],[(-.02,.02),(.2,.3)]]},
                  {'disturbance_radii':[-.1,.1]},{'actuator_limit':-1},
                  {'K':[float('nan'),.1]}):
   with self.subTest(changes=changes),self.assertRaises((ControlInputError,TypeError)):
    d={**base,**changes};robust_invariant_box_2x2(**d)
 def test_scalar_exact(self):
  v=scalar_robust_interval(closed_loop_gain=.7,state_radius=1,disturbance_radius=.2,input_gain=.2,input_limit=.3,state_feedback_exact=True)
  self.assertTrue(v['conditional_certificate']);self.assertAlmostEqual(v['worst_one_step_abs_state'],.9)
  b=scalar_robust_interval(closed_loop_gain=1.1,state_radius=1,disturbance_radius=.2,input_gain=.2,input_limit=.3,state_feedback_exact=True)
  self.assertFalse(b['conditional_certificate'])
 def test_scalar_reject_bias(self):
  with self.assertRaises(ControlInputError):scalar_robust_interval(closed_loop_gain=.4,state_radius=1,disturbance_radius=.2,input_gain=.1,input_limit=1,state_feedback_exact=False)
 def test_corner_exact_vs_state_corners(self):
  rng=random.Random(1391)
  for _ in range(100):
   a=[[(rng.uniform(-.7,-.1),rng.uniform(.2,.8)),(-.1,.1)],[(-.2,.1),(.1,.5)]]
   b=[(.4,.5),(.1,.2)];K=[rng.uniform(-.5,.5),rng.uniform(-.5,.5)];r=[1,2];w=[.02,.04]
   res=robust_invariant_box_2x2(A_intervals=a,B_intervals=b,state_feedback_K=K,state_radii=r,disturbance_radii=w,actuator_limit=3,full_state_available=True)
   all_worst=[0,0]
   for bits in itertools.product([0,1],repeat=6):
    arr=[a[0][0][bits[0]],a[0][1][bits[1]],a[1][0][bits[2]],a[1][1][bits[3]]]
    bv=[b[0][bits[4]],b[1][bits[5]]]
    for j in (0,1):
     for signs in itertools.product((-1,1),repeat=2):
      x=[signs[k]*r[k] for k in (0,1)]
      v=sum((arr[2*j+k]-bv[j]*K[k])*x[k] for k in (0,1))
      all_worst[j]=max(all_worst[j],abs(v)+w[j])
   for j in (0,1):self.assertAlmostEqual(res['max_successor_abs_bound'][j],all_worst[j],places=11)
 def test_bias_rollout(self):
  d=[[0,0]]*6
  clean=simulate_2x2_state_feedback(A=[[.5,0],[0,.6]],B=[.2,.1],K=[.4,.5],x0=[1,1],disturbances=d,input_limit=.5)
  bias=simulate_2x2_state_feedback(A=[[.5,0],[0,.6]],B=[.2,.1],K=[.4,.5],x0=[1,1],disturbances=d,input_limit=.5,measurement_biases=[[0,0]]*2+[[.4,-.2]]*4)
  self.assertNotEqual(clean['states'],bias['states'])
 def test_reject_future_data(self):
  with self.assertRaises(ControlInputError):simulate_2x2_state_feedback(A=[[.5,0],[0,.6]],B=[.2,.1],K=[.4,.5],x0=[1,1],disturbances=[[0,0]],measurement_biases=[[0,0],[1,1]],input_limit=.5)
 def test_casebook(self):self.assertEqual(casebook()['status'],'passed')
if __name__=='__main__':unittest.main()
