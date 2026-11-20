# Investigation 12 — NIST copper thermochemistry reproduction

**Question.** Can the Materials Atlas reproduce a second published numerical representation, separate from Hahn1's regression observations, while keeping its domain explicit?

**Authoritative source.** NIST WebBook, SRD69, copper, solid-phase Shomate representation 298–1358 K, Chase 1998. The source reports a compiled fitted representation, not direct observations from this Atlas. [Public derivative: the source coefficients and selected display rows are withheld pending redistribution clearance.] [Primary link](https://webbook.nist.gov/cgi/inchi?ID=C7440508&Table=on&Type=JANAFS).

**Reproduction method.** Use t=T/1000 in the published Cp, H relative to 298.15 K, S formulas; verify heat capacity in J/(mol K), enthalpy in kJ/mol and entropy in J/(mol K). [Public derivative: source-row evaluation results and numerical comparison errors are withheld pending redistribution clearance; the comparison is unavailable in this edition.]

**Independent functional identity.** For an interior temperature T, numerically differentiate H(T) against T and check Cp, with 1000 J/kJ scaling. Alternatively integrate Cp(T)/1000 from 400 to 900 K using a separate quadrature algorithm and compare with the corresponding enthalpy difference [dataset-derived numerical result withheld pending redistribution clearance]. A successful identity validates the formula implementation in this domain, not the underlying source assessment.

**Counterexample.** Asking for Cp at 1500 K must fail: that temperature is beyond the published **solid phase** fit even though the same NIST page provides separate **liquid** data. Do not silently switch phases; the transition enthalpy cannot be inferred by continuing a single solid fit. Similarly, a named copper alloy, composite or specimen does not inherit elemental-copper coefficients without measurement/model justification.

**Provenance.** No original HTTP transport bytes were authenticated. Checked date 2026-11-12. Numerical facts were read from the publisher HTML; this package stores a local normalized computation record, not a complete NIST source snapshot. NIST's displayed coefficient rounding precludes a separately justified coefficient uncertainty. The previous Hahn1 response-unit ambiguity remains untouched.

**Outcome.** Successful narrow computational reproduction; no material property qualification, laboratory replication, or permission to extrapolate.
