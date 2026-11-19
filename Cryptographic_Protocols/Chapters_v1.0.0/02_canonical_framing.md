# 02 — Canonical binary encoding and transcript ambiguity

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How does a protocol prevent two logically different messages from sharing the same authenticated byte string?

## Threat model, prerequisites and assumptions

All fields are byte strings; lengths are unsigned big-endian integers, number of fields is bounded, and trailing bytes are rejected. Semantic validation still happens above the framing layer.

## Governing formalism

`Enc(x1,...,xn) = u16(n) || Σ[u32(|xi|)||xi]; Enc(a,bc) != Enc(ab,c).`

## Derivation and interpretation

Naive concatenation maps the pairs ("ab","c") and ("a","bc") to the same bytes. Prefix lengths before each field so decoding determines a unique segmentation; enforce upper bounds before allocation and reject noncanonical trailing data. A unique serialization is necessary but not sufficient: Unicode normalization and semantic aliases still need a policy.

## Worked constructed investigation

Enc([0x61,0x6263]) begins 00 02 | 00 00 00 01 61 | 00 00 00 02 62 63. Its one-field alternative Enc([0x616263]) begins 00 01 and cannot collide. Verify both through `crypto_atlas.framing`.

## Offline reconstruction and verification method

Run `encode_fields`/`decode_fields` on empty, multi-field, null-byte and one-megabyte inputs; compare output with a second parser using a byte cursor. Check truncation at each boundary and rejected surplus bytes.

## Negative control and known failure

Concatenating a role string directly with a variable-length identity allows ambiguous messages; hashing ambiguous bytes does not restore the missing boundary.

## Applicability, uncertainty and acceptance boundaries

The framing format is original educational notation, not an interoperable TLS, COSE, ASN.1 or canonical CBOR encoding.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC9846, RFC9180. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: language-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
