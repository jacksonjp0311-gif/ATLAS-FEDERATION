# Investigation 02 — An error is not a stop, and a stop is not an error

**Origin:** constructed actor/action journal. The agent's task is to collect a report, analyze it and deliver a verified conclusion. A tool call returns an error. A defective runtime might treat a third consecutive tool error as an operator Stop command. This confuses failure handling with user intent.

Agent Atlas represents a tool error with `{actor:'tool', action:'tool_error'}`. It remains a nonterminal journal event; a parent may choose a bounded retry if authorization and side-effect reconciliation permit. By contrast, `{actor:'operator',action:'stop'}` is terminal and cannot be followed by an implicit retry. A worker cannot impersonate the operator by emitting the stop event type. A final commit from an authorized parent is also terminal for the declared run. These are testable finite-state invariants.

The example does not imply that a tool error always should be retried. If the tool performs a non-idempotent operation, the error may conceal a completed external action. Reconciliation with provider state and host policy is needed before attempting the action again. Repeated retries without new evidence can worsen risk and cost.

**Results:** local journal verification detects a mutated middle event, truncated prefix and unauthorized stop actor. No filesystem durability or external actor authentication was tested. Real implementation needs trusted host logs and transaction commits. A useful study would reproduce the historical error trigger and prove it no longer invokes the native operator Stop path.

**Source pointer:** LangGraph checkpointing documentation; OWASP excessive agency cautions.
