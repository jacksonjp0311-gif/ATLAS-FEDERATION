# Chapter 15 — Diffusion as a mechanism-specific, temperature-dependent process

Diffusion coefficients are not universal constants for an element. A source record must identify diffusing species, host crystal phase, direction, specimen microstructure, concentration regime and temperature. Bulk self-diffusion, grain-boundary diffusion, surface diffusion and interdiffusion can be different processes with different activation energy and prefactors.

## Arrhenius model

For a supplied regime, `D(T) = D0 exp[-Q/(R T)]`, with D0 in m²/s, Q in J/mol, R in J/(mol·K) and T in K. Holding D0 and Q fixed, a higher T implies higher D for Q positive. Arrhenius behavior can fail across phase changes, trap saturation, changing defect mechanisms, mixed pathways or non-ideal concentration dependence. Do not extrapolate one high-temperature experimental segment to all service temperatures.

The `arrhenius_diffusivity` utility checks positive D0/T and nonnegative Q and returns D at a temperature for which **the caller must independently establish the parameter regime**. It neither fits parameters nor measures diffusion. For a stipulated one-dimensional homogeneous Gaussian random walk, the root-mean-square displacement is `sqrt(2 D t)`; this is a displacement scale, not an exact penetration front. Boundary conditions and chemical reaction can invalidate the simplifying model.

## Distinguish activation from proof of mechanism

An Arrhenius line fitted through only two temperature values does not uniquely identify the mechanism. If the intercept and slope are measured, repeatability, uncertainties in both axes, temperature calibration and sample state affect interpretation. An apparent activation energy may mix different kinetic paths. A diffusion-length result also does not tell whether interface bonding, corrosion or material failure occurred.

Our teaching calculation uses `D0=1e-5 m²/s`, `Q=100000 J/mol`, `T=850 K` as expressly synthetic parameters; no matching real alloy is asserted. A separate 3600-second demonstration with specified `D=1e-12 m²/s` returns a one-dimensional RMS displacement near 85 micrometers. The two examples are intentionally not combined into a material-specific claim.

## Evidence packet for a future real study

Require species/host/phase, concentration profile and method, temperature time series, specimen history, surface condition, grain size and orientation, calibration records, raw measurements, fit residuals, analysis code, confidence intervals, source locator and a warning for any model extrapolation. Link to Materials and Measurement records for shared uncertainty definitions.

**Source:** NIST materials data resources, which distinguishes experimental and computational diffusion repositories, `https://www.nist.gov/mgi/materials-data-resources`, and NIST reported kinetics study summaries describing Arrhenius behavior on their own narrow experimental ranges.
