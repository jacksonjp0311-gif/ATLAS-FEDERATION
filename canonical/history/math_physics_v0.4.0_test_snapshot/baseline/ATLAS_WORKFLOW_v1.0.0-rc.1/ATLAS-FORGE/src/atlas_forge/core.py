"""Small dependency-free, auditable research Atlas scaffold and validator."""
from __future__ import annotations
from importlib.resources import files
from pathlib import Path
from typing import Any
from datetime import date
import hashlib
import json
import re

KINDS = {"editorial", "source_reported", "formal_derivation", "simulation", "synthetic", "measured", "reproduced"}
STATUSES = {"editorial_pending_review", "portion_checked", "human_reviewed", "independently_reproduced"}


def canonical_bytes(obj: dict) -> bytes:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def packet_sha256(packet: dict) -> str:
    return hashlib.sha256(canonical_bytes({k: v for k, v in packet.items() if k != "content_sha256"})).hexdigest()


def rank_domains() -> list[dict]:
    return json.loads((files("atlas_forge") / "resources" / "top_ten.json").read_text(encoding="utf-8"))


def slugify(s: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", s.strip()).strip("-").upper()
    if not slug or len(slug) > 65:
        raise ValueError("Invalid domain slug")
    return slug


def make_packet(**kwargs: Any) -> dict:
    packet = {k: v for k, v in kwargs.items() if k != "content_sha256"}
    packet["content_sha256"] = packet_sha256(packet)
    return packet


def init_atlas(slug: str, out: str | Path) -> Path:
    policy = json.loads((files("atlas_forge") / "resources/workflow_policy.json").read_text(encoding="utf-8"))
    if slug.lower() != policy["active_domain"] and not policy["next_domain_allowed"]:
        raise ValueError("Measurement v1 acceptance is incomplete; creating another domain is blocked")
    matches = [d for d in rank_domains() if d["slug"] == slug.lower()]
    if not matches:
        raise ValueError("Unknown domain. Use rank to list choices")
    d = matches[0]
    target = Path(out) / slugify(d["title"])
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing project: {target}")
    target.mkdir(parents=True)
    (target / "data").mkdir()
    (target / "docs").mkdir()
    manifest = {"atlas_id": target.name.lower(), "title": d["title"], "version": "0.1.0", "schema_version": "1.0", "created_date": date.today().isoformat(), "purpose": "Evidence-preserving scientific reference", "mission": d["initial_scope"], "status": "starter_unvalidated", "packet_count": 0, "source_count": 0, "interfaces": ["jsonl", "python-cli"], "external_sources_mirrored": False}
    (target / "atlas_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (target / "data" / "packets.jsonl").write_text("", encoding="utf-8")
    (target / "data" / "sources.json").write_text("[]\n", encoding="utf-8")
    (target / "README.md").write_text(f"# {d['title']}\n\n> Scaffold only. No scientific claims have been independently verified.\n\n**Scope:** {d['initial_scope']}\n\n**Research cycle:** Discover → Verify → Connect → Teach → Reuse → Measure → Correct.\n\nStart with [{d['starter_source_description']}]({d['starter_source_url']}) as a **source lead**, not a licensed mirror or an independently verified claim.\n\nEdit source records, add bounded packets, update the manifest counts, validate, and keep a correction ledger before publication.\n", encoding="utf-8")
    (target / "docs" / "RESEARCH_BACKLOG.md").write_text("# Research backlog\n\n- [ ] Review primary source passages and rights\n- [ ] Create bounded, citation-backed packets with units and limits\n- [ ] Add corrections/contradictions and negative evidence\n- [ ] Perform independently authored query evaluation\n- [ ] Check versioning and release manifest\n",encoding="utf-8")
    return target


def _problem(errors: list[str], condition: bool, message: str):
    if not condition:
        errors.append(message)


def check_packet(p: dict, source_ids: set[str]) -> list[str]:
    e = []
    required = ["packet_id", "claim", "evidence_kind", "review_status", "source_id", "source_url", "source_locator", "inspected_scope", "applicability", "limitations", "rights", "version", "content_sha256"]
    for key in required:
        _problem(e, key in p and isinstance(p.get(key), str) and bool(p[key].strip()), f"missing or invalid {key}")
    _problem(e, p.get("evidence_kind") in KINDS, "unknown evidence_kind")
    _problem(e, p.get("review_status") in STATUSES, "unknown review_status")
    _problem(e, isinstance(p.get("source_id"), str) and p.get("source_id") in source_ids, "source_id absent from source registry")
    _problem(e, isinstance(p.get("source_url"), str) and p["source_url"].startswith(("http://", "https://")), "source_url must be HTTP(S)")
    _problem(e, packet_sha256(p) == p.get("content_sha256"), "content_sha256 mismatch")
    if p.get("evidence_kind") in {"synthetic", "simulation"}:
        _problem(e, p.get("review_status") != "independently_reproduced", "synthetic/simulation cannot claim independent experimental reproduction")
    if p.get("evidence_kind") == "measured":
        for key in ("artifact_sha256", "instrument", "calibration_context", "units"):
            _problem(e, bool(p.get(key)), f"measured packets require {key}")
    if p.get("review_status") in {"human_reviewed", "independently_reproduced"}:
        _problem(e, bool(p.get("reviewer")) and bool(p.get("review_artifact")), "independent/human review requires reviewer and review_artifact")
    if p.get("review_status") == "independently_reproduced":
        _problem(e, p.get("evidence_kind") == "reproduced", "independently_reproduced requires reproduced data kind")
    return e


def validate(path: str | Path) -> dict:
    path = Path(path)
    errors = []
    try:
        manifest = json.loads((path / "atlas_manifest.json").read_text(encoding="utf-8"))
        sources = json.loads((path / "data" / "sources.json").read_text(encoding="utf-8"))
        lines = (path / "data" / "packets.jsonl").read_text(encoding="utf-8").splitlines()
        packets = [json.loads(line) for line in lines if line.strip()]
    except (OSError, ValueError) as exc:
        return {"valid": False, "errors": [f"unreadable core file: {type(exc).__name__}: {exc}"], "packets": 0, "sources": 0}
    if not isinstance(manifest, dict) or not isinstance(sources, list):
        return {"valid": False, "errors": ["manifest must be object and sources must be list"], "packets": len(packets), "sources": 0}
    _problem(errors, bool(manifest.get("atlas_id")) and bool(manifest.get("title")), "missing atlas identity")
    _problem(errors, manifest.get("schema_version") == "1.0", "unsupported manifest schema")
    _problem(errors, manifest.get("packet_count") == len(packets), "packet_count mismatch")
    _problem(errors, manifest.get("source_count") == len(sources), "source_count mismatch")
    source_ids = set()
    for i,s in enumerate(sources):
        if not isinstance(s,dict):
            errors.append(f"source {i} not an object"); continue
        _problem(errors, bool(s.get("source_id")), f"source {i} missing source_id")
        _problem(errors, isinstance(s.get("url"), str) and s["url"].startswith("https://"), f"source {i} must use HTTPS")
        _problem(errors, bool(s.get("version")) and bool(s.get("rights")), f"source {i} missing version/rights")
        sid = s.get("source_id")
        if not isinstance(sid, str) or not sid:
            errors.append(f"source {i}: invalid source_id")
        elif sid in source_ids:
            errors.append(f"duplicate source ID {sid}")
        else:
            source_ids.add(sid)
    packet_ids=set()
    for i,p in enumerate(packets):
        if not isinstance(p,dict): errors.append(f"packet {i} not an object"); continue
        pid = p.get("packet_id")
        if not isinstance(pid, str) or not pid:
            errors.append(f"packet {i}: invalid packet_id")
        elif pid in packet_ids:
            errors.append(f"duplicate packet ID {pid}")
        else:
            packet_ids.add(pid)
        errors.extend(f"packet {i}: {t}" for t in check_packet(p,source_ids))
        match = next((s for s in sources if isinstance(s,dict) and s.get("source_id")==p.get("source_id")),None)
        if match and match.get("url")!=p.get("source_url"):
            errors.append(f"packet {i}: source_url disagrees with registered source")
    return {"valid": not errors, "errors": errors, "packets":len(packets),"sources":len(sources),"atlas_id":manifest.get("atlas_id")}


def query(path: str | Path, question: str, limit: int=5) -> dict:
    verdict = validate(path)
    if not verdict["valid"]:
        return {"status":"invalid_atlas", "errors":verdict["errors"],"results":[]}
    tokens = set(re.findall(r"[a-z0-9]+",question.lower())) - {"what","is","the","a","and","of","how","do","to"}
    if not tokens:
        return {"status":"unresolved", "results":[],"reason":"no distinctive query terms"}
    packets=[json.loads(line) for line in (Path(path)/"data"/"packets.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    hits=[]
    for p in packets:
        text=" ".join(str(p.get(k,"")) for k in ["packet_id","claim","applicability","limitations"])
        words=set(re.findall(r"[a-z0-9]+",text.lower()))
        score=len(words&tokens)
        if score: hits.append((score,p))
    hits.sort(key=lambda x:(-x[0],x[1]["packet_id"]))
    return {"status":"partial" if hits else "unresolved", "results":[{"match_score":score,**p} for score,p in hits[:limit]],"notice":"Lexical reference hits only; not a verified answer" if hits else "No relevant evidence packet; live research or human review needed"}
