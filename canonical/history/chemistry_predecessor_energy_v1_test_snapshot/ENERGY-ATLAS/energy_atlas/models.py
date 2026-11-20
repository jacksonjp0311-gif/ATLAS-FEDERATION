"""Energy Atlas v0.1: pure-Python, unit-explicit energy reference models.

These are EDUCATIONAL idealizations. They do not estimate engineering safety,
verify physical measurements, control high-voltage equipment, or run a grid.
All values are caller-supplied; results are conditional on declared assumptions.
"""
from __future__ import annotations
from math import exp,log,pi,sqrt,isfinite
from typing import Sequence

SIGMA=5.670374419e-8 # W/m^2/K^4 from exact SI defining constants
C_LIGHT=299792458 # m/s exact
JOULES_PER_KWH=3_600_000 # exact unit relationship
BETZ_MAX=16/27 # ideal actuator-disk model (not measured turbine efficiency)

class InvalidPhysicalModel(ValueError):
    pass

def real(x,name,minimum=None,maximum=None):
    if type(x) not in (float,int) or not isfinite(x):raise InvalidPhysicalModel(f'{name}: finite numeric value required')
    v=float(x)
    if minimum is not None and v<minimum:raise InvalidPhysicalModel(f'{name}: below lower bound {minimum}')
    if maximum is not None and v>maximum:raise InvalidPhysicalModel(f'{name}: above upper bound {maximum}')
    return v

def unit_convert(value,source,target):
    """Exact unit ratios for J, kJ, Wh, kWh, MJ, and GJ; no physical measurement."""
    units={'J':1,'kJ':1000,'Wh':3600,'kWh':3600000,'MJ':1000000,'GJ':1000000000}
    if source not in units or target not in units:raise InvalidPhysicalModel('unsupported energy unit')
    return real(value,'energy')*units[source]/units[target]

def steady_energy_balance(inputs_j:Sequence, outputs_j:Sequence, stored_delta_j):
    """Residual ΣEin − ΣEout − ΔEstored in joules; no hidden loss guess."""
    if not isinstance(inputs_j,(list,tuple)) or not isinstance(outputs_j,(list,tuple)):raise InvalidPhysicalModel('flows must be sequences')
    a=[real(x,'inflow J',0) for x in inputs_j];b=[real(x,'outflow J',0) for x in outputs_j]
    d=real(stored_delta_j,'change stored J')
    residual=sum(a)-sum(b)-d
    scale=max(1.0,sum(a),sum(b),abs(d))
    return {'input_j':sum(a),'output_j':sum(b),'stored_delta_j':d,'residual_j':residual,
            'relative_residual':residual/scale,'model':'closed accounted boundary; any unreported loss appears in residual',
            'empirical_measurement_performed':False}

def converter_efficiency(input_energy_j,useful_energy_j):
    """Ordinary converter ratio. Not heat-pump COP and not exergy efficiency."""
    i=real(input_energy_j,'input energy J',0)
    o=real(useful_energy_j,'useful output energy J',0)
    if i<=0 or o>i:raise InvalidPhysicalModel('passive converter needs positive input and useful output <= input')
    return {'efficiency':o/i,'loss_j':i-o,'note':'input and useful output must have the same accounting boundary'}

def carnot_engine(T_hot_K,T_cold_K):
    h=real(T_hot_K,'hot Kelvin',0)
    c=real(T_cold_K,'cold Kelvin',0)
    if not 0<c<h:raise InvalidPhysicalModel('require 0 < cold < hot absolute temperature')
    return {'max_thermal_efficiency':1-c/h,'ideal_cooling_cop':c/(h-c),
            'ideal_heating_cop':h/(h-c),'note':'reversible bounds, not achieved device efficiency or electricity generation promise'}

def reversible_ideal_gas_work(mol,T_K,V1_m3,V2_m3,Rgas=8.31446261815324):
    n=real(mol,'moles',0);T=real(T_K,'absolute temperature',0);a=real(V1_m3,'initial m3',0);b=real(V2_m3,'final m3',0)
    if min(n,T,a,b)<=0:raise InvalidPhysicalModel('positive n,T,V required')
    return {'work_by_gas_j':n*T*real(Rgas,'gas constant J/mol K',0)*log(b/a),
            'assumptions':'reversible isothermal ideal gas; constant temperature; signed work by gas'}

