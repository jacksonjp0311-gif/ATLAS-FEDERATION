"""ATLAS FORGE original federation — Electronics/Semiconductors v0.2.

Bounded, reference-scale mathematics; no measured silicon parameters or circuit qualification.
All physical inputs are SI. Standard library only and deterministic.
"""
from __future__ import annotations
import math
from .models import Q, K_B, thermal_voltage, ideal_nmos_current, rc_step


def _real(name, x, minimum=None, strict=False):
    if isinstance(x, bool) or not isinstance(x, (float, int)) or not math.isfinite(x):
        raise ValueError(f'{name} must be a finite real value')
    if minimum is not None and (x <= minimum if strict else x < minimum):
        raise ValueError(f'{name} outside allowed range')
    return float(x)


def bernoulli_stable(z):
    """B(z)=z/(exp(z)-1), B(0)=1; avoids overflow and cancellation."""
    z = _real('dimensionless z', z)
    if z > 50:
        u = math.exp(-z)
        return z*u/(1-u)
    if z < -50:
        u = math.exp(z)
        return (-z)/(1-u)
    if abs(z) < 1e-3:
        w=z*z
        return 1-z/2+w*(1/12+w*(-1/720+w/30240))
    return z/math.expm1(z)


def sg_electron_current(n_left_m3, n_right_m3, field_V_m,
                        length_m, mobility_m2_Vs, temperature_K):
    """Exact constant-field, constant-mobility fitted *electron charge* current.

    Particle flux F = (D/L) [B(-Pe)n_L - B(Pe)n_R],
    Pe= -q E L/(k_B T), J_n=-q F, D=mu k_BT/q.
    Positive J_n means conventional current along +x, so J_n=q*mu*n*E
    when n_L=n_R and drift alone is present.
    """
    n_l=_real('left electron density', n_left_m3, 0)
    n_r=_real('right electron density', n_right_m3, 0)
    E=_real('electric field', field_V_m)
    L=_real('length', length_m, 0, strict=True)
    mu=_real('mobility', mobility_m2_Vs, 0, strict=True)
    Vt=thermal_voltage(temperature_K)
    Pe=-E*L/Vt
    if not math.isfinite(Pe):raise ValueError('Peclet number overflow')
    d=mu*Vt
    F=(d/L)*(bernoulli_stable(-Pe)*n_l-bernoulli_stable(Pe)*n_r)
    J=-Q*F
    if not math.isfinite(J):raise ValueError('nonfinite electron current')
    return J


def minority_diffusion_profile(n_left_m3,n_right_m3,length_m,diffusion_m2_s,
                                lifetime_s,cells=32):
    """Solve D u''-u/tau=0, positive Dirichlet BC, via tridiagonal M-matrix.

    With particle flux F=-D u', exact discrete conservation is
    F_right-F_left+ dx * sum(interior u_i)/tau == 0.
    Returns all cells+1 nodes, face fluxes, and conservation residual.
    """
    left=_real('left excess density',n_left_m3,0)
    right=_real('right excess density',n_right_m3,0)
    L=_real('length',length_m,0,strict=True)
    D=_real('diffusion',diffusion_m2_s,0,strict=True)
    tau=_real('lifetime',lifetime_s,0,strict=True)
    if type(cells) is not int or not 4 <= cells <= 512:
        raise ValueError('cells must be int in [4,512]')
    dx=L/cells
    ratio=dx*dx/(D*tau)
    if not math.isfinite(ratio) or ratio>1e200:raise ValueError('unresolvable physical scales')
    m=cells-1
    diag=[2.+ratio]*m
    rhs=[0.]*m; rhs[0]+=left;rhs[-1]+=right
    # standard Thomas algorithm for diagonal 2+r² and offdiagonal -1
    for i in range(1,m):
        factor=-1./diag[i-1]
        diag[i]+=factor
        rhs[i]-=factor*rhs[i-1]
    interior=[0.]*m
    interior[-1]=rhs[-1]/diag[-1]
    for i in range(m-2,-1,-1):
        interior[i]=(rhs[i]+interior[i+1])/diag[i]
    vals=(left,*interior,right)
    faces=tuple(-D*(vals[i+1]-vals[i])/dx for i in range(cells))
    recomb=sum(interior)*dx/tau
    residual=faces[-1]-faces[0]+recomb
    if not all(math.isfinite(v) and v>=-1e-10*max(left,right,1) for v in vals):
        raise ArithmeticError('positivity or finiteness lost')
    return {'density_m3':vals,'particle_flux_m2_s':faces,
            'integrated_recombination_m2_s':recomb,
            'discrete_conservation_residual_m2_s':residual,'dx_m':dx}


