"""Chemistry Atlas 0.2: source-scoped, bounded, offline reference computations.

No compound synthesis, operational etch, chemical exposure, combustion,
medical, hazardous gas or fabrication instructions. Every result is relative to
caller-supplied mathematical species, physical parameters and conditions.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from functools import reduce
from math import exp, log, log10, sqrt, hypot, isfinite, gcd
from hashlib import sha256
from .models import ChemistryModelError,R_GAS,FARADAY,ELEMENTARY_CHARGE,number,positive


def _lcm(a,b):return abs(a*b)//gcd(a,b) if a and b else 0


def balance_charge_and_atoms(reactants:list[dict],products:list[dict])->dict:
    """Exact unique positive stoichiometric nullspace with a formal charge row.

    Species must be supplied as {label,atoms,charge}; the label is not parsed.
    Electron symbol may have atoms={} and charge=-1. Rejects nonunique solves.
    A balanced chemical *notation* does not establish physical reaction.
    """
    if not isinstance(reactants,list) or not isinstance(products,list) or not 1<=len(reactants)<=8 or not 1<=len(products)<=8:
        raise ChemistryModelError('reactant/product list required (1..8 each)')
    entries=reactants+products
    if len(entries)>12:raise ChemistryModelError('bounded species count <=12')
    labels=set();species=[]
    for item in entries:
        if not isinstance(item,dict) or set(item)!={'label','atoms','charge'}:raise ChemistryModelError('exact species fields required')
        label=item['label'];atoms=item['atoms'];charge=item['charge']
        if not isinstance(label,str) or not label or len(label)>100 or label in labels:
            raise ChemistryModelError('unique bounded label required')
        if not isinstance(atoms,dict) or len(atoms)>20:raise ChemistryModelError('bounded atom map required')
        if type(charge) is not int or abs(charge)>20:raise ChemistryModelError('integer formal charge within cap')
        for k,v in atoms.items():
            if not isinstance(k,str) or not k or len(k)>3 or not k[0].isupper() or type(v) is not int or not 1<=v<=100000:
                raise ChemistryModelError('valid element symbol with positive count required')
        if not atoms and charge!=-1:raise ChemistryModelError('empty atom map reserved for formal electron')
        labels.add(label);species.append(item)
    elements=sorted(set(k for x in species for k in x['atoms']))
    if not elements or len(elements)>20:raise ChemistryModelError('at least one element and <=20 types required')
    n=len(species);signs=[1]*len(reactants)+[-1]*len(products)
    rows=[[Fraction(signs[j]*x['atoms'].get(el,0)) for j,x in enumerate(species)] for el in elements]
    rows.append([Fraction(signs[j]*x['charge']) for j,x in enumerate(species)])
    m=len(rows);pivots=[];i=0
    for j in range(n):
        k=next((k for k in range(i,m) if rows[k][j]!=0),None)
        if k is None:continue
        rows[i],rows[k]=rows[k],rows[i];factor=rows[i][j];rows[i]=[z/factor for z in rows[i]]
        for k in range(m):
            if k!=i and rows[k][j]!=0:
                mul=rows[k][j];rows[k]=[a-mul*b for a,b in zip(rows[k],rows[i])]
        pivots.append(j);i+=1
        if i==m:break
    free=[j for j in range(n) if j not in pivots]
    if len(free)!=1:raise ChemistryModelError('not uniquely determined by atom and charge conservation')
    x=[Fraction(0)]*n;x[free[0]]=Fraction(1)
    for r,col in enumerate(pivots):x[col]=-rows[r][free[0]]
    if all(t<0 for t in x):x=[-t for t in x]
    if any(t<=0 for t in x):raise ChemistryModelError('no strictly positive coefficient set for supplied sides')
    denom=reduce(_lcm,(a.denominator for a in x),1)
    integers=[int(t*denom) for t in x];d=reduce(gcd,integers)
    coefficients=[t//d for t in integers]
    if any(c>1000000 for c in coefficients):raise ChemistryModelError('coefficient limit exceeded')
    residuals={el:sum(signs[j]*coefficients[j]*a['atoms'].get(el,0) for j,a in enumerate(species)) for el in elements}
    charge_residual=sum(signs[j]*coefficients[j]*a['charge'] for j,a in enumerate(species))
    assert all(z==0 for z in residuals.values()) and charge_residual==0
    return {'schema':'atlas.chem-ionic-stoichiometry/1','reactant_coefficients':dict(zip([r['label'] for r in reactants],coefficients[:len(reactants)])),
      'product_coefficients':dict(zip([r['label'] for r in products],coefficients[len(reactants):])),
      'coefficient_vector':coefficients,'atom_residuals':residuals,'charge_residual':charge_residual,
      'math_conservation_verified':True,'physical_reaction_verified':False,
      'limitations':['Species and charge states are supplied; no solution speciation, charge assignment or actual chemistry proved',
                     'Only unique positive nullspace accepted; underdetermined equations are refused, not guessed',
                     'No synthesis procedure, energy balance, electronic spin, phases, kinetics, or hazard control inferred']}


def thermodynamic_reaction_delta(reactants:list[dict],products:list[dict],temperature_K:float)->dict:
    """∑νΔfG°, ∑νΔfH° from caller-provided same-state property tables.

    Assumes supplied chemical potentials/Gibbs formation energies are at T, not
    extrapolated from 298 K. Values in J/mol and coefficients dimensionless.
    """
    t=positive(temperature_K,'temperature K')
    def calc(rows,name):
        if not isinstance(rows,list) or not 1<=len(rows)<=20:raise ChemistryModelError(name+' 1..20 rows')
        labels=set();out=[0.,0.]
        for row in rows:
            if not isinstance(row,dict) or set(row)!={'id','coefficient','gibbs_formation_J_mol','enthalpy_formation_J_mol'}:
                raise ChemistryModelError('strict formation-energy row schema')
            key=row['id']
            if not isinstance(key,str) or not key or key in labels:raise ChemistryModelError('unique species ID required')
            labels.add(key);nu=positive(row['coefficient'],'coefficient')
            out[0]+=nu*number(row['gibbs_formation_J_mol'],'formation Gibbs J/mol')
            out[1]+=nu*number(row['enthalpy_formation_J_mol'],'formation enthalpy J/mol')
        return out,labels
    p,pids=calc(products,'products');r,rids=calc(reactants,'reactants')
    if pids&rids:raise ChemistryModelError('species repeated on sides unsupported in simple reference')
    dg=p[0]-r[0];dh=p[1]-r[1]
    return {'schema':'atlas.chem-reaction-thermochemistry/1','temperature_K':t,'delta_G_standard_J_per_mol_reaction':dg,
      'delta_H_standard_J_per_mol_reaction':dh,'log_equilibrium_constant':-dg/(R_GAS*t),
      'entropy_or_heat_capacity_independently_verified':False,
      'limitations':['Every supplied formation energy must refer to the same temperature, phases and standard-state convention',
                     'Computing log K does not imply reaction reaches equilibrium, positive kinetics, or safe process',
                     'These data are caller-supplied, not extracted from an authenticated thermochemical publisher file']}


def vanthoff_logK(logK_reference, T_reference_K, T_target_K, delta_H_J_mol):
    log0=number(logK_reference,'reference log K');t0=positive(T_reference_K,'reference K');t=positive(T_target_K,'target K')
    dh=number(delta_H_J_mol,'reaction enthalpy J/mol')
    lk=log0-dh/R_GAS*(1/t-1/t0)
    return {'schema':'atlas.chem-vanthoff/1','logK_target':lk,'ratio_K_target_to_reference':exp(lk-log0) if abs(lk-log0)<690 else None,
     'reference_logK':log0,'temperature_K':t,'assumption':'reaction delta H constant over temperature interval; no phase transition or heat capacity changes',
     'limitations':['No predictive claim for real system without phase-aware thermodynamic data','Huge logK ratio returned as null, not overflow/infinity']}


def ionic_strength(ions:list[dict]):
    """Molarity-based I = 0.5 Σc_i z_i². Returns charge imbalance separately."""
    if not isinstance(ions,list) or not 1<=len(ions)<=256:raise ChemistryModelError('bounded list of ions')
    names=set();total=0.;net=0.
    for ion in ions:
        if not isinstance(ion,dict) or set(ion)!={'ion','molarity_mol_L','charge'}:raise ChemistryModelError('ion exact fields')
        label=ion['ion'];z=ion['charge']
        if not isinstance(label,str) or not label or label in names or type(z)!=int or z==0 or abs(z)>8:raise ChemistryModelError('bounded unique ion/charge')
        names.add(label);c=number(ion['molarity_mol_L'],'ion molarity',0)
        total+=c*z*z*.5;net+=c*z
    return {'schema':'atlas.chem-ionic-strength/1','I_molarity_basis_mol_L':total,'charge_balance_residual_mol_L_equivalent':net,
      'electroneutrality_proven':abs(net)<1e-10,'limitations':['Concentration-basis ionic strength is not an activity model or solution speciation',
      'Ion charges/molarity assigned by user; counterions or dissolved complexes may be missing']}


def debye_huckel_limiting_log_gamma(z:int,ionic_strength_mol_L,A_sqrt_L_per_mol):
    """Dilute-solution limiting model log10 γ≈−A z²√I, A caller supplied."""
    if type(z)!=int or z==0 or abs(z)>8:raise ChemistryModelError('bounded ion charge')
    i=number(ionic_strength_mol_L,'ionic strength mol/L',0)
    a=positive(A_sqrt_L_per_mol,'solvent and temperature specific A')
    if i>0.01:raise ChemistryModelError('limiting law not used above stated dilute ionic-strength cap')
    val=-a*z*z*sqrt(i)
    return {'schema':'atlas.chem-debye-huckel-limiting/1','log10_mean_idealized_gamma':val,'gamma':10**val,
     'limitations':['Only limiting-law illustration at stated low ionic strength; solvent/temp coefficients supplied',
     'No validated activity correction for concentrated mixtures, multicomponent interactions, or specific ion pairing']}


def semiconductor_carrier_neutrality(net_doping_m3,intrinsic_carriers_m3):
    """n−p=N_D−N_A, np=n_i² for ideal nondegenerate full ionization.

    Stable quadratic solution for both donor/acceptor sign cases.
    """
    d=number(net_doping_m3,'net doping number density m^-3');ni=positive(intrinsic_carriers_m3,'intrinsic carrier density m^-3')
    if d>=0:
        n=.5*(d+hypot(d,2*ni));p=ni*ni/n
    else:
        p=.5*(-d+hypot(d,2*ni));n=ni*ni/p
    return {'schema':'atlas.chem-semiconductor-carrier-neutrality/1','electron_density_m3':n,'hole_density_m3':p,
        'mass_action_relative_error':abs(n*p-ni*ni)/max(ni*ni,1e-30),
        'assumptions':['thermal equilibrium, non-degenerate statistics, one temperature, charge-neutral uniform material',
                       'dopants fully ionized and no trap, compensation or interface band-bending'],
        'limitations':['Not validated for degenerate doping, low-temperature freeze-out, high injection, junctions, defects or devices',
                       'Carrier densities cannot be used as a wafer fabrication recipe or material purity certification']}


def fick_flux_1d(D_m2_s,c_left_mol_m3,c_right_mol_m3,spacing_m):
    d=number(D_m2_s,'diffusivity m2/s',0);a=number(c_left_mol_m3,'left concentration',0)
    b=number(c_right_mol_m3,'right concentration',0);dx=positive(spacing_m,'spacing m')
    return {'schema':'atlas.chem-fick-flux/1','flux_mol_m2_s':-d*(b-a)/dx,
      'assumption':'constant effective diffusivity, continuum, concentration-gradient driven transport',
      'limitations':['Nonideal chemical potential gradients, multicomponent diffusion, interfaces and convection omitted']}


def diffuse_no_flux_1d(concentration:list[float],D_m2_s,dx_m,dt_s,steps:int):
    """Explicit 1D finite-volume diffusion with reflecting boundaries; mass-conserving.

    Concentrations are invented abstract samples, not industrial impurity profiles.
    """
    if not isinstance(concentration,list) or not 2<=len(concentration)<=256:
        raise ChemistryModelError('2..256 discretized cells required')
    vals=[number(v,'concentration',0) for v in concentration]
    d=number(D_m2_s,'diffusivity',0);dx=positive(dx_m,'grid spacing');dt=positive(dt_s,'time step')
    if type(steps)!=int or not 0<=steps<=2000 or steps*len(vals)>200000:
        raise ChemistryModelError('simulation resource cap')
    lam=d*dt/(dx*dx)
    if lam>.5+1e-14:raise ChemistryModelError('explicit 1D diffusion CFL lambda exceeds 1/2')
    total_before=sum(vals)*dx
    for _ in range(steps):
        vals=[v+lam*((vals[i-1] if i else v) - 2*v + (vals[i+1] if i<len(vals)-1 else v)) for i,v in enumerate(vals)]
        if min(vals)<-1e-9:raise AssertionError('stable positive transport produced negative concentration')
    total_after=sum(vals)*dx
    return {'schema':'atlas.chem-1d-diffusion/1','concentrations_mol_m3':vals,'integral_before_mol_m2':total_before,
         'integral_after_mol_m2':total_after,'conserved_relative_residual':(total_after-total_before)/max(1.,abs(total_before)),
         'stability_coefficient':lam,'boundary_condition':'zero net flux at both ends',
         'limitations':['Toy one-dimensional constant-D Fickian continuum, no real processing recipe',
                        'Physical D(T), surface reactions, charged dopant transport and geometry omitted']}


def beer_lambert_absorbance(epsilon_L_mol_cm,path_cm,concentration_mol_L):
    e=number(epsilon_L_mol_cm,'molar absorption coefficient',0);l=number(path_cm,'optical path cm',0);c=number(concentration_mol_L,'molarity',0)
    a=e*l*c
    return {'schema':'atlas.chem-absorbance/1','absorbance_decadic':a,
     'transmitted_fraction_ideal':10**(-a) if a<300 else None,
     'scope':'single ideal absorbing species, monochromatic light, no scattering or stray light',
     'limitations':['No independent optical calibration, chemical selectivity, instrument dynamic range or sample identity',
                    'Absorbance is a measurement model, not proof of analyte concentration in unknown real mixtures']}


def source_bytes_audit(raw:bytes|None,expected_sha256:str|None,source_id:str,license_status:str):
    """Byte integrity audit; an authenticated publisher source needs external proof."""
    if not isinstance(source_id,str) or not source_id or len(source_id)>160:raise ChemistryModelError('bounded source identifier')
    if license_status not in ('cleared_for_archive','restricted','unknown'):raise ChemistryModelError('license status invalid')
    if expected_sha256 is not None and (not isinstance(expected_sha256,str) or len(expected_sha256)!=64 or any(v not in '0123456789abcdef' for v in expected_sha256)):
        raise ChemistryModelError('expected SHA-256 lower-hex or null')
    if raw is not None and (type(raw)!=bytes or len(raw)>2_000_000):raise ChemistryModelError('bounded raw bytes <=2MB')
    digest=sha256(raw).hexdigest() if raw is not None else None
    matched=bool(digest is not None and expected_sha256 is not None and digest==expected_sha256)
    return {'schema':'atlas.chem-source-bytes-audit/1','source_id':source_id,'local_bytes_present':raw is not None,
       'sha256_observed':digest,'matches_supplied_expected_digest':matched,
       'license_status_caller_assertion':license_status,'publisher_origin_authenticated':False,
       'copyright_and_license_independently_verified':False,
       'eligible_for_external_rights_review':matched and license_status=='cleared_for_archive',
       'automatically_republishable':False,
       'limitations':['Matching hashes validate only supplied bytes and expected digest, not publisher identity',
                      'Caller-provided rights assertions do not grant actual redistribution rights']}
