# ATLAS FORGE — Network Stacks Atlas · scoped scientific reference v1.0.0

Original canonical domain #16. This is ONE federation and extends OS Internals v1.0.0.

This manual documents reconstructible algorithms, assumptions, negative controls, sources and limits.

**Scope boundary:** validated local numerical software models, not a production TCP/IP stack, authenticated network service, TLS library, or physical engineering acceptance.

# 01 — Layering, interface contracts and failure propagation

**Scientific question.** How can a broken wire-level claim be isolated across a layer boundary?

## Definitions, physical assumptions and scope

Distinguish physical signaling, link encapsulation, network forwarding, transport and application semantics. An accepted inner header is not proof of a valid outer frame or authenticated peer. MTU, retransmission and clock assumptions are cross-layer variables.

## Governing principle and derivation

If each of n independently validated layers can fail with probability p_i, an illustrative series-path reliability model is P(success)=product_i(1-p_i). This is not a measured reliability or an independence claim; shared faults invalidate the product. Preserve exact bytes, clocks and evidence provenance at each handoff.

**Equation / invariant:** `P_series = Π_i(1-p_i) [independent-layer illustrative model]`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

For constructed p=(0.01,0.02,0.03), P=0.99×0.98×0.97≈0.941094, not the arithmetic mean of layer successes.

## Reconstructible offline procedure

Start from a known cable/interface, separately verify link frames, IP headers, transport checksum/state, DNS resolution and application authentication. Label the layer whose invariant failed and do not promote the lower-layer result to upper-layer security.

## Independent test or negative control

A well-formed UDP length with corrupted payload is accepted by the length-only model; the correct conclusion is missing integrity coverage, not a reliable payload.

## Known failures, uncertainty and acceptance gates

No physical loss measurements, NIC firmware conformance, layer timing or wire interoperability.

## Source pointers (not authenticated publisher files)

- RFC894: Standard for the Transmission of IP Datagrams over Ethernet Networks (April 1984), https://www.rfc-editor.org/info/rfc894/
- RFC791: Internet Protocol, IPv4 (September 1981), https://www.rfc-editor.org/info/rfc791/
- RFC768: User Datagram Protocol (August 1980), https://www.rfc-editor.org/info/rfc768/

**Exact predecessor dependencies:** os-internals-atlas, computer-architecture-digital-hardware-atlas. See immutable relation revisions in `data/relations.jsonl`.


# 02 — Ethernet II framing and local link ambiguity

**Scientific question.** Which bytes belong to a frame and which belong to the physical medium?

## Definitions, physical assumptions and scope

Ethernet II has 6 destination MAC bytes, 6 source bytes, a 2-byte EtherType and payload. Preamble, inter-frame gap and frame check sequence are separate and must be defined by the capture interface. VLAN-tagged and IEEE 802.3 length-framed cases require different parsing.

## Governing principle and derivation

Header octets = 6 + 6 + 2 = 14; a minimally modeled frame has length 14+payload. This does not imply actual on-wire padding, FCS, time or bitrate overhead. The EtherType discriminator is 0x0600 and above, while length values use a different interpretation.

**Equation / invariant:** `L_model = 14 + L_payload; EtherType ≥ 0x0600`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

A 100-octet upper-layer payload yields 114 modeled octets, but link-layer CRC and hardware padding/capture configuration must be separately established.

## Reconstructible offline procedure

Decode EtherType and MAC addresses from a captured frame; explicitly reject unsupported VLAN tags and truncated headers, then hand off payload to an IP-specific parser.

## Independent test or negative control

If EtherType is 0x8100, a 14-byte parser must abstain rather than mistake the VLAN tag as IPv4 or UDP data.

## Known failures, uncertainty and acceptance gates

No link FCS, actual transceiver, pause frames, Ethernet autonegotiation or measured line coding.

## Source pointers (not authenticated publisher files)

- RFC894: Standard for the Transmission of IP Datagrams over Ethernet Networks (April 1984), https://www.rfc-editor.org/info/rfc894/

**Exact predecessor dependencies:** os-internals-atlas, materials-atlas. See immutable relation revisions in `data/relations.jsonl`.


