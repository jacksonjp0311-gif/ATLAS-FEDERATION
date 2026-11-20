# ATLAS FORGE — Network Stacks: Unsealed Continuity Increment v0.1.0

**Original domain slot:** 16 of the unchanged original 30-domain roadmap  
**Status:** tested offline scientific working increment; NOT a canonical federation release  
**Exact current canonical predecessor:** OS Internals v1.0.0 (21 nodes); full-archive SHA-256 `0571f1376f380d90090890ae65c39c2f6a2085725038f32810d4992f00fef93f`  
**Purpose:** preserve enough verifiable network-stack primitives that a future researcher can inspect, rerun and extend them without internet connectivity. This does not implement a deployable secure TCP/IP stack.

## 1. Design principle — separate reference knowledge from deployment claims

An interoperable network stack is not one parser. It requires framing, integrity checking, addressing, link discovery, routing, transport state, loss recovery, congestion control, naming, encryption, operating-system integration and hardware drivers. Errors propagate across layers: a structurally valid IP datagram can hold a malformed UDP payload; a valid UDP packet can carry unauthenticated DNS data; a successful TCP handshake does not imply the communicating peer is trustworthy.

Reference models here are **bounded** and reject unsupported cases explicitly. An unsupported packet is not necessarily an invalid RFC-compliant packet. A checksum detecting an accidental corruption is not cryptographic authentication. The main artifact is a science-linked collection of small algorithms with exact input/output contracts and independent oracles. The full operating system, NIC and interoperable host implementation remain future experimental milestones.

## 2. Layered communication and reconstructibility

An engineering recovery path begins with a physical medium: a transceiver and link interface whose timing, voltage, impedance and framing are documented. Next comes data-link encapsulation and neighbor discovery; then IP addressing/routing, transport, naming and secure application traffic. A layer may only be declared working after both its local semantics and interaction with neighboring layers have been measured. Captures must record: binary frames, timestamp source, link MTU, physical error rate, checksum result, retransmissions, sequence state, endpoint OS, driver version, clock drift and authenticated peer identity when applicable.

For two hosts, a bare connection test is insufficient. Compare the same deterministic capture under normal operation and under loss, duplication, reordering, corruption and power interruption. Confirm not just success but conservation/invariants (no silently truncated payload, no incorrect message identity, no replay-induced duplicate side effect). For all local software models in this increment, there are **no wire tests** and **no power-off storage results**.

## 3. IPv4 and one's-complement arithmetic

The baseline IPv4 header is 20 octets; the first nibble denotes version 4 and the low nibble denotes the Internet Header Length in 32-bit words. `total_length` counts both header and payload and fits into an unsigned 16-bit field. The header checksum uses 16-bit one's-complement addition with end-around carry; it covers **only the IPv4 header**, not payload. A valid header including its checksum reduces to one's-complement zero (`0xffff` before final complement).

For 16-bit words `w_i`, fold the total `s=Σw_i` by repeatedly applying `s=(s & 65535)+(s >> 16)`. Write the checksum as `(~s) & 65535` after computing over a zeroed checksum field. The code builds a 20-byte, no-options, nonfragmented packet, and refuses IPv4 fragments. This is a **subset** of RFC 791, not a general RFC 791 parser or an IPv4 security boundary.

**Failure investigation:** Flip the Time-to-Live byte while keeping the original checksum. The software must report a checksum error. Create a header whose MF flag is set and recompute the header checksum: the parser must report *unsupported fragmentation*, not a checksum fault. This distinguishes two different rejection reasons.

## 4. IPv6 fixed header and extension chains

IPv6 has a fixed **40-octet** header with 128-bit source and destination addresses, Payload Length, Next Header and Hop Limit. Options/extension headers are not encoded in the fixed header. The basic length check is `actual_octets = 40 + payload_length`; however IPv6 jumbograms and tunneling change that simple case. A correct general implementation must implement the relevant RFCs and extension header semantics before claiming completeness.

