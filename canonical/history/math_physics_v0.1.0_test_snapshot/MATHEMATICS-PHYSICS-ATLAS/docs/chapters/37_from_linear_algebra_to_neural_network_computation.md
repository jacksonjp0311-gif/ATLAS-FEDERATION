# Chapter 37: From linear algebra to neural network computation

**Discipline:** AI foundations. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

A neural network can be understood as a composition of affine maps and nonlinear activation functions. Matrix operations provide the bulk computation, while derivatives propagate sensitivity during training. The mathematical representation is portable across CPU, GPU and other architectures if numerical formats and operator definitions are preserved. A successful calculation, however, does not show that the trained system understands science or generalizes to unseen data.

## Equation, symbols and domain

`Layer map y=σ(Wx+b); gradients follow the chain rule and matrix transposes.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Take a one-layer model with W=[[2,0]], b=[1], input x=[3,4] and identity activation, yielding output seven. Compute derivative of output with respect to x.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Loss functions, data, numerical precision and training dynamics require independent evaluation. This chapter neither trains a foundation model nor measures AI benchmark improvement.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
