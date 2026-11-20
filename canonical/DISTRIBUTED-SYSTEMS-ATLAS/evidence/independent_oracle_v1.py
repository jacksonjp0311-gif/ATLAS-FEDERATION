"""Independent enumerators built separately from implementation; finite evidence only.

This file never imports atlas model_check or linearizability internals until comparison.
Reports exact finite question counts, negative controls, and size limitations.
"""
from itertools import combinations,permutations,product
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from distributed_atlas.linearizability import Op,history_witness
from distributed_atlas.model_check import check_agreement


def oracle_linear(ops,initial='0'):
    # Independent exhaustive permutation criterion. Strict real-time precedence.
    for order in permutations(ops):
        if any(a.end<=b.start and order.index(a)>order.index(b) for a,b in combinations(ops,2)):
            continue
        if any(b.end<=a.start and order.index(b)>order.index(a) for a,b in combinations(ops,2)):
            continue
        reg=initial
        legal=True
        for op in order:
            if op.kind=='write':reg=op.value
            elif op.result!=reg:legal=False;break
        if legal:return True
    return False

def check():
    count=0
    # All 3-op order/overlap profiles of two writes and a read, small finite alphabet.
    profiles=[(0,2),(1,3),(2,4),(3,5),(1,5)]
    for i,j,k in product(range(len(profiles)),repeat=3):
        for x,y,z in product(('0','1'),repeat=3):
            ops=(Op('w1','write',*profiles[i],value=x,result='ok'),
                 Op('w2','write',*profiles[j],value=y,result='ok'),
                 Op('r','read',*profiles[k],result=z))
            got=history_witness(ops) is not None
            want=oracle_linear(ops)
            if got!=want:raise AssertionError(('history mismatch',ops,got,want))
            count+=1
    safe=check_agreement()
    unsafe=check_agreement(unsafe=True)
    if not safe['safe'] or safe['exhausted'] is not True or unsafe['safe'] is not False:raise AssertionError('Paxos model-checker negative control failed')
    return {'schema':'atlas.distributed-independent-v1/1','finite_register_history_comparisons':count,
            'paxos_macro_states_explored':safe['states'],'unsafe_counterexample':unsafe['trace'],
            'result':'passed','publisher_authentication':False,'physical_power_loss_proven':False}
if __name__=='__main__':print(json.dumps(check(),sort_keys=True))
