# 21. Architectural invariants, refinement obligations, and finite exhaustive testing

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Architectural invariants, refinement obligations, and finite exhaustive testing. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A rigorous design must have invariants that survive every valid state transition. In AT8, registers and RAM remain bytes, PC is always aligned when an instruction can be fetched, ROM bytes never change, outputs are port-index/byte tuples, and COMMIT is the only architectural visibility boundary. For a valid branch, the target must lie inside ROM; for a normal instruction, PC increments by exactly two. Every illegal or resource-exhausted instruction must trap without partial architectural mutation. These properties are asserted in unit tests and deterministic oracle reports.

This edition does not contain a mechanized theorem prover proof or model-check all 2^(2048) RAM states. The word “formal” here identifies logical contracts and the possibility of future refinement proofs, not completed formal verification. Exhaustive testing of the 8-bit ALU input space and bounded random programs gives useful finite coverage; it is not universal proof for arbitrary ROM contents. A future verifier should model AT8 in a separate theorem prover, establish inductive invariants, and compare any hardware netlist/RTL with the reference on all reachable states under explicit environmental assumptions.

## Executable contract and invariants

**Governing statement:** `invariant: regs, RAM ∈ Byte; PC mod 2=0; ROM_after=ROM_before; commit_effects_only`.

**Implementation:** `computer_atlas.isa.validate_rom; tests/test_spec.py; evidence/independent_oracle.py`.

**Relevant dimensions:** Boolean predicates, finite state counts. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Force invalid ROM operands, empty input tapes and fall-through PC; verify explicit rejections and no earlier committed data loss. Check all 256×256 adder pairs.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

No machine-checked proof certificate or externally reviewed formal equivalence result exists in this release.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `RISCV-MANUAL`, official pointer: https://github.com/riscv/riscv-isa-manual. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
