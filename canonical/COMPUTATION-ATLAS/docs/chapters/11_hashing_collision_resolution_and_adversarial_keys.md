# Chapter 11 — Hashing, collision resolution, and adversarial keys

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A hash table maps keys to buckets using a hash function and capacity. Expected O(1) operations depend on assumptions about hash distribution, load factor, and adversarial inputs. Collisions are unavoidable when the key universe exceeds the bucket count; collision handling is part of correctness, not an optional optimization. Separate chaining stores multiple keys per bucket, while open addressing probes alternative slots. A hash digest used for data integrity has different security properties from the hash function used for table indexing. Cryptographic hash collision resistance does not authenticate the party who created a file or guarantee that a scientific claim is true. Hashable-key equality and hashing must be consistent for dictionary invariants to hold.

## Formal statement, symbols, and units

Load factor α=n/m for n keys and m buckets. Index h(k) mod m. Pigeonhole principle: if n>m then at least one collision exists.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

In a chaining table, lookup examines the indexed bucket and must compare full keys because different keys may hash alike. Rehashing at a threshold can yield amortized insertion bounds even though an individual resize costs O(n). Under adversarial collision patterns, many operations can degrade to linear time. Comparing the expected-case claim against worst-case input shows why the model's distribution assumption matters.

## Reconstruction exercise with independently checkable output

Construct a toy table of five buckets, insert keys 1,6,11 and inspect their shared bucket. Search for each key and a missing colliding key. Repeat the design with open addressing to analyze deletion semantics.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not mistake SHA-256 for an identity signature, conflate record revision hashes with experimental validation, or use a non-cryptographic checksum as a security proof.

## Source orientation

- Pat Morin, Open Data Structures: https://www.opendatastructures.org/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- NIST FIPS 180-4 Secure Hash Standard: https://csrc.nist.gov/pubs/fips/180-4/upd1/final

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
