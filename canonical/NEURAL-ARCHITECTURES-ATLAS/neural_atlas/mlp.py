"""Fully explicit one-hidden-layer tanh regression and exact analytic gradients."""
import math

def forward(x,w1,b1,w2,b2):
    if len(w1)!=len(b1) or len(w1)!=len(w2) or any(len(row)!=len(x) for row in w1):
        raise ValueError('MLP width mismatch')
    a=[math.tanh(math.fsum(u*v for u,v in zip(x,row))+bias) for row,bias in zip(w1,b1)]
    return math.fsum(aa*w for aa,w in zip(a,w2))+b2,a

def loss_and_grads(x,target,w1,b1,w2,b2):
    y,hidden=forward(x,w1,b1,w2,b2)
    err=y-target
    d_w2=[err*a for a in hidden]
    d_b2=err
    delta=[err*w*(1.0-a*a) for w,a in zip(w2,hidden)]
    d_w1=[[d*xi for xi in x] for d in delta]
    d_b1=delta
    return 0.5*err*err,{'w1':d_w1,'b1':d_b1,'w2':d_w2,'b2':d_b2}

def sgd_step(x,target,w1,b1,w2,b2,lr):
    if not math.isfinite(lr) or lr<=0:raise ValueError('learning rate must be positive')
    loss,g=loss_and_grads(x,target,w1,b1,w2,b2)
    nw1=[[v-lr*d for v,d in zip(row,deriv)] for row,deriv in zip(w1,g['w1'])]
    nb1=[v-lr*d for v,d in zip(b1,g['b1'])]
    nw2=[v-lr*d for v,d in zip(w2,g['w2'])]
    return loss,nw1,nb1,nw2,b2-lr*g['b2']
