# Energy v0.2.0 — Survival Services Casebook (11 original constructed cases)

No real experiment, water quality measurement, electrical operation, or life-critical application is represented.

## Case 1: gravity-water-lifting

**Scope:** Not potable-water validation, pump sizing or wiring

**Output:**

```json
{
  "schema": "atlas.energy-water-lift/1",
  "volume_m3": 1.0,
  "total_dynamic_head_m": 10.0,
  "ideal_hydraulic_energy_j": 98066.5,
  "required_input_energy_j": 196133.0,
  "required_input_Wh": 54.48138888888889,
  "conversion_loss_j": 98066.5,
  "model_scope": "prescribed volume/head with constant overall efficiency; no pipe-curve or dynamic operating point",
  "water_quality_certified": false,
  "pump_installation_safe": false,
  "limitations": [
    "Static/dynamic head must come from a real hydraulic survey; this formula does not select a pump",
    "Friction, transients, motor start, water chemistry, filters, storage and electrical protection are not independently modeled"
  ]
}
```

## Case 2: water-sensible-heat

**Scope:** Not water disinfection or safe cooking

**Output:**

```json
{
  "schema": "atlas.energy-sensible-heat/1",
  "useful_heat_j": 376560.0,
  "input_heat_j": 470700.0,
  "input_kWh": 0.13075,
  "limitations": [
    "Neglects evaporation, phase change, vessel heat capacity, convection and temperature-dependent cp",
    "Heating energy is NOT verification that contaminated water is potable or a food process is safe"
  ],
  "water_potability_verified": false,
  "safe_equipment_instructions": false
}
```

## Case 3: shelter-degree-hours

**Scope:** UA and degree-hours are authored values; not real building audit

**Output:**

```json
{
  "schema": "atlas.energy-shelter-heat-loss/1",
  "heat_loss_kWh": 18.0,
  "assumptions": "constant envelope UA and specified positive temperature degree-hours",
  "limitations": [
    "Infiltration, weather, solar gains, indoor moisture, thermal inertia and human health limits not resolved",
    "Not heating equipment design, ventilation prescription or combustion safety analysis"
  ]
}
```

## Case 4: generator-energy-account

**Scope:** No combustion, generator connection or indoor fuel use authorized

**Output:**

```json
{
  "schema": "atlas.energy-fuel-conversion/1",
  "chemical_input_kWh": 48.61111111111111,
  "electricity_at_assumed_efficiency_kWh": 12.152777777777777,
  "conversion_loss_kWh": 36.45833333333333,
  "fuel_specification_origin": "caller_supplied_not_verified",
  "limitations": [
    "Heating value and performance require measured fuel grade, environment and device-specific testing",
    "NO instructions for connecting generators, fuel storage, combustion, exhaust systems, ventilation or grid backfeed",
    "Carbon monoxide/fire risk requires official emergency guidance and properly qualified equipment"
  ]
}
```

## Case 5: priority-power-budget

**Scope:** Mathematical proportional sharing is not a safety/critical-load control plan

**Output:**

```json
{
  "schema": "atlas.energy-priority-load/1",
  "available_power_kW": 1.0,
  "served_kW": 1.0,
  "unserved_kW": 1.5,
  "unused_power_kW": 0.0,
  "services": {
    "heating": {
      "priority": 2,
      "requested_kW": 1.8,
      "served_kW": 0.45,
      "unserved_kW": 1.35,
      "minimum_requested_kW": 1.0,
      "minimum_satisfied": false
    },
    "lights": {
      "priority": 2,
      "requested_kW": 0.2,
      "served_kW": 0.05,
      "unserved_kW": 0.15000000000000002,
      "minimum_requested_kW": 0.1,
      "minimum_satisfied": false
    },
    "water": {
      "priority": 1,
      "requested_kW": 0.5,
      "served_kW": 0.5,
      "unserved_kW": 0.0,
      "minimum_requested_kW": 0.5,
      "minimum_satisfied": true
    }
  },
  "all_declared_minima_met": false,
  "not_a_real_safety_dispatch": true,
  "limitations": [
    "Priority policy is a hypothetical mathematical convention, not a professional triage policy",
    "Critical equipment may fail under partial power; duty cycle, startup current, voltage/frequency and minimum-on time missing",
    "Medical life support cannot be certified from kilowatt arithmetic"
  ]
}
```

