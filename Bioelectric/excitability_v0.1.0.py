"""Dimensionless FitzHugh–Nagumo toy excitability reference, not clinical biology."""
from __future__ import annotations
from dataclasses import dataclass
import math
from .foundations import _real

@dataclass(frozen=True)
class FHNState:
    v:float
    w:float
    def __post_init__(self):
        for name in ('v','w'):
            x=_real(getattr(self,name),name)
            if abs(x)>50:raise ValueError('state outside finite reference range')


def fhn_derivative(state:FHNState,input_drive=0.0,a=0.7,b=0.8,epsilon=0.08):
    if type(state) is not FHNState:raise ValueError('FHNState required')
    I=_real(input_drive,'drive')
    aa=_real(a,'a');bb=_real(b,'b',positive=True)
    eps=_real(epsilon,'epsilon',positive=True)
    if eps>1:raise ValueError('reference epsilon 0..1')
    return (state.v-state.v**3/3-state.w+I,eps*(state.v+aa-bb*state.w))


def fhn_rk4_step(state:FHNState,dt,drive=0,a=0.7,b=0.8,epsilon=0.08):
    timestep=_real(dt,'dt',positive=True)
    if timestep>0.025:raise ValueError('reference integration step >0.025 unsupported')
    def deriv(s):return fhn_derivative(s,drive,a,b,epsilon)
    k1=deriv(state)
    k2=deriv(FHNState(state.v+0.5*timestep*k1[0],state.w+0.5*timestep*k1[1]))
    k3=deriv(FHNState(state.v+0.5*timestep*k2[0],state.w+0.5*timestep*k2[1]))
    k4=deriv(FHNState(state.v+timestep*k3[0],state.w+timestep*k3[1]))
    return FHNState(state.v+timestep*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6,
                    state.w+timestep*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6)


def fhn_trace(initial:FHNState,steps,dt,drive=0):
    if type(steps) is not int or not 1<=steps<=10000:raise ValueError('steps 1..10000')
    state=initial;out=[(state.v,state.w)]
    for _ in range(steps):
        state=fhn_rk4_step(state,dt,drive)
        out.append((state.v,state.w))
    return {'states':out,'final_state':out[-1],'dimensionless_toy_dynamics_only':True,
            'diagnostic_or_therapeutic_validity':False}
