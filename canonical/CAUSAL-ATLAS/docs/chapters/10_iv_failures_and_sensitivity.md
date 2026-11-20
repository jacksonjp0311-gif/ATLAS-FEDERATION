# 10 Instrumental variables: failures, sensitivity and identification limits

## Do not confuse a calculable ratio with a defensible effect

The instrument route can fail in several different places. If the instrument does not change treatment, division is undefined. If it changes treatment only slightly, perturbations in a small numerator or denominator can dominate the ratio. If it affects outcomes through another path, exclusion fails. If some units respond in the opposite direction, the ratio can become a signed mixture rather than a complier average. These are distinct problems; one diagnostic cannot clear all of them.

Staiger and Stock's weak-instrument research analyzes why conventional approximations can be unreliable when instrument–treatment relationships are weak. The Atlas inspected the introduction, not every theorem or an implementation of their inference procedures. See [SS1997](../SOURCE_REGISTER.md#ss1997), pp. 557–559. Our small-denominator guard is a computational choice, not a replacement for that statistical analysis.

## Direct-path contamination: an exact constructed example

Reuse the population in Chapter 9, whose true complier effect is 0.30. Add an outcome improvement of 0.05 from the invitation itself for every type: perhaps the synthetic mechanism includes extra attention independently of actual training. Now the offer contrast is 0.20, while the attendance contrast remains 0.50. The ratio becomes 0.40. Arithmetic is correct, but interpreting it as the training effect introduces a 0.10 error.

For this specified additive mechanism,

`DeltaY = theta*DeltaD + gamma`,

where `gamma` is the direct contribution to the assignment contrast. Thus

`theta(gamma) = (DeltaY-gamma)/DeltaD`.

If the investigator assumes `gamma` lies between 0 and 0.05, the scenario range is [0.30, 0.40]. The bounds are conditional on the supplied interval and the additive decomposition. They are neither estimated from the four means nor a confidence interval. They do not cover arbitrary dependence violations, heterogeneous direct effects with a different target, or missing-outcome mechanisms by magic.

`exclusion_sensitivity` preserves the input bounds, signs, first stage and equation. When the denominator is negative it orders the resulting endpoints correctly. It never clips an uncomfortable estimate to a convenient range. When the denominator is zero or fails the declared operational guard, the result remains unresolved.

## Defiers can reverse a ratio even when every type benefits

Construct three types: 0.40 compliers with effect +0.10, 0.30 defiers with effect +0.90, and 0.30 never-takers with effect +0.20. Take the offer to be independent and exclusion to hold within this model. The first stage is `0.40-0.30=0.10`, which is positive. The reduced form is `0.40*0.10-0.30*0.90=-0.23`. The ratio is −2.30 even though every individual type has a positive treatment effect and the population mean effect is +0.37.

This does not refute the local-effect theorem. It violates one of its conditions. The numerator is a signed effect mixture, and the denominator subtracts the shares of oppositely responding types. The common record links the ratio example to the monotonicity qualification so a future consumer cannot retrieve the impressive negative number without its cause.

A ratio outside the possible range of a binary-outcome average is a warning in this constructed example, not a universal rule proving which empirical assumption failed. Sampling error can also produce out-of-range estimates. Never use clipping to conceal an identification problem.

## Weak numerical support is not evidence of a large effect

Take treatment-arm means 0.200 and 0.201, so the first stage is 0.001. Let the outcome contrast be 0.0003. The ratio is 0.30. An additive perturbation of just 0.001 to that outcome contrast changes the ratio to 1.30. This is a deterministic sensitivity illustration, not a repeated-sample distribution or a weak-IV test.

Three separate outputs matter: the small first stage, the selected refusal threshold, and the absence of sampling inference. A threshold of 0.005 rejects this ratio. A threshold of zero permits the arithmetic but still does not call it identified. The tool must not silently select a threshold after looking at the result. A strong denominator would not rescue an instrument that directly affects the outcome.

## What an empirical extension must add

Before real use, specify the sampling unit and assignment process, the exact instrument contrast, covariates and missingness rules. Retain both reduced-form and first-stage estimates, their uncertainty and their dependence. Choose an appropriate weak-identification-aware inferential method and compare it to the ordinary approximation. Predefine what happens when the evidence cannot support a useful interval; an unbounded or very wide answer can be more honest than a finite but misleading one.

This version does not implement two-stage least-squares model fitting, Anderson–Rubin tests, generalized method-of-moments estimators, cluster-robust covariance or instrument selection. Naming these methods is not claiming support. The bounded deliverable is exact finite-model reasoning, supplied-mean ratios and explicit direct-contribution sensitivity.

Use [IV_DESIGN_REVIEW.md](../templates/IV_DESIGN_REVIEW.md) to document the study, and attach the finite-model counterexamples to any explanation of why the assumptions matter.
