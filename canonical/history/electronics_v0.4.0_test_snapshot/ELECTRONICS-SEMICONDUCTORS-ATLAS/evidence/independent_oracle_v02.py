#!/usr/bin/env python3
"""Independent NumPy/SciPy/mpmath numerical comparisons for original ATLAS FORGE Electronics v0.2.
Oracle independently assembles matrices and analytic equations; no outside physical data.
"""
import json,random,math,sys
from pathlib import Path
import numpy as np
import mpmath as mp
from scipy.optimize import brentq
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from electronics_atlas.v02_models import (bernoulli_stable,sg_electron_current,
  minority_diffusion_profile,minority_analytic,resistor_network,ideal_cmos_inverter_output,
  ripple_adder_unsigned,diode_current_local_uncertainty)
from electronics_atlas.models import Q,K_B,ideal_nmos_current
rng=random.Random(20261116)
mp.mp.dps=80
counts={};errors={}; max_error=0.
def check(label,got,want,rtol=1e-9,atol=1e-12):
 global max_error
 if not(math.isfinite(float(got)) and math.isfinite(float(want))):raise AssertionError('nonfinite '+label)
 diff=abs(float(got)-float(want));max_error=max(max_error,diff)
 if diff>atol+rtol*max(abs(float(want)),abs(float(got))):
  raise AssertionError(f'{label}: {got} != {want} diff={diff}')
 counts[label]=counts.get(label,0)+1
 errors[label]=max(errors.get(label,0),diff)

for _ in range(350):
 z=rng.uniform(-200,200)
 rz=mp.mpf(str(z)); exact=float(rz/mp.expm1(rz))
 check('bernoulli_mp80',bernoulli_stable(z),exact,rtol=2e-13,atol=1e-200)

for _ in range(260):
 nL=10**rng.uniform(15,21); nR=10**rng.uniform(15,21)
 L=10**rng.uniform(-8,-5);T=rng.uniform(260,400);mu=10**rng.uniform(-4,-.5)
 Pe=rng.uniform(-24,24)
 field=-Pe*(K_B*T/Q)/L
 vt=mp.mpf(str(K_B))*mp.mpf(str(T))/mp.mpf(str(Q))
 d=mp.mpf(str(mu))*vt
 # Direct high-precision exact solution using exponential boundary conditions.
 ex=mp.exp(mp.mpf(str(Pe)))
 nLmp=mp.mpf(str(nL)); nRmp=mp.mpf(str(nR))
 F=(d/mp.mpf(str(L)))*mp.mpf(str(Pe))*(ex*nLmp-nRmp)/(ex-1) if abs(Pe)>1e-14 else (d/mp.mpf(str(L)))*(nLmp-nRmp)
 exact=float(-mp.mpf(str(Q))*F)
 got=sg_electron_current(nL,nR,field,L,mu,T)
 check('sg_constant_field_mp80',got,exact,rtol=2e-11,atol=1e-6)

for _ in range(90):
 n=rng.randrange(8,50); L=10**rng.uniform(-6,-4);D=10**rng.uniform(-4,-2);tau=10**rng.uniform(-8,-5)
 l=rng.random()*2.;r=rng.random()*2.;p=minority_diffusion_profile(l,r,L,D,tau,n)
 h=L/n;r2=h*h/(D*tau)
 A=np.diag(np.full(n-1,2+r2)) + np.diag(np.full(n-2,-1.),1)+ np.diag(np.full(n-2,-1.),-1)
 b=np.zeros(n-1);b[0]+=l;b[-1]+=r
 v=np.linalg.solve(A,b)
 for a,b0 in zip(p['density_m3'][1:-1],v):check('minority_independent_dense',a,b0,rtol=2e-9,atol=1e-10)
 check('minority_conservation',p['particle_flux_m2_s'][-1]-p['particle_flux_m2_s'][0]+p['integrated_recombination_m2_s'],0,atol=max(1e-8,abs(p['particle_flux_m2_s'][0])*1e-9))

