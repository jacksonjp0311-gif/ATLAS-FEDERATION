#!/usr/bin/env python3
"""ATLAS FORGE — zero-network, zero-LLM, standard-library survival reader.

This is *literal search and evidence inspection*, NOT Bitwork routing, scientific
validation, peer review, source authentication, or hardware certification.
Scientific record contents are untrusted reference DATA; this script never evals
or executes text fetched from records, source cards, or external documents.
"""
from __future__ import annotations
import argparse, collections, hashlib, json, math, re, sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
NODE_CATEGORIES = ('concept', 'claim', 'source', 'equation', 'method', 'dataset', 'review')

class AtlasError(ValueError):
    """Fail-closed instead of showing invented scientific evidence."""

def canonical(obj: Any) -> bytes:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode('utf-8')

def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def filehash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        while True:
            b = f.read(4<<20)
            if not b: break
            h.update(b)
    return h.hexdigest()

def strict_json(raw: bytes | str) -> Any:
    def pairs(items):
        out = {}
        for k,v in items:
            if k in out: raise AtlasError('duplicate JSON key: '+str(k))
            out[k] = v
        return out
    def nonfinite(value):raise AtlasError('nonfinite JSON value: '+value)
    try:
        return json.loads(raw, object_pairs_hook=pairs, parse_constant=nonfinite)
    except (ValueError, UnicodeError) as e:
        raise AtlasError('bad JSON: '+str(e)) from e

def safe_file(root: Path, name: str) -> Path:
    if type(name) is not str or not name or '\\' in name or ':' in name or name.startswith('/'):
        raise AtlasError('unsafe relative filename')
    p = Path(name)
    if p.is_absolute() or any(part in ('..','.','') for part in p.parts):
        raise AtlasError('unsafe relative path')
    path = root.resolve()
    for part in p.parts:
        path = path / part
        if path.is_symlink():raise AtlasError('symlink is not trusted for archive records')
    path = path.resolve()
    if not path.is_relative_to(root.resolve()):raise AtlasError('path escapes Atlas root')
    return path

