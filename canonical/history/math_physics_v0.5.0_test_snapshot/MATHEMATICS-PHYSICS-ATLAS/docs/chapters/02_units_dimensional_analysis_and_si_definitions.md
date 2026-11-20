# Chapter 02: Units, dimensional analysis, and SI definitions

**Discipline:** Metrology. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Units encode the type of physical quantity. SI defining constants provide a repeatable common basis for measuring length, time, mass, electrical charge, temperature and amount of substance. Dimensional homogeneity is necessary for a physical relation, but it is not sufficient to prove one: two incorrect formulas may have identical units. Distinguish exact defining constants from experimental constants such as the gravitational constant.

## Equation, symbols and domain

`[force]=kg·m·s^-2; [energy]=kg·m²·s^-2; [power]=kg·m²·s^-3.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Derive that a force of one newton acting through one meter of displacement transfers one joule in the aligned ideal case, then divide by one second to obtain one watt.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A dimensionally correct model can still omit losses or wrong physical mechanisms. Instrument calibration and provenance remain independent evidence requirements.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **BIPM, SI Brochure Ninth Edition, revised June 2026:** https://www.bipm.org/en/si-brochure-9 — scope: Official SI defining constants and unit descriptions, complete brochure revision 4.01 June 2026
- **NIST CODATA Recommended Fundamental Constants, 2022 adjustment:** https://physics.nist.gov/cuu/Constants/ — scope: NIST versioned fundamental physical constants; distinguish exact SI defining constants from adjusted measurements
