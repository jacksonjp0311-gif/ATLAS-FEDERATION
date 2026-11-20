# Chapter 35: Covariance and propagated measurement uncertainty

**Discipline:** Metrology. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Measurement results require uncertainty as well as a numerical estimate. When inputs are correlated, a propagation formula that ignores covariance can be misleading. This matters for scientific knowledge that must survive multiple instrument generations and software implementations. The uncertainty budget should retain calibration, resolution, physical model and statistical sampling information rather than a guessed final percentage.

## Equation, symbols and domain

`For z=ab, u_z²≈b²u_a²+a²u_b²+2abCov(a,b).`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Let a=2±0.1, b=3±0.2 with zero covariance. Then z=6 and propagated standard uncertainty is sqrt(0.09+0.16)=0.5. Repeat with known positive covariance.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

This is a first-order local approximation. Large nonlinear uncertainty, dependence on unknown common sources and non-Gaussian distributions require more advanced methods.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions
- **BIPM, SI Brochure Ninth Edition, revised June 2026:** https://www.bipm.org/en/si-brochure-9 — scope: Official SI defining constants and unit descriptions, complete brochure revision 4.01 June 2026