def conduction_rate(k_W_mK,area_m2,thickness_m,T_hot_K,T_cold_K):
    k=real(k_W_mK,'thermal conductivity',0);area=real(area_m2,'area',0);L=real(thickness_m,'thickness',0)
    th=real(T_hot_K,'hot Kelvin',0);tc=real(T_cold_K,'cold Kelvin',0)
    if L<=0 or th<tc:raise InvalidPhysicalModel('positive thickness, hot >= cold required')
    return k*area*(th-tc)/L

def convection_rate(h_W_m2K,area_m2,T_surface_K,T_fluid_K):
    return real(h_W_m2K,'convection coefficient',0)*real(area_m2,'area',0)*(
        real(T_surface_K,'surface K',0)-real(T_fluid_K,'fluid K',0))

def radiation_rate(emissivity,area_m2,T_surface_K,T_surroundings_K):
    eps=real(emissivity,'emissivity',0,1);a=real(area_m2,'area m2',0)
    t=real(T_surface_K,'surface K',0);u=real(T_surroundings_K,'surrounding K',0)
    return SIGMA*eps*a*(t**4-u**4)

def lumped_cooling(T0_K,T_environment_K,time_s,mass_kg,cp_J_kgK,h_W_m2K,area_m2):
    T0=real(T0_K,'initial K',0);Te=real(T_environment_K,'ambient K',0);t=real(time_s,'time s',0)
    m=real(mass_kg,'mass kg',0);cp=real(cp_J_kgK,'heat capacity',0);h=real(h_W_m2K,'heat transfer',0);a=real(area_m2,'area',0)
    if min(m,cp,h,a)<=0:raise InvalidPhysicalModel('positive thermal mass and heat transfer')
    tau=m*cp/(h*a)
    return {'temperature_K':Te+(T0-Te)*exp(-t/tau),'time_constant_s':tau,
           'assumptions':'uniform internal temperature, constant properties and convection, no internal heat source'}

def dc_ohms_law(*,V=None,I=None,R=None):
    """Supply exactly two of V (V), I (A), R (Ω), solve third; R must be >0 if supplied."""
    if sum(x is not None for x in (V,I,R))!=2:raise InvalidPhysicalModel('exactly two V,I,R required')
    if V is not None:V=real(V,'voltage V')
    if I is not None:I=real(I,'current A')
    if R is not None:R=real(R,'resistance ohm',0)
    if R is not None and R<=0:raise InvalidPhysicalModel('strictly positive resistance')
    if R is None:
        if I==0:raise InvalidPhysicalModel('cannot infer resistance from zero current')
        R=V/I
        if R<=0:raise InvalidPhysicalModel('inferred resistance nonpositive')
    if V is None:V=I*R
    if I is None:I=V/R
    return {'voltage_V':V,'current_A':I,'resistance_ohm':R,'power_W':V*I,
            'note':'power positive under passive sign convention; negative current/voltage can represent reversed reference'}

def rc_discharge(V0,seconds,R_ohm,C_farad):
    v=real(V0,'initial voltage');t=real(seconds,'time',0);R=real(R_ohm,'resistance',0);C=real(C_farad,'capacitance',0)
    if R*C<=0:raise InvalidPhysicalModel('RC>0 required')
    V=v*exp(-t/(R*C))
    return {'voltage_V':V,'energy_J':0.5*C*V*V,'tau_s':R*C,
            'assumptions':'linear passive lumped RC, capacitor initially at V0, no load or leakage beyond R'}

def ac_single_phase(V_rms,I_rms,power_factor,reactive_sign=1):
    v=real(V_rms,'Vrms',0);i=real(I_rms,'Irms',0);pf=real(power_factor,'pf',-1,1)
    if reactive_sign not in (-1,1):raise InvalidPhysicalModel('reactive sign -1 or +1')
    s=v*i
    return {'apparent_VA':s,'real_W':s*pf,'reactive_var':reactive_sign*s*sqrt(max(0,1-pf*pf)),
       'assumptions':'single sinusoidal steady-state, RMS, one phase, chosen reactive sign; harmonics omitted'}

def balanced_three_phase(V_line_rms,I_line_rms,pf):
    v=real(V_line_rms,'line rms voltage',0);i=real(I_line_rms,'line rms current',0);p=real(pf,'pf',-1,1)
    return {'real_W':sqrt(3)*v*i*p,'apparent_VA':sqrt(3)*v*i,'assumptions':'balanced sinusoidal 3 phase'}

