#!/usr/bin/env python3
"""Check exact predecessor file hashes and immutable node revisions.

Usage: python verify_electronics_v1rc_preservation.py --base-zip v0.4.zip
       --target /extracted/ATLAS_COLLECTION_Electronics_Semiconductors_v0.4.0
       --output outside/release.json
"""
import argparse,hashlib,json,os
from pathlib import Path
from zipfile import ZipFile
N='ELECTRONICS-SEMICONDUCTORS-ATLAS'
BASE='ATLAS_COLLECTION_Electronics_Semiconductors_v0.4.0'
EXPECT='85393f8a447b7289023c5f53105e3097f616e800e8b22cb967730fefcccd4a0d'

def sha_bytes(x):return hashlib.sha256(x).hexdigest()
def sha_file(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(4<<20),b''):h.update(b)
    return h.hexdigest()

def main(base,target,output):
    if sha_file(base)!=EXPECT:raise ValueError('base must be exact canonical v0.4 ZIP')
    with ZipFile(base) as z:
        if z.testzip() is not None:raise ValueError('corrupt predecessor ZIP')
        files=json.loads(z.read(BASE+'/FILE_MANIFEST.json'))['files']
        prev_reg=json.loads(z.read(BASE+'/common/registry.json'))
        curr_reg=json.loads((target/'common/registry.json').read_bytes())
        def electron_prefix(path):
            return z.read(BASE+'/'+path)
        changed=[];deleted=[];same=0;unauthorized=[]
        for rel,want in files.items():
            path=target/rel
            if not path.exists():deleted.append(rel);continue
            if sha_file(path)==want:same+=1
            else:
                changed.append(rel)
                if not (rel.startswith(N+'/') or rel in {
                    'CURRENT_CHECKPOINT.json','README.md','common/registry.json',
                    'common/registry.lock.json','tools/check_collection.py',
                    'common/nodes/electronics-semiconductors-atlas/atlas_manifest.json',
                    *('common/nodes/electronics-semiconductors-atlas/data/'+c+'.jsonl' for c in
                        ['concepts','claims','equations','methods','sources','relations','datasets','reviews'])
                }):unauthorized.append(rel)
        e_changed=[]
        for path in [f'{N}/data/{c}.jsonl' for c in ['concepts','claims','equations','methods','sources','relations','datasets','reviews']] + [
          'common/nodes/electronics-semiconductors-atlas/data/'+c+'.jsonl' for c in ['concepts','claims','equations','methods','sources','relations','datasets','reviews']]:
            if not (target/path).read_bytes().startswith(electron_prefix(path)):
                e_changed.append(path)
        prev_other={v['node_id']:v['manifest_sha256'] for v in prev_reg['nodes'] if v['node_id']!='electronics-semiconductors-atlas'}
        new_other={v['node_id']:v['manifest_sha256'] for v in curr_reg['nodes'] if v['node_id']!='electronics-semiconductors-atlas'}
        old_queue=sha_bytes(electron_prefix('DOMAIN_QUEUE.json'))
        cur_queue=sha_file(target/'DOMAIN_QUEUE.json')
        old_policy=sha_bytes(electron_prefix('BUILD_POLICY.json'))
        cur_policy=sha_file(target/'BUILD_POLICY.json')
        # Test files from previous version should be exactly retained, not weakened.
        changed_tests=[f for f in changed if '/tests/' in f]
        current={p.relative_to(target).as_posix() for p in target.rglob('*') if p.is_file()
                 and not any(x in ('__pycache__','.git','build','output') or x.endswith('.egg-info') for x in p.relative_to(target).parts)}
        additions=sorted(current-(set(files)|{'FILE_MANIFEST.json'}))
        status='passed' if not (deleted or unauthorized or e_changed or changed_tests) and prev_other==new_other and old_queue==cur_queue and old_policy==cur_policy else 'failed'
        result={'schema':'atlas.electronics-v1rc-historical-preservation/1',
           'result':status,'base_full_archive_sha256':EXPECT,
           'previous_files':len(files),'previous_byte_identical':same,'authorized_old_changes':len(changed),
           'new_files':len(additions),'previous_deleted_files':deleted,'unauthorized_changes':unauthorized,
           'changed_old_files':changed,'changed_historical_tests':changed_tests,
           'old_electronics_record_relation_prefixes_identical':not e_changed,
           'other_12_node_registry_hashes_unchanged':prev_other==new_other,
           'domain_queue_sha256_unchanged':old_queue==cur_queue,'build_policy_sha256_unchanged':old_policy==cur_policy,
           'original_publisher_transport_authenticated':False,'independent_scientific_review':False}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('changed_old_files','previous_deleted_files')},indent=2))
    if status!='passed':raise SystemExit(1)
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--base-zip',type=Path,required=True)
    p.add_argument('--target',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();main(a.base_zip,a.target,a.output)
