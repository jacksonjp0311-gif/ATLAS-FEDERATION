"""Conditional coverage calculations, not calibration or confidence certification.

Numerical scope: 1 <= finite degrees of freedom <= 10000 and central coverage
0.5 <= p <= 0.9999. Infinite df is an explicit normal assumption. The beta
continued fraction follows DLMF 8.17(v); Student-t tails follow by integrating
its density. No third-party runtime dependency or automatic normality test.
"""
from __future__ import annotations
from decimal import Decimal, localcontext
import math
from statistics import NormalDist
from typing import Iterable


def _finite(value: object, name: str) -> float:
    if isinstance(value, bool):
        raise ValueError(name + ' cannot be a boolean')
    try:
        result = float(value)
    except (ValueError, TypeError, OverflowError) as exc:
        raise ValueError(name + ' must be finite numeric data') from exc
    if not math.isfinite(result):
        raise ValueError(name + ' must be finite')
    return result


def _df(value: object) -> float:
    if isinstance(value, bool):
        raise ValueError('degrees of freedom cannot be a boolean')
    try:
        result = float(value)
    except (ValueError, TypeError, OverflowError) as exc:
        raise ValueError('invalid degrees of freedom') from exc
    if not (1 <= result <= 10000 or result == math.inf):
        raise ValueError('finite df must be between 1 and 10000, or explicitly infinity')
    return result


def _beta_fraction(a: float, b: float, x: float) -> float:
    # Modified Lentz evaluation of the alternating incomplete-beta fraction.
    tiny, eps = 1e-300, 3e-14
    den = 1.0 - (a+b)*x/(a+1)
    if abs(den) < tiny: den = tiny
    inv, top = 1.0/den, 1.0
    result = inv
    for m in range(1, 20001):
        even = m*(b-m)*x/((a+2*m-1)*(a+2*m))
        odd = -(a+m)*(a+b+m)*x/((a+2*m)*(a+2*m+1))
        for coefficient in (even, odd):
            den = 1 + coefficient*inv
            top = 1 + coefficient/top
            if abs(den) < tiny: den = math.copysign(tiny, den)
            if abs(top) < tiny: top = math.copysign(tiny, top)
            inv = 1.0/den
            delta = inv*top
            result *= delta
        if abs(delta-1.0) < eps:
            return result
    raise ValueError('Incomplete beta fraction failed to converge')


def _beta_regularized(x: float, a: float, b: float) -> float:
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    weight = math.exp(math.lgamma(a+b)-math.lgamma(a)-math.lgamma(b)
                      + a*math.log(x)+b*math.log1p(-x))
    if x < (a+1)/(a+b+2):
        result = weight*_beta_fraction(a,b,x)/a
    else:
        result = 1-weight*_beta_fraction(b,a,1-x)/b
    if not -1e-12 <= result <= 1+1e-12:
        raise ValueError('Incomplete beta result outside probability range')
    return min(1.0,max(0.0,result))


def student_t_survival(t: object, df: object) -> float:
    """P(T>t); finite t and declared numeric range, not a data-driven guarantee."""
    x, nu = _finite(t,'t'), _df(df)
    if nu == math.inf:
        return 0.5*math.erfc(x/math.sqrt(2))
    if x == 0: return 0.5
    # x*x may overflow to infinity, giving the correct limiting tail.
    ratio = nu/(nu+x*x)
    tail = 0.5*_beta_regularized(ratio,nu/2,0.5)
    return tail if x>0 else 1-tail


def coverage_factor(probability: object, df: object) -> float:
    """Central two-sided Student-t factor. 'inf' requires a normal-limit choice."""
    p,nu = _finite(probability,'central probability'),_df(df)
    if not 0.5 <= p <= 0.9999:
        raise ValueError('central probability must be between 0.5 and 0.9999')
    if nu == math.inf: return NormalDist().inv_cdf((1+p)/2)
    tail=(1-p)/2
    lo,hi=0.0,1.0
    while student_t_survival(hi,nu)>tail:
        hi*=2
        if hi>1e8: raise ValueError('Student-t quantile not bracketed')
    for _ in range(100):
        mid=(lo+hi)/2
        if student_t_survival(mid,nu)>tail:lo=mid
        else:hi=mid
        if hi-lo<=2e-13*max(1.0,mid):return (lo+hi)/2
    raise ValueError('Student-t quantile failed to converge')


