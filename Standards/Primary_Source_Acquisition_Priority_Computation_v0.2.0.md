# ATLAS FORGE — Computation primary-source preservation plan, v0.2.0

**Date:** November 14, 2026. **Research mandate:** design the knowledge collection for a future reader who cannot reach the original website, publisher, author or cloud model. **Current limitation:** 396 source cards, zero original primary-source files authenticated by the strict on-disk provenance audit.

## Preserve first the information that cannot be reconstructed from an algorithm summary

Every scientific claim should distinguish original observation, derivation, author's new explanatory synthesis, copied source, and unresolved hypothesis. A rights-checked source accession packet contains: publisher/author, stable identifier and exact release edition, license evidence, acquisition timestamp, URL and redirect chain, SHA-256 of unchanged source bytes, separate SHA-256 of any transformed derivative, exact inspected page/section, correction/errata status, and a note explaining which claim depends on the source. The source file and its license should be stored adjacent to machine-readable metadata. A hash verifies only byte consistency relative to an expected digest; it cannot prove publisher identity or the scientific accuracy of an article.

For **Computation Atlas v0.2.0**, prioritize the following accessions.

| Priority | Material | Rights and integrity action | Knowledge at risk if absent |
|---|---|---|---|
| 1 | NIST Dictionary of Algorithms and Data Structures | Confirm source publication edition, embedded third-party contributions, reusable rights, then retain official original bytes with SHA-256 | Precise historical definition and algorithm taxonomy |
| 2 | Author-site *Open Data Structures*, Pat Morin | Verify the author-site CC BY edition's license and attribution. Do not assume the differently licensed Athabasca University Press edition has identical rights | Full worked data structures and algorithm proofs |
| 3 | MIT OCW 6.006 and 6.046J | Preserve release-specific PDFs only with applicable OCW license, attribution and terms | Foundational lectures, advanced graph/FFT/complexity source material |
| 4 | MIT OCW 18.06 | Verify course PDF/source terms and edition, preserve the syllabus/notes that support the cited linear algebra statement | Exact matrix and elimination educational provenance |
| 5 | Python documentation and SciPy reference | Acquire source-controlled documentation at a pinned commit and include PSF/SciPy license notices | Reproducibility of numeric API behavior and known implementation limits |
| 6 | Lamport 1978 paper | Original ACM copyright; follow author-hosted and publisher permissions before mirroring | Historical primary argument for logical clocks and partial-order concurrency |
| 7 | AWS Builders Library idempotency article | Retain permitted bibliographic notes now; archive full copyrighted article only if publication rights permit | Practical treatment of provider-side deduplication and lost acknowledgments |
| 8 | NIST FIPS 203 | Verify current standard edition and errata sheet, applicable government-publication rights, archive exact official standard with provenance | Post-quantum terminology and algorithm parameters, not their secure implementation |

## Evidence-grade transition rules

- **L0:** bibliographic locator. A functioning link is not an offline primary source.
- **L1:** limited, attributed source context and original explanatory synthesis. The present v0.2 package is generally L0/L1 for external references.
- **L2:** original bytes retained under documented rights, provenance and fixity. Promote only when both source file and metadata are physically present and reproducibly verified.
- **L3:** independently rerun a stated analysis against authentic source data, with original data, transformation script and discrepancy report. Passing synthetic unit tests does **not** confer L3.
- **L4:** separately performed scientific corroboration or expert methodological review with source-linked acceptance; a citation count or independent software library agreement is insufficient.

## Reconstructibility checks before v1 content graduation

A future user with **no internet** should be able to read the mathematical definition and its assumptions; independently derive a small example by hand; execute or rewrite the reference method in a documented language; find every claimed original source byte or an explicit documented absence; see contradictory results and known errors; and identify which statement was *proved conditionally*, *tested on finite inputs*, or *measured empirically*. No equation should be separated from variables, units, preconditions and counterexamples. Optional optimized indexes should not be required to read the source documents.

## Long-term source storage and continuity

A full-version archive, standalone domain bundle, manifest and release receipt should be stored as immutable snapshots with separate SHA256 values and periodic restore drills. At least three geographically or administratively independent storage copies are a **future requirement**, not a completed activity. Do not rely on a single Library account as disaster recovery. The user-directed sequence is to finish all 30 scientific domain libraries, then implement and independently evaluate Bitwork-powered cross-domain routing, and transfer only the integrated tested collection to the desktop.

## This edition's honest boundary

The generated Computation v0.2 package contains 50 original explanatory chapters, 26 constructed casebook investigations, 232 records and offline mathematical code. It has no externally authenticated original article/PDF source bytes, no independent physicist/mathematician review, and no live AI-performance benchmark. Its internal source closure, software tests and exact historical revisions are necessary preservation properties but cannot satisfy the broader survival claim by themselves.
