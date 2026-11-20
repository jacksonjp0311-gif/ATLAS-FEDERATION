# Investigation 09 — Two sources disagree; the agent must not pick a winner

An author-constructed memory set includes a report “machine status is ready” from source A and “machine status is fault” from source B, with identical subject/predicate/context fields and different source revisions. A third old memory with a different context has expired under the caller's supplied time. The task is to preserve the uncertainty while answering a downstream question.

The comparison returns one unresolved conflict with **both** source identities, their exact revisions, qualifiers and value digests. The expired memory is listed, not deleted. It does not mark source B true because it is newer or sensor-like. It does not mark source A true because it sounds like an operator. Both could be true at distinct actual times that the coarse context failed to capture.

Future correction requires a source-specific updated observation, a more precise context (machine, batch, timestamp, state variable), and a retained correction relationship. A compacted summary saying “the machine is faulty” would lose the contradictory origin and turn a hypothesis into a supposed fact. The safe output says the current condition is **unresolved** and names the next measurable check.

**Boundary:** exact structured JSON equality, not semantic contradiction detection. In a live language agent, context extraction and identity resolution could themselves be wrong and must be evaluated with held-out data. The two claims are hypothetical; no personal or factory records were fetched.
