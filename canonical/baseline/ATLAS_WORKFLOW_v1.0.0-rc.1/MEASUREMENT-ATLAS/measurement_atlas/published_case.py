"""Replay a publisher-documented calibration case; never a new laboratory claim."""
from __future__ import annotations
from importlib.resources import files
from pathlib import Path
from decimal import Decimal
import hashlib,json
from .calibration import fit_polynomial

PINS = {'NOTICE.md': '3a0d4cacca7bfd019d8163d76198db10f446c778dfcc5ca680f3b5e2e826cda1', 'capture.json': '1bbec97efb74bb24b331f8bdb11de61554d8cf570abc2ec18ac8267409c54298', 'certified_targets.json': 'c2cfd4cd6cb6a53cb429887ae3a739dca00ddc1a08da310da840a1e2fc831b7b', 'observations.json': '3d36e30f268705c686241d9332b8be0ba1deef2e0da7acafb33639bbf0d2ca0a', 'targets.json': '39709ec4b8f316af57228bdffb6a0e7ef6bc053bd6ab3ed58ce026eda005c161'}


def load_case(directory=None):
    raise RuntimeError('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')


def reproduce(directory: Path | None = None) -> dict:
    rows,meta,targets,certified = load_case(directory)
    x=[r['load'] for r in rows]; y=[r['deflection'] for r in rows]
    models = {};checks=[]
    for name,degree in [('linear',1),('quadratic',2)]:
        fit = fit_polynomial(x,y,degree=degree,x_unit=meta['columns']['load']['unit'],
                             y_unit=meta['columns']['deflection']['unit'])
        models[name]=fit
        pairs=[(f'beta_{i}',value,spec) for i,(value,spec) in enumerate(zip(fit.coefficients,targets[name]['coefficients']))]
        pairs += [('residual_sd',fit.residual_sd,targets[name]['residual_sd']),
                  ('lack_of_fit_F',fit.lack_of_fit_F,targets[name]['lack_of_fit_F'])]
        for field,actual,spec in pairs:
            delta=abs(actual-Decimal(str(spec['value'])))
            checks.append({'model':name,'quantity':field,'computed':str(actual),
                'published':spec['value'],'absolute_tolerance':spec['absolute_tolerance'],
                'absolute_error':str(delta),'passed':delta<=Decimal(str(spec['absolute_tolerance'])),
                'source_url':targets[name]['source_url']})
        checks.append({'model':name,'quantity':'residual_df','computed':fit.residual_df,
            'published':targets[name]['degrees_of_freedom'],
            'passed':fit.residual_df==targets[name]['degrees_of_freedom'],
            'source_url':targets[name]['source_url']})
    ex=targets['inverse_example']; inverse=models['quadratic'].invert(ex['deflection'])
    checks.append({'model':'quadratic','quantity':'illustrative_inverse_load','computed':str(inverse),
        'published':ex['published_load'],'absolute_tolerance':ex['absolute_tolerance'],
        'passed':abs(inverse-Decimal(ex['published_load']))<=Decimal(str(ex['absolute_tolerance'])),
        'source_url':ex['source_url']})
    q=models['quadratic']
    actual={**{f'beta_{i}':v for i,v in enumerate(q.coefficients)},
            **{f'coefficient_sd_{i}':q.covariance[i][i].sqrt() for i in range(3)},
            'residual_sd':q.residual_sd,'r_squared':q.r_squared,'sse':q.sse,
            'mse':q.sse/q.residual_df}
    certified_checks=[]
    for field,value in certified['targets'].items():
        target=Decimal(value)
        tolerance=Decimal(5).scaleb(target.as_tuple().exponent-1)
        delta=abs(actual[field]-target)
        certified_checks.append({'quantity':field,'computed':str(actual[field]),
            'certified':value,'absolute_tolerance':str(tolerance),
            'absolute_error':str(delta),'passed':delta<=tolerance})
    certified_checks.append({'quantity':'residual_df','computed':q.residual_df,
        'certified':certified['residual_df'],'passed':q.residual_df==certified['residual_df']})
    certified_ok=all(c['passed'] for c in certified_checks)
    disagreements=[c for c in checks if not c['passed']]
    return {'schema':'measurement.published-reproduction/1','dataset_id':meta['dataset_id'],
        'result':('passed_with_source_discrepancies' if disagreements else 'passed') if certified_ok else 'failed',
        'certified_reference_checks':certified_checks,'certified_reference_passed':certified_ok,
        'certified_reference_source':certified,'handbook_all_within_printed_rounding':not disagreements,
        'handbook_disagreements':disagreements,
        'capture':meta,'models':{name:m.as_dict() for name,m in models.items()},'checks':checks,
        'illustrative_inverse':{'deflection':ex['deflection'],'load':str(inverse),
                               'data_kind':ex['status']},
        'residuals':{'load':x,'linear':[str(r) for r in models['linear'].residuals],
                     'quadratic':[str(r) for r in models['quadratic'].residuals]},
        'interpretation':['Published straight-line fit has pronounced lack of fit under the case assumptions.',
          'The certified comparison and handbook display-rounding comparison are separate; some handbook values do not agree within printed rounding.',
          'Failing to reject lack of fit does not prove truth, absence of drift or universal validity.',
          'The inverse reading is the publisher hypothetical example, not a 41st measured reading.'],
        'independent_physical_replication':False,'independent_human_review':False,
        'published_interval_reproduced':False,'traceability_certification':False,
        'original_byte_capture':False,'implementation':'local_decimal_reanalysis_of_publisher_numbers'}


def main(argv=None):
    import argparse
    p=argparse.ArgumentParser(description=__doc__); p.parse_args(argv)
    try:
        r=reproduce();print(json.dumps(r,indent=2,ensure_ascii=False,allow_nan=False))
        return 0 if r['certified_reference_passed'] else 2
    except (ValueError,OSError,KeyError) as exc:
        print(json.dumps({'result':'failed','error':str(exc)}));return 2
