"""Offline finite versioned schema envelope, strict decoding, and canonical digests.

This is an original educational reference, NOT a security signature, externally
authenticated publisher document, or untrusted-input sandbox.
"""
from __future__ import annotations
import hashlib, json, math, re

class ContractError(ValueError):
    pass

_NAME = re.compile(r'^[a-z][a-z0-9_.-]{0,63}$')


def _safe_value(value, depth=0):
    if depth>8:raise ContractError('maximum nesting depth exceeded')
    if value is None or type(value) in (bool,int,str):
        if type(value) is str and len(value)>4096:raise ContractError('string too long')
        if type(value) is int and abs(value)>10**18:raise ContractError('integer out of bounds')
        return value
    if type(value) is float:
        if not math.isfinite(value):raise ContractError('nonfinite float')
        return value
    if type(value) is list and len(value)<=256:
        return [_safe_value(v,depth+1) for v in value]
    if type(value) is dict and len(value)<=128:
        result={}
        for k,v in value.items():
            if type(k) is not str or not _NAME.fullmatch(k):raise ContractError('invalid object key')
            result[k]=_safe_value(v,depth+1)
        return result
    raise ContractError('unsupported data type or size')


def canonical_bytes(value):
    return json.dumps(_safe_value(value),sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False).encode('utf-8')


def digest(value):return hashlib.sha256(canonical_bytes(value)).hexdigest()


def envelope(kind:str,version:int,payload:dict,record_id:str):
    if type(kind) is not str or not _NAME.fullmatch(kind):raise ContractError('invalid kind')
    if type(record_id) is not str or not _NAME.fullmatch(record_id):raise ContractError('invalid record ID')
    if type(version) is not int or not 1<=version<=255:raise ContractError('invalid version')
    if type(payload) is not dict:raise ContractError('payload must be mapping')
    clean=_safe_value(payload)
    result={'kind':kind,'version':version,'record_id':record_id,'payload':clean}
    result['sha256']=digest(result)
    return result


def parse_envelope(raw:bytes,allowed_kinds=None,max_size=65536):
    if type(raw) is not bytes or not 1<=len(raw)<=max_size:raise ContractError('bounded bytes required')
    try:obj=json.loads(raw.decode('utf-8'),parse_constant=lambda _: (_ for _ in ()).throw(ValueError('invalid numeric constant')))
    except (ValueError,UnicodeDecodeError) as exc:raise ContractError('malformed JSON') from exc
    if type(obj) is not dict or set(obj)!={'kind','version','record_id','payload','sha256'}:
        raise ContractError('exact envelope fields required')
    if allowed_kinds is not None and obj['kind'] not in allowed_kinds:
        raise ContractError('kind not allowed')
    if type(obj['sha256']) is not str or not re.fullmatch(r'[a-f0-9]{64}',obj['sha256']):
        raise ContractError('invalid digest syntax')
    expected=envelope(obj['kind'],obj['version'],obj['payload'],obj['record_id'])
    if expected['sha256']!=obj['sha256']:raise ContractError('envelope digest mismatch')
    return expected


def migrate_payload(kind, from_version:int, to_version:int, payload:dict, migrations:dict):
    """Consecutive pure adapters. Never invent missing values without declared rule."""
    if type(from_version) is not int or type(to_version) is not int or not 1<=from_version<=to_version<=255:
        raise ContractError('invalid migration versions')
    if type(migrations) is not dict:raise ContractError('migration functions mapping required')
    current=_safe_value(payload)
    if type(current) is not dict:raise ContractError('object payload required')
    for v in range(from_version,to_version):
        func=migrations.get((kind,v,v+1))
        if not callable(func):raise ContractError(f'missing explicit {v}->{v+1} migration')
        staged=func(dict(current))
        current=_safe_value(staged)
        if type(current) is not dict:raise ContractError('migration must produce object')
    return current
