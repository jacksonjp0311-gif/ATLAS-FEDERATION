"""Control Atlas: external OpenMCT motor-log validation without network actions.

Parses a user's locally acquired, publisher-versioned log. It DOES NOT infer
bounds, validate physical safety, or claim the public data was fetched here.
Run only on explicitly supplied files, never from knowledge records.
"""
from __future__ import annotations
import csv
from io import StringIO
from math import isfinite, sqrt, fsum
from statistics import median
from typing import Mapping
from .methods import ControlInputError

COLUMNS=("REF","MEAS","DT_ms","CURRENT_RAW","CURRENT_AVG","PWM",
         "DMM_CURRENT_A","DMM_TIME_s","DMM_AGE_ms","DMM_SAMPLE_ID")
MAX_SAMPLES=200000


def _finite(x, where):
    if isinstance(x,bool):raise ControlInputError(f'boolean forbidden at {where}')
    try:r=float(x)
    except (ValueError,TypeError):raise ControlInputError(f'non-numeric {where}') from None
    if not isfinite(r):raise ControlInputError(f'nonfinite {where}')
    return r


def parse_openmct(text: str, *, max_dmm_age_ms:float=1000)->dict:
    """Metadata rows 1..2, header row 3, CSV samples thereafter.

    Optional DMM data can be absent as blank or NaN, but not used to infer
    synchronous currents. DMM_SAMPLE_ID repeated values refer to the same
    asynchronous reading; do not treat them as independent replicates.
    """
    age_max=_finite(max_dmm_age_ms,'max_dmm_age_ms')
    if age_max<0:raise ControlInputError('nonnegative max DMM age required')
    if not isinstance(text,str) or len(text)>60_000_000:raise ControlInputError('text missing or too large')
    lines=text.lstrip('\ufeff').splitlines()
    if len(lines)<5:raise ControlInputError('need two metadata lines, exact header, and at least two samples')
    metadata=lines[:2]
    if not all(s.strip() and len(s)<4096 for s in metadata):raise ControlInputError('missing/invalid acquisition metadata')
    reader=csv.reader(StringIO('\n'.join(lines[2:])),strict=True)
    try:header=next(reader)
    except (StopIteration,csv.Error):raise ControlInputError('header missing') from None
    header=[x.strip() for x in header]
    if tuple(header)!=COLUMNS:raise ControlInputError(f'OpenMCT expected ten ordered fields; got {header}')
    if not (2 <= len(lines)-3 <= MAX_SAMPLES):raise ControlInputError('sample count outside 2..200000')
    out=[];unique_dmm=set();accepted_dmm=0;stale_dmm=0;repeat_dmm=0;non_dmm=0
    for i,row in enumerate(reader):
        if len(row)!=len(COLUMNS):raise ControlInputError(f'row {i}: width mismatch')
        obj={k:v.strip() for k,v in zip(COLUMNS,row)}
        for k in ('REF','MEAS','DT_ms','CURRENT_RAW','CURRENT_AVG','PWM'):
            obj[k]=_finite(obj[k],f'row {i} field {k}')
        if not 0<obj['DT_ms']<=2000:raise ControlInputError(f'row {i}: nonpositive/unsupported loop interval')
        if not 0<=obj['PWM']<=255:raise ControlInputError(f'row {i}: PWM outside reported 8-bit actuator levels')
        # Empty/NaN DMM are missing data; do not convert to zero, and do not
        # interpolate asynchronous external-meter samples.
        extra=('DMM_CURRENT_A','DMM_TIME_s','DMM_AGE_ms','DMM_SAMPLE_ID')
        vals=[obj[k] for k in extra]
        missing=[not v or v.lower() in ('nan','na','null') for v in vals]
        if any(missing):
            if not all(missing):raise ControlInputError(f'row {i}: partial async meter record')
            for k in extra:obj[k]=None
            non_dmm+=1
        else:
            for k in extra:obj[k]=_finite(obj[k],f'row {i} {k}')
            if obj['DMM_AGE_ms']<0:raise ControlInputError(f'row {i}: negative meter sample age')
            sid=obj['DMM_SAMPLE_ID']
            if sid in unique_dmm:repeat_dmm+=1
            elif obj['DMM_AGE_ms']>age_max:stale_dmm+=1;unique_dmm.add(sid)
            else:accepted_dmm+=1;unique_dmm.add(sid)
        out.append(obj)
    if len(out)<2:raise ControlInputError('insufficient recorded samples')
    # The documentation constructs t[k] from preceding row DT_ms, not from
    # a nominal loop period. No inference about a hardware/GUI clock follows.
    t=[0.0];
    for r in out[:-1]:t.append(t[-1]+r['DT_ms']/1000)
    dts=[r['DT_ms'] for r in out[:-1]]
    med=median(dts);jit=max(abs(x-med) for x in dts)/med
    return {'schema':'atlas.control-openmct-parse/1','dataset':'external_supplied_openmct_v2_log',
        'samples':out,'times_s':t,'count':len(out),'median_dt_ms':med,
        'max_fractional_dt_deviation':jit,
        'dmm_unique_fresh':accepted_dmm,'dmm_duplicate_ids':repeat_dmm,
        'dmm_unique_stale':stale_dmm,'dmm_rows_absent':non_dmm,
        'metadata_lines':metadata,
        'limits':['Parsed external data is not independently authenticated by this function',
            'Reference REF is not applied PWM; dynamic identification uses PWM',
            'DMM data may be asynchronous and repeated IDs are not replicates',
            'Reconstruction timestamps are estimates from acquisition DT_ms, not verified clock sync']}


