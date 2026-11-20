# Chapter 05: Derivatives, sensitivities and automatic differentiation

**Discipline:** Calculus. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Derivatives quantify local sensitivity and power optimization, gradient-based learning and control. Polynomial differentiation follows from the binomial expansion and the limit definition. Finite differences approximate slopes without symbolic derivatives but suffer truncation and roundoff errors. Automatic differentiation applies the chain rule through a computational graph and is distinct from symbolic simplification or finite differencing.

## Equation, symbols and domain

`f′(x)=lim_(h→0)[f(x+h)-f(x)]/h.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For f(x)=x², derive f′(x)=2x and compare a centered finite difference with step h at x=2. Explain why making h arbitrarily tiny in floating point eventually becomes unreliable.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A derivative can fail to exist at a kink; noisy sampled sensor data may not have a meaningful instantaneous derivative. Local gradients do not determine global optimum.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability
- **MIT OpenCourseWare 18.01SC Single Variable Calculus, Fall 2010:** https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/ — scope: One-variable differentiation, integration, limits and fundamental theorem learning topics
