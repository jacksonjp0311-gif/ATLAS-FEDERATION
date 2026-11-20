# Unknown external submission overrides ordinary retry

After a potentially mutating operation is submitted without an authoritative outcome, provider reconciliation precedes retry; operator Stop still overrides all unapproved continuations.

**Record:** `agent-atlas:retry-reconcile-precedence`  
**Revision:** `0713f3e532deeb7819240f730e75682675ebea220aab8df360f7baab1b1db591`

## Primary source links
- [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)
- [AWS Well Architected: make responses idempotent](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel_prevent_interaction_failure_idempotent.html)

**Status:** Original bounded research reference. Publisher pages were inspected only in declared portions; no live-agent validation, independent reviewer, genuine outcome adjudication or source content redistribution.
