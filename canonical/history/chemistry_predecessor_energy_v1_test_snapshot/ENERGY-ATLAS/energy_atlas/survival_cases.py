"""Reproducible constructed survival-energy studies; never real-world certification."""
from .survival_models import *
from .models import InvalidPhysicalModel

def casebook_survival():
    cases=[]
    def add(name,out,ok,limit):cases.append({'id':name,'origin':'constructed_stipulated_offline_case',
         'status':'passed' if ok else 'failed','passed':bool(ok),'output':out,'limitations':limit})
    x=water_lift_energy(1,10,.5)
    add('gravity-water-lifting',x,abs(x['required_input_energy_j']-196133)<1e-7,
        'Not potable-water validation, pump sizing or wiring')
    x=heating_energy(2,4184,15,60,useful_fraction=.8)
    add('water-sensible-heat',x,abs(x['useful_heat_j']-376560)<1e-6,
       'Not water disinfection or safe cooking')
    x=shelter_heat_loss(150,120)
    add('shelter-degree-hours',x,x['heat_loss_kWh']==18,'UA and degree-hours are authored values; not real building audit')
    x=fuel_to_delivered_electricity(5,35,.25)
    add('generator-energy-account',x,abs(x['electricity_at_assumed_efficiency_kWh']-12.152777777777779)<1e-10,
        'No combustion, generator connection or indoor fuel use authorized')
    services=[{'service_id':'water','priority':1,'requested_kW':.5,'minimum_kW':.5},
              {'service_id':'lights','priority':2,'requested_kW':.2,'minimum_kW':.1},
              {'service_id':'heating','priority':2,'requested_kW':1.8,'minimum_kW':1.0}]
    x=emergency_load_allocation(services,1)
    add('priority-power-budget',x,abs(x['served_kW']-1)<1e-10 and not x['all_declared_minima_met'],
        'Mathematical proportional sharing is not a safety/critical-load control plan')
    x=energy_reserve_estimate(2,10,.75,.25,.9)
    add('battery-reserve-sensitivity',x,abs(x['illustrative_days_at_constant_daily_load']-2.25)<1e-12,
        'No field autonomy guarantee, standby losses or BMS constraints')
    profile=[
      {'load_kW':2,'renewable_kW':4,'dt_hours':1,'grid_available':False},
      {'load_kW':3,'renewable_kW':0,'dt_hours':1,'grid_available':False},
      {'load_kW':3,'renewable_kW':0,'dt_hours':1,'grid_available':False}]
    x=microgrid_profile(profile,1,4,charge_limit_kW=2,discharge_limit_kW=2,eta_charge=.9,eta_discharge=.9)
    add('microgrid-multiday-ledger',x,x['totals']['energy_balance_residual_kWh']<1e-10 and x['totals']['unserved_kWh']>0,
        'No actual protection, islanding, BMS, inverter, AC stability or weather observations')
    x=microgrid_profile([{'load_kW':1,'renewable_kW':0,'dt_hours':1,'grid_available':True}],.1,5,
         charge_limit_kW=1,discharge_limit_kW=1)
    add('grid-up-import-ledger',x,x['totals']['unserved_kWh']==0 and x['totals']['imported_kWh']>0,
        'Assumes unlimited external grid during indicated availability')
    x=evaluate_survival_scenarios([
       {'scenario_id':'windy','profile':[{'load_kW':1,'renewable_kW':2,'dt_hours':2,'grid_available':False}]},
       {'scenario_id':'calm','profile':[{'load_kW':3,'renewable_kW':0,'dt_hours':2,'grid_available':False}]}],
       0,2,charge_limit_kW=2,discharge_limit_kW=2)
    add('outage-scenarios-adverse-weather',x,x['worst_supplied_unserved_energy']['scenario_id']=='calm',
        'The worst of two invented scenarios is not the worst possible real storm')
    try:water_lift_energy(1,10,0);refused=True
    except InvalidPhysicalModel:refused=True
    else:refused=False
    add('invalid-pump-efficiency-refused',{'refused':refused},refused,'Bounded input validation only')
    try:emergency_load_allocation([{'service_id':'x','priority':1,'requested_kW':1,'minimum_kW':2}],1);refused=True
    except InvalidPhysicalModel:refused=True
    else:refused=False
    add('invalid-critical-demand-refused',{'refused':refused},refused,'No medical or safety certification')
    return {'schema':'atlas.energy-survival-casebook/1','count':len(cases),
      'status':'passed' if all(x['passed'] for x in cases) else 'failed','cases':cases,
      'real_installed_equipment_tested':False,'independent_field_review':False,
      'power_system_operated':False,'actual_survival_outcomes_observed':False}
