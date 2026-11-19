# ATLAS FORGE — source preservation progress, Computation v0.2.0

## Evidence inventory

This edition is the first source-byte-preservation pilot for Computation Atlas. The previous federation's **390** bibliography/source cards remain link-only, with no locally authenticated publisher-original content. Computation v0.2 adds **six** cards: three represent authenticated original software/license assets and three are external documentation references. The eight-node federation now has **396 source cards**; **three** have newly authenticated local original software bytes. The rest remain bibliographic evidence, not self-contained primary-source archives.

### Captured original software and rights

| Asset | SHA256 | Original Git blob SHA1 |
|---|---|---|
| TheAlgorithms/Python `searches/jump_search.py` | `bb274db1e8952b5e3a924acd66dd2b6880ec49d9b74d354fec97fee4713786b2` | `1bd7493dbbfe3dca0d837da005c7830c10c9dc3e` |
| `maths/extended_euclidean_algorithm.py` | `932d502e02bc3a6fe680a8185159cba3757556f91427758d2cfe288ee6d07f16` | `b3b279581f388930fdea285c6421819cfcd58df0` |
| `LICENSE.md` | `4395a1dc4bda1d6054c45b4d1230c709c7398e6d66f1d0aff4b22d95973bea56` | `de631c3ef33374d91a78dca3a656806e4e3bb890` |

Repository: `https://github.com/TheAlgorithms/Python` at immutable commit `30507bbe41397065728167fb09aa820f9fce8dc7`, licensed MIT with full notice preserved. Both original code files and the original license are present in the source tree and installed standalone wheel. Git identifiers and SHA256 establish reproducible expected byte content but do not establish independent signatures, peer review, or mathematical correctness.

## Outstanding preservation gaps

- **0** publisher-original scholarly papers captured by the strict source audit.
- **393** source cards do not carry a linked, authenticated local original-source asset under the current policy (including the three new link-only cards).
- Missing licenses or third-party rights decisions must remain unknown; do not guess from a source being online.
- No human scientific review, multi-media archive redundancy, independent machine restoral, or certified signatures.

## Acquisition protocol

1. Select a bibliography record and record owner, immutable revision (DOI/version/commit), exact source URL, document type, rights, and acquisition timestamp.
2. Confirm explicit copying, redistribution, and modification permissions, including restrictions on embedded third-party content.
3. Acquire the original bytes and save *unmodified*. Hash with SHA256 and, for Git sources, compare Git object IDs. Retain license and attribution with the artifact.
4. Link exact local path and revision into its source record, then test archive extraction, rights completeness, and exact byte fidelity.
5. Run meaningful mathematical/empirical reproduction separately; never treat an integrity hash as a scientific validation.
6. Revalidate independent cold offline restoration and produce a revisioned checklist for each domain.

## Safety against false coverage claims

This pilot documents educational source-code preservation. It is not a preserved copy of human mathematics, nor does it make 30 domains complete. Keep the unresolved missing-paper source debt visible in every release.
