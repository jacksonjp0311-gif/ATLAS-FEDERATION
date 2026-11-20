# Chapter 23 — Diffusion, transport, and dimensional time scales

**Domain:** Materials and phases  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Diffusion moves particles due to statistical motion and chemical-potential gradients. An approximate continuum model uses a diffusivity D with units m²/s; both magnitude and temperature dependence vary drastically with species, phase and structure. Diffusion matters to batteries, semiconductor junctions, contamination control, polymers and corrosion. The familiar root-mean-square displacement scaling with sqrt(time) is a mathematical result for ideal independent Brownian motion, not a calibrated physical process schedule. Real diffusion can be anisotropic, concentration-dependent or dominated by grain boundaries.

## Mathematical or physical principle

`One-dimensional RMS displacement ℓ_rms=√(2Dt); for d independent dimensions ℓ_rms=√(2dDt).`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

The mean-square displacement follows from adding independent random increments with zero mean and finite variance in a homogeneous medium. The square-root time law is slower than linear travel, so doubling diffusion length requires approximately four times the time under the same D. Real semiconductor dopant redistribution adds interface and reaction conditions. A diffusion coefficient measured at one temperature cannot be used at another without a validated relation.

## Reconstruct an illustrative result offline

Set D=10^-12 m²/s and t=100 s in one dimension, obtaining ℓ≈sqrt(2×10^-10) m. Multiply time by four and verify the length doubles. Explain why this does not tell someone how to operate a dopant furnace.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No temperature-cycle, doping recipe or hazardous vapor handling is supplied. Transport boundaries, defects and measured D uncertainty remain open.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/) — inspected: Intrinsic/extrinsic carrier concepts, donor acceptor and band structure; not a fabrication tutorial
- [NIST Chemical Kinetics Database, SRD 17](https://kinetics.nist.gov/kinetics/) — inspected: Data Version 2026, gas-phase reaction kinetics indexing and research references

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
