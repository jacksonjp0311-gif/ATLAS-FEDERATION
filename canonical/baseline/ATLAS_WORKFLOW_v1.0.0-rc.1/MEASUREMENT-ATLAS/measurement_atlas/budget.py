"""Transparent measurement uncertainty budgets. Educational calculations, not calibration certificates.

Units must already be harmonized; the caller supplies a defensible first-order model.
"""
from __future__ import annotations
from math import isfinite, sqrt
from .uncertainty import combine_linear, _finite


def _num(v, label):
    return _finite(v,label)


def type_b(half_width, distribution):
    """Standard uncertainty from an explicitly assumed symmetric bounded distribution.

    A uniform distribution has u=a/sqrt(3); a symmetric triangular distribution
    has u=a/sqrt(6). These are model assumptions, not default instrument truths.
    """
    a=_num(half_width,'half width')
    if a<0:raise ValueError('half width must be nonnegative')
    if distribution not in ('uniform','triangular'):
        raise ValueError('distribution must be uniform or triangular')
    return {'standard_uncertainty':a/sqrt(3 if distribution=='uniform' else 6),
            'distribution':distribution,'half_width':a,
            'limitations':'Distribution and symmetric bounds must be justified by source or experiment.'}


def uncertainty_budget(components, correlations=None, output_unit=None):
    """Calculate first-order combined uncertainty from named components.

    Each component has name, standard_uncertainty >= 0, sensitivity, and unit.
    Components must use one common measurement unit *after* multiplication by
    sensitivity. Correlations are a matrix; not treating absent values as inferred.
    """
    if not isinstance(components,list) or not 1<=len(components)<=8:
        raise ValueError('budget must contain 1..8 components')
    if output_unit is None or not isinstance(output_unit,str) or not output_unit.strip():
        raise ValueError('explicit nonblank output unit required')
    names=[];u=[];sens=[];unit=[]
    for c in components:
        if not isinstance(c,dict) or set(c)!={'name','standard_uncertainty','sensitivity','output_unit'}:
            raise ValueError('each component requires exact name, standard_uncertainty, sensitivity, output_unit')
        name=c['name']
        if not isinstance(name,str) or not name.strip() or name in names:
            raise ValueError('unique component names required')
        if c['output_unit'] != output_unit:
            raise ValueError('component output units mismatch; convert explicitly before budget')
        uu=_num(c['standard_uncertainty'],'standard uncertainty')
        if uu<0:raise ValueError('standard uncertainty cannot be negative')
        names.append(name);u.append(uu);sens.append(_num(c['sensitivity'],'sensitivity'))
    n=len(u)
    if correlations is None:
        corr=[[float(i==j) for j in range(n)] for i in range(n)]
    else:
        if not isinstance(correlations,list) or len(correlations)!=n or any(not isinstance(r,list) or len(r)!=n for r in correlations):
            raise ValueError('correlation matrix dimensions mismatch')
        corr=[[_num(v,'correlation') for v in row] for row in correlations]
        for i in range(n):
            if abs(corr[i][i]-1)>1e-10:raise ValueError('correlation diagonal must be 1')
            for j in range(n):
                if abs(corr[i][j])>1+1e-10:raise ValueError('correlation outside [-1,1]')
    # Validate correlation PSD even if a zero-uncertainty component would mask invalid correlations.
    combine_linear([1.0]*n, corr)
    cov=[[corr[i][j]*u[i]*u[j] for j in range(n)] for i in range(n)]
    propagated=combine_linear(sens,cov)
    net=[sens[i]*sum(cov[i][j]*sens[j] for j in range(n)) for i in range(n)]
    return {'schema':'measurement-atlas.budget.v1','output_unit':output_unit,
            'combined_standard_uncertainty':propagated['combined_standard_uncertainty'],
            'combined_variance':propagated['variance'],
            'signed_variance_contributions':dict(zip(names,net)),
            'components':[dict(c) for c in components],
            'correlation_matrix':corr,
            'assumptions':['first-order linear propagation','input standard uncertainties and sensitivities supplied by caller',
                           'correlation is specified or set to independence','all component uncertainties represented in compatible output units'],
            'decision':'no coverage probability or conformity decision inferred'}
