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
