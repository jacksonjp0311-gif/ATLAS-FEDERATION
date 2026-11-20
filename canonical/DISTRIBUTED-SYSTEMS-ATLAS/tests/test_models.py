import itertools,sqlite3,tempfile,unittest
from pathlib import Path
from distributed_atlas.clocks import LamportClock, VectorClock,precedes,concurrent
from distributed_atlas.quorums import majority_size,all_quorums,guaranteed_overlap,intersection_lower_bound,worst_case_crash_availability
from distributed_atlas.crdts import GCounter,ORSet
from distributed_atlas.paxos import Acceptor,propose,unsafe_ignore_prior
from distributed_atlas.transactions import Participant,coordinate
from distributed_atlas.journal import apply_once,extend_chain,verify_chain
class TestClocks(unittest.TestCase):
 def test_initial(self):self.assertEqual(LamportClock().value,0)
 def test_local(self):self.assertEqual(LamportClock().local(),1)
 def test_send_receive(self):
  a,b=LamportClock(),LamportClock(4);self.assertEqual(b.receive(a.send()),5)
 def test_recv_max(self):self.assertEqual(LamportClock(10).receive(2),11)
 def test_bad_timestamp(self):
  with self.assertRaises(ValueError):LamportClock().receive(-1)
 def test_reject_bool_stamp(self):
  with self.assertRaises(ValueError):LamportClock().receive(True)
 def test_vector_send_receive(self):
  a,b=VectorClock(('A','B'),'A'),VectorClock(('A','B'),'B')
  x=a.send(); y=b.receive(x)
  self.assertTrue(precedes(x,y))
 def test_vector_concurrent(self):
  a,b=VectorClock(('A','B'),'A'),VectorClock(('A','B'),'B')
  self.assertTrue(concurrent(a.local(),b.local()))
 def test_vector_equality_is_not_strict(self):self.assertFalse(precedes({'A':1},{'A':1}))
 def test_membership_reject(self):
  with self.assertRaises(ValueError):VectorClock(('A','A'),'A')
 def test_missing_vector_key_reject(self):
  with self.assertRaises(ValueError):VectorClock(('A','B'),'A').receive({'A':1})
class TestQuorums(unittest.TestCase):
 def test_majority_odd(self):self.assertEqual(majority_size(5),3)
 def test_majority_even(self):self.assertEqual(majority_size(4),3)
 def test_reject_zero(self):
  with self.assertRaises(ValueError):majority_size(0)
 def test_intersection(self):self.assertTrue(guaranteed_overlap(5,3,3))
 def test_disjoint(self):self.assertFalse(guaranteed_overlap(6,3,3))
 def test_bound(self):self.assertEqual(intersection_lower_bound(6,4,4),2)
 def test_availability(self):self.assertFalse(worst_case_crash_availability(5,3,3))
 def test_all_quorums_count(self):self.assertEqual(len(list(all_quorums(5,3))),10)
class TestCRDT(unittest.TestCase):
 def test_gcounter(self):
  a=GCounter();a.increment('a',4);self.assertEqual(a.value,4)
 def test_merge(self):
  a,b=GCounter({'a':2}),GCounter({'b':5});self.assertEqual(a.merge(b).value,7)
 def test_idempotence(self):
  a=GCounter({'a':3});self.assertEqual(a.merge(a).values,a.values)
 def test_commutative(self):
  a,b=GCounter({'a':2}),GCounter({'a':8});self.assertEqual(a.merge(b),b.merge(a))
 def test_negative_increment(self):
  with self.assertRaises(ValueError):GCounter().increment('a',-1)
 def test_orset_add_remove(self):
  s=ORSet();s.add('x','a:1');s.remove('x');self.assertNotIn('x',s.value)
 def test_orset_concurrent_add(self):
  a,b=ORSet(),ORSet();a.add('x','a:1');b.add('x','b:1');a.remove('x');self.assertIn('x',a.merge(b).value)
 def test_orset_merge_commute(self):
  a,b=ORSet(),ORSet();a.add('x','a:1');b.add('y','b:1');self.assertEqual(a.merge(b),b.merge(a))
 def test_orset_duplicate_dot(self):
  a=ORSet();a.add('x','a:1')
  with self.assertRaises(ValueError):a.add('y','a:1')
class TestPaxos(unittest.TestCase):
 def test_single_proposal(self):
  a=[Acceptor() for _ in range(3)];self.assertEqual(propose(a,1,'x')[0],'x')
 def test_second_ballot_adopts(self):
  a=[Acceptor() for _ in range(3)];propose(a,1,'x',reachable=[0,1]);self.assertEqual(propose(a,2,'y',reachable=[1,2])[0],'x')
 def test_loss_of_quorum(self):
  a=[Acceptor() for _ in range(5)];self.assertIsNone(propose(a,1,'x',reachable=[0,1])[0])
 def test_stale_ballot(self):
  a=[Acceptor() for _ in range(3)];propose(a,2,'x');self.assertIsNone(propose(a,1,'y')[0])
 def test_unsafe_negative_control(self):
  a=[Acceptor() for _ in range(3)];propose(a,1,'x');self.assertEqual(unsafe_ignore_prior(a,2,'y'),'y')
class TestTwoPhase(unittest.TestCase):
 def test_commit(self):self.assertEqual(coordinate([Participant('a'),Participant('b')],[True,True]),'COMMIT')
 def test_abort(self):self.assertEqual(coordinate([Participant('a'),Participant('b')],[True,False]),'ABORT')
 def test_blocked(self):
  a=Participant('a');self.assertEqual(coordinate([a],[True],False),'NO_DECISION');self.assertTrue(a.blocked)
 def test_cannot_commit_abort(self):
  a=Participant('a');a.prepare(False)
  with self.assertRaises(ValueError):a.decide(True)
class TestJournal(unittest.TestCase):
 def test_local_idempotence(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'x.db';self.assertEqual(apply_once(p,'k',3),3);self.assertEqual(apply_once(p,'k',3),3)
 def test_restart(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'x.db';apply_once(p,'one',7);self.assertEqual(apply_once(p,'two',2),9)
 def test_conflicting_replay(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'x.db';apply_once(p,'one',7)
   with self.assertRaises(ValueError):apply_once(p,'one',8)
 def test_chain(self):
  e=[{'a':1},{'b':2}];h1=extend_chain('0'*64,e[0]);h2=extend_chain(h1,e[1]);self.assertTrue(verify_chain(e,[h1,h2]))
 def test_tamper_detection(self):
  e=[{'a':1}];h=extend_chain('0'*64,e[0]);self.assertFalse(verify_chain([{'a':2}],[h]))
if __name__=='__main__':unittest.main()
