import unittest,tempfile,sqlite3,os,json,hashlib
from pathlib import Path
from patterns_atlas.ledger import CommandJournal,JournalError
from patterns_atlas.atomicfiles import ContentStore,SnapshotError
from patterns_atlas.events import EventChain
from patterns_atlas.workflow import RecoveryWorkflow,SimulatedInterruption

class Paths(unittest.TestCase):
    def setUp(self):self._tmp=tempfile.TemporaryDirectory();self.p=Path(self._tmp.name)
    def tearDown(self):self._tmp.cleanup()

class TestLedger(Paths):
    def test_one_command(self):
        with CommandJournal(self.p/'cmd.sqlite') as j:
            o=j.execute('c1',{'x':2},lambda p:{'result':p['x']*4})
            self.assertEqual(o['result'],{'result':8});self.assertTrue(o['new_commit'])
            self.assertEqual(j.verify_replay()['rows'],1)
    def test_duplicate_command_no_double_reducer(self):
        counter=[]
        def fn(p):counter.append(1);return p
        with CommandJournal(self.p/'cmd.sqlite') as j:
            a=j.execute('c1',{'x':2},fn);b=j.execute('c1',{'x':2},fn)
            self.assertEqual(len(counter),1);self.assertFalse(b['new_commit']);self.assertEqual(a['entry_sha256'],b['entry_sha256'])
    def test_same_id_conflicting_data_refused(self):
        with CommandJournal(self.p/'cmd.sqlite') as j:
            j.execute('id',{'x':1},lambda p:p)
            with self.assertRaises(JournalError):j.execute('id',{'x':2},lambda p:p)
            self.assertEqual(j.verify_replay()['rows'],1)
    def test_restart_replays(self):
        with CommandJournal(self.p/'cmd.sqlite') as j:j.execute('id',{'x':1},lambda p:p)
        with CommandJournal(self.p/'cmd.sqlite') as j:self.assertEqual(j.verify_replay()['rows'],1)
    def test_reducer_exception_rolls_back(self):
        with CommandJournal(self.p/'cmd.sqlite') as j:
            with self.assertRaises(ArithmeticError):j.execute('bad',{},lambda p:(_ for _ in ()).throw(ArithmeticError()))
            self.assertEqual(j.verify_replay()['rows'],0)
    def test_corrupted_result_hash_refused(self):
        with CommandJournal(self.p/'cmd.sqlite') as j:
            j.execute('ok',{'x':3},lambda p:p)
            j.db.execute("UPDATE commands SET result_json=? WHERE command_id='ok'",('"changed"',))
            with self.assertRaises(JournalError):j.verify_replay()
    def test_corrupted_payload_refused(self):
        with CommandJournal(self.p/'cmd.sqlite') as j:
            j.execute('ok',{'x':3},lambda p:p)
            j.db.execute("UPDATE commands SET payload_json=? WHERE command_id='ok'",('{"x":4}',))
            with self.assertRaises(JournalError):j.verify_replay()
    def test_invalid_id_refused(self):
        with CommandJournal(self.p/'cmd.sqlite') as j:
            with self.assertRaises(JournalError):j.execute('../../evil',{},lambda p:p)
    def test_multi_command_head_sha(self):
        with CommandJournal(self.p/'cmd.sqlite') as j:
            a=j.execute('a',{},lambda p:{'n':0})
            b=j.execute('b',{},lambda p:{'n':1})
            self.assertEqual(b['sequence'],2);self.assertNotEqual(a['entry_sha256'],b['entry_sha256'])
            self.assertEqual(j.verify_replay()['head_sha256'],b['entry_sha256'])
    def test_nonfinite_payload_refused(self):
        with CommandJournal(self.p/'cmd.sqlite') as j:
            with self.assertRaises(ValueError):j.execute('x',{'v':float('nan')},lambda p:p)
    def test_reducer_external_side_effect_not_claimed(self):
        with CommandJournal(self.p/'cmd.sqlite') as j:
            j.execute('x',{'v':1},lambda p:p)
            self.assertFalse(j.verify_replay()['external_exactly_once_delivery_proven'])

