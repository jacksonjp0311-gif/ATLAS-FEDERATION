# 53. Thermochemical data and the Shomate heat-capacity relation

**Theme:** Thermochemical reconstruction · **Chemistry Atlas scoped research v1.0.0**

**Evidence level:** project-written mathematical/reference explanation with scope-limited official sources. Every worked numeric input is hypothetical; publisher originals are not in this archive.

## Scientific foundation

Temperature-dependent thermochemistry is essential to reconstructing heat engines, material phases and chemical-process energy accounting. Tabulated heat capacities, entropies and enthalpies cannot safely be copied without their source conditions, phase, pressure standard and fitted temperature range. The NIST Chemistry WebBook describes Shomate fitted polynomials and standard thermodynamic tables for multiple phases. The fitted coefficients for a particular species are source data that must be accompanied by the original table, version and validation range. This edition implements analytic integration from user-supplied coefficients but imports no authentic coefficient table.

## Governing relationship and dimensional conventions

`Let t=T/1000. Cp°(T)=A+Bt+Ct²+Dt³+E/t² [J mol^-1 K^-1]. DeltaH=integral_(T1 to T2) Cp dT; DeltaS=integral Cp/T dT.`

Dimensionless activities and properly normalized state conventions are required before taking logarithms. All heat-capacity and carrier-density inputs must carry the declared temperature, phase and units.

## Reconstruction and derivation

Substitute t=T/1000 so dT=1000 dt. Integrating each polynomial term gives 1000[A Delta t+(B/2) Delta(t²)+(C/3) Delta(t³)+(D/4) Delta(t⁴)-E Delta(1/t)] joules per mole. Entropy requires the integral of Cp/T, resulting in A ln(t2/t1)+B Delta t+(C/2) Delta(t²)+(D/3) Delta(t³)-(E/2) Delta(1/t²). The reference model rejects temperatures outside the declared fit range. Matching analytic and independent quadrature is software evidence, not a test of a specific source dataset.

## Original worked investigation

Take an authored constant Cp of 40 J/mol/K from 300 to 500 K. Predict DeltaH=8,000 J/mol and DeltaS=40 ln(500/300) J/mol/K. Then set B to a nonzero coefficient and check both integrals against a fine numerical quadrature. Never label those invented coefficients as NIST measurements.

**Evidence requirement:** reproduce this arithmetic by hand or with independently written code; do not assert a laboratory result from an authored fixture.

## Failure boundaries and uncertainty

The model assumes no phase transition over the interval, valid original coefficients, and a stable reference state. A closed-form numerical result cannot establish the chemical identity or purity of a real material.

An incomplete dataset, untested thermodynamic fit or missing device safety requirement must remain explicitly unknown. No hazardous synthesis, energized apparatus or chemical processing steps are specified by this reference.

## Published source navigation (link only)

- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/)
- [NIST Chemistry WebBook — database thermochemistry user guide](https://webbook.nist.gov/chemistry/guide/)

These URLs are citations, not local authenticated copies of the publisher's full document. Check edition, license, original-byte hash and applicability before empirical use.
