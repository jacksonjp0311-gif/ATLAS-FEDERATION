"""Energy Atlas 0.2: offline survival-services energy accounting.

These mathematical examples do NOT design, wire, operate, approve, certify,
or protect actual batteries, grids, fuel systems, water purification, medical
loads, or electrical apparatus. Always retain true load data, ratings,
protections, independent reviews and applicable safety standards.
"""
from __future__ import annotations
from math import fsum
from typing import Sequence
from .models import InvalidPhysicalModel, real, microgrid_interval_dispatch, JOULES_PER_KWH


def water_lift_energy(volume_m3, head_m, pump_efficiency, *, density_kg_m3=1000., gravity_m_s2=9.80665):
    """Ideal hydraulic water-lifting work, not potable-water or pump-system design."""
    vol=real(volume_m3,'water volume m3',0)
    head=real(head_m,'total dynamic head m',0)
    efficiency=real(pump_efficiency,'aggregate pump efficiency',0,1)
    density=real(density_kg_m3,'density kg/m3',0)
    gravity=real(gravity_m_s2,'gravity m/s2',0)
    if efficiency<=0 or density<=0 or gravity<=0:raise InvalidPhysicalModel('positive efficiency, density, gravity required')
    hydraulic=vol*head*density*gravity
    electrical=hydraulic/efficiency
    return {'schema':'atlas.energy-water-lift/1','volume_m3':vol,'total_dynamic_head_m':head,
        'ideal_hydraulic_energy_j':hydraulic,'required_input_energy_j':electrical,
        'required_input_Wh':electrical/3600.,'conversion_loss_j':electrical-hydraulic,
        'model_scope':'prescribed volume/head with constant overall efficiency; no pipe-curve or dynamic operating point',
        'water_quality_certified':False,'pump_installation_safe':False,
        'limitations':['Static/dynamic head must come from a real hydraulic survey; this formula does not select a pump',
         'Friction, transients, motor start, water chemistry, filters, storage and electrical protection are not independently modeled']}


def heating_energy(mass_kg,heat_capacity_j_kgK,T_initial_C,T_target_C,*,useful_fraction=1.0):
    """Sensible heat requirement, not water disinfection/food safety."""
    m=real(mass_kg,'mass kg',0);cp=real(heat_capacity_j_kgK,'heat capacity J/kg K',0)
    a=real(T_initial_C,'initial Celsius');b=real(T_target_C,'target Celsius')
    eff=real(useful_fraction,'heat delivered fraction',0,1)
    if cp<=0 or eff<=0 or b<a:raise InvalidPhysicalModel('positive capacity/efficiency, target >= initial')
    q=m*cp*(b-a)
    return {'schema':'atlas.energy-sensible-heat/1','useful_heat_j':q,'input_heat_j':q/eff,
        'input_kWh':q/eff/JOULES_PER_KWH,
        'limitations':['Neglects evaporation, phase change, vessel heat capacity, convection and temperature-dependent cp',
          'Heating energy is NOT verification that contaminated water is potable or a food process is safe'],
        'water_potability_verified':False,'safe_equipment_instructions':False}


def shelter_heat_loss(UA_W_per_K, degree_hours_Kh):
    """Quasi-steady degree-hour heat loss, not safe heating system sizing."""
    ua=real(UA_W_per_K,'aggregate heat loss coefficient W/K',0)
    dh=real(degree_hours_Kh,'indoor minus outdoor degree-hours K*h',0)
    return {'schema':'atlas.energy-shelter-heat-loss/1', 'heat_loss_kWh':ua*dh/1000.,
        'assumptions':'constant envelope UA and specified positive temperature degree-hours',
        'limitations':['Infiltration, weather, solar gains, indoor moisture, thermal inertia and human health limits not resolved',
         'Not heating equipment design, ventilation prescription or combustion safety analysis']}


def fuel_to_delivered_electricity(volume_L, heating_value_MJ_L, electrical_efficiency):
    """Mass/energy arithmetic using caller-provided fuel specifications; never equipment operation."""
    volume=real(volume_L,'fuel volume L',0);hv=real(heating_value_MJ_L,'heating value MJ/L',0)
    eta=real(electrical_efficiency,'electrical efficiency',0,1)
    if eta<=0:raise InvalidPhysicalModel('efficiency > 0')
    available=volume*hv/3.6
    return {'schema':'atlas.energy-fuel-conversion/1', 'chemical_input_kWh':available,
        'electricity_at_assumed_efficiency_kWh':available*eta,
        'conversion_loss_kWh':available*(1-eta),
        'fuel_specification_origin':'caller_supplied_not_verified',
        'limitations':['Heating value and performance require measured fuel grade, environment and device-specific testing',
          'NO instructions for connecting generators, fuel storage, combustion, exhaust systems, ventilation or grid backfeed',
          'Carbon monoxide/fire risk requires official emergency guidance and properly qualified equipment']}