def ideal_transformer(V_primary,turns_primary,turns_secondary,I_secondary):
    v=real(V_primary,'primary voltage');np=real(turns_primary,'primary turns',0);ns=real(turns_secondary,'secondary turns',0);isec=real(I_secondary,'secondary current')
    if np*ns<=0:raise InvalidPhysicalModel('positive nonzero turns required')
    return {'V_secondary':v*ns/np,'I_primary':isec*ns/np,
            'assumptions':'ideal lossless transformer, voltage and current magnitudes, sinusoidal steady-state; not physical electrical safety design'}

def line_resistive_loss(I_rms_A,R_ohm,conductors=1):
    i=real(I_rms_A,'current RMS A',0);r=real(R_ohm,'single-conductor resistance Ω',0)
    if type(conductors)!=int or not 1<=conductors<=100:raise InvalidPhysicalModel('conductors 1..100')
    return conductors*i*i*r

def solar_pv_power(P_rated_W,irradiance_W_m2,T_cell_C,gamma_per_C,ref_W_m2=1000):
    p=real(P_rated_W,'rated power W',0);G=real(irradiance_W_m2,'plane irradiance',0);T=real(T_cell_C,'cell Celsius')
    gamma=real(gamma_per_C,'power temperature coefficient',-1,1);ref=real(ref_W_m2,'reference irradiance',0)
    if ref<=0:raise InvalidPhysicalModel('positive reference irradiance')
    factor=1+gamma*(T-25)
    if factor<0:raise InvalidPhysicalModel('linear PV model invalid at supplied temperature, no negative energy prediction')
    return {'dc_power_W':p*G/ref*factor,'scope':'linear rated DC nameplate approximation; excludes inverter, shading, spectrum, degradation, soiling and clipping'}

def wind_turbine_power(rho_kg_m3,rotor_area_m2,wind_speed_m_s,Cp):
    rho=real(rho_kg_m3,'density kg/m3',0);area=real(rotor_area_m2,'swept area',0);v=real(wind_speed_m_s,'wind speed',0);cp=real(Cp,'power coefficient',0,BETZ_MAX)
    incident=0.5*rho*area*v**3
    return {'incident_wind_W':incident,'ideal_extracted_W':incident*cp,'ideal_betz_W':incident*BETZ_MAX,
            'scope':'steady actuator disk, Betz constraint, no cut-in/rated/cut-out or generator electrical losses'}

def hydroelectric_power(rho_kg_m3,flow_m3_s,head_m,hydraulic_efficiency):
    rho=real(rho_kg_m3,'density',0);q=real(flow_m3_s,'volume flow',0);h=real(head_m,'head m',0);eta=real(hydraulic_efficiency,'efficiency',0,1)
    return rho*9.80665*q*h*eta

def battery_step(stored_kWh,capacity_kWh,dt_hours,charge_input_kW=0,discharge_output_kW=0,eta_charge=1,eta_discharge=1):
    e=real(stored_kWh,'stored kWh',0);cap=real(capacity_kWh,'capacity kWh',0);dt=real(dt_hours,'time h',0)
    ch=real(charge_input_kW,'charging input kW',0);dis=real(discharge_output_kW,'discharge delivered kW',0)
    etac=real(eta_charge,'charge efficiency',0,1);etad=real(eta_discharge,'discharge efficiency',0,1)
    if cap<=0 or e>cap or min(etac,etad)<=0 or (ch>0 and dis>0):raise InvalidPhysicalModel('invalid capacity/efficiencies or simultaneous charge and discharge')
    new=e+ch*dt*etac-dis*dt/etad
    if new<-1e-12 or new>cap+1e-12:raise InvalidPhysicalModel('requested storage step exceeds limits; no silently clipped energy')
    return {'stored_kWh':min(cap,max(0,new)),'soc':min(cap,max(0,new))/cap,'loss_kWh':ch*dt*(1-etac)+dis*dt*(1/etad-1),
            'assumptions':'constant capacity, one-way efficiencies, ideal power constraints, no degradation or safety control'}

def capacity_factor(energy_kWh,rated_kW,hours):
    e=real(energy_kWh,'output kWh',0);p=real(rated_kW,'rated kW',0);h=real(hours,'hours',0)
    if p*h<=0 or e>p*h+1e-9:raise InvalidPhysicalModel('invalid capacity-factor interval')
    return e/(p*h)

