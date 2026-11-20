# Investigation 20 — The timeout after a remote mutation

A dispatched worker has an authorized API operation that can mutate an external account. It sends the request; the client times out without a provider receipt. The worker later says the task succeeded. A parent that treats this as a simple worker failure may retry and cause a duplicate side effect.

The existing Agent Atlas outbox model classifies the transition as unknown after submission, while the new proof packet requires reconciliation before admission or retry. Its output `reconcile_external_effect_first` is a **decision code**, not an API call. It does not prove that a provider committed the first request or that an idempotency key was actually honored. If the user presses Stop, the conservative priority is `respect_operator_stop`.

A replay test should distinguish four real provider conditions: never reached, committed and acknowledged, committed with response lost, and pending/uncertain. That requires an authorized test service with recorded transaction IDs, durable state, and a policy specifying which actions may be repeated. The casebook does not contact any provider or dispatch a worker. Its correct classifications are checks of declared recovery rules, not evidence of exactly-once semantics.
