# Chapter 15: Bayesian updating versus evidence reliability

**Discipline:** Probability. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Bayesian inference offers a consistent way to combine beliefs and likelihood under a model. Evidence likelihood must be defined with respect to competing hypotheses, not assigned because a result appears plausible. Reusing dependent observations as independent evidence can double count information, producing unwarranted confidence. This is relevant for multi-agent reasoning where several reports may share the same original source.

## Equation, symbols and domain

`Posterior odds = prior odds × likelihood ratio.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

A test with sensitivity 0.9 and false-positive rate 0.1 produces likelihood ratio nine for a positive result. Start with prior odds 1:1 and recover posterior 9:1, then document that these parameters were stipulated.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Incorrect prior odds, test calibration, dependence or selection bias can dominate conclusions. Posterior numerical precision does not establish causation.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions
- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
