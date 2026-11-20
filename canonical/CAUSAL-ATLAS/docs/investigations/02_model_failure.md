# Investigation B Deliberately break the working models

**Data origin: the same original finite population as Investigation A.**

## Why known truth is useful here

A real observational analysis does not reveal its true propensity and both potential outcome means. A deliberately authored population does. That makes it suitable for falsification exercises, not for proving real-world effectiveness. We vary the working functions while keeping the generating distribution fixed.

The truth is ATE=1/10. The generating propensity is1/5 for easy work and4/5 for difficult work. Generating outcome means are(4/5,9/10) and(1/5,3/10). The input file distinguishes generating `e,mu0,mu1` from working `g,m0,m1`; overwriting the former to fit the latter would erase the test.

## Exact checks

With either the true propensity or both true outcome means, the AIPW population expectation equals1/10. With both working components wrong—g=1/2 for both groups and outcome means m0=1/2,m1=3/5 for both groups—the result is−13/50, or−0.26. The bias is−9/25, or−0.36.

The runtime checks the independently derived algebraic expression for that bias in every synthetic population. It also checks constant-outcome shifts and treatment-label reversals on sample scores. These tests target different errors; simply recomputing one reference value with the same formula would be weaker evidence.

```sh
python -m causal_atlas population examples/process_both_models_wrong.json
```

## Do not repair a failed model by renaming the result

The −0.26 result is retained with `propensity_exact: false`, `outcome_means_exact: false`, the known true effect and the bias. A test passes when it reproduces that failure faithfully. It does not change the example's status to an identified causal answer.

In real data the exactness flags cannot be obtained by looking at outcome fit alone. A propensity score can predict treatment well while creating extreme weights, and a good prediction score need not justify causal adjustment. Conversely, a disappointing prediction score does not by itself invalidate every target contrast. Those are different questions requiring design, diagnostics and statistical theory.

## A second nonidentification exercise

The exact binary engine evaluates two models that share the same observed joint distribution: a hidden common cause determines both A and Y, or A directly determines Y. Both show an observed difference of1; their intervention effects are0 and1. This is a separate failure mode from bad nuisance fitting. No choice among the four estimators can infer which of these two mechanisms is true from their identical observation table alone.

## Review prompt

Explain which assumption changed in each test and whether more sample size would necessarily solve it. Distinguish model-estimation error from identification ambiguity. A reader who reports “AIPW is wrong” without those distinctions has not understood the example; a reader who reports “doubly robust means safe” has also failed the review.

**Evidence:** local residual-score derivation, exact finite-model enumeration, retained source correction notice. **Unperformed:** fitted-model benchmark, sampling inference, independent human review.
