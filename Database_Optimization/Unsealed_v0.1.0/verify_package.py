"""Offline integrity and exact revision validator for a *staged* Atlas domain.

Does not validate the entire canonical federation or simulate physical failure.
"""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def sha(data):return hashlib.sha256(data).hexdigest()
def canon(obj):return json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()

def verify():
    manifest=json.loads((ROOT/'FILE_MANIFEST.json').read_bytes())
    assert manifest['schema']=='atlas.db-optimization.unsealed-file-manifest/1'
    for path,info in manifest['files'].items():
        f=ROOT/path
        assert f.is_file(), f'Missing: {path}'
        raw=f.read_bytes()
        assert len(raw)==info['bytes'],f'Byte length: {path}'
        assert sha(raw)==info['sha256'],f'Hash mismatch: {path}'
    atlas=json.loads((ROOT/'atlas_manifest.json').read_bytes())
    assert atlas['node_id']=='database-optimization-atlas'
    assert sha(canon(atlas['collections']))==atlas['corpus_revision']
    records={};relation_count=0
    for kind,desc in atlas['collections'].items():
        raw=(ROOT/desc['path']).read_bytes()
        assert sha(raw)==desc['sha256'],f'Collection hash failure {kind}'
        parsed=[json.loads(x) for x in raw.splitlines() if x]
        assert len(parsed)==desc['records'],kind
        for item in parsed:
            current_revision=item['revision']
            without={k:v for k,v in item.items() if k!='revision'}
            assert sha(canon(without))==current_revision,(kind,item.get('record_id'))
            if kind=='relations':
                relation_count+=1
            else:
                rid=item['record_id']
                assert rid not in records
                records[rid]=current_revision
    prior=json.loads((ROOT/'EXACT_PREDECESSOR_LINKS.json').read_bytes())
    exact={x['record_id']:x['revision'] for x in prior['predecessor_records']}
    for line in (ROOT/'data/relations.jsonl').read_text().splitlines():
        r=json.loads(line)
        for edge in ('from','to'):
            dest=r[edge]
            expected=records.get(dest['record_id'],exact.get(dest['record_id']))
            assert expected and expected==dest['revision'],(edge,dest)
    receipt=json.loads((ROOT/'TEST_RECEIPT.json').read_bytes())
    assert receipt['unit_tests_failed']==0 and receipt['oracle_failures']==0
    assert receipt['unit_tests_passed']>=30
    assert receipt['oracle_comparisons']>=54018
    return {'schema':'atlas.db-optimization.staged-content-validation/1','result':'passed',
            'file_hashes_checked':len(manifest['files']),
            'records_validated':len(records),'relations_validated':relation_count,
            'predecessor_exact_dependencies':len(exact),
            'canonical_federation_released':False,
            'full_federation_regression_executed':False}

if __name__=='__main__': print(json.dumps(verify(),sort_keys=True))
