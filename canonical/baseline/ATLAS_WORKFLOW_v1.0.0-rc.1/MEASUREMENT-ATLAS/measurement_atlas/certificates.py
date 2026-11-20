"""Structured, operator-entered calibration information. Not a certificate verifier.

No PDF/OCR parsing, accreditation inference, implicit expiry, or automatic
conversion of a confidence level into a coverage factor is performed.
"""
from __future__ import annotations
from datetime import date
from .units import number, parse_unit, validate_kind
import math

FIELDS = {'certificate_id','source_locator','instrument_id','calibration_date',
          'quantity_kind','unit','value','uncertainty_kind','uncertainty',
          'coverage_factor','coverage_probability','conditions','traceability_references',
          'correction','valid_range','operator_due_date','data_origin'}
REQUIRED_TEXT = ('certificate_id','source_locator','instrument_id','calibration_date',
                 'quantity_kind','unit','uncertainty_kind','data_origin')


def reported_standard_uncertainty(uncertainty: float, kind: str,
                                  coverage_factor: float | None = None) -> dict:
    u=number(uncertainty,'uncertainty')
    if u<0:raise ValueError('uncertainty must be nonnegative')
    if kind=='standard':
        if coverage_factor is not None:raise ValueError('standard uncertainty must not supply an expanded coverage factor')
        standard=u;k=None
    elif kind=='expanded':
        if coverage_factor is None:raise ValueError('expanded uncertainty needs its stated coverage factor; do not infer from 95 percent')
        k=number(coverage_factor,'coverage_factor')
        if k<=0:raise ValueError('coverage_factor must be positive')
        standard=u/k
    else:raise ValueError('uncertainty_kind must be standard or expanded')
    if not math.isfinite(standard):raise ValueError('standard uncertainty outside finite range')
    return {'standard_uncertainty':standard,'reported_uncertainty':u,'reported_kind':kind,
            'coverage_factor':k,'coverage_probability_inferred':False,
            'interpretation':'Arithmetic interpretation of supplied terms, not validation of the certificate.'}


def review_certificate(record: dict, *, as_of: str) -> dict:
    """Check completeness and numerical meaning of manually entered certificate fields."""
    if not isinstance(record,dict):raise ValueError('certificate input must be an object')
    unknown=set(record)-FIELDS
    if unknown:raise ValueError('unknown certificate fields: '+', '.join(sorted(unknown)))
    try:reference_date=date.fromisoformat(as_of)
    except (ValueError,TypeError) as exc:raise ValueError('as_of must be an explicit ISO date') from exc
    issues=[]
    for key in REQUIRED_TEXT:
        if not isinstance(record.get(key),str) or not record[key].strip():issues.append('missing_or_invalid:'+key)
    for key in ('conditions','traceability_references'):
        v=record.get(key)
        if not isinstance(v,list) or not v or any(not isinstance(x,str) or not x.strip() for x in v):
            issues.append('missing_or_invalid:'+key)
    if isinstance(record.get('calibration_date'),str):
        try:
            d=date.fromisoformat(record['calibration_date'])
            if d>reference_date:issues.append('calibration_date_is_after_as_of')
        except ValueError:issues.append('invalid:calibration_date')
    if record.get('operator_due_date') is not None:
        try:
            due=date.fromisoformat(record['operator_due_date'])
            if due<reference_date:issues.append('operator_due_date_exceeded_not_a_universal_expiry_rule')
        except (ValueError,TypeError):issues.append('invalid:operator_due_date')
    try:
        unit=parse_unit(record.get('unit'));validate_kind(unit,record.get('quantity_kind'))
        value=number(record.get('value'),'value')
        if record['quantity_kind']=='temperature' and value*unit.scale+unit.offset<0:
            raise ValueError('negative absolute temperature outside model')
        component=reported_standard_uncertainty(record.get('uncertainty'),record.get('uncertainty_kind'),record.get('coverage_factor'))
        component.update({'unit':unit.symbol,'quantity_kind':record['quantity_kind']})
        if record.get('coverage_probability') is not None:
            probability=number(record['coverage_probability'],'coverage_probability')
            if not 0<probability<1:raise ValueError('coverage_probability must be between zero and one')
            component['reported_coverage_probability']=probability
            component['probability_basis_checked']=False
        if record.get('correction') is not None:number(record['correction'],'correction')
        if record.get('valid_range') is not None:
            v=record['valid_range']
            if not isinstance(v,list) or len(v)!=2:raise ValueError('valid_range must have two limits')
            lo,hi=number(v[0],'range lower'),number(v[1],'range upper')
            if not lo<hi:raise ValueError('valid_range must be increasing')
            if not lo<=value<=hi:issues.append('reported_value_outside_declared_range')
    except (ValueError,TypeError) as exc:
        issues.append('numerical_or_unit_issue:'+str(exc));component=None
    return {'schema':'measurement.certificate-review/1',
            'status':'incomplete' if issues else 'structured_for_review',
            'as_of':as_of,'certificate_id':record.get('certificate_id'),'issues':issues,
            'component':component if not issues else None,
            'input':record,'authenticity_verified':False,'traceability_established':False,
            'fit_for_intended_use':None,'additional_use_uncertainty_assessed':False,
            'limits':['No signatory, accreditation, instrument identity or document authenticity is verified.',
                      'A reported calibration uncertainty need not include transport, drift or subsequent use.',
                      'Source terms and a competent review are required before use in a real budget.']}


def specification_component(reading: float, *, unit: str, quantity_kind: str,
                            percent_reading: float=0.0, percent_range: float=0.0,
                            full_scale: float | None=None, counts: int=0,
                            resolution: float=0.0, distribution: str,
                            interpretation_basis: str) -> dict:
    """Explicit additive-bound model; caller must justify that these terms really add."""
    x=number(reading,'reading');u=parse_unit(unit);validate_kind(u,quantity_kind)
    if u.offset:raise ValueError('affine temperature reading needs an explicit manufacturer model; unsupported here')
    if not isinstance(interpretation_basis,str) or not interpretation_basis.strip():raise ValueError('interpretation_basis required')
    if isinstance(counts,bool) or not isinstance(counts,int) or counts<0:raise ValueError('counts must be a nonnegative integer')
    pr=number(percent_reading,'percent_reading');pf=number(percent_range,'percent_range');r=number(resolution,'resolution')
    if min(pr,pf,r)<0:raise ValueError('bound contributions must be nonnegative')
    fs=0.0 if full_scale is None else number(full_scale,'full_scale')
    if fs<0 or (pf>0 and fs<=0):raise ValueError('positive full_scale required for a percent_range term')
    if counts and r<=0:raise ValueError('positive resolution required with counts')
    if distribution not in ('uniform','triangular'):raise ValueError('explicit uniform or triangular assumption required')
    bound=abs(x)*pr/100+fs*pf/100+counts*r
    if not math.isfinite(bound):raise ValueError('bound overflow')
    std=bound/math.sqrt(3 if distribution=='uniform' else 6)
    return {'schema':'measurement.specification-component/1','half_width':bound,
            'standard_uncertainty':std,'unit':unit,'quantity_kind':quantity_kind,
            'distribution_assumption':distribution,'interpretation_basis':interpretation_basis,
            'combination_model':'sum_of_nonnegative_additive_limits',
            'complete_measurement_uncertainty':False,
            'limitations':['Terms and distribution are caller-justified assumptions, not inferred from a manufacturer document.',
                           'Do not independently count overlapping specifications or assume this exhausts a measurement budget.']}
