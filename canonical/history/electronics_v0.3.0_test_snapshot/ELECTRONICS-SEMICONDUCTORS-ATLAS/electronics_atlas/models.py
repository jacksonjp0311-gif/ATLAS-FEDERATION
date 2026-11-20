"""ATLAS FORGE Electronics/Semiconductors v0.1.0.

Pure standard-library, finite, bounded, ORIGINAL reference calculations.
Not a device simulator, engineering approval, wafer-fabrication recipe or
laboratory calibration. All physical quantities use SI units.
"""
import math

Q = 1.602176634e-19  # exact coulomb, SI elementary charge magnitude
K_B = 1.380649e-23  # exact J/K, Boltzmann constant
EPSILON_0_APPROX = 8.8541878188e-12  # approximate F/m; NOT exact

def _positive(**values):
    for name,value in values.items():
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<=0:
            raise ValueError(f"{name} must be finite and strictly positive")

def _nonnegative(**values):
    for name,value in values.items():
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0:
            raise ValueError(f"{name} must be finite and nonnegative")

def thermal_voltage(temperature_K):
    _positive(temperature_K=temperature_K)
    return K_B*temperature_K/Q

def mass_action_carriers(net_doping_m3, intrinsic_concentration_m3):
    _positive(intrinsic_concentration_m3=intrinsic_concentration_m3)
    if isinstance(net_doping_m3,bool) or not isinstance(net_doping_m3,(int,float)) or not math.isfinite(net_doping_m3):
        raise ValueError('net doping must be finite')
    d=net_doping_m3; ni=intrinsic_concentration_m3
    h=math.hypot(d,2*ni)
    if d>=0:
        majority=0.5*(d+h); minority=ni*(ni/majority)
        return majority,minority  # electron n, hole p
    majority=0.5*(-d+h); minority=ni*(ni/majority)
    return minority,majority

def built_in_potential(acceptor_m3,donor_m3,intrinsic_concentration_m3,temperature_K):
    _positive(acceptor_m3=acceptor_m3,donor_m3=donor_m3,intrinsic_concentration_m3=intrinsic_concentration_m3)
    # logarithms prevent overflow in the product Na*Nd/ni^2
    k=math.log(acceptor_m3/intrinsic_concentration_m3)+math.log(donor_m3/intrinsic_concentration_m3)
    if k<=0:raise ValueError('nondegenerate depletion model requires Na*Nd>ni^2')
    return thermal_voltage(temperature_K)*k

def depletion_width(acceptor_m3,donor_m3,intrinsic_concentration_m3,relative_permittivity,temperature_K,applied_forward_bias_V=0.0):
    _positive(relative_permittivity=relative_permittivity)
    if isinstance(applied_forward_bias_V,bool) or not isinstance(applied_forward_bias_V,(int,float)) or not math.isfinite(applied_forward_bias_V):
        raise ValueError('bias must be finite')
    vbi=built_in_potential(acceptor_m3,donor_m3,intrinsic_concentration_m3,temperature_K)
    v=vbi-applied_forward_bias_V
    if v<=0:raise ValueError('depletion approximation invalid at/above built-in bias')
    factor=(2*EPSILON_0_APPROX*relative_permittivity/Q)*(1/acceptor_m3+1/donor_m3)
    return math.sqrt(factor*v)

def diode_current(saturation_current_A,bias_V,temperature_K,ideality=1.0):
    _positive(saturation_current_A=saturation_current_A,ideality=ideality)
    if isinstance(bias_V,bool) or not isinstance(bias_V,(int,float)) or not math.isfinite(bias_V):raise ValueError('bias must be finite')
    x=bias_V/(ideality*thermal_voltage(temperature_K))
    if x>700:raise ValueError('exponential outside bounded reference domain')
    return saturation_current_A*math.expm1(x)

def diode_voltage_from_current(saturation_current_A,current_A,temperature_K,ideality=1.0):
    _positive(saturation_current_A=saturation_current_A,ideality=ideality)
    if isinstance(current_A,bool) or not isinstance(current_A,(int,float)) or not math.isfinite(current_A) or current_A<=-saturation_current_A:
        raise ValueError('current must be finite and greater than negative saturation')
    return ideality*thermal_voltage(temperature_K)*math.log1p(current_A/saturation_current_A)

def mos_gate_capacitance(relative_permittivity,area_m2,thickness_m):
    _positive(relative_permittivity=relative_permittivity,area_m2=area_m2,thickness_m=thickness_m)
    return EPSILON_0_APPROX*relative_permittivity*area_m2/thickness_m

def ideal_nmos_current(k_A_per_V2,gate_over_source_V,drain_over_source_V,threshold_V):
    _positive(k_A_per_V2=k_A_per_V2)
    _nonnegative(drain_over_source_V=drain_over_source_V)
    for name,x in [('gate_over_source_V',gate_over_source_V),('threshold_V',threshold_V)]:
        if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):raise ValueError(f'{name} must be finite')
    vov=max(0.,gate_over_source_V-threshold_V)
    if vov==0:return 0.
    vds=drain_over_source_V
    if vds<=vov:return k_A_per_V2*(vov*vds-0.5*vds*vds)
    return 0.5*k_A_per_V2*vov*vov

def rc_step(initial_voltage_V,supply_voltage_V,resistance_ohm,capacitance_F,time_s):
    _positive(resistance_ohm=resistance_ohm,capacitance_F=capacitance_F)
    _nonnegative(time_s=time_s)
    for name,x in [('initial_voltage_V',initial_voltage_V),('supply_voltage_V',supply_voltage_V)]:
        if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):raise ValueError(name)
    return initial_voltage_V+(supply_voltage_V-initial_voltage_V)*(-math.expm1(-time_s/(resistance_ohm*capacitance_F)))

def switch_dynamic_power(capacitance_F,supply_voltage_V,frequency_Hz,activity_factor):
    _positive(capacitance_F=capacitance_F)
    _nonnegative(supply_voltage_V=supply_voltage_V,frequency_Hz=frequency_Hz,activity_factor=activity_factor)
    if activity_factor>1:raise ValueError('activity factor must be <= 1')
    return activity_factor*capacitance_F*supply_voltage_V**2*frequency_Hz

def current_divergence_1d(edge_current_densities_A_m2,spacing_m):
    _positive(spacing_m=spacing_m)
    if len(edge_current_densities_A_m2)<2:raise ValueError('requires at least two edge values')
    if any(isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) for x in edge_current_densities_A_m2):raise ValueError('finite currents required')
    return tuple((b-a)/spacing_m for a,b in zip(edge_current_densities_A_m2,edge_current_densities_A_m2[1:]))

def _bit(x):
    if type(x) not in (int,bool) or x not in (0,1,False,True):raise ValueError('binary input must be 0 or 1')
    return int(x)

def logic_not(x):return 1-_bit(x)
def logic_nand(a,b):return 1-_bit(a)*_bit(b)
def logic_nor(a,b):return 1-int(bool(_bit(a) or _bit(b)))
