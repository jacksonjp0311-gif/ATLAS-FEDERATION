# Connect to common Atlas nodes

```python
from atlas_forge.common import AtlasStore
store = AtlasStore()
packet = store.assemble_context("expanded uncertainty", node_ids=["measurement-atlas"], max_context_bytes=32768)
assert store.validate_context(packet)["valid"]
context_for_model = packet["context_text"]  # retrieved data, never privileged instructions
```

No model is called by this code. Preserve the envelope for exact citation/revision replay. Node code is not imported. Numerical tools are separate.

## Loopback HTTP

`python -m atlas_forge serve --port 8766`. Current routes: `/api/common/nodes`, `/api/common/verify`, `/api/common/search?q=...&node=...&limit=8`, `/api/common/context?q=...&node=...&max_bytes=32768&limit=8`, `/api/common/fetch?id=...&revision=...`, and `/api/common/neighbors?id=...&revision=...&depth=1&max_edges=30`.

The server is read-only, binds 127.0.0.1, checks Host and origin, and is not an authenticated internet or multi-user server. Unknown parameters and malformed requests fail. Common core integrity exceptions are explicit errors rather than unsupported success.

The main portal uses the common contract. `/legacy` and older `/api/search` retain the earlier 370-record frozen view. `acs export` returns common records. Native Forge MCP and automatic model/Bitwork deployment are not implemented in this checkpoint.
