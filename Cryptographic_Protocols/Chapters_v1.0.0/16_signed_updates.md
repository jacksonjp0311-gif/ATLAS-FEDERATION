# 16 — Authenticated software updates, rollback and threshold policy

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How can offline rebuild tooling reject a validly signed but obsolete or unauthorized update?

## Threat model, prerequisites and assumptions

A secure update workflow separates trusted root metadata, delegate roles, artifact hashes, version monotonicity and expiry. Clock trust is not assumed merely because an offline file has a date.

## Governing formalism

`AllowUpdate=SignatureThresholdOK ∧ HashMatch ∧ RoleAuthorized ∧ Version>=trusted_min ∧ NotExpired_as_policy_verified.`

## Derivation and interpretation

Threshold signatures are distinct from multiple copies of one shared key. A policy may require, for example, 2 signatures from 3 independently managed keys; the actual threshold and authorization must be stored outside attacker-modifiable update metadata. Rollback prevention requires protected local version state.

## Worked constructed investigation

An attacker presents legitimate signed release v4 after the system already accepted v6. Its signature may verify, but a reader with trusted minimum version v6 must refuse to install it. A changed archive hash must fail independently of the signature count.

## Offline reconstruction and verification method

Write a pencil-and-paper acceptance table with authorized signer sets, expected hashes, minimum versions, timestamps and unresolved clock trust. Use verified historical Atlas release receipts as data examples, not as proof of a complete signed-update system.

## Negative control and known failure

Replacing both the package and an unprotected version marker defeats a purely local rollback check. A signed file is not a synonym for a trustworthy source.

## Applicability, uncertainty and acceptance boundaries

No threshold signature implementation, secure boot, TUF client, trusted offline clock or tested update chain is supplied.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: NIST80057, NIST800193, RFC8032. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: computer-architecture-digital-hardware-atlas, distributed-systems-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
