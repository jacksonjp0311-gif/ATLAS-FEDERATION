"""Numerical teaching utilities. Returns models, not calibrated measurements.

Assumes first-order (linearized) uncertainty propagation and an explicitly
supplied covariance matrix. Coverage k is supplied, never inferred as 95%.
"""
from math import sqrt, isfinite, fsum, hypot


def _finite(v, label):
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        raise ValueError(f"{label} must be a finite number")
    try:value=float(v)
    except (OverflowError,ValueError) as exc:raise ValueError(f"{label} exceeds finite numeric range") from exc
    if not isfinite(value):raise ValueError(f"{label} must be a finite number")
    return value


def type_a(observations):
    """Return (sample mean, sample standard deviation, standard uncertainty of mean).

    At least two independent repeat readings are required; independence and
    stationarity must be justified by the experimenter, not this function.
    """
    xs = [_finite(x, 'observation') for x in observations]
    n = len(xs)
    if n < 2:
        raise ValueError('at least two observations required')
    mean = fsum(x/n for x in xs)
    sd = hypot(*(x-mean for x in xs))/sqrt(n-1)
    variance = sd*sd
    if not isfinite(mean) or not isfinite(variance):raise ValueError('sample exceeds finite floating-point range')
    return {'n': n, 'mean': mean, 'sample_sd': sqrt(variance), 'standard_uncertainty_mean': sqrt(variance/n),
            'assumptions': ['independent repeat measurements', 'stable process', 'sample standard deviation model']}


def combine_linear(sensitivities, covariance):
    """First-order c^T Sigma c with a unit-scale-invariant PSD check.

    The matrix is converted to a dimensionless correlation matrix before a
    pivoted Schur-complement check. Tolerances are relative, never a fixed
    absolute variance floor. At most eight inputs; not an arbitrary-precision
    or nonlinear propagation solver.
    """
    j = [_finite(x, 'sensitivity') for x in sensitivities]
    n = len(j)
    if not 1 <= n <= 8 or len(covariance) != n:
        raise ValueError('covariance dimensions mismatch or maximum 8 inputs exceeded')
    c = []
    for row in covariance:
        if len(row) != n: raise ValueError('covariance dimensions mismatch')
        c.append([_finite(x, 'covariance') for x in row])
    tol = 1e-12
    for i in range(n):
        if c[i][i] < 0: raise ValueError('negative variance')
        for k in range(n):
            pair_scale = max(abs(c[i][k]), abs(c[k][i]))
            if abs(c[i][k]-c[k][i]) > tol*pair_scale:
                raise ValueError('asymmetric covariance')
    u = [sqrt(c[i][i]) for i in range(n)]
    correlation = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if u[i] == 0 or u[k] == 0:
                if c[i][k] != 0: raise ValueError('zero variance cannot have nonzero covariance')
                continue
            # Sequential division avoids forming an under/overflowing product.
            corr = (c[i][k]/u[i])/u[k]
            if not isfinite(corr) or abs(corr) > 1+tol:
                raise ValueError('covariance implies correlation outside [-1, 1]')
            correlation[i][k] = corr
    a = [[(correlation[i][k]+correlation[k][i])/2 for k in range(n)] for i in range(n)]
    for step in range(n):
        pivot = max(range(step,n), key=lambda k:a[k][k])
        if pivot != step:
            a[step],a[pivot]=a[pivot],a[step]
            for row in a:row[step],row[pivot]=row[pivot],row[step]
        d=a[step][step]
        if d < -tol:raise ValueError('covariance matrix is not positive semidefinite')
        if d <= tol:
            if any(abs(a[i][k]) > tol for i in range(step,n) for k in range(step,n)):
                raise ValueError('covariance matrix is not positive semidefinite')
            break
        for i in range(step+1,n):
            for k in range(i,n):
                a[i][k] -= a[i][step]*a[k][step]/d
                a[k][i] = a[i][k]
    terms = [j[i]*c[i][k]*j[k] for i in range(n) for k in range(n)]
    if not all(isfinite(t) for t in terms):raise ValueError('propagation exceeds finite floating-point range')
    try:v=fsum(terms);bound=tol*fsum(abs(t) for t in terms)
    except OverflowError as exc:raise ValueError('propagation exceeds finite floating-point range') from exc
    if not isfinite(v) or v < -bound: raise ValueError('negative or nonfinite propagated variance')
    return {'variance':max(0.0,v),'combined_standard_uncertainty':sqrt(max(0.0,v)),
            'model':'first-order covariance propagation',
            'validation':'dimensionless pivoted positive-semidefinite check, relative tolerance 1e-12',
            'assumptions':['uncertainties evaluated at the provided operating point',
                           'sensitivity coefficients supplied by caller','covariance matrix supplied by caller']}


def expanded_uncertainty(standard_uncertainty, coverage_factor):
    u=_finite(standard_uncertainty,'standard uncertainty')
    k=_finite(coverage_factor,'coverage factor')
    if u<0 or k<=0:raise ValueError('u must be nonnegative and k positive')
    if not isfinite(u*k):raise ValueError('expanded uncertainty exceeds finite floating-point range')
    return {'expanded_uncertainty':u*k, 'coverage_factor':k,
            'warning':'Do not infer confidence probability from k without distribution and degrees-of-freedom assumptions.'}


def compare_difference(value_a, value_b, variance_a, variance_b, covariance_ab=0):
    """Return signed difference and its uncertainty, NOT a pass/fail verdict."""
    a=_finite(value_a,'value a');b=_finite(value_b,'value b')
    propagated=combine_linear([1,-1],[[variance_a,covariance_ab],[covariance_ab,variance_b]])
    difference=a-b
    if not isfinite(difference):raise ValueError('difference exceeds finite floating-point range')
    return {'difference':difference,'standard_uncertainty_difference':propagated['combined_standard_uncertainty'],
            'decision':'requires an explicit decision rule and coverage model'}
