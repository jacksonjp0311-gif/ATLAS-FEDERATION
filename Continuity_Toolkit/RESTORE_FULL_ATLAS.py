#!/usr/bin/env python3
"""Recover the FULL original ATLAS FORGE federation from fixed-size offline volumes.

No internet, model, external archive utility or pip dependency required.
The expected digest MUST be obtained from a trusted copy of the manifest.
The script checks volume names, hashes, full archive hash, size, ZIP paths,
CRC and member count, and refuses to overwrite any existing target.
"""
from __future__ import annotations
from pathlib import Path,PurePosixPath
from hashlib import sha256
from zipfile import ZipFile
from argparse import ArgumentParser
import json,re,shutil,sys

def digest(path):
    h=sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(4<<20),b''):h.update(b)
    return h.hexdigest()

def validate_name(name):
    if type(name) is not str or not re.fullmatch(r'ATLAS_COLLECTION_Computer_Architecture_v0\.5\.0\.zip\.part[0-9]{3}',name):
        raise ValueError('unrecognized or unsafe volume name')
    return name

def recover(parts_dir:Path,manifest_file:Path,output:Path):
    parts_dir=parts_dir.resolve();output=output.resolve()
    if output.exists():raise ValueError('refusing overwrite: '+str(output))
    if not parts_dir.is_dir() or parts_dir.is_symlink():raise ValueError('parts directory not found or symlinked')
    def paired(items):
        result={}
        for k,v in items:
            if k in result:raise ValueError('duplicate manifest key')
            result[k]=v
        return result
    doc=json.loads(manifest_file.read_bytes(),object_pairs_hook=paired)
    if doc.get('schema')!='atlas.full-archive-volume-manifest/1' or doc.get('full_archive_filename')!='ATLAS_COLLECTION_Computer_Architecture_v0.5.0.zip':
        raise ValueError('incorrect archive manifest')
    rows=doc.get('parts')
    if not isinstance(rows,list) or not rows or len(rows)>256:raise ValueError('invalid volume list')
    if not re.fullmatch(r'[0-9a-f]{64}',str(doc.get('full_archive_sha256'))):raise ValueError('full digest missing')
    expected_names=[f'ATLAS_COLLECTION_Computer_Architecture_v0.5.0.zip.part{i:03d}' for i in range(1,len(rows)+1)]
    if [x.get('filename') for x in rows]!=expected_names:raise ValueError('unordered or missing volume')
    total=0
    for part in rows:
        n=validate_name(part['filename']);file=parts_dir/n
        if file.is_symlink() or not file.is_file() or file.stat().st_size!=part['bytes']:
            raise ValueError('missing/symlinked/incorrect-volume-size '+n)
        if digest(file)!=part['sha256']:raise ValueError('volume SHA-256 mismatch '+n)
        total+=file.stat().st_size
    if total!=doc['full_archive_bytes']:raise ValueError('full expected byte count mismatch')
    output.parent.mkdir(parents=True,exist_ok=True)
    tmp=output.with_suffix(output.suffix+'.partial')
    if tmp.exists():raise ValueError('stale incomplete archive exists: '+str(tmp))
    try:
        h=sha256()
        with tmp.open('xb') as out:
            for item in rows:
                with (parts_dir/item['filename']).open('rb') as f:
                    while True:
                        b=f.read(4<<20)
                        if not b:break
                        out.write(b);h.update(b)
        if h.hexdigest()!=doc['full_archive_sha256']:raise ValueError('complete archive SHA-256 mismatch')
        with ZipFile(tmp) as z:
            members=z.infolist()
            if len(members)!=doc['zip_members']:raise ValueError('ZIP member count mismatch')
            if len(set(z.namelist()))!=len(members):raise ValueError('duplicate ZIP member paths')
            prefix=doc['root_directory']+'/'
            for m in members:
                n=m.filename
                if not n.startswith(prefix) or '\\' in n or ':' in n:
                    raise ValueError('unsafe or foreign archive member')
                sub=PurePosixPath(n[len(prefix):])
                if sub.is_absolute() or not sub.parts or '..' in sub.parts:
                    raise ValueError('path traversal or empty member')
                if (m.external_attr>>16)&0o170000==0o120000:
                    raise ValueError('symlink entry refused')
            if z.testzip() is not None:raise ValueError('ZIP CRC failure')
        tmp.rename(output)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise
    return {'schema':'atlas.full-archive-volume-restore/1','result':'passed',
            'output':str(output),'full_archive_sha256':doc['full_archive_sha256'],
            'full_archive_bytes':total,'parts_verified':len(rows),'zip_members':doc['zip_members'],
            'scientific_acceptance':'not_implied_by_file_hashes'}

def main(argv=None):
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('--parts-dir',type=Path,default=Path.cwd())
    parser.add_argument('--manifest',type=Path,default=None)
    parser.add_argument('--output',required=True,type=Path)
    a=parser.parse_args(argv)
    manifest=a.manifest or a.parts_dir/'FULL_ARCHIVE_PARTS_MANIFEST.json'
    try:report=recover(a.parts_dir,manifest,a.output)
    except (OSError,ValueError,KeyError,TypeError,json.JSONDecodeError) as exc:
        print(json.dumps({'result':'FAIL_CLOSED','message':str(exc)[:500]}),file=sys.stderr)
        return 2
    print(json.dumps(report,indent=2,sort_keys=True));return 0
if __name__=='__main__':raise SystemExit(main())