def effective_df(components: Iterable[dict], *, independent: bool) -> dict:
    """Welch-Satterthwaite approximation for explicitly independent contributions.

    Each component has name, standard_uncertainty, sensitivity, df. Infinite
    input df must be explicitly supplied, never inferred from 'Type B'. All
    sensitivities must convert their input contribution into a common output unit.
    """
    if independent is not True:
        raise ValueError('This formula requires explicitly declared independence; correlations unsupported')
    rows=list(components)
    if not rows or len(rows)>10000:raise ValueError('Require 1 to 10000 components')
    with localcontext() as ctx:
        ctx.prec=60
        terms=[];names=set()
        for row in rows:
            if not isinstance(row,dict) or set(row)!={'name','standard_uncertainty','sensitivity','df'}:
                raise ValueError('Each component requires exactly name, standard_uncertainty, sensitivity, df')
            name=row['name']
            if not isinstance(name,str) or not name.strip() or name in names:raise ValueError('Unique nonempty component names required')
            names.add(name)
            u=_finite(row['standard_uncertainty'],'standard uncertainty');c=_finite(row['sensitivity'],'sensitivity')
            if u<0:raise ValueError('Standard uncertainty cannot be negative')
            # Component df need only be positive; quantile evaluation has its own bounded range.
            if isinstance(row['df'],bool):raise ValueError('df cannot be boolean')
            try:nu=Decimal(str(row['df']))
            except Exception as exc:raise ValueError('Invalid component df') from exc
            if nu.is_nan() or nu<=0:raise ValueError('Component df must be positive or infinity')
            term=(Decimal(str(u))*Decimal(str(c)))**2
            terms.append((term,nu))
        variance=sum(t for t,n in terms)
        if variance<=0:raise ValueError('Zero combined variance does not define effective df')
        # Dimensionless weights avoid fourth-power underflow at small scales.
        denominator=sum((t/variance)**2/n for t,n in terms if n.is_finite())
        nu_eff=Decimal('Infinity') if denominator==0 else 1/denominator
        uc=variance.sqrt()
        if not math.isfinite(float(uc)) or float(uc)==0:
            raise ValueError('Combined standard uncertainty cannot be represented safely')
        return {'combined_standard_uncertainty':float(uc),
                'effective_df':'infinity' if nu_eff.is_infinite() else str(nu_eff),
                'method':'Welch-Satterthwaite independent-component approximation',
                'independence':'caller_declared_not_tested','exact_coverage_guaranteed':False,
                'limitations':['Not applicable to general correlated contributions.',
                 'The output distribution and reliability of component uncertainty estimates need justification.',
                 'Sensitivity coefficients must convert all contributions to a common output unit.']}


def expanded_interval(estimate: object, standard_uncertainty: object, *, probability: object,
                      df: object, unit: str, model: str) -> dict:
    """Named conditional interval; does not infer normality or df from numeric data."""
    if model not in {'normal_mean_iid','welch_satterthwaite_approximation'}:
        raise ValueError('Declare normal_mean_iid or welch_satterthwaite_approximation')
    if not isinstance(unit,str) or not unit.strip():raise ValueError('Explicit unit label required')
    estimate=_finite(estimate,'estimate');u=_finite(standard_uncertainty,'standard uncertainty')
    if u<=0:raise ValueError('Positive standard uncertainty required; zero does not certify exactness')
    k=coverage_factor(probability,df);half=k*u;lo,hi=estimate-half,estimate+half
    if not all(map(math.isfinite,(half,lo,hi))) or lo==hi:raise ValueError('Interval endpoints not representable')
    return {'estimate':estimate,'standard_uncertainty':u,'coverage_factor':k,
            'central_probability':float(probability),'df':'infinity' if _df(df)==math.inf else float(df),
            'lower':lo,'upper':hi,'expanded_uncertainty':half,'unit':unit.strip(),
            'model':model,'status':'conditional_model_interval','assumptions_checked':False,
            'limitations':['Coverage is conditional on the declared statistical model, not a measured guarantee.',
             'A frequentist confidence level concerns repeated use of the interval procedure.',
             'This calculation alone is not a conformity or fitness-for-purpose decision.']}
