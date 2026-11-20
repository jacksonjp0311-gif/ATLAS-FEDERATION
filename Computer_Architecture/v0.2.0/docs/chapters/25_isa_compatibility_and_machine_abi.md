# 25. Preserving byte-exact AT8 semantics and an explicit programming contract

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

AT8-0.1 is two-byte fixed encoding [opcode|register, operand]. The new compiler MUST not reinterpret reserved low bits, register numbers or branch destinations. CPU architectural compatibility is defined by identical externally observable state transitions for every legal instruction, not merely programs that happen to halt. Four general registers are R0..R3, each an unsigned byte; ROM addresses are even and 0..254, and RAM addresses are byte indices 0..255.

## Technical derivation and invariants

For a program P with inputs I, define architectural trace T(P,I) as the sequence of committed (PC, register file, RAM changes, flags, output events) records. An ABI is a convention over this ISA: v0.2 structured programs use R0 as source-visible accumulator and R3, R2, R1 as compiler-reserved loop counters. The compiler must not clobber an active outer loop register. This is not a production calling convention and has no stack, heap or interrupt-safe preservation rules.

## Executable method and reproduction requirements

Keep `computer_atlas.isa.assemble`, `decode`, `SpecMachine` and `MicrocodedMachine` byte-identical to v0.1. The new `v02_bootstrap` compiler emits only those instructions and refuses more than 128 encoded instructions. Negative controls should reject invalid register encodings, unsupported ISA opcodes, odd branch addresses, missing HALT and ambiguous memory semantics.

## Constructed investigation

Compile `SET 5; ADD 7; STORE 4; XOR 3; OUT 0; HALT` (one statement per line). The encoded program executes on the unmodified AT8 and leaves RAM[4]=12, R0=15, and output port 0 emits 15. Re-running with a second execution engine must produce the same architectural state.

## Counterexamples, scientific limits and missing evidence

This contract does not establish a stack ABI, binary executable format, linker, interrupts, privilege modes or hardware pipeline. Its deliberately limited conventions preserve a testable bootstrap, not a general OS ABI.

## Source and dependency ledger

**Primary orientation:** `MIT-6004` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.
