# Chapter 14: Random variables, expectation and variance

**Discipline:** Probability. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Expectation summarizes a distribution’s mean while variance measures spread around that mean. Neither is a substitute for bounds on rare events. Independence is a property of joint distributions and cannot be inferred from separate measurements. Reliable AI evaluation preserves the true sampling scheme, correlated sources and the difference between observed data and simulated samples.

## Equation, symbols and domain

`E[X]=Σ_x x p(x); Var(X)=E[(X−E[X])²].`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For a fair binary variable with values zero and one, compute expectation 0.5 and variance 0.25. Change the probability of one to 0.9 and recompute.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A mean alone cannot predict safety, tail behavior or worst-case cost. Heavy-tailed distributions may lack finite variance, making some standard formulas invalid.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
