"""Independent finite v0.3 comparisons, intentionally separate from reference kernels.

NumPy solves the RC nodal matrices independently; Python integer identities verify
Boolean outputs; direct parity syndrome and energy arithmetic check other outputs.
Numerical agreement is not a hardware experiment or expert peer review.
"""
import json,itertools,random,math
import numpy as np
from electronics_atlas.v03_models import (rc_nodal_backward_euler,charge_supply_energy,
    nand_full_adder,nand_ripple_add,hamming84_encode,hamming84_decode,register_path_timing)

def run():
    rng=random.Random(20261116)
    counts={'nodal_systems':0,'nodal_values':0,'arithmetic_truth':0,
            'hamming_clean':0,'hamming_single':0,'hamming_double':0,
            'timing_constraints':0,'energy_checks':0}
    max_diff=0.
    for case in range(350):
        n=rng.randrange(1,9); C=[rng.uniform(.02,3) for _ in range(n)];old=[rng.uniform(-3,3) for _ in range(n)]
        dt=rng.uniform(.01,.3);edges=[]
        for i in range(n):edges.append((i,-1,rng.uniform(.2,4)))
        for i in range(n):
            for j in range(i+1,n):
                if rng.random()<.25:edges.append((i,j,rng.uniform(.2,2)))
        fixed={0:1.25} if n>1 and case%3==0 else {}
        inj={i:rng.uniform(-1,1) for i in range(n) if i not in fixed}
        ours=rc_nodal_backward_euler(C,edges,old,fixed,inj,dt)
        G=np.zeros((n,n))
        for i,j,g in edges:
            G[i,i]+=g
            if j>=0:
                G[j,j]+=g;G[i,j]-=g;G[j,i]-=g
        unknown=[i for i in range(n) if i not in fixed]
        ref=[None]*n
        for i,value in fixed.items():ref[i]=value
        if unknown:
            mat=G[np.ix_(unknown,unknown)]+np.diag([C[i]/dt for i in unknown]);rhs=np.array([C[i]/dt*old[i]+inj.get(i,0)-sum(G[i,j]*ref[j] for j in fixed) for i in unknown])
            sol=np.linalg.solve(mat,rhs)
            for i,v in zip(unknown,sol):ref[i]=float(v)
        err=max(abs(a-b) for a,b in zip(ours['node_voltages_V'],ref))
        max_diff=max(max_diff,err)
        assert err<=3e-11,err
        assert ours['relative_kcl_residual']<1e-12
        counts['nodal_systems']+=1;counts['nodal_values']+=n
    for width in [1,2,3,4,5,6,7,8,12,16,24,32,64]:
        for case in range(500):
            a=rng.randrange(1<<width);b=rng.randrange(1<<width);cin=case%2
            s,c=nand_ripple_add(a,b,width,cin)
            truth=a+b+cin
            assert (s,c)==(truth%(1<<width),truth//(1<<width))
            counts['arithmetic_truth']+=1
    for a,b,c in itertools.product((0,1),repeat=3):
        s,carry=nand_full_adder(a,b,c)
        assert s+2*carry==a+b+c
        counts['arithmetic_truth']+=1
    for nibble in range(16):
        code=hamming84_encode(nibble)
        # independent direct Hamming parity constraints:
        bits=[(code>>i)&1 for i in range(8)]
        assert sum(bits)%2==0
        for p in (1,2,4):assert sum(bits[i-1] for i in range(1,8) if i&p)%2==0
        assert hamming84_decode(code)['data']==nibble
        counts['hamming_clean']+=1
        for i in range(8):
            r=hamming84_decode(code^(1<<i));assert r['data']==nibble and r['status']=='corrected_single'
            counts['hamming_single']+=1
        for i,j in itertools.combinations(range(8),2):
            r=hamming84_decode(code^(1<<i)^(1<<j))
            assert r['status']=='detected_double' and r['data'] is None
            counts['hamming_double']+=1
    for k in range(3000):
        skew=rng.uniform(-2,2)
        cqmin=rng.uniform(0,1);cqmax=cqmin+rng.uniform(0,2)
        cd=rng.uniform(0,2);pd=cd+rng.uniform(0,3)
        setup=rng.uniform(0,2);hold=rng.uniform(0,2);period=rng.uniform(.001,9)
        r=register_path_timing(period,cqmin,cqmax,cd,pd,setup,hold,skew)
        assert r['setup_pass']==(period+skew+1e-15>=cqmax+pd+setup)
        assert r['hold_pass']==(cqmin+cd+1e-15>=hold+skew)
        counts['timing_constraints']+=2
    for _ in range(1000):
        C=10**rng.uniform(-14,-9);V=rng.uniform(0,5);cycles=rng.randrange(1,1001);rising=rng.randrange(cycles+1);freq=rng.uniform(1e3,1e10)
        r=charge_supply_energy(C,V,rising,cycles,freq)
        expected=C*V**2*rising;assert math.isclose(expected,r['supply_energy_J'],rel_tol=2e-15)
        assert math.isclose(expected*freq/cycles,r['mean_dynamic_power_W'],rel_tol=2e-15)
        counts['energy_checks']+=2
    return {'schema':'atlas.electronics-v03-independent-numerical-oracle/1','status':'passed',
            'counts':counts,'total_comparisons':sum(counts.values()),
            'max_abs_rc_voltage_difference':max_diff,'numpy_version':np.__version__,
            'deterministic_seed':20261116,'physical_measurements':0,
            'authenticated_original_publisher_files':0,
            'independent_science_peer_review':False}

if __name__=='__main__':print(json.dumps(run(),indent=2))
