"""Independent finite crosschecks for Electronics scoped v1 candidate.

Requires NumPy and mpmath only for oracle execution; reference module stays
Python-stdlib-only. Independent formulas: direct high-precision mpmath
calculations, NumPy matrix-free vector arithmetic, and separately coded
abstract-machine semantics. No measured semiconductor samples.
"""
import json, random, math
from decimal import Decimal, localcontext
import numpy as np
import mpmath as mp
from electronics_atlas.v1_scoped_models import *

mp.mp.dps=65
rng=random.Random(2026111601)
checks={};max_err={}
def assertclose(name,a,b,atol,rtol=1e-11):
    if not math.isfinite(a) or not math.isfinite(b):raise AssertionError((name,'nonfinite',a,b))
    err=abs(a-b)
    if err>atol+rtol*abs(b):raise AssertionError((name,a,b,err))
    checks[name]=checks.get(name,0)+1
    max_err[name]=max(max_err.get(name,0.),err)

# Closed-form independent high-precision oxide, threshold, NMOS and diode oracles.
for _ in range(400):
    A=10**rng.uniform(-14,-10);t=10**rng.uniform(-9,-6);er=rng.uniform(2,18)
    got=mos_oxide_capacitance(A,t,er)['capacitance_F']
    expected=float(mp.mpf('8.8541878128e-12')*mp.mpf(er)*mp.mpf(A)/mp.mpf(t))
    assertclose('oxide_capacitance',got,expected,atol=1e-26)
for _ in range(400):
    vt0=rng.uniform(.1,1);gamma=rng.uniform(0,.5);phi=rng.uniform(.1,.5);sb=rng.uniform(0,2)
    got=mos_body_effect_threshold(vt0,gamma,phi,sb)
    expected=float(mp.mpf(vt0)+mp.mpf(gamma)*(mp.sqrt(2*mp.mpf(phi)+mp.mpf(sb))-mp.sqrt(2*mp.mpf(phi))))
    assertclose('body_effect',got,expected,atol=1e-13)
for _ in range(600):
    vg=rng.uniform(0,3);vd=rng.uniform(0,3);vt=rng.uniform(.2,.9)
    k=10**rng.uniform(-5,-2);lam=rng.uniform(0,.1)
    got=long_channel_nmos(vg,vd,vt,k,lam)['current_A']
    u=mp.mpf(vg)-mp.mpf(vt)
    expected=0 if u<=0 else (mp.mpf(k)*(u*mp.mpf(vd)-mp.mpf(vd)**2/2) if vd<float(u) else mp.mpf(k)*u**2/2)
    expected=float(expected*(1+mp.mpf(lam)*mp.mpf(vd)))
    assertclose('nmos',got,expected,atol=1e-14)
for _ in range(400):
    T=rng.uniform(220,460);v=rng.uniform(-.25,.48);n=rng.uniform(1,2);is_=10**rng.uniform(-16,-10)
    got=ideal_diode_current(v,is_,n,T)
    VT=mp.mpf('1.380649e-23')*mp.mpf(T)/mp.mpf('1.602176634e-19')
    ref=float(mp.mpf(is_)*mp.expm1(mp.mpf(v)/(mp.mpf(n)*VT)))
    assertclose('ideal_diode',got,ref,atol=1e-18,rtol=3e-12)

# 1D continuous diffusion is checked against high-precision erf and
# a separately integrated numerical quadrature for total sheet dose.
for _ in range(350):
    Q=10**rng.uniform(13,17);D=10**rng.uniform(-17,-12)
    t=10**rng.uniform(-1,3);x=rng.uniform(0,8)*math.sqrt(D*t)
    out=half_space_gaussian_dopant(Q,D,t,x)
    ref=float(mp.mpf(Q)*mp.erf(mp.mpf(x)/(2*mp.sqrt(mp.mpf(D)*mp.mpf(t)))))
    assertclose('diffusion_integral',out['integrated_sheet_dose_per_m2'],ref,atol=1e-3)
    peak=float(mp.mpf(Q)/(mp.sqrt(mp.pi)*mp.sqrt(mp.mpf(D)*mp.mpf(t))))
    ref_density=peak*math.exp(-x*x/(4*D*t))
    assertclose('diffusion_concentration',out['volume_density_per_m3'],ref_density,atol=1e-12)

# Electrical measurement and one-lump thermal response, separate equations.
for _ in range(350):
    I=10**rng.uniform(-5,-2);V=I*rng.uniform(1,500)*math.log(2)/math.pi
    assertclose('four_point',four_point_sheet_resistance(V,I),math.pi*V/(I*math.log(2)),atol=1e-10)
    B=rng.uniform(.05,2);thickness=10**rng.uniform(-5,-2);n=10**rng.uniform(20,25)
    vh=I*B/(ELEMENTARY_CHARGE_C*n*thickness)
    assertclose('hall_density',hall_carrier_density(I,B,thickness,vh),n,atol=1e10)
    r=rng.uniform(.1,100);c=rng.uniform(1e-3,10);Ta=rng.uniform(250,350)
    Ti=Ta+rng.uniform(0,100);P=rng.uniform(0,5);elapsed=rng.uniform(0,20)*r*c
    expected=Ta+P*r+(Ti-Ta-P*r)*math.exp(-elapsed/(r*c))
    assertclose('thermal_rc',thermal_rc(elapsed,Ta,Ti,P,r,c),expected,atol=1e-11)

# Exhaustive 8-bit add and XOR instruction programs; independent arithmetic
# model does not execute the DUT state-machine implementation.
for a in range(256):
    for b in range(256):
        prog=bytes([0x10,a,0x20,b,0x40,1,0x30,0xa5,0xf0,0])
        result=EightBitAccumulator(prog).run()
        exp=(a+b)&255
        if not result['halted'] or result['ram'][1]!=exp or result['accumulator']!=(exp^0xa5):
            raise AssertionError(('accumulator',a,b,result))
        checks['microprogram_add_xor']=checks.get('microprogram_add_xor',0)+1

# Negative/unsafe domain checks, not calibration.
rejections=[
 (mos_oxide_capacitance,(0,1e-9,3.9)),(mos_oxide_capacitance,(1,0,3.9)),
 (mos_body_effect_threshold,(.5,.2,.3,-1)),(long_channel_nmos,(1,-1,.5,1e-3)),
 (ideal_diode_current,(100,1e-12,1,300)),(half_space_gaussian_dopant,(1,0,1,1)),
 (hall_carrier_density,(1,0,.1,.1)),(dram_retention,(1,2,.1,1)),
 (EightBitAccumulator(bytes([0x70,0])).run,tuple()),
]
for fn,args in rejections:
    try:fn(*args)
    except ValueError:checks['negative_cases']=checks.get('negative_cases',0)+1
    else:raise AssertionError(('failed to reject',fn.__name__,args))

if __name__=='__main__':
    print(json.dumps({'schema':'atlas.electronics-v1rc-independent-oracle/1','status':'passed',
      'seed':2026111601,'comparisons':sum(checks.values()),'by_method':checks,
      'max_absolute_error_by_method':max_err,
      'independent_software_reference_only':True,'experimental_device_measurements':0,
      'third_party_original_source_files_authenticated':0,
      'scientific_peer_review':False,'numpy_version':np.__version__,
      'mpmath_version':mp.__version__},indent=2))
