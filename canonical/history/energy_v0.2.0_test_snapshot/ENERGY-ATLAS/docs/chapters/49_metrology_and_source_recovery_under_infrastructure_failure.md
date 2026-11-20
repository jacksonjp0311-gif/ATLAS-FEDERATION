# 49. Metrology and source recovery under infrastructure failure

**Area:** Preservation · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

If energy science must survive the loss of internet access and specialized vendors, numerical results need more than a copied constant. Each measurable quantity requires a definition, unit, reference state, measuring instrument, calibration method, uncertainties, and original evidence where permitted. The NIST 2022 CODATA adjustment supplies recommended values as of its declared scientific edition; exact SI defining constants must be distinguished from experimentally adjusted constants with standard uncertainties. The current Atlas contains derived constants in its own JSON but does not retain the original NIST publication bytes. This remains a documented preservation deficit, not a reason to invent a primary-source file or label a table authenticated from memory.

## Equation, symbols and dimensional units

`A measured quantity is reported as x ± u with unit and coverage convention. Dimensionless residual of balance r=(Ein−Eout−ΔEstored)/scale is an internal closure check, not experimental validation.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

To reconstruct a claim, record the traceable source URL/DOI/edition, publisher attribution, explicit value, uncertainty and covariance where applicable, and measurement conditions. For a derived result, state how uncertainty propagates and whether inputs are correlated. A near-zero energy-balance residual on invented numbers shows only that the arithmetic conserves its own bookkeeping. An engineer should also investigate unmodeled energy paths, sensor bias, sampling rates, rounding and operating regimes. Software tests provide regression evidence but cannot certify a real sensor or generator.

## Hand reconstruction and independent calculation

Compare exact c = 299,792,458 m/s (defined SI) with a non-exact measurement such as Newtonian gravitational constant G, whose CODATA recommendation carries uncertainty. Create a record distinguishing exact definition from measured adjusted value; then locate the original source document or explicitly mark it unavailable. Do not invent the uncertainty value when the source is inaccessible.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

A DOI is a locator, not an archived original. Publisher PDFs and normative standards may have copyright/rights restrictions. A copied checksum without original authenticated bytes is not a fixity proof of those bytes.

## Life safety and operational boundary

Only rights-cleared original materials with verifiable source hashes can move into a higher evidence level; otherwise preserve original explanation and the missing-source gap.

## Source navigation and preservation debt

- **NIST CODATA Recommended Fundamental Physical Constants, 2022 adjustment, 2025 publication:** https://www.nist.gov/publications/codata-recommended-values-fundamental-physical-constants-2022 — Publication metadata for 2022 adjustment, distinction between exact SI constants and adjusted measured values; full PDF not downloaded
- **NIST Measurement Uncertainty Guidance:** https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty — Measurement uncertainty, measurand, instrument and calibration context
- **BIPM The International System of Units (SI) Brochure, ninth edition:** https://www.bipm.org/en/publications/si-brochure — Energy, power, voltage and electrical units, formal SI definitions

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.
