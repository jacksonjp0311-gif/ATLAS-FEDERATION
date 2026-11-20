# ATLAS FORGE — Software Design Patterns constructed casebook

24 software-only investigations, not physical power-loss experiments.

## Case 01: Design patterns as reconstructible engineering contracts

**Exact reference:** `README.md and tests`.

**Constructed test:** Select a failed local sensor-processing workflow. State its normal flow, the assumption that a value arrives in millivolts, the alternate value in volts, and the failure when units are confused. Identify which boundary a PortAdapter could normalize and how to verify it through a replayable sample. Require source-level hashes, pass/fail test, and evidence maturity for each claim.

**Independent requirement:** Pattern=(problem,context,forces,solution,invariants,negative_cases,evidence).

**Negative control:** Do not infer implementation quality from an architectural diagram. Patterns can increase complexity and centralize failure. A local reference can demonstrate finite behavior but not reliability across unknown operating systems, storage hardware, attackers, or physical devices.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 02: Canonical data, strict schemas, and versioned contracts

**Exact reference:** `contracts.envelope, contracts.parse_envelope`.

**Constructed test:** Create the mapping {b:2,a:1}, wrap it as a version-one command, serialize and decode it. Reverse the order of input keys: the payload digest must not change. Modify a value without recomputing SHA-256: decoding must refuse. Supply a NaN, an unexpected schema field, an invalid ID, and excessive nesting: reject each. Record exact byte-length bounds and the trusted provenance of any external envelope.

**Independent requirement:** H=SHA256(canonical(kind,version,id,payload)); digest equality ≠ authentication.

**Negative control:** JSON key ordering alone is not a complete cross-language canonical-JSON standard: numeric formatting, Unicode normalization and large integers must be specified before interoperability can be certified outside this Python reference. No signed origin or network protocol is provided.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 03: Factory construction and explicit dependency injection

**Exact reference:** `composition.build_adapter, composition.PortAdapter`.

**Constructed test:** Call build_adapter({source_units:mV}) and normalize a record containing 1234 mV; the output is 1.234 V. Construct the same adapter from source_units:V and input 1.234; both agree to floating-point precision. Reject an unknown unit or undeclared configuration field. This makes a missing calibration explicit rather than implicitly assigning SI units.

**Independent requirement:** implementation = Factory(checked_configuration), not global hidden state.

**Negative control:** Factory construction does not imply that a real sensor is calibrated. An adapter can translate units while preserving a systematically wrong voltage. Do not use a software conversion test to certify electrical safety, instrument isolation or clinical devices.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 04: Adapters and anti-corruption layers for incompatible information

**Exact reference:** `composition.PortAdapter.normalize`.

**Constructed test:** Convert a synthetic reference signal of 2500 mV to 2.5 V and compare it with a 2.5 V reference using the same canonical field. Try an unrecognized Celsius unit for a voltage field: reject it before downstream use. Include a negative control where the same numeric '2500' is supplied with the wrong unit; the results must differ and the source identity must accompany the example.

**Independent requirement:** V_SI = V_mV/1000; raw_data != certified_calibration.

**Negative control:** Structural interface compatibility does not verify physical equivalence, measurement uncertainty or safety certification. Cross-domain integration also requires calibrated instruments, correct sampling, environmental constraints and human expert review.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 05: Strategy pattern and deterministic policy substitution

**Exact reference:** `composition.StrategyRegistry`.

**Constructed test:** Register an integer doubling strategy and an independent identity strategy. Evaluate the same integer and compare results to the reference definition. Attempt to register another function under the existing name; the registry must refuse the conflict. Attempt an unknown name and verify it fails rather than silently returning a default result.

**Independent requirement:** result=StrategyRegistry[name](payload) with explicit named policy.

**Negative control:** A callable policy is trusted local code. This is not a plugin sandbox or secure environment for arbitrary third-party Python. Strategies can have hidden side effects; full scientific reproducibility requires pure implementations, versioned inputs and independently checked outputs.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 06: Decorator pattern for explicit audit boundaries

**Exact reference:** `composition.audited`.

**Constructed test:** Wrap a function mapping x to {out:x+1} with an audit decorator and inspect the result SHA-256. Invoke the wrapper twice on the same input; the output digests should agree, although two audit entries exist. Wrap a function that raises: verify no false completed entry appears. Keep detailed failure information separately if the surrounding workflow requires it.

**Independent requirement:** record(receipt)=digest(output) only AFTER successful invocation.

**Negative control:** An audit decorator does not make a distributed operation transactional. A crash after external action but before logging can leave missing evidence; a crash after logging but before completion can produce misleading partial records unless state transitions are separately modeled.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 07: Pipes and filters with verifiable intermediate results

**Exact reference:** `composition.Pipeline.run`.

