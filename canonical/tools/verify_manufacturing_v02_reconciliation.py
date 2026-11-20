#!/usr/bin/env python3
"""Verify Manufacturing v0.2 MERGES two verified branches of one ATLAS FORGE.

A) Original Electronics v1.0.0-rc.1 13-node mainline (latest)
B) Manufacturing v0.1.0 14-node sibling from older Electronics v0.4.0
This verifier compares exact bytes; it does not certify scientific claims,
physical device/machine quality, original source identity, or expert review.
"""
import argparse,hashlib,json
from pathlib import Path
from zipfile import ZipFile
MAIN_SHA='2b24bd5a3fbb6e9b51887ce2bea68dd0b2a0b0c728521b4ac5b483d457d6ebb8'
SIBLING_SHA='eefab1265ec2262ce6e1a2fa5a8ca9fee2735e2e14ada30e2e783f406283bd97'
MAIN_ROOT='ATLAS_COLLECTION_Electronics_Semiconductors_v1.0.0-rc.1'
SIBLING_ROOT='ATLAS_COLLECTION_Manufacturing_v0.1.0'
NODE='manufacturing-atlas'
ALLOWED_ROOT={'BUILD_POLICY.json','CURRENT_CHECKPOINT.json','README.md',
              'common/registry.json','common/registry.lock.json','tools/check_collection.py'}

def sh(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(4<<20),b''):h.update(b)
 return h.hexdigest()

def verify(base,sibling,target):
 if sh(base)!=MAIN_SHA:raise ValueError('mainline predecessor full archive sha mismatch')
 if sh(sibling)!=SIBLING_SHA:raise ValueError('Manufacturing sibling archive sha mismatch')
 with ZipFile(base) as z,ZipFile(sibling) as sib:
  if z.testzip() is not None or sib.testzip() is not None:raise ValueError('damaged historical ZIP')
  old_files=json.loads(z.read(MAIN_ROOT+'/FILE_MANIFEST.json'))['files']
  oldreg=json.loads(z.read(MAIN_ROOT+'/common/registry.json'))
  newreg=json.loads((target/'common/registry.json').read_text())
  if len(oldreg['nodes'])!=13 or len(newreg['nodes'])!=14:raise ValueError('wrong federation node count')
  older={x['node_id']:x for x in oldreg['nodes']}
  current={x['node_id']:x for x in newreg['nodes']}
  if not all(current.get(n)==v for n,v in older.items()):raise ValueError('older 13 node manifests changed')
  if NODE not in current:raise ValueError('Manufacturing node missing')
  changed=[];deleted=[];unchanged=0
  for rel,sha in old_files.items():
   file=target/rel
   if not file.is_file():deleted.append(rel);continue
   if sh(file)==sha:unchanged+=1
   else:changed.append(rel)
  unauthorized=sorted(set(changed)-ALLOWED_ROOT)
  if unauthorized or deleted:raise ValueError('mainline altered: '+repr((unauthorized[:5],deleted[:5])))
  siblingfiles=json.loads(sib.read(SIBLING_ROOT+'/MANUFACTURING-ATLAS/FILE_MANIFEST.json'))['files']
  original_mdata={}
  for name in ('concepts','claims','equations','methods','sources','datasets','reviews','relations'):
   old=sib.read(SIBLING_ROOT+f'/MANUFACTURING-ATLAS/data/{name}.jsonl')
   now=(target/f'MANUFACTURING-ATLAS/data/{name}.jsonl').read_bytes()
   if not now.startswith(old):raise ValueError('manufacturing old record/relation prefix modified '+name)
   original_mdata[name]=len(old.splitlines())
  oldfull=sib.read(SIBLING_ROOT+f'/common/nodes/{NODE}/data/relations.jsonl')
  currentfull=(target/f'common/nodes/{NODE}/data/relations.jsonl').read_bytes()
  if not currentfull.startswith(oldfull):raise ValueError('manufacturing old cross-domain relations changed')
  # Each old manufacturing chapter, original model and historical test unchanged.
  protected=[f for f in siblingfiles if f.startswith(('docs/chapters/','tests/')) or f=='manufacturing_atlas/models.py']
  for rel in protected:
   oldraw=sib.read(SIBLING_ROOT+'/MANUFACTURING-ATLAS/'+rel)
   if (target/'MANUFACTURING-ATLAS'/rel).read_bytes()!=oldraw:
    raise ValueError('old manufacturing science or test modified '+rel)
  # Historical v0.1 snapshot needs its exact release manifest and tests.
  snap=target/'history/manufacturing_v0.1.0_branch_test_snapshot/MANUFACTURING-ATLAS'
  for rel in ('tests/test_models.py','tests/test_manifest.py','manufacturing_atlas/models.py','FILE_MANIFEST.json'):
   if (snap/rel).read_bytes()!=sib.read(SIBLING_ROOT+'/MANUFACTURING-ATLAS/'+rel):
    raise ValueError('historic sibling snapshot mismatch '+rel)
  queue=z.read(MAIN_ROOT+'/DOMAIN_QUEUE.json')
  if queue!=sib.read(SIBLING_ROOT+'/DOMAIN_QUEUE.json') or queue!=(target/'DOMAIN_QUEUE.json').read_bytes():
    raise ValueError('canonical 30 domain queue diverged')
  currentfiles=json.loads((target/'FILE_MANIFEST.json').read_text())['files']
  return {'schema':'atlas.original-federation-two-branch-reconciliation/1','result':'passed',
   'electronics_mainline_sha256':MAIN_SHA,'manufacturing_sibling_sha256':SIBLING_SHA,
   'prior_mainline_files':len(old_files),'prior_mainline_byte_identical':unchanged,
   'prior_mainline_authorized_changes':len(changed),'prior_mainline_changed_paths':sorted(changed),
   'old_mainline_deleted':0,'unauthorized_previous_changes':[],
   'prior_manufacturing_records_by_collection':original_mdata,
   'prior_manufacturing_chapters_tests_and_model_byte_identical':True,
   'prior_manufacturing_jsonl_byte_prefixes_preserved':True,
   'prior_manufacturing_cross_relations_preserved':True,
   'prior_13_node_registry_entries_unchanged':True,'current_nodes':14,
   'original_30_domain_queue_sha256':hashlib.sha256(queue).hexdigest(),
   'original_30_domain_queue_unchanged':True,
   'target_files_in_manifest':len(currentfiles),
   'evidence_limit':'file provenance/reproducibility only, no experimental manufacturing qualification or independent peer review'}

if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--mainline',type=Path,required=True)
 ap.add_argument('--manufacturing-sibling',type=Path,required=True)
 ap.add_argument('--target',type=Path,required=True)
 ap.add_argument('--out',type=Path,required=True)
 args=ap.parse_args();r=verify(args.mainline,args.manufacturing_sibling,args.target)
 args.out.parent.mkdir(parents=True,exist_ok=True)
 args.out.write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps({k:v for k,v in r.items() if k!='prior_mainline_changed_paths'},indent=2))
