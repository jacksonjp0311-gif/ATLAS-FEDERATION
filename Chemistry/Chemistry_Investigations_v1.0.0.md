# Chemistry Atlas v1.0.0 — Fourteen New Constructed Investigations

**No authentic compound, semiconductor, electrochemical cell, laboratory device, or primary publisher dataset was measured or acquired.**

## Investigation 40: Photon energy and supplied semiconductor gap

**Check:** passed. **Origin:** original offline fixture.

**Scope:** Energy above the gap does not guarantee light absorption or a working photodiode

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "schema": "atlas.chem-v1-photon-bandgap/1",
  "photon_energy_J": 3.9728917142978567e-19,
  "photon_energy_eV": 2.479683968664005,
  "bandgap_eV": 2.0,
  "energetically_above_supplied_gap": true,
  "assumptions": [
    "vacuum wavelength, single photon and caller-supplied gap"
  ],
  "limitations": [
    "Energy exceeding a gap is not proof of absorption, photocurrent, device efficiency or safe photo-processing",
    "Excitons, phonons, indirect transitions, interfaces and material absorption are omitted"
  ]
}
```

## Investigation 41: Empirical bandgap temperature dependence

**Check:** passed. **Origin:** original offline fixture.

**Scope:** Fit parameters invented for teaching and no independent calibration performed

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "schema": "atlas.chem-v1-varshni/1",
  "temperature_K": 300.0,
  "bandgap_eV": 1.1245192307692307,
  "derivative_eV_K": -0.0002546145627876397,
  "limitations": [
    "Empirical material-specific fit: do not extrapolate outside measured phase/temperature region",
    "Not a device design or proof of optical absorption/transport"
  ]
}
```

## Investigation 42: Intrinsic carrier statistics

**Check:** passed. **Origin:** original offline fixture.

**Scope:** Density-of-states input is asserted, not measured; no wafer quality assessment

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "schema": "atlas.chem-v1-intrinsic-carriers/1",
  "ln_carrier_density_per_m3": 36.249433754904295,
  "intrinsic_carrier_density_m3": 5532597190560799.0,
  "log_unit_reference": "natural log numerical density in m^-3",
  "limitations": [
    "Effective density of states and band gap are supplied at target temperature, not derived",
    "Nondegenerate, thermal equilibrium and ideal crystalline material only; traps, dopants, surfaces and devices omitted"
  ]
}
```

## Investigation 43: Ideal diode zero-bias current

**Check:** passed. **Origin:** original offline fixture.

**Scope:** No actual diode measured or fabricated

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "schema": "atlas.chem-v1-ideal-diode/1",
  "current_A": 0.0,
  "dimensionless_exponent": 0.0,
  "limitations": [
    "Ideal diode equation is not a silicon processing recipe or certified device IV curve",
    "No series/shunt resistance, reverse breakdown, self-heating, high injection, recombination or contacts"
  ]
}
```

## Investigation 44: Shomate heat capacity integral

**Check:** passed. **Origin:** original offline fixture.

**Scope:** Hypothetical coefficients, single phase, no reference thermochemical data acquired

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "schema": "atlas.chem-v1-shomate/1",
  "Cp_T1_J_mol_K": 30.6,
  "Cp_T2_J_mol_K": 30.8,
  "delta_H_J_mol": 3070.000000000001,
  "delta_S_J_mol_K": 8.83046217355343,
  "units": "Cp in J mol^-1 K^-1, H difference J mol^-1, S difference J mol^-1 K^-1",
  "limitations": [
    "Use only for source-verified species, phase, temperature segment and coefficients",
    "Parameter sets not authenticated in this release; no missing phase transitions inferred or independent calorimetry"
  ]
}
```

## Investigation 45: Reaction ΔCp and log equilibrium constant

**Check:** passed. **Origin:** original offline fixture.

**Scope:** No real reaction or measured equilibrium state

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "schema": "atlas.chem-v1-heat-capacity-equilibrium/1",
  "delta_H_J_mol": -98963.0,
  "delta_S_J_mol_K": -196.7932712217131,
  "delta_G_J_mol": -30085.355072400416,
  "logK": 10.33839001958349,
  "limitations": [
    "Reaction ΔCp assumed constant in one phase/temperature segment; input standard states must match",
    "A thermodynamic equilibrium position is not kinetic feasibility or safe chemical manufacture"
  ]
}
```

## Investigation 46: Electrochemical reversible-work accounting

**Check:** passed. **Origin:** original offline fixture.

**Scope:** Not battery chemistry specification or construction

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "schema": "atlas.chem-v1-electrochemical-work/1",
  "reversible_work_magnitude_J": 115782.39854797201,
  "illustrative_delivered_work_J": 92625.91883837762,
  "coulombs_transferred": 96485.33212331001,
  "limitations": [
    "This is only the magnitude of a reversible specified cell state; not a validated battery capacity, voltage curve or safety limit",
    "Overpotentials, diffusion, temperature, cycle life, contacts and materials sourcing not modeled"
  ]
}
```

## Investigation 47: Faraday charge-to-moles conversion

**Check:** passed. **Origin:** original offline fixture.

**Scope:** No actual electrolysis or chemical identity

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "schema": "atlas.chem-v1-faradaic-yield/1",
  "theoretical_mol": 1.0,
  "illustrative_product_mol": 0.9000000000000001,
  "limitations": [
    "No reaction identity, electrode, electrolyte, purity, side reactions, equipment or hazard specifications",
    "Faradaic efficiency is supplied, not measured; not an electrolysis synthesis recipe"
  ]
}
```

## Investigation 48: Bragg interplanar spacing

**Check:** passed. **Origin:** original offline fixture.

**Scope:** A spacing is not a material-phase identification

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "schema": "atlas.chem-v1-bragg-spacing/1",
  "d_spacing_nm": 0.15406000000000003,
  "assumptions": "elastic coherent diffraction from parallel planes, correctly calibrated theta and specified wavelength",
  "limitations": [
    "Peak indexing, phase identity, strain, texture, instrument broadening, radiation safety and specimen properties not inferred"
  ]
}
```

## Investigation 49: First-order measurement uncertainty

**Check:** passed. **Origin:** original offline fixture.

**Scope:** Uncertainties and correlations invented, not calibrated

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "schema": "atlas.chem-v1-uncertainty-product/1",
  "product": 6.0,
  "standard_uncertainty": 0.5,
  "limitations": [
    "First-order local approximation only: large nonlinear, non-Gaussian errors require other methods",
    "No instrument calibration or correlation verified from empirical observations"
  ]
}
```

## Investigation 50: Missing calibration blocks extrapolation

**Check:** passed. **Origin:** original offline fixture.

**Scope:** Rejected out-of-domain or contradictory input; no field evidence

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "refused": true
}
```

## Investigation 51: Invalid cell temperature rejected

**Check:** passed. **Origin:** original offline fixture.

**Scope:** Rejected out-of-domain or contradictory input; no field evidence

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "refused": true
}
```

## Investigation 52: Invalid covariance rejected

**Check:** passed. **Origin:** original offline fixture.

**Scope:** Rejected out-of-domain or contradictory input; no field evidence

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "refused": true
}
```

## Investigation 53: Noninteger electrons rejected

**Check:** passed. **Origin:** original offline fixture.

**Scope:** Rejected out-of-domain or contradictory input; no field evidence

Reconstruct the mathematical step from the chapter and the pure-Python function, then compare an independent calculation. Do not treat numerical agreement as an experimental observation.

```json
{
  "refused": true
}
```