**Constructed test:** Build a two-stage pipeline where the first stage converts an integer into {v:x+1}, and the second multiplies that field by three. With x=2, output {v:9} and two intermediate receipts. Mutate the second stage to a different calculation and verify its result digest changes. Reject an empty pipeline and a noncallable stage.

**Independent requirement:** x_(i+1)=f_i(x_i); each intermediate SHA256 is part of the receipt.

**Negative control:** Pipelines do not guarantee transactional side effects or identical behavior under parallel execution. A physical sensor or network source requires separate timing, provenance and replay controls. The full chain's correctness is not established solely by intermediate hash equality.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 08: State machines with explicit forbidden transitions

**Exact reference:** `state.StateMachine, state.recovery_machine`.

**Constructed test:** Start idle; prepare -> prepared; validate -> verified; commit -> committed. From idle try commit directly: refuse, state and trace unchanged. From prepared reject -> hold; reset -> idle. Execute identical sequences in separate instances and compare history digests. Deliberately declare duplicate transitions to show that an ambiguous graph is refused at initialization.

**Independent requirement:** next = T(current,event), undefined T is a failure not a self-loop.

**Negative control:** A discrete state machine does not prove physical interlocking or enforce electrical disconnection. Devices, mechanical actuators, and power supplies require external sensors, fail-safe hardware, verified timing and qualified operators.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 09: Retry with bounded attempts and explicit idempotency preconditions

**Exact reference:** `resilience.bounded_retry`.

**Constructed test:** Make an operation fail twice with a designated transient OSError, then succeed on its third call. The retry wrapper returns attempt count three. Next make an operation fail with a ValueError that is not designated transient; it must be raised immediately. Repeat with retries set to zero and prove exactly one attempt. Do not use this simple wrapper to send repeated machine commands without durable command identification.

**Independent requirement:** attempts<=1+retry_budget; retry only if chosen exception is transient.

**Negative control:** The reference does not know whether a prior external operation committed. A local retry success does not imply exactly-once delivery to a robot, industrial controller, database on another host or medical instrument. Classification is policy, not an objective property proven by exception type.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 10: Circuit breaker states and recovery under unreliable dependencies

**Exact reference:** `resilience.CircuitBreaker`.

**Constructed test:** With threshold two and reset interval five, record failures at ticks 0 and 1. An attempt at tick 2 is rejected. At tick 6 the breaker admits one half-open probe; a simultaneous second probe is rejected. Record a successful probe and confirm the breaker closes. Repeat with a failed probe: it must reopen. Try a backward clock tick and verify refusal.

**Independent requirement:** closed --threshold failures--> open --cooldown--> half_open --probe--> closed/open.

**Negative control:** A circuit breaker does not guarantee service availability, safety, or failover. Network and resource errors may require human intervention; an overly aggressive breaker can block recovery. State in this model is in memory unless independently persisted.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 11: Bulkhead capacity partitioning and blast-radius limits

**Exact reference:** `resilience.Bulkhead`.

**Constructed test:** Set lane search capacity one and restore capacity two. Acquire search once and verify a second search acquisition is refused while restore can still acquire twice. Release the search lease and verify it becomes available. Try releasing an unacquired lease or allocating a boolean-sized capacity: reject. The result must include independent per-lane counts.

**Independent requirement:** allocated[lane] <= capacity[lane] independently for every lane.

**Negative control:** A thread counter does not preempt a deadlocked task, enforce CPU memory limits, or isolate crashes in separate processes. Real isolation requires worker supervision, timeouts, process/container boundaries and instrumented resource limits.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 12: Queues, backpressure, duplicates and delivery guarantees

**Exact reference:** `resilience.Bulkhead and ledger.CommandJournal`.

**Constructed test:** Model a queue lane with two available slots and attempt a third acquisition. The third must be refused without increasing the recorded allocation. Process a command with a stable id in the SQLite journal, then submit the same id and payload again; the reducer must not run a second time. Change the payload under the old id: fail closed rather than reusing a conflicting result.

**Independent requirement:** admitted_work <= declared_capacity; at-least-once != exactly-once effect.

**Negative control:** The package does not include a production broker, distributed consensus, network partitions, poison-message dead-letter storage, or a measured throughput guarantee. This chapter records the missing contracts for the eventual Distributed Systems Atlas.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 13: Command identity and database-local idempotent effects

**Exact reference:** `ledger.CommandJournal.execute`.

**Constructed test:** Insert command ID c1 with {a:5,b:7}, using a pure reducer that returns {sum:12}. Submit the same command again and assert the reducer ran once; the replay returns the exact stored result with new_commit=False. Now reuse c1 with {a:5,b:8}: refuse. Close SQLite, reopen the database and verify c1 persists with a valid hash chain.

