#!/usr/bin/env python3
"""Reconstruct the original ATLAS FORGE Compiler Design v0.1.0 complete federation.

Must use the EXACT canonical Database Optimization v1.0.0 predecessor. Checks all
changed-member SHA-256 hashes, the final file manifest and full archive SHA-256.
No claim of scientific authentication or compiler soundness follows from hashes.
"""
EXPECTED_PREDECESSOR="13d8f5d19ed98d052dad9c424b22295599722b82a2938ec6f94f2a95122fe8c2"
EXPECTED_OUTPUT="cfd36e91dd1a093bf1edbd8a752f1fd6505e66123c577d167ed0f687c1381ebd"
from pathlib import Path, PurePosixPath
from zipfile import ZipFile, ZipInfo, ZIP_STORED, ZIP_DEFLATED
from hashlib import sha256
import json, re, sys, time
BINARY={'.zip','.whl','.png','.jpg','.jpeg','.webp','.gif','.mp4','.gz','.pdf','.ico','.woff','.woff2'}

def digest_file(p):
 h=sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(4<<20),b''):h.update(b)
 return h.hexdigest()

def assert_unique(z):
 names=z.namelist();assert len(names)==len(set(names)),'duplicate archive entry'

def restore(base,delta,target):
 if digest_file(base)!=EXPECTED_PREDECESSOR:
  raise RuntimeError("wrong original ATLAS FORGE predecessor")
 t=time.time(); base=Path(base); delta=Path(delta); target=Path(target)
 with ZipFile(base) as b,ZipFile(delta) as d:
  assert_unique(b);assert_unique(d)
  m=json.loads(d.read('PATCH_MANIFEST.json'))
  assert m['schema']=='atlas.original-federation-incremental/1'
  assert m['edition']=='Compiler_Design_v0.1.0'
  assert m['target_sha256']==EXPECTED_OUTPUT
  assert digest_file(base)==m['base_sha256'],('base hash mismatch',base)
  before=m['base_root'];after=m['target_root'];changed=m['changed_files']
  assert not m['deleted_files'],'deletions forbidden'
  assert set(d.namelist())=={'PATCH_MANIFEST.json'}|{'files/'+p for p in changed}
  prev=json.loads(b.read(before+'/FILE_MANIFEST.json'))['files']
  updated=json.loads(d.read('files/FILE_MANIFEST.json'))['files']
  assert not (set(prev)-set(updated)),'old deleted'
  assert set(updated)==set(prev)|set(changed)-{'FILE_MANIFEST.json'}
  assert len(updated)==m['target_files_sha256_count']
  for rel,hash_value in updated.items():
   q=PurePosixPath(rel)
   assert not q.is_absolute() and '..' not in q.parts and '\\' not in rel and ':' not in rel
   assert re.fullmatch(r'[a-f0-9]{64}',hash_value)
   assert (changed.get(rel)==hash_value if rel in changed else prev.get(rel)==hash_value),'drift '+rel
  target.parent.mkdir(parents=True,exist_ok=True)
  if target.exists():raise RuntimeError('refuse existing target')
  with ZipFile(target,'w',allowZip64=True) as out:
   for rel in sorted(updated)+['FILE_MANIFEST.json']:
    edit=rel in changed; source=d if edit else b
    inp=('files/'+rel) if edit else before+'/'+rel
    expected=changed['FILE_MANIFEST.json'] if rel=='FILE_MANIFEST.json' else updated[rel]
    info=ZipInfo(after+'/'+rel,date_time=tuple(m['compression_timestamp']))
    info.create_system=3; info.external_attr=0o100644<<16
    info.compress_type=ZIP_STORED if PurePosixPath(rel).suffix.lower() in BINARY else ZIP_DEFLATED
    with source.open(inp,'r') as stream,out.open(info,'w',force_zip64=True) as dest:
     h=sha256()
     while data:=stream.read(4<<20):dest.write(data);h.update(data)
     assert h.hexdigest()==expected,('entry drift',rel)
  h=digest_file(target)
  assert h==m['target_sha256'],('full archive hash',h,m['target_sha256'])
  assert target.stat().st_size>m.get('target_files_sha256_count',0)
  print(json.dumps({'edition':m['edition'],'hash':h,'files':len(updated),'seconds':round(time.time()-t,2),'archive_bytes':target.stat().st_size}),flush=True)
  return m
if __name__=='__main__':
 import argparse
 a=argparse.ArgumentParser();a.add_argument('base');a.add_argument('delta');a.add_argument('target')
 x=a.parse_args();restore(x.base,x.delta,x.target)
