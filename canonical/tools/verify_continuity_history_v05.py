#!/usr/bin/env python3
"""Audit the SAME original ATLAS FORGE predecessor v0.4 against v0.5 survival edition.

No prior node, scientific record, relation, original domain queue or historical
version may be mutated. Only root checkpoint/policy/readmes, runner, and new
survival tools/docs are permitted. File identity is NOT scientific truth.
"""
from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
import argparse,json
BASE='ATLAS_COLLECTION_Computer_Architecture_v0.4.0'
EXPECTED='3f4fcece03c4821bea59dbbc784f690aed6a2cd01a85f22f59f08aa529670bac'
ALLOWED={'FILE_MANIFEST.json','BUILD_POLICY.json','CURRENT_CHECKPOINT.json',
         'README.md','START_HERE.md','tools/check_collection.py'}
def digest(p):
 h=sha256()
 with Path(p).open('rb') as f:
  for part in iter(lambda:f.read(4<<20),b''):h.update(part)
 return h.hexdigest()
def run(base:Path,target:Path):
 if digest(base)!=EXPECTED:raise ValueError('wrong full predecessor v0.4')
 with ZipFile(base) as z:
  assert z.testzip() is None
  old=json.loads(z.read(BASE+'/FILE_MANIFEST.json'))['files']
  oldreg=z.read(BASE+'/common/registry.json')
  oldlock=z.read(BASE+'/common/registry.lock.json')
  oldqueue=z.read(BASE+'/DOMAIN_QUEUE.json')
 new=json.loads((target/'FILE_MANIFEST.json').read_text())['files']
 deleted=sorted(set(old)-set(new))
 changed=sorted(p for p in old if p in new and old[p]!=new[p])
 unauthorized=[p for p in changed if p not in ALLOWED]
 new_files=sorted(set(new)-set(old))
 # New files are additions to root tools/docs only; nothing infiltrates a node.
 unauthorized_new=[p for p in new_files if not(p.startswith('SURVIVAL/') or p.startswith('tools/'))]
 oldnodechanged=[p for p in changed if '/data/' in p or p.startswith('common/') or p.endswith('/atlas_manifest.json')]
 original_registry=(target/'common/registry.json').read_bytes()==oldreg and (target/'common/registry.lock.json').read_bytes()==oldlock
 original_queue=(target/'DOMAIN_QUEUE.json').read_bytes()==oldqueue
 files_hashes=[p for p,want in new.items() if digest(target/p)!=want]
 status='passed' if not(deleted or unauthorized or unauthorized_new or oldnodechanged or files_hashes) and original_registry and original_queue else 'failed'
 return {'schema':'atlas.original-federation-continuity-v05-preservation/1','result':status,
         'previous_full_archive_sha256':EXPECTED,'previous_files':len(old),'previous_byte_identical':len(old)-len(changed),
         'authorized_modified_existing_files':len(changed),'changed_existing_paths':changed,
         'new_file_count':len(new_files),'new_paths':new_files,'previous_files_deleted':deleted,
         'unauthorized_modified_paths':unauthorized,'unauthorized_new_paths':unauthorized_new,
         'old_node_manifests_and_data_changed':oldnodechanged,'original_registry_identical':original_registry,
         'original_30_domain_queue_identical':original_queue,'source_hash_errors':files_hashes,
         'all_fifteen_node_manifests_unchanged':original_registry,
         'scientific_peer_review_implied':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--base',required=True,type=Path)
 p.add_argument('--target',required=True,type=Path);p.add_argument('--out',required=True,type=Path)
 a=p.parse_args();report=run(a.base,a.target)
 a.out.parent.mkdir(exist_ok=True,parents=True)
 a.out.write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k not in ('new_paths','changed_existing_paths')},indent=2))
 if report['result']!='passed':raise SystemExit(1)
