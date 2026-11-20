# Investigation 14 — A hash, signature, and KEM solve different problems

**Origin:** original security reference exercise. Two files yield matching SHA-256 digests relative to a separately trusted expected hash. That supports byte consistency against that expected value; it does not prove who originally wrote either file. A signature scheme aims to authenticate a signed message under key assumptions; a KEM produces shared-key material under public-key assumptions. NIST FIPS 203 describes ML-KEM, not a universal replacement for signatures or author identity.

**Failure case:** an attacker replaces both a data file and its unsigned expected hash. The naive checksum check passes; the provenance claim does not. Operational signature and key custody tests are out of scope, and the NIST 2025 errata-planning notice requires version-qualified language.
