# 22. Agent Atlas 0.2: what is learned and what is not

The 0.2 content edition extends the 0.1 reference with source-backed discussions and standalone, bounded code for trace lineage and timing, uncertain outbox effects, memory contradictions, paired evaluation, and MAST annotation missingness. Its release status is **scientific reference under development**. None of these methods invokes an agent or external service. They establish implementation contracts for future experiments and help frame observation and recovery requirements.

## Verified contract candidates

**Trace lineage** requires exactly one root, coherent parent references, no duplicate span IDs and timestamps under a stated common clock. Child overlap is accounted for, but no inferred task truth is produced. **Outbox reconciliation** refuses invalid transitions and treats submitted-unacknowledged effects as unknown, not as safe auto-retry. **Memory comparison** retains both sources and qualifiers of discordant claims; expiry is reported, not deletion. **Paired evaluation** reports discordances and a conditional exact p value, without claiming held-out evaluation. **MAST schema analysis** treats unavailable labels as unknown, not negative. These are all authored algorithms, with authored tests.

## Required next empirical work

Acquire rights-cleared authentic agent traces, reconcile per-provider event semantics and clock domains, and validate failure labels against independently reviewed evidence. For durable outbox behavior, test actual crashes, restarts and provider idempotency semantics. For memory, test retrieval and correction on genuinely held-out questions and explicit privacy cases. For performance, run matched tasks with pinned environment and calibrated outcome graders; compare against a simpler model under the same tool permissions, wall time and total cost budget. Record failed trials and aborted runs rather than suppressing them.

A real agent may fail despite passing all local reference tests, because language-model outputs are stochastic, task descriptions ambiguous, provider networks unreliable and external effects unobserved. Likewise, an offline test failure is a software defect rather than evidence of unsafe live behavior. This edition makes the two evidence classes separable.

## Interfaces and build order

The common Atlas record carries exact source references and qualifier closure. Agent Atlas is one more **knowledge node**, not the Bitwork/cross-domain router itself. Signal, Cymatics, Measurement, Causal, Materials and Control retain their own evidence maturity. The user's sequence remains complete all thirty reference domains first, then implement and benchmark Bitwork routing, then run integration/desktop tests and transfer. No desktop installation, GitHub push, live model invocation or routing rewrites are part of this release.

**Source limitations:** MAST full annotated trace dataset not downloaded; OpenAI trace documentation is a public vendor source; LangGraph persistence guide is an evolving implementation description; these do not constitute independent assessment. All quantified tests in the v0.2 casebook are constructed studies, not proven agent improvements.
