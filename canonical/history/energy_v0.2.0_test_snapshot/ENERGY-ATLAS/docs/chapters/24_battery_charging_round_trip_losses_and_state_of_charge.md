# 24. Battery charging, round-trip losses, and state of charge

**Area:** Storage. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

A useful elementary battery model tracks stored energy in kWh, charge input and delivered discharge power. With fixed one-way efficiencies, stored energy increases by η_charge P_charge Δt and decreases by P_discharge Δt/η_discharge. The difference appears as loss and heat under a chosen accounting boundary. A round trip through the battery returns less electrical energy than supplied unless idealized efficiencies equal one. This says nothing about Coulombic efficiency, calendar aging, nonlinear voltage, cell mismatch or safe charge acceptance. A physically accountable model rejects a step that exceeds capacity rather than silently clipping storage and hiding the excess energy.

## Fundamental relationship, symbols and SI dimensions

`E_next=E_current+η_ch P_ch Δt−P_dis Δt/η_dis; η_roundtrip≈η_chη_dis (matched boundaries).`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The relation follows from ordinary energy accounting: input electrical energy times charge efficiency becomes stored chemical energy, while delivered electrical energy requires a larger internal energy decrease. Defining the reference endpoints matters: including inverter and transformer losses changes efficiency. In a multi-hour dispatch the battery's power rating, state-dependent performance and reserve constraints must be modeled in addition to energy capacity.

## Reconstruct the example without external AI

Start with 5 kWh in a 10 kWh idealized battery. Charge at 2 kW for one hour with η_ch=.9, obtaining 6.8 kWh. Then discharge a specified amount and compute how much internally stored energy must be consumed at η_dis=.8.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A step that requests more than available energy is invalid. Automatically changing output without explicitly recording curtailed discharge invents a delivered service that was never supplied.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements
- [DOE Energy Storage Grand Challenge Roadmap](https://www.energy.gov/energy-storage-grand-challenge/articles/energy-storage-grand-challenge-roadmap) — inspected: Energy storage use cases and technology constraints

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
