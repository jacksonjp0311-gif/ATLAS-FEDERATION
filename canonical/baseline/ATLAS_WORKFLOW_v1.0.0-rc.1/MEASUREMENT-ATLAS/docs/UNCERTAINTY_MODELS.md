# Uncertainty models and applicability

These formulae are standard mathematical models. Their correctness under a particular experimental regime requires validation of assumptions and an uncertainty budget.

For independent repeated readings x_i, sample mean m = sum(x_i)/n, sample SD s = sqrt(sum((x_i - m)^2)/(n - 1)), and Type A standard uncertainty u(m) = s/sqrt(n). Serial correlation, drifting instruments, outliers and bias break the naive model.

For a differentiable measurand f(x), first-order propagation is u_y^2 ≈ J C Jᵀ, where J is the vector of sensitivity coefficients and C is the input covariance matrix. Strong nonlinearity, asymmetric distributions, or poorly characterized tails may require simulation or a different method. The implementation checks covariance symmetry and positive semidefiniteness for up to eight variables, but it cannot validate a physical covariance estimate.

Expanded uncertainty U = k u requires k to be stated. A claim of approximate coverage probability requires a distribution model and effective degrees of freedom or another justified coverage procedure.

Difference between estimates a and b has variance u_a² + u_b² - 2 cov(a,b), assuming compatible units and the same measured quantity. No equivalence or acceptance decision is automatic.

**Sources for detailed auditing (link-only):** [NIST TN 1297](https://www.nist.gov/pml/nist-technical-note-1297), [BIPM JCGM publications](https://www.bipm.org/en/committees/jc/jcgm/publications), [NIST SI Units](https://www.nist.gov/pml/owm/metric-si/si-units). These are research entry points; the starter did not perform a new source-passage verification or mirror the full text.
