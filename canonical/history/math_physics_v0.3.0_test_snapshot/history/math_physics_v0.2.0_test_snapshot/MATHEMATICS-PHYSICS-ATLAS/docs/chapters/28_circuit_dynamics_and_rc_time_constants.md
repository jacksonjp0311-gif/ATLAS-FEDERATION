# Chapter 28: Circuit dynamics and RC time constants

**Discipline:** Electromagnetism. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Lumped electrical circuits provide a model between field theory and computing hardware. Resistance and capacitance describe certain linear approximations, while transients require a differential equation. Charge conservation and Ohm’s law give an exponential relaxation for an ideal RC branch. Real components have tolerances, parasitic elements, breakdown and temperature dependence.

## Equation, symbols and domain

`V(t)=V0 e^(−t/RC), τ=RC for ideal capacitor discharge.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For R=1000ohm and C=0.001F, time constant is one second. From 10V at t=1s, the ideal voltage is 10/e volts.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

The equation is not a circuit construction guide or a safe discharge procedure. A correct RC trajectory does not establish isolation, grounding or electrical approval.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 8.02SC Electricity and Magnetism, Fall 2010:** https://ocw.mit.edu/courses/8-02sc-physics-ii-electricity-and-magnetism-fall-2010/ — scope: Electrostatics, electricity, circuits, magnetic fields, Maxwell wave principles
- **OpenStax University Physics Volume 1, 2016:** https://openstax.org/books/university-physics-volume-1/pages/1-introduction — scope: Classical mechanics, units, conservation laws, energy and relativity introductions
