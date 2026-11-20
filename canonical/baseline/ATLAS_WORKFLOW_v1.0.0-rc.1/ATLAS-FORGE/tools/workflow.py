#!/usr/bin/env python3
"""Run from a source checkout; no installation or host configuration needed."""
from pathlib import Path
import argparse
import json
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from atlas_forge.workflow import gate_report, authorize_next_domain, subject_digest
from atlas_forge.common import AtlasStore, ContractError

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('action',choices=['status','conform','subject','advance','skills-check'])
p.add_argument('--node',default='causal-atlas')
a=p.parse_args()
try:
    if a.action=='status':r=gate_report(ROOT);code=0
    elif a.action=='subject':r={'subject_sha256':subject_digest(ROOT)};code=0
    elif a.action=='advance':r=authorize_next_domain(ROOT,a.node);code=0
    elif a.action=='conform':
        s=AtlasStore();d=s.discover();r={'valid':True,'records':d['records'],'relations':d['relations'],'nodes':[n['node_id'] for n in d['nodes']]};code=0
    else:
        errors=[];names=[]
        for skill in sorted((ROOT/'.agents/skills').glob('*/SKILL.md')):
            text=skill.read_text(encoding='utf-8');name=skill.parent.name;names.append(name)
            if not text.startswith('---\n') or f'name: {name}\n' not in text.split('---',2)[1]:errors.append(f'{name}: missing/mismatched name')
            if 'description:' not in text.split('---',2)[1]:errors.append(f'{name}: missing description')
            if len(text)>16000:errors.append(f'{name}: exceeds local skill size limit')
        r={'valid':not errors and len(names)==5,'skills':names,'errors':errors,'host_installation_verified':False};code=0 if r['valid'] else 2
    print(json.dumps(r,indent=2));sys.exit(code)
except (ValueError,OSError,KeyError,TypeError) as exc:
    print(json.dumps({'status':'blocked','error':str(exc)},indent=2));sys.exit(2)
