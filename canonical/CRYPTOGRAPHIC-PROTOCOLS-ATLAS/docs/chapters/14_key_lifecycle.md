# 14 — Key lifecycle, epochs, rotation and compromise response

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

What operational metadata is necessary to know whether a valid tag was created under an authorized key?

## Threat model, prerequisites and assumptions

Trust decisions include key identifier, purpose, epoch, algorithm, creation/activation/retirement, revocation state, custodian and compromise response. Timing and policy cannot be inferred from cryptographic arithmetic.

## Governing formalism

`Accept(record)=VerifyTag(K_epoch,record) AND EpochAllowed(epoch,t) AND RoleAllowed(actor,action) AND NotRevoked(key_id).`

## Derivation and interpretation

Rotating keys requires moving from old to new encryption/authentication domains while preventing rollback. A key-change message itself needs authentication under an authorized root. Old secrets should be deleted when no longer necessary, subject to recovery and legal requirements.

## Worked constructed investigation

An archival reader may verify a 2025 signed receipt with a retired key if policy includes historical validation and a trusted timestamp, while refusing new data signed after revocation. Neither policy follows automatically from a SHA-256 digest.

## Offline reconstruction and verification method

Maintain a minimal offline key inventory and recovery checklist (identifier, source, allowed purpose, epoch, retirement, trusted anchors, revocation evidence, audit). Consult NIST SP 800-57 for actual lifecycle guidance.

## Negative control and known failure

A cryptographically valid replay under an expired or compromised key must be refused by an independent policy decision; MAC verification alone cannot make that decision.

## Applicability, uncertainty and acceptance boundaries

No real production key-management system, HSM, secure erase or operator approval process has been exercised.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: NIST80057, NIST800193, RFC9846. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: computer-architecture-digital-hardware-atlas, distributed-systems-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
