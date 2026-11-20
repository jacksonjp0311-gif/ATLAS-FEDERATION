"""CHEMISTRY ATLAS 0.1.0 — bounded offline educational chemical arithmetic.

The functions model declared reactions, solution quantities and material parameters;
they are NOT procedures for synthesizing compounds, handling hazardous materials,
operating reactors, etching semiconductors or making any life-safety judgment.

Every result is conditional on caller-provided data and model assumptions.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from functools import reduce
from math import exp,log,log10,isfinite,prod,sqrt,gcd
from pathlib import Path
import re

AVOGADRO=6.02214076e23        # exactly defined elementary entities/mol
ELEMENTARY_CHARGE=1.602176634e-19  # exactly defined coulomb
K_BOLTZMANN=1.380649e-23     # exactly defined J/K
R_GAS=AVOGADRO*K_BOLTZMANN    # derived exactly from defining constants (decimal float is rounded)
FARADAY=AVOGADRO*ELEMENTARY_CHARGE # derived from defining constants

class ChemistryModelError(ValueError):pass

def number(value,name,lower=None,upper=None):
    if type(value) not in (float,int) or not isfinite(value):raise ChemistryModelError(name+' must be finite number')
    value=float(value)
    if lower is not None and value<lower:raise ChemistryModelError(name+' below lower bound')
    if upper is not None and value>upper:raise ChemistryModelError(name+' above upper bound')
    return value

def positive(value,name):
    v=number(value,name,0)
    if v<=0:raise ChemistryModelError(name+' must be positive')
    return v

TOKEN=re.compile(r'[A-Z][a-z]?|\d+|\(|\)')

def parse_formula(formula):
    """Strict neutral formula with nested parenthetical groups. No hydrates/charges."""
    if not isinstance(formula,str) or not 1<=len(formula)<=128:raise ChemistryModelError('bounded neutral chemical formula required')
    tokens=TOKEN.findall(formula)
    if ''.join(tokens)!=formula:raise ChemistryModelError('unsupported formula syntax; no charges, isotopes, hydrates or dots')
    position=0
    def parse_group(nested=False):
        nonlocal position
        result=defaultdict(int)
        while position<len(tokens):
            t=tokens[position]
            if t==')':
                if not nested:raise ChemistryModelError('unmatched closing group')
                break
            if t=='(':
                position+=1; child=parse_group(True)
                if position>=len(tokens) or tokens[position]!=')':raise ChemistryModelError('missing closing group')
                position+=1
            elif t[0].isupper():
                child={t:1};position+=1
            else:raise ChemistryModelError('unexpected multiplier')
            mult=1
            if position<len(tokens) and tokens[position].isdigit():
                mult=int(tokens[position]);position+=1
                if not 1<=mult<=100000:raise ChemistryModelError('invalid multiplier')
            for el,c in child.items():
                result[el]+=c*mult
                if result[el]>1_000_000:raise ChemistryModelError('formula atom count cap')
        if not result:raise ChemistryModelError('empty chemical group')
        return dict(result)
    result=parse_group()
    if position!=len(tokens):raise ChemistryModelError('unbalanced formula groups')
    return dict(sorted(result.items()))

def atom_balance(reactants,products,reactant_coefficients,product_coefficients):
    """Atom conservation in specified neutral species; no reaction feasibility proof."""
    if not all(isinstance(x,list) for x in (reactants,products,reactant_coefficients,product_coefficients)):
        raise ChemistryModelError('lists required')
    if not 1<=len(reactants)==len(reactant_coefficients)<=16 or not 1<=len(products)==len(product_coefficients)<=16:
        raise ChemistryModelError('bounded consistent reaction sides required')
    def tally(species,coefs):
        counts=defaultdict(Fraction)
        for item,f in zip(species,coefs):
            atoms=parse_formula(item)
            if isinstance(f,bool) or not isinstance(f,(int,Fraction)) or f<=0:raise ChemistryModelError('positive integer/rational coefficients required')
            for el,v in atoms.items():counts[el]+=f*v
        return dict(counts)
    a=tally(reactants,reactant_coefficients);b=tally(products,product_coefficients)
    diff={el:str(a.get(el,0)-b.get(el,0)) for el in sorted(set(a)|set(b))}
    return {'schema':'atlas.chem-atom-balance/1','balanced':all(a.get(k,0)==b.get(k,0) for k in diff),'element_residuals':diff,
            'scope':'atomic count only; charge, energy, kinetics, equilibrium and practical feasibility NOT checked'}

def _lcm(a,b):return abs(a*b)//gcd(a,b) if a and b else 0

def balance_reaction(reactants,products):
    """Find UNIQUE 1-D positive rational nullspace, then primitive coefficients.

    Rejects underdetermined/multiple or non-positive nullspaces rather than
    guessing a chemical equation. No redox charges or isotope labels supported.
    """
    if not isinstance(reactants,list) or not isinstance(products,list) or not 1<=len(reactants)<=8 or not 1<=len(products)<=8:
        raise ChemistryModelError('1..8 reactant/product formula lists required')
    species=reactants+products
    if len(set(species))!=len(species):raise ChemistryModelError('duplicated species not supported')
    parsed=[parse_formula(x) for x in species]
    elems=sorted(set().union(*(p.keys() for p in parsed)))
    if len(elems)>20 or len(species)>12:raise ChemistryModelError('resource cap')
    rows=[[Fraction(p.get(el,0) * (1 if j<len(reactants) else -1)) for j,p in enumerate(parsed)] for el in elems]
    # Deterministic exact reduced-row echelon form over Fraction.
    n=len(species);pivots=[];i=0
    for j in range(n):
        choice=next((k for k in range(i,len(rows)) if rows[k][j]),None)
        if choice is None:continue
        rows[i],rows[choice]=rows[choice],rows[i]
        q=rows[i][j];rows[i]=[v/q for v in rows[i]]
        for k in range(len(rows)):
            if k!=i and rows[k][j]:
                q=rows[k][j];rows[k]=[a-q*b for a,b in zip(rows[k],rows[i])]
        pivots.append(j);i+=1
        if i==len(rows):break
    free=[k for k in range(n) if k not in pivots]
    if len(free)!=1:raise ChemistryModelError('reaction is not uniquely determined by atomic constraints')
    vec=[Fraction(0)]*n;vec[free[0]]=Fraction(1)
    for r,c in enumerate(pivots):vec[c]=-rows[r][free[0]]
    if all(v<0 for v in vec):vec=[-v for v in vec]
    if any(v<=0 for v in vec):raise ChemistryModelError('no positive coefficient solution under requested sides')
    denominator=reduce(_lcm,(v.denominator for v in vec),1)
    ints=[int(v*denominator) for v in vec]
    divisor=reduce(gcd,ints)
    ints=[x//divisor for x in ints]
    if any(x>1_000_000 for x in ints):raise ChemistryModelError('coefficient cap exceeded')
    proof=atom_balance(reactants,products,ints[:len(reactants)],ints[len(reactants):])
    if not proof['balanced']:raise AssertionError('exact nullspace calculation failed conservation')
    return {'schema':'atlas.chem-reaction-balance/1','reactants':dict(zip(reactants,ints[:len(reactants)])),
            'products':dict(zip(products,ints[len(reactants):])),'coefficient_vector':ints,
            'exact_atom_conservation':True,'charge_conservation_checked':False,'physical_reaction_proven':False,
            'limitations':['Neutral molecular formula subset only; isotopes, ionic charges, electrons, phases and hydrates not parsed',
              'Mathematical balancing never demonstrates actual synthesis, safe chemical handling or reaction feasibility']}

def molar_mass(formula,atomic_masses_g_mol):
    atoms=parse_formula(formula)
    if not isinstance(atomic_masses_g_mol,dict) or not atomic_masses_g_mol:raise ChemistryModelError('caller supplied molar masses required')
    total=0.
    for el,count in atoms.items():
        if el not in atomic_masses_g_mol:raise ChemistryModelError('missing atomic mass '+el)
        total+=count*positive(atomic_masses_g_mol[el],el+' molar mass')
    return {'molar_mass_g_mol':total,'formula_atom_counts':atoms,
       'mass_values':'caller supplied; isotopic composition and standard atomic weight uncertainty not inferred'}

def amount_of_substance(mass_g,molar_mass_g_mol):
    m=number(mass_g,'mass g',0);M=positive(molar_mass_g_mol,'molar mass g/mol')
    return {'moles':m/M,'entities_estimate':m/M*AVOGADRO,'standard_mole_definition':'NA exact, material molar mass supplied externally'}

def limiting_extent(available_mol,reactant_coefficients):
    if not isinstance(available_mol,dict) or not isinstance(reactant_coefficients,dict) or set(available_mol)!=set(reactant_coefficients) or not available_mol:
        raise ChemistryModelError('matching reactants and stoichiometry required')
    limits={s:number(q,'amount mol',0)/positive(reactant_coefficients[s],'coefficient') for s,q in available_mol.items()}
    limit=min(limits.values());limiting=sorted(k for k,v in limits.items() if abs(v-limit)<=1e-12*max(1,limit))
    return {'max_reaction_extent_mol':limit,'limiting_species':limiting,'remaining_reactants_mol':{
       k:max(0,available_mol[k]-reactant_coefficients[k]*limit) for k in available_mol},
       'limitations':['100% conversion and complete mixing are assumed, not experimentally established']}

def solution_molarity(solute_mol,solution_liters):
    n=number(solute_mol,'solute mol',0);v=positive(solution_liters,'solution liters')
    return {'molarity_mol_L':n/v,'note':'total final solution volume, not solvent volume; non-ideal volume changes ignored'}

def dilution(C_initial_mol_L,V_initial_L,V_final_L):
    c=number(C_initial_mol_L,'initial concentration',0);v0=number(V_initial_L,'initial liters',0);vf=positive(V_final_L,'final solution liters')
    if vf<v0:raise ChemistryModelError('this function only models dilution, not evaporation')
    return {'final_concentration_mol_L':c*v0/vf,'solute_mol':c*v0,
        'limitations':['Concentration arithmetic, not preparation, mixing, safety or thermodynamic activity']}

def ideal_gas_pressure(moles,T_K,volume_m3):
    n=number(moles,'moles',0);T=positive(T_K,'Kelvin');V=positive(volume_m3,'volume m3')
    return {'pressure_Pa':n*R_GAS*T/V,'gas_constant_J_mol_K':R_GAS,
        'limits':'ideal dilute nonreacting gas, uniform equilibrium; no high-pressure, phase, mixture nonideality'}

def reaction_free_energy(delta_G_standard_j_mol,T_K,reaction_quotient):
    dg=number(delta_G_standard_j_mol,'standard reaction ΔG J/mol');t=positive(T_K,'Kelvin');Q=positive(reaction_quotient,'dimensionless Q')
    change=dg+R_GAS*t*log(Q)
    return {'delta_G_reaction_j_mol':change,'spontaneous_forward_thermodynamically_favored':change<0,
       'kinetically_fast_proven':False,'activity_based_quotient_required':True,
       'limits':'constant T, specified reference states, dimensionless activities; not an actual reaction-rate prediction'}

def equilibrium_constant(delta_G_standard_j_mol,T_K):
    dg=number(delta_G_standard_j_mol,'standard reaction Gibbs J/mol');t=positive(T_K,'Kelvin')
    lnK=-dg/(R_GAS*t)
    return {'ln_K_dimensionless':lnK,'K_dimensionless':exp(lnK) if -700<lnK<700 else None,
       'limits':'dimensionless activities and specified standard states; K omitted to avoid overflow/underflow'}

def reaction_enthalpy(formation_enthalpies_j_mol,reactant_coeffs,product_coeffs):
    if not isinstance(formation_enthalpies_j_mol,dict) or not isinstance(reactant_coeffs,dict) or not isinstance(product_coeffs,dict):raise ChemistryModelError('dicts required')
    if not reactant_coeffs or not product_coeffs:raise ChemistryModelError('nonempty reaction required')
    balance=0.
    for sign,side in [(-1,reactant_coeffs),(1,product_coeffs)]:
        for k,c in side.items():
            if k not in formation_enthalpies_j_mol:raise ChemistryModelError('missing formation enthalpy '+str(k))
            balance+=sign*positive(c,'coefficient')*number(formation_enthalpies_j_mol[k], 'formation enthalpy')
    return {'delta_H_reaction_j_per_extent_mol':balance,
      'scope':'Hess law with compatible formation enthalpies for the SAME phases/reference state, not heat measured'}

def arrhenius_log_ratio(Ea_j_mol,T1_K,T2_K):
    Ea=number(Ea_j_mol,'activation energy',0);t1=positive(T1_K,'T1');t2=positive(T2_K,'T2')
    value=-Ea/R_GAS*(1/t2-1/t1)
    return {'ln_k2_over_k1':value,'k2_over_k1':exp(value) if -700<value<700 else None,
       'scope':'Arrhenius activation energy constant over temperatures, not proof of a reaction mechanism'}

def first_order_kinetics(initial_concentration_mol_L,rate_constant_per_s,seconds):
    c=number(initial_concentration_mol_L,'initial concentration',0);k=number(rate_constant_per_s,'first order k',0);t=number(seconds,'seconds',0)
    return {'concentration_mol_L':c*exp(-k*t),'half_life_s':log(2)/k if k>0 else None,
       'model':'closed elementary effective first-order loss, k constant in 1/s; not real chemistry safety'}

def pH_from_activity(hydrogen_ion_activity):
    a=positive(hydrogen_ion_activity,'dimensionless hydrogen ion activity')
    return {'pH':-log10(a),'activity_not_concentration':True,
       'scope':'thermodynamic activity relative to standard convention; pH may be negative or >14'}

def henderson_hasselbalch(pKa,base_activity,acid_activity):
    pka=number(pKa,'pKa');b=positive(base_activity,'dimensionless base activity');a=positive(acid_activity,'dimensionless acid activity')
    return {'pH_ideal_ratio':pka+log10(b/a),'scope':'assumes conjugate pair equilibrium, appropriate activity conventions; pH not a preparation recipe'}

def nernst_potential(E_standard_V,electrons,T_K,quotient):
    E0=number(E_standard_V,'standard potential V');t=positive(T_K,'Kelvin');Q=positive(quotient,'dimensionless activity quotient')
    if type(electrons)!=int or not 1<=electrons<=100:raise ChemistryModelError('electron count positive integer')
    return {'potential_V':E0-R_GAS*t/(electrons*FARADAY)*log(Q),'faraday_C_mol':FARADAY,
      'limits':'ideal reversible cell thermodynamics, activity-based quotient, measured standard potentials needed, not battery safety or operational voltage under load'}

def faraday_charge(moles_electrons):
    n=number(moles_electrons,'moles electrons',0)
    return {'charge_C':n*FARADAY,'F_C_per_mol':FARADAY,'origin':'exact SI defining constants, output rounded to binary float'}

def conductivity_semiconductor(electrons_m3,holes_m3,mu_e_m2_Vs,mu_h_m2_Vs):
    n=number(electrons_m3,'electron density m^-3',0);p=number(holes_m3,'hole density m^-3',0)
    mn=number(mu_e_m2_Vs,'electron mobility',0);mp=number(mu_h_m2_Vs,'hole mobility',0)
    sigma=ELEMENTARY_CHARGE*(n*mn+p*mp)
    return {'conductivity_S_m':sigma,'resistivity_ohm_m':1/sigma if sigma>0 else None,
      'scope':'homogeneous linear drift model with caller-supplied carrier concentrations and mobilities, no contact effects, doping activation, temperature or defects inferred'}

def diffusion_length(D_m2_s,seconds,dimensions=1):
    D=number(D_m2_s,'diffusivity',0);t=number(seconds,'time seconds',0)
    if type(dimensions)!=int or not 1<=dimensions<=3:raise ChemistryModelError('spatial dimensions 1..3')
    return {'rms_displacement_m':sqrt(2*dimensions*D*t),'scope':'ideal independent Brownian diffusion, constant D; not a furnace doping or gas handling protocol'}

def mass_balance_process(inputs_kg,outputs_kg,inventory_change_kg):
    if not isinstance(inputs_kg,list) or not isinstance(outputs_kg,list):raise ChemistryModelError('input/output lists')
    inflow=sum(number(x,'input mass kg',0) for x in inputs_kg)
    outflow=sum(number(x,'output mass kg',0) for x in outputs_kg)
    change=number(inventory_change_kg,'inventory delta kg')
    residual=inflow-outflow-change
    return {'mass_in_kg':inflow,'mass_out_kg':outflow,'inventory_change_kg':change,
     'unaccounted_residual_kg':residual,'relative_residual':residual/max(1,inflow,outflow,abs(change)),
     'scope':'material accounting only; cannot identify missing species, emissions, leaks or instrument error'}
