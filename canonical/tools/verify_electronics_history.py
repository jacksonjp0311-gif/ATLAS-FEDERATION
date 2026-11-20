#!/usr/bin/env python3
"""Verify the original 12-node federation is retained by Electronics v0.1.

Compares original publisher-independent file hashes; does not constitute
scientific acceptance or cryptographic signatures.
"""
import argparse,hashlib,json
from pathlib import Path
from zipfile import ZipFile
ALLOWED={'BUILD_POLICY.json','CURRENT_CHECKPOINT.json','README.md','START_HERE.md',
         'common/registry.json','common/registry.lock.json','tools/check_collection.py'}
BASE_SHA='2c967aef70f6db6b6e5bee39aa094c0cfc63aba769b1af7d31fb8a8eeda3eb31'

def sha(data):return hashlib.sha256(data).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--base-zip',type=Path,required=True)
 ap.add_argument('--target',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--out',type=Path,required=True)
 args=ap.parse_args()
 base=args.base_zip
 with base.open('rb') as f:
  h=hashlib.sha256()
  for c in iter(lambda:f.read(4<<20),b''):h.update(c)
 if h.hexdigest()!=BASE_SHA:raise SystemExit('Wrong predecessor archive SHA-256')
 with ZipFile(base) as z:
  roots={x.filename.split('/')[0] for x in z.infolist()}
  if roots!={'ATLAS_COLLECTION_Mathematics_Physics_v1.0.0-rc.1'}:raise SystemExit('Unexpected base ZIP root')
  original=json.loads(z.read('ATLAS_COLLECTION_Mathematics_Physics_v1.0.0-rc.1/FILE_MANIFEST.json'))['files']
 target=args.target.resolve()
 missing=[];changed=[];unchanged=0
 for rel,expected in sorted(original.items()):
  p=target/rel
  if not p.is_file():missing.append(rel);continue
  if sha(p.read_bytes())!=expected:changed.append(rel)
  else:unchanged+=1
 if missing or set(changed)-ALLOWED:
  raise SystemExit(f'Historical preservation failed missing={missing[:8]} unauthorized={sorted(set(changed)-ALLOWED)[:8]}')
 original_queue_sha=original['DOMAIN_QUEUE.json']
 if sha((target/'DOMAIN_QUEUE.json').read_bytes())!=original_queue_sha:raise SystemExit('Original 30 domains changed')
 policy=json.loads((target/'BUILD_POLICY.json').read_text())
 if policy.get('Bitwork_router_changes') or policy.get('Bitwork_router_modified') or not policy.get('canonical_original_thirty_unchanged'):
  raise SystemExit('Architectural policy changed')
 registry=json.loads((target/'common/registry.json').read_text())
 ids={x['node_id'] for x in registry['nodes']}
 if len(ids)!=13 or 'electronics-semiconductors-atlas' not in ids:raise SystemExit('Expected thirteen-node expansion missing')
 report={'schema':'atlas.electronics-historical-preservation/1','result':'passed','predecessor_full_zip_sha256':BASE_SHA,
  'prior_files':len(original),'prior_unchanged_files':unchanged,'prior_authorized_changed':len(changed),
  'prior_changed_paths':changed,'prior_deleted_files':len(missing),'unauthorized_changes':[],
  'original_30_queue_sha256':original_queue_sha,'new_node':'electronics-semiconductors-atlas',
  'prior_node_jsonl_content':'all byte-identical',
  'Bitwork_router_modified':False,'scope':'file-byte and immutable-revision preservation, NOT external scientific review'}
 args.out.parent.mkdir(parents=True,exist_ok=True)
 args.out.write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