**Independent requirement:** same ID + same payload -> same committed row; same ID + different payload -> error.

**Negative control:** The reducer must be pure and deterministic. If it sends a command to a printer before database COMMIT, a later retry can send it again after a crash. A local unique ID does not establish exactly-once actuation, distributed exactly-once effects, or physical safety.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 14: Unit of Work, SQLite transactions and rollback boundaries

**Exact reference:** `ledger.CommandJournal`.

**Constructed test:** Make a reducer raise after a transaction has begun. The database must roll back and contain zero committed commands for that ID. Submit a valid command afterward; the sequence must begin at one. In a separate test mutate a stored result directly using SQLite and verify the journal's independent hash-chain audit reports corruption. Read SQLite's official WAL and atomic-commit documentation for host/storage caveats.

**Independent requirement:** BEGIN IMMEDIATE; validate->reduce->insert->COMMIT or ROLLBACK.

**Negative control:** SQLite durability depends on the operating system, filesystem, disk controller, flush implementation and power conditions. A passing unit test on a desktop cannot substitute for controlled power-cut experiments. Do not claim transactional consistency between SQLite and a printer, actuator, or independently committed external database.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 15: Hash-chained command history with independent replay checks

**Exact reference:** `ledger.CommandJournal.verify_replay`.

**Constructed test:** Commit two commands and capture the final head hash. Reopen SQLite and confirm the same head. Use a separate SQLite connection to alter result_json without updating the recorded hash: replay must fail. Test a changed payload and a broken previous-hash link. A recovered journal that fails a hash audit must enter a HOLD state instead of silently deriving new snapshots from untrusted history.

**Independent requirement:** H_i=SHA256(seq,id,payload_sha,payload,result,prev=H_(i-1)).

**Negative control:** Hash chains are not digital signatures or tamper-proof logs when the attacker controls the entire file. Reliable audit needs separately anchored head values, trusted timestamps, key management or independent replicas, as appropriate. Crash durability also needs physical storage testing.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 16: Event sourcing with immutable blobs and a versioned head pointer

**Exact reference:** `events.EventChain, atomicfiles.ContentStore`.

**Constructed test:** Append events {n:1} and {n:2}, close the process and construct a new reader from the same directory. Replay must return both in order with the same head hash. Corrupt the head pointer to an unknown digest: the next append and replay must refuse. Limit replay length to a declared bound and test rejection when the event chain exceeds it.

**Independent requirement:** entry_i={event_i,prev:H_(i-1),sequence:i}; head points to last hash.

**Negative control:** The sample is single-writer only; two concurrent writers can race on the same head and one update may be lost. A hash chain whose pointer is not independently anchored does not resist an attacker rewriting all content. Event sourcing can also expose sensitive information unless retention and access controls are engineered separately.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 17: Content-addressed immutable artifacts and integrity checks

**Exact reference:** `atomicfiles.ContentStore.put/get`.

**Constructed test:** Store the bytes of a small offline instruction file. The returned name must equal SHA-256 of those bytes. Store the same bytes again and verify the name is unchanged. Corrupt the stored blob through a separate test tool and require the next retrieval to fail. Submit a malformed hash or too-large file: reject it before writing.

**Independent requirement:** blob_name=SHA256(blob_bytes); retrieval recomputes the digest.

**Negative control:** Content-addressed naming is not secure provenance without a separately trusted digest. One local copy is also vulnerable to physical media failure. Multi-disk backups, verified redundancy and lawful redistribution are required for meaningful long-term survival.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 18: Atomic same-filesystem pointer replacement and rollback design

**Exact reference:** `atomicfiles.ContentStore.publish`.

**Constructed test:** Publish an initial head pointing at blob A, then update it to blob B. A fresh reader must see the complete digest for B, while blob A remains retrievable by hash. Attempt a path traversal tag or symlink head: the operation must fail. A power interruption simulation can test the software's handling of stale/missing pointers, but cannot certify actual Windows or Linux storage devices under a power cut.

**Independent requirement:** write temp->fsync(file)->os.replace(temp,head)->best_effort_fsync(parent).

**Negative control:** os.replace provides atomic rename semantics on appropriate platforms and filesystems; it does not by itself guarantee power-loss atomicity or synchronous commit across SQLite and filesystem storage. Not all filesystems safely support directory fsync or network shares. Test on the actual device before a blackout-readiness claim.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 19: Recovering a derived snapshot after a committed journal update

**Exact reference:** `workflow.RecoveryWorkflow.apply/recover`.

**Constructed test:** Commit command A normally. Commit command B but deliberately raise a simulated interruption before publishing its snapshot. Close the process. Reopen the journal, validate every hash-chain link, and call recover(): it should detect that the snapshot head is stale and reconstruct a two-command view. A second recover should return recovered=False because the views now agree. Corrupt the existing snapshot pointer: refuse silent repair and require an operator to establish a trusted recovery basis.

