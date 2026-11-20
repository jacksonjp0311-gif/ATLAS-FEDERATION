# Chapter 06: Integration and conservation over time

**Discipline:** Calculus. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Integration accumulates a varying rate into a total. It connects physical power to energy, velocity to displacement, probability density to probability and differential equations to trajectories. The fundamental theorem of calculus connects an accumulated integral with a derivative when appropriate regularity holds. Numerical quadrature approximates integrals when antiderivatives are unavailable.

## Equation, symbols and domain

`∫_a^b f(x)dx = F(b)-F(a) when F′=f.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Integrate f(t)=t² over [0,3] by its antiderivative t³/3 to obtain nine. Reconstruct the same result with Simpson quadrature for an even partition.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Finite sampling and interpolation introduce numerical error; discontinuities and singularities demand extra care. Integrating an invented power profile does not establish measured energy.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
- **MIT OpenCourseWare 18.01SC Single Variable Calculus, Fall 2010:** https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/ — scope: One-variable differentiation, integration, limits and fundamental theorem learning topics
