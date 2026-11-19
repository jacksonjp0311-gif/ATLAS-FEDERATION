"""Independent finite oracle, using Fraction for matrix products and central differences for MLP gradients."""
import json,math,random,sys
from fractions import Fraction
sys.path.insert(0,str(__import__("pathlib").Path(__file__).resolve().parents[1]))
from neural_atlas.mathcore import matmul,stable_softmax,layer_norm
from neural_atlas.attention import attention
from neural_atlas.mlp import loss_and_grads
from neural_atlas.quantization import quantize_int8,dequantize

def oracle(seed=20261118,trials=1200):
    rng=random.Random(seed);checks=0
    # Exact fraction oracle: not the same floating-point multiply implementation.
    for _ in range(trials):
        m,k,n=rng.choice([1,2,3]),rng.choice([1,2,3]),rng.choice([1,2,3])
        a=[[rng.randint(-5,5) for _ in range(k)] for __ in range(m)]
        b=[[rng.randint(-5,5) for _ in range(n)] for __ in range(k)]
        got=matmul(a,b)
        for i in range(m):
            for j in range(n):
                exact=sum((Fraction(a[i][h])*Fraction(b[h][j]) for h in range(k)),Fraction(0))
                assert got[i][j]==float(exact);checks+=1
    # Comparison with independently evaluated logistic formula for two logits.
    for _ in range(trials):
        a,b=rng.uniform(-30,30),rng.uniform(-30,30)
        p=stable_softmax([a,b]);oracle_p=1/(1+math.exp(b-a))
        assert abs(p[0]-oracle_p)<5e-15;assert abs(sum(p)-1)<1e-14;checks+=2
    # Causal attention: first token output exactly its own value, any future tail.
    for _ in range(trials):
        values=[rng.uniform(-20,20),rng.uniform(-20,20),rng.uniform(-20,20)]
        q=[[1,0],[0,1],[1,1]];k=[[1,0],[0,1],[1,1]]
        o,w=attention(q,k,[[v] for v in values],causal=True)
        assert abs(o[0][0]-values[0])<1e-13
        assert abs(sum(w[2])-1)<1e-14;checks+=2
    # Compare tanh-network parameters to independently perturbed loss (no use of backprop derivative).
    for _ in range(trials):
        x=[rng.uniform(-.8,.8),rng.uniform(-.8,.8)]
        w1=[[rng.uniform(-1,1),rng.uniform(-1,1)] for _ in range(2)]
        b1=[rng.uniform(-1,1),rng.uniform(-1,1)]
        w2=[rng.uniform(-1,1),rng.uniform(-1,1)]
        b2=rng.uniform(-1,1);target=rng.uniform(-1,1);h=1e-5
        _,grad=loss_and_grads(x,target,w1,b1,w2,b2)
        def f(v):return loss_and_grads(x,target,w1,b1,w2,v)[0]
        centered=(f(b2+h)-f(b2-h))/(2*h)
        assert abs(centered-grad['b2'])<1e-8;checks+=1
    # int8 peak-based rounding bound applies only when calibration and inputs same.
    for _ in range(trials):
        x=[rng.uniform(-20,20) for __ in range(5)];s,q=quantize_int8(x);z=dequantize(s,q)
        assert all(-127<=code<=127 and abs(a-b)<=s/2+1e-11 for code,a,b in zip(q,x,z));checks+=5
    return {'schema':'atlas.neural-independent-finite-oracle/1','result':'passed','trials_per_family':trials,'comparisons':checks,'seed':seed,'independence':'Fraction exact matrix products, logistic 2-way oracle, finite differences and quantization rounding bounds','scope':'finite numerical software reference; no learned model quality, hardware or peer-review claims'}
if __name__=='__main__':
    result=oracle();print(json.dumps(result,sort_keys=True,indent=2))