# 03 — ARP binding and spoofing boundaries

**Scientific question.** How does an IPv4 next-hop destination resolve to a local hardware address?

## Definitions, physical assumptions and scope

Classic Ethernet/IPv4 ARP carries htype=1, ptype=0x0800, hlen=6, plen=4 and op 1 or 2. IP address ownership is not authenticated by ordinary ARP: an arbitrary host can transmit a plausible binding. Cache lifetime and conflict resolution are host policy.

## Governing principle and derivation

The canonical Ethernet/IPv4 ARP payload is 8-byte fixed fields plus 2×(6+4) address bytes = 28 bytes. Only fixed lengths are modeled; this equation cannot attest sender ownership.

**Equation / invariant:** `L_ARP = 8 + 2(hlen+plen) = 28 bytes`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

Given sender MAC 31:32:33:34:35:36 and sender IP 192.0.2.1, decode the request independently and store the observation only with its capture source and timestamp.

## Reconstructible offline procedure

Inspect and reject invalid hardware/protocol types or operations; compare a known trusted binding to the capture. Never treat arbitrary ARP fields as an identity proof.

## Independent test or negative control

A forged ARP reply with the right lengths and fields passes structural parsing; that is a negative security case, not a successful identity check.

## Known failures, uncertainty and acceptance gates

No dynamic neighbor cache, duplicate-address detection, anti-spoofing or switch enforcement.

## Source pointers (not authenticated publisher files)

- RFC826: An Ethernet Address Resolution Protocol (November 1982), https://www.rfc-editor.org/info/rfc826/
- RFC894: Standard for the Transmission of IP Datagrams over Ethernet Networks (April 1984), https://www.rfc-editor.org/info/rfc894/

**Exact predecessor dependencies:** os-internals-atlas, cryptographic-protocols-atlas. See immutable relation revisions in `data/relations.jsonl`.


# 04 — IPv4 header, length, TTL and checksum

**Scientific question.** When does a network-layer datagram satisfy the modeled IPv4 invariants?

## Definitions, physical assumptions and scope

IPv4 version=4, header length IHL in 4-octet words, total length covers header and payload, and TTL is decremented when forwarded. The header checksum covers only the header, not the payload. This model supports IHL=5 without options and explicitly rejects fragmentation.

## Governing principle and derivation

For 16-bit words w_i, fold the one’s-complement sum S=Σw_i with end-around carry until ≤0xffff; checksum C=~S&0xffff. With C in the header, the folded sum should equal 0xffff. A correct checksum does not authenticate a packet.

**Equation / invariant:** `C = ~(fold16(Σ_i w_i)) & 0xffff`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

The 20-byte header plus a 5-byte payload produces TotalLength=25. Flip the TTL byte but preserve checksum: the checksum must now fail.

## Reconstructible offline procedure

Build a nonfragmented packet in network byte order, validate total length, recompute the header checksum, then interpret the source/destination and protocol fields.

## Independent test or negative control

Set MF=1 and recompute checksum; the IPv4 model must reject for unsupported fragmentation rather than falsely report checksum corruption.

## Known failures, uncertainty and acceptance gates

No IPv4 options, routing, PMTU behavior, fragment reassembly or secure IP authentication.

## Source pointers (not authenticated publisher files)

- RFC791: Internet Protocol, IPv4 (September 1981), https://www.rfc-editor.org/info/rfc791/
- RFC1071: Computing the Internet Checksum (September 1988), https://www.rfc-editor.org/info/rfc1071/

**Exact predecessor dependencies:** os-internals-atlas, cryptographic-protocols-atlas. See immutable relation revisions in `data/relations.jsonl`.


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


# 06 — IPv6 fixed header and bounded extension chain

**Scientific question.** Which parts of IPv6 can be parsed without pretending all options are supported?

## Definitions, physical assumptions and scope

IPv6 has a 40-octet fixed header with source/destination addresses of 128 bits, PayloadLength, NextHeader and HopLimit. Extensions are linked by NextHeader. A bounded options-chain model can inspect lengths but cannot execute arbitrary option semantics.

## Governing principle and derivation

