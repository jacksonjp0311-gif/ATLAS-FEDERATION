# 33. Precise traps, finite watchdog budgets and deterministic I/O tapes

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

A reproducible computer requires failure semantics as carefully defined as success semantics. If an input port is exhausted, an instruction is illegal, a branch address is misaligned, or a program counter falls beyond ROM, a model must report a trap with the responsible PC before committing side effects. A watchdog step budget is another explicit stop condition, distinct from HALT.

## Technical derivation and invariants

Define `Snapshot(S)` as architectural state. A failed instruction should satisfy `Snapshot_after_trap = Snapshot_before_instruction`; this preserves precisely observable state so a debugger or recovery process can diagnose without guessing which writes occurred. A loop stopped due to a testing budget is not automatically a program that cannot terminate under another input or budget.

## Executable method and reproduction requirements

The new trace audit includes ROM hash, ordered retired PC and instruction events, aggregate event hash, halted flag and any explicit trap. Input tapes are finite port-indexed byte sequences and output is an ordered list of (port,byte) pairs, independent of host terminal devices. Test bounded loops, insufficient input, replay determinism and invalid metadata.

## Constructed investigation

`IN R0,1; HALT` with an empty port1 tape traps with input_exhausted without incrementing port cursor. `L: JMP L` with step limit=10 returns a bounded unfinished trace instead of an infinite tool call. Altering a ROM byte changes its digest even if a finite output is coincidentally unchanged.

## Counterexamples, scientific limits and missing evidence

Software traps cannot protect against physical power loss, clock-domain crossing, cache errors or all timing faults. A future OS and interrupt node must add privilege and device exception semantics; the educational AT8 v0.1 ISA deliberately lacks them.

## Source and dependency ledger

**Primary orientation:** `RISCV-MANUAL` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.
