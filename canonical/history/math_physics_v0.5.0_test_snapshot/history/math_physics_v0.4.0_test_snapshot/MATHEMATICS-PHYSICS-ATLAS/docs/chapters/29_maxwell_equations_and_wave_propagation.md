# Chapter 29: Maxwell equations and wave propagation

**Discipline:** Electromagnetism. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Maxwell’s equations unify electric and magnetic fields and describe waves under classical assumptions. Differential relations express source densities and local changes; integral forms relate field flux and circulation to charge and current. Applying boundary and material conditions is necessary before predicting propagation. The speed of electromagnetic waves in vacuum connects electromagnetic constants and the exact SI speed of light definition.

## Equation, symbols and domain

`∇·E=ρ/ε0, ∇·B=0, ∇×E=−∂B/∂t, ∇×B=μ0J+μ0ε0∂E/∂t.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

In charge-free vacuum, combine curl equations to motivate a wave equation with propagation speed c=1/sqrt(μ0ε0). Explain why vacuum ε0 and μ0 derived from adjusted constants are no longer separately exact.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Actual antennas, waveguides, dielectric losses and quantum material responses need additional constitutive models and measurements. No RF transmitter construction or exposure assessment is provided.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 8.02SC Electricity and Magnetism, Fall 2010:** https://ocw.mit.edu/courses/8-02sc-physics-ii-electricity-and-magnetism-fall-2010/ — scope: Electrostatics, electricity, circuits, magnetic fields, Maxwell wave principles
- **NIST CODATA Recommended Fundamental Constants, 2022 adjustment:** https://physics.nist.gov/cuu/Constants/ — scope: NIST versioned fundamental physical constants; distinguish exact SI defining constants from adjusted measurements
