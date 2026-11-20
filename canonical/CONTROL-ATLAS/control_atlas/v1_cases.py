"""Control v1 authored numerical casebook and real-record-derived summary.

No real hardware operations. The Mendeley v2 raw dataset has NOT been fetched.
"""
import json,random
from importlib.resources import files
from .empirical import parse_openmct,validate_openmct_identification,COLUMNS
from .multivariable import two_by_two_observer_error_tube,two_sensor_consistency
from .methods import ControlInputError


def v1_casebook():
    cases=[]
    def add(name,result,passed,origin,limits):
        cases.append({'id':name,'result':result,'passed':bool(passed),'origin':origin,'limits':limits})
    D=files('control_atlas').joinpath('resources/derived_evidence/public_motor_rpm_summary.json')
    derived=json.loads(D.read_text('utf-8'))
    add('actual_public_motor_descriptive_summary',
        {'nominal_labels':[z['nominal_file_label'] for z in derived['series']],
         'rows':[z['n'] for z in derived['series']],
         'mean_rpm':[z['mean_rpm'] for z in derived['series']],
         'per_row_pwm_available':False,'raw_csv_archived':False},
        len(derived['series'])==3 and all(s['n']==49 for s in derived['series']),
        'third_party_derived_descriptive_stats_not_new_measurement',
        'Source Git blob identities and rights limits stored; do not fit plant gain from nominal filename labels')
    rng=random.Random(110113)
    x=0.;rows=[]
    for k in range(180):
        pwm=80 if k//9%2 else 220
        rows.append([0,x,20,500,510,pwm,0.5,k*.02,2,k//4]);x=.6*x+.35*pwm+3+rng.gauss(0,1)
    text='Mode, System Identification\nDate, 2026-10-12\n'+','.join(COLUMNS)+'\n'+'\n'.join(','.join(map(str,row)) for row in rows)
    parsed=parse_openmct(text);model=validate_openmct_identification(parsed)
    add('synthetic_openmct_parser_and_chronological_arx',
        {'rows':parsed['count'],'unique_DMM':parsed['dmm_unique_fresh'],
         'repeated_DMM_ids':parsed['dmm_duplicate_ids'],
         'fit':model['model'],'holdout_rmse':model['performance']},
        parsed['count']==180 and parsed['dmm_unique_fresh']==45 and abs(model['model']['a']-.6)<.03,
        'synthetic_author_generated_motor_data',
        'Model fitting of authored data not a replay of real OpenMCT logs')
    rows_const=[]
    for k,r in enumerate(rows):
        c=list(r);c[5]=100;rows_const.append(c)
    txt='Mode, System Identification\nDate, 2026-10-12\n'+','.join(COLUMNS)+'\n'+'\n'.join(','.join(map(str,row)) for row in rows_const)
    refused=False
    try:validate_openmct_identification(parse_openmct(txt))
    except ControlInputError:refused=True
    add('constant_input_rejected',{'refused':refused},refused,'synthetic_negative_test',
        'No fabricated excitation for unidentifiable b and intercept')
    A=[[.9,.05],[0,.8]];C=[[1,0],[0,1]];L=[[.45,0],[0,.4]]
    observer=two_by_two_observer_error_tube(A=A,C=C,L=L,initial_error_radii=[.4,.25],
      process_error_radii=[.03,.05],measurement_error_radii=[.1,.12],steps=25)
    add('bounded_mimo_observer',{'first':observer['error_radii'][0],
      'last':observer['error_radii'][-1],'sufficient_contraction':observer['sufficient_row_sum_contraction']},
      observer['sufficient_row_sum_contraction'],'authored_synthetic_model',
      'Hard noise and plant model bounds must be externally validated')
    contradiction=two_sensor_consistency(estimate=[1,2],estimated_error_radii=[.1,.1],C=C,
      sensor_values=[10,2],measurement_error_radii=[.1,.1])
    add('sensor_outlier_does_not_diagnose',contradiction,
       not contradiction['compatible'] and not contradiction['root_cause_identified'],
       'authored_synthetic_contradiction',
       'Contradiction does not isolate sensor, actuator, clock, process disturbance or model error')
    # A stable 2x2 rotation can fail a sufficient interval row-norm condition.
    fail=two_by_two_observer_error_tube(A=[[.3,.9],[-.9,.3]],C=C,L=[[0,0],[0,0]],
      initial_error_radii=[.1,.1],process_error_radii=[.001,.001],measurement_error_radii=[.01,.01],steps=8)
    add('sufficient_condition_false_negative',{'row_sum_gain':fail['row_sum_gain'],
       'stationary_bound':fail['conservative_stationary_infinity_norm_envelope']},
       not fail['sufficient_row_sum_contraction'] and fail['conservative_stationary_infinity_norm_envelope'] is None,
       'synthetic_bound_algorithm_counterexample',
       'No sufficient row-sum proof is not evidence that the exact stable dynamics are unstable')
    return {'schema':'atlas.control-v1-casebook/1','status':'passed' if all(q['passed'] for q in cases) else 'failed',
      'count':len(cases),'cases':cases,'new_hardware_experiments':0,
      'openmct_publisher_raw_data_analyzed':False,'safety_certified':False,'live_routing':False}
