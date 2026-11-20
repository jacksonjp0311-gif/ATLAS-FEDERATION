# 01. Architecture, microarchitecture, and reconstruction contracts

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Architecture, microarchitecture, and reconstruction contracts. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A computer architecture is a contract for externally observable computation. An instruction-set architecture (ISA) specifies the bits in instructions, the machine-visible state, how instructions transform that state, how memory and devices are addressed, and when execution faults. A microarchitecture implements that contract with datapaths, control, storage and timing. Distinguishing these layers is essential: an architecturally correct emulator does not establish that a physical processor was fabricated, and a fabricated logic circuit does not automatically implement the promised ISA. The AT8 reference intentionally has one small immutable ROM, four 8-bit general-purpose registers, 256 8-bit RAM cells, four abstract ports and a 2-byte fixed instruction format. All memory and register values are reset to zero. The reference model defines exact deterministic state transitions. A second four-phase implementation interprets the same binary words using an alternative control decomposition. A third independent reference validates the instruction results. These are three useful *software* evidence streams but not three independent silicon implementations.

A complete reconstruction chain proceeds from electrical gates through register cells, interconnect and timing into a CPU datapath, then firmware/assembler, memory interfaces, boot, and an executing program. AT8 implements only the digital semantic middle layer in Python. Its material, timing, transistor and packaging dependencies are typed cross-links to the existing Electronics and Manufacturing nodes, whose physical evidence gaps remain open.

## Executable contract and invariants

**Governing statement:** `S_(t+1)=ISA_step(S_t, instruction_at_PC); implementation != architectural specification`.

**Implementation:** `computer_atlas.spec.SpecMachine and computer_atlas.microcoded.MicrocodedMachine`.

**Relevant dimensions:** bits, bytes, finite state. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Compare the same ROM on both machines, checking PC, all four registers, 256 RAM bytes, flags, output tape and input cursor after every committed instruction.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

An ISA can be mathematically coherent while a circuit fails setup/hold, overheats, or never passes a wafer test; do not promote executable Python into a fabricated hardware claim.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
