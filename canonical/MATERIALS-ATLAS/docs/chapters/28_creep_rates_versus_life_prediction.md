# 28. Creep: a steady strain-rate formula is not a rupture forecast

## Response and physical regime

At elevated homologous temperatures or otherwise creep-sensitive conditions, stress and time can produce inelastic deformation. Materials may exhibit primary, approximately steady secondary, and tertiary creep with damage accumulation; the regime boundaries depend on composition, grain size, stress, temperature, environment, and service history. A simplified *Norton–Arrhenius* steady-state strain-rate relation is `εdot=A σ^n exp(−Q/(RT))`.

`εdot` is s⁻¹, σ is entered in MPa, n is dimensionless, Q is J/mol, R=8.31446261815324 J/(mol K), T is kelvin, and **A must carry units s⁻¹ MPa⁻ⁿ**. The parameter set is not universal; it must be fitted to relevant creep measurements, ideally with uncertainty, stress/temperature coverage, and documented sample state. Substituting a tensile strength or a creep rate for an unrelated alloy violates the model's material identity.

## Sensitivity example

For constructed values `A=10⁻⁸ s⁻¹ MPa⁻³`, `n=3`, `Q=200,000 J/mol`, `T=900 K`, σ=50 MPa, the model gives approximately **3.086×10⁻¹⁵ s⁻¹**. Doubling stress to 100 MPa at constant temperature changes the rate by `2^3=8`; this identity follows from the *stipulated model*, not empirical validation. The strain accumulated over a selected duration under the constant-rate assumption is `ε≈εdot t`. It does not include elastic strain, primary creep, tertiary acceleration or microstructural damage.

## Why extrapolation is dangerous

A calibrated rate over hours at a particular stress and temperature does not establish safe lifetime for years at another temperature. A mechanism map may change from dislocation climb to diffusional creep, or microstructural aging may invalidate constant A, n, Q. Grain-boundary cavitation, oxidation, load multiaxiality, welds and stresses from thermal cycling can make rupture behavior very different from strain-rate behavior. The Atlas refuses to output creep rupture or component safe-life estimates from the rate alone.

## Essential reporting

Report the source of A/n/Q, regression model, applied stress basis and stress evolution, precise T/K history, sample composition/heat treatment, specimen geometry, stress and strain measurement system, calibration, confidence bands, replication, and whether the requested quantity lies inside the measured regime. The v1 implementation checks positive finite temperature and stress, dimensional convention for the pre-factor, and numerical overflow/underflow. It returns a conditional rate and a steady-regime increment with explicit exclusions.

**Connections:** mechanical properties (Chapter 07), fracture and fatigue (Chapter 17), degradation (Chapter 10), and time-sensitive equipment modeling (Control Atlas, queued).
