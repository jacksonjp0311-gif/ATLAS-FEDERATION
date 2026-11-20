# Materials Atlas review templates

## Experimental property record
Material ID / batch / nominal vs verified composition / processing state / sample location / geometry / method + revision / measured property and units / raw file and local hash / temperature and atmosphere / orientation / replicate count / calibration and uncertainty / instrument changes / rights / reviewer / use limitations.

## Computed property record
Structure ID / phase and composition / input file hash / software and version / functional and correction scheme / pseudopotential / k point settings / convergence / energy normalization / magnetic state / structural relaxation / competing phases included / calculated property and units / data release / known accuracy limitations / source and rights.

## Candidate comparison
Operating conditions / failure mode / property definition and direction / comparable condition table / required reliability / manufacturability / cost assumptions / missing values / screening result / uncertainty and qualification plan / refusal reasons.

## Evidence-change log
Original record ID and revision / new source or raw data / contradictory values and condition differences / author and checker / review status / downstream contexts affected / supersession link / versioned release change.


## v0.3.0 extra report templates

### Finite-T phase-model assessment

- Hypothesis, phase family and reference state:
- Specified binary species, composition basis and pressure:
- Model form, parameter Ω, units and calibration origin:
- Temperature range, competing phase assumptions and kinetic limitations:
- Independent boundary algorithm, residual/precision checks and failures:
- Relation to actual experimental tie lines or assessed CALPHAD, if any:
- Source IDs and versioned evidence qualification:
- Decision: only model result / physically corroborated / not established:

### Indexed XRD uncertainty assessment

- Specimen, phase hypothesis, texture, sample preparation and temperature:
- Instrument/radiation spectrum, wavelength and shared uncertainty:
- Peak-profile fitting and instrument correction method:
- hkl, 2θ and u(2θ) per independent peak, with excluded peaks listed:
- Random versus correlated uncertainty model and covariance treatment:
- Weighted cell parameter and chi-square diagnostics:
- Independent refinement or structure-factor evidence, if any:
- Limitations, source closure and abstention conditions:


## v1 template — material-property evidence packet

- Decision question and explicit refusal condition:
- Actual material grade, chemistry, lot, product form, surface/heat treatment, and specimen history:
- Property definition and unit dimension (temperature, time, orientation, frequency):
- Observation versus publisher compilation versus theoretical model versus synthetic example:
- Primary source locator, rights and inspected portion; authenticated upstream hash or `null`:
- Measured and missing uncertainty components; replication and specimen sampling:
- Model selection with falsification tests, residual checks and out-of-domain behavior:
- Competing explanations, differences among published sources, unsupported transfer:
- Required standard and qualified review (not assumed met):
- Final defensible statement and exact source closure:

## v1 template — corrosion and localized damage study

- Coupon condition, exposed area mask, cleaning/blank correction and mass uncertainties:
- Duration, environment, temperature, pH, medium, flow and redox conditions:
- Density measurement basis; equivalent uniform-rate model:
- Pitting morphology, local maximum depth and spatial distribution (measured or explicitly unknown):
- Replicates, censoring and detection thresholds:
- Field-transfer hypothesis, failure mechanism and untested conditions:
- Pass/fail: `insufficient-evidence` until governing qualification evidence exists:

## v1 template — thermal and creep multi-physics boundary ledger

- Geometry and time dependence of heat conduction:
- Conductivities k(T), anisotropy, contact resistances, boundary fluxes and heat sources:
- Stress and temperature histories (measured vs controller set-points):
- Creep model parameter units (stress unit embedded in A), fit range and uncertainty:
- Primary/tertiary creep, damage, oxidation, weld and rupture evidence:
- Models excluded; assumptions tested; actual specimen evidence and governing limits:
