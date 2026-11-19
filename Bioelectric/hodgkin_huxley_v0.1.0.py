"""Original educational Hodgkin–Huxley squid-axon reference model.

Legacy biophysical units mV, ms, uA/cm², mS/cm², uF/cm² are explicit.
These literature parameter values do NOT generalize to human tissues or
clinical devices, and no body-connected experiments should be inferred.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
from .foundations import _real


def _exp(x):
    if x>700:return float('inf')
    if x< -700:return 0.0
    return math.exp(x)


def _vtrap(x,scale):
    """x/(1-exp(-x/scale)); analytic removable singularity x=0 -> scale."""
    if abs(x/scale)<1e-6:
        return scale*(1+0.5*x/scale+(x/scale)**2/12)
    return x/(-math.expm1(-x/scale))


def hh_rates(v_mV:float)->dict:
    """H-H squid axon gating rates in ms^-1; v_mV uses rest near -65 mV."""
    v=_real(v_mV,'membrane voltage mV')
    if not -150<=v<=100:raise ValueError('outside reference parameter range, not extrapolated')
    am=0.1*_vtrap(v+40,10)
    bm=4*_exp(-(v+65)/18)
    ah=0.07*_exp(-(v+65)/20)
    bh=1/(1+_exp(-(v+35)/10))
    an=0.01*_vtrap(v+55,10)
    bn=0.125*_exp(-(v+65)/80)
    d={'m':(am,bm),'h':(ah,bh),'n':(an,bn)}
    if not all(math.isfinite(a) and math.isfinite(b) and a>=0 and b>=0 for a,b in d.values()):
        raise ValueError('invalid reference rates')
    return d


def gate_steady_state_and_tau(alpha, beta):
    a=_real(alpha,'alpha',nonnegative=True);b=_real(beta,'beta',nonnegative=True)
    if a+b<=0:raise ValueError('alpha + beta must be positive')
    return a/(a+b),1/(a+b)


def exact_gate_update(gate,alpha,beta,dt_ms):
    x=_real(gate,'gate fraction')
    if not 0<=x<=1:raise ValueError('gate fraction 0..1')
    dt=_real(dt_ms,'step milliseconds',nonnegative=True)
    xinf,tau=gate_steady_state_and_tau(alpha,beta)
    return xinf+(x-xinf)*math.exp(-dt/tau)


@dataclass(frozen=True)
class HHState:
    v_mV:float
    m:float
    h:float
    n:float
    def __post_init__(self):
        v=_real(self.v_mV,'membrane voltage')
        if not -150<=v<=100:raise ValueError('HH model voltage domain exceeded')
        for name in ('m','h','n'):
            x=_real(getattr(self,name),name)
            if not 0<=x<=1:raise ValueError('gate probability outside 0..1')


def hh_rest_state(v_mV=-65.0):
    rates=hh_rates(v_mV)
    x={k:gate_steady_state_and_tau(*rates[k])[0] for k in rates}
    return HHState(v_mV,x['m'],x['h'],x['n'])


def hh_ionic_currents(state:HHState)->dict:
    if type(state) is not HHState:raise ValueError('HHState required')
    v=state.v_mV
    # Original 1952 idealized squid giant axon calibration, temperature ~6.3 C.
    i_na=120.0*state.m**3*state.h*(v-50.0)
    i_k=36.0*state.n**4*(v+77.0)
    i_l=0.3*(v+54.387)
    return {'sodium_uA_per_cm2':i_na,'potassium_uA_per_cm2':i_k,
            'leak_uA_per_cm2':i_l,'total_uA_per_cm2':i_na+i_k+i_l}


def hh_step(state:HHState,dt_ms:float,injected_current_uA_per_cm2:float=0):
    if type(state) is not HHState:raise ValueError('HHState required')
    dt=_real(dt_ms,'step milliseconds',positive=True)
    if dt>0.025:raise ValueError('HH explicit integration step too large for this reference')
    inj=_real(injected_current_uA_per_cm2,'injected current')
    if abs(inj)>50:raise ValueError('out of synthetic test current range')
    rates=hh_rates(state.v_mV)
    ions=hh_ionic_currents(state)
    # C_m = 1 uF/cm² and g in mS/cm² => uA/cm² yield mV/ms.
    dv=dt*(inj-ions['total_uA_per_cm2'])/1.0
    after=HHState(state.v_mV+dv,
        exact_gate_update(state.m,*rates['m'],dt),
        exact_gate_update(state.h,*rates['h'],dt),
        exact_gate_update(state.n,*rates['n'],dt))
    return after


def hh_trace(steps:int=500,dt_ms=0.01,applied_current_uA_per_cm2=0.0,initial:HHState|None=None):
    if type(steps) is not int or not 1<=steps<=20000:raise ValueError('steps 1..20000')
    state=initial if initial is not None else hh_rest_state()
    result=[state]
    for k in range(steps):
        state=hh_step(state,dt_ms,applied_current_uA_per_cm2)
        result.append(state)
    return {'schema':'atlas.bioelectric-hh-reference/1','steps':steps,'dt_ms':dt_ms,
        'membrane_mV':[x.v_mV for x in result],
        'last_gates':{'m':state.m,'h':state.h,'n':state.n},
        'model':'historical idealized 6.3 C squid giant axon parameters',
        'measured_human_or_organism_data':False,'medical_device_applicability':False}
