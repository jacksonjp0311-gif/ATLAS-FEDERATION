"""Original bounded synthetic chemistry cases, not experimental chemical data."""
from hashlib import sha256
from math import isclose
from .advanced import *
from .models import ChemistryModelError


def advanced_casebook():
    cases=[]
    def add(name,result,yes,limit):
        cases.append({'id':name,'result':result,'passed':bool(yes),'data_origin':'original_constructed_math_fixture',
            'limitations':limit,'physical_chemical_experiment_performed':False})
    ionic=balance_charge_and_atoms([
       {'label':'H+','atoms':{'H':1},'charge':1},
       {'label':'OH-','atoms':{'O':1,'H':1},'charge':-1}],[{'label':'H2O','atoms':{'H':2,'O':1},'charge':0}])
    add('ionic acid-base bookkeeping',ionic,ionic['coefficient_vector']==[1,1,1] and ionic['charge_residual']==0,'Charge/atom conservation not proof of physical mixing or safety')
    e=balance_charge_and_atoms([{'label':'Fe3+','atoms':{'Fe':1},'charge':3},
        {'label':'e-','atoms':{},'charge':-1}],[{'label':'Fe2+','atoms':{'Fe':1},'charge':2}])
    add('formal electron conservation',e,e['coefficient_vector']==[1,1,1],'Formal redox bookkeeping not electrolysis protocol')
    g=thermodynamic_reaction_delta([{'id':'A','coefficient':1,'gibbs_formation_J_mol':-1000,'enthalpy_formation_J_mol':-800}],
        [{'id':'B','coefficient':1,'gibbs_formation_J_mol':-3000,'enthalpy_formation_J_mol':-2400}],300)
    add('source-supplied delta Gibbs',g,g['delta_G_standard_J_per_mol_reaction']==-2000,'Formation values are invented and measured conditions unverified')
    v=vanthoff_logK(0,300,400,1000)
    add('vanthoff-temperature-dependence',v,v['logK_target']>0,'ΔH temperature-independent hypothesis only')
    ions=ionic_strength([{'ion':'cation','molarity_mol_L':.01,'charge':1}, {'ion':'anion','molarity_mol_L':.01,'charge':-1}])
    add('molar ionic strength',ions,abs(ions['I_molarity_basis_mol_L']-.01)<1e-12 and ions['electroneutrality_proven'], 'Not activity or ion-speciation proof')
    dh=debye_huckel_limiting_log_gamma(1,.001,.509)
    add('dilute-ion activity warning',dh,0<dh['gamma']<1,'Solvent/temperature coefficient invented for this exercise')
    electrons=semiconductor_carrier_neutrality(1e21,1e16)
    add('donor-majority-carriers',electrons,electrons['electron_density_m3']>electrons['hole_density_m3'],'Full ionization and nondegenerate charge neutrality assumed')
    holes=semiconductor_carrier_neutrality(-1e21,1e16)
    add('acceptor-majority-carriers',holes,holes['hole_density_m3']>holes['electron_density_m3'],'No actual silicon wafer or device measured')
    flux=fick_flux_1d(1e-12,3,1,.001)
    add('Fick-gradient-flux',flux,abs(flux['flux_mol_m2_s']-2e-9)<1e-18,'No real diffusion profile')
    diff=diffuse_no_flux_1d([0.,0.,1.,0.,0.],.1,1,1,20)
    add('reflecting-boundary-diffusion',diff,abs(diff['conserved_relative_residual'])<1e-12 and abs(sum(diff['concentrations_mol_m3'])-1)<1e-10,
        'Synthetic no-flux boundary not semiconductor diffusion furnace data')
    a=beer_lambert_absorbance(100.,1.,.002)
    add('spectroscopic-transmission',a,abs(a['absorbance_decadic']-.2)<1e-12,'No validated real spectrometer or analyte purity')
    sample=b'original constructed document'; digest=sha256(sample).hexdigest()
    src=source_bytes_audit(sample,digest,'authored-reference','cleared_for_archive')
    add('source-bytes-not-proven-authentic',src,src['matches_supplied_expected_digest'] and not src['publisher_origin_authenticated'],
        'Hash match is not authentic publisher provenance or legal license grant')
    bad=source_bytes_audit(sample,'f'*64,'authored-reference','restricted')
    add('mismatched-archive-byte-hash',bad,not bad['matches_supplied_expected_digest'] and not bad['automatically_republishable'],
        'No restricted source redistributed')
    try:debye_huckel_limiting_log_gamma(1,.1,.509);refused=True
    except ChemistryModelError:refused=True
    else:refused=False
    add('dilute-scope-refusal',{'rejected':refused},refused,'A concentration-limit rejection is not a scientific claim about actual concentrated solution')
    return {'schema':'atlas.chemistry-v02-casebook/1','status':'passed' if all(x['passed'] for x in cases) else 'failed',
       'count':len(cases),'cases':cases,'authentic_chemical_experiments':0,
       'source_original_bytes_imported':0,'independent_scientific_review':False}
