"""Offline, dependency-free fixity and knowledge-gap audit.

Checks bytes and internal references; DOES NOT verify science, source truth,
research completeness, copyright clearance or author identity.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path


def _sha(raw:bytes)->str:return hashlib.sha256(raw).hexdigest()
def _canonical(v)->bytes:return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
def _json(p:Path):return json.loads(p.read_text(encoding='utf-8'))


def audit_archive(root:Path, *, check_inventory:bool=False)->dict:
    root=Path(root).resolve()
    errors=[];warnings=[]
    registry=root/'common/registry.json'
    if not registry.is_file():return {'result':'failed','errors':['common registry unavailable']}
    data=_json(registry)
    nodes=data['nodes'];records={};relations=[];by_node={};source_ids=[]
    for node in nodes:
        nid=node['node_id'];p=(root/'common'/node['manifest']).resolve()
        if not p.is_relative_to(root/'common') or not p.is_file():errors.append('missing/unsafe node manifest: '+nid);continue
        if _sha(p.read_bytes())!=node['manifest_sha256']:errors.append('node manifest hash mismatch: '+nid)
        manifest=_json(p)
        if manifest['node_id']!=nid:errors.append('node ID mismatch: '+nid)
        by_node[nid]={'records':0,'sources':0,'relations':0}
        for collection,entry in manifest['collections'].items():
            f=(p.parent/entry['path']).resolve()
            if not f.is_relative_to(p.parent) or not f.is_file():errors.append('missing/unsafe member '+str(f));continue
            raw=f.read_bytes()
            if _sha(raw)!=entry['sha256']:errors.append('collection checksum mismatch '+str(f))
            entries=[json.loads(line) for line in raw.splitlines() if line.strip()]
            if len(entries)!=entry['records']:errors.append('collection count mismatch '+str(f))
            for rec in entries:
                h=rec.get('revision');computed=_sha(_canonical({k:v for k,v in rec.items() if k!='revision'}))
                if h!=computed:errors.append('record/relation revision mismatch '+str(rec.get('record_id',rec.get('relation_id'))))
                if collection=='relations':relations.append(rec);by_node[nid]['relations']+=1
                else:
                    rid=rec['record_id']
                    if rid in records:errors.append('duplicate record ID '+rid)
                    records[rid]=rec;by_node[nid]['records']+=1
                    if rec.get('type')=='source':source_ids.append(rid);by_node[nid]['sources']+=1
    for rid,r in records.items():
        for src in r.get('sources',[]):
            s=records.get(src['record_id'])
            if s is None or s['revision']!=src['revision'] or s['type']!='source':errors.append('source closure failure '+rid)
    for rel in relations:
        for key in ('from','to'):
            x=rel[key];r=records.get(x['record_id'])
            if r is None or r['revision']!=x['revision']:errors.append('relation closure failure '+rel['relation_id'])
    if check_inventory:
        p=root/'FILE_MANIFEST.json'
        if not p.is_file():errors.append('release file inventory absent')
        else:
            inventory=_json(p)['files']
            for rel,digest in inventory.items():
                f=(root/rel).resolve()
                if not f.is_relative_to(root) or not f.is_file() or _sha(f.read_bytes())!=digest:
                    errors.append('file inventory mismatch '+rel)
    # The source cards are generally locators, not files. Never infer local source
    # possession from a publication URL or from a hash copied into metadata.
    declared_sources=len(source_ids)
    authenticated_original=[]
    for rid in source_ids:
        src=records[rid];pro=src.get('provenance',{})
        loc=pro.get('original_byte_path')
        hash_value=pro.get('original_byte_sha256')
        if loc and hash_value:
            path=(root/loc).resolve()
            if path.is_relative_to(root) and path.is_file() and _sha(path.read_bytes())==hash_value:
                authenticated_original.append(rid)
    if declared_sources>len(authenticated_original):
        warnings.append('Many source cards have no locally authenticated original bytes; the archive is not fully offline-primary-source recoverable.')
    roadmap=_json(root/'DOMAIN_QUEUE.json')
    planned=roadmap.get('candidates',[])
    content_ready=sum(bool(x.get('content_ready',False)) for x in planned)
    return {'schema':'atlas.offline-survival-audit/1','result':'passed_structural_only' if not errors else 'failed',
        'nodes':len(by_node),'record_count':len(records),'source_cards':declared_sources,
        'verified_local_primary_source_files':len(authenticated_original),
        'relation_count':len(relations),'by_node':by_node,
        'domain_candidates_declared':len(planned),'content_ready_candidates_in_roadmap':content_ready,
        'full_human_knowledge_preserved':False,
        'scientific_validity_independently_verified':False,
        'all_primary_sources_available_offline':len(authenticated_original)==declared_sources,
        'global_router_built':False,'desktop_transfer_complete':False,
        'errors':errors,'warnings':warnings,
        'interpretation':'Byte/reference closure only. No truth, author, rights, science, or backup-location certification.'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument('--out',type=Path)
    p.add_argument('--check-files',action='store_true')
    args=p.parse_args();report=audit_archive(args.root,check_inventory=args.check_files)
    if args.out:args.out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps(report,indent=2,ensure_ascii=False))
    raise SystemExit(report['result']=='failed')
if __name__=='__main__':main()
