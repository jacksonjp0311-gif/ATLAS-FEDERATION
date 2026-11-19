# Computation Atlas v1.0.0 — scoped release audit

**Release content status: scoped reference v1.0.0. Independent scientific acceptance: open.**

## Executed source-tree checks

- **1,384 automated tests passed, zero skipped**, including the 128 new Computation tests; all eight node suites completed. The historic Agent v1 suite runs unchanged against its original preserved seven-node snapshot.
- The original Computation v0.1 standalone ZIP independently replayed **76 tests with zero failures**. Its 162 original record revisions persist. All 232 v0.2 record and 250 local relation revisions persist.
- **87,385 NumPy/SciPy/NetworkX numerical comparisons** on author-generated tests passed; maximum numerical discrepancy was 8.811e-13. These are code oracles, not scientific experiments or formal universal proofs.
- Common source/relationship closure, JSON schema and **32** source-linked context checks pass. Shared registry holds **1,475 records, 707 relationships, eight nodes**; standalone Computation contains 234 records and 251 local relationships.
- **1664 protected files** from the previous full collection are byte-identical, including previously created nodes and baseline source code. No Bitwork/router implementation was altered.
- Clean offline wheel installation loads the shared reader and Computation 1.0.0, runs the 32-case reference casebook and validates source closure.

## Preservation and science limitations

- **396 source cards, zero authenticated locally retained original primary-publisher files** under the strict survival audit. No claim that all outside scientific literature survives offline. Rights-cleared primary-source acquisition remains outstanding.
- Mathematical references cover a *declared* educational scope, not all of mathematics or computation. Peer review, full standard conformance, independent proof kernels and measured real-world speedups remain open.
- NIST FIPS 203 and Lamport sources are bibliography/scope references; no deployed cryptography, authenticated distributed system or live agent tests were performed.
- Casebook inputs and numerical oracles are **authored fixtures**. Passing tests must not be sold as a new computational discovery or a measured improvement to AI models.

## Reproduce

```sh
python tools/check_collection.py --out output/new_unique_check
python tools/survival_audit.py --root . --check-files
python tools/check_manifest.py verify .
cd COMPUTATION-ATLAS
python -m computation_atlas
python -m unittest discover -s tests -q
python tools/advanced_oracle_v02.py
```

Exact archive SHA-256, manifests and post-extraction replay are recorded in the external release receipt, not assumed from this source-stage audit.
