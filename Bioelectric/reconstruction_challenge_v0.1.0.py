#!/usr/bin/env python3
"""ATLAS original Bioelectric finite offline science challenge (nonclinical).

Checks SI electrochemistry, RC, cable conservation, squid HH, abstract FHN,
ADC/synthetic impedance and explicit science/medical HOLD. No human/animal
experiments or physical stimulation settings in this program.
"""
from pathlib import Path
import hashlib,json,math,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from bioelectric_atlas.foundations import nernst_potential,ghk_voltage,passive_membrane_voltage
from bioelectric_atlas.cable import cable_step,cable_charge_coulombs
from bioelectric_atlas.hodgkin_huxley import hh_rest_state,hh_trace
from bioelectric_atlas.excitability import FHNState,fhn_trace
from bioelectric_atlas.instruments import adc_ideal_quantize,electrode_dummy_impedance


def run():
    Ek=nernst_potential(1,140,5,310.15)
    onlyk=ghk_voltage(1,0,0,140,5,10,110,4,104,310.15)
    assert abs(Ek-onlyk)<1e-12
    passive=passive_membrane_voltage(.1,0,1e-6,1e-3,0.001)
    assert abs(passive['voltage_volts']-.1/math.e)<1e-12
    cable_before=(0.0,0,1,0,0)
    cable_after=cable_step(cable_before,.1,1,1,0,0)
    assert abs(sum(cable_after)-sum(cable_before))<1e-12
    hh=hh_trace(100,0.01,0)
    assert len(hh['membrane_mV'])==101 and not hh['medical_device_applicability']
    fhn=fhn_trace(FHNState(-1,0),100,0.01)
    assert fhn['final_state'] and not fhn['diagnostic_or_therapeutic_validity']
    dummy=electrode_dummy_impedance(100,900,1e-6,0)
    assert abs(dummy['real_ohm']-1000)<1e-10
    adc=adc_ideal_quantize(0.5,0,1,10)
    assert not adc['clipped']
    entries={'E_K_millivolts':1000*Ek,'passive_millivolts_after_one_tau':1000*passive['voltage_volts'],
      'cable_after':list(cable_after),'hh_final_millivolts':hh['membrane_mV'][-1],
      'fhn_final':list(fhn['final_state']), 'dummy_DC_ohm':dummy['real_ohm'],
      'adc_code':adc['code']}
    digest=hashlib.sha256(json.dumps(entries,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
    return {'schema':'atlas.bioelectric-reconstruction-challenge/1','status':'passed_software_only',
      'numerical_results':entries,'output_sha256':digest,
      'physical_biological_samples_tested':0,'publisher_original_files_authenticated':0,
      'independent_expert_scientific_review':False,'living_subjects_experimented_on':False,
      'medical_device_electrical_safety_approved':False,'body_connected_or_mains_hardware_authorized':False,
      'next_required':'authenticated sources, calibrated nonclinical apparatus, independent review and qualified ethical protocol'}

if __name__=='__main__':
    x=run();print(json.dumps(x,indent=2))
    if len(sys.argv)>1:
        p=Path(sys.argv[1]);p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(x,indent=2)+'\n')
