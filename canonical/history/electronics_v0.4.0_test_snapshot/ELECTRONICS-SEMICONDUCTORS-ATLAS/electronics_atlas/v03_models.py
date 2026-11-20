"""ATLAS FORGE / original Electronics node v0.3.0: bounded reconstruction kernels.

Standard-library-only executable mathematical reference. Does not calibrate silicon,
guarantee metastability resolution, or model transistor fabrication.
"""
from __future__ import annotations
from dataclasses import dataclass
import math


def _real(name, x, lower=None, strict=False):
    if type(x) not in (int, float) or not math.isfinite(x):
        raise ValueError(f"{name}: finite real required")
    if lower is not None and (x <= lower if strict else x < lower):
        raise ValueError(f"{name}: outside valid domain")
    return float(x)


def _bit(x):
    if type(x) is not int or x not in (0, 1):
        raise ValueError("bit must be exactly integer 0 or 1")
    return x


def _solve_dense(matrix, rhs):
    """Pivoted Gaussian elimination, small bounded matrices only.

    Not a production sparse SPD solver. Singularity refuses rather than guessing.
    """
    n = len(rhs)
    if not n or n > 16 or len(matrix) != n or any(len(row) != n for row in matrix):
        raise ValueError("system dimension must be 1..16 and square")
    a = [list(map(float, row)) + [float(rhs[i])] for i, row in enumerate(matrix)]
    if any(not math.isfinite(v) for row in a for v in row):
        raise ValueError("nonfinite linear system")
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(a[i][k]))
        scale = max((abs(a[i][j]) for i in range(k, n) for j in range(k, n)), default=0.)
        if not scale or abs(a[p][k]) < 1e-13 * scale:
            raise ValueError("singular or numerically unresolved linear system")
        a[k], a[p] = a[p], a[k]
        for i in range(k + 1, n):
            f = a[i][k] / a[k][k]
            a[i][k] = 0.
            for j in range(k + 1, n + 1):
                a[i][j] -= f * a[k][j]
    x = [0.] * n
    for k in range(n - 1, -1, -1):
        x[k] = (a[k][-1] - sum(a[k][j] * x[j] for j in range(k + 1, n))) / a[k][k]
    if any(not math.isfinite(v) for v in x):
        raise ValueError("unresolvable numerical scales")
    return x


def rc_nodal_backward_euler(capacitance_F, conductances_S, initial_V,
                           fixed_V, injection_A, step_s):
    """One implicit step C dV/dt + G V = I (grounded nodal network).

    Conductances [(i,j,g)] include grounded node -1; fixed_V maps node -> volts.
    Fixed nodes are ideal prescribed sources. Zero-capacitance unknowns are not
    supported. Returns full voltages and residual of *discretized* KCL.
    """
    n = len(capacitance_F)
    if type(n) is not int or n < 1 or n > 16 or len(initial_V) != n:
        raise ValueError("node count 1..16 and matching vectors required")
    C = [_real("capacitance_F", c, 0, strict=True) for c in capacitance_F]
    old = [_real("initial_V", v) for v in initial_V]
    dt = _real("step_s", step_s, 0, strict=True)
    if type(fixed_V) is not dict or type(injection_A) is not dict:
        raise ValueError("fixed_V and injection_A must be mappings")
    if any(type(i) is not int or not 0 <= i < n for i in list(fixed_V) + list(injection_A)):
        raise ValueError("node identifiers outside graph")
    fixed = {i:_real("fixed voltage",v) for i,v in fixed_V.items()}
    injection = {i:_real("current",v) for i,v in injection_A.items()}
    if any(i in fixed for i in injection):
        raise ValueError("source injection on fixed voltage node must be accounted as unknown supply")
    if not isinstance(conductances_S, (tuple,list)):
        raise ValueError("conductance list required")
    edges = []
    for edge in conductances_S:
        if not isinstance(edge,(tuple,list)) or len(edge)!=3:
            raise ValueError("edge triple required")
        i,j,g=edge
        if type(i) is not int or type(j) is not int or i==j or not (0<=i<n and (j==-1 or 0<=j<n)):
            raise ValueError("invalid edge endpoint")
        edges.append((i,j,_real("conductance",g,0,strict=True)))
    gmat=[[0.]*n for _ in range(n)]
    for i,j,g in edges:
        gmat[i][i]+=g
        if j != -1:
            gmat[j][j]+=g; gmat[i][j]-=g; gmat[j][i]-=g
    unknown=[i for i in range(n) if i not in fixed]
    V=old[:]
    for i,value in fixed.items():V[i]=value
    if unknown:
        a=[];b=[]
        for i in unknown:
            alpha=C[i]/dt
            if not math.isfinite(alpha):raise ValueError("C/dt numerical overflow")
            a.append([gmat[i][j]+(alpha if i==j else 0.) for j in unknown])
            b.append(alpha*old[i]+injection.get(i,0.)-sum(gmat[i][j]*V[j] for j in fixed))
        vals=_solve_dense(a,b)
        for i,v in zip(unknown, vals):V[i]=v
    residual=max((abs(C[i]*(V[i]-old[i])/dt+sum(gmat[i][j]*V[j] for j in range(n))-injection.get(i,0.)) for i in unknown),default=0.)
    res_scale=max([1.]+[abs(injection.get(i,0.))+abs(C[i]*(V[i]-old[i])/dt)+sum(abs(gmat[i][j]*V[j]) for j in range(n)) for i in unknown])
    return {'node_voltages_V': tuple(V), 'kcl_residual_A': residual,
            'relative_kcl_residual':residual/res_scale, 'method':'implicit_backward_euler',
            'known_voltage_nodes': tuple(sorted(fixed)), 'time_step_s':dt}


