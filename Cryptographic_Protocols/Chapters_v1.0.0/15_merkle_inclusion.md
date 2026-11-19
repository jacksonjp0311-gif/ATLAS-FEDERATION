# 15 — Merkle inclusion proofs and append-only evidence

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How can a reader verify that a leaf belongs to an ordered commitment without downloading every other leaf?

## Threat model, prerequisites and assumptions

The model uses the historical RFC 6962 v1 domain prefixes and an ordered list; it does not claim current Certificate Transparency v2 protocol conformance. A trusted signed root is a separate requirement.

## Governing formalism

`LeafHash(m)=SHA256(0x00||m); NodeHash(L,R)=SHA256(0x01||L||R); EmptyRoot=SHA256(empty).`

## Derivation and interpretation

For n non-power-of-two leaves, split the tree at the largest power of two strictly below n; recursively hash left and right ranges. An inclusion proof contains the necessary sibling hashes. Verification rebuilds the root with the same leaf index and tree size.

## Worked constructed investigation

For leaves [a,b,c], root=NodeHash(NodeHash(LeafHash(a),LeafHash(b)),LeafHash(c)); a three-leaf tree is not the hash of LeafHash(a) and NodeHash(b,c). Reordering leaves changes the root.

## Offline reconstruction and verification method

Compute `tree_hash`, `inclusion_proof`, and `verify_inclusion` for every index of trees with 1..89 leaves; compare to an independently implemented recursive oracle. Refuse wrong leaves, wrong indices, forged siblings and excess proof elements.

## Negative control and known failure

An attacker who substitutes both the tree root and proof can still satisfy mathematical membership checks: obtain the expected root from a trusted signed checkpoint.

## Applicability, uncertainty and acceptance boundaries

No certificate issuance system, log consistency proof, independent witness signature or live gossip network is implemented.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC6962, RFC9162, RFC8032. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: computation-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
