"""Pointwise normal-error regression intervals and bounded inverse intervals.

The inverse solves the two prediction-band equations, not a symmetric derivative
shortcut. A conservative derivative bound must prove both bands monotone before
root finding; otherwise this limited solver refuses the case. This numerical
bound is not an instrument certification or proof that the error model is true.
"""
from __future__ import annotations
from decimal import Decimal, localcontext
import json, hashlib
from importlib.resources import files
from .calibration import PolynomialFit, _number, PRECISION
from .coverage import coverage_factor
from .published_case import load_case

D=Decimal
ERROR_MODEL='iid_normal_equal_variance_exact_predictors'


def _check(fit: PolynomialFit, error_model: str):
    if not isinstance(fit,PolynomialFit):raise ValueError('A fitted PolynomialFit is required')
    if error_model != ERROR_MODEL:
        raise ValueError('Declare iid_normal_equal_variance_exact_predictors; this does not verify the assumptions')
    if fit.residual_sd<=0:raise ValueError('Positive residual standard deviation required')


def regression_interval(fit: PolynomialFit, x: object, *, probability: object,
                        new_observation: bool, error_model: str) -> dict:
    _check(fit,error_model)
    k=D(str(coverage_factor(probability,fit.residual_df)))
    with localcontext() as ctx:
        ctx.prec=PRECISION
        mean=fit.predict(x);sd=fit.prediction_sd(x,new_observation=new_observation)
        lower,upper=mean-k*sd,mean+k*sd
    return {'estimate':str(mean),'standard_deviation':str(sd),'coverage_factor':str(k),
            'lower':str(lower),'upper':str(upper),'unit':fit.y_unit,
            'probability':float(probability),'residual_df':fit.residual_df,
            'kind':'future_single_response_prediction' if new_observation else 'fitted_mean_confidence',
            'error_model':error_model,'assumptions_checked':False,'simultaneous_band':False}


def inverse_prediction_interval(fit: PolynomialFit, response: object, *, probability: object,
                                error_model: str, allow_clipping: bool=False) -> dict:
    _check(fit,error_model)
    if type(allow_clipping) is not bool:raise ValueError('allow_clipping must be a boolean')
    yy=_number(response);k=D(str(coverage_factor(probability,fit.residual_df)))
    with localcontext() as ctx:
        ctx.prec=PRECISION
        estimate=fit.invert(yy)
        n=fit.degree+1
        zs=[(v-fit.center)/fit.scale for v in (fit.x_min,fit.x_max)]
        deriv=[fit.scaled_coefficients[1]+(2*fit.scaled_coefficients[2]*z if n==3 else 0) for z in zs]
        if deriv[0]*deriv[1]<=0:raise ValueError('Calibration function is nonmonotone or flat')
        sign=D(1 if deriv[0]>0 else -1)
        # Cauchy-Schwarz: |d(sd_prediction)/dz| <= sqrt(h_prime^T Cov h_prime).
        # For degree <=2 the quadratic bound is convex, so its maximum is at an endpoint.
        variance_bound=[]
        for z in zs:
            hp=[D(0),D(1),2*z][:n]
            v=sum(hp[i]*hp[j]*fit.scaled_covariance[i][j] for i in range(n) for j in range(n))
            if v<0:raise ValueError('Negative derivative variance bound')
            variance_bound.append(v.sqrt())
        min_slope=min(abs(d) for d in deriv);sd_derivative_bound=max(variance_bound)
        margin=min_slope-k*sd_derivative_bound
        if margin<=max(min_slope,k*sd_derivative_bound)*D('1e-12'):
            raise ValueError('Monotonic prediction-band sufficient condition not met; general confidence-set solver required')
        clipped=[]
        def root(offset: Decimal, endpoint: str) -> Decimal:
            # Multiply by slope sign, yielding an increasing function in x.
            def f(x):return sign*(fit.predict(x)+offset*k*fit.prediction_sd(x,new_observation=True)-yy)
            lo,hi=fit.x_min,fit.x_max;fl,fh=f(lo),f(hi)
            if fl>0 or fh<0:
                if not allow_clipping:raise ValueError('Prediction interval endpoint outside supported calibration range')
                bound=lo if fl>0 else hi;clipped.append(endpoint);return bound
            if fl==0:return lo
            if fh==0:return hi
            for _ in range(180):
                mid=(lo+hi)/2;fm=f(mid)
                if fm==0 or hi-lo<=D('1e-24')*max(D(1),abs(mid)):return +mid
                if fm<0:lo=mid
                else:hi=mid
            raise ValueError('Prediction-band inversion did not converge')
        lower=root(sign,'lower');upper=root(-sign,'upper')
        if not lower<=estimate<=upper:raise ValueError('Inverted bounds failed ordering check')
        return {'schema':'measurement.inverse-interval/1','estimate':str(estimate),
                'lower':str(lower),'upper':str(upper),'response':str(yy),'unit':fit.x_unit,
                'central_probability':float(probability),'coverage_factor':str(k),'residual_df':fit.residual_df,
                'status':'range_limited_confidence_set' if clipped else 'conditional_single_use_interval',
                'range_limited':bool(clipped),'clipped_endpoints':clipped,
                'calibration_range':[str(fit.x_min),str(fit.x_max)],
                'method':'invert_pointwise_future_response_prediction_bounds',
                'monotonicity_sufficient_condition':{'min_mean_slope_in_scaled_coordinate':str(min_slope),
                     'sd_derivative_upper_bound':str(sd_derivative_bound),'positive_margin':str(margin)},
                'error_model':error_model,'assumptions_checked':False,'physical_validation':False,
                'limitations':['Single-use procedure, not a simultaneous or repeated-use guarantee.',
                    'Reference-input uncertainty, drift, hysteresis and model error are not supplied by this fit.',
                    'Caller must justify independent normally distributed equal-variance errors and exact predictors.',
                    'Clipped bounds describe only intersection with the measured predictor range; no full interval outside it is claimed.']}


def reproduce_interval():
    raise RuntimeError('Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.')


def main(argv=None):
    import argparse
    p=argparse.ArgumentParser(description=__doc__);p.parse_args(argv)
    try:
        report=reproduce_interval();print(json.dumps(report,indent=2,allow_nan=False));return 0
    except (OSError,ValueError,KeyError) as exc:
        print(json.dumps({'result':'failed','error':str(exc)}));return 2
