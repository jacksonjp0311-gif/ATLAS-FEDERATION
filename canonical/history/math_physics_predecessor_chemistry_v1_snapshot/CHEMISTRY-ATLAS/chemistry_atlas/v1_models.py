"""Chemistry Atlas 1.0 — bounded scientific continuity calculations.

No chemical synthesis, semiconductor fabrication, hazardous substance handling,
equipment control, or independently verified field characterization is performed.
Every parameter is caller-provided, source/state conventions are explicit.
"""
from __future__ import annotations
from math import exp,log,log1p,sqrt,expm1,isfinite
from hashlib import sha256
from .models import ChemistryModelError,number,positive,R_GAS,FARADAY,ELEMENTARY_CHARGE,K_BOLTZMANN

H_SI=6.62607015e-34   # exact SI defining J s
C_SI=299792458        # exact SI defining m/s


def photon_bandgap(wavelength_nm,bandgap_eV):
    """Photon energy vs a stated band gap; absorption not guaranteed."""
    lam=positive(wavelength_nm,'wavelength nm');eg=positive(bandgap_eV,'bandgap eV')
    energy=H_SI*C_SI/(lam*1e-9)
    return {'schema':'atlas.chem-v1-photon-bandgap/1','photon_energy_J':energy,
       'photon_energy_eV':energy/ELEMENTARY_CHARGE,'bandgap_eV':eg,
       'energetically_above_supplied_gap':energy/ELEMENTARY_CHARGE>=eg,
       'assumptions':['vacuum wavelength, single photon and caller-supplied gap'],
       'limitations':['Energy exceeding a gap is not proof of absorption, photocurrent, device efficiency or safe photo-processing',
                     'Excitons, phonons, indirect transitions, interfaces and material absorption are omitted']}


def varshni_bandgap(T_K,E0_eV,alpha_eV_K,beta_K):
    """Empirical E_g(T)=E_g(0)-alpha*T^2/(T+beta); coefficients supplied."""
    t=number(T_K,'Kelvin',0);e0=positive(E0_eV,'E(0) eV');a=number(alpha_eV_K,'alpha',0)
    beta=positive(beta_K,'beta K');eg=e0-a*t*t/(t+beta)
    if eg<=0:raise ChemistryModelError('empirical gap model invalid at given T')
    return {'schema':'atlas.chem-v1-varshni/1','temperature_K':t,'bandgap_eV':eg,
        'derivative_eV_K':-a*t*(t+2*beta)/(t+beta)**2,
        'limitations':['Empirical material-specific fit: do not extrapolate outside measured phase/temperature region',
          'Not a device design or proof of optical absorption/transport']}


def intrinsic_carrier_density(Nc_m3,Nv_m3,gap_eV,T_K):
    """Nondegenerate intrinsic carrier statistics; log evaluation for stability."""
    nc=positive(Nc_m3,'Nc m^-3');nv=positive(Nv_m3,'Nv m^-3');eg=positive(gap_eV,'gap eV');T=positive(T_K,'temperature K')
    ln_ni=.5*(log(nc)+log(nv))-eg*ELEMENTARY_CHARGE/(2*K_BOLTZMANN*T)
    ni=exp(ln_ni) if ln_ni>-700 else 0.
    return {'schema':'atlas.chem-v1-intrinsic-carriers/1','ln_carrier_density_per_m3':ln_ni,
        'intrinsic_carrier_density_m3':ni,'log_unit_reference':'natural log numerical density in m^-3',
        'limitations':['Effective density of states and band gap are supplied at target temperature, not derived',
          'Nondegenerate, thermal equilibrium and ideal crystalline material only; traps, dopants, surfaces and devices omitted']}


def diode_ideal_current(Is_A,V_V,ideality,T_K):
    """Ideal Shockley diode teaching formula with numerical saturation guard."""
    Is=positive(Is_A,'saturation current A');v=number(V_V,'applied V');n=positive(ideality,'ideality factor');t=positive(T_K,'Kelvin')
    x=ELEMENTARY_CHARGE*v/(n*K_BOLTZMANN*t)
    if x>690:raise ChemistryModelError('diode model exponential outside safe numerical range')
    return {'schema':'atlas.chem-v1-ideal-diode/1','current_A':Is*expm1(x),'dimensionless_exponent':x,
        'limitations':['Ideal diode equation is not a silicon processing recipe or certified device IV curve',
          'No series/shunt resistance, reverse breakdown, self-heating, high injection, recombination or contacts']}


def shomate_thermochemistry(A,B,C,D,E,T1_K,T2_K,valid_min_K,valid_max_K):
    """Analytic ∫Cp(T)dT and ∫Cp(T)/T dT, using published Shomate form.

    Cp=A+B*t+C*t²+D*t³+E/t² in J/mol/K, t=T/1000 K.
    Inputs are arbitrary authored coefficients unless independently sourced.
    """
    coefs=[number(v,name) for v,name in zip((A,B,C,D,E),('A','B','C','D','E'))]
    t1=positive(T1_K,'T1 Kelvin');t2=positive(T2_K,'T2 Kelvin')
    lo=positive(valid_min_K,'valid range min');hi=positive(valid_max_K,'valid range max')
    if lo>=hi or not(lo<=t1<=hi and lo<=t2<=hi):raise ChemistryModelError('outside specified Shomate validity range')
    A,B,C,D,E=coefs
    def cp(t):return A+B*t+C*t*t+D*t*t*t+E/t**2
    x=t1/1000;y=t2/1000
    delta_H_J_mol=1000*(A*(y-x)+(B/2)*(y*y-x*x)+(C/3)*(y**3-x**3)+(D/4)*(y**4-x**4)-E*(1/y-1/x))
    delta_S_J_mol_K=A*log(y/x)+B*(y-x)+(C/2)*(y*y-x*x)+(D/3)*(y**3-x**3)-(E/2)*(1/y**2-1/x**2)
    return {'schema':'atlas.chem-v1-shomate/1','Cp_T1_J_mol_K':cp(x),'Cp_T2_J_mol_K':cp(y),
        'delta_H_J_mol':delta_H_J_mol,'delta_S_J_mol_K':delta_S_J_mol_K,
        'units':'Cp in J mol^-1 K^-1, H difference J mol^-1, S difference J mol^-1 K^-1',
        'limitations':['Use only for source-verified species, phase, temperature segment and coefficients',
         'Parameter sets not authenticated in this release; no missing phase transitions inferred or independent calorimetry']}


