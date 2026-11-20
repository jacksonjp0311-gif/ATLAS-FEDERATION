"""Energy Atlas v1 — offline survival accounting, *never* equipment control.

Every input is a stipulated mathematical quantity. No physical system is
connected; none of these functions designs or certifies generators, potable
water, medical backup, electrical wiring, batteries or grid islanding.
"""
from __future__ import annotations
from math import isfinite, fsum
from .models import InvalidPhysicalModel, real


def _nonneg(v, name):
    return real(v, name, 0)


def _positive(v,name):
    result=_nonneg(v,name)
    if result<=0:raise InvalidPhysicalModel(name+' must be positive')
    return result


def _eff(v,name):
    v=real(v,name,0,1)
    if v<=0:raise InvalidPhysicalModel(name+' must be >0')
    return v


def scenario_envelope(results:list[dict],weights:list[float]|None=None):
    """Empirical/scenario-weighted *stipulated* stress metrics, not reliability.

    Inputs: rows with exactly scenario_id, unserved_kWh, demand_kWh,
    critical_unserved_kWh. Weights normalized by caller. Missing scenarios
    or nonrepresentative weather do not justify interpreting expected values
    as a physical failure probability.
    """
    if not isinstance(results,list) or not 1<=len(results)<=512:raise InvalidPhysicalModel('1..512 scenario results')
    if weights is None:weights=[1/len(results)]*len(results)
    if not isinstance(weights,list) or len(weights)!=len(results):raise InvalidPhysicalModel('one weight per scenario')
    ws=[_nonneg(w,'scenario weight') for w in weights]
    if abs(fsum(ws)-1)>1e-9:raise InvalidPhysicalModel('weights must sum to 1; no silent normalization')
    ids=set();rows=[]
    for row,w in zip(results,ws):
        if not isinstance(row,dict) or set(row)!={'scenario_id','demand_kWh','unserved_kWh','critical_unserved_kWh'}:
            raise InvalidPhysicalModel('exact scenario fields required')
        sid=row['scenario_id']
        if not isinstance(sid,str) or not sid or sid in ids:raise InvalidPhysicalModel('unique scenario ID required')
        ids.add(sid)
        demand=_nonneg(row['demand_kWh'],'demand kWh');unserved=_nonneg(row['unserved_kWh'],'unserved kWh')
        critical=_nonneg(row['critical_unserved_kWh'],'critical unserved kWh')
        if critical>unserved+1e-9 or unserved>demand+1e-9:raise InvalidPhysicalModel('demand hierarchy inconsistent')
        rows.append({'id':sid,'weight':w,'demand_kWh':demand,'unserved_kWh':unserved,'critical_unserved_kWh':critical})
    mean=fsum(r['unserved_kWh']*r['weight'] for r in rows)
    outage_fraction=fsum(r['weight'] for r in rows if r['unserved_kWh']>1e-12)
    critical_mean=fsum(r['critical_unserved_kWh']*r['weight'] for r in rows)
    return {'schema':'atlas.energy-scenario-envelope/1','scenarios':len(rows),
            'scenario_weighted_unserved_kWh':mean,'scenario_weighted_critical_unserved_kWh':critical_mean,
            'fraction_of_supplied_scenario_weight_with_any_unserved_energy':outage_fraction,
            'worst_unserved_kWh':max(r['unserved_kWh'] for r in rows),
            'units':'kWh, dimensionless scenario fraction',
            'physical_outage_probability_estimated':False,
            'limitations':['Scenario weights are caller-selected, not a verified weather or outage probability distribution',
                           'Correlation of renewable, fuel, load and temperature conditions must be measured, not assumed independent',
                           'Battery or inverter safety, maintenance and medical continuity not assessed']}


def demand_generation_bounds(load_min_kW,load_max_kW,generation_min_kW,generation_max_kW,duration_h,*,reserve_kWh=0):
    """Interval-only energy residual. No probabilistic confidence assignment."""
    lo=_nonneg(load_min_kW,'minimum load');hi=_nonneg(load_max_kW,'maximum load')
    g_lo=_nonneg(generation_min_kW,'minimum generation');g_hi=_nonneg(generation_max_kW,'maximum generation')
    dt=_positive(duration_h,'duration');reserve=_nonneg(reserve_kWh,'reserve')
    if lo>hi or g_lo>g_hi:raise InvalidPhysicalModel('inverted bounds')
    return {'schema':'atlas.energy-supply-bounds/1',
        'minimum_energy_shortfall_before_storage_kWh':max(0.,(lo-g_hi)*dt),
        'maximum_energy_shortfall_before_storage_kWh':max(0.,(hi-g_lo)*dt),
        'guaranteed_available_reserve_kWh':reserve,
        'upper_bound_shortfall_after_ideal_reserve_kWh':max(0.,(hi-g_lo)*dt-reserve),
        'limitations':['Intervals are stipulated hard bounds not confidence intervals',
         'Reserve assumes 100% usable delivery here; actual battery efficiency/power limits reduce availability',
         'No power quality, startup, inverter dynamics, fuel availability or physical safety modeled']}


