# Computation Atlas v0.2.0 — evidence and validation

**Content status:** Research foundation; not scoped scientific content v1.0. All 30 domains are incomplete. No Bitwork routing or desktop transfer.

## Verification scope

- New Computation test suite: **125 tests passed**, no skipped tests.
- Full eight-node source-tree check: **1,381 tests passed**, no errors or skips.
- Source-linked exact context closure: **32 of 32** representative contexts validated.
- Structural checks: 1,457 corpus records, 677 relationships, eight manifests; compiled JSON Schema over every record, relation, manifest and context; bounded Draft 2020-12 spot checks, **not exhaustive Draft 2020-12 for the large context corpus**.
- Independent numerical comparisons: **17,589** deterministic synthetic comparisons against independently implemented NumPy/SciPy/NetworkX/Python-oracle calculations. Not independent human review or hardware experimentation.
- Historical protection: **2,106 of 2,106** earlier protected file paths have the same SHA256; prior Computation **162 records and 175 relations** retain exact revisions. Other node manifests are not rebuilt.
- Previous Agent v1.0 release tests: executed unmodified against the embedded exact archived seven-node snapshot; the new shared registry is tested separately as eight-node.
- License-aware local archive: **two original MIT-licensed source-code files plus one MIT license**; both Git blob IDs are validated against a pinned commit SHA and exact bytes, and copied into the source wheel. No scholarly original primary paper is locally retained in this increment.
- Standalone source closure: 216 records, 221 Computation-only relations; the full federation preserves an additional five cross-node edges (226 full).

## Important limitations

The work is a mathematical and software preservation reference. Synthetic comparisons and checksums do not confer correctness or scientific novelty. Source-local snapshots protect only a narrow portion of the bibliography. Repository authorization and distribution rights must be reviewed per source. The archive is not cryptographically signed, independently reproduced on Windows, formally certified, or evaluated against live AI/Bitwork tasks.

## Reproduction

```sh
cd COMPUTATION-ATLAS
python -m unittest discover -s tests -q
python tools/numerical_oracle_v02.py
python tools/check_manifest.py verify .
cd ..
python tools/check_collection.py --out /tmp/atlas-v02-independent-check
python tools/check_manifest.py verify .
```

**Final extracted-package replay:** see external release audit attached to full ZIP; packaged internal receipt is a source-tree preflight rather than a claim of future verification.
