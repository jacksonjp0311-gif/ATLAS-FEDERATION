# Causal Atlas reference guide

A bounded first reference edition. Begin with the target question, then assumptions, identification, calculation, and diagnostics. This is not a completed domain encyclopedia.

## Questions and targets

- [Association and intervention](records/association-intervention.md)
- [Potential outcomes](records/potential-outcomes.md)
- [Target population and contrast](records/target-population.md)
- [Identification versus estimation](records/identification.md)

## Graphs and adjustment

- [Causal directed acyclic graph](records/causal-dag.md)
- [Intervention operator](records/do-operator.md)
- [D-separation](records/d-separation.md)
- [Collider conditioning](records/collider-conditioning.md)
- [Back-door adjustment check](records/backdoor.md)

## Assumptions and estimators

- [Consistency for a defined treatment](records/consistency.md)
- [Conditional exchangeability](records/exchangeability.md)
- [Positivity and support](records/positivity.md)
- [Standardized contrast](records/standardization.md)
- [Inverse-probability weighting](records/ipw.md)
- [Weight diagnostics](records/weight-diagnostics.md)
- [Treatment-confounder feedback](records/time-varying.md)

## Study design

- [Specify a target trial](records/target-trial.md)
- [Align time zero](records/time-zero.md)
- [Baseline eligibility](records/baseline-eligibility.md)
- [Assignment and adherence contrasts](records/itt-per-protocol.md)
- [Outcome ascertainment](records/outcome-ascertainment.md)

## Diagnostics and limits

- [Negative-control outcome](records/negative-control-outcome.md)
- [Negative-control exposure](records/negative-control-exposure.md)
- [Limits of null controls](records/negative-control-limits.md)

## Worked examples

Run `python -m causal_atlas casebook` to inspect fully synthetic, exactly reproducible examples. No patient, operator, or laboratory data are included. See [CASEBOOK.md](CASEBOOK.md).

## Scope not implemented

Continuous treatments, censoring, longitudinal g-methods, mediation identification, instrumental variables, transportability, sensitivity bounds, causal discovery and statistical confidence intervals require later work. Negative controls are reference concepts, not automated bias certification.
