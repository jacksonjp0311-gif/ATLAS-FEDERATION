"""Small, dependency-free OLS reproduction tools for declared calibration models.

Only degree 1 and 2 polynomials are supported. Decimal arithmetic, a centered
scaled predictor, and pivoted elimination are used for the tiny normal system.
This is not a general-purpose regression library, a traceability determination,
or an instrument calibration service. Predictors are treated as exact and errors
as independent with a common variance. Those are assumptions, not test results.
"""
from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, localcontext
from typing import Iterable

D = Decimal
PRECISION = 60


def _number(value: object) -> Decimal:
    if isinstance(value, bool):
        raise ValueError('Booleans are not measurements')
    try:
        out = D(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError('Expected a finite numeric value') from exc
    if not out.is_finite() or (out and abs(out.adjusted()) > 100):
        raise ValueError('Nonfinite or out-of-range numeric value')
    return out


def _solve_inverse(a: list[list[Decimal]], b: list[Decimal]):
    n = len(b)
    aug = [a[i][:] + [D(int(i == j)) for j in range(n)] + [b[i]] for i in range(n)]
    scale = max(abs(v) for row in a for v in row)
    for j in range(n):
        pivot = max(range(j, n), key=lambda i: abs(aug[i][j]))
        if abs(aug[pivot][j]) <= scale * D('1e-45'):
            raise ValueError('Rank-deficient or unsupported ill-conditioned design')
        aug[j], aug[pivot] = aug[pivot], aug[j]
        divisor = aug[j][j]
        aug[j] = [v / divisor for v in aug[j]]
        for i in range(n):
            if i != j:
                multiplier = aug[i][j]
                aug[i] = [u - multiplier * v for u, v in zip(aug[i], aug[j])]
    return tuple(row[-1] for row in aug), tuple(tuple(row[n:2*n]) for row in aug)


@dataclass(frozen=True)
class PolynomialFit:
    degree: int
    n: int
    distinct_levels: int
    x_unit: str
    y_unit: str
    x_min: Decimal
    x_max: Decimal
    center: Decimal
    scale: Decimal
    scaled_coefficients: tuple[Decimal, ...]
    coefficients: tuple[Decimal, ...]
    scaled_covariance: tuple[tuple[Decimal, ...], ...]
    covariance: tuple[tuple[Decimal, ...], ...]
    residuals: tuple[Decimal, ...]
    sse: Decimal
    residual_sd: Decimal
    residual_df: int
    pure_error_ss: Decimal
    pure_error_df: int
    lack_of_fit_ss: Decimal
    lack_of_fit_df: int
    lack_of_fit_F: Decimal | None
    r_squared: Decimal | None

    def predict(self, x: object, *, allow_extrapolation: bool = False) -> Decimal:
        xx = _number(x)
        if not allow_extrapolation and not self.x_min <= xx <= self.x_max:
            raise ValueError('Prediction is outside the fitted load range')
        with localcontext() as ctx:
            ctx.prec = PRECISION
            z = (xx - self.center) / self.scale
            value = D(0)
            for c in reversed(self.scaled_coefficients):
                value = value * z + c
            return +value

    def prediction_sd(self, x: object, *, new_observation: bool) -> Decimal:
        """Model-based SD; caller explicitly chooses mean or one future response."""
        if not isinstance(new_observation, bool):
            raise ValueError('Specify new_observation as a boolean')
        xx = _number(x)
        if not self.x_min <= xx <= self.x_max:
            raise ValueError('Prediction is outside the fitted load range')
        with localcontext() as ctx:
            ctx.prec = PRECISION
            z = (xx - self.center) / self.scale
            h = [D(1), z, z*z][:self.degree + 1]
            variance = sum(h[i]*h[j]*self.scaled_covariance[i][j]
                           for i in range(len(h)) for j in range(len(h)))
            if new_observation:
                variance += self.residual_sd**2
            if variance < 0:
                raise ValueError('Negative model variance')
            return variance.sqrt()

    def invert(self, response: object) -> Decimal:
        """Resolve the unique monotone in-range solution; never pick an outside root."""
        yy = _number(response)
        with localcontext() as ctx:
            ctx.prec = PRECISION
            lo, hi = self.x_min, self.x_max
            b = self.coefficients[1]
            c = self.coefficients[2] if self.degree == 2 else D(0)
            d_lo, d_hi = b + 2*c*lo, b + 2*c*hi
            if d_lo*d_hi <= 0:
                raise ValueError('Inverse is nonmonotone or flat over the calibration range')
            gl, gh = self.predict(lo)-yy, self.predict(hi)-yy
            if gl == 0: return lo
            if gh == 0: return hi
            if gl*gh > 0:
                raise ValueError('Response has no in-range inverse; extrapolation refused')
            for _ in range(160):
                mid = (lo + hi)/2
                gm = self.predict(mid)-yy
                if gm == 0 or hi-lo <= D('1e-30')*max(D(1),abs(mid)):
                    return +mid
                if gl*gm <= 0:
                    hi = mid
                else:
                    lo, gl = mid, gm
            raise ValueError('Inverse did not converge')

    def as_dict(self) -> dict:
        def dec(v): return None if v is None else str(v)
        if self.pure_error_df <= 0:
            status = 'unavailable_no_replicates'
        elif self.lack_of_fit_df <= 0:
            status = 'unavailable_no_lack_of_fit_degrees_of_freedom'
        elif self.pure_error_ss == 0:
            status = 'undefined_zero_pure_error'
        else:
            status = 'computed_not_automatically_accepted'
        return {
            'degree': self.degree, 'n': self.n, 'distinct_levels': self.distinct_levels,
            'x_unit': self.x_unit, 'y_unit': self.y_unit,
            'range': [str(self.x_min),str(self.x_max)],
            'coefficients': [str(v) for v in self.coefficients],
            'coefficient_covariance': [[str(v) for v in row] for row in self.covariance],
            'residual_sd': str(self.residual_sd), 'residual_df': self.residual_df,
            'sse': str(self.sse), 'r_squared': dec(self.r_squared),
            'lack_of_fit': {'F':dec(self.lack_of_fit_F),'status':status,
                'pure_error_ss':str(self.pure_error_ss),'pure_error_df':self.pure_error_df,
                'lack_of_fit_ss':str(self.lack_of_fit_ss),'lack_of_fit_df':self.lack_of_fit_df},
            'method': 'centered_scaled_decimal_ols_60_digits_degree_1_or_2',
            'assumptions': ['Reference x values treated as exact.',
                'Independent additive errors with common response variance.',
                'Regression model form and calibration stability require separate checks.',
                'No claim of SI units, traceability, normality or fitness for purpose.'],
            'calibration_certification': False,
        }


def fit_polynomial(x: Iterable[object], y: Iterable[object], *, degree: int,
                   x_unit: str, y_unit: str) -> PolynomialFit:
    """Fit a bounded small calibration model and compute replicated lack-of-fit."""
    if type(degree) is not int or degree not in (1,2):
        raise ValueError('Only polynomial degree 1 or 2 is supported')
    if not isinstance(x_unit,str) or not x_unit.strip() or not isinstance(y_unit,str) or not y_unit.strip():
        raise ValueError('Both unit labels must be explicit; unknown source units must be stated')
    xs, ys = tuple(map(_number,x)), tuple(map(_number,y))
    n, p = len(xs), degree+1
    if n != len(ys) or n <= p or n > 10000:
        raise ValueError('Equal-length inputs, more rows than coefficients and at most 10000 rows required')
    if len(set(xs)) < p:
        raise ValueError('Too few distinct predictor values for the model')
    with localcontext() as ctx:
        ctx.prec = PRECISION
        center = sum(xs,D(0))/n
        scale = max(abs(v-center) for v in xs)
        zs = [(v-center)/scale for v in xs]
        design = [[D(1),z,z*z][:p] for z in zs]
        a = [[sum(row[i]*row[j] for row in design) for j in range(p)] for i in range(p)]
        b = [sum(row[i]*yy for row,yy in zip(design,ys)) for i in range(p)]
        coeff, inv = _solve_inverse(a,b)
        fitted = [sum(h*c for h,c in zip(row,coeff)) for row in design]
        residuals = tuple(yy-f for yy,f in zip(ys,fitted))
        sse = sum(e*e for e in residuals)
        mse = sse/(n-p)
        cov = tuple(tuple(mse*v for v in row) for row in inv)
        transform = [[D(1),-center/scale,(center/scale)**2],
                     [D(0),1/scale,-2*center/scale**2],
                     [D(0),D(0),1/scale**2]]
        transform = [row[:p] for row in transform[:p]]
        original = tuple(sum(transform[i][j]*coeff[j] for j in range(p)) for i in range(p))
        orig_cov = tuple(tuple(sum(transform[i][k]*cov[k][l]*transform[j][l]
                         for k in range(p) for l in range(p)) for j in range(p)) for i in range(p))
        groups: dict[Decimal,list[Decimal]] = {}
        for xx,yy in zip(xs,ys): groups.setdefault(xx,[]).append(yy)
        pure_ss = sum(sum((yy-sum(g)/len(g))**2 for yy in g) for g in groups.values())
        pure_df, lof_df = n-len(groups), len(groups)-p
        # Compute nonnegative between-replicate model error directly, not by cancellation.
        lof_ss = D(0)
        for xx,g in groups.items():
            z = (xx-center)/scale; h = [D(1),z,z*z][:p]
            f = sum(c*v for c,v in zip(coeff,h))
            lof_ss += len(g)*(sum(g)/len(g)-f)**2
        fstat = (lof_ss/lof_df)/(pure_ss/pure_df) if pure_df>0 and lof_df>0 and pure_ss>0 else None
        ybar = sum(ys)/n; total = sum((v-ybar)**2 for v in ys)
        r2 = D(1)-sse/total if total>0 else None
        return PolynomialFit(degree,n,len(groups),x_unit.strip(),y_unit.strip(),min(xs),max(xs),
            center,scale,coeff,original,cov,orig_cov,residuals,sse,mse.sqrt(),n-p,
            pure_ss,pure_df,lof_ss,lof_df,fstat,r2)
