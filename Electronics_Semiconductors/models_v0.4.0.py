"""ATLAS FORGE canonical Electronics node v0.4.0 — bounded electronic logic references.

Pure Python 3.10+; algebraic digital abstraction only. No transistor fabrication,
metastability time guarantee, actual timing library or laboratory calibration.
"""
from __future__ import annotations
import math
from .v03_models import nand_ripple_add


def _f(name, value, nonnegative=False, positive=False):
    if type(value) not in (int,float) or not math.isfinite(value):
        raise ValueError(f"{name}: finite real required")
    if (positive and value <= 0) or (nonnegative and value < 0):
        raise ValueError(f"{name}: outside physical input domain")
    return float(value)


def _bit(v):
    if type(v) is not int or v not in (0,1):
        raise ValueError('exact binary 0/1 required')
    return v


def digital_noise_margins(vdd_V, vil_max_V, vih_min_V, vol_max_V, voh_min_V):
    """Conservative static margins; 0 <= VOL <= VIL < VIH <= VOH <= VDD.

    Does not characterize transition slopes, dynamic noise or analog hysteresis.
    """
    vdd=_f('supply',vdd_V,positive=True)
    vil=_f('VIL',vil_max_V,nonnegative=True)
    vih=_f('VIH',vih_min_V,nonnegative=True)
    vol=_f('VOL',vol_max_V,nonnegative=True)
    voh=_f('VOH',voh_min_V,nonnegative=True)
    if not (0<=vol<=vil<vih<=voh<=vdd):
        raise ValueError('inconsistent digital voltage windows')
    return {'noise_margin_low_V':vil-vol,'noise_margin_high_V':voh-vih,
            'worst_static_noise_margin_V':min(vil-vol,voh-vih),
            'undefined_input_window_V':(vil,vih),'measured_characterization':False}


def input_logic_level(voltage_V,vil_max_V,vih_min_V):
    v=_f('voltage',voltage_V); vil=_f('VIL',vil_max_V)
    vih=_f('VIH',vih_min_V)
    if vil>=vih:raise ValueError('digital thresholds must be distinct')
    return 0 if v<=vil else 1 if v>=vih else None


def logic_dag_arrival(gates, input_arrivals_s, outputs):
    """Min/max path arrival envelopes through an acyclic positive-delay gate DAG.

    Gate tuple: (output_name, (input_names...), delay_min_s, delay_max_s).
    Arrival envelopes are NOT transition sensitization proofs, crosstalk or SI.
    """
    if not isinstance(input_arrivals_s,dict) or not isinstance(gates,(list,tuple)):
        raise ValueError('gates and input arrivals must be collections')
    if not isinstance(outputs,(list,tuple)) or not outputs:
        raise ValueError('one or more outputs required')
    earliest={};latest={};critical={}
    for name,rng in input_arrivals_s.items():
        if type(name) is not str or not name or not isinstance(rng,(tuple,list)) or len(rng)!=2:
            raise ValueError('invalid input timing pin')
        lo=_f('input earliest',rng[0],nonnegative=True);hi=_f('input latest',rng[1],nonnegative=True)
        if lo>hi:raise ValueError('earliest input exceeds latest')
        earliest[name]=lo;latest[name]=hi;critical[name]=(name,)
    pending={}
    for item in gates:
        if not isinstance(item,(tuple,list)) or len(item)!=4:raise ValueError('gate shape invalid')
        name,ins,dmin,dmax=item
        if type(name) is not str or not name or name in pending or name in earliest:
            raise ValueError('duplicate/invalid gate output')
        if not isinstance(ins,(tuple,list)) or not ins or any(type(i) is not str or not i for i in ins):
            raise ValueError('gate must have named input pins')
        lo=_f('minimum delay',dmin,nonnegative=True);hi=_f('maximum delay',dmax,nonnegative=True)
        if lo>hi:raise ValueError('invalid delay bounds')
        pending[name]=(tuple(ins),lo,hi)
    allnames=set(earliest)|set(pending)
    if any(i not in allnames for ins,_,_ in pending.values() for i in ins):
        raise ValueError('floating or unbound source pin')
    while pending:
        ready=sorted(name for name,(ins,_,_) in pending.items() if all(i in earliest for i in ins))
        if not ready:raise ValueError('combinational feedback loop detected')
        for name in ready:
            ins,dmin,dmax=pending.pop(name)
            earliest[name]=min(earliest[i] for i in ins)+dmin
            longest=max(ins,key=lambda i:(latest[i],i))
            latest[name]=latest[longest]+dmax
            critical[name]=critical[longest]+(name,)
    if any(o not in earliest for o in outputs):raise ValueError('requested output missing')
    return {o:{'earliest_s':earliest[o], 'latest_s':latest[o],
               'latest_path':critical[o]} for o in outputs}


