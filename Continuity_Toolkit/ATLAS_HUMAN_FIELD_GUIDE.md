# ATLAS FORGE — The human continuity field guide

**Original canonical scientific federation · Computer Architecture v0.5.0 Continuity Edition**

> Preserve the ability to understand, challenge, and reconstruct technology. Preserve **failure evidence** alongside successes. Do not claim that documentation can replace measurements or expert oversight.

## What this artifact is

This release is one descendant of the original ATLAS FORGE chain, not a fork or replacement archive. It retains every prior scientific node and the unchanged original thirty-domain queue. No network, cloud model, or vendor login is required to open the bundled original documents or use the elementary recovery reader.

Its source corpus comprises **15 federated nodes**, **3,235 exact-revision scientific records**, **2,415 qualified relationships**, and **547 bibliographic source cards**. The 60-chapter Computer Architecture manual, 52-chapter Electronics manual, and 30-chapter Manufacturing manual illustrate the cross-disciplinary intent. The full collection contains much more than those three nodes.

Only **9 of the original 30 planned domain IDs** currently have registered nodes (with six additional scientific/enabling nodes), and node presence does not equal completed scientific acceptance. The frozen original queue still labels Manufacturing as queued even though its node exists; the live priority overlay corrects the active status without editing history. This is **not** a complete atlas of all human knowledge or all thirty planned domain libraries. The contents do not demonstrate fabricated silicon, an independently reproduced machine, source-original publication authentication, security against archive tampering by an adversary possessing the release manifest, or peer-reviewed science for the entire federation.

## The reconstruction ladder

| Layer | What you can inspect | Evidence currently available | Missing evidence |
|---|---|---|---|
| 1. Mathematics, units and measurement | Equations, dimensions, numerical tests, metrology protocols | Reference proofs and finite tests | Independent scientific review, authentic complete publisher originals and calibration |
| 2. Materials and chemistry | Properties, reaction/microstructure dependencies | Source-linked records and mathematical cases | Physical sample identity, raw process measurements, uncertainty controls |
| 3. Electronics and semiconductor devices | Diode/MOSFET and RC models, logic, timing, memory | Bounded executable reference models | Measured transistors, process corner models, timing and device reliability |
| 4. Manufacturing | Tolerances, traceability, process plans, evidence gates | Deterministic models and gate-aware casebook | Qualified machines, real physical samples, inspected builds |
| 5. Digital computer | AT8 ISA, assembly, ROM boot recovery, NAND arithmetic | Multiple execution models, test vectors and hashes | Real gates/clock/memory, hardware secure boot, fabricated CPU |
| 6. Compiler, OS and AI | Tooling prerequisites and research workflows | Partial reusable references | Full self-hosting compiler, OS, verified model runtime, benchmarked agent improvement |

## What 'verified' means in this library

- **Byte integrity:** a record or file matches the SHA-256 digest in its trusted manifest. This cannot establish that the content is true, rights-cleared, or safe.
- **Exact revision:** record content and relations have checked immutable revision digests, and relation references must match their exact record revision.
- **Numerical oracle:** another computation agrees on the stated bounded synthetic inputs, not on every possible physical state.
- **Reconstruction challenge:** a fixed software exercise reproduces the source→assembler→boot→execution result. It demonstrates software consistency, **not** fabricated electronics.
- **Scientific verification:** requires original sources, expert review, instrument calibration, real-world observations, and acknowledged counterexamples. This broader acceptance is not yet demonstrated.

## How to use it without dependency on an AI

With a browser, open `SURVIVAL/ATLAS_OFFLINE_PORTAL.html`. Its search works locally with no remote scripts or services. With Python 3.10+ available:

```bash
python tools/atlas_offline.py catalog
python tools/atlas_offline.py search "MOS transistor carrier transport" --limit 10
python tools/atlas_offline.py trace computer-architecture-digital-hardware-atlas:chapter-60-method --depth 2
python tools/atlas_offline.py gaps
python tools/atlas_offline.py audit
python tools/atlas_offline.py challenge
```

The `search` command ranks literal term matches. It is not an AI inference service, has no adaptive routing, and does not score truth. The `trace` command follows only stored, exact-revision relationships; it does not infer new scientific dependencies. The `gaps` command reports missing evidence, not scientific verdicts.

## Human reconstruction challenge: three levels

1. **Offline archive challenge:** open this archive on a clean, disconnected computer and verify its root manifest, node manifests, and record revisions; reproduce the catalog without any remote resource.
2. **Mathematical/computational challenge:** execute the bundled AT8 example `SET 5; ADD 7; STORE 0; XOR 3; OUT 0; HALT` and independently confirm output `15`. Verify that the ROM checksum and NAND netlist hashes match the preserved receipts. Test invalid ROM and injected parity faults.
3. **Physical challenge:** design, manufacture, instrument and independently evaluate an electronic circuit or processor that reproduces an approved subset of AT8. This requires responsible lab engineering, qualified reviewers and documented calibrated measurements. The current edition **does not** include this evidence.

## How to preserve it

For disaster recovery, retain complete archive pieces, their verification manifest, restore script, at least one offline human-readable printed guide, and one unmodified copy of the original release chain. Store independent redundant copies with controlled access and rights review. Test restoration periodically on a clean device before depending on a copy.

No single storage technology guarantees permanence. SHA-256 is a corruption detector when its expected digest is obtained independently from a trusted source. A corrupted archive paired with an attacker-modified manifest can still appear internally consistent.

## What the next stewards should do

Independently authenticate publisher originals, perform source-to-equation reviews, validate physical materials and electronic models, construct and test hardware, add compiler and OS reconstruction nodes, grow the remaining original domains, and retain every negative result. Publish corrections as append-only new versions, not silent rewriting of old evidence.

**The original thirty-domain queue is a commitment to unfinished work, not a completion badge. Bitwork routing remains deferred.**
