---
name: atlas-node-conformance
description: Migrate or validate Atlas data against the generic node contract without writing domain-specific search branches.
compatibility: Requires Python 3.10 or newer and access to the Atlas Forge checkout.
---

# Common node conformance

Run `python tools/workflow.py conform`. Read `schemas/common/` and `docs/COMMON_CONTRACT.md`. Every collection, including empty collections, must be explicit. Unknown required extensions fail compatibility. References include exact revisions, and record IDs remain stable.

During migration preserve the original record and evidence labels in provenance. The only source-format dispatch belongs in the offline importer, not the search/context runtime. Do not execute imported source code.

Run:

```sh
python -m unittest discover -s tests -v
python tools/schema_check.py
```

Verify the synthetic conformance-fixture node loads without a kernel edit. It is a test fixture, not a new scientific domain. Retain byte hashes and provenance receipts. A conformance pass does not establish scientific truth.