## Case 6: battery-reserve-sensitivity

**Scope:** No field autonomy guarantee, standby losses or BMS constraints

**Output:**

```json
{
  "schema": "atlas.energy-reserve-budget/1",
  "usable_delivered_kWh": 4.5,
  "illustrative_days_at_constant_daily_load": 2.25,
  "residual_without_generation_kWh": 4.5,
  "limitations": [
    "No warranty of autonomy; no power limit, degradation, weather, minimum voltage, standby losses or BMS state",
    "Demand must be independently measured for real use; medical and other critical loads need qualified continuity design"
  ]
}
```

## Case 7: microgrid-multiday-ledger

**Scope:** No actual protection, islanding, BMS, inverter, AC stability or weather observations

**Output:**

```json
{
  "schema": "atlas.energy-microgrid-profile/1",
  "intervals": [
    {
      "index": 0,
      "duration_h": 1.0,
      "stored_before_kWh": 0.9999999999999998,
      "load_served_kW": 2.0,
      "unmet_load_kW": 0.0,
      "renewable_generated_kW": 4.0,
      "renewable_curtailed_kW": 0.0,
      "grid_import_kW": 0.0,
      "battery_charge_kW": 2.0,
      "battery_discharge_kW": 0.0,
      "stored_after_kWh": 2.8,
      "storage_delta_kWh": 1.8,
      "conversion_loss_kWh": 0.19999999999999996,
      "balance_residual_kWh": 0.0,
      "assumptions": "single energy-only interval; renewable first, ideal grid if present, no inverter rating, protections, AC stability or BMS constraints"
    },
    {
      "index": 1,
      "duration_h": 1.0,
      "stored_before_kWh": 2.8,
      "load_served_kW": 2.0,
      "unmet_load_kW": 1.0,
      "renewable_generated_kW": 0.0,
      "renewable_curtailed_kW": 0.0,
      "grid_import_kW": 0.0,
      "battery_charge_kW": 0.0,
      "battery_discharge_kW": 2.0,
      "stored_after_kWh": 0.5777777777777775,
      "storage_delta_kWh": -2.2222222222222223,
      "conversion_loss_kWh": 0.22222222222222232,
      "balance_residual_kWh": 0.0,
      "assumptions": "single energy-only interval; renewable first, ideal grid if present, no inverter rating, protections, AC stability or BMS constraints"
    },
    {
      "index": 2,
      "duration_h": 1.0,
      "stored_before_kWh": 0.5777777777777775,
      "load_served_kW": 0.5199999999999996,
      "unmet_load_kW": 2.4800000000000004,
      "renewable_generated_kW": 0.0,
      "renewable_curtailed_kW": 0.0,
      "grid_import_kW": 0.0,
      "battery_charge_kW": 0.0,
      "battery_discharge_kW": 0.5199999999999998,
      "stored_after_kWh": 0.0,
      "storage_delta_kWh": -0.5777777777777775,
      "conversion_loss_kWh": 0.05777777777777778,
      "balance_residual_kWh": 1.457167719820518e-16,
      "assumptions": "single energy-only interval; renewable first, ideal grid if present, no inverter rating, protections, AC stability or BMS constraints"
    }
  ],
  "totals": {
    "load_kWh": 8.0,
    "renewable_kWh": 4.0,
    "served_kWh": 4.52,
    "unserved_kWh": 3.4800000000000004,
    "curtailed_kWh": 0.0,
    "imported_kWh": 0.0,
    "conversion_loss_kWh": 0.48000000000000004,
    "battery_delta_kWh": -0.9999999999999998,
    "hours": 3.0,
    "energy_balance_residual_kWh": 2.220446049250313e-16
  },
  "final_storage_kWh": 0.0,
  "minimum_storage_kWh": 0.0,
  "unserved_share_of_demand": 0.43500000000000005,
  "number_of_intervals_with_unserved_load": 2,
  "expected_loss_of_load_established": false,
  "electrical_grid_stability_verified": false,
  "limitations": [
    "Input scenarios and load/generation profiles are caller supplied; no independent stochastic reliability inference",
    "No AC frequency, voltage, inverter startup, battery health, islanding/protection, transfer switches or black-start guarantee",
    "No hazardous electrical wiring or operational controls are implemented"
  ]
}
```

