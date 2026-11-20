# Chapter 33 — Preservation-grade software and scientific reconstruction

**Domain:** Methodology. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A preservation library must remain understandable when the original cloud services, package managers, websites, and author are gone. Store human-readable algorithms and proofs beside machine-executable reference programs. Record exact source and dataset bytes when legally permitted, cryptographic file hashes, licensing, encoding, source versions, and transformation histories. Preserve compilers and interpreters where licensing and storage permit, but do not make them the only way to understand the theory. Explicitly state which results are exact math, which are synthetic experiments, which are empirical reproductions, and which have independent human review. Redundant copies stored in separate failure domains improve survivability but must be tested with actual restoration drills.

## Formal statement, symbols, and units

Integrity: SHA256(file_bytes)=expected_hash. Authenticity requires a trusted signature/channel; scientific validity requires independent evidence. These three propositions are not equivalent.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

A content hash detects a changed file only when the expected hash is obtained from a trusted earlier record. If both payload and expected hash are replaced together, hashing alone does not authenticate the original publisher. A link-only source card is useful navigation today but cannot reconstruct the primary document after network loss. A survival ledger should therefore count original source bytes separately from source citations and provide an acquisition plan. A fully replayed ZIP test supports software restorability, but not all dependency or platform portability.

## Reconstruction exercise with independently checkable output

Disconnect the network, extract the collection to a new directory, verify file inventory, run tests, open markdown chapters, execute the casebook, and inspect the original-source ledger. Repeat on distinct hardware when available. Record any dependency requiring a missing wheel, key, or remote service.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not advertise an archive as containing “all of humanity's knowledge.” Scope is necessarily finite. Structural test counts and locally written explanations cannot replace original scientific measurements, expert review, archival rights clearance, or geographic redundancy.

## Source orientation

- NIST FIPS 180-4 Secure Hash Standard: https://csrc.nist.gov/pubs/fips/180-4/upd1/final
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