def charge_supply_energy(capacitance_F, supply_V, rising_events, cycles, frequency_Hz):
    """Idealized capacitor energy accounting; excludes leakage, short circuit, interconnect.

    rising_events counts 0->1 charges over `cycles`. Assumes discharge to 0 V.
    Dynamic supply energy per charge is C*V^2, with 1/2 stored and 1/2 lost
    on charge and 1/2 lost on discharge. Not an energy per arbitrary transition.
    """
    c=_real('capacitance_F',capacitance_F,0,strict=True)
    v=_real('supply_V',supply_V,0)
    f=_real('frequency_Hz',frequency_Hz,0,strict=True)
    if type(cycles) is not int or cycles<1 or type(rising_events) is not int or not 0<=rising_events<=cycles:
        raise ValueError("events and cycles must be nonnegative integers with events <= cycles")
    E=c*v*v*rising_events
    if not math.isfinite(E):raise ValueError("energy overflow")
    return {'supply_energy_J': E, 'mean_dynamic_power_W': E*f/cycles,
            'rising_activity_fraction':rising_events/cycles,
            'capacitor_stored_energy_per_charge_J':.5*c*v*v,
            'limitations':'capacitive only; no leakage, drive overlap, process/thermal effects'}


def nand(a,b):return 1-(_bit(a)&_bit(b))

def nand_xor(a,b):
    x=nand(a,b)
    return nand(nand(a,x),nand(b,x))

def nand_full_adder(a,b,cin):
    """NAND-only full adder. Result (sum, carry); no transistor sizing implied."""
    x=nand_xor(a,b); s=nand_xor(x,cin)
    carry=nand(nand(a,b),nand(x,cin))
    return s,carry

def nand_ripple_add(a,b,width,cin=0):
    if type(width) is not int or not 1<=width<=128 or type(a) is not int or type(b) is not int or a<0 or b<0 or a >= (1<<width) or b >= (1<<width):
        raise ValueError("bounded nonnegative operands and width 1..128 required")
    carry=_bit(cin);result=0
    for shift in range(width):
        bit,carry=nand_full_adder((a>>shift)&1,(b>>shift)&1,carry)
        result |= bit<<shift
    return result,carry


