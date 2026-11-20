"""Reproducible author-constructed energy examples. None is an external experiment."""
from __future__ import annotations
from .models import *

def casebook():
    cases=[]
    def add(name,details,valid,limitations):
        cases.append({'id':name,'result':details,'passed':bool(valid),'origin':'author_constructed_physics_example',
                      'limits':limitations})
    c=unit_convert(1,'kWh','J');add('kwh-to-joules',{'J':c},c==3600000,'Unit conversion, not measurement')
    c=steady_energy_balance([1000],[250,600],150);add('first-law-closure',c,c['residual_j']==0,'Boundary assumed complete')
    c=steady_energy_balance([1000],[700],200);add('missing-loss-diagnostic',c,c['residual_j']==100,'Residual is not automatically identified as a specific physical loss')
    c=converter_efficiency(1000,700);add('ordinary-conversion-efficiency',c,c['efficiency']==.7,'Not heat pump COP')
    c=carnot_engine(500,300);add('carnot-reversible-ideal',c,abs(c['max_thermal_efficiency']-.4)<1e-12,'Upper bound in ideal reversible cycle')
    c=reversible_ideal_gas_work(1,300,.01,.02);add('isothermal-ideal-gas-work',c,c['work_by_gas_j']>0,'Ideal gas, reversible path')
    c=conduction_rate(1,2,.1,310,300);add('fourier-conduction-rate',{'W':c},abs(c-200)<1e-12,'1D steady conduction constant k')
    c=radiation_rate(1,1,400,300);add('stefan-boltzmann-net',{'W':c},abs(c-SIGMA*(400**4-300**4))<1e-9,'Blackbody view factor one')
    c=lumped_cooling(350,300,100,10,500,20,2);add('lumped-thermal-decay',c,300<c['temperature_K']<350,'Biot number limitation not checked')
    c=dc_ohms_law(V=12,R=6);add('ohms-law',c,c['current_A']==2 and c['power_W']==24,'Resistor assumed ohmic')
    c=rc_discharge(10,1,1,1);add('rc-discharge',c,c['voltage_V']<10 and c['energy_J']<50,'Lumped ideal RC')
    c=ac_single_phase(230,10,.8);add('ac-pf-and-reactive-power',c,abs(c['real_W']-1840)<1e-8,'Sinusoidal one-phase only')
    c=balanced_three_phase(400,10,1);add('three-phase-balanced',c,abs(c['real_W']-sqrt(3)*4000)<1e-7,'Balanced sinusoidal system')
    c=ideal_transformer(120,100,200,3);add('ideal-transformer',c,c['V_secondary']==240 and c['I_primary']==6,'Ignores saturation, faults, insulation and losses')
    c=line_resistive_loss(10,.2,2);add('i2r-line-loss',{'W':c},c==40,'Known conductor resistance and RMS current')
    c=solar_pv_power(1000,1000,45,-.004);add('pv-cell-temperature-effect',c,abs(c['dc_power_W']-920)<1e-10,'Linear DC module reference, not plant generation')
    c=wind_turbine_power(1.2,10,10,.4);add('wind-betz-bound',c,abs(c['ideal_extracted_W']-2400)<1e-10 and c['ideal_extracted_W']<=c['ideal_betz_W'],'Ideal steady actuator disk, excludes generator conversion')
    c=hydroelectric_power(1000,1,10,.8);add('hydraulic-gravitational-power',{'W':c},abs(c-78453.2)<1e-6,'Illustrative flow/head, not surveyed site')
    c=battery_step(5,10,1,charge_input_kW=2,eta_charge=.9);add('battery-charge-conservation',c,abs(c['stored_kWh']-6.8)<1e-10,'Nominal capacity unchanged, no degradation')
    c=battery_step(5,10,1,discharge_output_kW=2,eta_discharge=.8);add('battery-delivered-vs-stored',c,abs(c['stored_kWh']-2.5)<1e-10 and abs(c['loss_kWh']-.5)<1e-10,'Does not model BMS or temperature')
    try:battery_step(1,10,1,discharge_output_kW=2,eta_discharge=.9);rejected=False
    except InvalidPhysicalModel:rejected=True
    add('reject-unaccounted-battery-energy',{'rejected':rejected},rejected,'No silent clipping of requested discharge')
    c=capacity_factor(500,100,10);add('capacity-factor-finite-interval',{'factor':c},c==.5,'Not a generator efficiency')
    c=simple_levelized_cost(1000,[100]*10,[1000]*10,.05);add('illustrative-discounted-lcoe',c,c['currency_per_kWh']>0,'Synthetic costs, energy output and discount')
    c=nuclear_mass_energy(1e-9);add('mass-energy-equivalence',{'J':c},abs(c-1e-9*C_LIGHT*C_LIGHT)<1e-6,'Not a reactor design, yield prediction or nuclear safety model')
    c=piecewise_energy_j([0,10,20],[10,10,20]);add('sampled-energy-trapezoid',c,c['joules']==250,'Depends on interpolation and real sample rate')
    return {'schema':'atlas.energy-casebook/1','status':'passed' if all(i['passed'] for i in cases) else 'failed',
      'count':len(cases),'cases':cases,'real_physical_experiments':0,'independent_scientific_review':False}
