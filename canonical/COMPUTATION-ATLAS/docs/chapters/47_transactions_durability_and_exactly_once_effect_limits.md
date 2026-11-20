# Chapter 47 — Transactions, durability and exactly-once effect limits

**Area:** Distributed Systems. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Atomicity, consistency, isolation and durability describe transactional guarantees under documented storage semantics. A database transaction may commit while the client loses the acknowledgment, creating an ambiguous external outcome. Exactly-once message delivery is a phrase that often hides the distinction between transport retries and unique external effects; safe idempotent application requires a provider-side contract or transactionally coordinated state. A caller-generated request ID alone does not prove deduplication. Two identical payloads may be intentional separate operations, and two nonidentical payloads may be retries of one logical operation.

## Mathematical contract

For idempotent operation f: f(f(x))=f(x) under the declared state and identity semantics. Exactly-once effect requires an authorization and deduplication boundary that survives crashes; mere at-least-once delivery does not imply exactly-once effects.

## Derivation and reasoning

If the service stores the request ID and its committed effect atomically, duplicate requests with that same logical ID can return the stored response rather than re-execute. If the client times out after submission and lacks authoritative provider reconciliation, retrying with a new ID can duplicate the action. A local event journal that is not itself durable or trusted cannot prove what the provider did.

## Worked reconstruction and independent check

Construct a simulated ledger with prepared, submitted, committed and acknowledgment-lost states. Ask whether the caller may safely retry under (a) no dedupe contract, (b) a provider-enforced idempotency token, and (c) unknown token-retention window. Document decisions as conditional rules, not as a live API implementation.

## Limitations, falsification, and invalid use

This content is a protocol-level explanation only. The archive does not implement a production database, distributed consensus protocol, trusted authorization, or two-phase commit; no live transaction is performed.

## Cross-domain meaning

A future Agent/Computation integration will need actual signed receipts and a host-controlled lifecycle, separate from reference reading.

## Source orientation and recoverability

- [Lamport, Time, Clocks and the Ordering of Events in a Distributed System](https://lamport.org/pubs/time-clocks.pdf) — original publisher bytes unavailable in this package.
- [AWS Builders Library, Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
