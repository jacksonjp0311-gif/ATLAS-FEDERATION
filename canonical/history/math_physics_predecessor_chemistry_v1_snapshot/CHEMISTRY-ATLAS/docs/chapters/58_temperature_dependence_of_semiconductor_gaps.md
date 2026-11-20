# 58. Temperature dependence of semiconductor gaps

**Theme:** Solid-state chemistry · **Chemistry Atlas scoped research v1.0.0**

**Evidence level:** project-written mathematical/reference explanation with scope-limited official sources. Every worked numeric input is hypothetical; publisher originals are not in this archive.

## Scientific foundation

Many semiconductor energy gaps change with lattice temperature because of electron-phonon coupling and thermal expansion. An empirical Varshni relation is often used for measured temperature trends over restricted ranges. Its coefficients are material- and publication-specific; they must not be transferred from one material or alloy composition to another without verification. Thermal variation matters to optical devices, leakage current and electronic behavior, but an empirical fit is not a microscopic proof. An AI model that receives only a room-temperature band gap cannot safely claim temperature-independent operation.

## Governing relationship and dimensional conventions

`Eg(T)=Eg(0)-alpha*T²/(T+beta), with T in kelvin, Eg in eV, alpha in eV/K and beta in K.`

Dimensionless activities and properly normalized state conventions are required before taking logarithms. All heat-capacity and carrier-density inputs must carry the declared temperature, phase and units.

## Reconstruction and derivation

Differentiate the empirical function to obtain dEg/dT=-alpha*T*(T+2 beta)/(T+beta)^2. If alpha is positive, the function decreases for positive T within the fit range. Near 0 K it approaches the supplied Eg(0). The value of beta and applicable temperature interval must be recorded with the data source, crystallographic phase and composition. The reference model returns the derivative explicitly so the sensitivity can be checked against independent numerical differences.

## Original worked investigation

Use authored Eg(0)=1.17 eV, alpha=4.73e-4 eV/K, beta=636 K at 300 K. Calculate the predicted Eg(T), then compare its analytical derivative to a symmetric numerical difference. State that these numbers are examples and must be pinned to a primary material source for scientific characterization.

**Evidence requirement:** reproduce this arithmetic by hand or with independently written code; do not assert a laboratory result from an authored fixture.

## Failure boundaries and uncertainty

This is an empirical model with finite validity; a good algebraic fit does not establish alloy band gap, processing temperature, device leakage or safe operation. No real semiconductor sample measured.

An incomplete dataset, untested thermodynamic fit or missing device safety requirement must remain explicitly unknown. No hazardous synthesis, energized apparatus or chemical processing steps are specified by this reference.

## Published source navigation (link only)

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/)
- [Materials Project API and computed materials data schema](https://docs.materialsproject.org/downloading-data/using-the-api)

These URLs are citations, not local authenticated copies of the publisher's full document. Check edition, license, original-byte hash and applicability before empirical use.