def heating_service_envelope(UA_W_K,periods:list[dict],thermal_efficiency=1.0):
    """Steady heat-loss service, excludes real building safety and ventilation."""
    ua=_nonneg(UA_W_K,'UA W per K');eta=_eff(thermal_efficiency,'thermal fraction')
    if not isinstance(periods,list) or not 1<=len(periods)<=8784:raise InvalidPhysicalModel('bounded thermal profile')
    data=[]
    for row in periods:
        if not isinstance(row,dict) or set(row)!={'inside_C','outside_C','hours','internal_gain_kW'}:
            raise InvalidPhysicalModel('thermal row requires 4 exact fields')
        t_in=real(row['inside_C'],'target Celsius');t_out=real(row['outside_C'],'outside Celsius')
        h=_positive(row['hours'],'interval hours');gain=_nonneg(row['internal_gain_kW'],'internal gain kW')
        useful=max(0.,ua*(t_in-t_out)/1000.-gain)*h
        data.append({'needed_useful_heat_kWh':useful,'input_heat_kWh':useful/eta,'hours':h})
    return {'schema':'atlas.energy-thermal-enclosure/1','periods':len(data),
         'useful_heat_kWh':fsum(x['needed_useful_heat_kWh'] for x in data),
         'input_heat_kWh':fsum(x['input_heat_kWh'] for x in data),
         'assumptions':['Prescribed constant UA and aggregate measured internal heat gain','No dynamic heat capacity or thermal bridge modeling'],
         'health_and_frost_protection_approved':False,
         'limitations':['No ventilation, infiltration, humidity, condensation, solar gain, calibration or indoor air quality model',
                        'A computed heat budget cannot certify combustion equipment, ventilation or safe shelter']}


def water_energy_boundary(volume_l,source_temp_C,target_temp_C,electrical_fraction,*,cp_j_kgK=4184,density_kg_l=1.0):
    """Sensible heating energy only; water potability can NOT be inferred."""
    v=_nonneg(volume_l,'volume liters');t1=real(source_temp_C,'source temperature');t2=real(target_temp_C,'target temperature')
    eta=_eff(electrical_fraction,'energy transferred to water')
    cp=_positive(cp_j_kgK,'specific heat');rho=_positive(density_kg_l,'density')
    if t2<t1:raise InvalidPhysicalModel('target below source for heating-only model')
    thermal=v*rho*cp*(t2-t1)
    return {'schema':'atlas.energy-water-thermal-boundary/1','liters':v,'useful_thermal_J':thermal,
        'input_electric_kWh':thermal/(eta*3.6e6),'density_kg_L':rho,
        'potability_verified':False,'biological_treatment_verified':False,
        'limitations':['Does not model phase change, vessel/ambient losses, altitude, or required boil duration',
                       'Heating energy does not make fuel- or chemical-contaminated water safe',
                       'Follow qualified public-health advice on water treatment; this model is not a treatment protocol']}


def _row(row,fields):
    if not isinstance(row,dict) or set(row)!=fields:raise InvalidPhysicalModel('incorrect interval fields')


