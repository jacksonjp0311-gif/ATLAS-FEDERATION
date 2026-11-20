# Chapter 25 — Material purity, contamination, and semiconductor yield

**Domain:** Electronics-enabling chemistry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

A material sample's performance can depend on contaminants at trace levels. In semiconductor manufacturing, surface particles, unintentional dopants, oxygen content and structural defects can drastically change device yield. Purity must therefore be described with an explicitly named analyte, reference method, basis (mass, amount or atomic fraction), detection limit and sampling conditions. A certificate that says “99.99% pure” is incomplete if the remaining fraction contains electrically active impurities. Analytical instruments can have blanks and contamination from their own preparation paths. A survival-grade archive must preserve detection methodology and uncertainty, not only a final percentage.

## Mathematical or physical principle

`w_i=m_i/m_total for mass fraction; residual=Σ feed mass−Σ product mass−Δinventory; detection below LOD is censored, not zero.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Mass fractions must sum to one when all components are measured and the basis is consistent. A missing species can leave a residual but not identify its chemistry. Detection limits create censored observations: “not detected” is weaker than “absent”. For electronics, electrical activation and defect chemistry matter in addition to total impurity atoms. The process mass-balance function is a simple accounting check; independent chemical analysis is required before associating a residual with a particular contaminant.

## Reconstruct an illustrative result offline

Take a fictional 100 g sample containing measured 0.01 g impurity A; its mass fraction is 0.0001 or 100 ppm by mass. Now posit an unmeasured trace impurity B. Explain why reporting exactly 99.99% of the main material would require B and other constituents to be bounded.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No actual purification, toxic chemical handling or lithography procedure is included. Analytical uncertainty, sampling bias and contamination pathways remain open.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/) — inspected: Intrinsic/extrinsic carrier concepts, donor acceptor and band structure; not a fabrication tutorial
- [NIST Guide to Expression of Uncertainty in Measurement](https://www.nist.gov/publications/guide-expression-uncertainty-measurement) — inspected: Uncertainty and calibration scope for reconstructed measurements

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