def minority_analytic(x_m,n_left_m3,n_right_m3,length_m,diffusion_m2_s,lifetime_s):
    x=_real('position',x_m,0)
    L=_real('length',length_m,0,strict=True)
    if x>L*(1+1e-12):raise ValueError('position beyond domain')
    x=min(x,L)  # clamp floating-point grid-end rounding only
    l=_real('left density',n_left_m3,0)
    r=_real('right density',n_right_m3,0)
    D=_real('diffusion',diffusion_m2_s,0,strict=True)
    tau=_real('lifetime',lifetime_s,0,strict=True)
    Ld=math.sqrt(D*tau)
    t=L/Ld
    if not math.isfinite(t):raise ValueError('unresolvable diffusion length')
    def ratio(a):
        if t < 40: return math.sinh(a)/math.sinh(t)
        return math.exp(a-t)*(-math.expm1(-2*a))/(-math.expm1(-2*t))
    return l*ratio((L-x)/Ld)+r*ratio(x/Ld)


def resistor_network(node_count,edges,prescribed_potentials_V,current_injections_A=None):
    """KCL in connected resistor graphs with at least one fixed V per component.

    Current_injections_A[i] is external current injected *into* node i.
    Returns fixed-node reaction currents from the voltage sources and
    an audit of Joule loss vs external electrical power.
    """
    if type(node_count) is not int or not 2 <= node_count <= 64:
        raise ValueError('node_count 2..64 required')
    if not isinstance(prescribed_potentials_V,dict) or not prescribed_potentials_V:
        raise ValueError('reference voltages required')
    def node(name,k):
        if type(k) is not int or not 0<=k<node_count:
            raise ValueError(f'{name} invalid node index')
        return k
    fixed={node('fixed',i):_real('fixed potential',v) for i,v in prescribed_potentials_V.items()}
    inject={node('injection',i):_real('injected current',v) for i,v in (current_injections_A or {}).items()}
    ggraph=[[] for _ in range(node_count)]
    parsed=[]
    for item in edges:
        if len(item)!=3:raise ValueError('each edge is (node_a,node_b,R_ohm)')
        a,b,res=item;a=node('edge',a);b=node('edge',b)
        if a==b:raise ValueError('self loops not allowed')
        R=_real('resistance',res,0,strict=True)
        g=1/R
        if not math.isfinite(g) or g==0:raise ValueError('unrepresentable conductance')
        parsed.append((a,b,g,R));ggraph[a].append(b);ggraph[b].append(a)
    # Every floating connected component makes the matrix singular.
    seen=set()
    for start in range(node_count):
        if start in seen:continue
        stack=[start];component=set()
        while stack:
            j=stack.pop()
            if j in component:continue
            component.add(j);stack.extend(ggraph[j])
        seen|=component
        if not component.intersection(fixed):
            raise ValueError('floating network component without fixed potential')
    unknown=[i for i in range(node_count) if i not in fixed]
    indices={k:i for i,k in enumerate(unknown)}
    m=len(unknown)
    A=[[0.]*m for _ in range(m)]
    rhs=[inject.get(i,0.) for i in unknown]
    for a,b,g,R in parsed:
        for x,y in ((a,b),(b,a)):
            if x in indices:
                k=indices[x];A[k][k]+=g
                if y in indices:A[k][indices[y]]-=g
                else:rhs[k]+=g*fixed[y]
    for k in range(m):
        pivot=max(range(k,m),key=lambda t:abs(A[t][k]))
        if abs(A[pivot][k])<=1e-14*max((abs(A[i][i]) for i in range(m)),default=0):
            raise ValueError('near-singular conductance system')
        if pivot!=k:
            A[pivot],A[k]=A[k],A[pivot];rhs[pivot],rhs[k]=rhs[k],rhs[pivot]
        for i in range(k+1,m):
            f=A[i][k]/A[k][k]
            if f==0:continue
            for j in range(k,m): A[i][j]-=f*A[k][j]
            rhs[i]-=f*rhs[k]
    x=[0.]*m
    for i in range(m-1,-1,-1):
        x[i]=(rhs[i]-sum(A[i][j]*x[j] for j in range(i+1,m)))/A[i][i]
    potential=[fixed.get(i,x[indices[i]] if i in indices else 0.) for i in range(node_count)]
    kcl=[-inject.get(i,0.) for i in range(node_count)]
    power=0.
    edge_current=[]
    for a,b,g,R in parsed:
        curr=g*(potential[a]-potential[b])
        edge_current.append(curr)
        kcl[a]+=curr;kcl[b]-=curr
        power+=curr*curr*R
    reaction={i:kcl[i] for i in fixed}
    delivered=sum(potential[i]*inject.get(i,0.) for i in range(node_count)) + sum(potential[i]*reaction[i] for i in fixed)
    residual=max((abs(kcl[i]) for i in unknown),default=0.)
    if not all(math.isfinite(v) for v in potential+[power,delivered,residual]):
        raise ValueError('nonfinite circuit result')
    return {'node_voltages_V':tuple(potential),'edge_currents_A':tuple(edge_current),
            'fixed_reaction_A':reaction,'unknown_kcl_residual_A':residual,
            'resistive_power_W':power,'injected_plus_supply_power_W':delivered}


