"""Scoped v1 standard-library reference tests. No physical durability claim."""
import tempfile,unittest,itertools
from pathlib import Path
from distributed_atlas.model_check import State,step,check_agreement,transitions
from distributed_atlas.linearizability import Op,history_witness
from distributed_atlas.durable_acceptor import DurableAcceptor

class TestAgreement(unittest.TestCase):
    def test_exhaustive_three_acceptors(self):
        r=check_agreement();self.assertTrue(r['safe']);self.assertTrue(r['exhausted']);self.assertEqual(r['states'],740)
    def test_negative_control_exposes_conflict(self):
        r=check_agreement(unsafe=True);self.assertFalse(r['safe']);self.assertEqual(set(r['choices']),{'A','B'});self.assertEqual(len(r['trace']),4)
    def test_underprovision_is_unknown_not_pass(self):
        r=check_agreement(max_states=20);self.assertIsNone(r['safe']);self.assertFalse(r['exhausted'])
    def test_bad_configuration(self):
        with self.assertRaises(ValueError):check_agreement(n=4)
    def test_prepare_persists_ballot(self):
        s=State(((-1,-1,None),)*3);s=step(s,1,(0,1));self.assertEqual(s.acceptors[0][0],2)
    def test_preempted_accept(self):
        s=State(((-1,-1,None),)*3);s=step(s,0,(0,1));s=step(s,1,(0,1));s=step(s,0,(0,1));self.assertEqual(s.chosen,());self.assertEqual(s.acceptors[0][1],-1)
    def test_promise_inherits_value(self):
        s=State(((-1,-1,None),)*3)
        for p,ids in [(0,(0,1)),(0,(0,1)),(1,(1,2)),(1,(1,2))]:s=step(s,p,ids)
        self.assertEqual(s.chosen,('A','A'))
    def test_no_duplicate_accept_targets(self):
        with self.assertRaises(ValueError):step(State(((-1,-1,None),)*3),0,(0,0))
    def test_stable_state_unchanged_on_simulated_restart(self):
        s=State(((-1,-1,None),)*3);s=step(s,0,(0,1));copied=State(tuple(s.acceptors),s.phase,s.prepared,s.chosen);self.assertEqual(copied,s)
    def test_terminal_states_not_enumerated_twice(self):
        self.assertGreater(check_agreement()['terminal_states'],0)

class TestLinearizability(unittest.TestCase):
    def test_empty(self):self.assertEqual(history_witness([]),())
    def test_read_initial(self):self.assertEqual(history_witness([Op('r','read',1,2,result='0')]),('r',))
    def test_writes_then_read(self):
        ops=[Op('w','write',1,2,value='v',result='ok'),Op('r','read',3,4,result='v')]
        self.assertEqual(history_witness(ops),('w','r'))
    def test_stale_read_negative(self):
        ops=[Op('w','write',1,2,value='v',result='ok'),Op('r','read',3,4,result='0')]
        self.assertIsNone(history_witness(ops))
    def test_overlapping_read_can_linearize_before_write(self):
        ops=[Op('w','write',1,5,value='v',result='ok'),Op('r','read',2,3,result='0')]
        self.assertEqual(history_witness(ops),('r','w'))
    def test_read_of_unwritten_value_reject(self):
        self.assertIsNone(history_witness([Op('r','read',1,2,result='x')]))
    def test_completed_only(self):
        with self.assertRaises(ValueError):history_witness([Op('r','read',1,1,result='0')])
    def test_write_ack_required(self):
        with self.assertRaises(ValueError):history_witness([Op('w','write',1,2,value='v',result=None)])
    def test_limit(self):
        with self.assertRaises(ValueError):history_witness([Op(str(i),'read',2*i,2*i+1,result='0') for i in range(10)])
    def test_duplicate_ids(self):
        with self.assertRaises(ValueError):history_witness([Op('r','read',1,2,result='0'),Op('r','read',3,4,result='0')])

class TestDurableAcceptor(unittest.TestCase):
    def test_promise_survives_restart(self):
        with tempfile.TemporaryDirectory() as t:
            path=Path(t)/'a.db';a=DurableAcceptor(path)
            self.assertEqual(a.promise(3),(-1,None));self.assertEqual(DurableAcceptor(path).read(),(3,-1,None));self.assertIsNone(DurableAcceptor(path).promise(2))
    def test_accepted_value_survives_reopen(self):
        with tempfile.TemporaryDirectory() as t:
            path=Path(t)/'a.db';a=DurableAcceptor(path)
            self.assertTrue(a.accept(1,'A'));self.assertEqual(DurableAcceptor(path).promise(2),(1,'A'))
    def test_stale_write_blocked(self):
        with tempfile.TemporaryDirectory() as t:
            a=DurableAcceptor(Path(t)/'a.db');a.promise(9);self.assertFalse(a.accept(8,'bad'));self.assertEqual(a.read(),(9,-1,None))
    def test_conflicting_same_ballot_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            a=DurableAcceptor(Path(t)/'a.db');a.accept(1,'A')
            with self.assertRaises(ValueError):a.accept(1,'B')
            self.assertEqual(a.read()[2],'A')
    def test_bad_ballot(self):
        with tempfile.TemporaryDirectory() as t:
            a=DurableAcceptor(Path(t)/'a.db')
            for ballot in (-1,True,'5'):
                with self.assertRaises(ValueError):a.promise(ballot)

if __name__=='__main__':unittest.main()
