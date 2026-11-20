# Investigation 01 — Worker result survives but the parent does not

**Origin:** constructed trace. This is not a capture of a running PEGASUS agent. A parent starts task T; a child computes a proposed result; the parent suffers a tool timeout before adopting that result. A naive system either discards the child output or assumes that a successful child message is an approved final answer. Both are incorrect.

Build a receipt from exact `(task_id,child_run_id,output)` bytes, then verify its local SHA-256 and task identity. The `receipt_survival` function returns **eligible for parent verification** only while the parent ledger is nonterminal. It does not claim a durable restart, signatures, verified outcome or conflict-free external side effects. An attacker or operator who can rewrite the whole ledger could forge the hash chain; a production system needs authenticated, durable stores.

**Failure hypotheses:** child output was never produced; parent missed a completed result; result belongs to a foreign task; receipt was altered; tool side effects occurred but acknowledgment was lost; parent was actually stopped by the operator. Each has a different required test. Preserve tool call IDs and actor in the journal. Do not resume after operator stop.

**Observed offline results:** valid local receipt hash admitted as a candidate, foreign receipt rejected, changed payload rejected, terminal stop rejects resumption. **Not observed:** a model making decisions, a live crash, a production database, or a genuine learning gain. Cite exact failure condition and required independent checks.

**Sources:** LangGraph persistence guide and MAST multi-agent failure taxonomy, linked in Chapter 07/12.