For an ordinary non-jumbo datagram, total packet length = 40+payload_length. Options-like extension length in 8-byte units is 8×(HdrExtLen+1). A fragment header is 8 bytes; non-atomic fragments require a separate reassembly policy.

**Equation / invariant:** `L_v6 = 40+L_payload; L_opt = 8(HdrExtLen+1)`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

A fixed IPv6 header declaring 3 payload bytes should be followed by exactly three bytes for this subset; a Hop-by-Hop header of HdrExtLen=0 occupies 8 bytes.

## Reconstructible offline procedure

Decode fixed fields; follow at most eight recognized extension headers; reject truncation, non-atomic fragment processing, unsupported ESP/AH and jumbograms. Consult later RFC updates to Hop-by-Hop processing.

## Independent test or negative control

A valid-looking 40-byte header with a declared 9-byte payload but only 3 available bytes must fail length checks; a fragment offset !=0 must not be treated as a complete datagram.

## Known failures, uncertainty and acceptance gates

No full option actions, IPsec, tunnels, jumbograms, general reassembly or IPv6 interoperability testing.

## Source pointers (not authenticated publisher files)

- RFC8200: Internet Protocol, Version 6 (IPv6) Specification (July 2017 (updated by RFC 9673)), https://www.rfc-editor.org/info/rfc8200/
- RFC9673: IPv6 Hop-by-Hop Options Processing Procedures (2024), https://www.rfc-editor.org/info/rfc9673/

**Exact predecessor dependencies:** os-internals-atlas, cryptographic-protocols-atlas. See immutable relation revisions in `data/relations.jsonl`.


# 07 — IPv6 neighbor discovery and link-local dependence

**Scientific question.** Why is IPv6 neighbor resolution not merely ARP with longer addresses?

## Definitions, physical assumptions and scope

IPv6 Neighbor Discovery uses ICMPv6 messages for router discovery, prefix discovery, address resolution and reachability detection. Link-local scope and hop-limit checks matter. Unauthenticated advertisements can be malicious in many environments.

## Governing principle and derivation

A generic hop-limit decrement has integer relation HL_new=HL_old−1 for forwarding when HL_old>1; Neighbor Discovery imposes additional message-specific validation that is not captured by this simple equation.

**Equation / invariant:** `HL_next = HL_current - 1; ND messages require distinct validation`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

A constructed neighbor solicitation and an IPv6 destination may share the same low 64 bits while differing in scope; they are not equivalent route identities.

## Reconstructible offline procedure

Record the interface index, link-local scope, source of Router Advertisement and neighbor cache state. Refuse to promote an arbitrary ICMPv6 packet to a trusted neighbor entry.

## Independent test or negative control

An off-link packet with Neighbor Discovery message type must not be processed as a valid local neighbor response merely because its bytes parse.

## Known failures, uncertainty and acceptance gates

No validated ND cache, DAD state machine, Router Advertisement authentication or wire tests.

## Source pointers (not authenticated publisher files)

- RFC4861: Neighbor Discovery for IP version 6 (September 2007), https://www.rfc-editor.org/info/rfc4861/
- RFC4443: Internet Control Message Protocol (ICMPv6) (March 2006), https://www.rfc-editor.org/info/rfc4443/
- RFC8200: Internet Protocol, Version 6 (IPv6) Specification (July 2017 (updated by RFC 9673)), https://www.rfc-editor.org/info/rfc8200/

**Exact predecessor dependencies:** os-internals-atlas, cryptographic-protocols-atlas. See immutable relation revisions in `data/relations.jsonl`.


# 08 — ICMP errors, checksums and diagnostic limits

**Scientific question.** How can control-plane diagnostic packets be distinguished from authenticated truth?

## Definitions, physical assumptions and scope

ICMPv4 messages have type, code, checksum and body. The checksum uses the same one’s-complement summation as IPv4 but includes the ICMP message. ICMPv6 has a pseudo-header and different message processing rules; the current runnable checksum model is only ICMPv4.

## Governing principle and derivation

For ICMPv4, checksum C=~fold16(message with checksum zero). This detects accidental corruption, not sender identity. Rate limiting and cross-layer validation determine whether diagnostics should change routing or PMTU state.

