#!/usr/bin/env python3
"""ATLAS original federation Computer Architecture 0.3 preservation verifier.

Uses exact v0.2 predecessor full ZIP, prevents old file deletion or historical
record rewrite, and verifies that every other Atlas node remains identical.
"""
from __future__ import annotations
from argparse import ArgumentParser
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile
import json
NODE='computer-architecture-digital-hardware-atlas'
SUB='COMPUTER-ARCHITECTURE-ATLAS'
BASE='ATLAS_COLLECTION_Computer_Architecture_v0.2.0'
OLD_SHA='ed06f0d2d22ebb9c6f5016e94ccff285b90eb4139ecc2dfc2cc9a324ce7674f3'
ALLOWED={'README.md','START_HERE.md','CURRENT_CHECKPOINT.json','BUILD_POLICY.json',
  'common/registry.json','common/registry.lock.json','tools/check_collection.py'}

def fh(path):
 h=sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(4<<20),b''):h.update(b)
 return h.hexdigest()

def audit(base:Path,target:Path):
 if fh(base)!=OLD_SHA:raise ValueError('wrong predecessor full ZIP SHA-256')
 with ZipFile(base) as z:
  if z.testzip() is not None:raise ValueError('corrupt previous release ZIP')
  prior=json.loads(z.read(BASE+'/FILE_MANIFEST.json'))['files']
  old_registry=json.loads(z.read(BASE+'/common/registry.json'))
  absent=[];changed=[];unal=[];equal=0
  for rel,digest in prior.items():
   p=target/rel
   if not p.is_file():absent.append(rel)
   elif fh(p)==digest:equal+=1
   else:
    changed.append(rel)
    if rel not in ALLOWED and not rel.startswith(SUB+'/') and not rel.startswith(f'common/nodes/{NODE}/'):
     unal.append(rel)
  old_tests=[]
  for m in z.namelist():
   prefix=BASE+'/'+SUB+'/tests/'
   if m.startswith(prefix) and m.endswith('.py'):
    rel=m[len(BASE+'/'):]
    old=z.read(m)
    if (target/rel).read_bytes()!=old:old_tests.append(rel)
    frozen=target/'history/computer_architecture_v0.2.0_test_snapshot'/rel
    if not frozen.is_file() or frozen.read_bytes()!=old:old_tests.append('frozen:'+rel)
  prefixes=[]
  for rel in prior:
   if (rel.startswith(SUB+'/data/') or rel.startswith(SUB+f'/computer_atlas/resources/common/nodes/{NODE}/data/')
       or rel.startswith(f'common/nodes/{NODE}/data/')) and rel.endswith('.jsonl'):
    if not (target/rel).read_bytes().startswith(z.read(BASE+'/'+rel)):
     prefixes.append(rel)
  old_nodes={n['node_id']:n for n in old_registry['nodes']}
  current_nodes={n['node_id']:n for n in json.loads((target/'common/registry.json').read_text())['nodes']}
  other_unchanged=all(current_nodes.get(k)==old_nodes[k] for k in old_nodes if k!=NODE)
  queue_same=fh(target/'DOMAIN_QUEUE.json')==prior['DOMAIN_QUEUE.json']
  policy=json.loads((target/'BUILD_POLICY.json').read_text())
  route_clean=not(policy.get('Bitwork_router_modified') or policy.get('Bitwork_router_changes'))
  new_files={p.relative_to(target).as_posix() for p in target.rglob('*') if p.is_file() and p!=target/'FILE_MANIFEST.json' and not any(x=='__pycache__' or x.endswith('.egg-info') for x in p.relative_to(target).parts)}-set(prior)
  okay=(not(absent or unal or old_tests or prefixes) and other_unchanged and queue_same and route_clean and len(current_nodes)==15)
  return {'schema':'atlas.computer-v03-historical-preservation/1','result':'passed' if okay else 'failed',
      'predecessor_full_zip_sha256':OLD_SHA,'prior_file_count':len(prior),
      'prior_files_identical':equal,'authorized_old_file_changes':len(changed),
      'changed_old_paths':sorted(changed),'prior_files_deleted':len(absent),
      'unauthorized_changed_paths':sorted(unal),'old_computer_tests_modified':sorted(old_tests),
      'old_jsonl_prefixes_modified':sorted(prefixes), 'new_files':len(new_files),
      'unchanged_other_14_node_registry_entries':other_unchanged,
      'original_30_domain_queue_unchanged':queue_same,'Bitwork_router_modified':not route_clean,
      'scope':'byte and structural integrity only, not source authenticity, physical calibration or expert review'}

def main():
 p=ArgumentParser(description=__doc__)
 p.add_argument('--base',type=Path,required=True)
 p.add_argument('--target',type=Path,required=True)
 p.add_argument('--out',type=Path,required=True)
 a=p.parse_args();r=audit(a.base,a.target)
 a.out.parent.mkdir(parents=True,exist_ok=True)
 if a.out.exists():raise SystemExit('refuse overwrite receipt')
 a.out.write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps({k:v for k,v in r.items() if k!='changed_old_paths'},indent=2))
 if r['result']!='passed':raise SystemExit(1)
if __name__=='__main__':main()
