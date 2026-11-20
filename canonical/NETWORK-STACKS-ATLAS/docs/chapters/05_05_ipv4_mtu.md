# 05 — IPv4 MTU, fragmentation and PMTU limits

**Scientific question.** How can an application compute a conservative payload ceiling from link MTU?

## Definitions, physical assumptions and scope

MTU is a per-path, not just per-host, limit. An IPv4 base header contributes 20 bytes; UDP contributes 8, while IP options/tunnels add overhead. IPv4 fragmentation is not used by the reference and may be blocked or unreliable in real networks.

## Governing principle and derivation

With packet MTU M and known header widths H_ip,H_transport, the upper payload budget is max(0,M-H_ip-H_transport) under a no-option, no-tunnel assumption. PMTU discovery must account for ICMP feedback, black holes and path change.

**Equation / invariant:** `L_payload_max = M - H_IP - H_transport (only under declared header assumptions)`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

At M=1500, IPv4 with 20-byte base header and 8-byte UDP header has maximum modeled UDP data payload 1472 bytes.

## Reconstructible offline procedure

Record link MTU, discovered path MTU, overhead and protocol version. Reject payload exceeding computed limit and mark unknown tunnels/extensions as evidence gaps.

## Independent test or negative control

An operator who assumes 1472 bytes across a 1280-byte encapsulated path will oversize packets; a successful local calculation does not establish successful route delivery.

## Known failures, uncertainty and acceptance gates

No real PMTU discovery, ICMP blackhole recovery, IPv4 fragmentation/reassembly or tunnel negotiation.

## Source pointers (not authenticated publisher files)

- RFC1191: Path MTU Discovery (November 1990), https://www.rfc-editor.org/info/rfc1191/
- RFC791: Internet Protocol, IPv4 (September 1981), https://www.rfc-editor.org/info/rfc791/
- RFC768: User Datagram Protocol (August 1980), https://www.rfc-editor.org/info/rfc768/

**Exact predecessor dependencies:** os-internals-atlas, distributed-systems-atlas. See immutable relation revisions in `data/relations.jsonl`.

