# Compare results without inventing a verdict

[Reference index](../REFERENCE_GUIDE.md) · Content edition 0.5.0


## Begin with the same measurand

Metrological compatibility compares a difference with a chosen multiple of its uncertainty, accounting for covariance. [VCOMP: 2.47 definition and note 2](https://jcgm.bipm.org/vim/en/2.47.html)

**Original example:** two invented estimates differ by 0.1 mm. Their standard uncertainties are 0.2 mm and 0.3 mm, with covariance 0.03 mm². The difference variance is 0.04+0.09−2×0.03=0.07 mm², so u(diff)≈0.26458 mm. Omitting the covariance gives √0.13 instead. An explicit illustrative k=2 would set a 0.52915 mm threshold; it is not automatically a confidence probability or a manufacturing tolerance.

## Explain the coverage factor

NIST's conventional effective-degree approximation has stated distributional and independence conditions. The Welch–Satterthwaite expression is not a generic correlated-budget solver. [TNB: B.1–B.3, equation B-1](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-b-coverage-factors)

For two independent variance contributions of 1 and 1, each with 10 degrees of freedom, the expression gives ν_eff=20. That arithmetic alone does not choose a coverage factor. A t-distribution calculation or another defensible coverage method remains a separately justified step.

## Proposed decision record

Record the measurand match, estimates, units, covariance basis, chosen multiplier and its interpretation, applicable external requirement, and consequence of an inconclusive result. Keep an evidence gap when the required rule is missing.

**Stop condition:** requested “pass/fail” would require a tolerance, contractual rule, risk model or coverage assumption that has not been supplied. The present reference is not a product-conformity authority.


## Exact reference records

- [Uncertainty of a difference](../records/measurement-difference.md)
- [Compatibility of results needs a chosen multiplier](../records/compatibility-rule.md)
- [Coverage factor is not a universal probability](../records/coverage-conditions.md)
- [Coverage depends on uncertainty-estimate reliability](../records/coverage-degrees-of-freedom.md)
- [Welch–Satterthwaite effective degrees of freedom](../records/effective-degrees-of-freedom.md)

## Implemented in checkpoint 0.7.0

The [coverage supplement](../COVERAGE_METHODS.md) now supplies t factors, explicit independent-component effective degrees and conditional intervals. The earlier example remains a historical derivation. The [inverse replay](../INVERSE_INTERVAL_REPLAY.md) adds a reproducible single-use case and retains the publisher disagreement.
