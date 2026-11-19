# ATLAS FORGE / Network Stacks Atlas — Original Domain #16

This is a **native node inside the ONE canonical ATLAS FORGE federation**; never use it as a separate Atlas or standalone substitute. Current release candidate: scoped offline scientific/software reference **v1.0.0**. Complete historical predecessor, exact revisions and original 30-domain roadmap are preserved.

- `docs/DEPTH_MANUAL_v1.0.0.md`: 22 original technical chapters, worked cases, equations and negative controls.
- `data/`: eight explicit atlas.common/1 collections, all records sealed with canonical immutable revisions.
- `net_atlas/`: dependency-minimal Python 3 reference models, deliberately bounded to supported protocol subsets.
- `tests/`, `evidence/`: unit suites, independent oracle, previous unsealed working-model comparison and build instructions.
- `docs/SCOPED_V1_GATES_v1.0.0.md`: independent scientific/wire/security HOLD register.

Run from this node folder:

```sh
PYTHONPATH=. python -m unittest discover -s tests -q
PYTHONPATH=. python evidence/independent_oracle_v1.py
PYTHONPATH=. python evidence/independent_oracle_prior.py
```

The final release only becomes canonical after full historical federation and exact fresh-restore verification and Library readback. RFC links are bibliographic pointers; they are **not** authenticated original publisher bytes. No Bitwork router or desktop transfer was changed.
