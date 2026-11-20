#!/usr/bin/env python3
"""Audit v0.4 fidelity to immutable v0.3 release, no historical deletions.

Usage: python tools/verify_history_v04.py --base-zip /path/v03.zip
      --target /path/extracted-v04 --output /separate/report.json
"""
from pathlib import Path
from hashlib import sha256
import argparse,json,zipfile,sys
V03_HASH='3e88286c8a2c68248cf331722007d76ad1979c09cddfacdd6089f39bd971f9dc'
ALLOWED_EXACT={'README.md','CURRENT_CHECKPOINT.json','common/registry.json','common/registry.lock.json','tools/check_collection.py'}
ALLOWED_PREFIX=('MATHEMATICS-PHYSICS-ATLAS/','common/nodes/mathematics-physics-atlas/','roadmaps/TECHNOLOGICAL_CONTINUITY_PRIORITY_v2.1_math_v03_active.json')

def hashfile(path):
 h=sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(4<<20),b''):h.update(b)
 return h.hexdigest()

def audit(base,target):
 if hashfile(base)!=V03_HASH:raise RuntimeError('wrong baseline archive SHA-256')
 with zipfile.ZipFile(base) as archive:
  base_root='ATLAS_COLLECTION_Mathematics_Physics_v0.3.0/'
  prev=json.loads(archive.read(base_root+'FILE_MANIFEST.json'))['files']
  base_queue=archive.read(base_root+'DOMAIN_QUEUE.json')
  base_build=archive.read(base_root+'BUILD_POLICY.json')
  original_record_strings=archive.read(base_root+'common/nodes/mathematics-physics-atlas/data/concepts.jsonl')
  names=('concepts','claims','equations','methods','datasets','reviews','sources')
  old_recs={}
  for name in names:
   blob=archive.read(base_root+f'common/nodes/mathematics-physics-atlas/data/{name}.jsonl')
   for raw in blob.splitlines():
    if raw.strip():
     entry=json.loads(raw);old_recs[entry['record_id']]=entry['revision']
  old_rel={}
  raw=archive.read(base_root+'common/nodes/mathematics-physics-atlas/data/relations.jsonl')
  for line in raw.splitlines():
   if line.strip():
    entry=json.loads(line);old_rel[entry['relation_id']]=entry['revision']
 old_deleted=[];changed=[];same=0
 for rel,expected in prev.items():
  p=target/rel
  if not p.is_file():old_deleted.append(rel);continue
  if hashfile(p)==expected:same+=1
  else:changed.append(rel)
 unauthorized=[rel for rel in changed if rel not in ALLOWED_EXACT and not any(rel.startswith(pre) for pre in ALLOWED_PREFIX)]
 new_record_map={}
 for name in names:
  for line in (target/f'common/nodes/mathematics-physics-atlas/data/{name}.jsonl').read_text().splitlines():
   if line.strip():
    entry=json.loads(line);new_record_map[entry['record_id']]=entry['revision']
 new_relation_map={}
 for line in (target/'common/nodes/mathematics-physics-atlas/data/relations.jsonl').read_text().splitlines():
  if line.strip():
   entry=json.loads(line);new_relation_map[entry['relation_id']]=entry['revision']
 altered_rec=[rid for rid,rev in old_recs.items() if new_record_map.get(rid)!=rev]
 altered_rel=[rid for rid,rev in old_rel.items() if new_relation_map.get(rid)!=rev]
 queue_ok=(target/'DOMAIN_QUEUE.json').read_bytes()==base_queue
 build_ok=(target/'BUILD_POLICY.json').read_bytes()==base_build
 snap=target/'history/math_physics_v0.3.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS'
 snap_ok=snap.is_dir()
 if snap_ok:
  snap_manifest=json.loads((snap/'FILE_MANIFEST.json').read_text())['files']
  snap_ok=all(hashfile(snap/path)==digest for path,digest in snap_manifest.items() if path.startswith('tests/'))
 result={
  'schema':'atlas.math-v04-historical-preservation/1','result':'passed' if not(old_deleted or unauthorized or altered_rec or altered_rel) and queue_ok and build_ok and snap_ok else 'failed',
  'prior_full_archive_sha256':V03_HASH,'prior_manifest_files':len(prev),
  'prior_files_byte_identical':same,'changed_in_allowed_scopes':len(changed),
  'changed_allowed_paths':changed,'prior_files_deleted':old_deleted,
  'unauthorized_prior_file_mutations':unauthorized,
  'prior_math_records_same_id_revision':len(old_recs)-len(altered_rec),'prior_math_relations_same_id_revision':len(old_rel)-len(altered_rel),
  'prior_math_record_revisions_altered':altered_rec,'prior_math_relation_revisions_altered':altered_rel,
  'original_30_domain_queue_byte_identical':queue_ok,
  'unchanged_BUILD_POLICY_including_router':build_ok,
  'original_v03_test_files_match_frozen_manifest':snap_ok,
  'historical_snapshot_note':'Snapshot exists in v04 for frozen test assertions; exact v03 full ZIP remains separate and is required baseline for incremental restore',
  'independent_scientific_review':False,'authenticated_original_publisher_transport_files':0}
 return result

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--base-zip',type=Path,required=True);p.add_argument('--target',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 result=audit(a.base_zip,a.target)
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='changed_allowed_paths'},indent=2))
 raise SystemExit(result['result']!='passed')
