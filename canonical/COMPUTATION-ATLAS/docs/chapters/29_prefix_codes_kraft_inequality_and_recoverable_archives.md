# Chapter 29 — Prefix codes, Kraft inequality, and recoverable archives

**Domain:** Information. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A prefix-free binary code has no codeword that begins another codeword. Such a code can be decoded greedily without explicit separators when the codebook is known. This does not by itself ensure efficient compression; code lengths should reflect symbol probabilities, and metadata overhead matters. Huffman coding produces an optimal binary prefix code for a specified finite symbol distribution under ordinary codeword-length cost, but not necessarily an optimal code under streaming, edit resilience, or CPU constraints. Archive survival depends on storing the codebook, version, bit ordering, and integrity metadata. A file that cannot be decoded without a vanished proprietary codec is not meaningfully preserved.

## Formal statement, symbols, and units

Kraft inequality: Σ_i 2^(−l_i)≤1 for a binary prefix code with lengths l_i. Average length L=Σ_i p_i l_i≥H(X).

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

A prefix-free code corresponds to leaves of a binary tree. A codeword of length l occupies 2^(−l) of the conceptual depth-infinite tree's capacity, and disjoint leaves cannot sum to more than one. Entropy provides a lower bound on expected code length, but finite codewords and integer lengths can introduce overhead. For survival archives, the decoder specification must be present in independent human-readable form.

## Reconstruction exercise with independently checkable output

Check that [0,10,11] is prefix-free and [0,01] is not. Compute Kraft sums, then describe how a bitstream of symbols can be decoded by walking a binary tree. Record the exact code assignment with the archive.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Checksums detect accidental corruption under assumptions, but do not correct it; parity or error-correcting codes serve a different purpose. Compression is not encryption and not provenance authentication.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- Pat Morin, Open Data Structures: https://www.opendatastructures.org/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
