#!/usr/bin/env python3
"""ATLAS FORGE external evidence-gap intake v0.1 (offline, stdlib only).

This is an ADDITIVE companion to the ORIGINAL ATLAS FORGE continuity v0.5.0.
It does not edit the canonical federation, mark scientific results verified,
validate a human reviewer's competence, prove original document authenticity,
or authorize physical/clinical/safety operations. It checks only integrity,
registry identity, format completeness, and missing evidence obligations.

Commands:
    plan --atlas /path/to/extracted/ATLAS --out gaps.json
    inspect --atlas /path/to/extracted/ATLAS --proposal my.json --workspace /evidence --out receipt.json
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path
from typing import Any

ORIGINAL_QUEUE_SHA256 = '9b3ceb5d942fa556e17cb3b731ed9a95b0468e795ed2c1ff8e21864c3e264c33'
SCHEMA = 'atlas.external-evidence-proposal/1'
KINDS = ('source_original','independent_review','physical_measurement','negative_result','software_reproduction')
GATE_HOLD = 'RECORDED_UNVERIFIED_EXTERNAL_REVIEW_REQUIRED'
GATE_INVALID = 'REJECTED_INCOMPLETE_OR_INCONSISTENT'
REQUIRED_METADATA = {
    'source_original': ('publisher_url','publication_edition','source_locator','rights_status','acquisition_method'),
    'independent_review': ('reviewer_identifier','independence_declaration','review_scope','conflicts_disclosed'),
    'physical_measurement': ('sample_identifier','instrument_identifier','calibration_reference','units','measurement_uncertainty','method'),
    'negative_result': ('failure_observation','test_conditions','expected_result','actual_result'),
    'software_reproduction': ('runtime_version','test_command','independent_implementation','input_fixture_digest'),
}
class EvidenceError(ValueError):
    pass


def canonical(x:Any)->bytes:
    return json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode('utf-8')


def sha(raw:bytes)->str:return hashlib.sha256(raw).hexdigest()


def file_sha(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(4<<20),b''):h.update(block)
    return h.hexdigest()


def strict_json(source:bytes|str):
    def pairs(items):
        d={}
        for k,v in items:
            if k in d:raise EvidenceError(f'duplicate JSON key {k}')
            d[k]=v
        return d
    def invalid(v):raise EvidenceError(f'nonfinite literal {v}')
    try:return json.loads(source,object_pairs_hook=pairs,parse_constant=invalid)
    except (ValueError,UnicodeError) as exc:raise EvidenceError(f'invalid JSON: {exc}') from exc


def safe_child(root:Path,relative:str)->Path:
    if type(relative) is not str or not relative or relative.startswith('/') or '\\' in relative or ':' in relative:
        raise EvidenceError('unsafe relative evidence path')
    p=Path(relative)
    if p.is_absolute() or any(x in ('','.','..') for x in p.parts):
        raise EvidenceError('unsafe evidence components')
    cur=root.resolve()
    for x in p.parts:
        cur=cur/x
        if cur.is_symlink():raise EvidenceError('refuse symlink in evidence path')
    if not cur.resolve().is_relative_to(root.resolve()):raise EvidenceError('file escapes permitted evidence workspace')
    return cur


def _registry(root:Path):
    p=root/'common/registry.json';lock=root/'common/registry.lock.json'
    if not p.is_file() or not lock.is_file():raise EvidenceError('missing original Atlas registry')
    doc=strict_json(p.read_bytes());seal=strict_json(lock.read_bytes())
    if seal.get('sha256')!=file_sha(p):raise EvidenceError('registry lock mismatch')
    if doc.get('schema')!='atlas.registry/1':raise EvidenceError('unexpected Atlas registry schema')
    items=doc.get('nodes',[])
    if not isinstance(items,list):raise EvidenceError('registry nodes must be list')
    result={}
    for item in items:
        n=item.get('node_id') if isinstance(item,dict) else None
        if not isinstance(n,str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',n) or n in result:
            raise EvidenceError('invalid or repeated node')
        result[n]=item
    return result


def original_domain_plan(root:Path):
    """Only report ORIGINAL queue slot presence; do not infer scientific acceptance."""
    root=Path(root).resolve();q=root/'DOMAIN_QUEUE.json'
    if file_sha(q)!=ORIGINAL_QUEUE_SHA256:raise EvidenceError('frozen original 30-domain queue digest changed')
    queue=strict_json(q.read_bytes());entries=queue.get('candidates')
    if queue.get('schema')!='atlas.domain-queue/2' or type(entries) is not list or len(entries)!=30:
        raise EvidenceError('unexpected original domain queue')
    priorities=[];ids=[]
    for row in entries:
        if not isinstance(row,dict):raise EvidenceError('malformed original candidate')
        no=row.get('priority');node=row.get('node_id')
        if type(no) is not int or not isinstance(node,str):raise EvidenceError('invalid priority/name')
        priorities.append(no);ids.append(node)
    if sorted(priorities)!=list(range(1,31)) or len(set(ids))!=30:raise EvidenceError('original queue is not uniquely numbered 1..30')
    registry=_registry(root)
    represented=[{'priority':x['priority'],'node':x['node_id'],'name':x['name'],
                  'queue_stated_status':x.get('status'),'registered_node':True,
                  'final_scientific_acceptance':'NOT_PROVEN_BY_NODE_PRESENCE'} for x in entries if x['node_id'] in registry]
    absent=[{'priority':x['priority'],'node':x['node_id'],'name':x['name'],
             'queue_stated_status':x.get('status'),'registered_node':False,
             'acceptance':'BLOCKED_NO_NODE'} for x in entries if x['node_id'] not in registry]
    extra=sorted(set(registry)-set(ids))
    report={'schema':'atlas.continuity-gap-closure-plan/1','source_edition':'Computer_Architecture_v0.5.0_continuity',
       'source_queue_sha256':file_sha(q),'registered_node_count':len(registry),
       'original_queue_count':30,'represented_original_domain_count':len(represented),
       'missing_original_domain_count':len(absent),'additional_enabling_nodes':extra,
       'represented':represented,'missing_domains':absent,
       'next_missing_original_priority':absent[0] if absent else None,
       'scientific_evidence':'All source authenticity, external peer review, and physical measurements require independent evidence; no acceptance inferred',
       'router_scope':'DEFER until original domain content completed',
       'preservation':'Read-only diagnostic. Does not alter any original Atlas files or historical statuses.'}
    return report


def _record(root:Path,id:str,expected_revision:str):
    if type(id) is not str or ':' not in id:raise EvidenceError('exact target record ID required')
    node=id.split(':',1)[0]
    reg=_registry(root)
    if node not in reg:raise EvidenceError('target node not registered')
    manifest_file=safe_child(root/'common',reg[node]['manifest'])
    if file_sha(manifest_file)!=reg[node]['manifest_sha256']:raise EvidenceError('node manifest hash mismatch')
    m=strict_json(manifest_file.read_bytes());folder=manifest_file.parent
    for kind,entry in m['collections'].items():
        if kind=='relations':continue
        path=safe_child(folder,entry['path'])
        if file_sha(path)!=entry['sha256']:raise EvidenceError('record collection sha256 mismatch')
        for line in path.read_bytes().splitlines():
            obj=strict_json(line)
            if obj.get('record_id')!=id:continue
            if obj.get('node_id')!=node:raise EvidenceError('foreign record')
            old=obj.get('revision')
            if type(old) is not str or sha(canonical({k:v for k,v in obj.items() if k!='revision'}))!=old:
                raise EvidenceError('record revision invalid')
            if old!=expected_revision:raise EvidenceError('submitted revision does not match exact Atlas record')
            return obj
    raise EvidenceError('target record ID not present in current edition')


def inspect_proposal(atlas:Path,workspace:Path,proposal:dict):
    """Structural intake only. ACCEPTED/INDEPENDENTLY_VERIFIED are never returned."""
    atlas=Path(atlas).resolve();workspace=Path(workspace).resolve()
    findings=[]
    try:
        if type(proposal) is not dict or proposal.get('schema')!=SCHEMA:raise EvidenceError('unsupported evidence proposal schema')
        kind=proposal.get('kind')
        if kind not in KINDS:raise EvidenceError('unsupported evidence type')
        target=proposal.get('target')
        if type(target) is not dict or set(target)!={'record_id','revision'}:
            raise EvidenceError('exact record_id and revision required')
        if not re.fullmatch(r'[0-9a-f]{64}',str(target.get('revision'))):raise EvidenceError('record revision must be SHA-256')
        record=_record(atlas,target['record_id'],target['revision'])
        evidence=proposal.get('artifact')
        if type(evidence) is not dict or set(evidence)!={'relative_path','sha256'}:
            raise EvidenceError('artifact path and hash required')
        if not re.fullmatch(r'[0-9a-f]{64}',str(evidence.get('sha256'))):raise EvidenceError('invalid artifact digest')
        path=safe_child(workspace,evidence['relative_path'])
        if not path.is_file():raise EvidenceError('evidence bytes not present')
        if path.stat().st_size==0:raise EvidenceError('empty evidence artifact')
        if path.stat().st_size>100_000_000:raise EvidenceError('evidence file exceeds 100 MB bounded intake; split with own manifest')
        dig=file_sha(path)
        if dig!=evidence['sha256']:raise EvidenceError('evidence file SHA-256 mismatch')
        meta=proposal.get('metadata')
        if type(meta) is not dict:raise EvidenceError('typed metadata object required')
        missing=[k for k in REQUIRED_METADATA[kind] if k not in meta or meta[k] in (None,'',[],{})]
        if missing:raise EvidenceError('required metadata missing: '+', '.join(missing))
        if kind=='physical_measurement':
            for field in ('sample_identifier','instrument_identifier','calibration_reference','units','method'):
                if type(meta[field]) is not str or not meta[field].strip():
                    raise EvidenceError('measurement metadata field must be substantive text: '+field)
            u=meta['measurement_uncertainty']
            if type(u) not in (int,float) or u<0 or u!=u or u==float('inf'):
                raise EvidenceError('nonnegative finite declared standard uncertainty required')
        if kind=='independent_review':
            if type(meta['independence_declaration']) is not str or not meta['independence_declaration'].strip():
                raise EvidenceError('textual independent reviewer declaration required')
        if kind=='source_original' and meta['rights_status'] not in ('unknown','permission_claimed','rights_review_pending','public_domain_claimed'):
            raise EvidenceError('unsupported rights declaration, cannot claim license approved by metadata')
        return {'schema':'atlas.external-evidence-intake-result/1','status':GATE_HOLD,
           'record_id':record['record_id'],'record_revision':record['revision'],
           'kind':kind,'byte_integrity_verified':True,'metadata_shape_complete':True,
           'original_publisher_authenticated':False,'external_scientific_review_accepted':False,
           'physical_measurement_validated_by_lab':False,'rights_cleared_for_publication':False,
           'next_action':'Independent authentication and qualified review of artifact provenance, methods and scope',
           'note':'File hash and proposal metadata only; no scientific truth or safety certification is inferred'}
    except (EvidenceError,KeyError,TypeError,OSError,ValueError) as exc:
        findings.append(str(exc)[:400])
        return {'schema':'atlas.external-evidence-intake-result/1','status':GATE_INVALID,
            'byte_integrity_verified':False,'metadata_shape_complete':False,
            'original_publisher_authenticated':False,'external_scientific_review_accepted':False,
            'physical_measurement_validated_by_lab':False,'rights_cleared_for_publication':False,
            'reasons':findings}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    plan=sub.add_parser('plan',help='read-only report from the immutable original domain queue')
    plan.add_argument('--atlas',type=Path,required=True);plan.add_argument('--out',type=Path,required=True)
    check=sub.add_parser('inspect',help='validate artifact bytes and exact record target; never certifies science')
    check.add_argument('--atlas',type=Path,required=True);check.add_argument('--workspace',type=Path,required=True)
    check.add_argument('--proposal',type=Path,required=True);check.add_argument('--out',type=Path,required=True)
    args=parser.parse_args(argv)
    try:
        if args.command=='plan':out=original_domain_plan(args.atlas)
        else:out=inspect_proposal(args.atlas,args.workspace,strict_json(args.proposal.read_bytes()))
        args.out.parent.mkdir(parents=True,exist_ok=True)
        if args.out.exists():raise EvidenceError('refuse to overwrite existing audit receipt')
        args.out.write_text(json.dumps(out,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
        print(json.dumps({'result':out.get('status','report_created'),'receipt':str(args.out),'sha256':file_sha(args.out)}))
        return 0 if args.command=='plan' or out['status']!=GATE_INVALID else 2
    except (OSError,EvidenceError,TypeError,ValueError) as exc:
        print(json.dumps({'result':'FAIL_CLOSED','reason':str(exc)[:400]}),file=sys.stderr)
        return 2

if __name__=='__main__':raise SystemExit(main())
