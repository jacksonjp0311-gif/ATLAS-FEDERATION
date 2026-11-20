# Idempotency key expresses intent, not mere payload equality

A caller-provided request ID enables provider deduplication; hashing identical payloads may merge distinct intended operations. Durable idempotency requires provider contract and atomic state handling.

**Record:** `agent-atlas:request-id-vs-payload-hash`  
**Revision:** `f643c989bb20a501d586455ca58f18e481553e981b67aad69c76d923eedb81e2`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) — Public discussion of uncertain outcomes, caller-provided idempotency key, late arrivals, atomic application/provider contracts
- [AWS Well Architected: make responses idempotent](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel_prevent_interaction_failure_idempotent.html) — Public reliability guidance on idempotency tokens; model is not a proof that a specific remote API is idempotent

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
