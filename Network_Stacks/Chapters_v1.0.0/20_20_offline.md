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

