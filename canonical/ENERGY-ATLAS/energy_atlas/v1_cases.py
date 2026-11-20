"""Original Energy v1 finite casebook; no laboratory equipment tested."""
from .survival_v1 import *


def casebook_v1():
    cases=[]
    def add(name,value,ok):
        cases.append({'id':name,'status':'passed' if ok else 'failed','output':value,
                     'origin':'original_constructed_offline_case','physical_evidence':False})
    r=scenario_envelope([{'scenario_id':'A','demand_kWh':20,'unserved_kWh':0,'critical_unserved_kWh':0},
       {'scenario_id':'B','demand_kWh':20,'unserved_kWh':10,'critical_unserved_kWh':2}],[.8,.2])
    add('conditional scenario weighting',r,abs(r['scenario_weighted_unserved_kWh']-2)<1e-12 and not r['physical_outage_probability_estimated'])
    r=demand_generation_bounds(1,3,.2,2,4,reserve_kWh=2)
    add('bounded demand and generation',r,abs(r['maximum_energy_shortfall_before_storage_kWh']-11.2)<1e-12)
    r=heating_service_envelope(200,[{'inside_C':20,'outside_C':0,'hours':10,'internal_gain_kW':0}],thermal_efficiency=.8)
    add('thermal shelter energy',r,abs(r['input_heat_kWh']-50)<1e-12)
    r=water_energy_boundary(10,20,70,.8)
    add('water sensible energy',r,abs(r['input_electric_kWh']-(10*4184*50/.8/3.6e6))<1e-12 and not r['potability_verified'])
    base={'critical_kW':1,'flexible_kW':1,'renewable_kW':0,'hours':1}
    r=survival_service_ledger([base],2,3,reserve_kWh=.5,discharge_limit_kW=1,charge_limit_kW=1)
    add('critical priority and flexible unserved',r,r['totals']['served_critical_kWh']==1 and abs(r['totals']['unserved_flexible_kWh']-1)<1e-12 and abs(r['conservation_residual_kWh'])<1e-12)
    r=survival_service_ledger([{'critical_kW':1,'flexible_kW':0,'renewable_kW':5,'hours':1}],0,3,reserve_kWh=0,discharge_limit_kW=1,charge_limit_kW=2)
    add('renewable storage and curtailment',r,abs(r['totals']['battery_charged_kWh']-1.8)<1e-12 and abs(r['totals']['curtailed_renewable_kWh']-2)<1e-12)
    r=survival_service_ledger([base],.5,3,reserve_kWh=.5,discharge_limit_kW=2,charge_limit_kW=0,backup_output_limit_kW=2,backup_fuel_kWh=10)
    add('backup fuel accounting',r,abs(r['totals']['backup_delivered_kWh']-2)<1e-12 and abs(r['totals']['backup_fuel_consumed_kWh']-2/.3)<1e-12)
    r=survival_service_ledger([base],.5,3,reserve_kWh=.5,discharge_limit_kW=2,charge_limit_kW=0,backup_output_limit_kW=2,backup_fuel_kWh=0)
    add('zero available electricity',r,r['totals']['unserved_critical_kWh']==1 and r['totals']['unserved_flexible_kWh']==1)
    r=survival_service_ledger([{'critical_kW':0,'flexible_kW':0,'renewable_kW':4,'hours':1}],.5,3,reserve_kWh=.5,discharge_limit_kW=0,charge_limit_kW=4)
    add('charge capacity saturation',r,abs(r['final_storage_kWh']-3)<1e-12 and r['totals']['curtailed_renewable_kWh']>1)
    r=survival_service_ledger([base]*3,2,3,reserve_kWh=.5,discharge_limit_kW=2,charge_limit_kW=2)
    add('finite battery exhaustion',r,abs(r['final_storage_kWh']-.5)<1e-12 and r['totals']['unserved_critical_kWh']>1)
    for name,call in [('negative solar power',lambda:survival_service_ledger([{'critical_kW':1,'flexible_kW':0,'renewable_kW':-1,'hours':1}],1,2,reserve_kWh=0,discharge_limit_kW=1,charge_limit_kW=1)),
       ('invalid scenario weights',lambda:scenario_envelope([{'scenario_id':'A','demand_kWh':1,'unserved_kWh':1,'critical_unserved_kWh':0}],[.1])),
       ('invalid thermal interval',lambda:heating_service_envelope(2,[{'inside_C':20,'outside_C':0,'hours':0,'internal_gain_kW':0}])),
       ('water not cooling model',lambda:water_energy_boundary(2,50,10,1)),
       ('invalid storage state',lambda:survival_service_ledger([base],4,3,reserve_kWh=0,discharge_limit_kW=1,charge_limit_kW=1))]:
        refused=False
        try:call()
        except InvalidPhysicalModel:refused=True
        add(name+' refused',{'refused':refused},refused)
    return {'schema':'atlas.energy-v1-synthetic-casebook/1','status':'passed' if all(c['status']=='passed' for c in cases) else 'failed',
       'count':len(cases),'cases':cases,'verified_field_performance':False,'actual_water_potability_verified':False,
       'physical_installation_or_protection_approved':False}
