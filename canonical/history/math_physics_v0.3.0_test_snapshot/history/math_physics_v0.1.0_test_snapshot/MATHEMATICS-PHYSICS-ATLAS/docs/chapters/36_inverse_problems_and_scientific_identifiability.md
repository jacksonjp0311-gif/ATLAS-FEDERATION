# Chapter 36: Inverse problems and scientific identifiability

**Discipline:** Numerical computation. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

An inverse problem infers hidden causes or parameters from observations. Even exact observations may be insufficient when multiple parameter sets produce identical outputs. Rank and nullspace analysis make the problem visible in linear settings. Regularization supplies additional assumptions and can improve numerical behavior, but it does not magically create measurement evidence. This issue appears in tomography, model training and system diagnostics.

## Equation, symbols and domain

`Given y=F(θ), uniqueness of θ requires injectivity over the admissible model domain.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Observe y=x1+x2=5. Both (2,3) and (1,4) fit exactly; a second independent observation is necessary to identify both unknowns without a prior.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A unique numerical minimum may be induced by regularization rather than by data. Report prior assumptions and identifiable observables separately.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions
