#!/usr/bin/env python3
"""v0.3 historical preservation: compare a verified v0.2 archive with a new v0.3 tree.

Checks file SHA256, exact record/relation revision continuity, old tests preserved
in frozen snapshots, canonical original domains and prohibited router paths.
Hashing establishes byte continuity, not source authenticity or scientific truth.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from zipfile import ZipFile

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--base',type=Path,required=True,help='SHA-verified full v0.2 archive')
p.add_argument('--target',type=Path,required=True,help='unpacked v0.3 source tree')
p.add_argument('--output',type=Path,required=True)
a=p.parse_args()
base_expected='c62d10c0b18d22a7201ef226fe7dc6248bc855e87ed176aa1b5200309ee29d88'
def sha_file(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(4<<20),b''):h.update(b)
 return h.hexdigest()
def same_prefix(expected,current):
 return current.startswith(expected)
assert sha_file(a.base)==base_expected,'base SHA256 mismatch'
with ZipFile(a.base) as z:
 prefix='ATLAS_COLLECTION_Mathematics_Physics_v0.2.0/'
 old_manifest=json.loads(z.read(prefix+'FILE_MANIFEST.json'))['files']
 added=sorted(set(p.relative_to(a.target).as_posix() for p in a.target.rglob('*') if p.is_file())-set(old_manifest)-{'FILE_MANIFEST.json'})
 changed=[];identical=0;missing=[];old_hash_errors=[];unauthorized=[]
 authorized=('MATHEMATICS-PHYSICS-ATLAS/','common/nodes/mathematics-physics-atlas/','roadmaps/')
 allowed_exact={'BUILD_POLICY.json','CURRENT_CHECKPOINT.json','README.md','START_HERE.md','common/registry.json','common/registry.lock.json','tools/check_collection.py'}
 for path,want in old_manifest.items():
  item=a.target/path
  if not item.is_file():missing.append(path);continue
  newhash=sha_file(item)
  if newhash==want:identical+=1;continue
  changed.append(path)
  if not(path in allowed_exact or path.startswith(authorized)):
   unauthorized.append(path)
 # Old historical invariants on previous 12-node corpus:
 frompath=a.target/'history/math_physics_v0.2.0_test_snapshot'
 frozen_compare=[]
 for rel in ('tests/test_integrity.py','tests/test_v02_models.py','tests/test_models.py'):
  source=prefix+'MATHEMATICS-PHYSICS-ATLAS/'+rel
  restored=(frompath/'MATHEMATICS-PHYSICS-ATLAS'/rel)
  if hashlib.sha256(z.read(source)).hexdigest()!=sha_file(restored):frozen_compare.append(rel)
 # All previous math records, sources and local/full relations must be literal prefix lines.
 prefix_errors=[]
 for key in ('concepts','claims','equations','methods','datasets','reviews','sources','relations'):
  for loc in ('MATHEMATICS-PHYSICS-ATLAS/data/','common/nodes/mathematics-physics-atlas/data/'):
   rel=loc+key+'.jsonl'
   if not same_prefix(z.read(prefix+rel),(a.target/rel).read_bytes()):prefix_errors.append(rel)
 # Decode original record and relation identifiers & compare revisioned objects in the current federation.
 original={};current={}
 for prefixnode in ['common/nodes/'+p+'/' for p in ['agent-atlas','causal-atlas','chemistry-atlas','computation-atlas','control-atlas','cymatics-atlas','energy-atlas','language-atlas','materials-atlas','mathematics-physics-atlas','measurement-atlas','signal-atlas']]:
  for category in ('concepts','claims','equations','methods','datasets','reviews','sources','relations'):
   path=prefixnode+'data/'+category+'.jsonl'
   raw=z.read(prefix+path)
   live=(a.target/path).read_bytes()
   for row in raw.splitlines():
    if not row:continue
    rec=json.loads(row)
    k='relation_id' if category=='relations' else 'record_id'
    oldid=(category,rec[k]);original[oldid]=rec['revision']
   for row in live.splitlines():
    if not row:continue
    rec=json.loads(row);k='relation_id' if category=='relations' else 'record_id'
    current[(category,rec[k])]=rec['revision']
 historic_bad=[str(key) for key,value in original.items() if current.get(key)!=value]
 # Canonical thirty queue retained byte-for-byte via root manifest comparison.
 specific_original_domain_files=[x for x in old_manifest if x.startswith('roadmaps/') and ('ORIGINAL_30' in x or '30_DOMAIN' in x)]
 domain_queue_unchanged=all(x not in changed for x in specific_original_domain_files)
 result={'schema':'atlas.math-v03-independent-preservation-audit/1',
         'status':'passed' if not(missing or unauthorized or frozen_compare or prefix_errors or historic_bad or not domain_queue_unchanged) else 'failed',
         'base_archive_sha256':base_expected,'old_manifest_files':len(old_manifest),
         'old_files_identical_sha256':identical,'old_files_changed_authorized':len(changed),
         'old_files_deleted':len(missing),'new_files_not_in_predecessor':len(added),
         'changed_paths':changed,'unauthorized_changed':unauthorized,'missing_paths':missing,
         'old_frozen_test_sha_mismatches':frozen_compare,'old_math_prefix_failures':prefix_errors,
         'old_record_and_relation_revisions_preserved':len(original),
         'old_revision_mismatches':historic_bad[:15],
         'prior_original_30_queue_unchanged':domain_queue_unchanged,
         'limits':['SHA256 continuity is not authentication of any publisher original',
                   'Changed paths must be reviewed for science content; this is file and revision checking only']}
 a.output.parent.mkdir(exist_ok=True,parents=True)
 a.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ('changed_paths','old_revision_mismatches')},indent=2))
 raise SystemExit(result['status']!='passed')
