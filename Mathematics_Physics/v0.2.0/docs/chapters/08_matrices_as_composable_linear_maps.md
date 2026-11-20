# Chapter 08: Matrices as composable linear maps

**Discipline:** Linear algebra. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Matrices represent linear maps between finite-dimensional vector spaces. Matrix multiplication composes maps; transpose changes coordinate relationships under a chosen real inner product. Associativity makes chains of transformations possible but matrix multiplication is not generally commutative. AI workloads rely extensively on matrix products, making the derivation and data layout important for rebuilding model execution.

## Equation, symbols and domain

`(AB)_(ij)=Σ_k A_(ik)B_(kj); (AB)v=A(Bv).`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Multiply a 1×2 row [1,2] by a 2×1 column [3,4] to obtain 11. Reverse the order and observe that the result is a 2×2 matrix, not the same scalar.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Dimensions must be checked before multiplication; numeric precision and memory layout matter for large computation. Matrix multiplication alone cannot infer scientific causation.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
