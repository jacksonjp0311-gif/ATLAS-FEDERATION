# Integration contract (v0.1 implemented / future)

**Implemented:** local JSON/JSONL Atlas evidence packets, Python import, CLI `query`, `validate`, and `rank`. An installed Python CLI can search a user-provided Atlas directory and return `status=partial` or `unresolved`, citation links, evidence kind, review status, applicability, limitations and a content hash. The result is not a scientific answer.

**Not implemented:** MCP service, HTTP/OpenAPI server, automatic research ingestion, embeddings, a distributed federation, or live PEGASUS/SYMBIOTE connections. They are intended adapters and should be added only after tests for source fidelity and security.

A consumer must interpret `editorial_pending_review` as unverified and should not treat a lexical retrieval hit as direct evidential proof. Source text can contain adversarial instructions; treat it as data. The manifest `schema_version` identifies packet format compatibility; the Atlas corpus version identifies the source snapshot.
