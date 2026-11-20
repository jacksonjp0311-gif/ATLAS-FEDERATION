# Computer Architecture & Digital Hardware — ATLAS FORGE v0.2.0

This is an **additive content edition inside the single original canonical ATLAS FORGE federation**. It extends the exact verified Computer Architecture v0.1.0 predecessor, retains all 14 other nodes and their source revisions, and does not edit the original 30-domain queue or implement Bitwork routing.

## Contents

36 original chapters and 30 constructed investigations. The original AT8 two-byte ISA remains unchanged. New independent reference components in `computer_atlas/`:

- `v02_bootstrap.py`: bounded `SET/ADD/XOR/AND/OR/STORE/LOAD/IN/OUT/REPEAT/END/HALT` language; compiler and independent source AST evaluator with 3-deep counted loops, no network or filesystem dependencies.
- `v02_control.py`: static ROM control-flow reachability, fall-off traps, conservative structural termination.
- `v02_ecc.py`: SECDED Hamming(13,8) per-byte ROM protection and fail-closed double-error handling, optional expected SHA-256.
- `v02_trace.py`: instruction-retirement differential checking of unchanged atomic and four-stage engines, event receipts and honest 12-type physical evidence HOLD.

## Reproduce

```sh
python -m unittest discover -s tests -q
PYTHONPATH=. python evidence/independent_oracle_v02.py
PYTHONPATH=. python evidence/continuity_challenge_v02.py
```

Use the full-collection `tools/check_collection.py --out /separate/results` after restoring the versioned patch onto its exact v0.1 full-federation base. The normal models use Python 3.10+ standard library only; no external model/inference service. Original-source binaries, physical CPU, source-to-equation expert review and actual fabrication are **not verified**.
