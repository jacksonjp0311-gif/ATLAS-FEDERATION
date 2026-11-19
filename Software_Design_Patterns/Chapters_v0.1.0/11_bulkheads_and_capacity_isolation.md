# 11. Bulkhead capacity partitioning and blast-radius limits

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A bulkhead partitions finite capacity so a failing subsystem cannot consume all resources shared by others. In a local recovery tool, domain indexing and file restoration might use separate worker budgets; a hung search should not exhaust the entire runtime. The Atlas bulkhead model accepts named lanes with bounded positive capacities, refuses a lease when a lane is full, and requires explicit balanced release. This demonstrates numerical isolation of allocations, not operating-system process isolation or protection against a malicious plugin.

## Formal contract and executable reference

**Invariant:** `allocated[lane] <= capacity[lane] independently for every lane`.

**Implementation:** `resilience.Bulkhead`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Set lane search capacity one and restore capacity two. Acquire search once and verify a second search acquisition is refused while restore can still acquire twice. Release the search lease and verify it becomes available. Try releasing an unacquired lease or allocating a boolean-sized capacity: reject. The result must include independent per-lane counts.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

A thread counter does not preempt a deadlocked task, enforce CPU memory limits, or isolate crashes in separate processes. Real isolation requires worker supervision, timeouts, process/container boundaries and instrumented resource limits.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `AZURE-BULKHEAD` — Microsoft Learn, Bulkhead Pattern (https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
