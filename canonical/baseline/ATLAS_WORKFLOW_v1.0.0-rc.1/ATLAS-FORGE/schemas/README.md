# Schema contracts

`federation_registry.v1.json` describes the node directory and membership edges.
`federation_node.v1.json` describes the pinned identity, adapter and reference-file hashes.
Existing packet and standalone Atlas schemas remain unchanged.

The runtime enforces integrity, safe paths, adapter compatibility, identity uniqueness,
record counts and source-reference constraints using the standard library. These JSON
Schemas describe interchange structure; they are not a scientific review mechanism.
Unique node IDs, matching hashes, valid graph targets and source joins also require runtime checks.

To preserve verified raw bytes on Windows as well as Linux, the release uses `.gitattributes`
with text conversion disabled. An intentional edit requires new hashes and review, not
silent newline normalization.
