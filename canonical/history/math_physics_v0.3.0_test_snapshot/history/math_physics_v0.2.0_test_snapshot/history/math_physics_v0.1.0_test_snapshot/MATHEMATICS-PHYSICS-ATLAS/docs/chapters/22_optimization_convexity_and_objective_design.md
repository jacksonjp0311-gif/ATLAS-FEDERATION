# Chapter 22: Optimization, convexity and objective design

**Discipline:** Optimization. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Optimization converts a declared objective and constraints into a mathematical search. Convexity provides useful global guarantees when assumptions hold; outside convex settings gradient descent can reach local minima or saddle points. In AI training, a low mathematical loss need not correspond to useful or safe behavior, so optimization targets must be validated independently. Numerical step-size choices affect convergence.

## Equation, symbols and domain

`For positive-definite Q: minimize 0.5 xᵀQx−bᵀx; gradient Qx−b.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For Q=diag(2,2), b=(2,4), the minimum occurs at x=(1,2). Verify a bounded gradient descent sequence approaches that solution.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A strongly convex quadratic example is not a proof about neural network training or real-world utility. Constraints, metric weights and source data determine the actual objective.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
