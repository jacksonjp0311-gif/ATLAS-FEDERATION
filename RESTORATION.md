# Atlas Federation — restoration and byte verification

Original program: **ATLAS FORGE**. Public display name: **Atlas Federation**.

## Choose the correct artifact

The public derivative `ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip` is distinct from the complete original. It preserves cleared material with explicit omissions, documented redactions, and separately identified manifests. It cannot reconstruct excluded content or serve as the original predecessor for historical delta restoration.

**Current delivery status:** the derivative is staged locally; a public release asset and public re-download verification are still pending. See [release status](RELEASE_STATUS.md). The steps below apply once the exact candidate and its matching checksum sidecar are publicly available.

## Verify and open the public derivative

Download the ZIP and its `.zip.sha256` sidecar from the same verified `compiler-design-v0.2.0-public` release. Keep their filenames unchanged. In their download directory:

```sh
sha256sum --check ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip.sha256
```

Stop if the check fails. Compare the asset byte length with its [published verification receipt](evidence/publication/PUBLIC_DERIVATIVE_VERIFICATION.json) as well. A checksum establishes byte identity; it does not independently establish scientific validity, rights, or who produced the file.

Inspect the archive listing, then extract it into a new empty directory:

```sh
python -m zipfile -l ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip
python -m zipfile -e ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip ./atlas-public-restore
```

Start with `ATLAS_COLLECTION_Compiler_Design_v0.2.0-public/PUBLIC_DERIVATIVE_NOTICE.md`, `PUBLIC_OMISSION_MANIFEST.json`, and `FILE_MANIFEST.json`. Original documents and receipts retain their historical meaning. Source programs should be reviewed before execution; some historical commands expect the original collection layout, omitted content, or additional dependencies. Examples and tests that depend on removed data remain unavailable. A successful extraction is not a successful scientific regression or a full original restoration.

The browsable export is mapped in [PUBLIC_SOURCE_DIRECTORY.md](PUBLIC_SOURCE_DIRECTORY.md). It excludes ZIP/WHL containers and uses a separate [browsable manifest](canonical/BROWSABLE_FILE_MANIFEST.json); use the archive `FILE_MANIFEST.json` for extracted release-package verification. Read [publication status](PUBLICATION_STATUS.md) for remaining access and rights limits.

## Original preservation record

The complete original Library artifact remains unchanged privately. It is **735,193,042 bytes** with SHA-256:

```text
0ca19d26cda186a43ed994b9a2c9bb87b38d90d65a07f4ba4edde3a8ccfafae7
```

The [original release receipt](evidence/Compiler_Design_v0.2.0_incremental/ATLAS_FORGE_RELEASE_COMPILER_DESIGN_v0.2.0.json) retains historical identities and verification context. Public restoration uses the separately identified derivative; it does not recover rights-held content from the private original. Private redaction rules, source-data fingerprints, and sanitization helpers are not part of these public instructions.

The original historical receipts report 3,405 tests and matching source/fresh-restored reports. Those receipts remain evidence for their original edition and run; they do not certify the public derivative.

The [release-upload continuation guide](PUBLIC_RELEASE_UPLOAD.md) records the exact candidate identity and the remaining authenticated upload and public re-download steps.