def emergency_load_allocation(services: list[dict], available_power_kW):
    """Priority-first abstract allocation. No protection, continuous-service or fairness guarantee.

    Services carry id, priority (smaller=earlier), requested_kW, minimum_kW.
    An undersupplied group at equal priority gets equal proportional reduction.
    No actual power flow or continuity is enforced; minima are checked after.
    """
    power=real(available_power_kW,'available power kW',0)
    if not isinstance(services,list) or not 1<=len(services)<=256:
        raise InvalidPhysicalModel('service list 1..256')
    prepared=[];ids=set()
    for s in services:
        if not isinstance(s,dict) or set(s)!={'service_id','priority','requested_kW','minimum_kW'}:
            raise InvalidPhysicalModel('exact service metadata fields required')
        sid=s['service_id'];p=s['priority']
        if not isinstance(sid,str) or not sid or len(sid)>128 or sid in ids:raise InvalidPhysicalModel('unique bounded service ID')
        if type(p) is not int or not 0<=p<=10000:raise InvalidPhysicalModel('priority 0..10000 integer')
        want=real(s['requested_kW'],'requested kW',0);minimum=real(s['minimum_kW'],'minimum kW',0)
        if minimum>want:raise InvalidPhysicalModel('minimum > requested')
        ids.add(sid);prepared.append((p,sid,want,minimum))
    groups=sorted({x[0] for x in prepared});out={};remaining=power
    for priority in groups:
        active=sorted((x for x in prepared if x[0]==priority),key=lambda x:x[1]);demand=fsum(x[2] for x in active)
        fraction=1 if demand<=remaining or demand==0 else remaining/demand
        for p,sid,want,minimum in active:
            served=want*fraction
            out[sid]={'priority':p,'requested_kW':want,'served_kW':served,'unserved_kW':want-served,
                      'minimum_requested_kW':minimum,'minimum_satisfied':served+1e-12>=minimum}
        remaining=max(0.,remaining-fsum(out[sid]['served_kW'] for _,sid,*_ in active))
    total=fsum(row['served_kW'] for row in out.values());unserved=fsum(row['unserved_kW'] for row in out.values())
    return {'schema':'atlas.energy-priority-load/1','available_power_kW':power,
        'served_kW':total,'unserved_kW':unserved,'unused_power_kW':max(0.,power-total),
        'services':{k:out[k] for k in sorted(out)},'all_declared_minima_met':all(r['minimum_satisfied'] for r in out.values()),
        'not_a_real_safety_dispatch':True,
        'limitations':['Priority policy is a hypothetical mathematical convention, not a professional triage policy',
          'Critical equipment may fail under partial power; duty cycle, startup current, voltage/frequency and minimum-on time missing',
          'Medical life support cannot be certified from kilowatt arithmetic']}


def energy_reserve_estimate(daily_load_kWh, capacity_kWh, initial_soc_fraction=1., reserve_fraction=0.,
                            discharge_efficiency=.9):
    """Zero-generation useful-energy budget; NOT predicted outage endurance."""
    demand=real(daily_load_kWh,'daily demand kWh',0);cap=real(capacity_kWh,'rated capacity kWh',0)
    soc=real(initial_soc_fraction,'state of charge fraction',0,1);floor=real(reserve_fraction,'reserve fraction',0,1)
    eta=real(discharge_efficiency,'discharge efficiency',0,1)
    if cap<=0 or eta<=0 or soc<floor:raise InvalidPhysicalModel('valid capacity, reserve and efficiency required')
    usable=cap*(soc-floor)*eta
    return {'schema':'atlas.energy-reserve-budget/1','usable_delivered_kWh':usable,
       'illustrative_days_at_constant_daily_load':usable/demand if demand>0 else None,
       'residual_without_generation_kWh':usable,
       'limitations':['No warranty of autonomy; no power limit, degradation, weather, minimum voltage, standby losses or BMS state',
        'Demand must be independently measured for real use; medical and other critical loads need qualified continuity design']}


