"""Original ATLAS FORGE Bioelectric v0.1 SI electrochemical and membrane references.

No clinical diagnosis, stimulation, medical device, physical cell measurements,
source-original authentication, or body-connected hardware assertions.
"""
from __future__ import annotations
import math

BOLTZMANN = 1.380649e-23  # J/K, exact SI definition
AVOGADRO = 6.02214076e23  # 1/mol, exact SI definition
ELEMENTARY_CHARGE = 1.602176634e-19  # C, exact SI definition
GAS_CONSTANT = BOLTZMANN * AVOGADRO
FARADAY = ELEMENTARY_CHARGE * AVOGADRO


def _real(value, name, *, positive=False, nonnegative=False):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError(f'{name} must be a finite real scalar')
    x=float(value)
    if positive and x<=0:raise ValueError(f'{name} must be positive')
    if nonnegative and x<0:raise ValueError(f'{name} must be nonnegative')
    return x


def thermal_voltage(temperature_kelvin:float)->float:
    """kB*T/e in V, where kB/e are exact SI defining constants."""
    T=_real(temperature_kelvin,'temperature',positive=True)
    return BOLTZMANN*T/ELEMENTARY_CHARGE


def nernst_potential(valence:int,c_inside:float,c_outside:float,temperature_kelvin:float)->float:
    """Ideal ion equilibrium voltage (V, inside relative outside).

    Concentrations must use same units, positive; activities and junction
    potentials neglected. Signs follow z: E=(RT/zF)ln(c_out/c_in).
    """
    if type(valence) is not int or valence==0 or abs(valence)>8:
        raise ValueError('nonzero integer valence within [-8,+8] required')
    cin=_real(c_inside,'inside concentration',positive=True)
    cout=_real(c_outside,'outside concentration',positive=True)
    T=_real(temperature_kelvin,'temperature',positive=True)
    return GAS_CONSTANT*T/(valence*FARADAY)*math.log(cout/cin)


def ghk_voltage(p_k:float,p_na:float,p_cl:float,
                potassium_in:float,potassium_out:float,
                sodium_in:float,sodium_out:float,
                chloride_in:float,chloride_out:float,
                temperature_kelvin:float)->float:
    """GHK constant-field *zero-current* potential in V (monovalent ions).

    Uses consistent concentration units and relative permeability weights.
    Ignores ion activities, pumps, other ions, multi-ion pore interactions.
    Chloride inside/outside terms are reversed by valence sign.
    """
    pk=_real(p_k,'K permeability',nonnegative=True)
    pna=_real(p_na,'Na permeability',nonnegative=True)
    pcl=_real(p_cl,'Cl permeability',nonnegative=True)
    if pk+pna+pcl<=0:raise ValueError('at least one ion permeability must be positive')
    ki=_real(potassium_in,'K inside',positive=True)
    ko=_real(potassium_out,'K outside',positive=True)
    nai=_real(sodium_in,'Na inside',positive=True)
    nao=_real(sodium_out,'Na outside',positive=True)
    cli=_real(chloride_in,'Cl inside',positive=True)
    clo=_real(chloride_out,'Cl outside',positive=True)
    T=_real(temperature_kelvin,'temperature',positive=True)
    top=pk*ko+pna*nao+pcl*cli
    bottom=pk*ki+pna*nai+pcl*clo
    if top<=0 or bottom<=0 or not math.isfinite(top/bottom):raise ValueError('unsafe scaled concentrations')
    return GAS_CONSTANT*T/FARADAY*math.log(top/bottom)


def conductance_equilibrium(conductances:list[float]|tuple[float,...],
                            reversals_volts:list[float]|tuple[float,...],
                            applied_current_amp:float=0.0)->dict:
    """Parallel linear Ohmic membranes: equilibrium sum(g E)+I divided sum(g)."""
    if not isinstance(conductances,(list,tuple)) or not isinstance(reversals_volts,(list,tuple)):
        raise ValueError('sequences required')
    if len(conductances)!=len(reversals_volts) or not 1<=len(conductances)<=32:
        raise ValueError('paired nonempty conductance/reversal values required')
    gs=[_real(g,'conductance',nonnegative=True) for g in conductances]
    es=[_real(v,'reversal voltage') for v in reversals_volts]
    current=_real(applied_current_amp,'applied current')
    total=sum(gs)
    if total<=0:raise ValueError('unconstrained equilibrium when all g=0')
    v=(sum(g*e for g,e in zip(gs,es))+current)/total
    if not math.isfinite(v):raise ValueError('nonfinite equilibrium')
    return {'equilibrium_volts':v,'total_conductance_siemens':total,
            'total_current_amp':current,'linear_model_only':True}


def passive_membrane_voltage(v0_volts:float,rest_volts:float,
                             capacitance_farads:float,conductance_siemens:float,
                             time_seconds:float,applied_current_amp:float=0.0)->dict:
    """Closed-form solution for a fixed leak+capacitance membrane model.

    C dV/dt=-g(V-E)+I. Zero g excluded: linear unbounded drift case
    handled separately as conservation, not a false finite time constant.
    """
    v0=_real(v0_volts,'initial voltage');eq=_real(rest_volts,'reversal voltage')
    C=_real(capacitance_farads,'capacitance',positive=True)
    g=_real(conductance_siemens,'conductance',positive=True)
    t=_real(time_seconds,'time',nonnegative=True)
    I=_real(applied_current_amp,'applied current')
    tau=C/g
    v_inf=eq+I/g
    voltage=v_inf+(v0-v_inf)*math.exp(-t/tau)
    return {'voltage_volts':voltage,'time_constant_seconds':tau,
            'steady_state_volts':v_inf,'stored_charge_coulombs':C*voltage,
            'passive_lumped_model':True,'physical_cell_measured':False}


def capacitor_stored_energy(capacitance_farads:float,voltage_volts:float)->float:
    C=_real(capacitance_farads,'capacitance',nonnegative=True)
    v=_real(voltage_volts,'voltage')
    return 0.5*C*v*v


def membrane_surface_capacitance(area_m2:float,specific_capacitance_f_per_m2:float)->float:
    area=_real(area_m2,'area',positive=True)
    cs=_real(specific_capacitance_f_per_m2,'specific capacitance',positive=True)
    return area*cs
