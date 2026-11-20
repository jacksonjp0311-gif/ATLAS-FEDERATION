![ATLAS FORGE knowledge hub](assets/atlas_forge_knowledge_hub.png)

# ENERGY ATLAS v0.2.0 — Survival Science Research Edition

**Reconstruct energy science, then account for real services without pretending to operate equipment.**

Energy Atlas is an offline-readable research library within ATLAS FORGE. This is an expanded content research edition, not a safety-certified electric grid, a live agent, an approved battery system, a medical backup plan, or a water-treatment guide.

## Reading order

- [50-chapter original scientific manual](docs/DEPTH_MANUAL_v0.2.0.md) covering energy, thermal systems, electricity, generation, storage, resilient services and measurement
- [Survival energy reconstruction path](docs/SURVIVAL_RECONSTRUCTION_PATH.md) for humans reading without an online model
- [36 constructed cases](docs/CASEBOOK.md), including [11 survival-service cases](docs/SURVIVAL_CASEBOOK_v0.2.0.md)
- [Source register](docs/SOURCE_REGISTER.md), [coverage gaps](docs/COVERAGE_MATRIX.md), [scoped v1 gates](docs/SCOPED_V1_RESEARCH_GATES.md), [validation](docs/VALIDATION_v0.2.0.md)
- [Machine-readable records](data/) with exact source revisions and [offline teaching methods](energy_atlas/survival_models.py)

## Offline entrypoints

```sh
python -m energy_atlas                  # original v0.1 cases
python -m energy_atlas survival-casebook
python -m unittest discover -s tests -p test_survival_models.py
python tools/survival_oracle.py         # optional NumPy independent math comparisons
```

**Records:** 241 exact source-linked Energy records (28 source cards), 200 internal relationships. Five older cross-domain relations are included in the full ten-node federation only, yielding 205 Energy relationships there; no dangling standalone targets.

**Knowledge survival:** 50 original chapters remain readable without cloud models. The 28 energy source cards are link-only and none has authenticated original publisher bytes; source acquisition remains a critical unfinished obligation. The historical v0.1 tests run on their preserved immutable context snapshot, not silently changed to pass this version.

**Fixed project order:** all 30 domain libraries before Bitwork routing; integrated verification and desktop transfer after routing. No router modifications in this release.
