#!/usr/bin/env python3
"""Audit original 15-node Computer v0.5 federation against additive Bioelectric v0.1.

Verifies exact archived predecessor file hashes, old node entries, prior
record bytes and unmodified historical roadmap. NOT a scientific review.
"""
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile
import argparse,json
BASE_SHA='ea4b1f70eeaabeec0ea5b553c27bf4b3e094efc1280b1067c3c4754247b3bf8e'
BASE_ROOT='ATLAS_COLLECTION_Computer_Architecture_v0.5.0'
NODE='bioelectric-atlas'
ALLOWED_OLD={'README.md','BUILD_POLICY.json','CURRENT_CHECKPOINT.json',
             'common/registry.json','common/registry.lock.json','tools/check_collection.py'}
def digest(p):
 h=sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(4<<20),b''):h.update(b)
 return h.hexdigest()

def audit(base:Path,target:Path):
 if digest(base)!=BASE_SHA:raise ValueError('wrong full predecessor ZIP digest')
 with ZipFile(base) as z:
  if z.testzip() is not None:raise ValueError('corrupted source archive')
  prior=json.loads(z.read(BASE_ROOT+'/FILE_MANIFEST.json'))['files']
  oldreg=json.loads(z.read(BASE_ROOT+'/common/registry.json'))
  queue=z.read(BASE_ROOT+'/DOMAIN_QUEUE.json')
  previous_corpus_paths=[p for p in prior if p.startswith('common/nodes/') and p.endswith('.jsonl')]
  missing=[];modified=[];forbidden=[];same=0
  for rel,want in prior.items():
   p=target/rel
   if not p.is_file():missing.append(rel)
   elif digest(p)==want:same+=1
   else:
    modified.append(rel)
    if rel not in ALLOWED_OLD:forbidden.append(rel)
  oldnod={x['node_id']:x for x in oldreg['nodes']}
  current=json.loads((target/'common/registry.json').read_text())
  currentnod={x['node_id']:x for x in current['nodes']}
  nodes_correct=(len(oldnod)==15 and len(currentnod)==16 and set(currentnod)==set(oldnod)|{NODE}
      and all(currentnod.get(n)==x for n,x in oldnod.items()))
  queue_equal=(target/'DOMAIN_QUEUE.json').read_bytes()==queue
  old_node_files_protected=all(rel not in modified and rel not in missing for rel in previous_corpus_paths)
  count_files=sum(1 for f in target.rglob('*') if f.is_file() and not any(x=='__pycache__' or x.endswith('.egg-info') for x in f.relative_to(target).parts))
  result='passed' if not(missing or forbidden) and nodes_correct and queue_equal and old_node_files_protected else 'failed'
  return {'schema':'atlas.original-federation-bioelectric-preservation/1','result':result,
      'predecessor_full_sha256':BASE_SHA,'prior_file_count':len(prior),'prior_byte_identical':same,
      'authorized_modified_old_files':len(modified),'authorized_modified_paths':sorted(modified),
      'deleted_old_files':len(missing),'forbidden_old_changes':forbidden,
      'previous_science_jsonl_files_untouched':len(previous_corpus_paths),
      'all_other_15_node_registry_entries_identical':nodes_correct,
      'original_30_domain_queue_byte_identical':queue_equal,
      'previous_science_jsonl_byte_identical':old_node_files_protected,
      'current_source_file_count_plus_manifests':count_files,
      'new_nodes':1,'new_node':NODE,
      'scientific_or_medical_device_validity':'not_established_by_file_hashes'}

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--base-archive',type=Path,required=True)
 p.add_argument('--target',type=Path,required=True)
 p.add_argument('--out',type=Path,required=True)
 a=p.parse_args();r=audit(a.base_archive,a.target)
 a.out.parent.mkdir(parents=True,exist_ok=True)
 if a.out.exists():raise SystemExit('refuse overwrite preservation receipt')
 a.out.write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps(r,indent=2))
 if r['result']!='passed':raise SystemExit(1)
