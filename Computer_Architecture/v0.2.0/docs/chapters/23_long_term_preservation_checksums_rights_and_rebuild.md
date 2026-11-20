# 23. Offline preservation: exact revisions, rights, sources, and reproducible builds

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Offline preservation: exact revisions, rights, sources, and reproducible builds. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

Scientific and engineering continuity requires preservation at multiple layers. Original authored code, exact record revisions, relationship endpoints, source cards, historical tests, offline artifacts and rebuild scripts must remain available as one coherent graph. A direct incremental release may be much smaller than its predecessor, but its restoration depends on the exact predecessor archive; periodically retained full archives and redundant storage are necessary to avoid brittle dependence on a long delta chain. All target files should be SHA-256 verified and a deterministic full ZIP should be reconstructed byte-for-byte, then extracted into a fresh environment where tests run again.

SHA-256 is a data-integrity mechanism, not evidence of technical validity, licensing, provenance truth or original publisher source authenticity. Bibliographic URLs should remain explicitly unverified until authenticated original bytes with edition, rights and page/equation locations are captured. Independent reviews and measured hardware traces should be separate signed records, not overwritten into existing test receipts. The original 30-domain roadmap must remain unmodified, and this new Computer Architecture node must be labeled an auxiliary enabling domain. ATLAS FORGE's planned Bitwork router remains downstream of scientific content completion.

## Executable contract and invariants

**Governing statement:** `SHA256(restored_full_archive)==SHA256(expected_release_archive) AND immutable_prior_revisions`.

**Implementation:** `ATLAS FORGE common.registry, file manifests, incremental restore and full regression`.

**Relevant dimensions:** bytes, file hashes, revision identifiers. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Restore the exact Manufacturing v0.2.0 archive, apply the new computer patch, verify every file and replay all historical and new tests from a clean extraction.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Archive integrity does not establish scientific truth, secure supply chains or real hardware reproducibility.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `RISCV-MANUAL`, official pointer: https://github.com/riscv/riscv-isa-manual. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
