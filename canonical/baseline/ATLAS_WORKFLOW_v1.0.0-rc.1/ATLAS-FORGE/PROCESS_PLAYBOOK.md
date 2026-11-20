# Atlas Research Process — version 1.0

**Founding goal:** make source-grounded human knowledge reusable across compatible AI systems without discarding the evidence that qualifies it.

1. **Charter and questions.** Define bounded scope, representative tasks, consumers, exclusions, and measurable success conditions.
2. **Discover.** Find primary papers, authoritative standards, datasets, criticisms, negative results, and corrections. Capture URL, publication version, accessed portion, date, license, and retrieval limits.
3. **Verify.** Extract bounded claims with exact locators, units, assumptions, uncertainty, applicable conditions, contradictions, and evidence status. Mark original authors' claims as reported; reproduction is a different event.
4. **Connect.** Link concepts, sources, instruments, and experiments; maintain versioned cross-Atlas dependency pointers without merging incompatible claims.
5. **Teach.** Write explanations, equations, demonstrations, alternative explanations and worked examples. Clearly label simulations versus experiments.
6. **Reuse.** Expose deterministic JSON/JSONL, Python/CLI, and optionally HTTP/OpenAPI and MCP interfaces. Carry limitations and provenance on every hit; abstain when unsupported.
7. **Measure.** Compare supported answers, citation validity, uncertainty and latency with strong baselines using held-out, independently authored tasks. Measure real dollars and energy only when instrumented; avoid ungrounded savings claims.
8. **Correct.** Detect source revisions, corrections/retractions and contradictory evidence. Add new records and previous-version links; never silently rewrite history.
9. **Release.** Run tests and package integrity checks; ship a README with approved banner, clear directory, source register, limitations, examples, changelog and traceable archive. Publish only when authorized and confirm the remote result.

**Evidence classes:** editorial summaries, source-reported claims, formal derivations, synthetic numerical illustrations, simulation, real measurements, independently reviewed conclusions, and reproduced results must not be conflated.

**Admission gate:** a content hash establishes byte identity, not truth. Scientific admission requires review of the exact claimed evidence scope, relevant counterevidence, source rights, assumptions, and the reviewer/decision record.

**Amortization thesis:** `C_independent(N)=N*b`; `C_shared(N)=k+N*(p*h+(1-p)*m)` under an explicit workload and cost model. Savings are conditional: do not infer GPU-energy improvement or quality increase from a cache hit.

**Minimum release quality:** integrity verifiable; science claims appropriately labeled; missing and adversarial queries unresolved; tests reproducible; no third-party restricted redistribution; no false integration claims; clear release limits.


## Current content-first phase

Owner direction recorded 2026-11-12: deepen Measurement scientific knowledge before further navigation work. Preserve and test the existing runtime; defer Bitwork/navigation expansion. Keep shared contracts and the Measurement-v1-before-next-domain gate unchanged. A deferred gate is not passed or removed.
