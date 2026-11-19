# ATLAS FORGE — Computer Architecture & Digital Hardware v0.1.0

**A supporting engineering node in the SINGLE original canonical ATLAS FORGE federation, not a separate Atlas or a rewritten slot of its preserved 30-domain queue.**

This package reconstructs a finite original 8-bit stored-program machine (**AT8**) from its architectural instruction contract through a NAND-only arithmetic reference, assembler/disassembler, independently implemented atomic and four-phase microcycle executors, deterministic I/O traces, bounded tests and an evidence-gated Manufacturing integration challenge.

## Navigate the research

- `docs/DEPTH_MANUAL_v0.1.0.md`: 24 original chapters with derivations, limitations, negative cases, examples, source cards and explicit cross-domain requirements.
- `docs/CASEBOOK_v0.1.0.md`: 18 constructed reproducible test cases.
- `docs/RECONSTRUCTION.md`: exact archive recovery and test commands.
- `docs/RECONSTRUCTION_BRIDGE.md`: electrical-to-computer technology evidence pathway.
- `docs/SOURCE_REGISTER_v0.1.0.md`: bibliographic navigation, original bytes unverified.
- `docs/SCOPED_V1_GATES.md`: separate software release and scientific/hardware acceptance requirements.
- `evidence/AT8_ISA_SPEC_v0.1.0.json`: machine-readable original ISA.
- `evidence/GOLDEN_PROGRAMS_v0.1.0.json`: ROMs, instruction counts, output tapes and hashes.
- `computer_atlas/{isa,spec,microcoded,gates,programs}.py`: Python standard-library reference kernels.

## Minimal offline demonstration

```sh
python -m computer_atlas
python -m unittest discover -s tests -q
python evidence/independent_oracle.py
python evidence/continuity_challenge.py
```

The full federation runner additionally checks the exact historical test snapshots, common graph registry, schema contracts, source-linked contexts and immutable predecessor files.

## Evidence boundaries

AT8 is an original educational ISA, **not RISC-V/Beta/Hack**; the microcycle model is **not fabricated RTL or timing-qualified hardware**. Physical CPU construction, independent expert review, original publisher-file authentication and manufacturing equipment calibration are not demonstrated. All such gates remain HOLD. Routing stays deferred; the 30-domain roadmap is not changed.


## New v0.2.0 contents

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
