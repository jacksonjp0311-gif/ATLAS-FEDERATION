"""Reconstruction-grade original test fixtures, no actual chemical experiments."""
from math import isclose,log,exp
from .v1_models import *
from .models import ChemistryModelError

def casebook_v1():
    cases=[]
    def add(name,x,ok,limit):cases.append({'id':name,'passed':bool(ok),'output':x,'origin':'author_constructed_offline_fixture','limits':limit})
    x=photon_bandgap(500,2)
    add('Photon energy and supplied semiconductor gap',x,x['energetically_above_supplied_gap'],
       'Energy above the gap does not guarantee light absorption or a working photodiode')
    x=varshni_bandgap(300,1.17,4.73e-4,636)
    add('Empirical bandgap temperature dependence',x,1.0<x['bandgap_eV']<1.17,
       'Fit parameters invented for teaching and no independent calibration performed')
    x=intrinsic_carrier_density(2e25,1e25,1.12,300)
    add('Intrinsic carrier statistics',x,x['intrinsic_carrier_density_m3']>0,
       'Density-of-states input is asserted, not measured; no wafer quality assessment')
    x=diode_ideal_current(1e-12,0,.95,300)
    add('Ideal diode zero-bias current',x,x['current_A']==0,
       'No actual diode measured or fabricated')
    x=shomate_thermochemistry(30,2,0,0,0,300,400,250,500)
    add('Shomate heat capacity integral',x,abs(x['delta_H_J_mol']-(30*100+2*((400/1000)**2-(300/1000)**2)*1000/2))<1e-8,
       'Hypothetical coefficients, single phase, no reference thermochemical data acquired')
    x=equilibrium_with_heat_capacity(298.15,350,-100000,-200,20)
    add('Reaction ΔCp and log equilibrium constant',x,isclose(x['delta_H_J_mol'],-100000+20*(350-298.15)),
       'No real reaction or measured equilibrium state')
    x=electrochemical_work_bound(1.2,1,.8)
    add('Electrochemical reversible-work accounting',x,x['illustrative_delivered_work_J']<x['reversible_work_magnitude_J'],
       'Not battery chemistry specification or construction')
    x=faradaic_yield(96485.33212331002,1,.9)
    add('Faraday charge-to-moles conversion',x,0.89<x['illustrative_product_mol']<.91,
       'No actual electrolysis or chemical identity')
    x=bragg_first_order_spacing(.15406,30)
    add('Bragg interplanar spacing',x,isclose(x['d_spacing_nm'],.15406,rel_tol=1e-12),
       'A spacing is not a material-phase identification')
    x=uncertainty_product(2,3,.1,.2,0)
    add('First-order measurement uncertainty',x,isclose(x['standard_uncertainty'],(.09+.16)**.5),
       'Uncertainties and correlations invented, not calibrated')
    for label, fn in [('Missing calibration blocks extrapolation',lambda:shomate_thermochemistry(30,0,0,0,0,250,500,270,450)),
       ('Invalid cell temperature rejected',lambda:diode_ideal_current(1e-12,1,1,0)),
       ('Invalid covariance rejected',lambda:uncertainty_product(1,2,0,0,.01)),
       ('Noninteger electrons rejected',lambda:faradaic_yield(1000,1.5))]:
        refused=False
        try:fn()
        except ChemistryModelError:refused=True
        add(label,{'refused':refused},refused,'Rejected out-of-domain or contradictory input; no field evidence')
    return {'schema':'atlas.chem-v1-casebook/1','status':'passed' if all(x['passed'] for x in cases) else 'failed',
       'count':len(cases),'cases':cases,'real_laboratory_experiments':0,'independent_peer_review':False,
       'independent_original_primary_source_bytes':0,'actual_semiconductor_fabrication':False}
