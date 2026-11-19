#!/usr/bin/env python3
"""Independent finite checks for ATLAS offline Software Design Patterns reference.

Finite oracle calculations and constructed crash injections, not physically
measured power-loss resilience, formal proof, code security or peer review.
"""
import hashlib,json,random,tempfile
from pathlib import Path
from patterns_atlas.contracts import envelope,parse_envelope,canonical_bytes,digest
from patterns_atlas.state import recovery_machine
from patterns_atlas.resilience import CircuitBreaker,Bulkhead
from patterns_atlas.ledger import CommandJournal
from patterns_atlas.atomicfiles import ContentStore
from patterns_atlas.workflow import RecoveryWorkflow,SimulatedInterruption
from patterns_atlas.composition import PortAdapter

def run(seed=20261117):
    rng=random.Random(seed);counts={};sample=[]
    def check(name,condition):
        if not condition:raise AssertionError('independent oracle failed: '+name)
        counts[name]=counts.get(name,0)+1

    # JSON canonicalization against an independently ordered sorted-pairs
    # object (not an imported copy of the package's canonical_json routine).
    for i in range(2048):
        pairs=[('a',rng.randint(-100000,100000)),('b',rng.randint(0,10000)),('c',[rng.randint(0,100) for j in range(4)])]
        rng.shuffle(pairs);payload=dict(pairs)
        contract=envelope('sample',1,payload,'msg_'+str(i))
        reloaded=parse_envelope(canonical_bytes(contract))
        check('envelope_roundtrip',reloaded==contract)
        check('canonical_payload_sha',digest(payload)==hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()).hexdigest())
    # Finite transition reference independent of StateMachine internals.
    graph={('idle','prepare'):'prepared',('prepared','validate'):'verified',('prepared','reject'):'hold',
           ('verified','commit'):'committed',('verified','reject'):'hold',('hold','reset'):'idle',
           ('committed','reset'):'idle'}
    for n in range(1280):
        model=recovery_machine();expected='idle';events=[]
        for j in range(20):
            available=[(event,next_) for (state,event),next_ in graph.items() if state==expected]
            if not available:break
            event,next_=rng.choice(available)
            model.step(event);expected=next_;events.append(event)
            check('state_machine_reference',model.current==expected)
        check('transition_history',len(model.history)==len(events))
    # Independent deterministic breaker machine: same contract, separate
    # concise state equations, no host/network calls.
    for i in range(500):
        threshold=rng.randint(1,6);reset=rng.randint(1,12)
        uut=CircuitBreaker(threshold,reset);state='closed';failures=0;opened=-1;t=0
        for step in range(20):
            t+=rng.randint(0,3)
            if state=='open' and t-opened>=reset:state='half_open'
            permit=(state!='open')
            check('breaker_admission',uut.allow(t)==permit)
            if not permit:continue
            result=rng.random()>0.45
            uut.record(result,t)
            if result:state='closed';failures=0;opened=-1
            else:
                failures+=1
                if state=='half_open' or failures>=threshold:state='open';opened=t
            check('breaker_transition',uut.state==state)
    # Offline SQLite journal vs independently held mapping. Local DB only.
    with tempfile.TemporaryDirectory(prefix='atlas-pattern-oracle-') as tmp:
        path=Path(tmp)/'journal.db';shadow={}
        with CommandJournal(path) as journal:
            for i in range(450):
                k='id_'+str(rng.randint(0,160));payload={'a':rng.randint(-50,50),'b':rng.randint(-50,50)}
                if k in shadow:payload=shadow[k][0]
                result=journal.execute(k,payload,lambda p:{'sum':p['a']+p['b']})
                if k not in shadow:shadow[k]=(payload,{'sum':payload['a']+payload['b']});expect_new=True
                else:expect_new=False
                check('journal_idempotent_commit',result['new_commit']==expect_new)
                check('journal_result',result['result']==shadow[k][1])
            audit=journal.verify_replay()
            check('journal_replay_cardinality',audit['rows']==len(shadow))
        with CommandJournal(path) as restored:
            check('journal_restart_recovery',restored.verify_replay()['rows']==len(shadow))
        for i in range(128):
            content=hashlib.sha256(f'sample-{i}'.encode()).digest()*2
            store=ContentStore(Path(tmp)/'cas')
            d=store.put(content)
            check('sha256_blob_identity',d==hashlib.sha256(content).hexdigest())
            store.publish('latest',d)
            check('cas_head_identity',store.resolve('latest')['data']==content)
        # Exercise interruption between SQLite COMMIT and snapshot publish.
        with RecoveryWorkflow(Path(tmp)/'recovery') as w:
            w.apply('a',{'v':4},lambda p:{'value':p['v']})
            try:w.apply('b',{'v':5},lambda p:{'value':p['v']},interrupt_after_commit=True)
            except SimulatedInterruption:pass
            else:raise AssertionError('simulated interruption not raised')
        with RecoveryWorkflow(Path(tmp)/'recovery') as w:
            repaired=w.recover()
            check('reconstruct_snapshot_after_interruption',repaired['recovered'] and repaired['command_count']==2)
            check('restart_replay_hash_valid',w.journal.verify_replay()['rows']==2)

    for i in range(320):
        value=rng.uniform(-20,20)
        norm=PortAdapter('mV').normalize({'sensor':'lab','voltage':value*1000})
        check('adapter_unit_conversion',abs(norm['voltage_V']-value)<1e-12)

    return {'schema':'atlas.software-patterns-independent-oracle/1','status':'passed',
        'seed':seed,'compared_cases':sum(counts.values()),'checks_by_group':counts,
        'measurements':0,'hardware_power_loss_verified':False,
        'external_exactly_once_guarantee':False,'independent_expert_peer_review':False,
        'source_originals_authenticated':0,
        'limits':'Constructed, finite software reference comparisons, not power-loss equipment tests or formal verification'}

if __name__=='__main__':
    result=run()
    print(json.dumps(result,indent=2))
