# Investigation 17 — A completed worker result without its parent dispatch

**Origin:** constructed task state, not a live PEGASUS trace. The worker claims completion, but the currently running parent has no matching dispatch record. A naïve summarizer could accept the final text because it appears to solve the problem; the offline admission rule selects `require_parent_dispatch` and does not mark completion.

To admit a real result, the host must match immutable task ID, parent-run ID, attempt index, goals and context snapshot, worker artifact digest, allowed tools and evidence, and a verification result bound to this same task. A stale worker from an earlier conversation cannot be used to prove a new request simply because its output looks relevant. If the parent is stopped, reactivation requires authorization by the operator, not an agent's self-preservation incentive.

This case is a source-backed design warning about asynchronous execution; it does not claim that PEGASUS actually demonstrated this failure or that the Atlas patched its runtime. Future host testing must preserve traces and evidence receipts for independent diagnosis.
