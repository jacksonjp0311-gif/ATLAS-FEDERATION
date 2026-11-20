# Chapter 21: Partial differential equations and boundary conditions

**Discipline:** Differential equations. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Partial differential equations model spatially distributed physical quantities. The same equation can describe different systems depending on boundary and initial conditions. Conservation-law derivations often yield flux-divergence forms, while constitutive relations determine material parameters. Finite differences must respect stability, boundary flux and domain geometry to avoid producing physically false results.

## Equation, symbols and domain

`∂u/∂t=D∂²u/∂x² for one-dimensional constant-D diffusion.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Discretize a three-cell diffusion profile with no-flux boundaries, and verify the sum stays constant for a stable explicit timestep under the declared coefficient.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A stable numerical solution may still use a wrong diffusion coefficient or ignore convection, reactions or electric fields. No semiconductor process recipe follows from this model.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability
- **MIT OpenCourseWare 8.02SC Electricity and Magnetism, Fall 2010:** https://ocw.mit.edu/courses/8-02sc-physics-ii-electricity-and-magnetism-fall-2010/ — scope: Electrostatics, electricity, circuits, magnetic fields, Maxwell wave principles
