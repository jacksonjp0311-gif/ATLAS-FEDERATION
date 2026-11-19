# 22 — Independent acceptance gates, restoration and preservation

**Scientific question.** How can new network science be added without rewriting the original ATLAS?

## Definitions, physical assumptions and scope

Each node uses the unchanged atlas.common/1 schema with concepts, claims, equations, methods, datasets, sources, reviews and exact relations. New records are sealed with immutable canonical SHA-256 revisions. Historic records/graphs and the original 30-domain queue are preserved.

## Governing principle and derivation

A canonical incremental patch from predecessor B to target T contains only changed/new members. For each file f, SHA256(content_source[f]) must equal SHA256(content_restored[f]); both complete source and fresh tests must be replayed with byte-identical receipts.

**Equation / invariant:** `∀f∈T SHA256(source_f)=SHA256(restored_f); sha256(ZIP_source)=sha256(ZIP_restored)`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

If 10,629 prior source files exist, all must remain present after addition. Only explicitly authorized integration metadata may change, and no prior scientific data file is silently revised.

## Reconstructible offline procedure

Validate registry, manifest and exact relations; run domain oracles; run all historic regression suites with frozen predecessor assertions; build direct patch, reconstruct independently and compare the two complete receipts before advancing the Library checkpoint.

## Independent test or negative control

Any failed historical test, unauthorized old file hash drift, mismatched deterministic ZIP, missing Library readback, or unsupported claim must keep the prior checkpoint authoritative.

## Known failures, uncertainty and acceptance gates

Software-content release is not wire interoperability, accredited peer review, physical-power testing or authenticated original publisher preservation.

## Source pointers (not authenticated publisher files)

- RFC9293: Transmission Control Protocol (TCP) (August 2022 (obsoletes RFC 793)), https://www.rfc-editor.org/info/rfc9293/
- RFC9846: The Transport Layer Security (TLS) Protocol Version 1.3 (July 2026 (obsoletes RFC 8446)), https://www.rfc-editor.org/info/rfc9846/

**Exact predecessor dependencies:** software-design-patterns-atlas, distributed-systems-atlas, os-internals-atlas. See immutable relation revisions in `data/relations.jsonl`.

