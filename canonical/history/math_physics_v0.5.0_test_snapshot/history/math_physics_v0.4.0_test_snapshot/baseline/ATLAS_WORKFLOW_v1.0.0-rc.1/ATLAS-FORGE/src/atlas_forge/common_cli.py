"""Portable command interface to the common Atlas runtime."""
from __future__ import annotations
import argparse
from pathlib import Path
import json
from .common import AtlasStore, ContractError, canonical, strict_json
from .routing import route_request


def main(argv=None):
    p=argparse.ArgumentParser(prog='atlas-forge acs',description=__doc__)
    p.add_argument('--root',type=Path,help='Explicit common registry root, not a remote URL')
    sub=p.add_subparsers(dest='action',required=True)
    for name in ('discover','conform','export'):sub.add_parser(name)
    for name in ('search','context','route-request'):
        c=sub.add_parser(name);c.add_argument('question');c.add_argument('--node',action='append',dest='node_ids')
        if name in ('search','context'):c.add_argument('--limit',type=int,default=8)
        if name=='context':
            c.add_argument('--render',action='store_true',help='Print only the budgeted model-facing context text');c.add_argument('--max-bytes',type=int,default=32768);c.add_argument('--route-receipt',type=Path)
    for name in ('fetch','neighbors'):
        c=sub.add_parser(name);c.add_argument('record_id');c.add_argument('revision')
        if name=='neighbors':c.add_argument('--depth',type=int,default=1);c.add_argument('--max-edges',type=int,default=30)
    for name in ('validate-context','changes-since'):
        c=sub.add_parser(name);c.add_argument('packet',type=Path)
    args=p.parse_args(argv)
    try:
        store=AtlasStore(args.root);a=args.action
        if a in ('discover','conform'):
            obj=store.discover()
            if a=='conform':obj={'valid':True,'record_count':obj['records'],'relation_count':obj['relations'],'nodes':[n['node_id'] for n in obj['nodes']],
                                 'scope':'common contract structure, hashes, references; not scientific verification'}
        elif a=='export':
            for r in store.export():print(canonical(r).decode())
            return 0
        elif a=='search':obj=store.search(args.question,node_ids=args.node_ids,limit=args.limit)
        elif a=='context':obj=store.assemble_context(args.question,node_ids=args.node_ids,limit=args.limit,max_context_bytes=args.max_bytes,
                                                   route_receipt=strict_json(args.route_receipt.read_bytes()) if args.route_receipt else None)
        elif a=='route-request':obj=route_request(store,args.question,args.node_ids)
        elif a=='fetch':obj=store.fetch(args.record_id,args.revision)
        elif a=='neighbors':obj=store.neighbors(args.record_id,args.revision,depth=args.depth,max_edges=args.max_edges)
        elif a=='validate-context':obj=store.validate_context(strict_json(args.packet.read_bytes()))
        elif a=='changes-since':obj=store.changes_since(strict_json(args.packet.read_bytes()))
        if a=='context' and args.render:
            print(obj['context_text']);return 0
        print(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False));return 0 if obj.get('valid',True) else 2
    except (KeyError,TypeError,ValueError,OSError) as exc:
        print(json.dumps({'status':'failed','error':str(exc)},ensure_ascii=False));return 2

if __name__=='__main__':raise SystemExit(main())
