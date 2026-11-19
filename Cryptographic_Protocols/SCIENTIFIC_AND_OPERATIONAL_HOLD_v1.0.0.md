# Cryptographic Protocols — Scientific and Operational HOLD

| Gate | Status | Evidence required to clear |
|---|---|---|
| Offline HMAC/HKDF published vector agreement | TESTABLE | RFC 4231 / RFC 5869 oracle execution receipts |
| Framing, anti-replay, MAC-only role model | TESTABLE | Independent finite oracle and negative controls |
| Merkle membership example | TESTABLE | Independent tree oracle, altered-leaf negatives |
| Full certified TLS 1.3/AEAD/HPKE implementation | HOLD | External interoperable library and full protocol conformance suite |
| Ed25519, X25519, X.509, randomness service | HOLD | Actual vetted implementations and test vectors |
| Constant-time, physical side-channel and entropy testing | HOLD | Real target hardware, instrumentation and review |
| Authenticated original publisher files and rights | HOLD | Licensed originals, hashes, edition/revision validation |
| Independent expert cryptographic review | HOLD | Signed independent audit and scoped adversarial assessment |
| Physical power-loss replay / nonce durability | HOLD | Power-cycle failure injection with stable keys/epochs |
| Atlas federation archive preservation | TESTABLE | Full predecessor/patch reconstruction and regression |

Scoped technical-content v1 means only original scientific explanation, reference arithmetic, simulation and source-linked correctness evidence. It does **not** mean the software can protect user traffic or key material.
