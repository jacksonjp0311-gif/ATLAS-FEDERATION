# Chapter 11: Least squares and identifiable parameter fitting

**Discipline:** Linear algebra. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Noisy observations often cannot satisfy a proposed linear model exactly. Least squares chooses parameters that minimize squared residuals under a declared metric. Differentiating the quadratic objective yields normal equations, but solving them can amplify conditioning problems. Physical parameter identification also needs independent calibration, representative data and a justified error model.

## Equation, symbols and domain

`min_x ||Ax-b||²; for full-rank A, AᵀAx=Aᵀb.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Fit a straight line to (0,1),(1,3),(2,5). The model y=1+2x yields zero residual. With a perturbed point, compute the new residual and distinguish fit quality from evidence of a mechanism.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Normal equations square the condition number; professional fitting often uses QR or SVD. A low error may reflect leakage or insufficiently diverse data, not correct physics.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions
