# Chemistry Atlas v0.2.0 — fourteen new worked investigations
All fourteen are explicitly constructed mathematical inputs, NOT actual chemical experiments, spectroscopy, semiconductor or clinical evidence.

## Investigation 26: ionic acid-base bookkeeping

Status in the bounded reference model: **passed**.

**Assumptions / limits:** Charge/atom conservation not proof of physical mixing or safety

```json
{
  "schema": "atlas.chem-ionic-stoichiometry/1",
  "reactant_coefficients": {
    "H+": 1,
    "OH-": 1
  },
  "product_coefficients": {
    "H2O": 1
  },
  "coefficient_vector": [
    1,
    1,
    1
  ],
  "atom_residuals": {
    "H": 0,
    "O": 0
  },
  "charge_residual": 0,
  "math_conservation_verified": true,
  "physical_reaction_verified": false,
  "limitations": [
    "Species and charge states are supplied; no solution speciation, charge assignment or actual chemistry proved",
    "Only unique positive nullspace accepted; underdetermined equations are refused, not guessed",
    "No synthesis procedure, energy balance, electronic spin, phases, kinetics, or hazard control inferred"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 27: formal electron conservation

Status in the bounded reference model: **passed**.

**Assumptions / limits:** Formal redox bookkeeping not electrolysis protocol

```json
{
  "schema": "atlas.chem-ionic-stoichiometry/1",
  "reactant_coefficients": {
    "Fe3+": 1,
    "e-": 1
  },
  "product_coefficients": {
    "Fe2+": 1
  },
  "coefficient_vector": [
    1,
    1,
    1
  ],
  "atom_residuals": {
    "Fe": 0
  },
  "charge_residual": 0,
  "math_conservation_verified": true,
  "physical_reaction_verified": false,
  "limitations": [
    "Species and charge states are supplied; no solution speciation, charge assignment or actual chemistry proved",
    "Only unique positive nullspace accepted; underdetermined equations are refused, not guessed",
    "No synthesis procedure, energy balance, electronic spin, phases, kinetics, or hazard control inferred"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 28: source-supplied delta Gibbs

Status in the bounded reference model: **passed**.

**Assumptions / limits:** Formation values are invented and measured conditions unverified

```json
{
  "schema": "atlas.chem-reaction-thermochemistry/1",
  "temperature_K": 300.0,
  "delta_G_standard_J_per_mol_reaction": -2000.0,
  "delta_H_standard_J_per_mol_reaction": -1600.0,
  "log_equilibrium_constant": 0.8018157002848403,
  "entropy_or_heat_capacity_independently_verified": false,
  "limitations": [
    "Every supplied formation energy must refer to the same temperature, phases and standard-state convention",
    "Computing log K does not imply reaction reaches equilibrium, positive kinetics, or safe process",
    "These data are caller-supplied, not extracted from an authenticated thermochemical publisher file"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 29: vanthoff-temperature-dependence

Status in the bounded reference model: **passed**.

**Assumptions / limits:** ΔH temperature-independent hypothesis only

```json
{
  "schema": "atlas.chem-vanthoff/1",
  "logK_target": 0.10022696253560506,
  "ratio_K_target_to_reference": 1.1054217789364227,
  "reference_logK": 0.0,
  "temperature_K": 400.0,
  "assumption": "reaction delta H constant over temperature interval; no phase transition or heat capacity changes",
  "limitations": [
    "No predictive claim for real system without phase-aware thermodynamic data",
    "Huge logK ratio returned as null, not overflow/infinity"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 30: molar ionic strength

Status in the bounded reference model: **passed**.

**Assumptions / limits:** Not activity or ion-speciation proof

```json
{
  "schema": "atlas.chem-ionic-strength/1",
  "I_molarity_basis_mol_L": 0.01,
  "charge_balance_residual_mol_L_equivalent": 0.0,
  "electroneutrality_proven": true,
  "limitations": [
    "Concentration-basis ionic strength is not an activity model or solution speciation",
    "Ion charges/molarity assigned by user; counterions or dissolved complexes may be missing"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 31: dilute-ion activity warning

Status in the bounded reference model: **passed**.

**Assumptions / limits:** Solvent/temperature coefficient invented for this exercise

```json
{
  "schema": "atlas.chem-debye-huckel-limiting/1",
  "log10_mean_idealized_gamma": -0.01609599329025705,
  "gamma": 0.9636160094164827,
  "limitations": [
    "Only limiting-law illustration at stated low ionic strength; solvent/temp coefficients supplied",
    "No validated activity correction for concentrated mixtures, multicomponent interactions, or specific ion pairing"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 32: donor-majority-carriers

Status in the bounded reference model: **passed**.

**Assumptions / limits:** Full ionization and nondegenerate charge neutrality assumed

```json
{
  "schema": "atlas.chem-semiconductor-carrier-neutrality/1",
  "electron_density_m3": 1.0000000001000001e+21,
  "hole_density_m3": 99999999990.0,
  "mass_action_relative_error": 0.0,
  "assumptions": [
    "thermal equilibrium, non-degenerate statistics, one temperature, charge-neutral uniform material",
    "dopants fully ionized and no trap, compensation or interface band-bending"
  ],
  "limitations": [
    "Not validated for degenerate doping, low-temperature freeze-out, high injection, junctions, defects or devices",
    "Carrier densities cannot be used as a wafer fabrication recipe or material purity certification"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 33: acceptor-majority-carriers

Status in the bounded reference model: **passed**.

**Assumptions / limits:** No actual silicon wafer or device measured

```json
{
  "schema": "atlas.chem-semiconductor-carrier-neutrality/1",
  "electron_density_m3": 99999999990.0,
  "hole_density_m3": 1.0000000001000001e+21,
  "mass_action_relative_error": 0.0,
  "assumptions": [
    "thermal equilibrium, non-degenerate statistics, one temperature, charge-neutral uniform material",
    "dopants fully ionized and no trap, compensation or interface band-bending"
  ],
  "limitations": [
    "Not validated for degenerate doping, low-temperature freeze-out, high injection, junctions, defects or devices",
    "Carrier densities cannot be used as a wafer fabrication recipe or material purity certification"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 34: Fick-gradient-flux

Status in the bounded reference model: **passed**.

**Assumptions / limits:** No real diffusion profile

```json
{
  "schema": "atlas.chem-fick-flux/1",
  "flux_mol_m2_s": 2e-09,
  "assumption": "constant effective diffusivity, continuum, concentration-gradient driven transport",
  "limitations": [
    "Nonideal chemical potential gradients, multicomponent diffusion, interfaces and convection omitted"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 35: reflecting-boundary-diffusion

Status in the bounded reference model: **passed**.

**Assumptions / limits:** Synthetic no-flux boundary not semiconductor diffusion furnace data

```json
{
  "schema": "atlas.chem-1d-diffusion/1",
  "concentrations_mol_m3": [
    0.1834889981708789,
    0.20627191852195315,
    0.22047816661433595,
    0.20627191852195317,
    0.18348899817087894
  ],
  "integral_before_mol_m2": 1.0,
  "integral_after_mol_m2": 1.0,
  "conserved_relative_residual": 0.0,
  "stability_coefficient": 0.1,
  "boundary_condition": "zero net flux at both ends",
  "limitations": [
    "Toy one-dimensional constant-D Fickian continuum, no real processing recipe",
    "Physical D(T), surface reactions, charged dopant transport and geometry omitted"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 36: spectroscopic-transmission

Status in the bounded reference model: **passed**.

**Assumptions / limits:** No validated real spectrometer or analyte purity

```json
{
  "schema": "atlas.chem-absorbance/1",
  "absorbance_decadic": 0.2,
  "transmitted_fraction_ideal": 0.6309573444801932,
  "scope": "single ideal absorbing species, monochromatic light, no scattering or stray light",
  "limitations": [
    "No independent optical calibration, chemical selectivity, instrument dynamic range or sample identity",
    "Absorbance is a measurement model, not proof of analyte concentration in unknown real mixtures"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 37: source-bytes-not-proven-authentic

Status in the bounded reference model: **passed**.

**Assumptions / limits:** Hash match is not authentic publisher provenance or legal license grant

```json
{
  "schema": "atlas.chem-source-bytes-audit/1",
  "source_id": "authored-reference",
  "local_bytes_present": true,
  "sha256_observed": "3d5151c9696ea2d8b957b7881900b1d812f562b611841540d66e023f366f5f31",
  "matches_supplied_expected_digest": true,
  "license_status_caller_assertion": "cleared_for_archive",
  "publisher_origin_authenticated": false,
  "copyright_and_license_independently_verified": false,
  "eligible_for_external_rights_review": true,
  "automatically_republishable": false,
  "limitations": [
    "Matching hashes validate only supplied bytes and expected digest, not publisher identity",
    "Caller-provided rights assertions do not grant actual redistribution rights"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 38: mismatched-archive-byte-hash

Status in the bounded reference model: **passed**.

**Assumptions / limits:** No restricted source redistributed

```json
{
  "schema": "atlas.chem-source-bytes-audit/1",
  "source_id": "authored-reference",
  "local_bytes_present": true,
  "sha256_observed": "3d5151c9696ea2d8b957b7881900b1d812f562b611841540d66e023f366f5f31",
  "matches_supplied_expected_digest": false,
  "license_status_caller_assertion": "restricted",
  "publisher_origin_authenticated": false,
  "copyright_and_license_independently_verified": false,
  "eligible_for_external_rights_review": false,
  "automatically_republishable": false,
  "limitations": [
    "Matching hashes validate only supplied bytes and expected digest, not publisher identity",
    "Caller-provided rights assertions do not grant actual redistribution rights"
  ]
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.

## Investigation 39: dilute-scope-refusal

Status in the bounded reference model: **passed**.

**Assumptions / limits:** A concentration-limit rejection is not a scientific claim about actual concentrated solution

```json
{
  "rejected": true
}
```

To independently reconstruct, derive the governing equation from the related chapter and recompute the numeric result with `chemistry_atlas.advanced`. The worked case is not a laboratory instruction.
