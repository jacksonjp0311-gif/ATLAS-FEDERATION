#!/usr/bin/env python3
"""Exact preservation verifier against the published Manufacturing v0.2 reconciled federation.

This checks file identity, graph registry and original queue, not scientific truth.
"""
import argparse,hashlib,json
from pathlib import Path
from zipfile import ZipFile
OLD_SHA='018dda14277a1980748c2a4fbaa95d73dc0b3a7680d4008ef754db796a56f894'
OLD_ROOT='ATLAS_COLLECTION_Manufacturing_v0.2.0_MERGED'
NODE='computer-architecture-digital-hardware-atlas'
ALLOWED={'README.md','BUILD_POLICY.json','CURRENT_CHECKPOINT.json','common/registry.json','common/registry.lock.json','tools/check_collection.py'}
def sha_file(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(4<<20),b''):h.update(x)
 return h.hexdigest()
def main(base,target,out):
 if sha_file(base)!=OLD_SHA:raise ValueError('not verified Manufacturing v0.2 predecessor')
 with ZipFile(base) as z:
  if z.testzip():raise ValueError('predecessor member CRC invalid')
  old=json.loads(z.read(f'{OLD_ROOT}/FILE_MANIFEST.json'))['files']
  reg=json.loads(z.read(f'{OLD_ROOT}/common/registry.json'))
  oldqueue=z.read(f'{OLD_ROOT}/DOMAIN_QUEUE.json')
 now={x['node_id']:x for x in json.loads((target/'common/registry.json').read_text())['nodes']}
 old_nodes={x['node_id']:x for x in reg['nodes']}
 if len(now)!=15 or set(now)!=set(old_nodes)|{NODE}:raise ValueError('not exactly one new computer node')
 if any(now[n]!=old_nodes[n] for n in old_nodes):raise ValueError('historical node registry entry changed')
 if (target/'DOMAIN_QUEUE.json').read_bytes()!=oldqueue:raise ValueError('original thirty-domain queue modified')
 unchanged=0;changed=[];deleted=[];forbidden=[]
 for rel,want in old.items():
  f=target/rel
  if not f.is_file():deleted.append(rel);continue
  if sha_file(f)==want:unchanged+=1
  else:
   changed.append(rel)
   if rel not in ALLOWED:forbidden.append(rel)
 if deleted or forbidden:raise ValueError('old file changed or deleted '+repr((deleted[:8],forbidden[:8])))
 root_legacy=['common/nodes/'+n for n in old_nodes]
 allfiles={f.relative_to(target).as_posix() for f in target.rglob('*') if f.is_file() and f.name!='FILE_MANIFEST.json' and not any(x in ('__pycache__','.git','build','output') or x.endswith('.egg-info') for x in f.relative_to(target).parts)}
 added=len(allfiles-set(old))
 result={'schema':'atlas.computer-v01-preservation/1','result':'passed',
  'predecessor_full_archive_sha256':OLD_SHA,'old_file_count':len(old),
  'old_unchanged':unchanged,'old_authorized_changes':len(changed),'changed_paths':changed,
  'old_deleted':0,'old_forbidden_changes':[], 'new_source_files_before_manifest':added,
  'all_fourteen_old_node_registry_entries_unchanged':True,
  'all_previous_exact_revision_bytes_preserved':True,'original_30_domain_queue_unchanged':True,
  'bitwork_router_untouched':True,'physical_evidence_review_not_performed':True}
 out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='changed_paths'},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--base',type=Path,required=True);p.add_argument('--target',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
 a=p.parse_args();main(a.base,a.target,a.output)
