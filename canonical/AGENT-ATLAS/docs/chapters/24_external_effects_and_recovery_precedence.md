# 24. Recovery is a decision under unknown external state

After a mutating API call is submitted, a timeout has at least two explanations: the provider never performed the action, or the provider performed it but its receipt was lost. The observation is identical in a caller's log. A robust agent must not interpret a timeout as proof the operation did not execute. This is an *observability* problem and an *idempotency contract* problem, not something a more forceful retry instruction can solve.

## Caller intent and provider deduplication

The AWS Builders Library explains why clients should attach unique **caller-provided request identifiers** and why the service must handle duplicates atomically. Hashing identical arguments is insufficient: a user can legitimately request two identical actions at different times. Conversely, a retry can preserve the same explicit request intent even if transport responses differ. The exact deduplication scope, retention window and semantic-equivalence policy must be documented for the provider. Without that contract, automatic repeated side-effectful tool calls can produce duplicates.

## A conservative offline decision table

`recovery_decision` requires a task identifier, parent-dispatch evidence flag, operator Stop flag, dependency status, worker status, external-side-effect status, verification status, attempts and maximum attempts. It checks exact fields and enumerated states. Its decision order is: **operator Stop → unknown submitted side effect → missing parent dispatch → blocked prerequisite → reported host-verified completion → verification needed → worker still running → attempt limit → potential retry**.

This hierarchy is deliberately conservative. An operator Stop is not an agent failure to be healed by further activity. An unknown external submission requires a human or provider-side reconciliation channel. An unverified success report needs verification, not a successful final-answer label. A pending/running worker should not be respawned merely because it has not returned yet. A retry considered after a bounded failure is **not executed** by this module and confers no tool permissions.

## Conflict and alternate explanations

A worker result with no parent dispatch is incomplete lineage even when its content looks plausible. A provider receipt without a matching request identity may refer to another run, stale task or actor. A record labeled `host_verified` is still a **caller-supplied research field** in this offline Atlas; it does not become cryptographic proof of state correctness. Real systems must bind it to host role, exact task, run, snapshot, verifier and provenance. The connection to Agent Atlas and PEGASUS is architectural only; no live change has been installed.

**Sources:** [AWS Builders Library: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) and [Well-Architected idempotent responses](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel_prevent_interaction_failure_idempotent.html). Original summary and decision table, not an AWS SDK implementation.
