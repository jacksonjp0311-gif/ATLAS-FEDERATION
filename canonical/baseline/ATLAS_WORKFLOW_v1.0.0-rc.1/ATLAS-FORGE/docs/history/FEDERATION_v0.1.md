# Cross-Atlas federation — design draft, not implemented

A future read-only directory should hold `atlas_id`, `version`, `manifest_sha256`, `base_uri`, supported `schema_versions`, query capabilities, source-of-truth links, and `last_verified_at`.

Routing: (1) classify domain and evidence requirements, (2) consult matching Atlas manifests, (3) fetch bounded packets, (4) verify version/hash and limits, (5) deduplicate cited claims, and (6) return source-attributed answers or unresolved requirements.

Never merge incompatible units, methods, or confidence labels. Do not treat two summaries that cite the same paper as independent corroboration. Test real connections to PEGASUS, SYMBIOTE, and other agents before reporting them as integrated.
