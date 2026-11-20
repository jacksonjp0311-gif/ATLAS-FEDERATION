"""Independent NumPy arithmetic oracle, not an empirical grid validation."""
import json,random,math,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from energy_atlas.survival_v1 import scenario_envelope,demand_generation_bounds,heating_service_envelope,water_energy_boundary,survival_service_ledger

rng=random.Random(20261114)
counts={}; max_error=0.
def compare(label,a,b,tol=1e-9):
    global max_error
    e=abs(float(a)-float(b));max_error=max(max_error,e)
    if e>tol*max(1.,abs(float(a)),abs(float(b))):raise AssertionError((label,a,b,e))
    counts[label]=counts.get(label,0)+1

for n in range(650):
    count=rng.randint(1,20)
    ws=np.array([rng.random()+.01 for _ in range(count)]);ws/=ws.sum()
    demands=np.array([rng.random()*100 for _ in range(count)])
    missing=np.array([rng.random()*demands[i] for i in range(count)])
    cmiss=np.array([rng.random()*missing[i] for i in range(count)])
    rows=[{'scenario_id':str(i),'demand_kWh':float(demands[i]),'unserved_kWh':float(missing[i]),'critical_unserved_kWh':float(cmiss[i])} for i in range(count)]
    r=scenario_envelope(rows,ws.tolist())
    compare('scenario_weighted_unserved',r['scenario_weighted_unserved_kWh'],np.dot(ws,missing))
    compare('scenario_weighted_critical',r['scenario_weighted_critical_unserved_kWh'],np.dot(ws,cmiss))
    compare('scenario_outage_weight',r['fraction_of_supplied_scenario_weight_with_any_unserved_energy'],np.sum(ws[missing>1e-12]))

for _ in range(720):
    lo=rng.random()*20;hi=lo+rng.random()*10;glo=rng.random()*10;ghi=glo+rng.random()*10;dt=rng.random()*10+.01;res=rng.random()*5
    r=demand_generation_bounds(lo,hi,glo,ghi,dt,reserve_kWh=res)
    compare('interval_shortfall_lower',r['minimum_energy_shortfall_before_storage_kWh'],np.maximum(0.,(lo-ghi)*dt))
    compare('interval_shortfall_upper',r['maximum_energy_shortfall_before_storage_kWh'],np.maximum(0.,(hi-glo)*dt))
    compare('interval_reserve_upper',r['upper_bound_shortfall_after_ideal_reserve_kWh'],np.maximum(0.,(hi-glo)*dt-res))

for _ in range(420):
    periods=[];count=rng.randint(1,15);ua=rng.random()*500+1;eff=rng.random()*.7+.3
    for j in range(count):periods.append({'inside_C':rng.uniform(0,35),'outside_C':rng.uniform(-20,40),'hours':rng.random()*24+.01,'internal_gain_kW':rng.random()*2})
    r=heating_service_envelope(ua,periods,thermal_efficiency=eff)
    arr=np.array([[p[k] for k in ('inside_C','outside_C','hours','internal_gain_kW')] for p in periods])
    expected=np.sum(np.maximum(0,ua*(arr[:,0]-arr[:,1])/1000-arr[:,3])*arr[:,2])/eff
    compare('steady_envelope_input_heat',r['input_heat_kWh'],expected)

for _ in range(420):
    liters=rng.random()*100;temp=rng.uniform(0,50);delta=rng.random()*80;eta=.2+rng.random()*.8;cp=rng.uniform(3800,4400)
    r=water_energy_boundary(liters,temp,temp+delta,eta,cp_j_kgK=cp)
    compare('water_sensible_input',r['input_electric_kWh'],liters*cp*delta/(3.6e6*eta))

for _ in range(620):
    cap=rng.random()*15+2;floor=rng.random()*.3*cap;init=floor+(cap-floor)*rng.random()
    echarge=rng.random()*.5+.5;edis=rng.random()*.5+.5;eta=rng.random()*.55+.25
    p=[{'critical_kW':rng.random()*5,'flexible_kW':rng.random()*4,'renewable_kW':rng.random()*6,'hours':rng.random()*2+.1} for i in range(rng.randint(1,20))]
    charge=rng.random()*7;dis=rng.random()*7;maxback=rng.random()*4;fuel=rng.random()*50;old_fuel=fuel
    ref=survival_service_ledger(p,init,cap,reserve_kWh=floor,charge_limit_kW=charge,discharge_limit_kW=dis,charge_efficiency=echarge,discharge_efficiency=edis,backup_output_limit_kW=maxback,backup_fuel_kWh=fuel,backup_electrical_efficiency=eta)
    energy=np.float64(init);misscritical=missflex=curtail=0.
    for row in p:
        h=row['hours'];critical=row['critical_kW']*h;flex=row['flexible_kW']*h;renew=row['renewable_kW']*h
        first=min(critical+flex,renew)
        short=max(0.,critical+flex-first)
        battery=min(short,dis*h,max(0.,energy-floor)*edis)
        energy-=battery/edis;short-=battery
        backup=min(short,maxback*h,fuel*eta)
        fuel-=backup/eta;short-=backup
        served=first+battery+backup
        misscritical+=max(0.,critical-served)
        missflex+=max(0.,flex-max(0.,served-critical))
        surplus=max(0.,renew-first)
        charge_in=min(surplus,charge*h,max(0.,cap-energy)/echarge)
        energy+=charge_in*echarge
        curtail+=max(0.,surplus-charge_in)
    compare('microgrid_terminal_storage',ref['final_storage_kWh'],energy)
    compare('microgrid_terminal_fuel',ref['final_fuel_chemical_kWh'],fuel)
    compare('microgrid_critical_shortfall',ref['totals']['unserved_critical_kWh'],misscritical)
    compare('microgrid_flexible_shortfall',ref['totals']['unserved_flexible_kWh'],missflex)
    compare('microgrid_renewable_curtailment',ref['totals']['curtailed_renewable_kWh'],curtail)
    compare('microgrid_energy_conservation',ref['conservation_residual_kWh'],0)
report={'schema':'atlas.energy-v1-independent-oracle/1','result':'passed',
    'comparisons':sum(counts.values()),'counts':counts,'max_abs_error':max_error,
    'seed':20261114,'numpy':np.__version__,
    'source':'independently written NumPy arithmetic on author-generated synthetic inputs',
    'real_world_performance_evaluated':False,'original_field_measurements':0,
    'limitations':['Cannot validate field devices, electrical protection, water sanitation or source credibility',
        'Stipulated scenarios are neither real weather probability models nor physical failure experiments']}
print(json.dumps(report,indent=2))
if len(sys.argv)>1:Path(sys.argv[1]).write_text(json.dumps(report,indent=2)+'\n')
