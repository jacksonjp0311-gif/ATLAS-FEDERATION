# 09 — CIDR, longest-prefix forwarding and route policy

**Scientific question.** What is the deterministic selection rule for overlapping destination prefixes?

## Definitions, physical assumptions and scope

CIDR prefixes form a partial order by address set inclusion. An IP address matches every network containing it, and the longest matching prefix is the most specific. Real systems also require routing tables, interface status, next-hop reachability, administrative distance and policy.

## Governing principle and derivation

For integer address A and prefix length p of width W, mask M=((2^p−1)<<(W−p)); A matches route N when (A & M)==(N & M). The maximal p wins in the bounded no-policy reference.

**Equation / invariant:** `route(A) = argmax_{N contains A} prefix_length(N)`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

For destination 10.12.4.7 and routes 0.0.0.0/0, 10.0.0.0/8 and 10.12.0.0/16, the /16 route wins.

## Reconstructible offline procedure

Build a table of known CIDR prefixes; use an exhaustive enumeration and an independent standard-library mask oracle to verify every choice and address-family mismatch.

## Independent test or negative control

If a maliciously advertised /25 overrides a benign /24, longest-prefix forwarding still works mathematically while network trust fails. Source authenticity is an independent requirement.

## Known failures, uncertainty and acceptance gates

No BGP/RPKI, weighted ECMP, recursive next-hop or measured convergence.

## Source pointers (not authenticated publisher files)

- RFC4632: Classless Inter-domain Routing (CIDR) (August 2006), https://www.rfc-editor.org/info/rfc4632/
- RFC1918: Address Allocation for Private Internets (February 1996), https://www.rfc-editor.org/info/rfc1918/
- RFC4271: A Border Gateway Protocol 4 (BGP-4) (January 2006), https://www.rfc-editor.org/info/rfc4271/

**Exact predecessor dependencies:** os-internals-atlas, distributed-systems-atlas. See immutable relation revisions in `data/relations.jsonl`.

