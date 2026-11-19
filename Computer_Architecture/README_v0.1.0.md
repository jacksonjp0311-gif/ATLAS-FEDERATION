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
