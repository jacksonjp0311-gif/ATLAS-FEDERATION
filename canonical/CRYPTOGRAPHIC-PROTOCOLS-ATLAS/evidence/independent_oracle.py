"""Independent published-vector and alternate-oracle verification; stdlib only.

Runs deterministic finite comparisons. Does not constitute security proof,
cryptanalysis or formal cryptographic certification.
"""
from __future__ import annotations
import hashlib, json, random, hmac
from crypto_atlas.primitives import hmac_sha256,hkdf_extract,hkdf_expand,hkdf_sha256
from crypto_atlas.framing import encode_fields,decode_fields
from crypto_atlas.replay import ReplayWindow
from crypto_atlas.merkle import tree_hash,inclusion_proof,verify_inclusion
from crypto_atlas.authenticated_channel import AuthenticatedSession,AuthenticationError


def alternate_hmac_sha256(key: bytes,data: bytes) -> bytes:
    """Manually apply RFC 2104 padding rather than use hmac module."""
    if len(key)>64:key=hashlib.sha256(key).digest()
    key=key.ljust(64,b'\x00')
    inner=bytes(x^0x36 for x in key)
    outer=bytes(x^0x5c for x in key)
    return hashlib.sha256(outer+hashlib.sha256(inner+data).digest()).digest()


def alternate_hkdf_extract(salt:bytes|None,ikm:bytes)->bytes:
    return alternate_hmac_sha256(salt if salt is not None else bytes(32),ikm)


def alternate_hkdf_expand(prk:bytes,info:bytes,length:int)->bytes:
    blocks=[]
    for i in range(1,(length+31)//32+1):
        blocks.append(alternate_hmac_sha256(prk,(blocks[-1] if blocks else b'')+info+bytes([i])))
    return b''.join(blocks)[:length]


def naive_replay(states:list[int],seq:int,width:int)->bool:
    if not states:return True
    high=max(states)
    return seq>high or (seq>=high-width+1 and seq not in states)


def run()->dict:
    rng=random.Random(5092026)
    totals={'rfc_hmac_vectors':0,'rfc_hkdf_vectors':0,'independent_hmac':0,'independent_hkdf':0,'frame_roundtrips':0,'replay_against_set_oracle':0,'merkle_inclusion':0,'authenticity_negative_controls':0}
    rfc_hmac=[(bytes.fromhex('0b'*20),b'Hi There','b0344c61d8db38535ca8afceaf0bf12b881dc200c9833da726e9376c2e32cff7'),(b'Jefe',b'what do ya want for nothing?','5bdcc146bf60754e6a042426089575c75a003f089d2739839dec58b964ec3843'),(bytes.fromhex('aa'*20),bytes.fromhex('dd'*50),'773ea91e36800e46854db8ebd09181a72959098b3ef8c122d9635514ced565fe')]
    for k,m,d in rfc_hmac:
        assert hmac_sha256(k,m).hex()==d
        assert alternate_hmac_sha256(k,m).hex()==d
        totals['rfc_hmac_vectors']+=1
    rfc_hkdf=[(b'\x0b'*22,bytes(range(13)),bytes(range(240,250)),42,'077709362c2e32df0ddc3f0dc47bba6390b6c73bb50f9c3122ec844ad7c2b3e5','3cb25f25faacd57a90434f64d0362f2a2d2d0a90cf1a5a4c5db02d56ecc4c5bf34007208d5b887185865'),(b'\x0b'*22,b'',b'',42,'19ef24a32c717b167f33a91d6f648bdf96596776afdb6377ac434c1c293ccb04','8da4e775a563c18f715f802a063c5a31b8a11f5c5ee1879ec3454e5f3c738d2d9d201395faa4b61a96c8')]
    for ikm,salt,info,L,prk,okm in rfc_hkdf:
        assert hkdf_extract(salt,ikm).hex()==prk
        assert hkdf_sha256(ikm,salt,info,L).hex()==okm
        assert alternate_hkdf_expand(alternate_hkdf_extract(salt,ikm),info,L).hex()==okm
        totals['rfc_hkdf_vectors']+=1
    for _ in range(1500):
        k=rng.randbytes(rng.randrange(0,130));m=rng.randbytes(rng.randrange(0,190))
        assert hmac_sha256(k,m)==alternate_hmac_sha256(k,m)
        totals['independent_hmac']+=1
        ikm=rng.randbytes(rng.randrange(0,132));salt=rng.randbytes(rng.randrange(0,90));info=rng.randbytes(rng.randrange(0,170));L=rng.randrange(0,512)
        prk=alternate_hkdf_extract(salt,ikm)
        assert hkdf_extract(salt,ikm)==prk
        assert hkdf_expand(prk,info,L)==alternate_hkdf_expand(prk,info,L)
        totals['independent_hkdf']+=1
    for _ in range(1000):
        fields=tuple(rng.randbytes(rng.randrange(0,80)) for j in range(rng.randrange(0,16)))
        assert decode_fields(encode_fields(*fields))==fields
        totals['frame_roundtrips']+=1
    for width in (1,2,8,32,64,128):
        for _ in range(20):
            w=ReplayWindow(width=width); accepted=[]
            for j in range(150):
                seq=rng.randrange(0,151)
                expected=naive_replay(accepted,seq,width)
                assert w.accept(seq)==expected
                if expected:accepted.append(seq)
                totals['replay_against_set_oracle']+=1
    for n in range(1,90):
        leaves=[rng.randbytes(rng.randrange(0,32)) for _ in range(n)]
        # Independent bottom-up unbalanced split tree with SHA-256 prefix domain.
        def alternate_tree(xs):
            if not xs:return hashlib.sha256(b'').digest()
            if len(xs)==1:return hashlib.sha256(b'\x00'+xs[0]).digest()
            k=2**((len(xs)-1).bit_length()-1)
            return hashlib.sha256(b'\x01'+alternate_tree(xs[:k])+alternate_tree(xs[k:])).digest()
        root=alternate_tree(leaves)
        assert tree_hash(leaves)==root
        for idx in range(n):
            proof=inclusion_proof(leaves,idx)
            assert verify_inclusion(leaves[idx],idx,n,proof,root)
            assert not verify_inclusion(leaves[idx]+b'wrong',idx,n,proof,root)
            totals['merkle_inclusion']+=2
    for k in range(180):
        key=rng.randbytes(32)
        client=AuthenticatedSession(key,b'case-'+k.to_bytes(2,'big'),b'C',b'S','client')
        server=AuthenticatedSession(key,b'case-'+k.to_bytes(2,'big'),b'C',b'S','server')
        data=rng.randbytes(rng.randrange(1,100))
        frame=client.send(data)
        damaged=frame[:-1]+bytes([frame[-1]^1])
        try:server.receive(damaged)
        except AuthenticationError:pass
        else:raise AssertionError('forgery accepted')
        assert server.receive(frame)==data
        try:server.receive(frame)
        except AuthenticationError:pass
        else:raise AssertionError('replay accepted')
        totals['authenticity_negative_controls']+=3
    return {'schema':'atlas.crypto-protocols-independent-oracle/1','result':'passed','seed':5092026,'comparisons':sum(totals.values()),'detail':totals,'limits':'Finite deterministic software checks only. Standard RFC vectors are independently specified; HMAC independent oracle uses a separate padding implementation but SHA-256 is the shared hashlib primitive. Not cryptanalysis or security proof.'}

if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
