"""Uniform discrete passive membrane cable and sealed-end diffusion.

Lumped node capacitance F, axial conductance S, leak S. Every time step
represents a synthetic network, not calibrated tissue, a human nerve, or a
clinical response. No stimulation design is provided.
"""
from __future__ import annotations
from .foundations import _real
import hashlib,json,math


def cable_step(voltage_volts:list[float]|tuple[float,...],dt_s:float,
               capacitance_per_node_f:float,axial_conductance_s:float,
               leak_conductance_s:float,reversal_v:float,
               input_currents_a:list[float]|tuple[float,...]|None=None)->tuple[float,...]:
    """Explicit-Euler sealed-end chain, stable for dt <= C/(deg*g_ax+gL).

    C dV_i/dt=Σneighbors g_ax(V_j-V_i)-gL(V_i-E)+I_i.
    """
    if not isinstance(voltage_volts,(list,tuple)) or not 1<=len(voltage_volts)<=256:
        raise ValueError('bounded nonempty voltage chain required')
    vs=[_real(v,'node voltage') for v in voltage_volts]
    dt=_real(dt_s,'step seconds',positive=True)
    C=_real(capacitance_per_node_f,'node capacitance',positive=True)
    ga=_real(axial_conductance_s,'axial conductance',nonnegative=True)
    gl=_real(leak_conductance_s,'leak conductance',nonnegative=True)
    eq=_real(reversal_v,'reversal voltage')
    if input_currents_a is None:inputs=[0.0]*len(vs)
    else:
        if not isinstance(input_currents_a,(list,tuple)) or len(input_currents_a)!=len(vs):
            raise ValueError('input current count must match cable nodes')
        inputs=[_real(v,'node current') for v in input_currents_a]
    deg=0 if len(vs)==1 else 1 if len(vs)==2 else 2
    if deg*ga+gl>0 and dt*(deg*ga+gl)>C*(1+1e-12):
        raise ValueError('explicit stability/positivity step bound exceeded')
    result=[]
    for i,v in enumerate(vs):
        axial=ga*((vs[i-1]-v if i>0 else 0)+(vs[i+1]-v if i+1<len(vs) else 0))
        dV=dt/C*(axial-gl*(v-eq)+inputs[i])
        x=v+dV
        if not math.isfinite(x):raise ValueError('unstable or nonfinite step')
        result.append(x)
    return tuple(result)


def cable_trace(initial_v,dt_s,steps,capacitance_per_node_f,axial_conductance_s,
                leak_conductance_s,reversal_v,inputs=None):
    if type(steps) is not int or not 0<=steps<=10000:raise ValueError('steps in 0..10000')
    if not isinstance(initial_v,(list,tuple)) or len(initial_v)>256:raise ValueError('cable nodes invalid')
    state=tuple(initial_v)
    traces=[state]
    for i in range(steps):
        state=cable_step(state,dt_s,capacitance_per_node_f,axial_conductance_s,
                         leak_conductance_s,reversal_v,inputs)
        traces.append(state)
    return {'states':traces,'steps':steps,'last_state':state,
            'synthetic_numerical_model':True,'physical_axon_measured':False}


def cable_charge_coulombs(voltages,capacitance_per_node_f,reference_v=0.0):
    if not isinstance(voltages,(list,tuple)) or not voltages:raise ValueError('nodes required')
    C=_real(capacitance_per_node_f,'capacitance',positive=True)
    ref=_real(reference_v,'reference voltage')
    return C*sum(_real(v,'voltage')-ref for v in voltages)


def cable_stability_bound_seconds(nodes:int,capacitance_per_node_f:float,
                                  axial_conductance_s:float,leak_conductance_s:float):
    if type(nodes) is not int or not 1<=nodes<=256:raise ValueError('node count 1..256')
    C=_real(capacitance_per_node_f,'capacitance',positive=True)
    ga=_real(axial_conductance_s,'axial conductance',nonnegative=True)
    gl=_real(leak_conductance_s,'leak conductance',nonnegative=True)
    max_deg=0 if nodes==1 else 1 if nodes==2 else 2
    if max_deg*ga+gl==0:return {'bound_seconds':None,'no_passive_decay_or_coupling':True}
    return {'bound_seconds':C/(max_deg*ga+gl),'no_passive_decay_or_coupling':False}