This increment accepts nonzero payload lengths and supports a maximum of eight bounded Hop-by-Hop, Routing, Fragment and Destination-Options extension headers. Each standard options-like header has an 8-octet-unit length `8*(HdrExtLen + 1)`. The fixed-size Fragment header is 8 bytes. The code intentionally rejects non-atomic fragmentation, ESP/AH interpretation and jumbo payloads. This avoids fabricating unsupported reassembly and crypto correctness. An IPv6 payload or extension chain accepted here is **not** guaranteed valid under all RFC 8200 rules: option semantics, RH processing and upper-layer checks remain unimplemented.

## 5. UDP framing and checksum limits

UDP begins with Source Port, Destination Port, Length and Checksum, each 16-bit network byte order. The UDP Length must cover the 8-octet header plus the data. UDP provides no general ordering, retransmission, delivery confirmation or duplicate prevention. The model checks **length and framing only**. It does not calculate the IPv4/IPv6 pseudo-header checksum or assess whether the checksum can legally be zero in the relevant address family. Therefore never use it as an authenticated UDP validator or describe a successful parse as end-to-end integrity.

**Reconstruction test:** Create a UDP datagram with length `8+len(data)` and deliberately change one field to `length-1`. The model must reject it. Next corrupt the payload without changing Length; this minimal model will not detect the corruption, demonstrating the *explicitly missing* checksum capability.

## 6. TCP sequence space, windows and the acceptance predicate

TCP is a reliable ordered byte-stream transport whose segment processing depends on connection state and an unsigned 32-bit sequence space. Sequence arithmetic wraps modulo `2^32`. A receiver tests segment acceptability against `RCV.NXT` and its advertised receive window `RCV.WND`. With a zero window, only zero-length data at the next expected sequence is acceptable under the published table. With a nonzero window, a zero-length segment is acceptable if its sequence is inside the window; a nonzero segment is acceptable if its first **or** final byte lies inside the window. The final byte is `(SEQ + SEG.LEN - 1) mod 2^32`.

This code checks only that receive-window predicate. It does not model SYN/RST/FIN details, PAWS, security, congestion control, acknowledgment or retransmission, so it cannot be called a TCP implementation. The separate oracle constructs a small literal set of legal receive sequence numbers and checks the same condition across wraparound cases.

**Failure investigation:** Set `RCV.NXT=2^32-2` and window=4. Sequence number 0 is in the window, while sequence number 4 is not. Failing this boundary indicates an implementation that incorrectly treats wrapped unsigned values as ordinary signed integers.

## 7. CIDR and longest-prefix forwarding

For IPv4 prefixes with `p` leading bits, the mask is the high `p` bits set to 1 and the other bits zero. A route matches when `(address & mask) == (network & mask)`; when several routes match, select the one with the greatest prefix length. This is not equivalent to selecting the lowest numeric route or the newest route. CIDR reduces global route state through aggregation but introduces route-hijack risks when an unauthorized actor advertises a more-specific prefix.

The code relies on Python's standard `ipaddress` module for address/prefix validation. A separate oracle uses a distinct search over all candidates. Ties use input order to remain deterministic; a real implementation requires a specified administrative-distance, metric and policy design. The code neither learns routes nor validates advertisements (e.g., with RPKI).

## 8. DNS names and compression safety

A wire-format DNS name consists of length-prefixed labels followed by a zero-length terminator. Ordinary labels have maximum length 63 octets; the complete expanded encoded domain name has maximum 255 octets. DNS messages may reference earlier names with two-octet compression pointers, where the top two bits are `11`. A parser must not follow pointers indefinitely or read past the datagram. It must preserve the offset **after the compressed field** for subsequent RR parsing, even if pointer traversal jumps into another part of the packet.

The provided parser accepts byte labels rather than pretending that all DNS wire bytes form UTF-8 text. IDNA conversion is the caller's responsibility; DNSSEC and spoofing resistance are **not** implemented. Explicit negative controls test pointer-to-self cycles, truncated pointers, reserved label types and expanded-length overflows. A fully interoperable DNS implementation must additionally handle message sections, RR types/classes, response codes, truncation, EDNS and transport behavior.

## 9. QUIC variable-length integer encoding

