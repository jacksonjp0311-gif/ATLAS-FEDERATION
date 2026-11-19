# 12 — TCP RTT estimation and retransmission timeout

**Scientific question.** How can RTT observations be converted to a conservative retry timer?

## Definitions, physical assumptions and scope

A basic RFC 6298 estimator tracks smoothed RTT (SRTT), RTT variation (RTTVAR) and a retransmission timeout (RTO). RTT samples from ambiguously retransmitted segments are not directly eligible; Karn-style exclusion and exponential backoff matter. The numeric reference models only the arithmetic.

## Governing principle and derivation

For later sample R: RTTVAR←(1−β)RTTVAR+β|SRTT−R|, SRTT←(1−α)SRTT+αR, where α=1/8, β=1/4. Then RTO←max(1s,SRTT+max(G,4RTTVAR)) in the bounded reference.

**Equation / invariant:** `RTO = max(1 s, SRTT + max(G,4 RTTVAR))`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

First sample R=0.25 s yields SRTT=.25 s, RTTVAR=.125 s and floored RTO 1 s; a later .35 s sample yields updated smoothed estimate .2625 s.

## Reconstructible offline procedure

Use a recorded eligible RTT series, independent Decimal arithmetic and explicit granularity G. Document whether retransmissions, delayed ACKs and timer precision make any sample ineligible.

## Independent test or negative control

A measured retransmitted ACK with ambiguous provenance must not be used as a clean RTT sample despite being a finite positive number.

## Known failures, uncertainty and acceptance gates

No Karn logic, timeout backoff, SACK, congestion window or live TCP engine.

## Source pointers (not authenticated publisher files)

- RFC6298: Computing TCP Retransmission Timer (June 2011), https://www.rfc-editor.org/info/rfc6298/
- RFC9293: Transmission Control Protocol (TCP) (August 2022 (obsoletes RFC 793)), https://www.rfc-editor.org/info/rfc9293/

**Exact predecessor dependencies:** os-internals-atlas, control-atlas. See immutable relation revisions in `data/relations.jsonl`.

