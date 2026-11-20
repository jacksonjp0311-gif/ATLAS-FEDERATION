# Chapter 03: Numbers, rational arithmetic and precision

**Discipline:** Computational foundations. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Integer and rational numbers support exact symbolic calculations; binary floating-point arithmetic represents a finite subset of real numbers. Scientific programs must decide when exactness matters, especially for conservation and discrete coefficients. Fractions prevent a balancing or linear-algebra proof from being undermined by roundoff. Numerical algorithms must separately track overflow, cancellation, conditioning and finite precision.

## Equation, symbols and domain

`p/q∈ℚ, q≠0; floating-point x̂=x(1+δ) under a bounded operation model.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Solve 3x=1 exactly as one third. A binary float approximates that value and cannot generally preserve equality 3x=1 as an exact rational identity.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Exact arithmetic may be computationally expensive; floating-point can be more appropriate for measured physical values with uncertainty. No representation turns a measured input into an exact constant.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
