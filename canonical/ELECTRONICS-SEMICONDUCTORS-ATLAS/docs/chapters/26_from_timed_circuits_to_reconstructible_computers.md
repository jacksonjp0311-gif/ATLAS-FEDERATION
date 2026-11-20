# Chapter 26: Evidence-driven handoff to computer architecture

**ATLAS FORGE / original canonical 13-node federation — Electronics & Semiconductors v0.3.0**

**Evidence status:** original educational/engineering synthesis and finite constructed software tests. No publisher-original file authentication, independent scientific review, wafer process, device calibration, or functioning CPU is claimed.

## Objective
Place the preceding electronics knowledge into a specific reconstruction dependency chain. A binary full adder is not a CPU; a register is not a reliable clocked system; a digital simulator is not semiconductor fabrication evidence.

## Interface ledger
1. **Material and geometry prerequisites:** carrier concentration, mobility, doping profiles, dielectric permittivity, transistor geometry and process uncertainty come from Chemistry, Materials and future Manufacturing.
2. **Electrical primitives:** measured transistor I–V, capacitance, leakage, switching delays, voltage windows, power supply/load requirements and thermal behavior must be established experimentally before hardware signoff.
3. **Logical primitives:** NAND truth tables, XOR, adders, decoder/multiplexer and finite state semantics can be verified exhaustively on bounded designs.
4. **Sequential primitives:** setup/hold, propagation/contamination delays, clock skew, unknown states and synchronizer requirements must be specified; timing signoff requires measured or characterized values.
5. **Information integrity:** explicit data formats, error detection, error-correction limits, reset, watchdog behavior, and machine-checkable test vectors.
6. **Architecture handoff:** a separately versioned Computer Architecture Atlas defines datapaths, control states, an instruction set, memory maps, boot sequence, interrupt/error handling and a minimal test program.
7. **AI continuation:** only after an executable computer, compiler/runtime and reproducible model/inference are available should the federation assert an end-to-end AI reconstruction demonstration.

## Minimal bounded proof obligation
Demonstrate gate-level XOR and NAND-only full adder, four-bit ripple addition with correct carry, abstract state storage, and a timing-path audit. The v0.3 reference gives these numerical/test-vector components without claiming their fabrication. A prospective laboratory campaign should compare characterized voltage transfers, delays and power/temperature traces to reference models, preserving raw data and uncertainty budgets.

## Scientific evidence boundary
ATLAS FORGE's new chapter is original synthesis with verifiable finite software tests and bibliographic pointers, not a rights-cleared archive of MIT publications or independent hardware expert certification. Keep the original 30-domain queue unchanged, complete content libraries first, Bitwork routing afterward, integrated validation and desktop transfer last.

## Reference implementation and source accountability
- **Executable kernel:** `electronics_atlas/v03_models.py` — `reconstruction dependency matrix`.
- **Equation/invariant:** `physical→logic→registers→architecture→compiler→AI runtime`.
- **Units:** SI units and binary abstractions.
- **Historical dependency:** Chapters 1–18 of the same Electronics node and Mathematics/Physics reference; unchanged historical release snapshots preserved.
- **Bibliography:** MIT OpenCourseWare 6.004 computation structures, course index and timing notes, *navigational reference only*. No complete authenticated publisher PDF or license clearance for republishing course material is represented.
- **Evidence:** local v0.3 tests; independently assembled finite NumPy/integer oracle. Calibration and expert review remain separately outstanding.