def simple_levelized_cost(initial_capex,annual_costs,annual_energy_kWh,discount):
    c0=real(initial_capex,'CAPEX',0);d=real(discount,'real discount',0)
    if not isinstance(annual_costs,(list,tuple)) or not isinstance(annual_energy_kWh,(list,tuple)) or len(annual_costs)!=len(annual_energy_kWh) or not annual_costs or len(annual_costs)>200:raise InvalidPhysicalModel('matching yearly cost and energy arrays 1..200')
    cpv=c0;epv=0
    for t,(c,e) in enumerate(zip(annual_costs,annual_energy_kWh),1):
        cpv+=real(c,'annual cost',0)/(1+d)**t;epv+=real(e,'annual energy kWh',0)/(1+d)**t
    if epv<=0:raise InvalidPhysicalModel('no discounted output')
    return {'currency_per_kWh':cpv/epv,'cost_npv':cpv,'energy_pv_kWh':epv,
           'limitations':'no assumed externalities, curtailment, taxation, salvage, fuel inflation or social discount; input assumptions dominate estimate'}

def nuclear_mass_energy(delta_mass_kg):
    return real(delta_mass_kg,'mass defect kg',0)*C_LIGHT*C_LIGHT

def piecewise_energy_j(times_s,power_W):
    """Trapezoidal integral over measured/supplied samples with explicit sampling assumption."""
    if not isinstance(times_s,(list,tuple)) or not isinstance(power_W,(list,tuple)) or len(times_s)!=len(power_W) or len(times_s)<2:raise InvalidPhysicalModel('at least two time/power samples')
    times=[real(x,'sample time') for x in times_s];power=[real(x,'power W') for x in power_W]
    if any(times[i+1]<=times[i] for i in range(len(times)-1)):raise InvalidPhysicalModel('strictly increasing timestamps required')
    out=sum((times[i+1]-times[i])*(power[i+1]+power[i])*0.5 for i in range(len(times)-1))
    return {'joules':out,'scope':'trapezoidal interpolation between samples, NOT exact continuous physical energy if samples are sparse'}

def microgrid_interval_dispatch(load_kW,renewable_kW,battery_stored_kWh,capacity_kWh,dt_hours,
                                charge_limit_kW,discharge_limit_kW,eta_charge=.9,eta_discharge=.9,
                                grid_available=False):
    """One bounded energy-only interval. NOT electrical grid stability/control.

    Priority renewable direct load, store surplus, discharge on deficit; with an
    external grid optionally serving leftovers, otherwise explicitly unmet.
    Power/current, inverter/grid protection and battery dynamics not modeled.
    """
    load=real(load_kW,'load kW',0);gen=real(renewable_kW,'renewable kW',0)
    stored=real(battery_stored_kWh,'stored kWh',0);cap=real(capacity_kWh,'capacity kWh',0)
    dt=real(dt_hours,'duration hours',0);cl=real(charge_limit_kW,'charge rating kW',0);dl=real(discharge_limit_kW,'discharge rating kW',0)
    ech=real(eta_charge,'charge efficiency',0,1);edis=real(eta_discharge,'discharge efficiency',0,1)
    if type(grid_available) is not bool or dt<=0 or cap<=0 or stored>cap or ech*edis<=0:
        raise InvalidPhysicalModel('valid finite storage and interval required')
    direct=min(load,gen);deficit=load-direct;surplus=gen-direct
    charging=min(surplus,cl,(cap-stored)/(dt*ech)) if surplus else 0.
    discharge=min(deficit,dl,stored*edis/dt) if deficit else 0.
    remaining=max(0.,deficit-discharge)
    imported=remaining if grid_available else 0.
    unmet=0. if grid_available else remaining
    curtailed=max(0.,surplus-charging)
    delta=charging*dt*ech-discharge*dt/edis
    loss=charging*dt*(1-ech)+discharge*dt*(1/edis-1)
    served=load-unmet
    residual=(gen+imported)*dt - (served+curtailed)*dt - delta-loss
    if abs(residual)>1e-8*max(1.,(gen+imported)*dt,served*dt):
        raise AssertionError('internal ledger imbalance')
    return {'load_served_kW':served,'unmet_load_kW':unmet,'renewable_generated_kW':gen,
       'renewable_curtailed_kW':curtailed,'grid_import_kW':imported,'battery_charge_kW':charging,
       'battery_discharge_kW':discharge,'stored_after_kWh':stored+delta,'storage_delta_kWh':delta,
       'conversion_loss_kWh':loss,'balance_residual_kWh':residual,
       'assumptions':'single energy-only interval; renewable first, ideal grid if present, no inverter rating, protections, AC stability or BMS constraints'}
