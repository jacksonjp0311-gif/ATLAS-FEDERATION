# 29. Reproducible source-to-ROM builds, content hashes and provenance

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

Reconstruction requires more than running a program once. The source text, compiler version, ISA specification, exact ROM bytes, input tape and output trace must have stable, separately verifiable identities. An archival manifest can contain SHA-256 of source UTF-8 and ROM bytes, along with a schema version and known source-to-execution mapping. This makes later corruption or accidental code drift detectable, assuming the manifest itself is retained through a trusted route.

## Technical derivation and invariants

A reproducible build statement is `H(C(S)) == H(rom_reference)` for the exact compiler/assembler release, source S, and byte representation. If the input language treats whitespace/comments differently, hashing original text is distinct from hashing a normalized AST; the receipt must state which is used. A SHA-256 collision is not assumed computationally practical, but a content hash alone does not authenticate the publisher or prove program correctness.

## Executable method and reproduction requirements

`compile_receipt` produces source and ROM hashes and source evaluator output, explicitly tagged as constructed software evidence. The full federation packer should independently archive deterministic source, test outcome receipts, SHA-256 file manifests and a direct restoration path. A clean process must re-run compiler, interpreter and machine-model tests without hidden cloud components.

## Constructed investigation

For source `SET 5; ADD 7; HALT`, compare `compile_source` results across fresh processes. The digest must be reproducible; a single literal change from ADD 7 to ADD 8 changes ROM bytes and the recorded hash. A manually edited ROM should fail the expected-manifest digest even when some observed output remains equal.

## Counterexamples, scientific limits and missing evidence

Hash mismatch may be accidental or adversarial; hash equality cannot establish physical execution, editorial correctness, science acceptance or license compliance. The human provenance and original publisher documents remain separate evidence categories.

## Source and dependency ledger

**Primary orientation:** `RISCV-MANUAL` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.
