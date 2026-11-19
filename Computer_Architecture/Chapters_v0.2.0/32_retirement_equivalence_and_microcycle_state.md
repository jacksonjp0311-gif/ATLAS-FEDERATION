# 32. Instruction retirement, staged side effects and differential machine execution

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

Correctness at the ISA boundary is defined by architecturally visible state: PC, registers, RAM, flags, I/O events, consumed input indices and halt/trap status. A microarchitecture may use many hidden control stages but must not expose a half-committed instruction. This creates an important testable separation between the **ISA reference** and an independently implemented four-stage FETCH–DECODE–EXECUTE–COMMIT model.

## Technical derivation and invariants

Let S_n be architectural state after retiring n instructions. For a valid instruction i, `SpecStep(S_n,i)=MicroRetire(S_n,i)` is the key bisimulation-style finite condition. A trapped instruction should not partially commit registers, RAM or input/output state. Non-retired microstage latches are intentionally not part of S_n; they are implementation detail. The two software models can share a specification but must not share the same execution routine.

## Executable method and reproduction requirements

`differential_retirement` advances both models, compares the entire snapshot after each retirement and records deterministic events with state SHA-256. An input exhaustion trap or illegal ROM branch is audited as a stopped computation, not silently turned into HALT. A bounded step budget prevents endless monitoring of loops.

## Constructed investigation

For the arithmetic program `LDI R0,5; ADDI R0,7; STORE R0,0; XORI R0,3; OUT R0,0; HALT`, both models leave RAM[0]=12, R0=15 and output event (port0,15). A broken microcycle implementation that increments the input cursor in DECODE instead of COMMIT would diverge when the input is exhausted.

## Counterexamples, scientific limits and missing evidence

Execution trace hashes establish reproducibility under exact software versions and inputs, not whether a silicon CPU clocked through these phases or whether real signals obey setup/hold. Exact physical timing requires device characterization, clock tree, power and memory-system evidence.

## Source and dependency ledger

**Primary orientation:** `MIT-6004` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.
