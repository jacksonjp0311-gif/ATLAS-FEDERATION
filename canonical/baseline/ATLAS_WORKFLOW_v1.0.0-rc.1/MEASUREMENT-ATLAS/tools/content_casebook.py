#!/usr/bin/env python3
"""Original synthetic teaching calculations. No instrument data or AI evaluation.

Uses the retained numerical library, with independent closed-form arithmetic or
finite enumeration as expected outcomes. This is not a new navigation feature.
"""
from pathlib import Path
import json,sys,math
from fractions import Fraction
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from measurement_atlas.uncertainty import combine_linear,compare_difference,expanded_uncertainty
from measurement_atlas.budget import type_b

def run():
    cases=[]
    def add(cid,title,refs,inputs,actual,expected,units,assumptions,limits):
        if set(actual)!=set(expected):raise AssertionError(cid+': mismatched result fields')
        for key,value in actual.items():
            if not math.isfinite(value) or not math.isclose(value,expected[key],rel_tol=1e-11,abs_tol=1e-12):
                raise AssertionError(f'{cid}: {key}: {value} != {expected[key]}')
        cases.append({'id':cid,'title':title,'data_origin':'synthetic_teaching_example',
                      'reference_ids':refs,'inputs':inputs,'results':actual,'expected':expected,
                      'result_units':units,'assumptions':assumptions,'limitations':limits,'passed':True})
    add('unit-scale','Convert a length and its absolute uncertainty',['quantity-value-unit'],
        {'value_mm':25,'u_mm':.2,'m_per_mm':.001},
        {'value_m':25*.001,'u_m':.2*.001},{'value_m':.025,'u_m':.0002},
        {'value_m':'m','u_m':'m'},['Exact declared scale conversion.'],['Not a general unit parser.'])
    add('temperature-offset','Convert a Celsius value but not an interval offset',['celsius-temperature-interval'],
        {'value_degC':20,'u_degC':.3,'interval_degC':5},
        {'value_K':20+273.15,'u_K':.3,'interval_K':5},{'value_K':293.15,'u_K':.3,'interval_K':5},
        {'value_K':'K','u_K':'K','interval_K':'K'},['Scale offset is exact in the stated relationship.'],['No instrument calibration uncertainty is invented.'])
    quant=type_b(.02/2,'uniform')['standard_uncertainty']
    add('rounding','A specified uniform rounding model',['quantization-assumption','resolution-meaning'],
        {'step_mm':.02}, {'u_mm':quant},{'u_mm':.005773502691896258},{'u_mm':'mm'},
        ['Rounding to nearest step; justified uniform residual.'],['Truncation and other noise need their own model.'])
    common=combine_linear([.25]*4,[[.04+(.01 if i==j else 0) for j in range(4)] for i in range(4)])
    add('shared-offset','Common offset survives averaging',['correlated-mean','shared-offset-average'],
        {'n':4,'u_common_mm':.2,'sigma_independent_mm':.1},
        {'variance_mm2':common['variance'],'u_mm':common['combined_standard_uncertainty']},
        {'variance_mm2':.0425,'u_mm':.20615528128088306},{'variance_mm2':'mm^2','u_mm':'mm'},
        ['Independent common offset and independent reading noise.'],['A mathematical covariance model, not measured sensor behavior.'])
    difference=compare_difference(12.3,12.2,.04,.09,.03)
    add('difference-covariance','Compare correlated estimates',['measurement-difference','compatibility-rule'],
        {'a_mm':12.3,'b_mm':12.2,'var_a_mm2':.04,'var_b_mm2':.09,'cov_mm2':.03},
        {'difference_mm':difference['difference'],'u_mm':difference['standard_uncertainty_difference']},
        {'difference_mm':.1,'u_mm':.2645751311064591},{'difference_mm':'mm','u_mm':'mm'},
        ['Same specified measurand; covariance is supplied.'],['No acceptance rule or probability is inferred.'])
    inv=combine_linear([.25,-.25,-.5],[[.04,0,0],[0,.01,-.002],[0,-.002,.0025]])
    add('inverse-calibration','Inverse calibration with coefficient covariance',['inverse-linear-calibration','inverse-calibration-sensitivities'],
        {'indication':10,'intercept':2,'slope':4,'input_order':['indication','intercept','slope'],'covariance':[[.04,0,0],[0,.01,-.002],[0,-.002,.0025]]},
        {'estimate':(10-2)/4,'variance':inv['variance'],'u':inv['combined_standard_uncertainty']},
        {'estimate':2,'variance':.00325,'u':.0570087712549569},
        {'estimate':'input-unit','variance':'input-unit^2','u':'input-unit'},
        ['Coefficient units match a declared response/input convention; linearization is adequate.'],['No evidence of linearity or applicable range is supplied by this arithmetic.'])
    area=combine_linear([50,100],[[.04,0],[0,.01]])
    add('area-budget','First-order rectangular area budget',['linear-propagation'],
        {'L_mm':100,'W_mm':50,'uL_mm':.2,'uW_mm':.1,'cov_mm2':0},
        {'area_mm2':100*50,'u_mm2':area['combined_standard_uncertainty']},
        {'area_mm2':5000,'u_mm2':14.142135623730951},{'area_mm2':'mm^2','u_mm2':'mm^2'},
        ['Declared independent inputs; first-order approximation.'],['Not the exact product distribution.'])
    ratio=combine_linear([.5,-2.5],[[.01,0],[0,.0004]])
    add('ratio-budget','First-order ratio budget',['linear-propagation'],
        {'x':10,'y':2,'ux':.1,'uy':.02,'cov':0},
        {'ratio':10/2,'u_ratio':ratio['combined_standard_uncertainty']},{'ratio':5,'u_ratio':.07071067811865475},
        {'ratio':'1','u_ratio':'1'},['Same input quantity kind; denominator bounded away from zero; local linearization adequate.'],['Not safe to generalize to near-zero denominators.'])
    vals=[Fraction(-1),Fraction(0),Fraction(1)];out=[v*v for v in vals]
    mu=sum(out)/3;variance=sum((v-mu)**2 for v in out)/3
    first=combine_linear([0],[[float(sum(v*v for v in vals)/3)]])
    add('nonlinear-counterexample','Finite enumeration exposes first-order failure',['linearization-counterexample'],
        {'X_values':[-1,0,1],'probabilities':['1/3','1/3','1/3'],'model':'Y=X^2'},
        {'exact_mean':float(mu),'exact_variance':float(variance),'first_order_variance':first['variance']},
        {'exact_mean':2/3,'exact_variance':2/9,'first_order_variance':0},
        {'exact_mean':'1','exact_variance':'1','first_order_variance':'1'},
        ['Equiprobable invented values; exact rational enumeration.'],['A counterexample to universal linearization, not a claim about every nonlinear problem.'])
    nu=float((Fraction(1)+Fraction(1))**2/(Fraction(1,10)+Fraction(1,10)))
    add('effective-dof','Conventional effective-degree arithmetic',['effective-degrees-of-freedom'],
        {'variance_contributions':[1,1],'degrees_of_freedom':[10,10]},
        {'nu_eff':nu},{'nu_eff':20},{'nu_eff':'1'},
        ['Independent components and conventional approximation conditions.'],['No t quantile or coverage probability has been calculated.'])
    add('frequency-conversion','Cyclic to angular frequency',['angular-frequency-unit'],
        {'frequency_Hz':10},{'angular_rate':2*math.pi*10},{'angular_rate':62.83185307179586},
        {'angular_rate':'rad/s'},['A defined periodic cycle.'],['Does not infer frequency from an experimental signal.'])
    u=expanded_uncertainty(.224,2)
    add('report-with-k','Report the chosen factor without inventing probability',['expanded-uncertainty','uncertainty-reporting'],
        {'standard_uncertainty_mm':.224,'chosen_k':2},{'expanded_mm':u['expanded_uncertainty']},{'expanded_mm':.448},{'expanded_mm':'mm'},
        ['k=2 is explicitly supplied.'],['No probability claim is assigned solely from k.'])
    return {'schema':'measurement.content-casebook/1','edition':'0.5.0','result':'passed','case_count':len(cases),'cases':cases,
            'actual_measurements':False,'independent_scientific_review':False,'actual_ai_evaluation':False}

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path);a=p.parse_args()
    r=run();text=json.dumps(r,indent=2,ensure_ascii=False)+'\n'
    if a.out:
        if a.out.exists():raise SystemExit('Refusing to overwrite a casebook receipt; use a fresh path.')
        a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(text,encoding='utf-8')
    print(text)
