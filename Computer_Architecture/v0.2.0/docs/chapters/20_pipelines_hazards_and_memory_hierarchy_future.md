# 20. Pipelines, dependencies, caches and memory hierarchy: research extensions

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Pipelines, dependencies, caches and memory hierarchy: research extensions. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A four-phase symbolic microsequence is not an instruction pipeline. Real pipelining overlaps the stages of several instructions, introducing hazards: data dependencies between reads and writes, branch/control dependencies, structural competition for hardware resources, and exception-ordering constraints. A pipeline may need forwarding, stalls, flushes, scoreboarding and precise commits. Likewise caches and virtual memory require explicit tags, replacement/eviction rules, dirty-state handling, coherence, translation and consistency semantics. AT8 v0.1 does not implement any of these mechanisms; its instructions commit sequentially in program order, and ROM and RAM access are idealized instantaneous logical operations.

The advantage of preserving a simple sequential architectural reference is that it can later serve as a correctness oracle for a pipelined implementation: every retired instruction must produce the same architectural state as the sequential model under the declared memory/IO semantics. This is differential verification, not an automatic performance model. The ATLAS FORGE roadmap should evolve this work toward a pipeline only after the base ISA is stable and supported by independent tests and circuit timing evidence. A speculative implementation that returns the right output for one program is not enough to prove ordering or precise traps.

## Executable contract and invariants

**Governing statement:** `forall retired instruction k: state_pipeline(k)==state_sequential_AT8(k) [FUTURE REQUIREMENT]`.

**Implementation:** `Future pipeline/register-transfer-level reference, explicitly not implemented`.

**Relevant dimensions:** clock cycles, bytes, access latencies (future). Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Describe a LOAD followed by ADDI using the loaded register and identify a true read-after-write dependency. Sequential AT8 needs no forwarding; a hypothetical pipeline might.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Do not report instruction-per-cycle throughput, cache hit rate or silicon speed without an actual implementation and measured workload.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-65900-2026`, official pointer: https://csg.csail.mit.edu/6.5900/lecnotes.html. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
