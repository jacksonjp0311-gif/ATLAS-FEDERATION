# 4 Augmented weighting with a derivation and falsification cases

Let m_a(L) be a working conditional outcome mean and g(L) a working treatment probability. The sample implementation uses this residual-form score:

`phi = m1(L)-m0(L) + A/g(L)*(Y-m1(L)) - (1-A)/(1-g(L))*(Y-m0(L))`.

Its estimate is the sample mean of phi. The models are supplied by the caller. There is no automatic nuisance fitting, cross-fitting, statistical interval or empirical correctness claim in this release.

## Why this form is useful to audit

The score consists of a predicted contrast plus a treated residual correction minus a control residual correction. When every outcome and both outcome predictions are increased by the same constant, residuals and contrasts remain unchanged. Swapping treatment labels, exchanging m0 and m1 and replacing g with1-g should negate the result. These are testable invariants. They are not evidence that a real causal model is correct, but they catch common algebraic and implementation errors.

The literature includes a correction notice for the control-group augmentation in an AIPW tutorial ([Kurz article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8793316/); [publisher corrigendum](https://journals.sagepub.com/doi/10.1177/0272989X221075672)). The notice and exact inspected scope are retained separately. We derive and test the residual form rather than asserting that every web-rendered equation or the publisher's analysis code has been independently verified. The publisher's assurance about its code remains an attributed statement.

## Derive the conditional bias

In a fully stipulated synthetic population, write e for the generating treatment probability and mu_a for the generating outcome mean in a stratum. Conditional expectation of the score is

`m1-m0 + e/g*(mu1-m1) - (1-e)/(1-g)*(mu0-m0)`.

Subtract the true stratum contrast `mu1-mu0`. Collecting the treated and control residuals gives

`bias(L) = (e-g) * ((mu1-m1)/g + (mu0-m0)/(1-g))`.

Average this expression with the explicit target-stratum probabilities. If g=e, the conditional bias vanishes for arbitrary working outcome means. If both m_a=mu_a, it vanishes for arbitrary interior working g. If neither condition holds, the terms need not cancel. This is an algebraic expectation result for the declared model, not a statement that fitted nuisance functions are correct or that any one sample returns the exact target.

Causal interpretation adds the identification assumptions; large-sample inference with fitted functions adds further regularity and estimation requirements that are not implemented here. “Doubly robust” does not mean protected against an unmeasured common cause, an undefined treatment, an inapplicable target population, or arbitrary misuse of reused training outcomes. The inspected source discusses the conditional model robustness rather than a universal guarantee.

## Four exact experiments

The original population has two equally common job difficulties, generating propensities0.2 and0.8, and process outcome means `(0.8,0.9)` for easy and `(0.2,0.3)` for difficult work. The target ATE is+0.10.

| Working inputs | Population score result | Interpretation |
|---|---:|---|
| Both correct | +0.10 | Baseline algebra check |
| Correct propensity, wrong outcome means | +0.10 | One conditional bias factor is zero |
| Correct outcome means, wrong propensity | +0.10 | Both outcome residual means are zero |
| g=0.5 everywhere, m0=0.5 and m1=0.6 everywhere | −0.26 | Both wrong; bias is −0.36 |

The last row is not a failure hidden by a test pass. The test passes **because it correctly reproduces the known failure of those working models**. The numerical result is kept beside the true synthetic effect and the bias identity, so a consumer cannot mistake successful code execution for successful causal identification.

## What supplied predictions do and do not allow

A file of m0, m1 and g values is enough to compute the score. It is not enough to evaluate how those values were obtained. An actual analysis must retain training populations, feature timing, loss functions, fit diagnostics, fold assignment if applicable, transformations, model revisions and sampling design. The `nuisance_origin` field makes missing provenance visible but cannot verify a caller's claim of out-of-fold fitting.

Do not choose the estimate that looks most favorable when OR, HT, Hájek and AIPW disagree. Investigate normalization, weights, overlap, modeling, units, target and finite-sample behavior. Report the prespecified primary analysis and separately labeled sensitivity analyses. Agreement across methods also need not reveal a shared identification mistake.

**Related records:** `aipw-method`, `double-robust-limits`, `aipw-correction`, `aipw-residual-identity`, `aipw-bias-identity`, `constant-outcome-test`, `conflicting-method-results`.
