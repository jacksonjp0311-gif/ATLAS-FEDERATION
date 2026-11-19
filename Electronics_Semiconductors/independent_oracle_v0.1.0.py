#!/usr/bin/env python3
"""Independent Decimal/math comparisons on authored synthetic Electronics fixtures."""
import sys,random,math,json
from decimal import Decimal,localcontext
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from electronics_atlas import models as m

def D(x):return Decimal(str(x))

def run():
 r=random.Random(20261116);checks=0;worst=0.;groups={}
 def verify(key,got,expected,rtol=1e-10,atol=1e-14):
  nonlocal checks,worst
  a=float(got);b=float(expected)
  if not math.isfinite(a) or not math.isfinite(b) or abs(a-b)>atol+rtol*abs(b):raise AssertionError((key,a,b,abs(a-b)))
  checks+=1;groups[key]=groups.get(key,0)+1
  if b:worst=max(worst,abs((a-b)/b))
 with localcontext() as cx:
  cx.prec=70
  q=D(m.Q); k=D(m.K_B); e0=D(m.EPSILON_0_APPROX)
  for _ in range(100):
   T=250+r.random()*300
   verify('thermal_voltage',m.thermal_voltage(T),k*D(T)/q)
   ni=10**r.uniform(13,17);d=r.choice((-1,1))*10**r.uniform(17,23)
   radical=(D(d)**2+4*D(ni)**2).sqrt()
   n=(D(d)+radical)/2;p=(radical-D(d))/2
   verify('electron_density',m.mass_action_carriers(d,ni)[0],n,rtol=2e-9)
   verify('hole_density',m.mass_action_carriers(d,ni)[1],p,rtol=2e-9)
   na=10**r.uniform(20,23);nd=10**r.uniform(20,23)
   tv=k*D(T)/q;vbi=tv*((D(na)/D(ni)).ln()+(D(nd)/D(ni)).ln())
   verify('junction_built_in',m.built_in_potential(na,nd,ni,T),vbi)
   eps=3+r.random()*11;vapp=-.5*r.random();width=(2*e0*D(eps)/q*(1/D(na)+1/D(nd))*(vbi-D(vapp))).sqrt()
   verify('depletion_width',m.depletion_width(na,nd,ni,eps,T,vapp),width)
   Is=10**r.uniform(-13,-7);bias=r.uniform(-.16,.16);ideality=r.uniform(1,2)
   current=D(Is)*((D(bias)/(D(ideality)*tv)).exp()-1)
   verify('diode_current',m.diode_current(Is,bias,T,ideality),current,rtol=1e-10,atol=1e-17)
   verify('diode_inverse',m.diode_voltage_from_current(Is,float(current),T,ideality),bias,rtol=2e-10,atol=1e-12)
   cap_area=10**r.uniform(-13,-9);thickness=10**r.uniform(-9,-7)
   verify('mos_cap',m.mos_gate_capacitance(eps,cap_area,thickness),e0*D(eps)*D(cap_area)/D(thickness))
   R=10**r.uniform(2,6);C=10**r.uniform(-13,-8);t=r.random()*3*R*C
   init=r.uniform(-1,1);supply=r.uniform(-1,2)
   vd=D(init)+(D(supply)-D(init))*(1-(-D(t)/(D(R)*D(C))).exp())
   verify('rc_step',m.rc_step(init,supply,R,C,t),vd,rtol=1e-10,atol=1e-13)
   kappa=10**r.uniform(-5,-2);vth=r.uniform(.15,1);vg=vth+r.uniform(0,2);vds=r.uniform(0,2)
   ov=max(0,vg-vth)
   current_m=(D(kappa)*(D(ov)*D(vds)-D(vds)**2/2) if vds<=ov else D(kappa)*D(ov)**2/2)
   verify('mosfet_regions',m.ideal_nmos_current(kappa,vg,vds,vth),current_m,rtol=1e-10,atol=1e-16)
   activity=r.random();f=10**r.uniform(5,9)
   verify('switch_dynamic_power',m.switch_dynamic_power(C,abs(supply),f,activity),D(C)*D(abs(supply))**2*D(f)*D(activity))
  for _ in range(100):
   n=r.randint(3,16);spacing=10**r.uniform(-8,-2)
   edges=[r.uniform(-1,1) for _ in range(n+1)]
   div=m.current_divergence_1d(edges,spacing)
   verify('continuity_telescoping',sum(div)*spacing,edges[-1]-edges[0],rtol=1e-8,atol=1e-11)
 for a in (0,1):
  verify('logic_not',m.logic_not(a),1-a)
  for b in (0,1):
   verify('logic_nand',m.logic_nand(a,b),1-a*b)
   verify('logic_nor',m.logic_nor(a,b),1-int(bool(a or b)))
 return {'schema':'atlas.electronics-independent-oracle/1','result':'passed','numeric_compared_values':checks,
   'groups':groups,'max_relative_difference':worst,'seed':20261116,
   'claim':'synthetic numerical software comparisons only; no laboratory, transport authentication or independent expert review'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