**Equation / invariant:** `C_ICMPv4 = ~(fold16(Σ_message_words)) & 0xffff`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

For a constructed eight-byte echo-request header/body, calculate checksum with the checksum field zeroed; verify that the final message folds to zero.

## Reconstructible offline procedure

Parse the correct message family, reject truncation and verify checksum. Retain original capture and do not automatically accept ICMP as a path-truth oracle.

## Independent test or negative control

Flipping a body byte without updating the checksum must trigger an ICMP checksum rejection; a correctly checksummed spoofed error is still untrusted.

## Known failures, uncertainty and acceptance gates

No complete ICMPv6 parser, ICMP message-code catalog, rate limiter or live path feedback.

## Source pointers (not authenticated publisher files)

- RFC791: Internet Protocol, IPv4 (September 1981), https://www.rfc-editor.org/info/rfc791/
- RFC1071: Computing the Internet Checksum (September 1988), https://www.rfc-editor.org/info/rfc1071/
- RFC4443: Internet Control Message Protocol (ICMPv6) (March 2006), https://www.rfc-editor.org/info/rfc4443/

**Exact predecessor dependencies:** os-internals-atlas, cryptographic-protocols-atlas. See immutable relation revisions in `data/relations.jsonl`.


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


# 10 — UDP framing, pseudo-header integrity and checksum exceptions

**Scientific question.** Can a lightweight transport be framed and integrity-checked correctly?

## Definitions, physical assumptions and scope

UDP fields are 16-bit source port, destination port, Length and Checksum. Length covers header and data. A checksum includes an IP-version-specific pseudo-header and UDP bytes, but is not a MAC. IPv4 optional omitted checksum is distinct from verified integrity; IPv6 normally prohibits zero.

## Governing principle and derivation

For IPv4 pseudoheader: src(4)+dst(4)+zero(1)+protocol(1)+length(2); for IPv6: src(16)+dst(16)+upper-layer length(4)+zero(3)+NextHeader(1). Internet checksum folds pseudoheader + UDP header + data.

**Equation / invariant:** `C_UDP = ~(fold16(IP_pseudoheader || UDP_header_zeroed || data)) & 0xffff`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

A three-byte UDP payload produces UDP Length 11; on an IPv4 network, changing one payload byte but retaining checksum must cause checksum rejection when checksum was present.

## Reconstructible offline procedure

Construct checksummed UDP datagrams with explicit source/destination IP addresses and ports, then independently verify pseudo-header arithmetic. Reject family mismatch, truncation and illegal IPv6 zero checksum.

## Independent test or negative control

An IPv4 UDP datagram with Checksum=0 passes length framing but must return integrity_not_assessed, not a verified checksum.

## Known failures, uncertainty and acceptance gates

No UDP-Lite, IP fragmentation, zero-checksum IPv6 exception protocols, socket API or transport delivery guarantees.

## Source pointers (not authenticated publisher files)

- RFC768: User Datagram Protocol (August 1980), https://www.rfc-editor.org/info/rfc768/
- RFC1071: Computing the Internet Checksum (September 1988), https://www.rfc-editor.org/info/rfc1071/
- RFC8200: Internet Protocol, Version 6 (IPv6) Specification (July 2017 (updated by RFC 9673)), https://www.rfc-editor.org/info/rfc8200/

**Exact predecessor dependencies:** os-internals-atlas, cryptographic-protocols-atlas. See immutable relation revisions in `data/relations.jsonl`.


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


# 13 — DNS label encoding and compression-pointer safety

**Scientific question.** How are DNS names encoded without infinite pointer traversal?

## Definitions, physical assumptions and scope

A domain name consists of length-prefixed octet labels followed by zero. Each regular label ≤63 bytes; fully expanded wire length ≤255 bytes. A compression pointer uses the high two bits 11 and a 14-bit offset, preserving the outer RR field cursor.

## Governing principle and derivation

An uncompressed name has encoded length 1+Σ_i(1+len(label)) bytes. A pointer occupies two bytes; a bounded decoder tracks visited offsets and rejected loops while retaining the next cursor from the original field.

**Equation / invariant:** `L_name = 1 + Σ_i(1+len(label_i)) ≤255`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

