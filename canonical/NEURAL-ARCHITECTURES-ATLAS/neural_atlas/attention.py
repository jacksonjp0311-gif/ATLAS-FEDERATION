"""Educational single-head scaled-dot-product attention; no training or GPU claims."""
from math import sqrt
from .mathcore import _matrix,stable_softmax,matmul,transpose

def attention(q,k,v,causal=False):
    l,d=_matrix(q);m,d2=_matrix(k);vlen,dv=_matrix(v)
    if d!=d2 or m!=vlen or (causal and l!=m):raise ValueError('incompatible attention shapes')
    scores=matmul(q,transpose(k))
    rows=[]
    for i,score in enumerate(scores):
        rows.append(stable_softmax([x/sqrt(d) for x in score],[j<=i for j in range(m)] if causal else None))
    return matmul(rows,v),rows