def ideal_cmos_inverter_output(vin_V,vdd_V,kn_A_per_V2,kp_A_per_V2,
                               vtn_V,vtp_abs_V):
    """Unique DC root of square-law NMOS and symmetric PMOS currents.

    No subthreshold, body, velocity saturation or channel-length modulation.
    Values in a both-off DC plateau are explicitly refused as indeterminate.
    """
    vdd=_real('supply',vdd_V,0,strict=True)
    vin=_real('input',vin_V,0)
    if vin>vdd:raise ValueError('input outside supply rails')
    kn=_real('kn',kn_A_per_V2,0,strict=True)
    kp=_real('kp',kp_A_per_V2,0,strict=True)
    vtn=_real('n threshold',vtn_V,0)
    vtp=_real('p threshold magnitude',vtp_abs_V,0)
    if vin<=vtn and vdd-vin<=vtp:
        raise ValueError('both devices off: DC output indeterminate')
    # With ideal lambda=0 square-law devices, both branches can saturate over a
    # finite interval with identical currents. DC voltage is NOT identifiable.
    vovn=max(0.,vin-vtn);vovp=max(0.,vdd-vin-vtp)
    plateau_lo=vovn;plateau_hi=vdd-vovp
    if plateau_hi>plateau_lo+1e-12*vdd:
        isn=0.5*kn*vovn*vovn; isp=0.5*kp*vovp*vovp
        if abs(isn-isp)<=1e-13*max(isn,isp,1e-100):
            raise ValueError('ideal saturation plateau: output is not uniquely determined')
    def mismatch(vout):
        n=ideal_nmos_current(kn,vin,vout,vtn)
        p=ideal_nmos_current(kp,vdd-vin,vdd-vout,vtp)
        return n-p
    low=0.;high=vdd
    if mismatch(low)>=0:return low
    if mismatch(high)<=0:return high
    for _ in range(90):
        mid=(low+high)/2
        if mismatch(mid)>0:high=mid
        else:low=mid
    return (low+high)/2


def noise_margins_from_characterization(vol_V,voh_V,vil_V,vih_V,vdd_V):
    """Compute NM_L=V_IL-V_OL and NM_H=V_OH-V_IH from characterized thresholds.
    This does NOT infer noise margins from an ideal square-law model.
    """
    vdd=_real('vdd',vdd_V,0,strict=True)
    vol=_real('vol',vol_V,0)
    voh=_real('voh',voh_V,0)
    vil=_real('vil',vil_V,0)
    vih=_real('vih',vih_V,0)
    if not (vol<=vil<vih<=voh<=vdd):
        raise ValueError('unacceptable logic-level ordering or negative margin')
    return (vil-vol,voh-vih)


def full_adder(a,b,carry_in):
    """Ideal Boolean full adder; not a timed or fabricated gate."""
    vals=(a,b,carry_in)
    if any(type(x) not in (bool,int) or x not in (0,1) for x in vals):
        raise ValueError('full-adder operands must be binary')
    s=int(a)^int(b)^int(carry_in)
    c=(int(a)&int(b)) | ((int(a)^int(b))&int(carry_in))
    return (s,c)


def ripple_adder_unsigned(a,b,width,carry_in=0):
    """Reconstruct n-bit unsigned integer adder from single-bit gates."""
    if type(width) is not int or not 1<=width<=64:
        raise ValueError('width must be 1..64')
    limit=1<<width
    if type(a) is not int or not 0<=a<limit or type(b) is not int or not 0<=b<limit:
        raise ValueError('operands out of unsigned word range')
    if type(carry_in) is not int or carry_in not in (0,1):
        raise ValueError('carry in must be 0 or 1')
    carry=carry_in;result=0
    for i in range(width):
        s,carry=full_adder((a>>i)&1,(b>>i)&1,carry)
        result |=s<<i
    return (result,carry)


def diode_current_local_uncertainty(Is_A,V_V,T_K,ideality,sigma_V,sigma_T,cov_V_T=0.):
    """Linear covariance propagation *with Is held constant* (unphysical across
    wide temperatures). Returns I, partial derivatives, and first-order sigma.
    """
    Is=_real('Is',Is_A,0,strict=True)
    V=_real('voltage',V_V)
    T=_real('kelvin',T_K,0,strict=True)
    n=_real('ideality',ideality,0,strict=True)
    sv=_real('sigma voltage',sigma_V,0)
    st=_real('sigma kelvin',sigma_T,0)
    cov=_real('voltage-temperature covariance',cov_V_T)
    if abs(cov)>sv*st+1e-30:
        raise ValueError('covariance violates Cauchy–Schwarz bound')
    x=V/(n*thermal_voltage(T))
    if x>700:raise ValueError('overflow outside reference scope')
    e=math.exp(x)
    I=Is*math.expm1(x)
    dV=Is*e/(n*thermal_voltage(T))
    dT=-Is*e*x/T
    variance=dV*dV*sv*sv+dT*dT*st*st+2*dV*dT*cov
    if variance < -1e-14*max((dV*sv)**2,(dT*st)**2,1e-300):
        raise ValueError('non-positive propagated variance')
    return {'current_A':I,'dI_dV_A_per_V':dV,'dI_dT_A_per_K':dT,
            'first_order_sigma_A':math.sqrt(max(0.,variance)),'fixed_Is_with_temperature':True}
