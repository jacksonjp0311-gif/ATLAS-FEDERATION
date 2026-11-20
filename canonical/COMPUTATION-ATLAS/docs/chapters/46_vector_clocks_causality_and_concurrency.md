# Chapter 46 — Vector clocks, causality and concurrency

**Area:** Distributed Systems. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Distributed processes do not necessarily share an exact global wall clock. Event causality is better described through local order and message transmission: an event happens before another if they occur in order on one process, if the first sends a message received by the second, or by transitive closure. Lamport logical clocks respect this ordering but cannot infer causality merely from a smaller scalar timestamp. Vector clocks extend the idea with one counter per participant, allowing a partial-order test under fixed participants and correct message propagation.

## Mathematical contract

Vector clocks a,b: a→b iff a_i≤b_i for every i and a_j<b_j for at least one j. If neither a≤b nor b≤a, the events are concurrent. Equal vectors are not independent identity proof.

## Derivation and reasoning

Local events increment one component; receipt merges component-wise maxima with the received timestamp, then increments the local component. These rules preserve causality because message receipt vector components dominate the sender's state. For two independent local events from (0,0), resulting vectors (1,0) and (0,1) are concurrent; comparing their physical time stamps cannot establish a causal relationship without additional evidence.

## Worked reconstruction and independent check

Start with two actors A and B. Tick A to (1,0), independently tick B to (0,1). Their events are concurrent. Let B receive A's message, merge to (1,1), then increment B to (1,2): A's earlier event happened before the receipt. Run the bounded vector-clock methods to reproduce these relations.

## Limitations, falsification, and invalid use

A vector clock does not authenticate actors or ensure a provider operation succeeded. Dynamic membership, malicious timestamps and missing messages require additional protocols. Never turn a comparison of timestamps into an authorization decision.

## Cross-domain meaning

Agent parent/worker handoff and SYMBIOTE learning exchange may benefit from causal envelopes, but no runtime connection is implemented here.

## Source orientation and recoverability

- [Lamport, Time, Clocks and the Ordering of Events in a Distributed System](https://lamport.org/pubs/time-clocks.pdf) — original publisher bytes unavailable in this package.
- [MIT OpenCourseWare 18.S191 Introduction to Computational Thinking](https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
