"""A fail-closed candidate-receipt bridge, not a Bitwork implementation.

No arbitrary command execution. A host can run its approved router separately,
then submit a receipt whose IDs and revisions resolve in the pinned Atlas store.
The receipt is self-reported; structural validation does not attest runtime use.
"""
from __future__ import annotations
from copy import deepcopy
import math
from .common import AtlasStore, ContractError, canonical, sha

SCHEMA = "atlas.route-receipt/1"


def route_request(store: AtlasStore, question: str, node_ids: list[str] | None = None) -> dict:
    # Reuse common query validation. The candidate feature export is data only.
    store.search(question,node_ids=node_ids,limit=1)
    result={"schema":"atlas.route-request/1","question":question,"node_ids":sorted(node_ids) if node_ids else None,
        "registry_revision":store.registry_revision,
        "mapping":[{"record_id":r["record_id"],"revision":r["revision"],"node_id":r["node_id"],
                    "title":r["title"],"text":r["content"]["text"],"tags":r["content"]["tags"]}
                   for r in store.export() if r["type"]!="source" and r["status"] not in {"withdrawn","superseded"}
                   and r["rights"]["status"]=="local_reference" and (not node_ids or r["node_id"] in node_ids)],
        "requirements":["Return exact record IDs and revisions; never replace them with category labels.",
                        "Declare runtime, encoder and index revisions. Scores are not scientific confidence.",
                        "Return abstain explicitly when support is insufficient. No commands are accepted."]}
    result["request_sha256"]=sha(canonical(result));return result


def validate_route_receipt(store: AtlasStore, question: str, node_ids: list[str] | None, receipt: dict) -> tuple[list[dict] | None,str | None]:
    try:
        required={"schema","request_sha256","registry_revision","runtime","encoder_revision","index_revision","status","candidates"}
        if not isinstance(receipt,dict) or set(receipt)!=required or receipt["schema"]!=SCHEMA:raise ContractError("invalid route receipt fields")
        request=route_request(store,question,node_ids)
        if receipt["request_sha256"]!=request["request_sha256"] or receipt["registry_revision"]!=store.registry_revision:raise ContractError("stale or foreign route receipt")
        runtime=receipt["runtime"]
        if not isinstance(runtime,dict) or set(runtime)!={"name","version","implementation_commit","execution_evidence"}:raise ContractError("runtime identity required")
        for key in runtime:
            if not isinstance(runtime[key],str) or not runtime[key].strip():raise ContractError("runtime identity has empty fields")
        for key in ("encoder_revision","index_revision"):
            if not isinstance(receipt[key],str) or not receipt[key].strip():raise ContractError("encoder/index revision required")
        if receipt["status"] not in {"candidates","abstain","error"}:raise ContractError("unsupported route status")
        if not isinstance(receipt["candidates"],list) or len(receipt["candidates"])>100:raise ContractError("invalid candidate list")
        if receipt["status"]!="candidates":return None,"external_router_"+receipt["status"]
        if not receipt["candidates"]:return None,"external_router_empty"
        seen=set();out=[];allowed={r["record_id"] for r in request["mapping"]}
        for c in receipt["candidates"]:
            if not isinstance(c,dict) or set(c)!={"record_id","revision","score","score_kind"}:raise ContractError("invalid route candidate")
            if not isinstance(c["record_id"],str) or c["record_id"] in seen or c["record_id"] not in allowed:raise ContractError("duplicate, foreign, or out-of-scope route candidate")
            if type(c["score"]) not in {int,float} or not math.isfinite(c["score"]):raise ContractError("candidate score must be finite")
            if not isinstance(c["score_kind"],str) or not c["score_kind"].strip():raise ContractError("score scale required")
            r=store.fetch(c["record_id"],c["revision"]);seen.add(c["record_id"])
            out.append({**deepcopy(c),"node_id":r["node_id"],"title":r["title"],"score_is_probability":False})
        return out,None
    except (KeyError,TypeError,ValueError,OSError) as exc:
        return None,str(exc)
