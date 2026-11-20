# 7. Fourier heat conduction and thermal resistance

**Area:** Heat Transfer. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Conduction moves heat in response to temperature gradients through a material. Fourier's law links heat flux to thermal conductivity and gradient, with a minus sign indicating flux down temperature. For a one-dimensional uniform slab under steady conditions, the heat rate is kA(Th−Tc)/L. The geometric approximation assumes no internal heat generation, constant conductivity, and negligible multidimensional paths. Thermal resistances in series can be added under the same one-dimensional steady assumption. In real buildings, motor windings and battery packs, contact resistance, radiation, convection and temperature-dependent conductivity matter. A useful calculation must not infer k from a single heat-rate observation without controlling area, thickness and other parallel pathways.

## Fundamental relationship, symbols and SI dimensions

`q'' = −k dT/dx; Qdot=kA(Th−Tc)/L; R_thermal=L/(kA).`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Integrate Fourier's law across a slab with constant k and steady uniform flux, giving a linear temperature profile. Resistance form follows by rearrangement. For multiple layers with equal cross-sectional area and series flow, total temperature drop is QdotΣR_i, provided each layer reaches the same steady heat rate. This is a mathematical boundary-value result, not a measurement of a real composite wall.

## Reconstruct the example without external AI

A 0.1 m thick slab has k=1 W/m/K, area 2 m², and 10 K temperature difference. Derive 200 W, then double thickness and compare. Describe how thermal bridging creates departures from 1D predictions.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Conductivity units W/(m K) are not the same as heat transfer coefficient W/(m² K). A contact temperature sensor can alter the measured profile and does not certify the model.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Chemistry WebBook SRD 69](https://webbook.nist.gov/chemistry/) — inspected: Thermodynamic data types and dependence on state, material, reference condition
- [DOE Energy Efficiency Versus Energy Intensity](https://www.energy.gov/cmei/energy-efficiency-vs-energy-intensity) — inspected: Efficiency differs from sector intensity and structural changes

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
