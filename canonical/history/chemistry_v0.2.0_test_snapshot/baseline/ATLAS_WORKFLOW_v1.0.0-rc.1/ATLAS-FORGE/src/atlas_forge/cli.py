"""Atlas scaffolding and read-only reference federation."""
from __future__ import annotations
import argparse
import sys
import json
from pathlib import Path
from .core import rank_domains, init_atlas, validate, query
from .federation import Federation

def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == 'acs':
        from .common_cli import main as common_main
        return common_main(argv[1:])
    ap = argparse.ArgumentParser(prog='atlas-forge', description='Build Atlases and query independent reference nodes')
    sub = ap.add_subparsers(dest='command', required=True)
    p=sub.add_parser('rank',help='Show proposed domains, not installed nodes');p.add_argument('--json',action='store_true')
    p=sub.add_parser('init',help='Create an unvalidated Atlas scaffold');p.add_argument('domain');p.add_argument('--out',default='output')
    p=sub.add_parser('validate',help='Validate a generated Atlas');p.add_argument('path')
    p=sub.add_parser('query',help='Legacy single-Atlas lexical query');p.add_argument('path');p.add_argument('question');p.add_argument('--limit',type=int,default=5)
    for name,helptext in [('nodes','Discover bundled nodes and snapshot state'),('verify-nodes','Verify registry and every raw node snapshot'),('search','Search enabled nodes without running upstream software'),('export-nodes','Export source-linked records as JSONL'),('serve','Open a read-only loopback node portal and API')]:
        p=sub.add_parser(name,help=helptext);p.add_argument('--registry-root',help='Explicit alternate local federation directory')
        if name in {'search','export-nodes'}:
            p.add_argument('--node',action='append',dest='node_ids',help='Restrict to this node; repeat for several nodes')
            p.add_argument('--include-starters',action='store_true')
        if name=='search':p.add_argument('question');p.add_argument('--per-node',type=int,default=5)
        if name=='export-nodes':p.add_argument('--out',required=True,help='New file; refuses to overwrite')
        if name=='serve':p.add_argument('--port',type=int,default=8766)
    a=ap.parse_args(argv)
    try:
        if a.command=='rank':
            domains=rank_domains()
            if a.json: print(json.dumps(domains,indent=2))
            else:
                for d in domains: print(f"{d['rank']:>2}  {d['title']:<23} {d['initial_scope']}")
            return 0
        if a.command=='init':print(init_atlas(a.domain,a.out));return 0
        if a.command in {'validate','query'}:
            result=validate(a.path) if a.command=='validate' else query(a.path,a.question,limit=max(1,a.limit))
            code=2 if (a.command=='validate' and not result['valid']) or result.get('status')=='invalid_atlas' else 0
        else:
            fed=Federation(a.registry_root)
            if a.command in {'nodes','verify-nodes'}:
                result=fed.discover();code=0 if result['valid'] else 2
            elif a.command=='search':
                result=fed.search(a.question,node_ids=a.node_ids,include_starters=a.include_starters,per_node=a.per_node)
                code=2 if result['errors'] else 0
            elif a.command=='export-nodes':
                records=fed.export(a.node_ids,include_starters=a.include_starters)
                out=Path(a.out)
                with out.open('x',encoding='utf-8',newline='\n') as f:
                    for r in records:f.write(json.dumps(r,sort_keys=True,ensure_ascii=False)+'\n')
                result={'written':str(out),'record_count':len(records),'contains_verified_answer':False};code=0
            elif a.command=='serve':
                from .server import serve
                serve(fed,a.port);return 0
        print(json.dumps(result,indent=2,ensure_ascii=False));return code
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print(json.dumps({'error':str(exc),'status':'failed'},ensure_ascii=False));return 2
