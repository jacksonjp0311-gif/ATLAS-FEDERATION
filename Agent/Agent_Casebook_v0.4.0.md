# Agent Atlas 0.1.0 — constructed casebook

All **13** cases are original offline examples, not measured LLM or tool performance. They are reproducible with `python -m agent_atlas casebook` and return declared expected outputs, observations and explicit `live_agent_or_external_model_test=false`.

| Case | What it tests | What it does not prove |
|---|---|---|
| DAG and critical path | Exact dependency ordering, supplied-cost path | Optimal real swarm speed |
| Affordability admission | Declared worker/budget selection | Actual model tokens or tool cost |
| Required dependency failed | Descendant blocking | Automatic repair of a live agent |
| Cyclic dependency refusal | Invalid plan detection | General semantic plan quality |
| Host mutation approval | Static request ID and catalog scope | OAuth, real user authentication or safe API call |
| Resource-scope denial | Approval cannot override catalog | Full defense against prompt injection |
| Explicit Stop terminal | Operator Stop not conflated with tool error | Durable service shutdown |
| Journal mutation detection | Local chain content hash | Trusted remote signatures or hardware logging |
| Worker receipt linkage | Exact task/child/output hash | Truth of result or side effects |
| Foreign worker denial | Different task receipt rejected | Complete distributed mutual authentication |
| Memory caveat retention | Qualifier preserved in budget | Better retrieval quality or scientific truth |
| pass-all vs pass-any | Two distinct statistics over repeated attempts | Live agent reliability or iid assumptions |
| Nonterminal receipt eligible | Parent could consider intact receipt | Real process restart or final answer delivery |

Read [investigations](REFERENCE_GUIDE.md) for mechanism, counterexample, alternate explanation and source cautions.


## v0.2 advanced casebook (seven original constructed cases)

Run `python -m agent_atlas advanced-casebook`. The cases demonstrate nested trace overlap with missing final verification, uncertain external submitted effect, a reported provider receipt that does not prove task truth, two conflicting memories with expiry, paired task discordances, MAST missing-label handling, and malformed-input refusals.

**No actual agent run, provider side effect, source MAST trace, model evaluation, or independent human labeling was conducted.** The source-referenced MAST dataset is an external example of a published schema and taxonomy only. The trace timestamps and outcomes used here are explicitly authored. [Investigations 07–12](REFERENCE_GUIDE.md#investigations) describe limits and next empirical evidence.


## v0.3.0 — source-qualified evidence-state experiments

Eight new constructed cases run with `python -m agent_atlas v03-casebook`. They cover parallel OTel spans, rejection of unexpected content attributes, unknown provider submissions, Stop priority, missing parent dispatch, unverified worker success, missing MAST labels, and complete paired repetitions. None uses an actual MAST trace or real LLM call.

The separate NumPy oracle checks timestamp coverage using discrete occupancy rather than interval merging, recovery precedence, grouped 14-code counts, and per-task pass-all totals. These compare algorithms, **not** independent truth.


## v0.4 — proof-qualified learning and evidence survival

Nine new **author-constructed** offline cases are executable through `python -m agent_atlas v04-casebook`. They cover matching SHA-256 fields without host authentication, mismatched parent dispatch, operator Stop dominance, uncertain external effects, paired evaluation with exact discordance arithmetic, missing labels, train/eval contamination, MAST null handling, and memory conflicts/expiry.

All records declare `origin=author_constructed_offline_fixture`. No real agent run, original MAST row, host-signed artifact, actual provider mutation or scientifically verified improvement is implied. `python tools/numerical_oracle_v04.py` computes independently coded decisions, SciPy binomial tails, NumPy annotation counts and memory precedence on additional deterministic *synthetic* cases.
