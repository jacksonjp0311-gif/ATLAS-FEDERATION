"""Deterministic offline manufacturing casebook, no empirical data or certification."""
from .models import *

def casebook():
    cases={
        'tolerance_fit':tolerance_fit(10.02,10.05,9.97,9.99),
        'signed_stackup_mm':interval_stackup([(10,10.02),(-4.01,-4),(-6.005,-6)]),
        'thermal_length_m':thermal_length(1,12e-6,20),
        'cutting_reference':cutting_estimate(10,100,4,.05,2,5,1500,.85),
        'cantilever_deflection_m':cantilever_deflection(10,1,200e9,1e-8),
        'leadscrew':leadscrew_position(10,1,.02,200),
        'capability_gate':capability(9,11,10,.2),
        'guardband':guardband_verdict(10.9,9,11,.2),
        'calibration':linear_calibration([0,1,2,3],[1,3,5,7]),
        'routing':critical_path({'prepare':{'duration_min':3},'inspect':{'duration_min':2,'requires':['prepare']}}),
        'casting_mm':cast_dimension_from_pattern(100,.02),
        'additive_height_mm':deposited_height(100,.2,.01),
        'discrete_ra_m':roughness_ra([0,1e-6,-1e-6]),
        'thermal_response_K':first_order_thermal_state(310,300,5,2,10,10),
    }
    return {'status':'passed','cases':len(cases),'values':cases,'scope':'bounded mathematical constructed fixtures; not observed manufacturing quality'}
