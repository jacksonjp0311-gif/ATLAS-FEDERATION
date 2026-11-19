# 19 — Completed histories and the linearization witness

**ATLAS FORGE / Distributed Systems / original scoped content v1.0.0 / chapter 19**

## Scientific question

When does an observed register history admit a single atomic sequence consistent with wall-clock ordering?

## Mathematical and engineering foundation

A completed operation has an invocation time s and response time e, with s<e. If operation A completed before B began, then A must precede B in any valid linearization. Overlapping operations have no forced order from time alone. A legal sequential register starts with a known value r0; a successful write(v) replaces r, and read() returns the current r. The checker seeks any permutation of completed operations that respects non-overlap precedence and sequential register semantics. It must not label unknown or pending invocations as confirmed failures or successes.

## Derivation and formal invariant

Define a directed precedence edge A->B when end(A)<=start(B). A sequential witness is a topological ordering of this real-time partial order that satisfies read and write specification. A write of value '1' at [1,2] followed by a read at [3,4] returning '0' has no witness (assuming initial '0' and no intervening write). If write spans [1,5] and the read spans [2,3], a read of '0' can be linearized before that write; stale-looking response is not automatically a violation.

## Worked constructed investigation

Run `history_witness([Op('w','write',1,2,value='1',result='ok'), Op('r','read',3,4,result='1')])`: witness ('w','r'). Change only the returned read value to '0': the witness becomes None. Overlap the two intervals and the same '0' read is consistent. Verify the implementation against a separate brute-force permutation oracle over 1,000 finite three-operation histories.

## Reproduction procedure and negative control

Cap the number of completed operations at nine to avoid pretending this exponential checker scales. Reject invalid time intervals, duplicate IDs, unsupported methods and unobserved return values. A real distributed-service history must include client-clock error estimates, process IDs, invocations, responses, and what happened to indeterminate operations after timeout.

## Assumptions, evidence class and known failures

This is a one-register educational checker. It is not Elle, Jepsen, multi-key serializability, a proof of real-time clock accuracy, or a general database consistency auditor.

The equations and protocols are educational reference models, not authenticated original publisher text. Integer ballot numbers and node counts are dimensionless. Logical event ticks are not calibrated seconds; measured physical time is required to make latency claims. All claims must retain source qualification, model bounds and unverified evidence status. A future system must not treat absence of counterexamples in this finite model as universal correctness.

## Software, reference, and future validation

Reference: `distributed_atlas/linearizability.py`. Bibliographic source card: `distributed-systems-atlas:source:LINEAR1990` at exact revision `cdceae6ef1d6c67c420c4e19a5b4d9f1606b61946140365a760b45f5bbfe413d`. Full source locator: https://www.cs.columbia.edu/~wing/publications/HerlihyWing90.pdf. No publisher original PDF is bundled; no rights to redistribute external paper content are asserted. Independent physical or qualified external review: **HOLD**.
