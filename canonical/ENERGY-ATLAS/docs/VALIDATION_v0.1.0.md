# Energy Atlas v0.1.0 — executed engineering and scientific-scope validation

**Edition:** substantive scientific-reference foundation, **not** content v1.0, certified energy equipment, or independent research breakthrough.

## Verified software and metadata

- Ten-node shared Atlas regression: **1,656 passing tests**, zero failures, zero skips. By suite: Forge 188, Measurement 218, Causal 233, Materials 122, Control 244, Agent 251, Computation 128, Language 135, LanguageV1 58, Energy 79.
- **11,000** independently implemented NumPy arithmetic comparisons across 11 synthetic categories, including PV models, wind power, Carnot bounds, AC real power, batteries, microgrid energy balance, trapezoidal integration and discounted LCOE. Maximum raw arithmetic discrepancy 9.09e-13 in the sampled units. No actual physical system measured.
- Shared contract schema passes for **1,927 records**, **1,133 relations**, **10 node manifests**, and **54 source-linked context packages**. Fast compiled JSON schema covers all; bounded Draft 2020-12 samples and independent AtlasStore context/source-closure validation also pass. Full Draft 2020-12 enumeration on every large context is not asserted.
- Clean isolated Python wheel installation exposes 176 Energy records and 144 standalone relations, and its source-linked casebook works with no source checkout imported. The complete collection has 149 Energy relationships, including five qualified cross-domain links whose targets exist only in the federation.
- Previous Language v1 archive checksum: `7f9dff64c080e8946a6ab445aa972d6edf1354ff479837203738e99248ece2af`. **2504 previous files matched exactly**, including all nine prior nodes and 771 original baseline files; the only edited paths are root navigation, registry, versioned checkpoint and test-runner metadata. Earlier Language v1 tests run unchanged against their immutable nine-node archive.
- Offline survival audit: **1927 records, 1133 relationships and 455 source cards**, no broken references. **0 authentic original primary-source bytes detected**. That is a major archival gap, not a missing mathematical reference.

## Scientific and safety boundaries

All Energy worked cases and numerical oracle inputs were authored for this edition. None is a field measurement, controlled experiment, actual energy efficiency discovery, certified electric system or a new source of energy. A nonzero energy-balance residual does not itself prove an unknown physical mechanism. A Betz upper bound, Carnot reversible cycle and linear PVWatts approximation have distinct assumptions; numerical tests cannot prove they apply to arbitrary equipment.

No independently authenticated original publisher source files, expert peer review, real solar/thermal/storage/grid equipment tests, authenticated sensor calibration, full nuclear safety validation, live software-controlled actuators, Bitwork router, or desktop deployment were performed. All those remain open gates.

## Reproduction commands

```sh
python tools/check_manifest.py verify .
python tools/survival_audit.py --root . --check-files
python tools/check_collection.py --out /different/path/unique-check
cd ENERGY-ATLAS
python -m energy_atlas
python -m unittest discover -s tests -q
python tools/numerical_oracle.py   # optional NumPy
```

The complete archive is tested again *after extraction* and recorded separately in the final external release receipt. The stored source-tree results do not substitute for that delivery replay.
