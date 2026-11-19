# 08 — Anti-replay windows and authenticated sequence numbers

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How does a receiver accept bounded out-of-order authentic traffic while rejecting duplicates and stale records?

## Threat model, prerequisites and assumptions

A receiver tracks high watermark h and a width-w bitmap. Authenticate the complete message before changing replay state; state can roll back after a crash unless durably persisted. A replay window is not meaningful without authenticating the sequence number.

## Governing formalism

`On seq s>h: bitmap←((bitmap << (s-h)) OR 1) mod 2^w, h←s; otherwise k=h-s, accept iff 0≤k<w and bit_k=0.`

## Derivation and interpretation

For a new maximum s, shift the bitmap and set the least-significant bit. For an older accepted s in the window, set its offset bit without moving h. Values below h-w+1 are stale. This is the same logic as a finite set of recent accepted identifiers under bounded arithmetic.

## Worked constructed investigation

For width 8, accept 7, then 5 and 6; reject a second 5 and any 0 after high reaches 20. A forged far-future sequence must fail authentication without advancing the high watermark.

## Offline reconstruction and verification method

Use `ReplayWindow` with an independent set-based oracle across thousands of random sequence permutations, and `AuthenticatedSession.receive` to show that invalid tags never mutate state.

## Negative control and known failure

A process that forgets its high watermark may accept an old authenticated frame again; restart survival is a separate persistence and identity-epoch problem.

## Applicability, uncertainty and acceptance boundaries

No real network clock, packet loss distribution, persistent anti-replay database, or concurrency interlock is tested.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC9846, RFC5116. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: distributed-systems-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