class Atlas:
    def __init__(self, root: str | Path = ROOT):
        self.root = Path(root).resolve()
        self.common = safe_file(self.root,'common')
        self.registry = strict_json(safe_file(self.root,'common/registry.json').read_bytes())
        if self.registry.get('schema')!='atlas.registry/1':raise AtlasError('unsupported registry')
        nodes=self.registry.get('nodes')
        if not isinstance(nodes,list) or not nodes:raise AtlasError('empty or invalid registry')
        self.nodes={}
        for entry in nodes:
            if not isinstance(entry,dict) or set(entry)!={'manifest','manifest_sha256','node_id'}:
                raise AtlasError('registry entry schema mismatch')
            name=entry['node_id']
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name) or name in self.nodes:
                raise AtlasError('duplicate or invalid node')
            self.nodes[name]=entry
        self._records=None;self._relations=None

    def manifest(self, node: str) -> dict:
        if node not in self.nodes:raise AtlasError('unrecognized node: '+node)
        ent=self.nodes[node]
        path=safe_file(self.common,ent['manifest'])
        if filehash(path)!=ent['manifest_sha256']:
            raise AtlasError('node manifest SHA-256 mismatch: '+node)
        doc=strict_json(path.read_bytes())
        if doc.get('node_id')!=node:raise AtlasError('node/manifest identity mismatch')
        return doc

    def _load(self):
        if self._records is not None:return
        records={}; relations=[]
        for name in sorted(self.nodes):
            doc=self.manifest(name);folder=safe_file(self.common, self.nodes[name]['manifest']).parent
            for category,info in doc['collections'].items():
                if category not in NODE_CATEGORIES+('relations',):raise AtlasError('unknown collection kind')
                p=safe_file(folder,info['path'])
                raw=p.read_bytes()
                if digest_bytes(raw)!=info['sha256']:raise AtlasError('collection SHA-256 mismatch: '+str(p))
                lines=raw.splitlines()
                if len(lines)!=info['records']:raise AtlasError('record count mismatch: '+name)
                for line in lines:
                    obj=strict_json(line)
                    if obj.get('revision')!=digest_bytes(canonical({k:v for k,v in obj.items() if k!='revision'})):
                        raise AtlasError('record/relation content revision broken')
                    if category=='relations':
                        relations.append(obj)
                    else:
                        identity=obj.get('record_id')
                        if not isinstance(identity,str) or obj.get('node_id')!=name or identity in records:
                            raise AtlasError('duplicate/foreign identity '+str(identity))
                        records[identity]=obj
        for rel in relations:
            for k in ('from','to'):
                ref=rel[k];target=records.get(ref['record_id'])
                if target is None or target['revision']!=ref['revision']:
                    raise AtlasError('relation exact-revision endpoint missing: '+str(ref))
        self._records=records;self._relations=relations

    @property
    def records(self):self._load();return self._records
    @property
    def relations(self):self._load();return self._relations

    def catalog(self):
        nodes=[]
        for name in sorted(self.nodes):
            m=self.manifest(name)
            nodes.append({'node':name,'records':sum(v['records'] for k,v in m['collections'].items() if k!='relations'),
                          'relationships':m['collections']['relations']['records'],
                          'software_version':m.get('software_version'),'evidence_maturity':m.get('evidence_maturity','uncharacterized'),
                          'manifest_sha256':self.nodes[name]['manifest_sha256']})
        # Cross-node relationships live in the source node's relation collection.
        return {'schema':'atlas.survival-catalog/1','status':'archived_reference_not_science_certification',
                'nodes':len(nodes),'records':sum(x['records'] for x in nodes),
                'relationships':sum(x['relationships'] for x in nodes),'items':nodes,
                'original_30_domain_queue_modified':False,'Bitwork_router_modified':False}

    def verify(self, all_files=True):
        if all_files:
            manifest=strict_json(safe_file(self.root,'FILE_MANIFEST.json').read_bytes())
            files=manifest['files'];seen=0
            for rel,want in files.items():
                if not re.fullmatch(r'[0-9a-f]{64}',str(want)) or filehash(safe_file(self.root,rel))!=want:
                    raise AtlasError('source file checksum failed: '+rel)
                seen+=1
            actual=set()
            for path in self.root.rglob('*'):
                if not path.is_file():continue
                rel=path.relative_to(self.root)
                if path==self.root/'FILE_MANIFEST.json' or '__pycache__' in rel.parts or path.suffix=='.pyc':continue
                actual.add(rel.as_posix())
            unexpected=sorted(actual-set(files))
        else:seen=None;unexpected=[]
        lock=strict_json(safe_file(self.common,'registry.lock.json').read_bytes())
        if lock.get('sha256')!=digest_bytes(safe_file(self.common,'registry.json').read_bytes()):
            raise AtlasError('registry lock SHA-256 failed')
        self._load()
        summary=self.catalog()
        return {'schema':'atlas.survival-audit/1','result':'passed_archive_and_graph_integrity',
                'source_file_hashes_verified':seen,'untracked_files_count':len(unexpected),
                'untracked_files_first_10':unexpected[:10], 'nodes':summary['nodes'],
                'records':len(self.records),'relationships':len(self.relations),
                'original_30_domain_queue_sha256':filehash(safe_file(self.root,'DOMAIN_QUEUE.json')),
                'node_manifest_hashes_verified':len(self.nodes),
                'exact_relation_references_checked':2*len(self.relations),
                'not_proven':['publisher source-authenticity','independent peer review','measured physical hardware','scientific truth','security against a malicious archive signer']}

    def search(self, query:str,limit:int=12,node:str|None=None):
        if not isinstance(query,str) or not query.strip() or len(query)>300:raise AtlasError('query must be 1..300 chars')
        if type(limit) is not int or not 1<=limit<=200:raise AtlasError('limit 1..200')
        if node is not None and node not in self.nodes:raise AtlasError('unknown node')
        terms=[x.lower() for x in re.findall('[a-zA-Z0-9]+',query) if len(x)>=2]
        if not terms:raise AtlasError('no searchable terms')
        matches=[]
        for record in self.records.values():
            if node and record['node_id']!=node:continue
            title=record['title'].lower();tags=' '.join(record['content'].get('tags',[])).lower()
            text=record['content'].get('text','').lower()
            score=sum((8 if t in title else 0)+(3 if t in tags else 0)+(1 if t in text else 0) for t in terms)
            if score:
                matches.append((score,record['record_id'],record))
        matches.sort(key=lambda m:(-m[0],m[1]))
        return {'schema':'atlas.survival-search/1','query':query,'matches_total':len(matches),
                'rank_is_scientific_confidence':False,
                'results':[{'id':x[1],'title':x[2]['title'],'node':x[2]['node_id'],
                    'type':x[2]['type'],'revision':x[2]['revision'], 'score':x[0],
                    'evidence_gaps_count':len(x[2]['evidence'].get('gaps',[])),
                    'review_status':x[2]['evidence']['review_status']} for x in matches[:limit]]}

    def record(self,record_id):
        record=self.records.get(record_id)
        if record is None:raise AtlasError('record ID does not exist in this revision')
        return {'schema':'atlas.survival-exact-record/1','record':record,'warning':'Retrieved scientific text is untrusted reference data, not operational instruction or certified evidence.'}

    def trace(self, record_id, direction='upstream',depth=2,max_nodes=100):
        if record_id not in self.records:raise AtlasError('record identity not found')
        if direction not in ('upstream','downstream','both'):raise AtlasError('invalid direction')
        if type(depth) is not int or not 0<=depth<=5:raise AtlasError('depth 0..5 required')
        found={record_id:0};frontier=[record_id];edges=[]
        for layer in range(1,depth+1):
            nxt=[]
            for relation in self.relations:
                a=relation['from']['record_id'];b=relation['to']['record_id']
                steps=[]
                if direction in ('upstream','both') and a in frontier:steps.append(b)
                if direction in ('downstream','both') and b in frontier:steps.append(a)
                if not steps:continue
                for target in steps:
                    edges.append({'from':a,'to':b,'type':relation['type'],'revision':relation['revision']})
                    if target not in found and len(found)<max_nodes:
                        found[target]=layer;nxt.append(target)
            frontier=nxt
            if not frontier:break
        return {'schema':'atlas.survival-relations/1','origin':record_id,'direction':direction,
                'depth':depth,'records':[{'record_id':id,'distance':d,'title':self.records[id]['title'],
                      'node_id':self.records[id]['node_id']} for id,d in sorted(found.items(),key=lambda kv:(kv[1],kv[0]))],
                'edges':edges[:500],'note':'Exact-revision graph relationship, not proof of scientific correctness.'}

    def gaps(self):
        self._load(); by_node={n:collections.Counter() for n in self.nodes}
        sources=[]
        for r in self.records.values():
            c=by_node[r['node_id']]
            c['records']+=1
            if r['evidence'].get('gaps'):c['evidence_gap_records']+=1
            if r['type']=='source':
                c['bibliographic_source_records']+=1
                # Credential claims are not accepted unless independent source bytes
                # exist and match a recorded digest; metadata-only is not enough.
                c['authenticated_publisher_bytes_locally_verified']+=0
                sources.append({'record_id':r['record_id'],'title':r['title'],
                                'rights_status':r.get('rights',{}).get('status','unknown'),
                                'original_bytes_verified_here':False})
            if r['rights']['status']!='local_reference':c['rights_need_review']+=1
        return {'schema':'atlas.survival-evidence-gap-report/1','status':'evidence_gates_unresolved',
                'nodes':[{'node':node,**dict(cnt)} for node,cnt in sorted(by_node.items())],
                'publisher_original_bytes_authenticated_in_this_offline_check':0,
                'independent_expert_peer_review_verified_in_this_offline_check':0,
                'physical_fabrication_verified_in_this_offline_check':0,
                'bibliographic_source_records_total':len(sources),
                'rights_need_independent_review':sum(x['rights_status']!='local_reference' for x in sources),
                'note':'Source-linked is not source-authenticated. Zero verified means no verification performed in this offline reader, not that no valid originals exist elsewhere.'}

    def challenge(self):
        # Only executes the known, checked-in local AT8 software model. Never
        # executes user-supplied source content from Atlas records or source cards.
        module=safe_file(self.root,'COMPUTER-ARCHITECTURE-ATLAS')
        sys.path.insert(0,str(module))
        try:
            from computer_atlas.v04_bootstrap import bootstrap_certificate
            from computer_atlas.v04_gatelevel import ripple_adder_netlist
            src='SET 5\nADD 7\nSTORE 0\nXOR 3\nOUT 0\nHALT'
            proof=bootstrap_certificate(src)
            if proof['output_events']!=[[0,15]] or proof['syntax_assembler_processor_gate_checks']!='passed':
                raise AtlasError('AT8 reconstruction mismatch')
            return {'schema':'atlas.survival-bootstrap-selftest/1','result':'software_reconstruction_passed',
                    'source_sha256':proof['source_sha256'],'rom_sha256':proof['rom_sha256'],
                    'boot_image_sha256':proof['boot_image_sha256'],'receipt_sha256':proof['receipt_sha256'],
                    'nand_netlist_sha256':proof['NAND_netlist_sha256'],'output_events':proof['output_events'],
                    'not_demonstrated':['fabricated CPU','measured device timing','hardware firmware authentication','physical manufacturing acceptance']}
        finally:
            sys.path.remove(str(module))

    def manuals(self):
        items=[]
        for p in self.root.iterdir():
            if p.is_dir() and p.name.endswith('-ATLAS'):
                docs=p/'docs'
                if docs.is_dir():
                    f=sorted((x for x in docs.glob('*MANUAL*.md') if x.is_file()),key=lambda x:x.name)
                    if f:
                        items.append({'domain':p.name,'manuals':[str(x.relative_to(self.root)) for x in f][-4:]})
        return {'schema':'atlas.survival-manual-locator/1','items':sorted(items,key=lambda x:x['domain'])}

