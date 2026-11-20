# Investigation 03 — Why two reported strengths may not conflict

**Evidence type:** Original hypothetical mechanical-testing comparison. The quantities and specimens are invented. Reference: [ASTM E8/E8M publisher scope](https://store.astm.org/standards/e8_e8m) and [NIST mechanical data provenance](https://www.nist.gov/programs-projects/ncal-data-management).

## Initial observation
A technician reports that “batch A is stronger than batch B” because two labels read 250 and 220 MPa. Before treating these as competing estimates of the same property, the analyst needs to learn whether the values are yield strengths, ultimate tensile strengths, applied engineering stresses, or design allowable limits. The temperature, strain rate, direction, specimen location, heat treatment and method edition can differ.

The Atlas can calculate engineering stress for a fabricated point: `5000 N / 20 mm² = 250 MPa`. Paused there, the result is only **one point**. An invented extension `0.5 mm` over `50 mm` initial gauge length gives `epsilon=0.01`, but none of these inputs establishes the elastic modulus or a 0.2% offset yield. Those quantities need curves, procedures and equipment records.

## Comparison gate
If two fully typed records differ in method or origin, `compare_properties` refuses to subtract their values. A simulated modulus from a perfectly periodic ideal crystal is not automatically an experimental tensile result from an annealed polycrystal. If the methods and all selected context fields match, arithmetic subtraction is allowed, but the interface does **not** claim statistical significance: shared calibration errors and within-lot variation are not modeled.

A conservative investigator must preserve both original results, record the discrepancy's possible context explanation, and either obtain compatible tests or scope the conclusion to the exact conditions actually observed.

## Application to process changes
If a plant changed material supplier and heat treatment simultaneously, even a real observed property difference does not uniquely identify which factor caused it. The Causal Atlas is needed for experiments and confounding; Manufacturing Atlas will later capture operating conditions and equipment. The Materials Atlas supplies the physical interpretation and conditions without assuming causal identification.

**Outcome:** computed stress and strain from invented inputs; no qualified material ranking, no laboratory replication and no standard compliance.