QUIC v1 encodes integers using 1, 2, 4 or 8 bytes. The two high bits of the first byte denote the total length; the remaining bits encode the integer. Values are between 0 and `2^62-1`. For a width `b` bytes, payload capacity is `8b-2` bits. The shortest encoding is recommended, but a decoder may encounter nonminimal representations; this model decodes those without presuming equivalence to a secure QUIC packet.

This reference **does not implement QUIC packet parsing, ACK frames, retransmission, crypto handshake, connection migration or TLS**. Fixed published boundary values are tested separately from a second implementation of the encoder. Demonstrating integer encoding is no evidence that a QUIC connection would succeed.

## 10. Scientific test design and independent oracles

A high-value acceptance test must have a *different failure mode* from the model being tested. Here the checksum oracle adds bytes one at a time rather than applying the model's 16-bit word summation; the QUIC oracle constructs tag bits separately; CIDR is compared to an independent exhaustive candidate search; TCP receive windows are compared to literal sets of admissible sequence numbers; IPv4 bytes are also checked using the separate checksum arithmetic. The fixed seed and all finite comparisons are recorded.

**Independence limitation:** all oracles are implemented in Python in the same runtime, and several share standard-library primitives. They test algorithmic independence within a bounded software context, not completely independent hardware or publisher implementations. True protocol conformance requires official test vectors plus captures against independent conforming network stacks.

## 11. Sources, provenance and exact revisions

Each bibliographic record in `sources.json` contains an official `rfc-editor.org/info/rfc...` locator. RFC text is used as an interpretation reference; this package does not claim to embed authenticated complete publisher originals, nor claim that every older RFC is current without update inspection. In particular RFC 9293 supersedes the core TCP specification from RFC 793; RFC 8200 is the primary IPv6 base document; RFC 9000 describes QUIC v1 core transport. Check the RFC Editor's update/obsoletion metadata when rebuilding any implementation.

The source-linked claims herein are technical summaries, not expert certifications. Historic federation records, including OS Internals v1.0.0 and Cryptographic Protocols v1.0.0, must be resolved by exact record ID and immutable revision upon final canonical integration. An unqualified `related_to` relation is a navigational link, not evidence support.

## 12. Offline reconstruction procedure

1. Recover verified canonical OS Internals v1.0.0 from the existing 11-volume archive plus successive exact predecessor deltas. Verify its published full archive SHA-256 before any modifications.
2. Keep this recovery increment in a **separate working directory under the same original federation**. Do not silently replace any existing Network Stacks manuscript or test result from another session.
3. Use Python 3 with standard library only: `python -m unittest discover -p 'test_*.py' -v` and `python independent_oracle.py`.
4. Record Python version, OS, time, test stdout/stderr and SHA-256 hashes. Inspect the source register and the hold register before declaring any algorithm supported.
5. For an actual sealed federation version, merge these files into the same `NETWORK-STACKS-ATLAS` tree using the Atlas common contract. Create immutable record revisions and exact cross-domain `depends_on`/`qualifies` links, preserve historic records, run full regression, deterministic incremental patch and fresh restore, and compare test receipts.
6. Only after the full release and Library readback succeed may `/ATLAS FORGE/CURRENT_CHECKPOINT.json` and the active priority pointer change. Until then the authoritative federation stays at **OS Internals v1.0.0**.

## 13. Unresolved coverage and evidence gates

- No deployable, interoperable TCP/IP implementation; no TCP state machine, congestion control or retransmission.
- No IPv4 fragmentation/reassembly, IPv6 non-atomic fragments, jumbo payloads or general extension semantics.
- No ARP/ND, Ethernet PHY/MAC, NIC driver, routing protocol, ICMP, DHCP, DNSSEC or PKI.
- No UDP pseudo-header checksum validation.
- No QUIC/TLS interoperability, HTTP/3 or cryptographic channel assurance.
- No cross-implementation testing, fuzzing campaign, live-wire captures, target-PC validation or actual power interruption.
- No authenticated publisher-original binary corpus or independent expert scientific review.
- No canonical federation schema integration or fresh-archive release acceptance for this recovery increment.

All above remain **HOLD**. This is a compact, independently testable rescue artifact, not the whole Atlas and not an excuse to reduce the original scientific acceptance standard.