**Independent requirement:** authoritative_journal_head != snapshot_head -> reconstruct derived view.

**Negative control:** A real controller can have other nonrebuildable state, including motor movements, heat, physical stock or remote financial transactions. Such effects are not rolled back by rebuilding a database view. The demonstration only certifies deterministic software-level derived state under its explicit model.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 20: CQRS-style separation of command authority and read projections

**Exact reference:** `workflow.RecoveryWorkflow`.

**Constructed test:** Commit two journal entries while intentionally interrupting publication after the second. The old snapshot contains one entry, while the verified authoritative ledger contains two. Calling recover reconstructs the projection; repeat without new commands to verify idempotent read results. The projection should not cause a second execution of the reducer or any physical device output.

**Independent requirement:** read_view = f(verified_committed_journal); commands do not trust stale projections.

**Negative control:** A read-projection pattern does not guarantee freshness without a defined synchronization protocol. This reference is single-host and local; distributed replicas, interleaved writers and conflict resolution belong to the Distributed Systems Atlas, not to an unproven local transaction claim.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 21: Cache-aside, invalidation and the limits of stale knowledge

**Exact reference:** `workflow snapshot revision comparison; Computer Architecture cache reference`.

**Constructed test:** Commit a new journal entry and deliberately leave the derived snapshot stale. The read-side recovery compares hashes, detects revision mismatch, and reconstructs a fresh projection. A second read returns the same digest without rebuilding. Contrast that with deliberately modifying a cached byte without its source update: retrieval must detect corruption or refuse inconsistent evidence rather than returning it as authoritative.

**Independent requirement:** cache_valid iff cache_revision == authoritative_revision.

**Negative control:** Cache coherence across multiple machines is not solved by local SHA-256 comparisons alone. Read stale values can be dangerous for control systems and medicine; real service deadlines, network partitions and consistency models require explicit designs and external validation.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 22: Software supply-chain evidence, rights, and untrusted inputs

**Exact reference:** `contracts.parse_envelope, evidence receipts`.

**Constructed test:** Build a compact release with a source manifest, test receipt and exact restore instructions. Modify a single source byte and verify that the file digest no longer matches. Feed an oversized JSON message and a nested malicious-looking path to the strict parser, which must reject them. Document each failure and its source revision. Ensure original third-party publications are only linked, not copied without rights clearance.

**Independent requirement:** release_acceptance = artifact_integrity AND scoped_tests AND independent_provenance.

**Negative control:** The reference parser is not a comprehensive hostile-data sandbox; pure Python strategies are not safe to execute from untrusted sources. Production threat modeling, independent code review, dependency scanning and patch management remain open work.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 23: Property-based, differential and interruption-oriented test design

**Exact reference:** `evidence/independent_oracle.py and tests`.

**Constructed test:** Generate 2,048 synthetic versioned envelopes with shuffled key order, verify canonical digest agreement and reject unauthorized modification. Generate 1,280 valid state-machine sequences and compare each transition with an independent hand-coded table. Run 500 circuit-breaker traces with a separately coded reference model. Inject a crash after journal commit and verify recovery from a fresh process. Report the exact number of comparisons, categories and test failures, not a vague claim of formal proof.

**Independent requirement:** oracle(inputs) == implementation(inputs) for explicit finite test set.

**Negative control:** Finite testing cannot establish correctness for all programs or operating conditions; models can share a mistaken requirement. Independent audit, deterministic build reproducibility and tests on target operating systems are needed before life-safety or critical infrastructure adoption.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

## Case 24: Reconstructing resilient software without network services

**Exact reference:** `python -m patterns_atlas; workflow.RecoveryWorkflow`.

**Constructed test:** Run `python -m patterns_atlas` from a clean extracted package. It should report a committed result of 12 for a 5+7 calculation, simulate an interrupted later command, reopen its SQLite journal, and reconstruct a two-entry snapshot without repeating a pure reducer. Repeat the test on the target Windows machine. Compare actual file hashes, SQLite journal-mode behavior, filesystem flush semantics and USB storage recovery. Preserve a short README with command syntax and negative cases.

**Independent requirement:** source + tests + schema + journal + snapshots + evidence -> reproducible bounded recovery.

**Negative control:** A successful offline software run does not certify local power backup, filesystem crash consistency, hardware control, or 3D printer functionality. An independent technician must test actual recovery hardware, battery conditions, source authenticity and safe operating procedures. The next original Atlas domain is Distributed Systems (#12), where multi-host consensus, retries and network partitions can be studied separately.

**Acceptance boundary:** no physical/production hardware or independent external scientific assurance provided.

