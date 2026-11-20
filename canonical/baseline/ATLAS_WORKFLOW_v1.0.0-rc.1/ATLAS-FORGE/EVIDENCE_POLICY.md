# Evidence governance

Publicly available text is not necessarily licensed for redistribution. Preserve stable citations and publication versions; link rather than mirror full texts when rights are unclear.

`evidence_kind` and `review_status` are separate. `measured` means original observations accompanied by instrumentation, data lineage, units, calibration context and original file hash. `reproduced` is reserved for a documented independent experiment or analysis with a reproducibility artifact. `source_reported` is only a scoped statement attributed to its source. `synthetic` and `simulation` never become measured by changing a label.

`review_status`: `editorial_pending_review`, `portion_checked`, `human_reviewed`, `independently_reproduced`. `portion_checked` means the identified source portion was inspected; it does not imply the underlying experiment was validated. `human_reviewed` requires a reviewer and review artifact. `independently_reproduced` additionally requires a reproduced evidence kind and an independent protocol/receipt.

Evidence packets are append-only in a released corpus. Corrections use `supersedes` IDs. No agent may auto-promote candidate evidence to independently verified status. Consumers must retain limiting conditions and source labels. A stale, retracted, unverifiable or incomplete answer should be marked `partial` or `unresolved`.
