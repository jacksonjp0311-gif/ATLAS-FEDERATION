# Integration contract v0.2

Implemented: standalone Atlas generation/validation/query, three pinned reference nodes,
Python federation, CLI discovery/search/export, a loopback-only read-only HTTP API,
and a browser node portal. See [Node Integration](NODE_INTEGRATION.md) for exact examples.
The historical v0.1 contract is retained in [history](history/INTEGRATION_CONTRACT_v0.1.md).

Not implemented: a Forge-native MCP service, OpenAPI document, automatic source refresh,
remote multi-user service, semantic answer synthesis, or live PEGASUS/SYMBIOTE connections.

Each result retains node/version identity, an original record, source locators and rights,
upstream evidence labels, and a separate Forge import status. Matching records yield
`partial` context, not a certified answer. A miss remains `unresolved`. Starter data requires
explicit opt-in. Shared citations are not independent corroboration. Snapshot hashes show
byte consistency, not scientific truth or authenticity.
