#!/usr/bin/env python3
"""Exact historical preservation against published Bioelectric v0.1 federation.

This is a byte-integrity/lineage audit, NOT independent scientific or physical
power-loss validation. Refuses old file deletions and unauthorized changes.
"""
from __future__ import annotations
from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
import argparse,json

BASE='ATLAS_COLLECTION_Bioelectric_v0.1.0'
N='software-design-patterns-atlas'
EXPECTED='685e9d8d610c1714eab4a1a11eef6006845be10982b5213184b1182ff6218ff5'
ALLOWED={'README.md','START_HERE.md','CURRENT_CHECKPOINT.json','BUILD_POLICY.json','common/registry.json',
         'common/registry.lock.json','tools/check_collection.py'}

def digest(path):
    h=sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(4<<20),b''):h.update(b)
    return h.hexdigest()

def audit(base,target):
    if digest(base)!=EXPECTED:raise ValueError('exact Bioelectric predecessor SHA-256 required')
    with ZipFile(base) as z:
        if z.testzip() is not None:raise ValueError('predecessor corrupt')
        previous=json.loads(z.read(BASE+'/FILE_MANIFEST.json'))['files']
        prior_reg=json.loads(z.read(BASE+'/common/registry.json'))
        original_queue=z.read(BASE+'/DOMAIN_QUEUE.json')
        original_test=z.read(BASE+'/tools/test_bioelectric_survival.py')
    now_reg=json.loads((target/'common/registry.json').read_text())
    previous_nodes={x['node_id']:x for x in prior_reg['nodes']}
    new_nodes={x['node_id']:x for x in now_reg['nodes']}
    previous_node_entries_equal=len(previous_nodes)==16 and len(new_nodes)==17 and all(new_nodes.get(n)==v for n,v in previous_nodes.items())
    queue_equal=(target/'DOMAIN_QUEUE.json').read_bytes()==original_queue
    frozen=target/'history/bioelectric_v0.1.0_survival_test_snapshot/tools/test_bioelectric_survival.py'
    frozen_test_equal=frozen.is_file() and frozen.read_bytes()==original_test
    identical=0;modified=[];deleted=[];unauthorized=[]
    for rel,expected in previous.items():
        p=target/rel
        if not p.is_file():deleted.append(rel)
        elif digest(p)==expected:identical+=1
        else:
            modified.append(rel)
            if rel not in ALLOWED:unauthorized.append(rel)
    oldscience_unchanged=all(rel not in modified and rel not in deleted for rel in previous if rel.startswith('common/nodes/') and not rel.startswith('common/nodes/'+N+'/'))
    if (target/'FILE_MANIFEST.json').exists():
        current=json.loads((target/'FILE_MANIFEST.json').read_text())['files']
        added=len(set(current)-set(previous))
    else:added=None
    valid=not deleted and not unauthorized and previous_node_entries_equal and queue_equal and frozen_test_equal and oldscience_unchanged
    return {'schema':'atlas.software-patterns-v01-preservation/1','result':'passed' if valid else 'failed',
            'predecessor_sha256':EXPECTED,'prior_file_count':len(previous),'prior_identical':identical,
            'prior_authorized_modified':len(modified),'modified_old_paths':modified,
            'prior_deleted':len(deleted),'deleted_paths':deleted,'unauthorized_changed_paths':unauthorized,
            'added_files_after_manifest':added,
            'previous_16_node_registry_entries_unchanged':previous_node_entries_equal,
            'old_science_data_file_hashes_unchanged':oldscience_unchanged,
            'original_30_domain_queue_byte_identical':queue_equal,
            'previous_bioelectric_release_specific_test_file_byte_identical':frozen_test_equal,
            'physical_power_loss_or_external_science_proven':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--base',type=Path,required=True);p.add_argument('--target',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();result=audit(a.base,a.target)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    if a.out.exists():raise SystemExit('refuse overwrite historical preservation receipt')
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('modified_old_paths','deleted_paths')},indent=2))
    if result['result']!='passed':raise SystemExit(1)
