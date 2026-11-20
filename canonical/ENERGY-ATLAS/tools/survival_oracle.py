"""Separate NumPy arithmetic reference checks on invented survival-energy inputs.

No field measurements, equipment certification, source acquisition or actual
reliability distribution. A separate algorithm implementation checks accounting.
"""
import json,random,math,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from energy_atlas.survival_models import (water_lift_energy,heating_energy,shelter_heat_loss,
   fuel_to_delivered_electricity,emergency_load_allocation,energy_reserve_estimate,microgrid_profile)

rng=np.random.default_rng(131114)
counts={'water_lift':0,'sensible_heating':0,'shelter_heat':0,'fuel_account':0,'reserve_energy':0,'priority_allocation':0,'profile_energy_balance':0,'profile_unserved':0}
errmax=0.
def check(k,got,expected):
 global errmax
 if not all(math.isfinite(float(x)) for x in [got,expected]):raise AssertionError('nonfinite numeric oracle')
 error=abs(float(got)-float(expected));errmax=max(error,errmax)
 if error>1e-8*max(1.,abs(float(expected))):raise AssertionError(f'{k} mismatch {got=} {expected=}')
 counts[k]+=1

for _ in range(500):
 volume=float(rng.uniform(0,50));head=float(rng.uniform(0,100));eta=float(rng.uniform(.05,1))
 check('water_lift',water_lift_energy(volume,head,eta)['required_input_energy_j'],volume*head*1000*9.80665/eta)
 mass=float(rng.uniform(0,500));cp=float(rng.uniform(500,5000));T0=float(rng.uniform(-10,20));T1=float(rng.uniform(T0,100));e=float(rng.uniform(.05,1))
 check('sensible_heating',heating_energy(mass,cp,T0,T1,useful_fraction=e)['input_heat_j'],mass*cp*(T1-T0)/e)
 ua=float(rng.uniform(0,800));dh=float(rng.uniform(0,500))
 check('shelter_heat',shelter_heat_loss(ua,dh)['heat_loss_kWh'],ua*dh/1000)
 L=float(rng.uniform(0,50));MJ=float(rng.uniform(1,50));eff=float(rng.uniform(.05,.9))
 check('fuel_account',fuel_to_delivered_electricity(L,MJ,eff)['electricity_at_assumed_efficiency_kWh'],L*MJ*eff/3.6)
 daily=float(rng.uniform(.01,100));cap=float(rng.uniform(1,500));soc=float(rng.uniform(.3,1));floor=float(rng.uniform(0,soc));dis=float(rng.uniform(.1,1))
 check('reserve_energy',energy_reserve_estimate(daily,cap,soc,floor,dis)['usable_delivered_kWh'],(soc-floor)*cap*dis)

for _ in range(250):
 n=int(rng.integers(1,9));power=float(rng.uniform(0,10))
 rows=[]
 for i in range(n):rows.append({'service_id':f'S{i}','priority':int(rng.integers(0,4)),'requested_kW':float(rng.uniform(0,6)),'minimum_kW':0.})
 got=emergency_load_allocation(rows,power)
 # Independent vector group scaling, not the implementation's per-service loop.
 pr=np.array([r['priority'] for r in rows]);demand=np.array([r['requested_kW'] for r in rows])
 used=0.;out=np.zeros(n)
 for k in sorted(set(pr)):
  mask=(pr==k);requested=float(np.sum(demand[mask]));alloc=min(max(0,power-used),requested)
  if requested>0:out[mask]=demand[mask]*alloc/requested
  used+=float(np.sum(out[mask]))
 for i,row in enumerate(rows):check('priority_allocation',got['services'][row['service_id']]['served_kW'],out[i])

for _ in range(500):
 n=int(rng.integers(1,11));profile=[]
 for i in range(n):
  profile.append({'load_kW':float(rng.uniform(0,15)),'renewable_kW':float(rng.uniform(0,15)),
   'dt_hours':float(rng.uniform(.1,2.)),'grid_available':bool(rng.integers(0,2))})
 cap=float(rng.uniform(1,20));start=float(rng.uniform(0,cap));chg=float(rng.uniform(0,6));dis=float(rng.uniform(0,6))
 ec=float(rng.uniform(.3,1));ed=float(rng.uniform(.3,1))
 got=microgrid_profile(profile,start,cap,charge_limit_kW=chg,discharge_limit_kW=dis,eta_charge=ec,eta_discharge=ed)
 check('profile_energy_balance',got['totals']['energy_balance_residual_kWh'],0)
 # Independent secondary state machine only for unserved-load calculation.
 stored=start;unserved=0.
 for row in profile:
  demand=row['load_kW'];generation=row['renewable_kW'];dt=row['dt_hours']
  delta=generation-demand
  if delta>=0:stored+=min(delta,chg,(cap-stored)/(dt*ec))*dt*ec
  else:
   output=min(-delta,dis,stored*ed/dt)
   stored-=output*dt/ed
   if not row['grid_available']:unserved+=max(0.,-delta-output)*dt
  stored=np.clip(stored,0,cap)
 check('profile_unserved',got['totals']['unserved_kWh'],unserved)

result={'schema':'atlas.energy-survival-oracle/1','result':'passed','comparisons':sum(counts.values()),'counts':counts,
  'seed':131114,'max_absolute_error':errmax,'numpy_version':np.__version__,
  'source':'independently implemented author-created examples','real_equipment_operated':False,
  'statistical_outage_probability_inferred':False,'independent_scientific_review':False}
print(json.dumps(result,indent=2))
if len(sys.argv)>1:Path(sys.argv[1]).write_text(json.dumps(result,indent=2)+'\n')