The name www.example.org is encoded 03 www 07 example 03 org 00 (hex length count 17). If www uses a pointer to example.org elsewhere, the caller offset must advance past the pointer, not through the expanded target.

## Reconstructible offline procedure

Decode wire labels as bytes first; enforce 63/255 limits, pointer hop cap, cycle detection and truncated-pointer rejection. Apply IDNA rules outside wire parser.

## Independent test or negative control

A 2-byte pointer pointing to itself is an explicit cycle failure; interpreting arbitrary DNS label bytes as UTF-8 is not part of the wire contract.

## Known failures, uncertainty and acceptance gates

No RR parser, EDNS, DNSSEC validation, recursive resolver, IDNA processing or live cache poisoning tests.

## Source pointers (not authenticated publisher files)

- RFC1035: Domain Names: Implementation and Specification (November 1987), https://www.rfc-editor.org/info/rfc1035/

**Exact predecessor dependencies:** os-internals-atlas, cryptographic-protocols-atlas. See immutable relation revisions in `data/relations.jsonl`.


# 14 — DNSSEC trust anchors and limits of name resolution

**Scientific question.** Why does a correct DNS wire parser not establish authentic name-to-address data?

## Definitions, physical assumptions and scope

DNSSEC defines authentication of DNS data via digital signatures and a chain of trust to configured trust anchors. A response with correct packet structure can be spoofed; DNSSEC success depends on key algorithms, rollover, time validation and authenticated trust anchor management.

## Governing principle and derivation

Logical chain: verified RRset signature AND verified DNSKEY chain AND valid trust-anchor path AND acceptable validity interval. Absence of one condition does not prove another. An offline parse is a syntax check only.

**Equation / invariant:** `DNSSEC_accepted ⇒ signature_valid ∧ trusted_chain ∧ time_valid`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

A constructed DNS A record returning 192.0.2.3 with no RRSIG is syntactically possible but cannot be promoted to DNSSEC-authenticated data.

## Reconstructible offline procedure

Preserve DNS response bytes, key IDs, algorithms, anchor edition, clock evidence and negative trust outcomes. Use an independently reviewed DNSSEC implementation for actual validation.

## Independent test or negative control

A syntactically correct answer with forged data and no trusted chain must remain unauthenticated rather than being accepted by the parser.

## Known failures, uncertainty and acceptance gates

No DNSSEC crypto implementation, resolver behavior, authenticated original publisher key material or trust-anchor lifecycle testing.

## Source pointers (not authenticated publisher files)

- RFC4033: DNS Security Introduction and Requirements (March 2005), https://www.rfc-editor.org/info/rfc4033/
- RFC1035: Domain Names: Implementation and Specification (November 1987), https://www.rfc-editor.org/info/rfc1035/

**Exact predecessor dependencies:** cryptographic-protocols-atlas, os-internals-atlas. See immutable relation revisions in `data/relations.jsonl`.


# 15 — QUIC variable integers versus secure connection state

**Scientific question.** What does correctness of QUIC integer encoding actually establish?

## Definitions, physical assumptions and scope

QUIC v1 encodes integers in 1,2,4,8 bytes; the high two bits indicate width, the remaining bits carry 6,14,30,62 information bits. Correct encoding is necessary but not sufficient for QUIC transport, loss recovery or TLS security.

## Governing principle and derivation

The maximum representable value at width w is 2^(8w−2)−1; the encoder chooses the shortest width capable of storing the unsigned integer. Decoders may admit nonminimal widths but must reject truncated frames.

**Equation / invariant:** `max_varint(w) = 2^(8w−2)−1 for w∈{1,2,4,8}`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

Values 63 and 64 lie at the 1-byte/2-byte boundary; their shortest encodings are hex 3f and 4040. The overall maximum is 2^62−1.

## Reconstructible offline procedure

Test all thresholds using published-format fixed vectors, a distinct integer constructor and truncated-byte controls; keep packet parsing and transport handshakes outside scope.

## Independent test or negative control

A four-byte length tag with only two available bytes must fail, even if the partial lower bits look like a small integer.

## Known failures, uncertainty and acceptance gates

No QUIC packet number spaces, flow-control, crypto, loss recovery or HTTP/3 interoperability.

