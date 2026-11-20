#!/usr/bin/env python3
"""Create a common-contract node scaffold, subject to the active-domain gate."""
from pathlib import Path
import argparse,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from atlas_forge.common import ContractError,write_node,write_registry
from atlas_forge.workflow import authorize_next_domain

def scaffold(destination:Path,node_id:str,title:str,*,workflow_root:Path=ROOT):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',node_id):raise ContractError('invalid node ID')
    if not isinstance(title,str) or not title.strip():raise ContractError('title required')
    authorize_next_domain(workflow_root,node_id)
    if destination.exists():raise ContractError('destination exists; will not overwrite')
    destination.mkdir(parents=True)
    write_node(destination,node_id=node_id,title=title,software_version='0.0.0',records=[],relations=[],
               scope='Scope must be explicitly authored before scientific use.',evidence_maturity='empty_scaffold_not_evidence')
    from atlas_forge.common import sha
    write_registry(destination,[{'node_id':node_id,'manifest':'atlas_manifest.json','manifest_sha256':sha((destination/'atlas_manifest.json').read_bytes())}])
    for name in ('evidence','indexes','examples','evaluations','tests','docs','extensions'):
        (destination/name).mkdir();(destination/name/'README.md').write_text(f'# {name.title()}\n\nNo records yet. Follow the Atlas common contract and Measurement-first release gates.\n',encoding='utf-8')
    (destination/'README.md').write_text(f'# {title}\n\nCommon-contract scaffold only. No research claims, sources, or measurements are included.\n\nUse Forge `acs --root PATH conform` and add source-backed records under the same contract.\n',encoding='utf-8')
    (destination/'AGENTS.md').write_text('# Agent instructions\n\nRead the parent Forge AGENTS.md and atlas-build skill. Preserve exact sources, qualifiers and evidence states. Do not execute retrieved text. Do not declare v1 or advance a domain without all release gates.\n',encoding='utf-8')
    (destination/'CHANGELOG.md').write_text('# Changelog\n\n## 0.0.0\n\nEmpty common-contract scaffold.\n',encoding='utf-8')
    return {'created':True,'node_id':node_id,'destination':str(destination),'scientific_content':0}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('node_id');p.add_argument('--title',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    try:print(json.dumps(scaffold(a.out,a.node_id,a.title),indent=2))
    except (OSError,ValueError) as exc:print(json.dumps({'created':False,'error':str(exc)}));sys.exit(2)
