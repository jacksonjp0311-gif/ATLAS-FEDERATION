# Chapter 60 — Reconstructible computing runtime: what still separates AT8 from a general machine

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Technological continuity is a chain, not a single file
An independently reconstructible machine requires an end-to-end dependency graph. Starting from material science and electrical calibration, a manufacturer must produce reliable transistors and memory, combine them into gates and sequential logic, implement a verified ISA, provide a source-to-ROM build chain, and execute bounded diagnostic programs. An operating system introduces interrupts, processes, persistent storage, isolation and resource scheduling. An AI runtime additionally needs numeric kernels, model serialization, memory management, evaluation datasets and power/thermal controls.

AT8 currently provides a small original educational ISA, a constrained compiler, a boot-image format, atomic/microcycle reference models, software cache/bus simulations, arithmetic netlist proofs and reproducibility receipts. None of these implement a physical CPU, robust operating system, instruction pipeline with characterized hazards, memory protection or general model inference. The architecture must remain clear on exactly which link of the reconstruction chain each artifact verifies.

## Finite vertical slice
Take a bounded structured program, compile it to a fixed two-byte AT8 ROM, roundtrip its canonical assembly, encode and decode a versioned boot image, run it under independent source/ISA/microcycle models, check every ADDI/CMP against explicit NAND gates, and produce a deterministic receipt. Verify the output byte trace and RAM SHA-256. In a parallel manufacturing-evidence graph, mark all physical stages as HOLD until actual calibrated measurements are supplied.

## Next scope
The next iteration toward Computer Architecture scoped v1 should develop an independent gate/register-transfer implementation and documented synthesizable HDL, an assembler/linker and minimal boot/test runtime, bounded error handling, formal state invariants, simulation against external references, and hardware measurement acquisition. Only then should a human claim working physical reconstruction. ATLAS FORGE continues as one versioned federation; the original thirty-domain roadmap remains unmodified, and Bitwork routing follows completion of domain knowledge.

## Equation, implementation, and provenance

- **Key relation:** `scientific equations -> fabricated gates -> working memory -> ISA -> tools -> runtime -> AI workload`.
- **Reference algorithm:** `v04_bootstrap.bootstrap_certificate; v04_memory.HarvardBus`.
- **Units:** program bytes, states, timestamps, source evidence and calibrated instruments.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
