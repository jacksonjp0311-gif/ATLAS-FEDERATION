"""ATLAS original SECDED(13,8) ROM integrity reference: 8 data + 4 parity + 1 overall.

Single-bit correction, double-bit detection only. Triple faults may be
miscorrected; no physical memory failure distribution or authenticity is proven.
"""
from __future__ import annotations
import hashlib

PARITY_POS=(1,2,4,8)
DATA_POS=(3,5,6,7,9,10,11,12)

class UncorrectableROMError(ValueError):pass


def encode_byte(byte: int) -> int:
    if type(byte) is not int or not 0<=byte<256:raise ValueError('exact byte 0..255 required')
    b=[0]*14
    for i,p in enumerate(DATA_POS):b[p]=(byte>>i)&1
    for p in PARITY_POS:b[p]=sum(b[i] for i in range(1,13) if (i&p) and i!=p)&1
    b[13]=sum(b[1:13])&1
    return sum(b[i]<<(i-1) for i in range(1,14))


def decode_word(word: int):
    if type(word) is not int or not 0<=word<(1<<13):raise ValueError('13-bit codeword required')
    b=[0]+[(word>>(i-1))&1 for i in range(1,14)]
    syndrome=sum(p for p in PARITY_POS if sum(b[i] for i in range(1,13) if i&p)%2)
    parity=sum(b[1:14])%2
    if not syndrome and not parity:status='clean'
    elif syndrome and parity:
        if syndrome>12:raise UncorrectableROMError('invalid syndrome')
        b[syndrome]^=1;status='corrected_single'
    elif not syndrome and parity:
        b[13]^=1;status='corrected_overall'
    else:
        return {'status':'detected_double','byte':None,'corrected_word':None,'syndrome':syndrome}
    data=sum(b[p]<<i for i,p in enumerate(DATA_POS))
    corrected=sum(b[p]<<(p-1) for p in range(1,14))
    return {'status':status,'byte':data,'corrected_word':corrected,'syndrome':syndrome}


def protect_rom(rom: bytes):
    if not isinstance(rom,bytes) or not 2<=len(rom)<=256 or len(rom)%2:
        raise ValueError('AT8 ROM must be even-length bytes within 2..256')
    return tuple(encode_byte(b) for b in rom)


def recover_rom(encoded,expected_sha256: str|None=None):
    if not isinstance(encoded,(list,tuple)) or len(encoded)<2 or len(encoded)>256 or len(encoded)%2:
        raise ValueError('bounded even length encoded ROM required')
    decoded=[];corrected=0;double=[]
    for i,word in enumerate(encoded):
        r=decode_word(word)
        if r['status']=='detected_double':double.append(i)
        elif r['status']!='clean':corrected+=1
        decoded.append(r['byte'])
    if double:raise UncorrectableROMError('double-error detected at byte indexes '+repr(double[:16]))
    rom=bytes(decoded)
    digest=hashlib.sha256(rom).hexdigest()
    if expected_sha256 is not None:
        if type(expected_sha256) is not str or len(expected_sha256)!=64 or any(c not in '0123456789abcdef' for c in expected_sha256):
            raise ValueError('lowercase expected SHA256 hex required')
        if digest!=expected_sha256:raise UncorrectableROMError('ROM hash mismatch after ECC recovery')
    return {'rom':rom,'rom_sha256':digest,'corrected_words':corrected,
      'double_errors_detected':0,'authentic_publisher_or_hardware_provenance':False}
