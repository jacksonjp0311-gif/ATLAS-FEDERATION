# Do not authorize a duplicate provider mutation from a model conclusion

Block automatic retry or evidence admission if side_effect_state is submitted_unknown, even if the worker reports success or the artifact hash appears to match.

**Record:** `agent-atlas:outbox-reconciliation-gate`  
**Revision:** `e43f985ed058837081707caf3d42cc725bf3c78f654b365ec502181c31fe01fe`

## Primary source links
- [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)
- [AWS Well Architected: make responses idempotent](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel_prevent_interaction_failure_idempotent.html)

**Status:** Original bounded research reference. Publisher pages were inspected only in declared portions; no live-agent validation, independent reviewer, genuine outcome adjudication or source content redistribution.
