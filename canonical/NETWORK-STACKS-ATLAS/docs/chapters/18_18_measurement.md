# 18 — Network measurements, clocks and uncertainty

**Scientific question.** Which measurements are needed to validate a reconstructed stack on real equipment?

## Definitions, physical assumptions and scope

Network performance requires jointly recording packet loss, one-way/two-way latency, jitter, transfer size, timestamp uncertainty, clock synchronization, payload integrity, link-layer errors and protocol retransmissions. Software-internal event timestamps are not hardware network timing evidence.

## Governing principle and derivation

Approximate throughput = received useful application octets ×8 / elapsed seconds, excluding headers when labeled application-goodput. Measured one-way delay requires two clock error models; a round-trip observation cannot uniquely determine asymmetry.

**Equation / invariant:** `goodput = 8*delivered_application_bytes / elapsed_seconds`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

A constructed 1,000,000-byte transfer over 2.0 s gives 4 Mbit/s useful-data goodput before considering retransmissions, excludes framing overhead and is not a wire measurement.

## Reconstructible offline procedure

Record capture interface, timestamp clock and resolution, OS/kernel, NIC, link MTU, checksum offload state, bytes/packets and replay seed. Compare normal and negative-control traces.

## Independent test or negative control

An apparently valid checksum captured while NIC offload is enabled can reflect deferred hardware work; treat it as a capture-context ambiguity.

## Known failures, uncertainty and acceptance gates

No traffic captures, real NIC timing, certified metrology or external device comparison.

## Source pointers (not authenticated publisher files)

- RFC9293: Transmission Control Protocol (TCP) (August 2022 (obsoletes RFC 793)), https://www.rfc-editor.org/info/rfc9293/
- RFC9000: QUIC: A UDP-Based Multiplexed and Secure Transport (May 2021), https://www.rfc-editor.org/info/rfc9000/

**Exact predecessor dependencies:** measurement-atlas, os-internals-atlas. See immutable relation revisions in `data/relations.jsonl`.

