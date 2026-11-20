# Public derivative release status

**Status: local candidate staged; no public asset upload or public re-download verification.**

| Field | Public derivative |
| :--- | :--- |
| Repository | `jacksonjp0311-gif/ATLAS-FEDERATION` |
| Intended release tag | `compiler-design-v0.2.0-public` |
| Intended ZIP asset | `ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip` |
| Extracted root | `ATLAS_COLLECTION_Compiler_Design_v0.2.0-public/` |
| Checksum sidecar | `ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip.sha256` |
| Content record | [`canonical/FILE_MANIFEST.json`](canonical/FILE_MANIFEST.json) |
| Omissions | [`canonical/PUBLIC_OMISSION_MANIFEST.json`](canonical/PUBLIC_OMISSION_MANIFEST.json) |
| Candidate verification receipt | [Local verification record](evidence/publication/PUBLIC_DERIVATIVE_VERIFICATION.json) |
| Local candidate length | 731,933,585 bytes |
| Local candidate SHA-256 | `9e91db0327913626c9faf56e5221a5016aadeef0509b45c56ffc667bb863090f` |
| Public asset length and SHA-256 verification | Pending public delivery |

The public derivative has its own byte length and checksum. It is not byte-identical to the preserved 735,193,042-byte original, whose SHA-256 is `0ca19d26cda186a43ed994b9a2c9bb87b38d90d65a07f4ba4edde3a8ccfafae7`.

The current connection can publish source files but cannot upload the binary release asset, and an authenticated upload session is unavailable. Publication requires uploading the verified candidate and its manifest/checksum material to this existing repository, then independently downloading the public asset and checking its full length and SHA-256. Until that succeeds, the [Releases page](https://github.com/jacksonjp0311-gif/ATLAS-FEDERATION/releases) is not evidence that this candidate has been delivered.

The ZIP belongs in a GitHub release, never in Git history. Historical source/fresh-restoration test receipts remain historical evidence; they must not be presented as a fresh derivative test run or public download verification.

The [release-upload continuation guide](PUBLIC_RELEASE_UPLOAD.md) records the exact candidate identity and the remaining authenticated upload and public re-download steps.
