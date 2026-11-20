# Chapter 17: Numerical conditioning and stability

**Discipline:** Numerical computation. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Numerical conditioning concerns how small changes in inputs can affect a mathematically exact output; numerical stability concerns how the algorithm propagates its own rounding. These are separate ideas. A well-implemented solver cannot rescue a fundamentally ill-conditioned inverse problem without additional information. Source-level tests must include near-singular and out-of-domain cases, not only easy integer examples.

## Equation, symbols and domain

`κ(A)=||A||||A⁻¹|| when A is invertible; sensitivity scales with conditioning.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Consider a system whose two equations become almost identical. Tiny measurement noise may cause large parameter swings, even while the residual of a fitted solution appears small.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A small residual is not a guarantee of accurate parameters. Calculating an inverse explicitly is often less stable than solving via a factorization.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
