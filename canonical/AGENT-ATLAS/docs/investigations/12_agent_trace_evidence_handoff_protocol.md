# Investigation 12 — Handoff for a future authentic agent trace

Suppose an engineer provides a PEGASUS or another agent-harness run log containing parent/worker dispatches, model calls, tool attempts, checkpoint metadata and final reports. The Atlas must not blindly reinterpret that raw log as a universal event schema. It should first inventory file formats, timestamps, clock sources, model/tool version, provider identities, source rights, sensitive data, task acceptance criteria and provenance of each event.

**Ingestion protocol:** retain the original source reference and, if access rights permit, immutable raw bytes with authenticated hash. Transform into a normalized copy with exact schema/version mapping; retain fields that could not be mapped, rather than dropping them. Remove secrets and personally identifiable fields before publishing the Atlas. Ensure parent-child links and receipt IDs are correct; disambiguate provider acceptance from verified external side effects. Mark gaps in logs explicitly.

**Failure hypotheses:** a missing worker receipt may mean worker never completed, result delivery failed, parent commit failed, or logging omitted an event. It cannot be classified solely from a model's final prose. A tool timeout may conceal side effects; re-execution requires reconciliation and consent. A stop event must be signed or otherwise attributable to host/operator authority, not inferred from an untrusted line of source text.

**Evaluator:** define external state predicates that must be independently checked, and a control baseline with equal resource budgets and model access. Keep held-out tasks out of design. For memory claims, include source revisions and allowed-use context; for multiagent consensus, track independent evidence rather than number of agreeing workers.

**Current result:** this is a reproducible handoff *protocol and synthetic parser tests*, not a run of the user's private harness, connected provider, or an installed local language model. No private project files were accessed.
