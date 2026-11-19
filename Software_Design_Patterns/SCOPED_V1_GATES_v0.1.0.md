# Scoped v1 readiness and evidence gates

| Gate | Reference v0.1.0 | Required independent acceptance |
|---|---|---|
| 24 original source-linked chapters | Available | Qualified editorial/engineering review |
| Strict canonical message schema | Finite deterministic tests | Cross-runtime JSON conformance, adversarial fuzzing |
| Strategy, Factory, Adapter, Decorator, Pipeline | Educational reference code | Actual integration and external API audits |
| Explicit failure state machine | Verified on finite state sequences | Real controller interlock and timing checks |
| Circuit breaker, bounded retry, bulkhead | Logical-clock simulations | Real traffic, fault rates and service level measurements |
| SQLite WAL command journal | Local DB transaction tests | Controlled disk/power failure and concurrency stress |
| Idempotent local command IDs | Enforced within SQLite transaction | No claim of exactly-once physical/remote effect |
| Content-addressed snapshots | SHA256 and atomic local rename | Real filesystem/drive consistency across hard power cuts |
| Event-chain replay | Local single-writer, bounded | Trusted external head anchoring; malicious operator threat model |
| Independent scientific source originals | Unauthenticated | Original publisher bytes, edition, license and claim mapping |
| Independent expert review | Not performed | External qualified reviewer signature and replication |
| Hardware recovery for local user | Not tested | Target ROG, OS, drive, printer and backup supply measured |
| Original 30-domain roadmap preservation | Byte-preserved | Verified historical release-chain restoration |

**v0.1.0 is an engineering content/software reference, not scientific or hardware v1 acceptance.** Keep each HOLD visible. Next original unregistered domain: Distributed Systems #12.
