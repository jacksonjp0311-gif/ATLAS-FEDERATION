#!/usr/bin/env python3
"""Replay publisher illustrations and explicitly synthetic practical examples."""
from pathlib import Path
import hashlib,json,math,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from measurement_atlas.decisions import normal_conformance,guard_band_decision
from measurement_atlas.certificates import review_certificate,specification_component
from measurement_atlas.units import convert_quantity

def run():
    p=ROOT/'evaluations/practical_targets.json';targets=json.loads(p.read_text());expected=(p.with_suffix('.sha256')).read_text().split()[0]
    if hashlib.sha256(p.read_bytes()).hexdigest()!=expected:raise ValueError('target integrity mismatch')
    rows=[]
    for c in targets['cases']:
        args={k:v for k,v in c.items() if k not in ('id','source','target_probability','absolute_tolerance')}
        actual=normal_conformance(**args,model_basis='Publisher illustrative normal knowledge distribution; not a new measurement')['conditional_probability']
        error=abs(actual-c['target_probability'])
        rows.append({'id':c['id'],'source':c['source'],'actual':actual,'display_target':c['target_probability'],
                     'absolute_error':error,'absolute_tolerance':c['absolute_tolerance'],'passed':error<=c['absolute_tolerance']})
    c=targets['uncertainty_reporting']
    standard=convert_quantity(c['standard_uncertainty_mg'],'mg','g',quantity_kind='mass')['value']
    actual=c['coverage_factor']*standard
    rows.append({'id':'nist-reporting-illustration','actual_expanded_g':actual,
        'display_target_g':c['displayed_expanded_uncertainty_g'],'absolute_tolerance_g':c['absolute_tolerance_g'],
        'passed':abs(actual-c['displayed_expanded_uncertainty_g'])<=c['absolute_tolerance_g']})
    cert=json.loads((ROOT/'examples/synthetic_certificate.json').read_text())
    valid=review_certificate(**cert);missing=review_certificate(**json.loads((ROOT/'examples/missing_factor_certificate.json').read_text()))
    rows.append({'id':'synthetic-complete-certificate','passed':valid['status']=='structured_for_review' and not valid['authenticity_verified']})
    rows.append({'id':'synthetic-missing-factor','passed':missing['status']=='incomplete' and missing['component'] is None})
    bound=specification_component(5,unit='V',quantity_kind='voltage',percent_reading=0.1,counts=2,resolution=0.001,distribution='uniform',interpretation_basis='Synthetic additive 0.1 percent reading plus two counts')
    rows.append({'id':'synthetic-specification','actual':bound,'passed':abs(bound['half_width']-.007)<1e-15})
    decision=guard_band_decision(.95,lower=0,upper=1,guard_width=.1,rule_id='synthetic-rule-1',unit='mm',quantity_kind='length')
    rows.append({'id':'synthetic-guard-band','actual':decision,'passed':decision['decision']=='not_accepted_under_declared_rule' and not decision['conformity_certified']})
    return {'schema':'measurement.practical-casebook/1','result':'passed' if all(r['passed'] for r in rows) else 'failed',
       'cases':rows,'case_count':len(rows),'target_sha256':expected,
       'data_origin':'publisher_illustrations_and_synthetic_examples','new_measured_observations':0,
       'independent_human_review':False,'heldout_evaluation':False,'calibration_certification':False}
if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,allow_nan=False));sys.exit(0 if result['result']=='passed' else 2)
