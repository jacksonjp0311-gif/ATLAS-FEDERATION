"""Nonclinical synthetic electrode impedance, digitization and error tools.

Only simulated electrical dummy networks are in scope. DO NOT attach this model
or its computed values to a person, animal, implant or mains-power circuit.
"""
from __future__ import annotations
import cmath,math,random,hashlib,json
from .foundations import _real


def electrode_dummy_impedance(rs_ohm,rct_ohm,cdl_f,frequency_hz):
    """Z=Rs + (Rct || 1/(jω Cdl)); illustrative passive dummy load only."""
    rs=_real(rs_ohm,'series resistance',nonnegative=True)
    rct=_real(rct_ohm,'interface resistance',positive=True)
    c=_real(cdl_f,'parallel capacitance',positive=True)
    freq=_real(frequency_hz,'frequency',nonnegative=True)
    z=complex(rs,0)+1/complex(1/rct,2*math.pi*freq*c)
    return {'real_ohm':z.real,'imag_ohm':z.imag,'magnitude_ohm':abs(z),
            'phase_radians':cmath.phase(z),'simulated_dummy_electrical_network':True,
            'human_or_animal_connection_authorized':False}


def adc_ideal_quantize(sample_volts:float,v_min_volts:float,v_max_volts:float,bits:int):
    """Uniform ideal single-ended encoder; nearest code and explicit rail clip."""
    sample=_real(sample_volts,'sample volts')
    lo=_real(v_min_volts,'minimum voltage');hi=_real(v_max_volts,'maximum voltage')
    if hi<=lo:raise ValueError('ADC max must exceed min')
    if type(bits) is not int or not 1<=bits<=24:raise ValueError('ADC bits 1..24')
    levels=(1<<bits)-1
    clamped=max(lo,min(hi,sample))
    q=int(math.floor((clamped-lo)*levels/(hi-lo)+0.5))
    q=max(0,min(levels,q))
    recon=lo+(q/levels)*(hi-lo)
    return {'code':q,'reconstructed_volts':recon,'step_volts':(hi-lo)/levels,
            'clipped':sample<lo or sample>hi,'ideal_adc_reference_only':True}


def uniform_sample_sine(amplitude_v,frequency_hz,sample_rate_hz,samples,phase_radians=0.0):
    a=_real(amplitude_v,'amplitude')
    f=_real(frequency_hz,'frequency',nonnegative=True)
    fs=_real(sample_rate_hz,'sample rate',positive=True)
    phase=_real(phase_radians,'phase')
    if type(samples) is not int or not 1<=samples<=10000:raise ValueError('samples 1..10000')
    return [a*math.sin(2*math.pi*f*(n/fs)+phase) for n in range(samples)]


def deterministic_voltage_noise(synthetic_samples:list[float],sigma_volts,seed=0):
    if not isinstance(synthetic_samples,list) or not 1<=len(synthetic_samples)<=10000:
        raise ValueError('finite sample list 1..10000 required')
    sigma=_real(sigma_volts,'noise standard deviation',nonnegative=True)
    if type(seed) is not int or not 0<=seed<=2**32-1:raise ValueError('integer seed required')
    r=random.Random(seed)
    samples=[_real(x,'input sample')+r.gauss(0,sigma) for x in synthetic_samples]
    blob=json.dumps(samples,sort_keys=True,allow_nan=False,separators=(',',':')).encode()
    return {'samples_volts':samples,'sha256':hashlib.sha256(blob).hexdigest(),
            'seed':seed,'synthetic_noise_only':True}


def root_sum_square_uncertainty(standard_uncertainties:list[float]|tuple[float,...]):
    if not isinstance(standard_uncertainties,(list,tuple)) or not 1<=len(standard_uncertainties)<=128:
        raise ValueError('standard uncertainties 1..128 required')
    sigmas=[_real(u,'standard uncertainty',nonnegative=True) for u in standard_uncertainties]
    return math.hypot(*sigmas)  # assumes zero covariance; explicitly scoped