def survival_service_ledger(profile:list[dict],initial_storage_kWh,storage_capacity_kWh,*,reserve_kWh,
                            discharge_limit_kW,charge_limit_kW,charge_efficiency=0.9,discharge_efficiency=0.9,
                            backup_output_limit_kW=0,backup_fuel_kWh=0,backup_electrical_efficiency=0.3):
    """Chronological *energy-only* service ledger; never operate physical equipment.

    Exactly critical_kW, flexible_kW, renewable_kW, hours per time row.
    Renewable serves critical then flexible demand. Storage discharges only
    remaining demand above reserve. Backup serves unmet demand with available
    chemical-fuel budget. Surplus renewable charges battery with losses.

    No simultaneous charge/discharge. No network, voltage, frequency, backfeed,
    inverter controls, battery-management, medical equipment or fire physics.
    """
    if not isinstance(profile,list) or not 1<=len(profile)<=8784:raise InvalidPhysicalModel('1..8784 intervals')
    cap=_positive(storage_capacity_kWh,'storage capacity');soc=_nonneg(initial_storage_kWh,'initial stored kWh')
    floor=_nonneg(reserve_kWh,'reserve kWh');maxdis=_nonneg(discharge_limit_kW,'max discharge power')
    maxch=_nonneg(charge_limit_kW,'max charge power');ech=_eff(charge_efficiency,'charge efficiency')
    edis=_eff(discharge_efficiency,'discharge efficiency');maxbackup=_nonneg(backup_output_limit_kW,'backup limit')
    fuel=_nonneg(backup_fuel_kWh,'chemical fuel input kWh');etab=_eff(backup_electrical_efficiency,'backup electrical efficiency')
    if floor>cap or soc>cap or soc<floor:raise InvalidPhysicalModel('initial storage outside declared reserve or capacity')
    start_soc=soc;start_fuel=fuel
    totals=dict(load_critical_kWh=0.,load_flexible_kWh=0.,renewable_generated_kWh=0.,
        served_critical_kWh=0.,served_flexible_kWh=0.,unserved_critical_kWh=0.,unserved_flexible_kWh=0.,
        backup_delivered_kWh=0.,battery_delivered_kWh=0.,battery_charged_kWh=0.,
        curtailed_renewable_kWh=0.,conversion_loss_kWh=0.,backup_fuel_consumed_kWh=0.)
    timeline=[]
    for idx,row in enumerate(profile):
        _row(row,{'critical_kW','flexible_kW','renewable_kW','hours'})
        hours=_positive(row['hours'],'hours');critical=_nonneg(row['critical_kW'],'critical')*hours
        flex=_nonneg(row['flexible_kW'],'flexible')*hours;renewable=_nonneg(row['renewable_kW'],'renewable')*hours
        demand=critical+flex
        # Generation is non-dispatchable here. Allocate energy to demand first.
        used_r=min(demand,renewable);remaining=demand-used_r
        used_storage=min(remaining,maxdis*hours,max(0.,soc-floor)*edis)
        removed_from_storage=used_storage/edis
        soc-=removed_from_storage
        if soc<floor and floor-soc<1e-10*max(1,cap):soc=floor
        remaining-=used_storage
        used_backup=min(remaining,maxbackup*hours,fuel*etab)
        burn=used_backup/etab
        fuel-=burn;remaining-=used_backup
        delivered=used_r+used_storage+used_backup
        critical_served=min(critical,delivered);flex_served=min(flex,max(0.,delivered-critical_served))
        unserved_critical=critical-critical_served;unserved_flexible=flex-flex_served
        unused_renewable=max(0.,renewable-used_r)
        charged_input=min(unused_renewable,maxch*hours,max(0.,cap-soc)/ech)
        stored_increase=charged_input*ech;soc+=stored_increase
        if soc>cap and soc-cap<1e-10*max(1,cap):soc=cap
        curtailed=max(0.,unused_renewable-charged_input)
        conversion_losses=removed_from_storage-used_storage+charged_input-stored_increase+burn-used_backup
        energy_residual=(renewable+burn+(start_soc if idx==0 else timeline[-1]['end_stored_kWh'])-(
           delivered+curtailed+conversion_losses+soc))
        if abs(energy_residual)>1e-8*max(1.,renewable+burn+demand+soc):raise AssertionError('energy balance violated')
        data={'step':idx,'hours':hours,'critical_demand_kWh':critical,'flexible_demand_kWh':flex,
            'renewable_kWh':renewable,'served_critical_kWh':critical_served,'served_flexible_kWh':flex_served,
            'unserved_critical_kWh':unserved_critical,'unserved_flexible_kWh':unserved_flexible,
            'battery_delivered_kWh':used_storage,'backup_delivered_kWh':used_backup,'fuel_consumed_kWh':burn,
            'charged_input_kWh':charged_input,'stored_increase_kWh':stored_increase,
            'end_stored_kWh':soc,'end_fuel_kWh':fuel,'curtailed_kWh':curtailed,
            'conversion_losses_kWh':conversion_losses,'energy_balance_residual_kWh':energy_residual}
        timeline.append(data)
        for k,v in {'load_critical_kWh':critical,'load_flexible_kWh':flex,'renewable_generated_kWh':renewable,
        'served_critical_kWh':critical_served,'served_flexible_kWh':flex_served,
        'unserved_critical_kWh':unserved_critical,'unserved_flexible_kWh':unserved_flexible,
        'backup_delivered_kWh':used_backup,'battery_delivered_kWh':used_storage,'battery_charged_kWh':stored_increase,
        'curtailed_renewable_kWh':curtailed,'conversion_loss_kWh':conversion_losses,
        'backup_fuel_consumed_kWh':burn}.items():totals[k]+=v
    total_load=totals['load_critical_kWh']+totals['load_flexible_kWh']
    total_served=totals['served_critical_kWh']+totals['served_flexible_kWh']
    total_unserved=totals['unserved_critical_kWh']+totals['unserved_flexible_kWh']
    return {'schema':'atlas.energy-v1-survival-services/1','intervals':len(timeline),'final_storage_kWh':soc,
         'final_fuel_chemical_kWh':fuel,'totals':totals,'timeline':timeline,
         'conservation_residual_kWh':(totals['renewable_generated_kWh']+(start_soc-soc)+totals['backup_fuel_consumed_kWh'])-(total_served+totals['curtailed_renewable_kWh']+totals['conversion_loss_kWh']),
         'load_balance_residual_kWh':total_load-total_served-total_unserved,
         'critical_coverage_fraction':totals['served_critical_kWh']/totals['load_critical_kWh'] if totals['load_critical_kWh'] else None,
         'electrical_installation_approved':False,'potable_water_service_verified':False,'medical_load_continuity_verified':False,
         'limitations':['Prescribed energy/interval accounting only; no instantaneous AC power flow or voltage/frequency/islanding',
           'Backup chemical input assumes perfect access to fuel and stable electrical efficiency; emissions and combustion safety omitted',
           'No startup surge, battery degradation, inverter protection, cable ratings or source reliability verification',
           'Critical-service labels are caller-declared priorities, NOT a medical or public-safety guarantee']}
