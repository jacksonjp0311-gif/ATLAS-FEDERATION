# Energy Atlas v0.1.0 — author-constructed worked investigations

All 25 examples are ORIGINAL specified models, not measurements from real plants. Each has an explicit limitation.

## Investigation 01: kwh-to-joules

**Output:** `{"J": 3600000.0}`

**Applicability/limitation:** Unit conversion, not measurement

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 02: first-law-closure

**Output:** `{"input_j": 1000.0, "output_j": 850.0, "stored_delta_j": 150.0, "residual_j": 0.0, "relative_residual": 0.0, "model": "closed accounted boundary; any unreported loss appears in residual", "empirical_measurement_performed": false}`

**Applicability/limitation:** Boundary assumed complete

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 03: missing-loss-diagnostic

**Output:** `{"input_j": 1000.0, "output_j": 700.0, "stored_delta_j": 200.0, "residual_j": 100.0, "relative_residual": 0.1, "model": "closed accounted boundary; any unreported loss appears in residual", "empirical_measurement_performed": false}`

**Applicability/limitation:** Residual is not automatically identified as a specific physical loss

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 04: ordinary-conversion-efficiency

**Output:** `{"efficiency": 0.7, "loss_j": 300.0, "note": "input and useful output must have the same accounting boundary"}`

**Applicability/limitation:** Not heat pump COP

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 05: carnot-reversible-ideal

**Output:** `{"max_thermal_efficiency": 0.4, "ideal_cooling_cop": 1.5, "ideal_heating_cop": 2.5, "note": "reversible bounds, not achieved device efficiency or electricity generation promise"}`

**Applicability/limitation:** Upper bound in ideal reversible cycle

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 06: isothermal-ideal-gas-work

**Output:** `{"work_by_gas_j": 1728.9438964931937, "assumptions": "reversible isothermal ideal gas; constant temperature; signed work by gas"}`

**Applicability/limitation:** Ideal gas, reversible path

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 07: fourier-conduction-rate

**Output:** `{"W": 200.0}`

**Applicability/limitation:** 1D steady conduction constant k

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 08: stefan-boltzmann-net

**Output:** `{"W": 992.315523325}`

**Applicability/limitation:** Blackbody view factor one

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 09: lumped-thermal-decay

**Output:** `{"temperature_K": 322.46644820586107, "time_constant_s": 125.0, "assumptions": "uniform internal temperature, constant properties and convection, no internal heat source"}`

**Applicability/limitation:** Biot number limitation not checked

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 10: ohms-law

**Output:** `{"voltage_V": 12.0, "current_A": 2.0, "resistance_ohm": 6.0, "power_W": 24.0, "note": "power positive under passive sign convention; negative current/voltage can represent reversed reference"}`

**Applicability/limitation:** Resistor assumed ohmic

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 11: rc-discharge

**Output:** `{"voltage_V": 3.6787944117144233, "energy_J": 6.766764161830635, "tau_s": 1.0, "assumptions": "linear passive lumped RC, capacitor initially at V0, no load or leakage beyond R"}`

**Applicability/limitation:** Lumped ideal RC

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 12: ac-pf-and-reactive-power

**Output:** `{"apparent_VA": 2300.0, "real_W": 1840.0, "reactive_var": 1379.9999999999998, "assumptions": "single sinusoidal steady-state, RMS, one phase, chosen reactive sign; harmonics omitted"}`

**Applicability/limitation:** Sinusoidal one-phase only

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 13: three-phase-balanced

**Output:** `{"real_W": 6928.203230275509, "apparent_VA": 6928.203230275509, "assumptions": "balanced sinusoidal 3 phase"}`

**Applicability/limitation:** Balanced sinusoidal system

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 14: ideal-transformer

**Output:** `{"V_secondary": 240.0, "I_primary": 6.0, "assumptions": "ideal lossless transformer, voltage and current magnitudes, sinusoidal steady-state; not physical electrical safety design"}`

**Applicability/limitation:** Ignores saturation, faults, insulation and losses

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 15: i2r-line-loss

**Output:** `{"W": 40.0}`

**Applicability/limitation:** Known conductor resistance and RMS current

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 16: pv-cell-temperature-effect

**Output:** `{"dc_power_W": 920.0, "scope": "linear rated DC nameplate approximation; excludes inverter, shading, spectrum, degradation, soiling and clipping"}`

**Applicability/limitation:** Linear DC module reference, not plant generation

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 17: wind-betz-bound

**Output:** `{"incident_wind_W": 6000.0, "ideal_extracted_W": 2400.0, "ideal_betz_W": 3555.555555555555, "scope": "steady actuator disk, Betz constraint, no cut-in/rated/cut-out or generator electrical losses"}`

**Applicability/limitation:** Ideal steady actuator disk, excludes generator conversion

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 18: hydraulic-gravitational-power

**Output:** `{"W": 78453.2}`

**Applicability/limitation:** Illustrative flow/head, not surveyed site

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 19: battery-charge-conservation

**Output:** `{"stored_kWh": 6.8, "soc": 0.6799999999999999, "loss_kWh": 0.19999999999999996, "assumptions": "constant capacity, one-way efficiencies, ideal power constraints, no degradation or safety control"}`

**Applicability/limitation:** Nominal capacity unchanged, no degradation

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 20: battery-delivered-vs-stored

**Output:** `{"stored_kWh": 2.5, "soc": 0.25, "loss_kWh": 0.5, "assumptions": "constant capacity, one-way efficiencies, ideal power constraints, no degradation or safety control"}`

**Applicability/limitation:** Does not model BMS or temperature

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 21: reject-unaccounted-battery-energy

**Output:** `{"rejected": true}`

**Applicability/limitation:** No silent clipping of requested discharge

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 22: capacity-factor-finite-interval

**Output:** `{"factor": 0.5}`

**Applicability/limitation:** Not a generator efficiency

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 23: illustrative-discounted-lcoe

**Output:** `{"currency_per_kWh": 0.2295045749654567, "cost_npv": 1772.173492918481, "energy_pv_kWh": 7721.734929184811, "limitations": "no assumed externalities, curtailment, taxation, salvage, fuel inflation or social discount; input assumptions dominate estimate"}`

**Applicability/limitation:** Synthetic costs, energy output and discount

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 24: mass-energy-equivalence

**Output:** `{"J": 89875517.87368177}`

**Applicability/limitation:** Not a reactor design, yield prediction or nuclear safety model

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.

## Investigation 25: sampled-energy-trapezoid

**Output:** `{"joules": 250.0, "scope": "trapezoidal interpolation between samples, NOT exact continuous physical energy if samples are sparse"}`

**Applicability/limitation:** Depends on interpolation and real sample rate

**Verification:** Recompute the case by hand and compare with `python -m energy_atlas`; no claim about measured field performance.
