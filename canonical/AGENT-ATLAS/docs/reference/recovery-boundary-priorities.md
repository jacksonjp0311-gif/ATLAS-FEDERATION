# Recovery precedence should be explicit and testable

Offline decision order: Stop > unknown external side effect > missing parent dispatch > blocked dependency > verified terminal > verification needed > running > attempt limit > retry consideration. No branch causes actual side effects.

**Record:** `agent-atlas:recovery-boundary-priorities`  
**Revision:** `fd6a2921d2f93360073a5772167725f7b636a28cf11fbf1c9c48065ce24705c8`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) — Public discussion of uncertain outcomes, caller-provided idempotency key, late arrivals, atomic application/provider contracts

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
