#!/usr/bin/env python3
"""Verify append-only canonical ATLAS FORGE continuation from Electronics 0.2.0.

Must be given the exact predecessor full ZIP and a new v0.3 source tree;
files are read and hashed, never modified. File equality != scientific review.
"""
import argparse,hashlib,json
from pathlib import Path
from zipfile import ZipFile
BASE_SHA='6b1d4306606f25712b8a27bed962817fccf83a8409ba4086e83d9b3b9dd8f0cd'
OLD_ROOT='ATLAS_COLLECTION_Electronics_Semiconductors_v0.2.0'
NEW_NODE='electronics-semiconductors-atlas'
ALLOWED={'CURRENT_CHECKPOINT.json','README.md','common/registry.json','common/registry.lock.json','tools/check_collection.py'}
NODE_PREFIX='ELECTRONICS-SEMICONDUCTORS-ATLAS/'
COMMON_PREFIX='common/nodes/electronics-semiconductors-atlas/'

def digest_bytes(data):return hashlib.sha256(data).hexdigest()
def digest_file(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for chunk in iter(lambda:f.read(4<<20),b''):h.update(chunk)
 return h.hexdigest()
def run(base,target):
 if digest_file(base)!=BASE_SHA:raise ValueError('wrong predecessor full ZIP digest')
 with ZipFile(base) as z:
  old=json.loads(z.read(f'{OLD_ROOT}/FILE_MANIFEST.json'))['files']
  old_reg=json.loads(z.read(f'{OLD_ROOT}/common/registry.json'))
  old_data={name:z.read(f'{OLD_ROOT}/{NODE_PREFIX}data/{name}.jsonl')
             for name in ('concepts','claims','equations','methods','sources','datasets','reviews','relations')}
  old_fullrel=z.read(f'{OLD_ROOT}/{COMMON_PREFIX}data/relations.jsonl')
  old_tests={name:z.read(f'{OLD_ROOT}/{NODE_PREFIX}tests/{name}') for name in ('test_models.py','test_v02_models.py')}
 old_node={n['node_id']:n['manifest_sha256'] for n in old_reg['nodes']}
 new_reg=json.loads((target/'common/registry.json').read_text())
 new_nodes={n['node_id']:n['manifest_sha256'] for n in new_reg['nodes']}
 assert set(old_node)==set(new_nodes) and len(new_nodes)==13
 assert all(new_nodes[n]==old_node[n] for n in old_node if n!=NEW_NODE),'prior nodes altered'
 missing=[];modified=[];identical=0
 for rel,expect in old.items():
  p=target/rel
  if not p.is_file():missing.append(rel)
  elif digest_file(p)==expect:identical+=1
  else:modified.append(rel)
 unauthorized=sorted(rel for rel in modified if not (rel in ALLOWED or rel.startswith(NODE_PREFIX) or rel.startswith(COMMON_PREFIX)))
 if missing or unauthorized:raise ValueError('missing or unauthorized files: '+repr((missing[:6],unauthorized[:6])))
 for name,data in old_data.items():
  if not (target/NODE_PREFIX/'data'/f'{name}.jsonl').read_bytes().startswith(data):
   raise ValueError('immutable previous revision lost: '+name)
 if not (target/COMMON_PREFIX/'data/relations.jsonl').read_bytes().startswith(old_fullrel):
  raise ValueError('prior cross-node relationships changed')
 for name,data in old_tests.items():
  hist=target/'history/electronics_v0.2.0_test_snapshot/ELECTRONICS-SEMICONDUCTORS-ATLAS/tests'/name
  if hist.read_bytes()!=data or (target/NODE_PREFIX/'tests'/name).read_bytes()!=data:
   raise ValueError('v02 historic test mutated '+name)
 if digest_file(target/'DOMAIN_QUEUE.json')!=old['DOMAIN_QUEUE.json']:
  raise ValueError('original thirty-domain queue edited')
 policy=json.loads((target/'BUILD_POLICY.json').read_text())
 if policy.get('Bitwork_router_modified') or policy.get('Bitwork_router_changes') or not policy.get('canonical_original_thirty_unchanged'):
  raise ValueError('policy condition violated')
 current={p.relative_to(target).as_posix() for p in target.rglob('*') if p.is_file() and not any(q in ('__pycache__','.git','build','output') or q.endswith('.egg-info') for q in p.relative_to(target).parts)}
 newfiles=len(current-(set(old)|{'FILE_MANIFEST.json'}))
 return {'schema':'atlas.electronics-v03-canonical-preservation/1','status':'passed','base_sha256':BASE_SHA,
  'predecessor_files':len(old),'byte_identical_old_files':identical,'authorized_old_changes':len(modified),
  'changed_paths':sorted(modified),'deleted_old_files':len(missing),'unauthorized_old_changes':unauthorized,
  'new_files':newfiles,'historical_record_prefixes':True,'historical_relation_prefixes':True,
  'prior_v02_tests_frozen_unchanged':True,'other_node_manifest_hashes_unchanged':12,
  'domain_queue_sha256':old['DOMAIN_QUEUE.json'],'router_unchanged':True,
  'scope':'structural byte/integrity preservation only; no scientific peer review or device measurements'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--base-zip',type=Path,required=True)
 ap.add_argument('--target',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
 report=run(a.base_zip,a.target)
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k!='changed_paths'},indent=2))
if __name__=='__main__':main()
