# Investigation 29 — Lost acknowledgment after an irreversible tool request

**Origin:** constructed protocol scenario; no external service was called. A parent sends an authorized mutation with a stable idempotency key. The network times out before an acknowledgment arrives. The initial evidence is `submitted_unknown`, which is not proof of success or failure. The model must not produce a new transaction ID and repeat the mutation blindly. An independently trusted provider receipt or reconciliation query can determine whether the original effect happened.

**Alternative failure:** a child replies `done` and an artifact has a matching hash, but no valid parent dispatch is linked to that child. Hash equality does not authenticate host or owner. This must remain unadmitted; a worker cannot authorize itself by text. If the operator has stopped the mission, the recovery policy preserves the stop instead of continuing until a goal is met.

**What would prove live reliability:** provider-backed idempotency semantics, real request IDs, robust journal persistence, audited client and server timestamps, duplicate-safe transitions, real failure injection and independent checking of resulting external state. There are **no** such live trials in this edition. Revisit earlier Agent Atlas v0.4 receipt tests and Chapter 43 for reconciliation prerequisites.