def equilibrium_with_heat_capacity(Tref_K,Ttarget_K,delta_Href_J_mol,delta_Sref_J_mol_K,
                                    delta_Cp_J_mol_K):
    """Constant ΔCp approximation to ΔH(T), ΔS(T), ΔG(T), logK(T)."""
    tr=positive(Tref_K,'reference K');t=positive(Ttarget_K,'target K');
    dh=number(delta_Href_J_mol,'reference deltaH');ds=number(delta_Sref_J_mol_K,'reference deltaS');cp=number(delta_Cp_J_mol_K,'reaction deltaCp')
    h=dh+cp*(t-tr);s=ds+cp*log(t/tr);g=h-t*s
    return {'schema':'atlas.chem-v1-heat-capacity-equilibrium/1','delta_H_J_mol':h,'delta_S_J_mol_K':s,
        'delta_G_J_mol':g,'logK':-g/(R_GAS*t),
        'limitations':['Reaction ΔCp assumed constant in one phase/temperature segment; input standard states must match',
          'A thermodynamic equilibrium position is not kinetic feasibility or safe chemical manufacture']}


def electrochemical_work_bound(E_equilibrium_V,moles_electrons,applied_efficiency=1):
    """Maximum reversible cell electrical work magnitude from given potential, not battery output."""
    e=number(E_equilibrium_V,'cell voltage');n=number(moles_electrons,'electron moles',0)
    eta=number(applied_efficiency,'ideal fractional voltage/energy performance',0,1)
    amount=abs(e)*n*FARADAY
    return {'schema':'atlas.chem-v1-electrochemical-work/1','reversible_work_magnitude_J':amount,
            'illustrative_delivered_work_J':amount*eta,'coulombs_transferred':n*FARADAY,
            'limitations':['This is only the magnitude of a reversible specified cell state; not a validated battery capacity, voltage curve or safety limit',
             'Overpotentials, diffusion, temperature, cycle life, contacts and materials sourcing not modeled']}


def faradaic_yield(charge_C,electrons_per_product,faradaic_efficiency=1):
    """Theoretical moles per known charge; no process design or chemistry identity."""
    charge=number(charge_C,'charge coulombs',0);electrons=positive(electrons_per_product,'integer electron count')
    if type(electrons_per_product) is not int or electrons_per_product>50:raise ChemistryModelError('electron stoichiometry integer 1..50')
    efficiency=number(faradaic_efficiency,'Faradaic efficiency',0,1)
    return {'schema':'atlas.chem-v1-faradaic-yield/1','theoretical_mol':charge/(electrons*FARADAY),
        'illustrative_product_mol':charge*efficiency/(electrons*FARADAY),
        'limitations':['No reaction identity, electrode, electrolyte, purity, side reactions, equipment or hazard specifications',
          'Faradaic efficiency is supplied, not measured; not an electrolysis synthesis recipe']}


def bragg_first_order_spacing(wavelength_nm,theta_deg,order:int=1):
    """Powder XRD geometry nλ=2d sinθ, θ is *Bragg angle*, not 2θ."""
    from math import radians,sin
    lam=positive(wavelength_nm,'X-ray wavelength nm');theta=number(theta_deg,'Bragg theta deg',0,90)
    if type(order) is not int or not 1<=order<=10 or theta==0 or theta>=90:raise ChemistryModelError('valid Bragg reflection order and angle')
    d=order*lam/(2*sin(radians(theta)))
    return {'schema':'atlas.chem-v1-bragg-spacing/1','d_spacing_nm':d,
        'assumptions':'elastic coherent diffraction from parallel planes, correctly calibrated theta and specified wavelength',
        'limitations':['Peak indexing, phase identity, strain, texture, instrument broadening, radiation safety and specimen properties not inferred']}


def uncertainty_product(a,b,u_a,u_b,covariance_ab=0):
    """First-order uncertainty propagation; covariance must be consistent with input SDs."""
    x=number(a,'a');y=number(b,'b');ua=number(u_a,'u_a',0);ub=number(u_b,'u_b',0);cov=number(covariance_ab,'covariance')
    if abs(cov)>ua*ub*(1+1e-12):raise ChemistryModelError('invalid input covariance')
    var=y*y*ua*ua + x*x*ub*ub + 2*x*y*cov
    if var < -1e-9*max(1,y*y*ua*ua+x*x*ub*ub):raise ChemistryModelError('negative propagated variance')
    return {'schema':'atlas.chem-v1-uncertainty-product/1','product':x*y,'standard_uncertainty':sqrt(max(0,var)),
        'limitations':['First-order local approximation only: large nonlinear, non-Gaussian errors require other methods',
          'No instrument calibration or correlation verified from empirical observations']}
