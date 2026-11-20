# 43. Semiconductor carrier statistics and doping assumptions

**Field:** Semiconductors · **Version:** v0.2.0 · **Scientific status:** original educational reference; cited publisher portions inspected, original publisher bytes not archived. No real experiment.

## Principles and physical scope

Modern AI computation depends on controlled electrical transport in semiconductors. Carrier density depends on material band structure, temperature, defects, dopants and injection conditions; an impurity concentration is not automatically the same as the density of mobile carriers. For an ideal uniform nondegenerate semiconductor at thermal equilibrium, mass-action np=n_i² and charge neutrality n−p=N_D−N_A provide a simple two-equation model. This is valuable because an algorithm can solve the equations stably and reveal where assumptions enter. It does not teach a physical doping recipe or establish manufacturing purity/yield. Materials properties and mobility require independent data by material, phase and temperature.

## Equation and definitions

`n−p=D and np=n_i², where D=N_D−N_A under full-ionization assumptions. For D≥0: n=(D+sqrt(D²+4n_i²))/2; p=n_i²/n. For D<0 solve p first to avoid cancellation.`

Inputs and reference states must be declared. The algebra alone cannot establish source data validity, experimental behavior or physical safety.

## Derivation and why the relationship holds

Multiply the carrier densities to express equilibrium mass action and subtract to express neutrality; solve the resulting quadratic. A naïve formula for the minority carrier can lose floating precision when the doping difference is large, so compute the majority root first and use the product identity for the minority. When doping is not fully ionized, semiconductor statistics are degenerate or contacts induce space charge, the simple equations cease to describe the real structure. An exact numerical solution only proves consistency with the declared ideal model.

## Reconstruct without external AI

Set n_i=10^16 m−3 and an invented donor excess D=10^21 m−3. Solve n and p; check n−p≈D and np≈10^32 m−6. Reverse the sign of D and confirm the majority changes from electrons to holes. Explain what experimental mobility and dopant-activation measurements are missing.

These examples are invented, not laboratory readings. Reproduce them by hand and compare only within the declared model domain.

## Failure case and missing evidence

This model excludes heterojunctions, high-injection physics, trap occupation, interface charge, strain and realistic process variability. Do not use it to specify dopant doses, furnace settings or fabricate a device.

## Source provenance and rights

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/) — Intrinsic/extrinsic carrier concepts, donor acceptor and band structure; not a fabrication tutorial
- [Materials Project API and computed materials data schema](https://docs.materialsproject.org/downloading-data/using-the-api) — Materials Project data API, computational vs observed provenance, dataset and code version distinctions

**Not retained:** original publisher documents, real chemical samples, source tables and independent domain review.
