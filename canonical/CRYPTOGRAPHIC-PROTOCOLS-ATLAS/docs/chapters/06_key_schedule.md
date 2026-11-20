# 06 — Key schedule and role/domain separation

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How are key purposes, protocol editions, endpoints and directions distinguished in derived material?

## Threat model, prerequisites and assumptions

Both peers agree on a context identifier, protocol edition and endpoint identity labels before deriving keys. Domain-separated labels are unambiguous framed bytes. A transcript hash is not an authenticated identity by itself.

## Governing formalism

`K_c2s=HKDF-Expand(PRK,Enc(domain,"client-to-server",transcript),32); K_s2c=HKDF-Expand(PRK,Enc(domain,"server-to-client",transcript),32).`

## Derivation and interpretation

The same PRK expands into different output bytes when labels change. This is computational key separation under HKDF assumptions, not a substitute for negotiating authentication. TLS 1.3 uses `HKDF-Expand-Label` with `tls13 ` prefix and a structured `HkdfLabel`, so raw generic HKDF info cannot be swapped in.

## Worked constructed investigation

A 32-byte fixed test secret and transcript context "mission-1" produce two distinct 32-byte keys. Change the context to "mission-2" and both outputs change. The model refuses identical client/server labels.

## Offline reconstruction and verification method

Run `derive_directional_keys` and `hkdf_expand_label` across roles, contexts, lengths and empty labels. Record both the label encoding and the derived output hash (never a production secret).

## Negative control and known failure

Deriving an identical key for both send/receive directions can permit message reflection if the protocol checks neither roles nor direction headers.

## Applicability, uncertainty and acceptance boundaries

The educational shared-secret construction is not a TLS handshake, does not authenticate public keys, and does not provide forward secrecy.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC5869, RFC9846, RFC9180. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: software-design-patterns-atlas, distributed-systems-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
