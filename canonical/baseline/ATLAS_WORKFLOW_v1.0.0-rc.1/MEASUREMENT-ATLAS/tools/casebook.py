#!/usr/bin/env python3
"""Synthetic, explicitly assumed teaching cases; not measured calibration data."""
from pathlib import Path
import json,sys,math
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from measurement_atlas.uncertainty import type_a,combine_linear,expanded_uncertainty,compare_difference
from measurement_atlas.budget import uncertainty_budget,type_b

def run():
    cases=[]
    def add(id,unit,assumptions,result,checks):
        if not all(checks):raise AssertionError(id)
        cases.append({'id':id,'data_origin':'synthetic_teaching_example','unit':unit,'assumptions':assumptions,'result':result})
    a=type_a([10.0,10.2,9.8,10.1,9.9]);add('repeat_readings','mm',['independent stable readings','values invented for arithmetic'],a,[math.isclose(a['mean'],10),math.isclose(a['standard_uncertainty_mean'],math.sqrt(.005))])
    b=type_b(.3,'uniform');add('uniform_bound','mm',['symmetric uniform distribution is justified by caller'],b,[math.isclose(b['standard_uncertainty'],.3/math.sqrt(3))])
    c=uncertainty_budget([{'name':'repeatability','standard_uncertainty':.1,'sensitivity':1,'output_unit':'mm'},{'name':'calibration','standard_uncertainty':.2,'sensitivity':1,'output_unit':'mm'}],output_unit='mm')
    add('independent_budget','mm',['uncorrelated inputs','units already harmonized','first-order model'],c,[math.isclose(c['combined_variance'],.05)])
    d=compare_difference(12.3,12.2,.04,.09,.03);add('correlated_difference','mm',['supplied covariance .03 mm^2','no conformity decision without a rule'],d,[math.isclose(d['standard_uncertainty_difference'],math.sqrt(.07))])
    e=expanded_uncertainty(.2,2);add('expanded','mm',['coverage factor chosen as 2','no probability inferred'],e,[math.isclose(e['expanded_uncertainty'],.4)])
    return {'schema':'measurement.casebook/1','data_origin':'synthetic_only','result':'passed','cases':cases,'real_laboratory_reproduction':False}
if __name__=='__main__':print(json.dumps(run(),indent=2))
