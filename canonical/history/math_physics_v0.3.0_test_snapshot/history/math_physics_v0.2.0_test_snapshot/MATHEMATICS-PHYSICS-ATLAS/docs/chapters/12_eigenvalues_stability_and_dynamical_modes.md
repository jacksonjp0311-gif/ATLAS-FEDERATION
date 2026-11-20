# Chapter 12: Eigenvalues, stability and dynamical modes

**Discipline:** Linear algebra. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Eigenvalues describe how a linear transformation acts along special directions. In differential-equation systems they classify exponential growth, decay and oscillation under a linear model. In AI they appear in optimization curvature, covariance spectra, propagation stability and dimensionality reduction. A numerical eigenvalue requires a model and a source of coefficients; one large eigenvalue does not automatically mean a system is unstable under every discretization.

## Equation, symbols and domain

`Av=λv; dynamical modes of x′=Ax depend on eigenvalues of A.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For diagonal A=diag(−1,−2), the dynamical system x′=Ax has two decaying modes. Replace one diagonal entry by +1 and explain which initial-state component grows.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Nonnormal matrices can amplify disturbances transiently even when eigenvalues indicate eventual decay. Nonlinear dynamics and uncertain coefficients need separate evaluation.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability
