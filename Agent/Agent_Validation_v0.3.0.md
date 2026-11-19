# Agent Atlas v0.3.0 — audited scope and reproduction

**Status:** tested research-content checkpoint, not an empirical agent improvement or release-certified autonomous system. No router has been modified.

## Reproducible tests

- Full seven-node regression: **1,161 tests passed, zero skipped**: Forge 188, Measurement 218, Causal 233, Materials 122, Control 244 and Agent **156**. All 16 representative source-linked contexts validate.
- **7,750** independently implemented NumPy/discrete-clock comparisons: 250 overlap checks, 1,500 recovery precedence states, 2,800 MAST positive counts, 2,800 missing-label counts, 400 repeated-task pass-all checks. These are author-generated fixtures, **not** actual model evaluations.
- Clean isolated package installation: six Python distributions available; Agent v0.3 wheel exposes 128 source-linked records and runs casebook/context from outside the source checkout.
- Prior **100 Agent records and 63 relations** retain exact revisions; **1,151 prior shared record revisions and 392 prior shared relation revisions** remain intact. Historical unmodified node and baseline file bytes also checked.
- MAST-Data official source schema and CC BY 4.0 dataset card checked; **zero original full trace rows imported**, no independently verified human labels. An empirical grouped-rate claim would be unsupported.

## What is deliberately not claimed

No live agent or external provider call, durable idempotency implementation, prompt-injection-proof agent, security audit, causally identified performance gain, independent expert review, Held-out benchmark, Bitwork router, GitHub publication or Windows desktop run.

OpenTelemetry GenAI semantic conventions are in development; the local adapter accepts a restricted metadata subset rather than arbitrary OTLP. AWS idempotency discussions describe provider contracts the offline module does not enforce. Author-created tests verify code behavior, not permissions, remote truth or deployment reliability.

## Reproduction commands

```sh
python tools/check_collection.py --out receipts/unique-new-folder
cd AGENT-ATLAS
python -m agent_atlas v03-casebook
python -m unittest discover -s tests -q
python tools/v03_numerical_oracle.py
```

The last script requires optional NumPy; core Agent methods have standard-library runtime dependencies only. Every release archive is verified by file hashes and an extracted-suite replay. Source rights and privacy audits remain a separate human responsibility.
