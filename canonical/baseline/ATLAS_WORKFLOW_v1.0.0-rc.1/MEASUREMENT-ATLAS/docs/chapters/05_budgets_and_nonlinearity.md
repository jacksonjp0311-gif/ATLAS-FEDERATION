# Build the uncertainty model and budget

[Reference index](../REFERENCE_GUIDE.md) · Content edition 0.5.0


## Use the complete declared model

The measurement function should represent the measurement process, including significant correction and variability contributions, rather than only a physical-law formula. First-order propagation uses sensitivities and input covariance. [TNA: A.1–A.3](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty)

For this package, assemble named inputs, estimate, unit, standard uncertainty, evaluation method, sensitivity and covariance justification. A budget worksheet is provided under `templates/`; it contains no calibration evidence by itself.

## Local worked example

For a deliberately simple area model A=L×W, take invented inputs L=100 mm, W=50 mm, u(L)=0.2 mm and u(W)=0.1 mm with zero covariance. Sensitivities are 50 mm and 100 mm. The first-order variance is 200 mm⁴, giving standard uncertainty about 14.1421 mm² around the nominal area 5000 mm². This is a linearized result, not an exact distribution for the product.

## Test the approximation

Consider an original finite-distribution counterexample: X is equally likely to be −1, 0 or 1; Y=X². E[X]=0 and the derivative at zero is zero. First-order propagation therefore produces zero variance. Direct enumeration instead gives E[Y]=2/3 and Var(Y)=2/9. A working implementation can faithfully calculate an inadequate approximation.

The casebook verifies both arithmetic paths and labels the discrepancy. A more appropriate distributional calculation is needed for that example; the counterexample does not condemn all first-order methods.

**Stop condition:** the local linearization fails a relevant test or important model inputs are missing. Do not convert software success into physical-model validation.


## Exact reference records

- [First-order uncertainty propagation](../records/linear-propagation.md)
- [Correlated measurement inputs](../records/covariance.md)
- [Combine Type A and Type B components](../records/combined-uncertainty.md)
- [Corrections for systematic effects](../records/systematic-corrections.md)
- [A zero derivative can hide nonlinear uncertainty](../records/linearization-counterexample.md)
