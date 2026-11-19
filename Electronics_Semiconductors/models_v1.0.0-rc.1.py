"""ATLAS FORGE: bounded and *uncalibrated* electronic-science reconstruction.

Every method documents assumptions. Implementations are standard-library reference
computations, not integrated-circuit fabrication, design-rule verification or
physical semiconductor device certification. Python >=3.10.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import exp, expm1, erf, sqrt, log, log1p, pi, isfinite

EPSILON_0_F_PER_M = 8.8541878128e-12
ELEMENTARY_CHARGE_C = 1.602176634e-19
BOLTZMANN_J_PER_K = 1.380649e-23


def finite(name, value, *, positive=False, nonnegative=False):
    if type(value) not in (float, int) or not isfinite(value):
        raise ValueError(name + ': finite real required')
    value=float(value)
    if (positive and not value>0.0) or (nonnegative and value<0.0):
        raise ValueError(name + ': outside allowed range')
    return value


def mos_oxide_capacitance(area_m2, oxide_thickness_m, relative_permittivity):
    """Uniform parallel plate gate; ignores fringing, interface traps, quantum C."""
    A=finite('area',area_m2,positive=True)
    t=finite('oxide thickness',oxide_thickness_m,positive=True)
    er=finite('relative permittivity',relative_permittivity,positive=True)
    cox=EPSILON_0_F_PER_M*er/t
    cap=cox*A
    if not isfinite(cap) or not isfinite(cox):raise ValueError('overflow')
    return {'capacitance_F':cap,'per_area_F_m2':cox,
            'assumption':'uniform insulating oxide and parallel-plate geometry'}


def mos_body_effect_threshold(vt0_V, gamma_sqrtV, phi_f_V, v_sb_V):
    """Long-channel NMOS bulk/body-effect idealization, reverse substrate bias."""
    vt0=finite('zero body bias threshold',vt0_V)
    gamma=finite('gamma',gamma_sqrtV,nonnegative=True)
    phi=finite('Fermi potential magnitude',phi_f_V,positive=True)
    sb=finite('source-bulk voltage',v_sb_V,nonnegative=True)
    result=vt0+gamma*(sqrt(2*phi+sb)-sqrt(2*phi))
    if not isfinite(result):raise ValueError('overflow')
    return result


def long_channel_nmos(v_gs_V,v_ds_V,v_threshold_V,transconductance_A_V2,channel_modulation_per_V=0):
    """Ideal enhancement NMOS, forward Vds only; no subthreshold or self-heating."""
    vg=finite('Vgs',v_gs_V);vd=finite('Vds',v_ds_V,nonnegative=True)
    vt=finite('Vt',v_threshold_V)
    k=finite('k',transconductance_A_V2,positive=True)
    lam=finite('lambda',channel_modulation_per_V,nonnegative=True)
    overdrive=vg-vt
    if overdrive<=0:
        ids=0.0;gm=0.0;region='cutoff'
    elif vd<overdrive:
        ids=k*(overdrive*vd-.5*vd*vd)*(1+lam*vd)
        gm=k*vd*(1+lam*vd);region='linear'
    else:
        ids=.5*k*overdrive**2*(1+lam*vd)
        gm=k*overdrive*(1+lam*vd);region='saturation'
    if not isfinite(ids) or not isfinite(gm):raise ValueError('overflow')
    return {'current_A':ids,'gm_S':gm,'region':region,'hardware_validated':False}


def thermal_voltage(temperature_K):
    t=finite('temperature',temperature_K,positive=True)
    return BOLTZMANN_J_PER_K*t/ELEMENTARY_CHARGE_C


def ideal_diode_current(bias_V, reverse_saturation_A, ideality, temperature_K):
    """Shockley minority-carrier ideal diode; not avalanche or series R."""
    v=finite('bias',bias_V);is_=finite('saturation',reverse_saturation_A,positive=True)
    n=finite('ideality',ideality,positive=True);t=finite('temperature',temperature_K,positive=True)
    argument=v/(n*thermal_voltage(t))
    if not isfinite(argument) or argument>700:raise ValueError('model overflow; current exceeds bounded regime')
    out=is_*expm1(argument)
    if not isfinite(out):raise ValueError('diode current overflow')
    return out


def half_space_gaussian_dopant(sheet_dose_m2, diffusivity_m2_s, seconds, depth_m):
    """One-sided semi-infinite Gaussian redistribution, conserved total dose Q.

    C(x,t)=Q/sqrt(pi*D*t)*exp(-x**2/(4*D*t)), x>=0.
    Not an implanted profile, furnace recipe, activation model, or defect model.
    """
    q=finite('sheet dose',sheet_dose_m2,nonnegative=True)
    d=finite('diffusivity',diffusivity_m2_s,positive=True)
    t=finite('time',seconds,positive=True)
    x=finite('depth',depth_m,nonnegative=True)
    spread=sqrt(d*t)
    peak=q/(sqrt(pi)*spread)
    c=peak*exp(-.25*(x/spread)**2)
    integrated=q*erf(x/(2*spread))
    if not all(isfinite(z) for z in (peak,c,integrated)):raise ValueError('model overflow')
    return {'volume_density_per_m3':c,'integrated_sheet_dose_per_m2':integrated,
            'total_sheet_dose_per_m2':q,'assumption':'semi-infinite unbounded diffusion with constant D'}


def four_point_sheet_resistance(voltage_V, current_A):
    """Infinite, uniform, thin sheet with four collinear equally spaced probes."""
    v=finite('V',voltage_V,nonnegative=True)
    i=finite('I',current_A,positive=True)
    return (pi/log(2))*(v/i)


def hall_carrier_density(current_A, magnetic_field_T, sample_thickness_m, hall_voltage_V):
    """Single majority carrier, ideal uniform Hall bar; magnitude only, no sign inference."""
    i=finite('current',current_A,positive=True)
    b=finite('field',magnetic_field_T)
    t=finite('thickness',sample_thickness_m,positive=True)
    v=finite('Hall voltage',hall_voltage_V)
    if b==0 or v==0:raise ValueError('zero Hall field or voltage is non-identifiable')
    n=abs(i*b/(ELEMENTARY_CHARGE_C*t*v))
    if not isfinite(n) or n==0:raise ValueError('invalid inferred density')
    return n


def thermal_rc(t_s, ambient_K, initial_K, power_W, resistance_K_W, capacitance_J_K):
    """One-lump thermal step response; not device temperature field."""
    t=finite('time',t_s,nonnegative=True)
    Ta=finite('ambient temperature',ambient_K,positive=True)
    Ti=finite('initial temperature',initial_K,positive=True)
    p=finite('step power',power_W,nonnegative=True)
    r=finite('thermal R',resistance_K_W,positive=True)
    c=finite('thermal C',capacitance_J_K,positive=True)
    target=Ta+p*r
    v=target+(Ti-target)*exp(-t/(r*c))
    if not isfinite(v) or v<=0:raise ValueError('invalid thermal result')
    return v


def dram_retention(initial_charge_C, min_valid_charge_C, leakage_time_constant_s, elapsed_s):
    """Simple exponential cell leakage, not statistically guaranteed retention."""
    q=finite('initial charge',initial_charge_C,positive=True)
    threshold=finite('minimum readable charge',min_valid_charge_C,positive=True)
    tau=finite('retention tau',leakage_time_constant_s,positive=True)
    t=finite('elapsed time',elapsed_s,nonnegative=True)
    if threshold>=q:raise ValueError('initial read margin required')
    left=q*exp(-t/tau)
    max_time=tau*log(q/threshold)
    return {'charge_C':left,'retains_state':left>=threshold,
            'ideal_refresh_deadline_s':max_time,
            'guaranteed_over_process_corners':False}


def poisson_defect_free_yield(density_defects_cm2, device_area_cm2):
    """Assumes independent spatial Poisson point defects and catastrophic any defect."""
    d=finite('defect density',density_defects_cm2,nonnegative=True)
    area=finite('area',device_area_cm2,nonnegative=True)
    return exp(-d*area)


def line_edge_overlay_budget(mask_error_nm, alignment_error_nm, etch_bias_nm, target_cd_nm):
    """Conservative deterministic CD error bound; no statistical process model."""
    a=finite('mask CD error',mask_error_nm,nonnegative=True)
    b=finite('alignment error',alignment_error_nm,nonnegative=True)
    c=finite('etch bias error',etch_bias_nm,nonnegative=True)
    d=finite('target critical dimension',target_cd_nm,positive=True)
    maxerr=a+b+c
    return {'max_absolute_feature_error_nm':maxerr,'relative_bound':maxerr/d,
            'within_target_halfwidth':maxerr<=d/2,'not_process_qualified':True}


@dataclass
class EightBitAccumulator:
    """Minimal software *architecture bridge*, not a fabricated or complete CPU.

    Each instruction is two bytes: [opcode, operand]. Opcodes: 0x1 LDI,
    0x2 ADD, 0x3 XOR, 0x4 STORE, 0x5 LOAD, 0x6 JNZ, 0xF HALT.
    Arithmetic is modulo 256; 16-byte RAM and no I/O, interrupts or timing.
    """
    program: bytes
    max_steps: int=128
    def run(self):
        if not isinstance(self.program,bytes) or len(self.program)%2 or not self.program:
            raise ValueError('nonempty even-length program bytes required')
        if type(self.max_steps) is not int or not 1<=self.max_steps<=100000:
            raise ValueError('bounded max steps required')
        mem=[0]*16;acc=0;pc=0;steps=0;flags=[]
        while steps<self.max_steps:
            if pc<0 or pc+1>=len(self.program) or pc%2:
                raise ValueError('PC outside valid aligned program')
            op=self.program[pc];operand=self.program[pc+1]
            pc+=2;steps+=1
            if op==0x10:acc=operand
            elif op==0x20:acc=(acc+operand)%256
            elif op==0x30:acc^=operand
            elif op==0x40:
                if operand>=16:raise ValueError('RAM address outside 16-byte memory')
                mem[operand]=acc
            elif op==0x50:
                if operand>=16:raise ValueError('RAM address outside 16-byte memory')
                acc=mem[operand]
            elif op==0x60:
                if acc!=0:
                    if operand>=len(self.program) or operand%2:raise ValueError('invalid jump target')
                    pc=operand
            elif op==0xF0:
                return {'halted':True,'accumulator':acc,'ram':mem,'steps':steps,
                        'program_counter':pc,'zero':acc==0,'silicon_implemented':False}
            else:raise ValueError('unsupported instruction')
        return {'halted':False,'accumulator':acc,'ram':mem,'steps':steps,
                'program_counter':pc,'zero':acc==0,'silicon_implemented':False}
