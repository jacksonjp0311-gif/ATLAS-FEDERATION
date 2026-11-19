# 13. Reset vector, boot ROM, and immutable firmware checksums

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Reset vector, boot ROM, and immutable firmware checksums. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A computer's first useful operation depends on a reset path and a program image. AT8 uses a fixed reset vector PC=0 and explicitly initialized registers, RAM, flags, input cursors and output tape. Its ROM is an immutable byte string of even length, validated before execution. This allows an exact SHA-256 ROM identity to travel with a reference execution trace. A hash proves the recorded bytes match a particular receipt; it does not establish that the content is scientifically correct, safe, originally authored by a claimed person or lawfully redistributable.

Physical firmware storage introduces further dependencies: boot ROM fabrication or programmable nonvolatile memory, power-on reset timing, input pin stabilization, clock start, voltage supervision, byte ordering, memory interfaces and recovery if the image is corrupted. AT8 does not include secure boot or signatures. A production design would require a chain of trust and authenticated firmware update mechanism, but none is silently attributed to the present model. The offline ATLAS FORGE archive preserves both source assembly and exact ROM bytes so they can be independently regenerated.

## Executable contract and invariants

**Governing statement:** `boot_pc=0; reset_regs=(0,0,0,0); program_SHA256=SHA256(ROM_bytes)`.

**Implementation:** `computer_atlas.isa.validate_rom; computer_atlas.spec.SpecMachine`.

**Relevant dimensions:** ROM bytes, SHA-256 digest. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Assemble a six-instruction program, record the byte string and SHA-256, run it on two independent implementations, then compare ROM and execution-trace digests after fresh extraction.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Checksums are not digital signatures, attestation, or evidence of a working hardware root of trust.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
