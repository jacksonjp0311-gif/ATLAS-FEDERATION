"""Independent NumPy crosschecks, exclusively on synthetic inputs.

This verifies stated arithmetic only, not experimental chemistry or any real
semiconductor, electrochemical process, or materials measurement.
"""
import json,random,math,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from chemistry_atlas.v1_models import (photon_bandgap,varshni_bandgap,intrinsic_carrier_density,
  diode_ideal_current,shomate_thermochemistry,equilibrium_with_heat_capacity,
  electrochemical_work_bound,faradaic_yield,bragg_first_order_spacing,uncertainty_product)
from chemistry_atlas.models import R_GAS,FARADAY,ELEMENTARY_CHARGE
rng=random.Random(20261114);counts={};max_abs=0.
def check(name,a,b):
 global max_abs
 if not (math.isfinite(float(a)) and math.isfinite(float(b))):raise AssertionError(name+' nonfinite')
 delta=abs(float(a)-float(b));max_abs=max(max_abs,delta)
 if delta>2e-8*max(1.,abs(float(a)),abs(float(b))):raise AssertionError((name,a,b,delta))
 counts[name]=counts.get(name,0)+1
for _ in range(480):
 lam=rng.uniform(150,3000);eg=rng.uniform(.1,5)
 r=photon_bandgap(lam,eg)
 check('photon_energy_hc',r['photon_energy_eV'],float(np.divide(6.62607015e-34*299792458,lam*1e-9*ELEMENTARY_CHARGE)))
 t=rng.uniform(50,600);a=rng.uniform(0,.001);beta=rng.uniform(30,700);e0=2
 g=varshni_bandgap(t,e0,a,beta)
 check('varshni_gap',g['bandgap_eV'],e0-a*t*t/(t+beta))
 eps=t*1e-5
 derivative=(varshni_bandgap(t+eps,e0,a,beta)['bandgap_eV']-varshni_bandgap(t-eps,e0,a,beta)['bandgap_eV'])/(2*eps)
 check('varshni_numerical_derivative',g['derivative_eV_K'],derivative)
 nc=rng.uniform(1e23,1e26);nv=rng.uniform(1e23,1e26);gap=rng.uniform(.05,2.5)
 c=intrinsic_carrier_density(nc,nv,gap,t)
 ln_est=float(np.log(np.sqrt(nc*nv))-gap*ELEMENTARY_CHARGE/(2*1.380649e-23*t))
 check('log_intrinsic_carriers',c['ln_carrier_density_per_m3'],ln_est)
 v=rng.uniform(-.2,.2);Is=rng.uniform(1e-15,1e-9);n=rng.uniform(1,2)
 d=diode_ideal_current(Is,v,n,t)
 check('ideal_diode',d['current_A'],float(Is*np.expm1(ELEMENTARY_CHARGE*v/(n*1.380649e-23*t))))
 te=rng.uniform(250,900);tr=rng.uniform(250,900);dh=rng.uniform(-2e5,2e5);ds=rng.uniform(-600,600);cp=rng.uniform(-30,90)
 x=equilibrium_with_heat_capacity(tr,te,dh,ds,cp)
 H=dh+cp*(te-tr);S=ds+cp*math.log(te/tr)
 check('equilibrium_deltaG',x['delta_G_J_mol'],H-te*S)
 check('equilibrium_logK',x['logK'],float(-(H-te*S)/(R_GAS*te)))
 f=rng.uniform(-3,3);mol=rng.uniform(0,2);eta=rng.uniform(0,1)
 x=electrochemical_work_bound(f,mol,eta)
 check('faraday_cell_work',x['reversible_work_magnitude_J'],abs(f)*mol*FARADAY)
 charge=rng.uniform(0,2e5);electrons=rng.randint(1,10)
 x=faradaic_yield(charge,electrons,eta)
 check('faradaic_stoichiometry',x['illustrative_product_mol'],charge*eta/(electrons*FARADAY))
 theta=rng.uniform(2,80);wave=rng.uniform(.01,.3)
 x=bragg_first_order_spacing(wave,theta)
 check('bragg_geometry',x['d_spacing_nm'],wave/(2*float(np.sin(np.deg2rad(theta)))))
 a=rng.uniform(-100,100);b=rng.uniform(-100,100);u_a=rng.uniform(0,10);u_b=rng.uniform(0,10)
 cov=rng.uniform(-1,1)*u_a*u_b
 x=uncertainty_product(a,b,u_a,u_b,cov)
 check('uncertainty_covariance',x['standard_uncertainty'],float(np.sqrt(max(0,b*b*u_a*u_a+a*a*u_b*u_b+2*a*b*cov))))

# Distinct numerical quadrature independently confirms analytical Shomate integrals.
for _ in range(250):
 lo=rng.uniform(180,350);hi=rng.uniform(600,1500)
 t1=rng.uniform(lo,hi);t2=rng.uniform(lo,hi)
 A=rng.uniform(10,90);B=rng.uniform(-5,5);C=rng.uniform(-3,3);D=rng.uniform(-3,3);E=rng.uniform(-1,1)
 calc=shomate_thermochemistry(A,B,C,D,E,t1,t2,lo,hi)
 grid=np.linspace(t1,t2,4001)
 v=grid/1000
 cps=A+B*v+C*v*v+D*v**3+E/v**2
 h=float(np.trapezoid(cps,grid))
 s=float(np.trapezoid(cps/grid,grid))
 # grid numerical quadrature error scales with interval, check independently to 5e-5 absolute relative
 if abs(calc['delta_H_J_mol']-h)>1e-5*max(1,abs(calc['delta_H_J_mol'])):raise AssertionError('Shomate heat integral')
 if abs(calc['delta_S_J_mol_K']-s)>1e-5*max(1,abs(calc['delta_S_J_mol_K'])):raise AssertionError('Shomate entropy integral')
 counts['shomate_numeric_quadrature'] = counts.get('shomate_numeric_quadrature',0)+2

report={'schema':'atlas.chem-v1-independent-numerical-oracle/1','status':'passed','comparisons':sum(counts.values()),
        'categories':counts,'random_seed':20261114,'max_absolute_difference':max_abs,'numpy_version':np.__version__,
        'original_publisher_source_bytes':0,'independent_laboratory_measurements':0,'semiconductor_devices_tested':0,
        'claim':'Bounded finite arithmetic and numerical quadrature checks on author-invented values, not physical model or empirical validation'}
print(json.dumps(report,indent=2))
if len(sys.argv)>1:Path(sys.argv[1]).write_text(json.dumps(report,indent=2)+'\n')
