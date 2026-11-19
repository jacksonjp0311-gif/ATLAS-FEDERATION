# Manufacturing v0.2.0 — original ATLAS FORGE reference directory

**One canonical fourteen-node federation.** This edition reconciles the authenticated-by-hash Electronics v1.0.0-rc.1 mainline with the independently verified Manufacturing v0.1.0 sibling release, preserving both histories and all source-linked exact revisions.

## Reconstruction modules

Chapters 01–18 preserve the Manufacturing v0.1.0 scientific model, SI traceability, tolerance and fits, machine and material processes, SPC/inspection, thermal and semiconductor dependencies.

Chapters 19–30 extend these foundations with covariance positive-semidefiniteness, false acceptance probability, conditional Cp/Cpk, finite-sample yield intervals, calibration traceability chain audits, rigid datum transformations, resource-constrained operation planning, mass/energy accounting, evidence-gated process graphs, semiconductor fabrication provenance, repair requalification and the software-to-physical-computer handoff.

Read `DEPTH_MANUAL_v0.2.0.md` for all 30 chapters, `CASEBOOK_v0.2.0.md` for 26 constructed investigations, and `SCOPED_V1_GATES_v0.2.0.md` before interpreting any industrial claims.

## Tests and examples

`python -m unittest discover -s tests -q` runs the current standalone Manufacturing unit tests. The original v0.1.0 suite remains preserved in its exact historical snapshot. With NumPy/SciPy installed for optional independent oracles, run `PYTHONPATH=. python evidence/independent_oracle_v02.py`. In the full federation, run `python evidence/reconstruction_challenge.py` to see which physical dependencies block fabrication of a computer while the Electronics software interpreter passes a finite program test.

## Provenance/rights/physical limits

No original publisher source files are authenticated in this increment. NIST links are bibliographic navigation; source-to-equation authenticity and redistribution rights are not independently reviewed. There are no calibrated machine measurements, fabricated wafers, working physical CPUs or independent external expert conclusions. A software passing state is not a manufacturing certificate.

The original thirty-domain queue, historic releases, exact revisioned records and deferred Bitwork router policy are preserved. Next content domain after Manufacturing maturation: Computer Architecture & Digital Hardware.
