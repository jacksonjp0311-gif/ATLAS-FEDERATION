# 09 — Authenticated handshakes, identity binding and key confirmation

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How can a key agreement be linked to participant identities and a specific session transcript?

## Threat model, prerequisites and assumptions

A secure handshake requires anti-downgrade negotiation, identity authentication and transcript binding under its own protocol semantics. A shared-secret MAC-only educational demonstration does not establish secure public-key negotiation.

## Governing formalism

`transcript_hash=SHA256(Enc(version,suite,client_id,server_id,messages)); Finished=MAC(K_finished,transcript_hash).`

## Derivation and interpretation

If an attacker changes a version, handshake parameter, or an endpoint label, a properly constructed Finished or signature verification over the transcript should fail. Key confirmation also requires matching role-specific keys, not simply receipt of an unverified welcome message.

## Worked constructed investigation

Construct two peers under context `mission-1`, IDs `reader` and `archive`, and a fixed test PSK; verify the authenticated record in both directions and reject a peer using a different context or key.

## Offline reconstruction and verification method

Use the `AuthenticatedSession` MAC-only model as a finite demonstration of role-separated authenticated messages. For a real handshake use a maintained, standards-conforming TLS library; do not adapt this demo into a custom network security protocol.

## Negative control and known failure

A shared PSK distributed to two organizations does not prove which holder sent a particular message, and key compromise invalidates the model’s identity interpretation.

## Applicability, uncertainty and acceptance boundaries

No PKI, ephemeral key exchange, real mutual authentication or full TLS handshake is implemented or certified.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC9846, RFC5869, RFC7748. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: distributed-systems-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
