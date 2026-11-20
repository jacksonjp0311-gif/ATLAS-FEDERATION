# 28. Distributed generation, storage dispatch, and unmet load

**Area:** Infrastructure. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

A small isolated electrical system must provide sufficient instantaneous power while respecting storage power and energy constraints. A dispatch model consumes timeseries of renewable generation and load, routes surplus into charging where available, and records curtailed generation or imported energy separately. During deficits it discharges storage within limits, then records unmet demand or required grid imports. A daily kWh balance alone cannot guarantee power adequacy at a specific time. Storage dispatch may require forecast uncertainty, reserve policies and reactive power support that a scalar energy model does not provide. A valid ledger must distinguish load actually served from demand requested and must not silently create energy by clipping battery state.

## Fundamental relationship, symbols and SI dimensions

`For each interval: generation + discharge + import = served_load + charge + export + curtailment + losses, with all terms sign-consistent.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The interval balance follows from conservation. A battery step adds state continuity between intervals. If maximum charge and discharge powers are not imposed, a model can make impossible spikes even with adequate total kWh. If reserve and grid-forming requirements are omitted, the result is only an idealized energy feasibility exercise. Matching all energy flows is necessary but insufficient for voltage and frequency stability.

## Reconstruct the example without external AI

Construct a two-hour toy load series 1 kW then 3 kW, with solar 3 kW then 0 and a 2 kWh battery. Allocate surplus and deficit, record charge/discharge losses, and identify any unmet load with no grid connection. Use separate source and storage states.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not claim a functioning or safe microgrid from an energy-only simulation. A grid needs protection, frequency regulation, grounding and synchronized power-electronic controls.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements
- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
