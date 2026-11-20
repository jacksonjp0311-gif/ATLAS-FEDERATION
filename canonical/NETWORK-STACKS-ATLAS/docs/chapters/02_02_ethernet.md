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

