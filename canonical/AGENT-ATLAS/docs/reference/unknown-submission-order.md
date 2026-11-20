# Unknown submitted side effects outrank blind retry attempts

When a mutating call may have reached the provider, subsequent network failure can leave the outcome unknown; retry requires provider idempotency semantics or explicit reconciliation.

**Record:** `agent-atlas:unknown-submission-order`  
**Revision:** `852a642e4fbf560d34cceed8be1c647e2d373e3a9b5f56adbc6c245a2b1c9694`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) — Public discussion of uncertain outcomes, caller-provided idempotency key, late arrivals, atomic application/provider contracts

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
