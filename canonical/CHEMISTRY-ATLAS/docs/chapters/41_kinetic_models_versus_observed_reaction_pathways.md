# 41. Kinetic models versus observed reaction pathways

**Field:** Kinetics · **Version:** v0.2.0 · **Scientific status:** original educational reference; cited publisher portions inspected, original publisher bytes not archived. No real experiment.

## Principles and physical scope

Kinetics asks how rapidly a system changes, not merely whether one equilibrium state has lower Gibbs energy. Reaction rates depend on mechanism, catalyst, transport, temperature and composition. A formal Arrhenius rate coefficient can summarize one mechanism over a limited temperature interval, but parameters are not universal constants of a named molecular formula. Some processes include reversible steps, intermediates, photochemical channels and competing phases. The NIST Chemical Kinetics Database contains measured and evaluated reaction-parameter records, so a future model must preserve the original reaction identity and bibliography alongside its numerical fit. A small offline simulation may verify differential-equation arithmetic while remaining empirically disconnected from any actual chemical pathway.

## Equation and definitions

`k(T)=A exp(−E_a/(RT)); first-order c(t)=c0 exp(−kt). For two temperatures, ln(k2/k1)=−E_a/R (1/T2−1/T1).`

Inputs and reference states must be declared. The algebra alone cannot establish source data validity, experimental behavior or physical safety.

## Derivation and why the relationship holds

The first-order law assumes a rate proportional to concentration and a constant coefficient over time. Separating variables yields the exponential solution. The Arrhenius relation is an empirical/transition-state-motivated temperature dependence and is locally useful when activation energy is approximately constant. A more complex reaction network requires coupled differential equations and potentially stiffness-aware numerical integration. A chemical database must distinguish a kinetic parameter from a prediction that every formulation shares it.

## Reconstruct without external AI

For an invented first-order coefficient k=0.1 s−1 and initial dimensionless amount 1, compute exp(−1) after 10 seconds. Compare with a distinct Arrhenius temperature-ratio calculation. Verify separately that the model does not claim a measured half-life or chemical safety.

These examples are invented, not laboratory readings. Reproduce them by hand and compare only within the declared model domain.

## Failure case and missing evidence

A thermodynamically favorable reaction can be kinetically slow, and a high-temperature extrapolation can change mechanisms. No real reaction, catalysts, harmful substances or industrial process recipes are used by the reference.

## Source provenance and rights

- [NIST Chemical Kinetics Database, SRD 17](https://kinetics.nist.gov/kinetics/) — Data Version 2026, gas-phase reaction kinetics indexing and research references
- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights

**Not retained:** original publisher documents, real chemical samples, source tables and independent domain review.