def microgrid_profile(profile: list[dict], initial_kWh, capacity_kWh, *,
                      charge_limit_kW,discharge_limit_kW,eta_charge=.9,eta_discharge=.9):
    """Chronological interval energy ledger, no power-flow safety or real controller.

    Each row: {load_kW, renewable_kW, dt_hours, grid_available}.
    Computed EENS is observed energy not served under these *supplied values*,
    not expected unserved energy under a probability model.
    """
    if not isinstance(profile,list) or not 1<=len(profile)<=10000:raise InvalidPhysicalModel('bounded 1..10000 intervals')
    storage=real(initial_kWh,'initial storage kWh',0);capacity=real(capacity_kWh,'capacity kWh',0)
    charge_limit=real(charge_limit_kW,'charge limit kW',0);discharge_limit=real(discharge_limit_kW,'discharge limit kW',0)
    ech=real(eta_charge,'charging efficiency',0,1);edis=real(eta_discharge,'discharging efficiency',0,1)
    if capacity<=0 or storage>capacity or ech<=0 or edis<=0:raise InvalidPhysicalModel('capacity and efficiency state invalid')
    keys={'load_kW','renewable_kW','dt_hours','grid_available'}
    totals={'load_kWh':0.,'renewable_kWh':0.,'served_kWh':0.,'unserved_kWh':0.,
            'curtailed_kWh':0.,'imported_kWh':0.,'conversion_loss_kWh':0.,'battery_delta_kWh':0.,'hours':0.}
    intervals=[];low=storage;balance=[]
    for i,row in enumerate(profile):
        if not isinstance(row,dict) or set(row)!=keys:raise InvalidPhysicalModel('exact profile fields required')
        dt=real(row['dt_hours'],'duration hours',0)
        if dt<=0:raise InvalidPhysicalModel('duration must be positive')
        if type(row['grid_available']) is not bool:raise InvalidPhysicalModel('grid_available boolean')
        r=microgrid_interval_dispatch(row['load_kW'],row['renewable_kW'],storage,capacity,dt,
                        charge_limit,discharge_limit,ech,edis,grid_available=row['grid_available'])
        # Clamp only floating-point roundoff at physical storage boundaries.
        # Never conceal a material violation of the energy balance.
        raw_storage=r['stored_after_kWh']
        if raw_storage < -1e-10 or raw_storage > capacity+1e-10:
            raise AssertionError('storage state outside capacity beyond numerical tolerance')
        storage=max(0.,min(capacity,raw_storage));low=min(low,storage)
        intervals.append({'index':i,'duration_h':dt,'stored_before_kWh':storage-r['storage_delta_kWh'],**r})
        for column,lookup in [('load_kWh','load_kW'),('renewable_kWh','renewable_kW')]:totals[column]+=real(row[lookup],lookup,0)*dt
        for column,lookup in [('served_kWh','load_served_kW'),('unserved_kWh','unmet_load_kW'),('curtailed_kWh','renewable_curtailed_kW'),('imported_kWh','grid_import_kW')]:totals[column]+=r[lookup]*dt
        totals['conversion_loss_kWh']+=r['conversion_loss_kWh'];totals['battery_delta_kWh']+=r['storage_delta_kWh'];totals['hours']+=dt
        balance.append(r['balance_residual_kWh'])
    totals['energy_balance_residual_kWh']=(totals['renewable_kWh']+totals['imported_kWh']-
        totals['served_kWh']-totals['curtailed_kWh']-totals['conversion_loss_kWh']-totals['battery_delta_kWh'])
    if abs(totals['energy_balance_residual_kWh'])>1e-8*max(1.,totals['load_kWh'],totals['renewable_kWh']):
        raise AssertionError('profile energy accounting not closed')
    return {'schema':'atlas.energy-microgrid-profile/1','intervals':intervals,'totals':totals,
       'final_storage_kWh':storage,'minimum_storage_kWh':low,
       'unserved_share_of_demand':totals['unserved_kWh']/totals['load_kWh'] if totals['load_kWh']>0 else None,
       'number_of_intervals_with_unserved_load':sum(x['unmet_load_kW']>0 for x in intervals),
       'expected_loss_of_load_established':False,'electrical_grid_stability_verified':False,
       'limitations':['Input scenarios and load/generation profiles are caller supplied; no independent stochastic reliability inference',
            'No AC frequency, voltage, inverter startup, battery health, islanding/protection, transfer switches or black-start guarantee',
            'No hazardous electrical wiring or operational controls are implemented']}


def evaluate_survival_scenarios(scenarios:list[dict], initial_kWh, capacity_kWh, **limits):
    """Bounded worst-case across user-provided weather/load scenarios, not a probability guarantee."""
    if not isinstance(scenarios,list) or not 1<=len(scenarios)<=256:raise InvalidPhysicalModel('1..256 scenarios')
    items=[];seen=set()
    for entry in scenarios:
        if not isinstance(entry,dict) or set(entry)!={'scenario_id','profile'}:
            raise InvalidPhysicalModel('exact scenario_id and profile required')
        name=entry['scenario_id']
        if not isinstance(name,str) or not name or name in seen or len(name)>128:raise InvalidPhysicalModel('unique scenario ID')
        seen.add(name)
        p=microgrid_profile(entry['profile'],initial_kWh,capacity_kWh,**limits)
        items.append({'scenario_id':name,'unserved_kWh':p['totals']['unserved_kWh'],'load_kWh':p['totals']['load_kWh'],
                     'renewable_kWh':p['totals']['renewable_kWh'],'minimum_storage_kWh':p['minimum_storage_kWh'],
                     'balance_residual_kWh':p['totals']['energy_balance_residual_kWh']})
    worst=max(items,key=lambda x:(x['unserved_kWh'],-x['minimum_storage_kWh']))
    return {'schema':'atlas.energy-scenario-panel/1','scenarios':items,'worst_supplied_unserved_energy':worst,
      'population_outage_probability_known':False,'weather_resource_verified':False,
      'limitations':['Worst of a supplied scenario set is not a bound on unobserved physical emergencies',
        'Weather, demand correlation, degradation and equipment failure distributions are absent unless independently supplied']}
