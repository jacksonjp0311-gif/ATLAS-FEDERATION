#!/usr/bin/env python3
"""Original finite Bioelectric numerical verification, independent arithmetic paths.

Verifies synthetic equations, not measured biology, diagnostic outcomes or
medical-device stimulus behavior. Distinct reference implementations avoid
importing DUT algorithms for expected results where possible.
"""
from __future__ import annotations
from pathlib import Path
import sys,math,random,hashlib,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from bioelectric_atlas import foundations,cable,hodgkin_huxley,instruments,excitability


def run(seed=20261117):
    r=random.Random(seed);counts={}
    def check(name,condition):
        if not condition:raise AssertionError('failed independent numerical case: '+name)
        counts[name]=counts.get(name,0)+1
    R=8.31446261815324;F=96485.332123310018
    # Evaluate 4,000 SI Nernst conditions against separately stated reference.
    for _ in range(4000):
        ci=10**r.uniform(-3,3);co=10**r.uniform(-3,3)
        temp=r.uniform(250,340);z=r.choice([-3,-2,-1,1,2,3])
        expected=R*temp/(z*F)*math.log(co/ci)
        observed=foundations.nernst_potential(z,ci,co,temp)
        check('independent_nernst_SI',math.isclose(expected,observed,rel_tol=2e-12,abs_tol=1e-12))
    # GHK single-permeable-ion limiting cases independently checked by Nernst.
    for _ in range(1000):
        c1=10**r.uniform(-2,2);c2=10**r.uniform(-2,2)
        temperature=r.uniform(270,330)
        for p in ('k','na','cl'):
            a={'k':(1,0,0),'na':(0,1,0),'cl':(0,0,1)}[p]
            if p=='k':obs=foundations.ghk_voltage(*a,c1,c2,10,100,2,80,temperature);ref=R*temperature/F*math.log(c2/c1)
            elif p=='na':obs=foundations.ghk_voltage(*a,120,7,c1,c2,2,80,temperature);ref=R*temperature/F*math.log(c2/c1)
            else:obs=foundations.ghk_voltage(*a,120,7,10,100,c1,c2,temperature);ref=-R*temperature/F*math.log(c2/c1)
            check('ghk_nernst_reduction',math.isclose(obs,ref,abs_tol=1e-12,rel_tol=2e-12))
    # Passive membrane closed form reference from independent RC equation.
    for _ in range(4000):
        v=r.uniform(-.2,.2);e=r.uniform(-.12,.12)
        C=10**r.uniform(-8,-5);g=10**r.uniform(-5,-2)
        dt=r.uniform(0,10)*C/g;I=r.uniform(-.00001,.00001)
        ref=e+I/g+(v-e-I/g)*math.exp(-dt*g/C)
        got=foundations.passive_membrane_voltage(v,e,C,g,dt,I)['voltage_volts']
        check('rc_analytic',math.isclose(ref,got,rel_tol=1e-12,abs_tol=1e-12))
    # Sealed cable: discrete diffusion conserves charge to rounding tolerance.
    for _ in range(3000):
        arr=[r.uniform(-1,1) for j in range(r.randrange(2,16))]
        ga=r.uniform(0,.6);C=r.uniform(.01,.2)
        dt=.1*C/max(.00001,2*ga)
        before=sum(arr)
        after=cable.cable_step(arr,dt,C,ga,0,0)
        check('sealed_cable_charge',math.isclose(sum(after),before,rel_tol=3e-12,abs_tol=3e-12))
    # Independent HH gate analytic behavior: compare initial derivative at tiny dt.
    for _ in range(3000):
        v=r.uniform(-90,40);rates=hodgkin_huxley.hh_rates(v)
        for name in ('m','n','h'):
            x=r.random();a,b=rates[name];dt=1e-5
            expected_increment=dt*(a*(1-x)-b*x)
            actual_increment=hodgkin_huxley.exact_gate_update(x,a,b,dt)-x
            check('hh_gate_local_derivative',abs(actual_increment-expected_increment)<4e-8)
    # Nonclinical FHN consistency under independent small time steps.
    for _ in range(3000):
        v=r.uniform(-1.5,1.5);w=r.uniform(-1,1);s=excitability.FHNState(v,w)
        f,g=excitability.fhn_derivative(s,0)
        dt=1e-5;t=excitability.fhn_rk4_step(s,dt,0)
        check('FHN_local_derivative',abs((t.v-v)-dt*f)<1e-8 and abs((t.w-w)-dt*g)<1e-8)
    # Electrode dummy circuit admittance vs independently algebraic expression.
    for _ in range(4000):
        rs=r.uniform(1,100);rt=r.uniform(100,100000);cd=10**r.uniform(-9,-4);f=r.uniform(0,10000)
        omega=2*math.pi*f
        # Parallel Rct + capacitor: numerator Rct, denominator 1+jωRC.
        Z=complex(rs,0)+rt/complex(1,omega*rt*cd)
        got=instruments.electrode_dummy_impedance(rs,rt,cd,f)
        check('dummy_electrode_Z',math.isclose(Z.real,got['real_ohm'],rel_tol=1e-12,abs_tol=1e-12) and math.isclose(Z.imag,got['imag_ohm'],rel_tol=1e-12,abs_tol=1e-12))
    # ADC independent nearest-code check, bounded quantization error, explicit rails.
    for _ in range(4000):
        bits=r.randint(2,16);v=r.random()*5
        got=instruments.adc_ideal_quantize(v,0,5,bits)
        check('ADC_midrange_error',abs(got['reconstructed_volts']-v)<=got['step_volts']*.5000001)
    # Deterministic independent digest replays across recorded synthetic noise.
    for _ in range(100):
        seed_i=r.randrange(2**32);a=instruments.deterministic_voltage_noise([0]*20,.001,seed_i)
        b=instruments.deterministic_voltage_noise([0]*20,.001,seed_i)
        check('synthetic_noise_determinism',a['sha256']==b['sha256'])
    return {'schema':'atlas.bioelectric-independent-numerical-oracle/1',
            'status':'passed','seed':seed,'comparisons':sum(counts.values()),'groups':counts,
            'laboratory_evidence':False,'human_medical_application':False,
            'external_scientific_review':False,
            'publisher_original_files_authenticated':0,
            'scope':'bounded idealized synthetic mathematical checks only'}

if __name__=='__main__':
    receipt=run()
    print(json.dumps(receipt,indent=2))
    if len(sys.argv)>1:
        p=Path(sys.argv[1]);p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(receipt,indent=2)+'\n')
