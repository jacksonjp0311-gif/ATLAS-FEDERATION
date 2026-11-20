# 1. Energy, work, power, and SI dimensions

**Area:** Foundations. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Energy is a conserved physical quantity that can change form; power is its rate of transfer. Distinguishing these concepts is essential for preserving correct engineering knowledge. A 1 kW device operating for one hour transfers 1 kWh, or exactly 3.6 MJ, but it is not producing 1 kWh at every instant. Work from a force requires displacement in the force direction. A joule is a newton metre, a watt is a joule per second, and electric quantities introduce volts, amperes and ohms. A useful report states the measurement boundary, sign convention, interval, uncertainties and whether values are rated, sampled, inferred or calibrated. Primary units must not be silently mixed with engineering units. Energy per unit mass, area, cycle and delivered service are distinct performance measures.

## Fundamental relationship, symbols and SI dimensions

`P=dE/dt; E=∫P dt; 1 Wh=3600 J; 1 kWh=3.6×10^6 J; 1 W=1 kg·m²/s³.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Dimensional analysis checks equations before computation: power times time has dimensions energy, whereas power divided by time does not. For a time-varying load, multiply average power by the interval only when the average is explicitly measured or defined. Integrating sample values needs an interpolation assumption, not just endpoints. The SI brochure gives the authoritative unit definitions, while sampled energy remains subject to instrument accuracy. A source record can preserve exact unit definitions even when no original laboratory measurements are available.

## Reconstruct the example without external AI

A 600 W heater runs continuously for 30 minutes. Compute 300 Wh = 0.3 kWh = 1.08 MJ by hand and with unit_convert. Repeat for a 600 W peak device whose output varies; explain why its true energy can be lower than the rated calculation.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Watts and watt-hours are not interchangeable. Demand charges, power capacity and stored energy answer different questions. An energy value without units and a reference interval is not a physically usable measurement.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions
- [NIST CODATA 2022 recommended fundamental physical constants](https://physics.nist.gov/cuu/Constants/) — inspected: 2022 recommendation, speed of light, elementary charge, Boltzmann and Stefan-Boltzmann constants

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