def synchronous_setup_hold(period_s,clk_to_q_min_s,clk_to_q_max_s,
                            comb_min_s,comb_max_s,setup_s,hold_s,
                            capture_minus_launch_skew_s=0.0,
                            setup_uncertainty_s=0.0,hold_uncertainty_s=0.0):
    """One launch/capture clock domain. Positive skew eases setup, hurts hold.

    launch edge=0, capture edge=skew for hold and period+skew for setup.
    """
    T=_f('period',period_s,positive=True)
    q0=_f('min clk-q',clk_to_q_min_s,nonnegative=True)
    q1=_f('max clk-q',clk_to_q_max_s,nonnegative=True)
    c0=_f('min combinational',comb_min_s,nonnegative=True)
    c1=_f('max combinational',comb_max_s,nonnegative=True)
    setup=_f('setup',setup_s,nonnegative=True)
    hold=_f('hold',hold_s,nonnegative=True)
    skew=_f('skew',capture_minus_launch_skew_s)
    su=_f('setup uncertainty',setup_uncertainty_s,nonnegative=True)
    hu=_f('hold uncertainty',hold_uncertainty_s,nonnegative=True)
    if q0>q1 or c0>c1:raise ValueError('min delay exceeds max delay')
    s=(T+skew-setup-su)-(q1+c1)
    h=(q0+c0)-(skew+hold+hu)
    if not math.isfinite(s) or not math.isfinite(h):raise ValueError('nonfinite slack')
    return {'setup_slack_s':s,'hold_slack_s':h,
            'setup_pass':s>=0,'hold_pass':h>=0,
            'critical_clock_period_lower_bound_s':q1+c1+setup+su-skew,
            'scope':'single-cycle single-clock bounded delay abstraction'}


def synchronizer_mtbf_log10(clock_Hz,data_toggle_Hz,T0_s,tau_s,resolution_s):
    """Log10 MTBF seconds for empirical exponential tail model; not a guarantee.

    MTBF = exp(T_res/tau)/(f_clock*f_data*T0).
    T0 and tau must come from measured silicon; no default fabricated values.
    """
    fc=_f('clock',clock_Hz,positive=True); fd=_f('data',data_toggle_Hz,positive=True)
    t0=_f('T0 measured calibration',T0_s,positive=True)
    tau=_f('tau measured calibration',tau_s,positive=True)
    tr=_f('resolution time',resolution_s,nonnegative=True)
    x=(tr/tau)/math.log(10)-(math.log10(fc)+math.log10(fd)+math.log10(t0))
    if not math.isfinite(x):raise ValueError('unrepresentable MTBF log')
    return {'log10_mtbf_seconds':x,'hardware_certified':False,
            'limitations':'empirical tail model; no deterministic metastability resolution bound'}


def primitive_alu(a,b,width,operation):
    """Combinational word ALU; no instruction-set, control, transistor or wire timing.

    For SUB, carry=1 means no unsigned borrow; overflow is two's-complement.
    """
    if type(width) is not int or not 1<=width<=16 or type(a) is not int or type(b) is not int:
        raise ValueError('bit width and words must be exact integers')
    lim=1<<width;mask=lim-1
    if not (0<=a<lim and 0<=b<lim) or operation not in ('ADD','SUB','AND','OR','XOR','SHL','SHR'):
        raise ValueError('word values or operation invalid')
    carry=0;overflow=0
    if operation=='ADD':
        result,carry=nand_ripple_add(a,b,width)
        overflow=int(bool((~(a^b)&(a^result)) & (1<<(width-1))))
    elif operation=='SUB':
        result,carry=nand_ripple_add(a,mask^b,width,1)
        overflow=int(bool(((a^b)&(a^result)) & (1<<(width-1))))
    elif operation=='AND':result=a&b
    elif operation=='OR':result=a|b
    elif operation=='XOR':result=a^b
    elif operation=='SHL':
        carry=(a>>(width-1))&1;result=(a<<1)&mask
    else:
        carry=a&1;result=a>>1
    return {'result':result, 'carry':carry,'overflow':overflow,
            'zero':int(result==0),'negative':(result>>(width-1))&1,
            'width':width,'operation':operation}


