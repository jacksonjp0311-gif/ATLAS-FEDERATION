# 01 — Layering, interface contracts and failure propagation

**Scientific question.** How can a broken wire-level claim be isolated across a layer boundary?

## Definitions, physical assumptions and scope

Distinguish physical signaling, link encapsulation, network forwarding, transport and application semantics. An accepted inner header is not proof of a valid outer frame or authenticated peer. MTU, retransmission and clock assumptions are cross-layer variables.

## Governing principle and derivation

If each of n independently validated layers can fail with probability p_i, an illustrative series-path reliability model is P(success)=product_i(1-p_i). This is not a measured reliability or an independence claim; shared faults invalidate the product. Preserve exact bytes, clocks and evidence provenance at each handoff.

**Equation / invariant:** `P_series = Π_i(1-p_i) [independent-layer illustrative model]`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

For constructed p=(0.01,0.02,0.03), P=0.99×0.98×0.97≈0.941094, not the arithmetic mean of layer successes.

## Reconstructible offline procedure

Start from a known cable/interface, separately verify link frames, IP headers, transport checksum/state, DNS resolution and application authentication. Label the layer whose invariant failed and do not promote the lower-layer result to upper-layer security.

## Independent test or negative control

A well-formed UDP length with corrupted payload is accepted by the length-only model; the correct conclusion is missing integrity coverage, not a reliable payload.

## Known failures, uncertainty and acceptance gates

No physical loss measurements, NIC firmware conformance, layer timing or wire interoperability.

## Source pointers (not authenticated publisher files)

- RFC894: Standard for the Transmission of IP Datagrams over Ethernet Networks (April 1984), https://www.rfc-editor.org/info/rfc894/
- RFC791: Internet Protocol, IPv4 (September 1981), https://www.rfc-editor.org/info/rfc791/
- RFC768: User Datagram Protocol (August 1980), https://www.rfc-editor.org/info/rfc768/

**Exact predecessor dependencies:** os-internals-atlas, computer-architecture-digital-hardware-atlas. See immutable relation revisions in `data/relations.jsonl`.