## Source pointers (not authenticated publisher files)

- RFC9000: QUIC: A UDP-Based Multiplexed and Secure Transport (May 2021), https://www.rfc-editor.org/info/rfc9000/
- RFC9001: Using TLS to Secure QUIC (May 2021), https://www.rfc-editor.org/info/rfc9001/

**Exact predecessor dependencies:** distributed-systems-atlas, cryptographic-protocols-atlas. See immutable relation revisions in `data/relations.jsonl`.


# 16 — TLS 1.3 version continuity and trusted channel boundaries

**Scientific question.** What evidence is needed to call an application channel authenticated and confidential?

## Definitions, physical assumptions and scope

TLS 1.3 has a transcript-bound authenticated handshake and AEAD-protected records. The authoritative July 2026 RFC 9846 obsoletes RFC 8446 while retaining the same protocol version with clarified requirements. A checksum or plaintext MAC framing example is not TLS.

## Governing principle and derivation

An abstract secure-channel acceptance predicate requires verified peer identity, valid transcript, fresh key shares, negotiated parameters and AEAD authentication. This logical conjunction is a specification model, not a runnable cryptographic implementation.

**Equation / invariant:** `channel_trusted ⇒ peer_authenticated ∧ handshake_valid ∧ AEAD_valid ∧ key_usage_within_limits`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

If a frame passes a CRC and IP checksum but has no peer authentication, confidentiality and authenticity remain unverified regardless of message delivery success.

## Reconstructible offline procedure

Preserve the exact TLS version, certificate/PSK policy, trust roots, time evidence, selected suites and handshake traces; use a conformant, maintained TLS stack for actual secure communication.

## Independent test or negative control

A reused ephemeral KeyShare or invalid certificate must not be masked by an otherwise successful transport connection.

## Known failures, uncertainty and acceptance gates

No TLS code or independent cryptographic certificate validation in this node; source publisher original bytes not locally authenticated.

## Source pointers (not authenticated publisher files)

- RFC9846: The Transport Layer Security (TLS) Protocol Version 1.3 (July 2026 (obsoletes RFC 8446)), https://www.rfc-editor.org/info/rfc9846/
- RFC9001: Using TLS to Secure QUIC (May 2021), https://www.rfc-editor.org/info/rfc9001/

**Exact predecessor dependencies:** cryptographic-protocols-atlas, distributed-systems-atlas. See immutable relation revisions in `data/relations.jsonl`.


# 17 — Routing control planes, path-vector safety and policy

**Scientific question.** How can forwarding math be separated from route-advertisement trust?

## Definitions, physical assumptions and scope

BGP advertises reachability with AS-path and attributes that are interpreted under local policy. Local prefix matching does not authenticate the route origin or guarantee convergence, loop-freedom or traffic correctness. Operational routing safety requires controls beyond a longest-prefix table.

## Governing principle and derivation

A simplistic hop-distance metric c(path)=Σ_i c_i demonstrates cumulative path costs, but BGP uses policy rather than minimizing that quantity. No convergence or safety theorem follows from choosing a shortest path.

**Equation / invariant:** `path_cost = Σ edge_cost (illustrative, NOT BGP selection rule)`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

Route 203.0.113.0/24 from an authorized AS and forged 203.0.113.128/25 from an attacker: a forwarding table may select the /25 even though it violates trust assumptions.

## Reconstructible offline procedure

Label route source and external authorization, tie each next-hop to interface reachability, and capture policy decisions. Preserve unknown trust outcomes and isolate routing from DNS.

## Independent test or negative control

A bogus more-specific route being selected by LPM is not a correctness success for network security or routing provenance.

## Known failures, uncertainty and acceptance gates

No BGP implementation, RPKI origin validation, traffic engineering or convergence measurements.

## Source pointers (not authenticated publisher files)

- RFC4271: A Border Gateway Protocol 4 (BGP-4) (January 2006), https://www.rfc-editor.org/info/rfc4271/
- RFC4632: Classless Inter-domain Routing (CIDR) (August 2006), https://www.rfc-editor.org/info/rfc4632/

