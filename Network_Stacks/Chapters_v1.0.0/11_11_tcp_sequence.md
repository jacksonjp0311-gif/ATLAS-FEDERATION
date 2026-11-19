# 11 — TCP sequence space, receive windows and wraparound

**Scientific question.** Which TCP byte ranges are acceptable to a receiver?

## Definitions, physical assumptions and scope

TCP sequence positions lie in 32-bit modular space. SYN and FIN each occupy sequence space. Acceptability depends on RCV.NXT, RCV.WND and segment length, with a special zero-window case. The receiver state is not just a simple unsigned comparison.

## Governing principle and derivation

For uint32 x and base y, forward distance d=(x−y) mod 2^32. Under a bounded half-range assumption, a zero-length segment fits a nonzero receive window when d<W; a nonzero segment fits when its first or last occupied byte lies in the window.

**Equation / invariant:** `d=(SEQ−RCV.NXT) mod 2^32; accept iff boundary overlap within W`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

With RCV.NXT=2^32−2, W=4, data SEQ=0 length=1 is acceptable, while SEQ=4 is outside. With W=0, only zero-length at RCV.NXT passes.

## Reconstructible offline procedure

Compare a bounded implementation with a literal enumeration of admissible sequence numbers including wraparound and zero-window controls.

## Independent test or negative control

Naive unsigned SEQ>=RCV.NXT fails around 2^32 wrap. Passing this check is not a connected TCP session or transport authentication.

## Known failures, uncertainty and acceptance gates

No ACK generation, connection handshake, PAWS, RST/SYN/FIN processing, congestion control or full RFC conformance.

## Source pointers (not authenticated publisher files)

- RFC9293: Transmission Control Protocol (TCP) (August 2022 (obsoletes RFC 793)), https://www.rfc-editor.org/info/rfc9293/

**Exact predecessor dependencies:** os-internals-atlas, distributed-systems-atlas. See immutable relation revisions in `data/relations.jsonl`.

