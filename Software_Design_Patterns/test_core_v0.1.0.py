import unittest,math,json
from patterns_atlas.contracts import ContractError,canonical_bytes,digest,envelope,parse_envelope,migrate_payload
from patterns_atlas.state import Transition,StateMachine,TransitionError,recovery_machine
from patterns_atlas.resilience import CircuitBreaker,Bulkhead,bounded_retry,Rejected
from patterns_atlas.composition import StrategyRegistry,PortAdapter,build_adapter,Pipeline,audited

class TestContracts(unittest.TestCase):
    def test_digest_order_invariant(self):
        self.assertEqual(digest({'a':1,'b':2}),digest({'b':2,'a':1}))
    def test_envelope_roundtrip(self):
        x=envelope('command',1,{'a':2},'c001')
        self.assertEqual(parse_envelope(canonical_bytes(x)),x)
    def test_digest_detects_modified_payload(self):
        x=envelope('command',1,{'a':2},'c001');x['payload']['a']=3
        with self.assertRaises(ContractError):parse_envelope(canonical_bytes(x))
    def test_schema_rejects_unknown_field(self):
        x=envelope('command',1,{},'c001');x['extraneous']=2
        with self.assertRaises(ContractError):parse_envelope(canonical_bytes(x))
    def test_kind_refusal(self):
        x=envelope('event',1,{},'e001')
        with self.assertRaises(ContractError):parse_envelope(canonical_bytes(x),allowed_kinds={'command'})
    def test_bad_id_refusal(self):
        with self.assertRaises(ContractError):envelope('c',1,{},'../../unsafe')
    def test_bad_float_refusal(self):
        for v in (math.inf,-math.inf,math.nan):
            with self.assertRaises(ContractError):canonical_bytes({'v':v})
    def test_bad_bool_version(self):
        with self.assertRaises(ContractError):envelope('command',True,{},'c001')
    def test_unicode_key_rejected(self):
        with self.assertRaises(ContractError):envelope('command',1,{'❤':3},'c001')
    def test_depth_bounded(self):
        v=[]
        for _ in range(12):v=[v]
        with self.assertRaises(ContractError):canonical_bytes(v)
    def test_migrate_explicit(self):
        x=migrate_payload('sample',1,3,{'a':1},{('sample',1,2):lambda p:{**p,'b':2},('sample',2,3):lambda p:{**p,'c':3}})
        self.assertEqual(x,{'a':1,'b':2,'c':3})
    def test_missing_migration_refused(self):
        with self.assertRaises(ContractError):migrate_payload('sample',1,3,{}, {})
    def test_parse_bad_utf8(self):
        with self.assertRaises(ContractError):parse_envelope(b'\xff')
    def test_parse_nan_refused(self):
        with self.assertRaises(ContractError):parse_envelope(b'{"n":NaN}')

class TestState(unittest.TestCase):
    def test_recovery_path(self):
        m=recovery_machine();self.assertEqual([m.step(s) for s in ['prepare','validate','commit']],['prepared','verified','committed'])
    def test_hold_recovery(self):
        m=recovery_machine();m.step('prepare');m.step('reject');m.step('reset');self.assertEqual(m.current,'idle')
    def test_invalid_transition_does_not_mutate(self):
        m=recovery_machine();snapshot=m.receipt()
        with self.assertRaises(TransitionError):m.step('commit')
        self.assertEqual(m.receipt(),snapshot)
    def test_duplicate_transition_rejected(self):
        with self.assertRaises(TransitionError):StateMachine(['a'], 'a',[Transition('a','tick','a')]*2)
    def test_undefined_state_rejected(self):
        with self.assertRaises(TransitionError):StateMachine(['a'], 'z',[])
    def test_deterministic_state_hash(self):
        a=recovery_machine();b=recovery_machine()
        for e in ('prepare','validate','commit'):
            a.step(e);b.step(e)
        self.assertEqual(a.receipt(),b.receipt())
    def test_reset_idempotence_not_assumed(self):
        m=recovery_machine();
        with self.assertRaises(TransitionError):m.step('reset')
    def test_invalid_type_event(self):
        with self.assertRaises(TransitionError):recovery_machine().step(True)