**Exact predecessor dependencies:** distributed-systems-atlas, cryptographic-protocols-atlas. See immutable relation revisions in `data/relations.jsonl`.


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


# 19 — Fault injection, adversarial framing and transport evidence

**Scientific question.** What is required to test a stack that faces loss, corruption, reordering and duplication?

## Definitions, physical assumptions and scope

A network stack failure model must distinguish corruption, duplication, reordering, omission, delay, partition, power interruption and maliciously crafted syntax. Synthetic tests are bounded and cannot reproduce all concurrency, NIC and OS behavior.

## Governing principle and derivation

For n injected cases, finite pass fraction k/n is a test statistic and not a production reliability estimate without a representative sampling model and confidence intervals. Different oracles must not simply call the same parser.

**Equation / invariant:** `p_observed = k/n (constructed finite tests; not measured field reliability)`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

Run 100 seeded frames, then independently flip a checksum-protected byte, truncate framing, reorder packets and inject duplicate identifiers. Require each invalid category to fail for the intended reason.

## Reconstructible offline procedure

Preserve seeds, expected negative failure type, alternate oracle method, test output and exact source-hash receipts. Don’t equate a successful parser call with transport-layer confidentiality.

## Independent test or negative control

A malformed fragment that fails checksum before fragmentation rejection is NOT proof that fragmentation handling works; create a valid-checksum unsupported fragment negative control.

## Known failures, uncertainty and acceptance gates

No field fault injection, operating-system packet fuzzing, production security audits or live transport simulation.

## Source pointers (not authenticated publisher files)

- RFC791: Internet Protocol, IPv4 (September 1981), https://www.rfc-editor.org/info/rfc791/
- RFC8200: Internet Protocol, Version 6 (IPv6) Specification (July 2017 (updated by RFC 9673)), https://www.rfc-editor.org/info/rfc8200/
- RFC9293: Transmission Control Protocol (TCP) (August 2022 (obsoletes RFC 793)), https://www.rfc-editor.org/info/rfc9293/

**Exact predecessor dependencies:** software-design-patterns-atlas, distributed-systems-atlas. See immutable relation revisions in `data/relations.jsonl`.


# 20 — Offline reconstruction and survival dependency chain

**Scientific question.** What files, circuits, software and evidence are needed to re-create communication progressively?

## Definitions, physical assumptions and scope

Start with verified power and timing sources, physical wiring/impedance, transceiver and NIC, firmware and kernel interface, Ethernet/IPv4/IPv6 framing, routing, transport, naming and authenticated services. Each stage adds new verifiable inputs and explicit unresolved dependencies.

## Governing principle and derivation

The dependency relation should be acyclic for a planned bootstrap: power→clock→PHY→link→IP→transport→application. Actual hardware may have bootstrapping cycles broken by read-only firmware, pre-shared configurations or static addressing.

**Equation / invariant:** `bootstrap_prerequisites(layer_i) ⊆ verified_layers_0..i−1 (planning constraint)`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

Without DNS and DHCP, two machines can still use static IPv4 addresses and a direct Ethernet link once NIC drivers and cabling are verified. This is a proposed procedure, not a tested physical reconstruction.

## Reconstructible offline procedure

Preserve a printed addressing plan, tests for each preceding stage, offline code, diagrams, source caveats, capture methods and hashes. Run software oracles and then independent physical checks before claiming a functioning network.

## Independent test or negative control

A host might pass all local Python tests while no network driver or physical transceiver works; mark operational networking as HOLD.

## Known failures, uncertainty and acceptance gates

No actual hardware wire-up, physical layer measurements, target ROG deployment or outage test.

## Source pointers (not authenticated publisher files)

- RFC894: Standard for the Transmission of IP Datagrams over Ethernet Networks (April 1984), https://www.rfc-editor.org/info/rfc894/
- RFC791: Internet Protocol, IPv4 (September 1981), https://www.rfc-editor.org/info/rfc791/
- RFC9293: Transmission Control Protocol (TCP) (August 2022 (obsoletes RFC 793)), https://www.rfc-editor.org/info/rfc9293/

**Exact predecessor dependencies:** os-internals-atlas, computer-architecture-digital-hardware-atlas, manufacturing-atlas. See immutable relation revisions in `data/relations.jsonl`.


