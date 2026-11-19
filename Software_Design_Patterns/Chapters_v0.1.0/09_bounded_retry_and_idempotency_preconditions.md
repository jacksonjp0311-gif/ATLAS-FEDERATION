# 09. Retry with bounded attempts and explicit idempotency preconditions

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

Retry is useful when a failure may be temporary, but automatic repetition is dangerous when an operation may have succeeded before its response was lost. A finite retry wrapper should accept a bounded attempt count and a deliberate classification of retryable exceptions. It must not catch every error, blindly replay irreversible physical commands, or change result ownership silently. Idempotency keys and durable knowledge of prior completion are prerequisites for safely retrying many mutations. Timeouts and backoff should also be explicit in a real system; this offline model deliberately does not sleep or call networks.

## Formal contract and executable reference

**Invariant:** `attempts<=1+retry_budget; retry only if chosen exception is transient`.

**Implementation:** `resilience.bounded_retry`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Make an operation fail twice with a designated transient OSError, then succeed on its third call. The retry wrapper returns attempt count three. Next make an operation fail with a ValueError that is not designated transient; it must be raised immediately. Repeat with retries set to zero and prove exactly one attempt. Do not use this simple wrapper to send repeated machine commands without durable command identification.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

The reference does not know whether a prior external operation committed. A local retry success does not imply exactly-once delivery to a robot, industrial controller, database on another host or medical instrument. Classification is policy, not an objective property proven by exception type.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `AZURE-RETRY` — Microsoft Learn, Retry Pattern (https://learn.microsoft.com/en-us/azure/architecture/patterns/retry). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