def bounded_memory_cycle(words,addr,width,read_enable,write_enable,write_value=None,
                         collision_policy='undefined'):
    """One abstract memory edge; collision read convention stated explicitly.

    Unknown (None) is preserved as unknown; bitcells and retention not modeled.
    """
    if not isinstance(words,(list,tuple)) or not 1<=len(words)<=256:
        raise ValueError('memory length 1..256 required')
    if type(width) is not int or not 1<=width<=16:
        raise ValueError('memory word width 1..16 required')
    lim=1<<width
    if any(x is not None and (type(x) is not int or not 0<=x<lim) for x in words):
        raise ValueError('invalid stored word')
    if type(addr) is not int or not 0<=addr<len(words):raise ValueError('out-of-range address')
    re=_bit(read_enable);we=_bit(write_enable)
    if collision_policy not in ('read_first','write_first','undefined'):
        raise ValueError('collision policy must be declared')
    if we and write_value is not None and (type(write_value) is not int or not 0<=write_value<lim):
        raise ValueError('invalid input word')
    old=words[addr];new=list(words)
    if we:new[addr]=write_value
    read= None if not re else (old if not we or collision_policy=='read_first' else
            new[addr] if collision_policy=='write_first' else None)
    return {'next_words':tuple(new),'read_word':read,
            'read_unknown':bool(re and read is None),
            'collision':bool(re and we),'collision_policy':collision_policy,
            'scope':'abstract memory only; no physical SRAM/DRAM or retention guarantee'}


def four_phase_handshake_step(state,request,acknowledge):
    """Protocol state transition; not a physical CDC synchronizer or analog proof.

    Four-phase return-to-zero request/acknowledge: 00 -> 10 -> 11 -> 01 -> 00.
    """
    req=_bit(request);ack=_bit(acknowledge)
    legal={'IDLE':{(0,0):'IDLE',(1,0):'REQUESTED'},
           'REQUESTED':{(1,0):'REQUESTED',(1,1):'ACKNOWLEDGED'},
           'ACKNOWLEDGED':{(1,1):'ACKNOWLEDGED',(0,1):'RETURNING'},
           'RETURNING':{(0,1):'RETURNING',(0,0):'IDLE'}}
    if state not in legal or (req,ack) not in legal[state]:
        raise ValueError('illegal handshake transition; data or CDC fault')
    return legal[state][(req,ack)]


def rc_midpoint_delay_uncertainty(resistance_ohm,capacitance_F,
                                  sigma_resistance_ohm,sigma_capacitance_F,covariance_R_C=0.0):
    """First-order covariance propagation for t_50=ln(2) R C; not calibration.

    Linearized near nominal, not guaranteed for large relative uncertainties.
    """
    r=_f('R',resistance_ohm,positive=True);c=_f('C',capacitance_F,positive=True)
    sr=_f('sigma R',sigma_resistance_ohm,nonnegative=True)
    sc=_f('sigma C',sigma_capacitance_F,nonnegative=True)
    cov=_f('cov R,C',covariance_R_C)
    if abs(cov)>sr*sc*(1+1e-12):
        raise ValueError('covariance outside positive-semidefinite 2x2 envelope')
    factor=math.log(2);dr=factor*c;dc=factor*r
    var=dr*dr*sr*sr+dc*dc*sc*sc+2*dr*dc*cov
    if var<0 and abs(var)<1e-12*(abs(dr*sr)+abs(dc*sc))**2:var=0.0
    if var<0 or not math.isfinite(var):raise ValueError('invalid propagated variance')
    return {'nominal_t50_s':factor*r*c,'linearized_sigma_t50_s':math.sqrt(var),
            'method':'first-order covariance propagation','physically_calibrated':False}
