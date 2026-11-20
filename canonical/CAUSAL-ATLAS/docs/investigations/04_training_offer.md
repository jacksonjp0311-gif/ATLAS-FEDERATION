# Investigation 4: an offer changes attendance, but whose outcome effect is identified?

## Question and scope

This original synthetic investigation separates the effect of an invitation from the effect of actually receiving training. It is not an account of the user's employer or a real participant dataset. The substantive question is whether training helps the people induced to attend by a particular offer, and whether that conclusion can be extended to everybody. Treating these as the same question is the deliberate trap.

The constructed population contains three types. Never-takers have mass 0.30 and potential outcome means 0.60 without training and 0.50 with training. Always-takers have mass 0.20 and means 0.20 and 0.30. Compliers have mass 0.50 and means 0.40 and 0.70. Assignment to the offer is stipulated independent of these types. Initially the offer has no direct effect on the outcome and there are no defiers.

## Derive, do not guess, the comparison

Without an offer the attendance mean is 0.20. With an offer it is 0.70. The first stage is 0.50. Expected outcomes are 0.44 without the offer and 0.59 with it, giving an offer contrast of 0.15. Dividing 0.15 by 0.50 yields 0.30, exactly the complier effect. The full-population effect is instead 0.14 because the effects in the never- and always-taking groups differ.

The tool reports both quantities because they are known in this fully specified model. In an actual study the potential outcome pair for each type would not be observed. A real reference packet could report the identified local target but must not pretend that this fixture teaches it the factory-wide effect. Changing the invitation can also change who complies.

## Deliberately violate exclusion

Now add 0.05 directly to the outcome whenever a place is offered. The first stage remains 0.50; the reduced form becomes 0.20. The ratio becomes 0.40 although the underlying training effect among compliers remains 0.30. Random assignment of the offer is still stipulated. Randomization did not remove the invitation's direct outcome pathway.

A scenario assuming direct contribution between zero and 0.05 produces a training-effect range of [0.30,0.40]. It is not a sampled confidence interval and cannot be interpreted as one. The source of those assumptions must be part of an empirical analysis record.

## Deliberately violate monotonicity

A second model contains 0.40 compliers with effect 0.10, 0.30 defiers with effect 0.90, and 0.30 never-takers with effect 0.20. Everyone benefits from treatment, but the outcome contrast is −0.23 and uptake contrast is +0.10. Their ratio is −2.30. A positive average first stage did not establish individual monotonicity.

## Evidence needed for real work

Request the allocation protocol, actual attendance records, eligibility timing, definition of training, an outcome collection plan, and evidence about alternative pathways and cross-worker spillovers. Identify the assignment unit; individual records do not create independent samples when a supervisor or shift receives the invitation as a group. Establish how missing outcomes are handled before selecting a model. None of this evidence is supplied by the constructed table.

Run `python -m causal_atlas quasi-casebook` or `python -m causal_atlas iv-population examples/iv_training_types.json`. The output preserves the supplied mechanism, compliance masses, local effect, population effect and exact decomposition. For the theorem's scope see [Chapter 9](../chapters/09_instrumental_variables.md); for assumptions and refusal behavior see [the IV design form](../templates/IV_DESIGN_REVIEW.md).