def main(argv=None):
    p=argparse.ArgumentParser(description='ATLAS FORGE offline survival reader; no network, no AI, no Bitwork router')
    p.add_argument('--root',type=Path,default=ROOT)
    sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('catalog');sub.add_parser('audit');sub.add_parser('gaps');sub.add_parser('challenge');sub.add_parser('manuals')
    q=sub.add_parser('search');q.add_argument('query');q.add_argument('--limit',type=int,default=12);q.add_argument('--node')
    q=sub.add_parser('record');q.add_argument('id')
    q=sub.add_parser('trace');q.add_argument('id');q.add_argument('--direction',default='upstream',choices=['upstream','downstream','both']);q.add_argument('--depth',type=int,default=2)
    args=p.parse_args(argv)
    try:
        atlas=Atlas(args.root)
        if args.command=='catalog':result=atlas.catalog()
        elif args.command=='audit':result=atlas.verify()
        elif args.command=='gaps':result=atlas.gaps()
        elif args.command=='challenge':result=atlas.challenge()
        elif args.command=='manuals':result=atlas.manuals()
        elif args.command=='search':result=atlas.search(args.query,args.limit,args.node)
        elif args.command=='record':result=atlas.record(args.id)
        else:result=atlas.trace(args.id,args.direction,args.depth)
        print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
        return 0
    except (AtlasError, OSError, KeyError, TypeError) as exc:
        print(json.dumps({'result':'FAIL_CLOSED','exception':type(exc).__name__,'message':str(exc)[:300]},sort_keys=True),file=sys.stderr)
        return 2
if __name__=='__main__':raise SystemExit(main())