for _ in range(130):
 nodes=rng.randint(3,12);edges=[]
 for i in range(1,nodes):edges.append((i-1,i,10**rng.uniform(1,5)))
 for j in range(nodes//2):
  a,b=rng.sample(range(nodes),2);edges.append((a,b,10**rng.uniform(1,5)))
 fixed={0:rng.uniform(-3,3)}
 injection={i:rng.uniform(-.0002,.0002) for i in range(1,nodes)}
 sol=resistor_network(nodes,edges,fixed,injection)
 A=np.zeros((nodes-1,nodes-1));rhs=np.array([injection[i] for i in range(1,nodes)])
 for a,b,R in edges:
  g=1./R
  for x,y in ((a,b),(b,a)):
   if x!=0:
    A[x-1,x-1]+=g
    if y!=0:A[x-1,y-1]-=g
    else:rhs[x-1]+=g*fixed[0]
 dense=np.linalg.solve(A,rhs)
 for a,b in zip(sol['node_voltages_V'][1:],dense):check('resistor_independent_dense',a,b,rtol=5e-9,atol=1e-8)
 check('resistor_power_balance',sol['resistive_power_W'],sol['injected_plus_supply_power_W'],rtol=2e-10,atol=1e-10)

for _ in range(220):
 vdd=1.2;vin=rng.uniform(.005,1.195);kn=10**rng.uniform(-5,-3);kp=10**rng.uniform(-5,-3);vtn=.22;vtp=.27
 def f(vo):
  return ideal_nmos_current(kn,vin,vo,vtn)-ideal_nmos_current(kp,vdd-vin,vdd-vo,vtp)
 # Boundaries may be exact roots; cannot use brentq when both off plateau.
 if abs(f(0))<1e-15:ref=0.
 elif abs(f(vdd))<1e-15:ref=vdd
 else:ref=brentq(f,0.,vdd,xtol=1e-14)
 try:got=ideal_cmos_inverter_output(vin,vdd,kn,kp,vtn,vtp)
 except ValueError: continue # documented nonunique plateau in ideal zero-channel-length-modulation model
 check('cmos_scipy_brentq',got,ref,rtol=1e-7,atol=2e-7)

for _ in range(1400):
 w=rng.randint(1,64);limit=1<<w;a=rng.randrange(limit);b=rng.randrange(limit);carry=rng.randrange(2)
 s,c=ripple_adder_unsigned(a,b,w,carry)
 check('ripple_python_integer_truth',s+(c<<w),a+b+carry,rtol=0,atol=0)

for _ in range(200):
 Is=10**rng.uniform(-13,-9);V=rng.uniform(-.1,.45);T=rng.uniform(290,320);n=rng.uniform(1,2);sigV=.001;sigT=.5
 got=diode_current_local_uncertainty(Is,V,T,n,sigV,sigT)
 h=1e-7
 def f(v,t):return Is*math.expm1(v/(n*(K_B*t/Q)))
 check('diode_dIdV_finite_difference',got['dI_dV_A_per_V'],(f(V+h,T)-f(V-h,T))/(2*h),rtol=3e-8,atol=1e-11)
 check('diode_dIdT_finite_difference',got['dI_dT_A_per_K'],(f(V,T+h)-f(V,T-h))/(2*h),rtol=3e-7,atol=1e-11)

result={'schema':'atlas.electronics-independent-v02-oracle/1','version':'Electronics_Semiconductors_0.2.0',
 'result':'passed','random_seed':20261116,'comparisons_per_category':counts,
 'total_individually_compared_numeric_values':sum(counts.values()),'max_abs_difference_per_category':errors,
 'status':'algorithmic benchmarks only; no physical measurement, device characterization or independent scientific peer review',
 'numpy':np.__version__,'scipy':'1.17.0','mpmath':mp.__version__}
print(json.dumps(result,indent=2))
if len(sys.argv)>1:Path(sys.argv[1]).write_text(json.dumps(result,indent=2)+'\n')
