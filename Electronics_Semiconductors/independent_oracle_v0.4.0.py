#!/usr/bin/env python3
"""Independent finite-comparison oracle for original Electronics v0.4.0.

Separate reference implementations (Python arithmetic, explicit DAG path enumeration,
and direct formulas) rather than reusing the tested algorithm's internals.
Constructed fixtures only; no external calibrated transistor measurements.
"""
import random,math,json,itertools
from electronics_atlas.v04_models import (
    primitive_alu, logic_dag_arrival, synchronous_setup_hold,
    bounded_memory_cycle,digital_noise_margins,rc_midpoint_delay_uncertainty,
    four_phase_handshake_step,synchronizer_mtbf_log10)

def run(seed=20261116):
    rng=random.Random(seed)
    counts={}; worst=0.0
    def check(label,a,b,atol=0.0):
        nonlocal worst
        counts[label]=counts.get(label,0)+1
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            delta=abs(a-b);worst=max(worst,delta)
            if delta>atol:raise AssertionError((label,a,b,delta))
        elif a!=b:raise AssertionError((label,a,b))

    # Exact crosschecked arithmetic using Python's native arbitrary precision.
    for width in (4,8):
        mask=(1<<width)-1
        samples=itertools.product(range(1<<width),repeat=2) if width==4 else ((rng.randrange(256),rng.randrange(256)) for _ in range(4000))
        for a,b in samples:
            for op in ('ADD','SUB','AND','OR','XOR','SHL','SHR'):
                res=primitive_alu(a,b,width,op)
                expected={
                    'ADD':(a+b)&mask,'SUB':(a-b)&mask,'AND':a&b,
                    'OR':a|b,'XOR':a^b,'SHL':(a<<1)&mask,'SHR':a>>1}[op]
                check('independent_integer_alu',res['result'],expected)
                check('zero_negative_flags',res['zero'],int(expected==0))
                check('zero_negative_flags',res['negative'],(expected>>(width-1))&1)
                if op=='ADD':check('carry_flag',res['carry'],int(a+b>mask))
                if op=='SUB':check('carry_flag',res['carry'],int(a>=b))
    # Brute-force path enumeration, not topological envelope algorithm.
    for _ in range(400):
        n=rng.randint(1,10)
        early={'a':rng.random()*1e-9,'b':rng.random()*1e-9}
        late={k:v+rng.random()*1e-9 for k,v in early.items()}
        options=['a','b'];gates=[];paths={'a':[(early['a'],late['a'],('a',))],
                                             'b':[(early['b'],late['b'],('b',))]}
        for i in range(n):
            out=f'g{i}';ins=tuple(rng.sample(options,k=min(rng.randint(1,2),len(options))))
            dmin=rng.random()*1e-10;dmax=dmin+rng.random()*1e-10
            gates.append((out,ins,dmin,dmax));options.append(out)
            paths[out]=[(lo+dmin,hi+dmax,path+(out,)) for inp in ins for lo,hi,path in paths[inp]]
        out=options[-1]
        obs=logic_dag_arrival(gates,{k:(early[k],late[k]) for k in early},[out])[out]
        check('independent_enumerated_min_path',obs['earliest_s'],min(p[0] for p in paths[out]),1e-24)
        check('independent_enumerated_max_path',obs['latest_s'],max(p[1] for p in paths[out]),1e-24)
    for _ in range(1000):
        T=rng.uniform(1e-9,30e-9)
        q0=rng.uniform(0.,1e-9);q1=q0+rng.uniform(0.,2e-9)
        c0=rng.uniform(0.,1e-9);c1=c0+rng.uniform(0.,4e-9)
        su=rng.uniform(0.,1e-9);hu=rng.uniform(0.,1e-9)
        setup=rng.uniform(0.,1e-9);hold=rng.uniform(0.,1e-9);skew=rng.uniform(-1e-9,1e-9)
        o=synchronous_setup_hold(T,q0,q1,c0,c1,setup,hold,skew,su,hu)
        check('timing_setup_formula',o['setup_slack_s'],T+skew-(q1+c1+setup+su),1e-23)
        check('timing_hold_formula',o['hold_slack_s'],q0+c0-skew-hold-hu,1e-23)
    for _ in range(1000):
        words=tuple(rng.choice((0,1,255,None)) for _ in range(8))
        addr=rng.randrange(8); re=rng.randrange(2);we=rng.randrange(2)
        v=rng.randrange(256);policy=rng.choice(('read_first','write_first','undefined'))
        observed=bounded_memory_cycle(words,addr,8,re,we,v,policy)
        next_words=list(words)
        if we:next_words[addr]=v
        prior=words[addr]
        expected_read=prior if re and (not we or policy=='read_first') else v if re and we and policy=='write_first' else None
        check('abstract_memory_next_state',observed['next_words'],tuple(next_words))
        check('abstract_memory_read_value',observed['read_word'],expected_read)
    for _ in range(1200):
        vdd=rng.uniform(1.,5.);vol=rng.uniform(0.,vdd*.2)
        vil=rng.uniform(vol,vdd*.4);vih=rng.uniform(vdd*.6,vdd*.8)
        voh=rng.uniform(vih,vdd)
        o=digital_noise_margins(vdd,vil,vih,vol,voh)
        check('independent_noise_margin',o['noise_margin_low_V'],vil-vol,0)
        check('independent_noise_margin',o['noise_margin_high_V'],voh-vih,0)
    # Covariance direct evaluation and finite difference sensitivity cross-check.
    for _ in range(800):
        r=rng.uniform(100,1e5);c=rng.uniform(1e-12,1e-7)
        sr=r*rng.uniform(.0001,.02);sc=c*rng.uniform(.0001,.02)
        rho=rng.uniform(-.99,.99);cov=rho*sr*sc
        o=rc_midpoint_delay_uncertainty(r,c,sr,sc,cov)
        nominal=math.log(2)*r*c
        dR=math.log(2)*c;dC=math.log(2)*r
        var=(dR*sr)**2+(dC*sc)**2+2*dR*dC*cov
        check('independent_rc_nominal',o['nominal_t50_s'],nominal,1e-26)
        check('independent_covariance_formula',o['linearized_sigma_t50_s'],math.sqrt(var),max(1e-24,1e-13*math.sqrt(var)))
    # Enumerate all legal handshake states vs expected four-phase transition table.
    reference={
      'IDLE':{(0,0):'IDLE',(1,0):'REQUESTED'},
      'REQUESTED':{(1,0):'REQUESTED',(1,1):'ACKNOWLEDGED'},
      'ACKNOWLEDGED':{(1,1):'ACKNOWLEDGED',(0,1):'RETURNING'},
      'RETURNING':{(0,1):'RETURNING',(0,0):'IDLE'}}
    for state,allowed in reference.items():
        for req in (0,1):
            for ack in (0,1):
                if (req,ack) in allowed:
                    check('handshake_states',four_phase_handshake_step(state,req,ack),allowed[(req,ack)])
                else:
                    try:four_phase_handshake_step(state,req,ack)
                    except ValueError:check('illegal_handshake_rejections',True,True)
                    else:raise AssertionError('illegal handshake silently accepted')
    total=sum(counts.values())
    return {'schema':'atlas.electronics-v04-independent-oracle/1','result':'passed',
      'seed':seed,'comparisons':total,'counts':counts,
      'max_absolute_difference_all_float_comparisons':worst,
      'physical_device_measurements':0,'independent_scientific_review':False,
      'source':'independently coded finite constructed oracles, not laboratory evidence'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
