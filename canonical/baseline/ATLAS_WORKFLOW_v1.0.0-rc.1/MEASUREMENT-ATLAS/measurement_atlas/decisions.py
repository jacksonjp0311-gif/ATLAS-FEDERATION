"""Conditional normal conformance probabilities and explicit guard-band rules.

Implements scalar mathematical models, not regulatory or calibration certification.
JCGM 106:2012, sections 7.1-7.4 and 8.1-8.3. Does not calculate global risks.
"""
from __future__ import annotations
import math
from .units import number, parse_unit, validate_kind


def _limits(lower, upper):
    lo=None if lower is None else number(lower,'lower')
    hi=None if upper is None else number(upper,'upper')
    if lo is None and hi is None:raise ValueError('at least one finite specification limit required')
    if lo is not None and hi is not None and lo>=hi:raise ValueError('lower must be strictly less than upper')
    return lo,hi


def _tail(z):return 0.5*math.erfc(z/math.sqrt(2.0))


def _normal_mass(lo,hi):
    # Stable subtraction in same-side tails; no 1 - Phi(z) cancellation.
    if lo>=0:return max(0.0,_tail(lo)-_tail(hi))
    if hi<=0:return max(0.0,_tail(-hi)-_tail(-lo))
    return max(0.0,min(1.0,1.0-_tail(hi)-_tail(-lo)))


def normal_conformance(value: float, standard_uncertainty: float, *,
                       lower: float | None=None, upper: float | None=None,
                       unit: str, quantity_kind: str, model_basis: str) -> dict:
    """Probability within supplied limits under an explicitly declared knowledge PDF."""
    x=number(value,'value');u=number(standard_uncertainty,'standard_uncertainty')
    if u<=0:raise ValueError('positive standard uncertainty required for continuous normal model')
    if not isinstance(model_basis,str) or not model_basis.strip():raise ValueError('explicit normal state-of-knowledge model_basis required')
    validate_kind(parse_unit(unit),quantity_kind);lo,hi=_limits(lower,upper)
    zl=-math.inf if lo is None else (lo-x)/u
    zh=math.inf if hi is None else (hi-x)/u
    p=_normal_mass(zl,zh)
    return {'schema':'measurement.normal-conformance/1','conditional_probability':p,
            'conditional_nonconformance_probability':1.0-p,'value':x,'standard_uncertainty':u,
            'lower':lo,'upper':hi,'unit':unit,'quantity_kind':quantity_kind,
            'model':'caller_declared_normal_state_of_knowledge','model_basis':model_basis,
            'decision':None,'global_consumer_risk':None,'global_producer_risk':None,
            'limitations':['A standard uncertainty alone does not establish a normal posterior or state-of-knowledge distribution.',
                          'This is not the frequentist probability that a fixed parameter falls in a realized confidence interval.',
                          'No acceptance rule, prior, process distribution or regulatory requirement is inferred.',
                          'Binary floating point may underflow extremely small tail probabilities.']}


def guard_band_decision(value: float, *, lower: float | None=None,
                        upper: float | None=None, guard_width: float,
                        rule_id: str, unit: str, quantity_kind: str) -> dict:
    """Apply a caller-selected nonnegative inward guard band, with inclusive endpoints."""
    x=number(value,'value');w=number(guard_width,'guard_width')
    if w<0:raise ValueError('guard_width must be nonnegative')
    if not isinstance(rule_id,str) or not rule_id.strip():raise ValueError('explicit rule_id required')
    validate_kind(parse_unit(unit),quantity_kind);lo,hi=_limits(lower,upper)
    al=None if lo is None else lo+w;au=None if hi is None else hi-w
    if (al is not None and not math.isfinite(al)) or (au is not None and not math.isfinite(au)):
        raise ValueError('acceptance limit overflow')
    if al is not None and au is not None and al>=au:
        raise ValueError('guard band leaves no positive-width acceptance interval')
    inside=(al is None or x>=al) and (au is None or x<=au)
    return {'schema':'measurement.guard-band-decision/1','rule_id':rule_id,
            'decision':'accepted_under_declared_rule' if inside else 'not_accepted_under_declared_rule',
            'acceptance_lower':al,'acceptance_upper':au,'inclusive_endpoints':True,
            'specification_lower':lo,'specification_upper':hi,'guard_width':w,
            'value':x,'unit':unit,'quantity_kind':quantity_kind,'conformity_certified':False,
            'risk_bound_established':False,
            'limitations':['Not accepted under a rule does not prove that the underlying item is nonconforming.',
                           'The guard width and its risk justification must be supplied externally.',
                           'A decision rule is not a probability distribution or an accreditation finding.']}
