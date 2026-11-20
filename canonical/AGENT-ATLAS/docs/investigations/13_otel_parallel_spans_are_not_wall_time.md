# Investigation 13 — A worker timeline double-counts simultaneous operations

**Origin:** constructed OTel-style span metadata, not a real agent run. The root invokes an agent for 100 ms. A plan occupies 5–14 ms. A tool span runs 20–90 ms and a model span 25–85 ms. Their intervals overlap. Summing child durations yields 9+70+60=139 ms, even though their union is 79 ms and root elapsed time is 100 ms. Those 139 ms are not 139 ms of user-visible latency and do not imply billed GPU usage.

The v0.3 `project_otel_metadata` calculator validates IDs, nesting, allowable operation names and metadata keys. It returns the union coverage and a reported tool span. It **does not** establish that the named tool actually modified the external resource. It rejects text content fields in the input. A result may be structurally valid while missing hidden operations due to uninstrumented libraries or sampling.

**Falsification challenge:** insert a child with an unknown parent, an end timestamp outside the root or two identical span IDs. The parser must reject those cases. The source is the OpenTelemetry GenAI span convention, a development-status public standard; the numbers and fields here are authored test fixtures.
