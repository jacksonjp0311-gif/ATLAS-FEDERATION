# EPRA evaluation protocol

The research amortization hypothesis is testable: shared source-grounded packets may reduce repeated workload cost while preserving source fidelity and answer quality. This starter does **not** claim to have measured that benefit.

1. Pre-register a domain question set and source coverage; reserve independently authored and hidden evaluation questions.
2. Compare repeated independent research, strong retrieval-augmented generation, and an Atlas packet-assisted method. Keep model/version/context budgets comparable.
3. Measure citation validity, factual/technical correctness, uncertainty reporting, appropriate abstention, full lifecycle compute cost, elapsed time and maintenance overhead. Log physical energy only with calibrated measurement.
4. Include a policy for source updates and contradictions; evaluate stale-source and rights-constrained questions.
5. Measure all offline packet construction, review and maintenance effort across total query volume, not just fast cache hits.
6. Report confidence intervals, failures, query coverage, source versions, and independent assessor provenance.

Cost model: C_baseline(N)=N*b; C_atlas(N)=k+N[p*h+(1-p)*m]. Let delta=b-[p*h+(1-p)*m]. A positive break-even N exists only if delta>0, then N>k/delta. Treat this model as an illustration until calibrated.