## Case 8: grid-up-import-ledger

**Scope:** Assumes unlimited external grid during indicated availability

**Output:**

```json
{
  "schema": "atlas.energy-microgrid-profile/1",
  "intervals": [
    {
      "index": 0,
      "duration_h": 1.0,
      "stored_before_kWh": 0.1,
      "load_served_kW": 1.0,
      "unmet_load_kW": 0.0,
      "renewable_generated_kW": 0.0,
      "renewable_curtailed_kW": 0.0,
      "grid_import_kW": 0.91,
      "battery_charge_kW": 0.0,
      "battery_discharge_kW": 0.09000000000000001,
      "stored_after_kWh": 0.0,
      "storage_delta_kWh": -0.1,
      "conversion_loss_kWh": 0.010000000000000005,
      "balance_residual_kWh": 3.122502256758253e-17,
      "assumptions": "single energy-only interval; renewable first, ideal grid if present, no inverter rating, protections, AC stability or BMS constraints"
    }
  ],
  "totals": {
    "load_kWh": 1.0,
    "renewable_kWh": 0.0,
    "served_kWh": 1.0,
    "unserved_kWh": 0.0,
    "curtailed_kWh": 0.0,
    "imported_kWh": 0.91,
    "conversion_loss_kWh": 0.010000000000000005,
    "battery_delta_kWh": -0.1,
    "hours": 1.0,
    "energy_balance_residual_kWh": 2.7755575615628914e-17
  },
  "final_storage_kWh": 0.0,
  "minimum_storage_kWh": 0.0,
  "unserved_share_of_demand": 0.0,
  "number_of_intervals_with_unserved_load": 0,
  "expected_loss_of_load_established": false,
  "electrical_grid_stability_verified": false,
  "limitations": [
    "Input scenarios and load/generation profiles are caller supplied; no independent stochastic reliability inference",
    "No AC frequency, voltage, inverter startup, battery health, islanding/protection, transfer switches or black-start guarantee",
    "No hazardous electrical wiring or operational controls are implemented"
  ]
}
```

## Case 9: outage-scenarios-adverse-weather

**Scope:** The worst of two invented scenarios is not the worst possible real storm

**Output:**

```json
{
  "schema": "atlas.energy-scenario-panel/1",
  "scenarios": [
    {
      "scenario_id": "windy",
      "unserved_kWh": 0.0,
      "load_kWh": 2.0,
      "renewable_kWh": 4.0,
      "minimum_storage_kWh": 0.0,
      "balance_residual_kWh": 0.0
    },
    {
      "scenario_id": "calm",
      "unserved_kWh": 6.0,
      "load_kWh": 6.0,
      "renewable_kWh": 0.0,
      "minimum_storage_kWh": 0.0,
      "balance_residual_kWh": 0.0
    }
  ],
  "worst_supplied_unserved_energy": {
    "scenario_id": "calm",
    "unserved_kWh": 6.0,
    "load_kWh": 6.0,
    "renewable_kWh": 0.0,
    "minimum_storage_kWh": 0.0,
    "balance_residual_kWh": 0.0
  },
  "population_outage_probability_known": false,
  "weather_resource_verified": false,
  "limitations": [
    "Worst of a supplied scenario set is not a bound on unobserved physical emergencies",
    "Weather, demand correlation, degradation and equipment failure distributions are absent unless independently supplied"
  ]
}
```

## Case 10: invalid-pump-efficiency-refused

**Scope:** Bounded input validation only

**Output:**

```json
{
  "refused": true
}
```

## Case 11: invalid-critical-demand-refused

**Scope:** No medical or safety certification

**Output:**

```json
{
  "refused": true
}
```