def _fit_regression(train):
    """Fit y[k+1]=a*y[k]+b*u[k]+c with centered 2x2 normal equations.

    Rank-deficient or weakly excited inputs are refused rather than assigning
    an arbitrary gain. No residual stochastic independence assumption is made.
    """
    if len(train)<20:raise ControlInputError('minimum 20 training transitions')
    xs=[row['MEAS'] for row in train]; us=[row['PWM'] for row in train]
    ys=[row['_next_y'] for row in train]
    N=len(train);mx=fsum(xs)/N;mu=fsum(us)/N;my=fsum(ys)/N
    x=[a-mx for a in xs];u=[a-mu for a in us];y=[a-my for a in ys]
    sxx=fsum(v*v for v in x);suu=fsum(v*v for v in u)
    sxu=fsum(a*b for a,b in zip(x,u));sxy=fsum(a*b for a,b in zip(x,y));suy=fsum(a*b for a,b in zip(u,y))
    if not sxx>1e-8 or not suu>1e-8:raise ControlInputError('unexcited or constant motor speed/PWM; gain not identified')
    det=sxx*suu-sxu*sxu
    if det<=1e-8*sxx*suu:raise ControlInputError('collinear speed and PWM; plant cannot be uniquely identified')
    a=(sxy*suu-suy*sxu)/det;b=(suy*sxx-sxy*sxu)/det;c=my-a*mx-b*mu
    if not all(isfinite(v) for v in (a,b,c)):raise ControlInputError('nonfinite fitted model')
    return {'a':a,'b':b,'c':c, 'model':'one_step_discrete_arx_speed_and_applied_pwm_with_intercept'}


def validate_openmct_identification(parsed: Mapping, *, train_fraction:float=.7,
                                      max_fractional_jitter:float=.2, min_pwm_span:float=15)->dict:
    """Chronological one-step and free-run held-out model check, for ONE log.

    Identified model is merely a descriptive predictor of input/output data.
    Closed-loop correlation, unknown deadbands, dt jitter and initialization
    can bias the regression; no physical bounds or stable controller certified.
    """
    frac=_finite(train_fraction,'train_fraction');jit=_finite(max_fractional_jitter,'jitter');span=_finite(min_pwm_span,'min_pwm_span')
    if not .5<=frac<=.85 or jit<0 or span<0:raise ControlInputError('invalid validation configuration')
    if not isinstance(parsed,dict) or parsed.get('schema')!='atlas.control-openmct-parse/1':raise ControlInputError('parsed supplied OpenMCT record required')
    samples=parsed['samples'];N=len(samples)
    if N<50:raise ControlInputError('at least 50 samples needed for this train/held-out design')
    if parsed['max_fractional_dt_deviation']>jit:raise ControlInputError('sample period varies too much for constant-coefficient sample model')
    # transitions k from x_k,u_k to x_{k+1}. Split by CLOCK ORDER.
    total=N-1;trainN=int(total*frac)
    train=[]
    for i in range(trainN):
        item=dict(samples[i]);item['_next_y']=samples[i+1]['MEAS'];train.append(item)
    pwms=[r['PWM'] for r in train]
    if max(pwms)-min(pwms)<span:raise ControlInputError('training lacks sufficient applied PWM excitation')
    model=_fit_regression(train)
    observed=[];pred_one=[];pred_free=[];free=float(samples[trainN]['MEAS'])
    for i in range(trainN,total):
        actual=samples[i+1]['MEAS'];u=samples[i]['PWM']
        one=model['a']*samples[i]['MEAS']+model['b']*u+model['c']
        free=model['a']*free+model['b']*u+model['c']
        if not (isfinite(one) and isfinite(free)):raise ControlInputError('validation model diverged numerically')
        observed.append(actual);pred_one.append(one);pred_free.append(free)
    def rmse(pred):return sqrt(fsum((o-p)**2 for o,p in zip(observed,pred))/len(observed))
    # persistence y[k+1]=y[k] is a meaningful zero-input learned baseline.
    persisted=[samples[i]['MEAS'] for i in range(trainN,total)]
    performance={'heldout_one_step_rmse_rpm':rmse(pred_one),
                 'heldout_free_run_rmse_rpm':rmse(pred_free),
                 'heldout_persistence_rmse_rpm':rmse(persisted)}
    return {'schema':'atlas.control-openmct-chronological-holdout/1',
       'status':'descriptive_prediction_evaluated_not_causal_or_safety_identification',
       'training_transitions':trainN,'validation_transitions':len(observed),
       'model':model,'performance':performance,'median_dt_ms':parsed['median_dt_ms'],
       'dmm_replicates_not_double_counted':True,
       'limitations':['Same-run train/test can overstate transferability across motors, datasets and controller regimes',
          'If data are closed-loop, input correlates with noise; naive OLS may be biased',
          'No prediction interval, formal confidence bounds, or sensor calibration is established',
          'No controller is designed or run, no actual robust-stability/safety certification',
          'One-step uses measured previous speed, free-run uses only held-out starting speed',
          'Natural periodic sampling from DT_ms is approximate; high jitter forces refusal',
          'Publisher data are not bundled or authenticated; user supplies actual raw file separately']}
