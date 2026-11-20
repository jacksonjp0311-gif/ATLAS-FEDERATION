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


## Computer Architecture v0.3.0

# ATLAS FORGE — Computer Architecture & Digital Hardware v0.3.0

**The same original 15-node ATLAS FORGE federation, not a replacement project.**

48 cumulative original technical chapters and 42 constructed investigations, with a bounded AT8 software reference for an ISA-stable, source-compiled, checksum-verified boot and execution pipeline.

## Added in this edition

- `computer_atlas/v03_boot.py`: deterministic boot image and two-slot recovery simulation
- `computer_atlas/v03_control.py`: conservative finite control-flow reachability and halting conditions
- `computer_atlas/v03_cache.py`: direct-mapped write-through RAM cache
- `computer_atlas/v03_workflow.py`: three-model verification and isolated batch receipts
- `tests/test_v03_boot_control.py`: finite deterministic positive and negative cases
- `evidence/independent_oracle_v03.py`: independently coded arithmetic/ECC/cache/ROM header comparisons
- `docs/chapters/37_*.md` through `48_*.md`: original reconstruction chapters
- `docs/DEPTH_MANUAL_v0.3.0.md`: all 48 chapters in one offline reading artifact

The original v0.1 and v0.2 edition tests, source records, scientific nodes, original 30-domain roadmap and deferred Bitwork routing remain untouched. No physical CPU, production OS, authenticated firmware boot chain or external scientific review is claimed.


## Computer Architecture v0.4.0 within the original ATLAS FORGE federation

12 new chapters (49–60) and bounded software reference models for explicit NAND datapaths, unknown-state logic, Harvard ROM/RAM boundary, parity and bus arbitration, and source-to-boot-to-retirement-to-gate evidence.
Read [v0.4.0 edition README](README_v0.4.0.md), [60-chapter manual](docs/DEPTH_MANUAL_v0.4.0.md), [reconstruction protocol](docs/RECONSTRUCTION_v0.4.0.md), and [acceptance gaps](docs/SCOPED_V1_GATES_v0.4.0.md).
This does not demonstrate hardware construction, certified firmware, or independent peer review.
