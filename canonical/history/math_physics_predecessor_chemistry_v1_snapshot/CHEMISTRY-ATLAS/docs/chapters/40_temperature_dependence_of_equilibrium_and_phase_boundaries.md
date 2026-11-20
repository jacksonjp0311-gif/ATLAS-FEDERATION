# 40. Temperature dependence of equilibrium and phase boundaries

**Field:** Thermodynamics · **Version:** v0.2.0 · **Scientific status:** original educational reference; cited publisher portions inspected, original publisher bytes not archived. No real experiment.

## Principles and physical scope

Chemical equilibria generally change with temperature because enthalpic and entropic terms change. The integrated van 't Hoff relation is a useful teaching approximation when reaction enthalpy is effectively constant over the chosen interval and there are no phase changes. Industrial materials systems can cross melting, sublimation, solubility or polymorphic boundaries, invalidating a simple extrapolation. Preserving a fitted equilibrium constant without a temperature and phase scope can cause future researchers to use it outside evidence. A better source format records ln K, source T, state convention, uncertainty and the enthalpy model used to reach another temperature. The chemistry model returns a logarithmic target to avoid overflow that could otherwise mask extrapolation instability.

## Equation and definitions

`ln(K2/K1) ≈ (Δ_rH°/R)(1/T1 − 1/T2) for approximately constant Δ_rH° and compatible standard states.`

Inputs and reference states must be declared. The algebra alone cannot establish source data validity, experimental behavior or physical safety.

## Derivation and why the relationship holds

Differentiate ln K=−Δ_rG°/(RT) using the Gibbs–Helmholtz identity under equilibrium assumptions, yielding d(ln K)/dT=Δ_rH°/(RT²). Integrate between temperatures and hold Δ_rH° fixed to obtain the stated relation. If Δ_rH° depends on temperature, its integral must use a measured heat-capacity model; a phase transition requires changing the physical model and species phases. The reference is a useful consistency check, not a high-pressure equilibrium simulator.

## Reconstruct without external AI

Take log K=0 at 300 K and a stipulated positive ΔH=1000 J/mol. Evaluate the target log K at 400 K and verify it increases. Now change ΔH to −1000 J/mol and show the direction reverses. List the missing information needed to apply this to an actual thermochemical dataset.

These examples are invented, not laboratory readings. Reproduce them by hand and compare only within the declared model domain.

## Failure case and missing evidence

A computed equilibrium constant does not show whether a reaction takes place quickly, safely, or reversibly. The constant-enthalpy approximation should not be treated as true through phase changes or large temperature ranges.

## Source provenance and rights

- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights
- [IUPAC Gold Book: chemical equilibrium](https://goldbook.iupac.org/terms/view/C01023) — Equilibrium, chemical potential and Gibbs relationship, 2025 online edition

**Not retained:** original publisher documents, real chemical samples, source tables and independent domain review.
