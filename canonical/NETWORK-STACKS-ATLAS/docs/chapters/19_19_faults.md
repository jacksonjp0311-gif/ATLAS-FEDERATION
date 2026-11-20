# 19 — Fault injection, adversarial framing and transport evidence

**Scientific question.** What is required to test a stack that faces loss, corruption, reordering and duplication?

## Definitions, physical assumptions and scope

A network stack failure model must distinguish corruption, duplication, reordering, omission, delay, partition, power interruption and maliciously crafted syntax. Synthetic tests are bounded and cannot reproduce all concurrency, NIC and OS behavior.

## Governing principle and derivation

For n injected cases, finite pass fraction k/n is a test statistic and not a production reliability estimate without a representative sampling model and confidence intervals. Different oracles must not simply call the same parser.

**Equation / invariant:** `p_observed = k/n (constructed finite tests; not measured field reliability)`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

Run 100 seeded frames, then independently flip a checksum-protected byte, truncate framing, reorder packets and inject duplicate identifiers. Require each invalid category to fail for the intended reason.

## Reconstructible offline procedure

Preserve seeds, expected negative failure type, alternate oracle method, test output and exact source-hash receipts. Don’t equate a successful parser call with transport-layer confidentiality.

## Independent test or negative control

A malformed fragment that fails checksum before fragmentation rejection is NOT proof that fragmentation handling works; create a valid-checksum unsupported fragment negative control.

## Known failures, uncertainty and acceptance gates

No field fault injection, operating-system packet fuzzing, production security audits or live transport simulation.

## Source pointers (not authenticated publisher files)

- RFC791: Internet Protocol, IPv4 (September 1981), https://www.rfc-editor.org/info/rfc791/
- RFC8200: Internet Protocol, Version 6 (IPv6) Specification (July 2017 (updated by RFC 9673)), https://www.rfc-editor.org/info/rfc8200/
- RFC9293: Transmission Control Protocol (TCP) (August 2022 (obsoletes RFC 793)), https://www.rfc-editor.org/info/rfc9293/

**Exact predecessor dependencies:** software-design-patterns-atlas, distributed-systems-atlas. See immutable relation revisions in `data/relations.jsonl`.

