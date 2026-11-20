# 59. Intrinsic carrier statistics and density-of-states assumptions

**Theme:** Semiconductor transport · **Chemistry Atlas scoped research v1.0.0**

**Evidence level:** project-written mathematical/reference explanation with scope-limited official sources. Every worked numeric input is hypothetical; publisher originals are not in this archive.

## Scientific foundation

Thermal excitation in a semiconductor produces electron and hole populations. For a uniform, undoped, nondegenerate equilibrium material with appropriate effective densities of states, intrinsic carrier concentration follows a thermal exponential relation. The carrier density is sensitive to temperature, band gap, and the effective density of allowed states in the conduction and valence bands. Simply multiplying dopant concentration by charge does not establish free carrier density. Traps, compensation, incomplete ionization, band bending and degenerate statistics can invalidate a simplified mass-action approach.

## Governing relationship and dimensional conventions

`ni=sqrt(Nc Nv)*exp[-Eg/(2 kB T)], where Nc and Nv are effective state densities in m^-3, Eg in joules, T in kelvin.`

Dimensionless activities and properly normalized state conventions are required before taking logarithms. All heat-capacity and carrier-density inputs must carry the declared temperature, phase and units.

## Reconstruction and derivation

In an ideal band model, thermally populated conduction-band electrons and valence-band holes follow Boltzmann statistics at low occupancy. Combining their equilibrium populations yields the exponential half-gap dependence of intrinsic density. The calculation is most stable using ln ni=0.5(ln Nc+ln Nv)-Eg/(2kBT), which avoids unnecessary overflow when multiplying large density parameters. The output remains conditional on the supplied, temperature-appropriate effective density of states; the software does not predict them from crystal physics.

## Original worked investigation

Specify Nc=2e25 m^-3, Nv=1e25 m^-3, Eg=1.12 eV and T=300 K, and compute ln ni before exponentiation. Increase temperature with the other inputs frozen and observe the increase in the ideal population. Then note that real Nc/Nv and Eg themselves vary with temperature.

**Evidence requirement:** reproduce this arithmetic by hand or with independently written code; do not assert a laboratory result from an authored fixture.

## Failure boundaries and uncertainty

The model assumes full thermal equilibrium and nondegenerate carriers. It is unsuitable for heavily doped junctions, freeze-out, surface/interface effects and device design without additional physical characterization.

An incomplete dataset, untested thermodynamic fit or missing device safety requirement must remain explicitly unknown. No hazardous synthesis, energized apparatus or chemical processing steps are specified by this reference.

## Published source navigation (link only)

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/)
- [Materials Project API and computed materials data schema](https://docs.materialsproject.org/downloading-data/using-the-api)

These URLs are citations, not local authenticated copies of the publisher's full document. Check edition, license, original-byte hash and applicability before empirical use.
