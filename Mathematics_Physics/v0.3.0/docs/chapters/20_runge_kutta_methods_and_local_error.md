# Chapter 20: Runge–Kutta methods and local error

**Discipline:** Numerical computation. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Runge–Kutta schemes approximate solutions by evaluating rates at multiple intermediate points. For sufficiently smooth problems, classical RK4 has fourth-order global accuracy as the step shrinks under suitable conditions. Stiff systems can behave poorly with explicit schemes despite small local residuals, so solver selection matters as much as step size. Numerical convergence should be tested against analytic cases and independent implementations.

## Equation, symbols and domain

`RK4: y_(n+1)=y_n+h(k1+2k2+2k3+k4)/6.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Use y′=−0.5y with y(0)=1 and t=1. Compare RK4 using 10, 20 and 40 steps with the analytic e^(−0.5) result and examine convergence.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

No fixed step count provides a universal guarantee for an unknown differential equation. Hidden discontinuities, stiffness and unbounded forcing can invalidate a simple error estimate.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
