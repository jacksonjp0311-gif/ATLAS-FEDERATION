# Effective degrees of freedom do not prove exact coverage

**ID:** `ws-approximation-ceiling` · **Origin:** `source_reported` · Assistant source-portion check, not independent review.

The conventional effective-degree method is approximate and assumes independent uncertainty components. It is not a general solution for correlated budgets.

## Assumptions

- All contributions refer to the same output unit after sensitivity scaling.

## Limitations

- The software refuses a declaration of non-independence and does not infer the output distribution.

## Evidence

[Coverage factors and effective degrees of freedom](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-b-coverage-factors) · B.1 caution and B.3 equation B-1. Inspected 12 November 2026. Original paraphrase or declared local derivation.