class TestResilience(unittest.TestCase):
    def test_breaker_starts_closed(self):self.assertTrue(CircuitBreaker().allow(0))
    def test_trip_after_threshold(self):
        c=CircuitBreaker(2,5);c.record(False,0);c.record(False,1)
        self.assertEqual(c.state,'open');self.assertFalse(c.allow(2))
    def test_half_open_probe(self):
        c=CircuitBreaker(1,3);c.record(False,0)
        self.assertTrue(c.allow(3));self.assertFalse(c.allow(3))
        c.record(True,3);self.assertEqual(c.state,'closed')
    def test_failed_probe_reopens(self):
        c=CircuitBreaker(1,3);c.record(False,0);c.allow(3);c.record(False,3)
        self.assertEqual(c.state,'open');self.assertFalse(c.allow(4))
    def test_open_record_refused(self):
        c=CircuitBreaker(1,3);c.record(False,0)
        with self.assertRaises(Rejected):c.record(True,1)
    def test_nonmonotone_clock_rejected(self):
        c=CircuitBreaker();c.allow(10)
        with self.assertRaises(ValueError):c.allow(9)
    def test_threshold_bool_rejected(self):
        with self.assertRaises(ValueError):CircuitBreaker(True,3)
    def test_retry_transient_succeeds(self):
        calls=[]
        def fn():
            calls.append(1)
            if len(calls)<3:raise OSError('offline retry')
            return 8
        self.assertEqual(bounded_retry(fn,3,lambda e:isinstance(e,OSError)),{'value':8,'attempts':3,'success':True})
    def test_retry_nonretryable_refused(self):
        with self.assertRaises(ValueError):bounded_retry(lambda: (_ for _ in ()).throw(ValueError()),5,lambda e:isinstance(e,OSError))
    def test_retry_budget_refused(self):
        with self.assertRaises(ValueError):bounded_retry(lambda:5,True,lambda e:True)
    def test_bulkhead_limits(self):
        b=Bulkhead({'a':1,'b':2});self.assertTrue(b.acquire('a'));self.assertFalse(b.acquire('a'))
        self.assertTrue(b.acquire('b'));self.assertEqual(b.snapshot()['allocated'],{'a':1,'b':1})
    def test_bulkhead_release(self):
        b=Bulkhead({'x':1});b.acquire('x');b.release('x');self.assertTrue(b.acquire('x'))
    def test_bulkhead_overrelease_refused(self):
        with self.assertRaises(ValueError):Bulkhead({'x':1}).release('x')
    def test_bulkhead_invalid_type(self):
        with self.assertRaises(ValueError):Bulkhead({'x':True})

class TestComposition(unittest.TestCase):
    def test_strategy_registry(self):
        r=StrategyRegistry();r.register('double',lambda x:x*2)
        self.assertEqual(r.execute('double',4),8)
    def test_strategy_duplicate_refused(self):
        r=StrategyRegistry();r.register('x',lambda x:x)
        with self.assertRaises(ValueError):r.register('x',lambda x:0)
    def test_strategy_missing_refused(self):
        with self.assertRaises(ValueError):StrategyRegistry().execute('missing',2)
    def test_adapter_units(self):
        x=build_adapter({'source_units':'mV'}).normalize({'sensor':'ref1','voltage':1234})
        self.assertAlmostEqual(x['voltage_V'],1.234)
    def test_adapter_bad_units_refused(self):
        with self.assertRaises(ValueError):PortAdapter('Celsius')
    def test_adapter_bad_sample_refused(self):
        with self.assertRaises(ValueError):PortAdapter('V').normalize({'sensor':'x','voltage':0,'extra':1})
    def test_pipeline(self):
        r=Pipeline([lambda x:{'v':x+1},lambda x:{'v':x['v']*3}]).run(2)
        self.assertEqual(r['result'],{'v':9});self.assertEqual(len(r['trace']),2)
    def test_pipeline_reject_empty(self):
        with self.assertRaises(ValueError):Pipeline([])
    def test_audited_decoration(self):
        events=[];f=audited(lambda x:{'out':x+1},events)
        self.assertEqual(f(9),{'out':10});self.assertEqual(len(events),1)
    def test_failed_action_not_pretend_recorded(self):
        events=[];f=audited(lambda x: (_ for _ in ()).throw(ValueError()),events)
        with self.assertRaises(ValueError):f(2)
        self.assertEqual(events,[])

if __name__=='__main__':unittest.main()
