# Measurement v1 release candidate scope

**Candidate:** 1.0.0-rc.1. **Final v1 accepted:** no. **Next domain allowed:** no.

This candidate preserves the eight agreed scientific families, the common record contract, source status distinctions and all existing release gates. It does not change the definition of v1 to bypass incomplete integrations or review. No next Atlas has been opened.

| Family | Implemented reference and methods | Scope boundary |
|---|---|---|
| Measurand and terminology | Source-linked definitions and explicit conditions | Domain-specific measurand validation still needs review |
| Units and quantity meaning | Bounded SI grammar, dimensional checks, declared kind, offsets and uncertainty scaling | Not a universal unit parser or quantity ontology |
| Repeated readings and dependence | Mean uncertainty and covariance-aware propagation | Caller must establish dependence and sampling model |
| Type B and resolution | Explicit distribution models, specification terms, structured report review | No automatic reading or authentication of certificates |
| Budgets and nonlinear models | Linearized budgets, correlations and documented nonlinear counterexamples | Not arbitrary nonlinear distribution propagation |
| Calibration and traceability | Degree-one/two fits, Pontius replay, traceability documentation checks | Original upstream bytes and actual certificate evidence still missing |
| Comparison and coverage | Conditional t factors, inverse intervals, normal knowledge probabilities and named rules | Not proof of model adequacy, global risk or regulatory compliance |
| Reporting and reproducibility | Source map, reports, retained discrepancies, portable exports and release checks | Independent review and platform/integration evidence still outstanding |

## What changed in the candidate

Six explicit CLI operations expose the new conversion, reported-uncertainty, certificate, specification, normal-probability and guard-band utilities. They do not alter Forge's search, context, Bitwork bridge, or evidence-admission semantics. The reference now has 92 bounded records and 44 source cards including the preserved legacy source, plus five starter-navigation records. None is silently promoted to independent scientific review.

## What the final gate still requires

G1 retains owner review and a frozen evaluation design. G2 retains complete source review with independent status kept separate. G3 requires the declared models and edge cases to be supported by numerical receipts. G4/G5 cover common conformance and context preservation. G6 requires actual Bitwork and downstream AI execution. G7 requires an independently authored held-out comparison. G8 requires clean releases and the supported Windows/Linux evidence. All required gates and approved frozen criteria must pass together.

The scope document is ready for review, not falsely signed on behalf of an owner or independent specialist. See the machine-readable gate report in the workflow workspace and [review handoff](V1_REVIEW_HANDOFF.md).
