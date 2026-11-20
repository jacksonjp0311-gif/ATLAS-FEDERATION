# 52. The chemical-potential foundation of material transformation

**Theme:** Thermodynamics · **Chemistry Atlas scoped research v1.0.0**

**Evidence level:** project-written mathematical/reference explanation with scope-limited official sources. Every worked numeric input is hypothetical; publisher originals are not in this archive.

## Scientific foundation

Chemical potential is the partial molar Gibbs energy of a component, with other components' amounts held fixed at constant temperature and pressure. It is the central measure behind diffusion, phase equilibrium, chemical reactions and electrochemical migration. Treating concentration as chemical potential without accounting for a standard state can give systematically wrong predictions. The same chemical compound can have distinct chemical potentials in different phases, compositions or environments. A modern AI materials system must retain standard states, reference temperatures and uncertainty when transferring a property between data sources. This chapter follows the Gold Book's conceptual definition without reproducing its text as an authenticated original publisher file.

## Governing relationship and dimensional conventions

`mu_i=(partial G/partial n_i)_(T,p,n_j), and mu_i=mu_i°+RT ln a_i for dimensionless activity a_i.`

Dimensionless activities and properly normalized state conventions are required before taking logarithms. All heat-capacity and carrier-density inputs must carry the declared temperature, phase and units.

## Reconstruction and derivation

Differentiate the Gibbs energy with respect to amount of one constituent while holding other amounts, temperature and pressure fixed. A change in Gibbs energy associated with a small transfer of that species depends on this partial derivative. Integrating an ideal logarithmic mixing term yields RT ln a_i, where the activity is defined relative to a named standard state. It is not meaningful to take logarithms of a dimensional concentration unless normalized by an appropriate standard value. The electrochemical potential includes an electric-potential term for ions.

## Original worked investigation

For a hypothetical neutral species at T=300 K, compare activities 1 and 0.1. The chemical-potential difference is RT ln(0.1), negative for the lower activity under a common standard state. Recompute with an explicitly supplied gas constant and explain why an activity is not automatically equal to a measured molarity.

**Evidence requirement:** reproduce this arithmetic by hand or with independently written code; do not assert a laboratory result from an authored fixture.

## Failure boundaries and uncertainty

A source entry that reports only “concentration=1” cannot establish its physical activity, standard state or equilibrium energy. Partial molar properties can vary with phase and composition. No physical chemical equilibrium measurement or authenticated source-table bytes were acquired.

An incomplete dataset, untested thermodynamic fit or missing device safety requirement must remain explicitly unknown. No hazardous synthesis, energized apparatus or chemical processing steps are specified by this reference.

## Published source navigation (link only)

- [IUPAC Gold Book 5.0 — activity](https://goldbook.iupac.org/terms/view/A00115)
- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/)

These URLs are citations, not local authenticated copies of the publisher's full document. Check edition, license, original-byte hash and applicability before empirical use.