def register_path_timing(period_s, clock_to_q_min_s, clock_to_q_max_s,
                         logic_contamination_s, logic_propagation_s,
                         setup_s, hold_s, capture_skew_s=0.):
    """Single synchronous path. +skew means capture clock occurs *later*.

    Setup: T>=tCQ_max+tPD_logic+tSetup - skew.
    Hold:  tCQ_min+tCD_logic >= tHold + skew.
    Changing clock period cannot cure a hold-time violation.
    """
    T=_real('period_s',period_s,0,strict=True)
    cqmin=_real('clock_to_q_min_s',clock_to_q_min_s,0)
    cqmax=_real('clock_to_q_max_s',clock_to_q_max_s,cqmin)
    cd=_real('logic_contamination_s',logic_contamination_s,0)
    pd=_real('logic_propagation_s',logic_propagation_s,cd)
    setup=_real('setup_s',setup_s,0); hold=_real('hold_s',hold_s,0)
    skew=_real('capture_skew_s',capture_skew_s)
    sm=T+skew-(cqmax+pd+setup)
    hm=cqmin+cd-(hold+skew)
    return {'setup_margin_s':sm,'hold_margin_s':hm,
            'minimum_period_for_setup_s':max(0,cqmax+pd+setup-skew),
            'setup_pass':sm>=-1e-15,'hold_pass':hm>=-1e-15,
            'guaranteed_timing':sm>=-1e-15 and hm>=-1e-15}


@dataclass
class EdgeRegister:
    """Deterministic epistemic register model: None means UNKNOWN, not analog probability."""
    setup_s:float
    hold_s:float
    state:int|None=0
    last_edge_s:float|None=None

    def __post_init__(self):
        self.setup_s=_real('setup_s',self.setup_s,0)
        self.hold_s=_real('hold_s',self.hold_s,0)
        if self.state is not None:_bit(self.state)

    def capture(self, sampled_bit, edge_s, transition_times_s=()):
        b=_bit(sampled_bit)
        edge=_real('edge_s',edge_s)
        if self.last_edge_s is not None and edge<=self.last_edge_s:
            raise ValueError("edge times strictly increasing")
        times=[_real('transition_time_s',t) for t in transition_times_s]
        if any(times[i]>=times[i+1] for i in range(len(times)-1)):
            raise ValueError("transition times must be strictly increasing")
        if any(edge-self.setup_s<=t<=edge+self.hold_s for t in times):
            self.state=None  # Physical metastability may be analog/time-dependent.
        else:self.state=b
        self.last_edge_s=edge
        return self.state


def hamming84_encode(data):
    """SECDED (8,4) extended Hamming: data bits in positions 3,5,6,7."""
    if type(data) is not int or not 0<=data<16:raise ValueError('data nibble 0..15')
    b=[0]*9
    for idx,pos in enumerate((3,5,6,7)):b[pos]=(data>>idx)&1
    for parity in (1,2,4):
        b[parity]=sum(b[pos] for pos in range(1,8) if (pos&parity) and pos!=parity)%2
    b[8]=sum(b[1:8])%2
    return sum(b[pos]<<(pos-1) for pos in range(1,9))


def hamming84_decode(word):
    """Single-bit correction; double-bit detection; triples outside guaranteed scope."""
    if type(word) is not int or not 0<=word<256:raise ValueError('8-bit codeword required')
    b=[0]+[(word>>(pos-1))&1 for pos in range(1,9)]
    syndrome=sum(parity for parity in (1,2,4) if sum(b[pos] for pos in range(1,8) if pos&parity)%2)
    overall=sum(b[1:9])%2
    if syndrome==0 and overall==0:status='clean'
    elif syndrome and overall:
        b[syndrome]^=1;status='corrected_single'
    elif not syndrome and overall:
        b[8]^=1;status='corrected_single'
    else:return {'status':'detected_double','data':None,'corrected_word':None,'syndrome':syndrome}
    nibble=sum(b[pos]<<idx for idx,pos in enumerate((3,5,6,7)))
    corrected=sum(b[pos]<<(pos-1) for pos in range(1,9))
    return {'status':status,'data':nibble,'corrected_word':corrected,'syndrome':syndrome}


def register_bank_step(words, address, value, write_enable):
    """Abstract synchronous word register bank, no physical SRAM/DRAM behavior."""
    if not isinstance(words,(list,tuple)) or not 1<=len(words)<=256:
        raise ValueError('bank requires 1..256 words')
    if type(address) is not int or not 0<=address<len(words):raise ValueError('invalid address')
    if not all(type(w) in (int,type(None)) and (w is None or 0<=w<256) for w in words):
        raise ValueError('word must be unsigned byte or UNKNOWN')
    if value is not None and (type(value) is not int or not 0<=value<256):raise ValueError('value byte or UNKNOWN')
    if type(write_enable) is not bool:raise ValueError('write_enable boolean required')
    new=list(words)
    if write_enable:new[address]=value
    return tuple(new),new[address]
