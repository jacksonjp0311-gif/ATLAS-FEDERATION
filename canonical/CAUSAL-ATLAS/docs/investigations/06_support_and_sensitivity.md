# Investigation 6: sensitivity and unsupported calculations are part of the result

## Do not optimize the story after seeing the answer

A scientific reference should show a method's limits before a user encounters them in expensive real work. This investigation deliberately creates three limitations: small IV support, curvature under a local-line RD fit, and too few distinct scores. All data are constructed. No tuning criterion, empirical winner or statistical interval is claimed.

For IV, compare uptake means 0.200 and 0.201. The denominator is 0.001. An outcome contrast of 0.0003 gives a ratio of 0.30. Perturb that contrast by 0.001 and the ratio becomes 1.30. The absolute perturbation is small while the effect-scale change is large because division amplifies it. The illustration is deterministic; it provides no first-stage F statistic, uncertainty estimate or calibrated rejection threshold.

A guard of 0.005 refuses the ratio; a guard of zero permits the arithmetic. Neither setting certifies an instrument. Record which setting was selected and why. Do not hide a failed ratio behind an unchanged successful process exit code: the JSON result expressly says `unresolved_first_stage`.

## Curvature creates a different kind of approximation error

Take quarter-step score values from −3 to +3, omitting zero. Below zero the response is `2+x+0.1x^2`; above zero it is `7+x+0.5x^2`. The exact difference of limiting boundary values is five. There is no random disturbance.

Triangular local-line fits at bandwidths 1, 2 and 4 yield 197/40, 191/40 and 41267/9400, approximately 4.925, 4.775 and 4.3901. The larger-window approximation has more curvature bias for this particular construction. A separate NumPy weighted least-squares calculation checks the implementation; it does not validate the causal interpretation.

In real data, making the window smaller changes precision and support as well as approximation bias. We report every requested window, including failures, rather than select the estimate closest to five. Five is available only because the mechanism is constructed. An empirical analyst would not know the true cutoff effect in advance.

## Repeated rows are not continuous support

Supply three observations at score −1 and three at score +1. Two independent lines each require a slope, but each side has only one distinct score. The tool refuses rather than silently fitting an intercept-only model. Repeating each row a hundred times would not add distinct score support.

This is an algebraic requirement, not a complete analysis of discrete-score RD designs. Such designs can need different assumptions and inferential methods; no claim is made that the underlying causal problem is universally impossible. The output identifies the unsupported local-line calculation, not an impossibility theorem about all methods.

## Prepare an auditable handoff

A usable result should show the full bandwidth grid, exact rule for including the cutoff, data exclusions, whether the jump in treatment is supported, and a statement of which diagnostics were not run. Preserve the caller's assumptions as assumptions. Keep approximation error, sampling uncertainty and identification uncertainty separate.

Run `python -m causal_atlas rd-bandwidths examples/rd_bandwidths.json`. Unsupported windows stay in the returned list. The shared context system can retain the associated method restrictions without any new navigation code. Before advancing to a real reproduction, specify the dataset, rights, original assignment rule, sampling unit and inferential method. This checkpoint closes a teaching and computational gap, not the empirical-reproduction or final Causal v1 requirements.
