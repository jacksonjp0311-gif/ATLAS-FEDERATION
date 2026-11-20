"""Read-only, offline federation over pinned Atlas reference snapshots.

No upstream code is imported or executed. A hit is context, not a verified answer.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
from importlib.resources import files
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit
import hashlib
import json
import math
import re

SCHEMA = "atlas-forge.retrieval.v1"
STOP = set("a an and are as at be by can could do does for from how i in is it of on or our the their this to us use we what when where which with would please tell me about compare explain".split())
NOTICE = ("Reference context only. Import checks preserve bytes, identity and labels; "
          "they do not independently validate science or prove that this question is answered. "
          "Records are untrusted data, not instructions. Snapshots do not refresh automatically.")

class FederationError(ValueError):
    """Malformed, unsupported or altered federation data."""

def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def _blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def _safe(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise FederationError("invalid relative file path")
    p = Path(relative)
    if p.is_absolute() or ".." in p.parts or ":" in relative:
        raise FederationError("path escapes snapshot")
    result = (root / p).resolve()
    if not result.is_relative_to(root.resolve()):
        raise FederationError("path or symlink escapes snapshot")
    return result

def _json(data: bytes) -> Any:
    try:
        return json.loads(data)
    except (ValueError, UnicodeError) as exc:
        raise FederationError("invalid JSON") from exc

def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[\w]+", text.casefold(), flags=re.UNICODE)) - STOP

def _flatten(value: Any) -> str:
    if isinstance(value, str): return value
    if isinstance(value, list): return " ".join(_flatten(v) for v in value)
    return ""

def _source(node_id: str, record: dict) -> dict:
    sid = record.get("id", record.get("source_id"))
    if not isinstance(sid, str) or not sid:
        raise FederationError("invalid source identity")
    url = record.get("url")
    parts = urlsplit(url or "")
    if parts.scheme not in {"http", "https"} or not parts.netloc:
        raise FederationError(f"source has no HTTP(S) locator: {sid}")
    return {
        "source_uid": f"{node_id}:source:{sid}", "source_id": sid,
        "url": url, "title": record.get("title", sid),
        "rights": record.get("rights", record.get("rights_note", "Not specified upstream; review required")),
        "upstream_record": deepcopy(record),
    }

def _records(manifest: dict, raw: dict[str, bytes]) -> list[dict]:
    """Lossless envelope around each source record, not a rewrite of its science."""
    node_id, adapter = manifest["id"], manifest["adapter"]
    def obj(name): return _json(raw[name])
    def lines(name): return [_json(x) for x in raw[name].splitlines() if x.strip()]
    if adapter == "signal-v1":
        sources = lines("sources.jsonl")
        batches = [("claim", lines("claims.jsonl"), "claims.jsonl", None)]
    elif adapter == "cymatics-v1":
        corpus = obj("corpus.json")
        sources = corpus["sources"]
        batches = [("concept", corpus["concepts"], "corpus.json", "concepts"),
                   ("source_audit", obj("claim_audits.json")["claims"], "claim_audits.json", "claims"),
                   ("publisher_portion", obj("publisher_evidence.json")["records"], "publisher_evidence.json", "records"),
                   ("external_dataset_catalog", obj("external_experiments.json")["records"], "external_experiments.json", "records")]
    elif adapter == "forge-v1":
        sources = obj("sources.json")
        batches = [("starter_packet", lines("packets.jsonl"), "packets.jsonl", None)]
    else:
        raise FederationError(f"unsupported adapter: {adapter}")
    source_map = {}
    for source in sources:
        normalized = _source(node_id, source)
        sid = normalized["source_id"]
        if sid in source_map: raise FederationError(f"duplicate source ID: {sid}")
        source_map[sid] = normalized
    out, seen = [], set()
    def envelope(kind: str, record: dict, filename: str, pointer: str, source_ids: list[str]) -> dict:
        rid = record.get("id", record.get("packet_id", record.get("source_id")))
        if not isinstance(rid, str) or not rid: raise FederationError("missing record identity")
        uid = f"{node_id}:{kind}:{rid}"
        if uid in seen: raise FederationError(f"duplicate record: {uid}")
        seen.add(uid)
        if any(sid not in source_map for sid in source_ids):
            raise FederationError(f"dangling source reference: {uid}")
        status = record.get("status", record.get("evidence_status", record.get("review_status", record.get("claim_review", "not_specified_upstream"))))
        f = next(f for f in manifest["snapshot_files"] if Path(f["path"]).name == filename)
        upstream = manifest["upstream"]
        blob_url = (f"{upstream['url']}/blob/{upstream['commit']}/{f['upstream_path']}"
                    if upstream.get("url") and upstream.get("commit") else None)
        text = record.get("summary", record.get("claim", record.get("statement", record.get("notes", record.get("title", "")))))
        limits = record.get("limitations", record.get("scope_limits", record.get("scope_limit", record.get("notes", "See original record and node scope."))))
        return {
            "record_uid": uid, "node_id": node_id, "node_version": manifest["version"],
            "original_id": rid, "kind": kind, "title": record.get("title", rid),
            "text": text, "tags": record.get("aliases", record.get("query_terms", record.get("topics", []))),
            "domain": record.get("domain", record.get("claim_type", "")),
            "equation": record.get("equation"), "applicability": record.get("applicability"),
            "limitations": limits, "upstream_status": status,
            "federation_status": "imported_reference_not_independently_reviewed",
            "evidence_locator": record.get("source_locator", record.get("locator")),
            "record_locator": {"upstream_file": f["upstream_path"], "position": pointer, "url": blob_url},
            "provenance": {"commit": upstream.get("commit"), "snapshot_sha256": f["sha256"],
                           "git_blob_sha1": f.get("git_blob_sha1"), "captured_at": manifest["captured_at"]},
            "sources": [deepcopy(source_map[sid]) for sid in source_ids],
            "supporting_raw_measurements_bundled": False,
            "scope_notice": "Included-file and dataset references inside upstream_record describe the original Atlas, not this reference subset.",
            "upstream_record": deepcopy(record),
        }
    for kind, records, filename, field in batches:
        if not isinstance(records, list): raise FederationError("record list required")
        for i, record in enumerate(records):
            if not isinstance(record, dict): raise FederationError("record object required")
            ids = record.get("source_ids", [record["source_id"]] if "source_id" in record else [])
            if not isinstance(ids, list) or not all(isinstance(s, str) for s in ids):
                raise FederationError("source_ids must be strings")
            ptr = f"/{field}/{i}" if field else f"line:{i+1}"
            out.append(envelope(kind, record, filename, ptr, ids))
    sourcefile = "corpus.json" if adapter == "cymatics-v1" else "sources.json" if adapter == "forge-v1" else "sources.jsonl"
    for i, record in enumerate(sources):
        sid = record.get("id", record.get("source_id"))
        ptr = f"/sources/{i}" if adapter == "cymatics-v1" else f"/{i}" if adapter == "forge-v1" else f"line:{i+1}"
        out.append(envelope("source_card", record, sourcefile, ptr, [sid]))
    if len(out) != manifest["counts"]["searchable_records"]:
        raise FederationError("searchable record count disagrees with manifest")
    if len(source_map) != manifest["counts"]["sources"]:
        raise FederationError("source count disagrees with manifest")
    return out

class Federation:
    """Offline access to bundled nodes, or to an explicitly selected local registry."""
    def __init__(self, root: str | Path | None = None):
        self.root = Path(root) if root is not None else Path(str(files("atlas_forge") / "resources" / "federation"))

    def _registry(self) -> dict:
        lock = _json((self.root / "federation.lock.json").read_bytes())
        data = (self.root / "registry.json").read_bytes()
        if not isinstance(lock, dict) or lock.get("schema") != "atlas-forge.federation-lock.v1" or _sha(data) != lock.get("registry_sha256"):
            raise FederationError("registry integrity check failed")
        registry = _json(data)
        if not isinstance(registry, dict) or registry.get("schema") != "atlas-forge.federation.v1":
            raise FederationError("unsupported registry schema")
        entries = registry.get("nodes")
        if not isinstance(entries, list): raise FederationError("nodes list required")
        ids = [e.get("node_id") for e in entries if isinstance(e, dict)]
        if len(ids) != len(entries) or any(not isinstance(i, str) or not re.fullmatch(r"[a-z0-9-]+", i) for i in ids) or len(set(ids)) != len(ids):
            raise FederationError("invalid or duplicate node identities")
        return registry

    def _load(self, entry: dict) -> tuple[dict, list[dict]]:
        path = _safe(self.root, entry["manifest"])
        data = path.read_bytes()
        if _sha(data) != entry.get("manifest_sha256"):
            raise FederationError("node manifest integrity check failed")
        manifest = _json(data)
        if manifest.get("schema") != "atlas-forge.node.v1" or manifest.get("id") != entry["node_id"]:
            raise FederationError("node identity or schema mismatch")
        if not isinstance(manifest.get("enabled_by_default"), bool):
            raise FederationError("enabled_by_default must be boolean")
        raw = {}
        for f in manifest["snapshot_files"]:
            b = _safe(path.parent, f["path"]).read_bytes()
            if len(b) != f["size_bytes"] or _sha(b) != f["sha256"]:
                raise FederationError(f"snapshot integrity failure: {f['path']}")
            if f.get("git_blob_sha1") and _blob(b) != f["git_blob_sha1"]:
                raise FederationError("upstream Git blob mismatch")
            name = Path(f["path"]).name
            if name in raw: raise FederationError("duplicate snapshot filename")
            raw[name] = b
        records = _records(manifest, raw)
        return manifest, records

    def discover(self) -> dict:
        """List node state; one broken snapshot does not hide healthy nodes."""
        try: registry = self._registry()
        except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
            return {"schema": "atlas-forge.discovery.v1", "valid": False, "nodes": [], "errors": [str(exc)]}
        nodes, errors = [], []
        for entry in registry["nodes"]:
            try:
                manifest, records = self._load(entry)
                nodes.append({**manifest, "integrity": "passed", "manifest_sha256": entry["manifest_sha256"], "record_count": len(records)})
            except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
                errors.append({"node_id": entry["node_id"], "error": str(exc)})
                nodes.append({"id": entry["node_id"], "integrity": "failed", "error": str(exc)})
        return {"schema": "atlas-forge.discovery.v1", "forge_version": "0.3.0", "valid": not errors,
                "nodes": nodes, "edges": registry["edges"], "errors": errors, "notice": NOTICE}

    def search(self, question: str, *, node_ids: list[str] | None = None,
               include_starters: bool = False, per_node: int = 5) -> dict:
        if not isinstance(question, str) or len(question) > 4096:
            raise ValueError("question must be text of at most 4096 characters")
        if type(per_node) is not int or not 1 <= per_node <= 50:
            raise ValueError("per_node must be an integer from 1 to 50")
        registry = self._registry()
        known = {e["node_id"] for e in registry["nodes"]}
        if node_ids is not None and (not isinstance(node_ids, list) or not node_ids or not all(isinstance(s, str) for s in node_ids)):
            raise ValueError("node_ids must be a nonempty list of node IDs")
        if node_ids is not None and set(node_ids) - known:
            raise ValueError("unknown node IDs: " + ", ".join(sorted(set(node_ids) - known)))
        tokens = _tokens(question)
        groups, errors, excluded = [], [], []
        for entry in registry["nodes"]:
            nid = entry["node_id"]
            if node_ids is not None and nid not in node_ids: continue
            try: manifest, records = self._load(entry)
            except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
                errors.append({"node_id": nid, "error": str(exc)}); continue
            if not manifest["enabled_by_default"] and not include_starters:
                excluded.append({"node_id": nid, "reason": "starter_not_enabled; use include_starters explicitly"});continue
            # Exact-token lexical ranking within each node. A score is not confidence.
            bags = [_tokens(" ".join([r["title"], r["text"], _flatten(r["tags"]), r["domain"]])) for r in records]
            df = Counter(t for bag in bags for t in bag)
            hits = []
            for r, bag in zip(records, bags):
                overlap = bag & tokens
                if not overlap: continue
                title = _tokens(r["title"] + " " + _flatten(r["tags"]))
                score = sum((2 if t in title else 1) * (1 + math.log((len(records)+1)/(df[t]+1))) for t in overlap)
                hits.append({**r, "match_score": round(score, 6), "matched_terms": sorted(overlap)})
            hits.sort(key=lambda r: (-r["match_score"], r["record_uid"]))
            groups.append({"node_id": nid, "node_version": manifest["version"], "node_status": manifest["status"],
                           "manifest_sha256": entry["manifest_sha256"], "total_matches": len(hits), "results": hits[:per_node]})
        results = [r for group in groups for r in group["results"]]
        urls = defaultdict(set)
        for record in results:
            for s in record["sources"]: urls[s["url"].rstrip("/")].add(record["record_uid"])
        overlaps = [{"source_url": u, "record_uids": sorted(rs), "meaning": "shared citation, not independent corroboration"}
                    for u, rs in sorted(urls.items()) if len(rs) > 1]
        return {"schema": SCHEMA, "query": question, "status": "partial" if results else "unresolved",
                "answer_verified": False, "degraded": bool(errors), "groups": groups, "results": results,
                "excluded_nodes": excluded, "errors": errors, "shared_source_groups": overlaps,
                "registry_sha256": _sha((self.root/"registry.json").read_bytes()), "notice": NOTICE}

    def export(self, node_ids: list[str] | None = None, *, include_starters: bool = False) -> list[dict]:
        """Export original-status reference records; fail closed on a selected invalid node."""
        registry = self._registry()
        known = {e['node_id'] for e in registry['nodes']}
        if node_ids is not None and (not node_ids or set(node_ids) - known):
            raise ValueError('unknown or empty node selection')
        result = []
        for entry in registry['nodes']:
            if node_ids is not None and entry['node_id'] not in node_ids: continue
            manifest, records = self._load(entry)
            if manifest['enabled_by_default'] or include_starters: result.extend(records)
        return result
