![ATLAS FORGE knowledge hub](assets/atlas_forge_knowledge_hub.png)

# CHEMISTRY ATLAS v0.1.0 · Technological Continuity

**Atoms → reactions → materials → semiconductors → processors → advanced AI**

An original **offline-readable, source-scoped chemistry reference**, not an industrial chemical manufacturing guide, instrument calibration certificate, or a trained chemical AI model. Chemistry is a new high-priority enabling domain alongside the original 30-domain ATLAS FORGE roadmap; it does not silently replace an original planned domain.

### Scientific directory

- [35-chapter scientific manual](docs/DEPTH_MANUAL_v0.1.0.md): human reconstructible definitions, derivations, equations, examples, counterexamples and publisher links.
- [Reading and reconstruction index](docs/REFERENCE_GUIDE.md).
- [25 executable original investigations](docs/CASEBOOK.md) demonstrating quantitative foundations, not laboratory results.
- [Source register](docs/SOURCE_REGISTER.md): 14 publisher cards with explicitly unresolved original-file/licensing status, including edition-sensitive OpenStax metadata.
- [Coverage and research gaps](docs/COVERAGE_MATRIX.md) · [Validation report](docs/VALIDATION_v0.1.0.md).
- [Standard-library numerical models](chemistry_atlas/models.py) · [tests](tests/) · [independent numerical oracle](tools/numerical_oracle.py).

### Reproduce offline

```sh
python -m chemistry_atlas
python -m unittest discover -s tests -q
python tools/numerical_oracle.py   # optional NumPy independent comparisons
```

**Data contract:** 168 Chemistry records (14 source cards), 140 internal typed relations. Six additional qualified cross-node links are present in the full 11-node collection, making 146 full Chemistry relations. The shared retrieval kernel is unmodified and Chemistry is not the new Bitwork router.

**Scientific limits:** No original publisher file, real experiment, verified chemical reaction mechanism, semiconductor fabrication, qualified hazardous handling or independent chemical-science peer review was acquired or carried out in this edition. The example chemistry models deliberately reject unsupported ions, isotopes and ambiguous balancing instead of inventing a result. Exact mass/charge bookkeeping does not establish actual sample purity or reaction feasibility.

**Priority order:** chemistry first, then mathematics/physics, electronics/semiconductors, manufacturing, computer architecture and the AI/software disciplines in the living technological-continuity roadmap. Complete content libraries before developing Bitwork routing, integrated evaluation and desktop transfer.
