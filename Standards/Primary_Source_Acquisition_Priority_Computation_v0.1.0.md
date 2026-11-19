# ATLAS FORGE — Primary-source acquisition priority for computation

**State:** 390 source cards across eight nodes; zero authenticated retained original publisher files under the strict survival audit. No network acquisition of third-party original files was completed in this release. Existing original explanatory Markdown, source code, and simulations are preserved.

## Rights-aware acquisition order

1. **NIST DADS official publications and source dictionary:** identify exact federal publication/edition, determine item-level public-domain status and embedded third-party rights, retain transport bytes with stable URL and SHA-256.
2. **Pat Morin Open Data Structures author-site CC BY edition:** author site explicitly licenses text and code CC BY; verify which file exactly bears that grant. The Athabasca University Press published edition advertises different CC BY-NC-ND rights. Do not conflate them.
3. **Python Software Foundation official documentation:** Python docs are under PSF license; retain license/copyright notices, exact documentation source revision, and SHA-256 alongside floating-point and rational-arithmetic references.
4. **MIT OpenCourseWare 6.042 and 6.006:** choose rights-cleared source PDFs, carry attribution, preserve specific course edition; rights may restrict commercial reuse.
5. **SciPy official documentation and source:** version-lock source references and preserve license/NOTICE before mirroring.
6. **Stanford Encyclopedia references:** retain bibliography and original commentary until the full rights terms authorize offline copies. The editorial article itself must not silently be treated as open-license.

## Per-source proof before upgrading evidence level

Store upstream author/publisher, publication/version/commit, source URL and redirect history, retrieval timestamp, exact unmodified transport bytes, local SHA-256, rights/license/attribution, original vs transformed copy relationship, byte-level re-fetch result, and an independent spot-check against publisher metadata. Source provenance must survive database exports.

Do **not** change a record to `source_bytes_archived=true` until the actual file is present, its SHA-256 matches the audit, the rights basis is documented, and its exact claim scope has been inspected. An archive hash establishes byte consistency, not source authenticity or scientific truth.

## Restoration drills

Restore using no network connection on a second machine, verify inventory checksums, ensure licenses and decoders are present, manually reconstruct selected algorithms from text alone, and independently recalculate numerical examples. Publish the failure log rather than hiding unavailable materials. Maintain geographically separated verified copies only when explicitly authorized and available.

## Current roadmap

Computation remains active at v0.1.0. The other 24+ domain topics remain queued according to the original 30-domain order, and Bitwork routing is deferred until domain content work is complete.