# 21 — Security boundaries, provenance and trust anchors

**Scientific question.** Why must protocol conformance be treated separately from cryptographic security?

## Definitions, physical assumptions and scope

Correct frame length, checksum and syntax mean only specified structural requirements held. None authenticate an IP/ARP sender, DNS server, route advertisement or upper-layer transaction. An offline scientific reader must preserve these negative qualifiers with every retrieved method.

## Governing principle and derivation

The condition data_accepted requires parser_valid AND required authenticated-origin checks AND replay policy AND state authorization. Without a required check, the application must abstain or label unauthenticated.

**Equation / invariant:** `auth_accepted ⇒ syntax_valid ∧ origin_trusted ∧ replay_accepted ∧ policy_allowed`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

A forged UDP datagram may have a correct UDP checksum; in this case the checksum model should return true but the application authenticity verdict is unknown/false.

## Reconstructible offline procedure

Carry exact record revisions and upstream source/rights labels through evidence retrieval; compare independent cryptographic primitives with published vectors before real integration.

## Independent test or negative control

Calling a validated IP checksum an authenticated packet is the negative control. Reject this evidence promotion as a category error.

## Known failures, uncertainty and acceptance gates

No production authentication, TLS interoperability, remote trust or independent security certification.

## Source pointers (not authenticated publisher files)

- RFC9846: The Transport Layer Security (TLS) Protocol Version 1.3 (July 2026 (obsoletes RFC 8446)), https://www.rfc-editor.org/info/rfc9846/
- RFC4033: DNS Security Introduction and Requirements (March 2005), https://www.rfc-editor.org/info/rfc4033/
- RFC9000: QUIC: A UDP-Based Multiplexed and Secure Transport (May 2021), https://www.rfc-editor.org/info/rfc9000/

**Exact predecessor dependencies:** cryptographic-protocols-atlas, software-design-patterns-atlas. See immutable relation revisions in `data/relations.jsonl`.


# 22 — Independent acceptance gates, restoration and preservation

**Scientific question.** How can new network science be added without rewriting the original ATLAS?

## Definitions, physical assumptions and scope

Each node uses the unchanged atlas.common/1 schema with concepts, claims, equations, methods, datasets, sources, reviews and exact relations. New records are sealed with immutable canonical SHA-256 revisions. Historic records/graphs and the original 30-domain queue are preserved.

## Governing principle and derivation

A canonical incremental patch from predecessor B to target T contains only changed/new members. For each file f, SHA256(content_source[f]) must equal SHA256(content_restored[f]); both complete source and fresh tests must be replayed with byte-identical receipts.

**Equation / invariant:** `∀f∈T SHA256(source_f)=SHA256(restored_f); sha256(ZIP_source)=sha256(ZIP_restored)`. Do not apply outside the stated assumptions.

## Worked construction (not experimental data)

If 10,629 prior source files exist, all must remain present after addition. Only explicitly authorized integration metadata may change, and no prior scientific data file is silently revised.

## Reconstructible offline procedure

Validate registry, manifest and exact relations; run domain oracles; run all historic regression suites with frozen predecessor assertions; build direct patch, reconstruct independently and compare the two complete receipts before advancing the Library checkpoint.

## Independent test or negative control

Any failed historical test, unauthorized old file hash drift, mismatched deterministic ZIP, missing Library readback, or unsupported claim must keep the prior checkpoint authoritative.

## Known failures, uncertainty and acceptance gates

Software-content release is not wire interoperability, accredited peer review, physical-power testing or authenticated original publisher preservation.

## Source pointers (not authenticated publisher files)

- RFC9293: Transmission Control Protocol (TCP) (August 2022 (obsoletes RFC 793)), https://www.rfc-editor.org/info/rfc9293/
- RFC9846: The Transport Layer Security (TLS) Protocol Version 1.3 (July 2026 (obsoletes RFC 8446)), https://www.rfc-editor.org/info/rfc9846/

**Exact predecessor dependencies:** software-design-patterns-atlas, distributed-systems-atlas, os-internals-atlas. See immutable relation revisions in `data/relations.jsonl`.

