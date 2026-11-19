# 14 — DNSSEC trust anchors and limits of name resolution

**Scientific question.** Why does a correct DNS wire parser not establish authentic name-to-address data?

## Definitions, physical assumptions and scope

DNSSEC defines authentication of DNS data via digital signatures and a chain of trust to configured trust anchors. A response with correct packet structure can be spoofed; DNSSEC success depends on key algorithms, rollover, time validation and authenticated trust anchor management.

## Governing principle and derivation

Logical chain: verified RRset signature AND verified DNSKEY chain AND valid trust-anchor path AND acceptable validity interval. Absence of one condition does not prove another. An offline parse is a syntax check only.

**Equation / invariant:** `DNSSEC_accepted ⇒ signature_valid ∧ trusted_chain ∧ time_valid`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

A constructed DNS A record returning 192.0.2.3 with no RRSIG is syntactically possible but cannot be promoted to DNSSEC-authenticated data.

## Reconstructible offline procedure

Preserve DNS response bytes, key IDs, algorithms, anchor edition, clock evidence and negative trust outcomes. Use an independently reviewed DNSSEC implementation for actual validation.

## Independent test or negative control

A syntactically correct answer with forged data and no trusted chain must remain unauthenticated rather than being accepted by the parser.

## Known failures, uncertainty and acceptance gates

No DNSSEC crypto implementation, resolver behavior, authenticated original publisher key material or trust-anchor lifecycle testing.

## Source pointers (not authenticated publisher files)

- RFC4033: DNS Security Introduction and Requirements (March 2005), https://www.rfc-editor.org/info/rfc4033/
- RFC1035: Domain Names: Implementation and Specification (November 1987), https://www.rfc-editor.org/info/rfc1035/

**Exact predecessor dependencies:** cryptographic-protocols-atlas, os-internals-atlas. See immutable relation revisions in `data/relations.jsonl`.

