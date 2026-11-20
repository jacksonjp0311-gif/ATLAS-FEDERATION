# 47. Optical spectroscopy, calibration and uncertainty

**Field:** Measurement · **Version:** v0.2.0 · **Scientific status:** original educational reference; cited publisher portions inspected, original publisher bytes not archived. No real experiment.

## Principles and physical scope

Optical spectroscopy can probe composition and electronic transitions, but measured light intensity does not uniquely determine chemical identity without wavelength selection, background correction, calibration and a justified optical model. The Beer–Lambert relation is a common teaching model for absorbance in a homogeneous, non-scattering solution under monochromatic light. Its coefficients depend on species and measurement conditions. Real devices may encounter stray light, scattering, detector nonlinearity, mixed absorbing species, temperature dependence and unknown path lengths. A successful numerical calculation using an invented molar absorption coefficient cannot certify a real sensor or identify a hazardous analyte.

## Equation and definitions

`A=log10(I0/I)=εlc; ideal transmittance T=10^(−A), with ε in L mol−1 cm−1, l in cm, c in mol/L.`

Inputs and reference states must be declared. The algebra alone cannot establish source data validity, experimental behavior or physical safety.

## Derivation and why the relationship holds

Absorbance is a logarithmic ratio of incident and transmitted intensities, so it is dimensionless. Under independent absorbing events and homogeneous conditions, the effective attenuation scales linearly with optical path length and concentration. This simple model breaks down in strongly scattering media or when multiple components contribute overlapping absorption spectra. The source register should contain wavelength, optics, detector configuration, calibration file, blank measurements and uncertainty. Values without those conditions are not enough for inverse concentration estimation.

## Reconstruct without external AI

Use a fictional species with ε=100 L mol−1 cm−1, optical path 1 cm and concentration .002 mol/L. Compute A=.2 and ideal transmittance ≈0.631. Show that doubling path length doubles A while transmittance squares; this is only a model demonstration, not actual spectroscopy.

These examples are invented, not laboratory readings. Reproduce them by hand and compare only within the declared model domain.

## Failure case and missing evidence

At extreme absorbance a real detector can hit its dynamic-range floor; a mathematical 10^(−A) may underflow. The reference returns unavailable for impractically large exponent rather than reporting false infinite precision. No analytical validation was conducted.

## Source provenance and rights

- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights
- [NIST Guide to Expression of Uncertainty in Measurement](https://www.nist.gov/publications/guide-expression-uncertainty-measurement) — Uncertainty and calibration scope for reconstructed measurements

**Not retained:** original publisher documents, real chemical samples, source tables and independent domain review.