class TestFiles(Paths):
    def test_put_get(self):
        s=ContentStore(self.p/'snap');d=s.put(b'hello');self.assertEqual(s.get(d),b'hello')
    def test_repeated_put_same_digest(self):
        s=ContentStore(self.p/'snap');self.assertEqual(s.put(b'abc'),s.put(b'abc'))
    def test_publish_and_resolve(self):
        s=ContentStore(self.p/'snap');h=s.put(b'abc');s.publish('latest',h)
        self.assertEqual(s.resolve('latest')['data'],b'abc')
    def test_prior_snapshot_remains(self):
        s=ContentStore(self.p/'snap');a=s.put(b'a');b=s.put(b'b');s.publish('latest',a);s.publish('latest',b)
        self.assertEqual(s.get(a),b'a');self.assertEqual(s.resolve('latest')['data'],b'b')
    def test_traversal_refused(self):
        s=ContentStore(self.p/'snap');h=s.put(b'a')
        with self.assertRaises(SnapshotError):s.publish('../oops',h)
    def test_bad_hash_refused(self):
        with self.assertRaises(SnapshotError):ContentStore(self.p/'snap').get('a')
    def test_corrupt_blob_detected(self):
        s=ContentStore(self.p/'snap');h=s.put(b'abc');(s.root/'blobs'/h).write_bytes(b'bad')
        with self.assertRaises(SnapshotError):s.get(h)
    def test_missing_pointer_refused(self):
        with self.assertRaises(SnapshotError):ContentStore(self.p/'snap').resolve('missing')
    def test_large_blob_refused(self):
        with self.assertRaises(SnapshotError):ContentStore(self.p/'snap').put(b'a'*1_048_577)
    def test_non_bytes_refused(self):
        with self.assertRaises(SnapshotError):ContentStore(self.p/'snap').put('text')
    def test_symlink_head_refused(self):
        s=ContentStore(self.p/'snap');h=s.put(b'data');(s.root/'heads'/'head').symlink_to(s.root/'blobs'/h)
        with self.assertRaises(SnapshotError):s.resolve('head')
    def test_same_data_hash(self):
        a=ContentStore(self.p/'a');b=ContentStore(self.p/'b')
        self.assertEqual(a.put(b'abc'),b.put(b'abc'))

class TestEvents(Paths):
    def test_empty_chain(self):
        self.assertEqual(EventChain(ContentStore(self.p/'snap')).replay()['events'],())
    def test_append_replay(self):
        e=EventChain(ContentStore(self.p/'snap'));e.append({'n':1});e.append({'n':2})
        self.assertEqual(e.replay()['events'],({'n':1},{'n':2}))
    def test_replay_after_restart(self):
        root=self.p/'snap';EventChain(ContentStore(root)).append({'id':1})
        self.assertEqual(EventChain(ContentStore(root)).replay()['events'],({'id':1},))
    def test_corrupt_head_not_silent_reset(self):
        store=ContentStore(self.p/'snap');e=EventChain(store);e.append({'n':1})
        (store.root/'heads'/'events').write_text('deadbeef')
        with self.assertRaises(SnapshotError):e.append({'n':2})
    def test_maximum_replay_budget(self):
        e=EventChain(ContentStore(self.p/'snap'))
        for n in range(5):e.append({'n':n})
        with self.assertRaises(SnapshotError):e.replay(3)
    def test_events_digest_deterministic(self):
        s1=EventChain(ContentStore(self.p/'a'));s2=EventChain(ContentStore(self.p/'b'))
        for s in (s1,s2):s.append({'n':2});s.append({'n':3})
        self.assertEqual(s1.replay()['head_sha256'],s2.replay()['head_sha256'])
    def test_bad_event_refused(self):
        with self.assertRaises(ValueError):EventChain(ContentStore(self.p/'snap')).append('hello')

class TestWorkflow(Paths):
    def test_normal_apply_and_snapshot(self):
        with RecoveryWorkflow(self.p/'recovery') as r:
            o=r.apply('id',{'a':5},lambda p:{'x':p['a']+1})
            self.assertEqual(o['command']['result'],{'x':6})
            self.assertFalse(r.recover()['recovered'])
    def test_interruption_then_recovery(self):
        root=self.p/'recovery'
        with RecoveryWorkflow(root) as r:
            r.apply('first',{},lambda p:{'v':1})
            with self.assertRaises(SimulatedInterruption):r.apply('second',{},lambda p:{'v':2},interrupt_after_commit=True)
        with RecoveryWorkflow(root) as r:
            q=r.recover();self.assertTrue(q['recovered']);self.assertEqual(q['command_count'],2)
            self.assertEqual(r.journal.verify_replay()['rows'],2)
    def test_recovered_second_time_no_change(self):
        with RecoveryWorkflow(self.p/'r') as r:
            r.apply('id',{},lambda p:{'ok':1});self.assertFalse(r.recover()['recovered'])
    def test_invalid_command_id(self):
        with RecoveryWorkflow(self.p/'r') as r:
            with self.assertRaises(JournalError):r.apply('/bad',{},lambda p:p)
    def test_hash_corruption_fails_closed(self):
        with RecoveryWorkflow(self.p/'r') as r:
            r.apply('id',{},lambda p:p)
            (r.store.root/'heads/current').write_text('corrupt')
            with self.assertRaises(SnapshotError):r.recover()

if __name__=='__main__':unittest.main()
