# 01 — Security goals and adversarial capabilities

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

What exactly does a cryptographic construction promise and under what adversary capabilities?

## Threat model, prerequisites and assumptions

Specify roles, protected assets, adversary visibility, key exposure conditions, and what counts as an accepted event. Distinguish passive eavesdropping, active forgery, rollback, concurrency, and a compromised endpoint. Do not use "encrypted" as a synonym for authenticated or authorized.

## Governing formalism

`Pr[forge success] <= Adv_EUF-CMA(A); Pr[distinguish] - 1/2 is confidentiality advantage; an integrity verdict alone establishes neither availability nor identity ownership.`

## Derivation and interpretation

EUF-CMA allows chosen-message MAC queries but the adversary must output an accepted new message/tag pair. IND-CPA compares ciphertexts for two equal-length challenge messages, while authenticated encryption additionally requires ciphertext integrity. Each metric assumes an explicitly modeled key distribution and oracle.

## Worked constructed investigation

Consider a signed archive with SHA-256 only: an adversary who can replace both data and hash can forge matching hashes. The same archive with a verified MAC uses a secret but cannot verify publicly; a signature adds a public verification key but only if that key is independently trusted.

## Offline reconstruction and verification method

Write a five-column threat table: attacker control, secret exposure, protected operation, acceptance predicate, evidence of failure. Classify each reference implementation as primitive arithmetic, authentication-only protocol model, or conceptual overview.

## Negative control and known failure

A MAC verification can pass even when a client lacks authorization to read the material. Treat authentication success and role authorization as separate predicates.

## Applicability, uncertainty and acceptance boundaries

The federation does not claim computational hardness proofs, penetration tests, side-channel resistance, or defense against malicious authorized administrators.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC2104, RFC5116, NIST80057. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: agent-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
