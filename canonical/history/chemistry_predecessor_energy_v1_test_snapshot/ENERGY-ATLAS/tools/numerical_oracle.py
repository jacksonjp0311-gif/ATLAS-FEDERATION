"""Independent NumPy checks of synthetic energy equations.

Zero real experiments, energy devices, or expert reviews. A passing case shows
model/code arithmetic consistency; physics applicability remains conditional.
"""
import json,sys,random,math
from pathlib import Path
import numpy as np
from energy_atlas.models import (solar_pv_power,wind_turbine_power,radiation_rate,
  carnot_engine,battery_step,microgrid_interval_dispatch,simple_levelized_cost,
  piecewise_energy_j,ac_single_phase,unit_convert,capacity_factor,BETZ_MAX,SIGMA)
seed=102026; rng=random.Random(seed);counts={};error=0.
def check(category,a,b,tol=2e-11):
 global error
 if not math.isfinite(float(a)) or not math.isfinite(float(b)):raise AssertionError('nonfinite')
 err=abs(float(a)-float(b));error=max(error,err)
 if err>tol*max(1.,abs(float(a)),abs(float(b))):raise AssertionError(f'{category}: {a=} {b=}')
 counts[category]=counts.get(category,0)+1
for i in range(1000):
 G=rng.uniform(0,1200);nameplate=rng.uniform(0,2500);T=rng.uniform(-30,80);gamma=-rng.uniform(0,.01)
 check('solar_linear_model',solar_pv_power(nameplate,G,T,gamma)['dc_power_W'],float(np.multiply(G/1000,nameplate)*(1+gamma*(T-25))))
 rho=rng.uniform(.8,1.3);A=rng.uniform(0,500);v=rng.uniform(0,20);cp=rng.uniform(0,BETZ_MAX)
 check('wind_kinetic_power',wind_turbine_power(rho,A,v,cp)['ideal_extracted_W'],float(np.multiply.reduce([.5,rho,A,v**3,cp])))
 eps=rng.uniform(0,1);area=rng.uniform(0,20);t1=rng.uniform(1,700);t2=rng.uniform(1,700)
 check('thermal_radiation',radiation_rate(eps,area,t1,t2),float(np.multiply.reduce([SIGMA,eps,area,t1**4-t2**4])))
 cold=rng.uniform(200,400);hot=cold+rng.uniform(.1,1000)
 check('carnot_limit',carnot_engine(hot,cold)['max_thermal_efficiency'],float(1-np.divide(cold,hot)))
 kw=rng.uniform(.1,1000);h=rng.uniform(.1,8000);e=rng.uniform(0,kw*h)
 check('capacity_factor',capacity_factor(e,kw,h),float(np.divide(e,kw*h)))
 V=rng.uniform(0,700);I=rng.uniform(0,100);pf=rng.uniform(-1,1)
 check('ac_real_power',ac_single_phase(V,I,pf)['real_W'],float(np.multiply.reduce([V,I,pf])))
 value=rng.uniform(0,15000)
 check('energy_unit_conversion',unit_convert(value,'kWh','J'),float(np.multiply(value,3.6e6)))
 cap=rng.uniform(1,50);E=rng.uniform(0,cap);dt=rng.uniform(.01,1)
 eta=rng.uniform(.6,1)
 if rng.random()<.5:
  power=rng.uniform(0,(cap-E)/(dt*eta))
  got=battery_step(E,cap,dt,charge_input_kW=power,eta_charge=eta)
  expect=E+power*dt*eta
 else:
  power=rng.uniform(0,E*eta/dt)
  got=battery_step(E,cap,dt,discharge_output_kW=power,eta_discharge=eta)
  expect=E-power*dt/eta
 check('battery_energy_update',got['stored_kWh'],expect)
 a=rng.uniform(0,3000);b=rng.uniform(0,3000);soc=rng.uniform(0,10)
 g=microgrid_interval_dispatch(a,b,soc,10,dt,10,10,.87,.82,grid_available=bool(i%2))
 check('microgrid_energy_residual',g['balance_residual_kWh'],0.,tol=1e-9)
 times=np.cumsum(np.asarray([0.,rng.uniform(1,20),rng.uniform(1,20),rng.uniform(1,20)]))
 vals=np.asarray([rng.uniform(0,100) for j in range(4)])
 got=piecewise_energy_j(times.tolist(),vals.tolist())['joules']
 expected=float(np.sum(np.diff(times)*(vals[:-1]+vals[1:])/2))
 check('trapezoid_numpy',got,expected)
 # present-value ratio recomputed as dot product on NumPy array
 n=5;annual=np.array([rng.uniform(0,100) for k in range(n)]);eng=np.array([rng.uniform(1,1000) for k in range(n)])
 rate=rng.uniform(0,.2);capital=rng.uniform(0,1000)
 expected=float((capital+np.sum(annual/(1+rate)**np.arange(1,n+1)))/np.sum(eng/(1+rate)**np.arange(1,n+1)))
 got=simple_levelized_cost(capital,annual.tolist(),eng.tolist(),rate)['currency_per_kWh']
 check('discounted_lcoe_numpy',got,expected)
report={'schema':'atlas.energy-numerical-oracle/1','status':'passed','comparisons':sum(counts.values()),
        'categories':counts,'seed':seed,'max_absolute_error':error,'numpy_version':np.__version__,
        'real_physical_measurements':0,'original_primary_source_rows':0,
        'independent_human_scientific_review':False,
        'claim':'independent vector arithmetic on author-generated finite examples; not validation of model applicability, safe equipment, actual economics, or unknown efficiency gains'}
Path(__file__).resolve().parents[1].joinpath('evidence/numerical_oracle_v0.1.0.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
