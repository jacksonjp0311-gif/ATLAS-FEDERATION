# 21 — Security boundaries, provenance and trust anchors

**Scientific question.** Why must protocol conformance be treated separately from cryptographic security?

## Definitions, physical assumptions and scope

Correct frame length, checksum and syntax mean only specified structural requirements held. None authenticate an IP/ARP sender, DNS server, route advertisement or upper-layer transaction. An offline scientific reader must preserve these negative qualifiers with every retrieved method.

## Governing principle and derivation

The condition data_accepted requires parser_valid AND required authenticated-origin checks AND replay policy AND state authorization. Without a required check, the application must abstain or label unauthenticated.

**Equation / invariant:** `auth_accepted ⇒ syntax_valid ∧ origin_trusted ∧ replay_accepted ∧ policy_allowed`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

A forged UDP datagram may have a correct UDP checksum; in this case the checksum model should return true but the application authenticity verdict is unknown/false.

## Reconstructible offline procedure

Carry exact record revisions and upstream source/rights labels through evidence retrieval; compare independent cryptographic primitives with published vectors before real integration.

## Independent test or negative control

Calling a validated IP checksum an authenticated packet is the negative control. Reject this evidence promotion as a category error.

## Known failures, uncertainty and acceptance gates

No production authentication, TLS interoperability, remote trust or independent security certification.

## Source pointers (not authenticated publisher files)

- RFC9846: The Transport Layer Security (TLS) Protocol Version 1.3 (July 2026 (obsoletes RFC 8446)), https://www.rfc-editor.org/info/rfc9846/
- RFC4033: DNS Security Introduction and Requirements (March 2005), https://www.rfc-editor.org/info/rfc4033/
- RFC9000: QUIC: A UDP-Based Multiplexed and Secure Transport (May 2021), https://www.rfc-editor.org/info/rfc9000/

**Exact predecessor dependencies:** cryptographic-protocols-atlas, software-design-patterns-atlas. See immutable relation revisions in `data/relations.jsonl`.

