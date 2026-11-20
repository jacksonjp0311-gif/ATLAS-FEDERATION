# Chapter 28 — Spectroscopy, analytical fingerprints, and measurement uncertainty

**Domain:** Metrology  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Chemical identification uses methods such as infrared, Raman, ultraviolet-visible, mass spectrometry, nuclear magnetic resonance and diffraction. Each detects different physical properties and has characteristic confounders. A spectrum is not an unambiguous substance identity without calibration, measurement context, sample purity and reference library quality. Instrument response, baseline correction, noise and sampling can create peaks that are absent in the chemical sample. NIST maintains compiled spectra and thermochemistry, but a query result must preserve the cited version and data rights. A future scientific community needs measurement procedures and raw spectra as well as interpretive descriptions.

## Mathematical or physical principle

`Beer–Lambert A=log10(I0/I); for ideal solutions A≈εcl with ε units chosen consistently.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

The logarithmic absorbance follows from exponential attenuation under assumptions of homogeneous absorbing medium and negligible scattering. Multiplying molar absorptivity by concentration and path length gives dimensionless absorbance only when units are compatible. A calibration series can test whether the ideal relation holds over a specified range. Presence of a predicted peak is evidence conditioned on resolution and competing species; absence of a peak may reflect detection limits or instrumentation.

## Reconstruct an illustrative result offline

For an invented reference I0=100 units and transmitted intensity I=10 units, absorbance is 1. Increase I to 50 and calculate the smaller absorbance. State why these numbers do not identify a particular molecule without an experimentally collected spectrum.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

The chapter does not teach construction of hazardous radiation sources, chemical extraction or unsafe instrument operation. Original spectrum data, certified calibrations and independent interpretation are absent.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — inspected: Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights
- [NIST Guide to Expression of Uncertainty in Measurement](https://www.nist.gov/publications/guide-expression-uncertainty-measurement) — inspected: Uncertainty and calibration scope for reconstructed measurements

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
