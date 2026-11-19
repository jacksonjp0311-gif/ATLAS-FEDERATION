"""Pure Python fixed-shape linear algebra and stabilized neural primitives."""
import math

def _matrix(x):
    if not isinstance(x,(list,tuple)) or not x or not all(isinstance(row,(list,tuple)) and row for row in x):
        raise ValueError('nonempty matrix required')
    cols=len(x[0])
    if not all(len(row)==cols and all(isinstance(v,(float,int)) and not isinstance(v,bool) and math.isfinite(v) for v in row) for row in x):
        raise ValueError('rectangular finite matrix required')
    return len(x),cols

def matmul(a,b):
    m,k=_matrix(a); j,n=_matrix(b)
    if k!=j:raise ValueError('incompatible matrix dimensions')
    return [[math.fsum(a[i][q]*b[q][c] for q in range(k)) for c in range(n)] for i in range(m)]

def transpose(a):
    _matrix(a)
    return [list(col) for col in zip(*a)]

def stable_softmax(logits, mask=None):
    if not isinstance(logits,(tuple,list)) or not logits or not all(isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x) for x in logits):
        raise ValueError('finite nonempty logits required')
    if mask is not None and (len(mask)!=len(logits) or not all(type(v) is bool for v in mask)):
        raise ValueError('boolean mask of equal width required')
    keep=[i for i in range(len(logits)) if mask is None or mask[i]]
    if not keep:raise ValueError('all entries masked; no valid probability distribution')
    maximum=max(logits[i] for i in keep)
    e={i:math.exp(logits[i]-maximum) for i in keep}
    denom=math.fsum(e.values())
    return [(e.get(i,0.0)/denom) for i in range(len(logits))]

def logsumexp(logits):
    stable_softmax(logits)  # enforce the same finite-domain precondition
    maximum=max(logits)
    return maximum+math.log(math.fsum(math.exp(x-maximum) for x in logits))

def layer_norm(x,gamma=None,beta=None,eps=1e-5):
    if not isinstance(x,(list,tuple)) or not x or not all(isinstance(v,(int,float)) and math.isfinite(v) and not isinstance(v,bool) for v in x):
        raise ValueError('finite nonempty vector required')
    if not (isinstance(eps,(float,int)) and math.isfinite(eps) and eps>0):raise ValueError('positive epsilon')
    if gamma is None:gamma=[1.0]*len(x)
    if beta is None:beta=[0.0]*len(x)
    if len(gamma)!=len(x) or len(beta)!=len(x) or not all(math.isfinite(float(v)) for v in (*gamma,*beta)):
        raise ValueError('feature-wise affine width mismatch')
    mean=math.fsum(x)/len(x)
    var=math.fsum((a-mean)**2 for a in x)/len(x)
    scale=math.sqrt(var+eps)
    return [((v-mean)/scale)*g+b for v,g,b in zip(x,gamma,beta)]
