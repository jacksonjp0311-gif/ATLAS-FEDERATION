"""MAC-only educational authenticated channel.

No secrecy, no forward secrecy, no external-identity verification, no durable
nonce state and no cross-process atomicity. Do not deploy as a protocol.
"""
from __future__ import annotations
from dataclasses import dataclass, field
import hashlib
import struct
from .framing import encode_fields,decode_fields
from .primitives import hkdf_extract,hkdf_expand,hmac_sha256,verify_tag
from .replay import ReplayWindow

DOMAIN = b"ATLAS-FORGE/AUTHENTICATED-CHANNEL/v1/EDUCATIONAL-ONLY"

class AuthenticationError(ValueError):
    pass


def derive_directional_keys(psk: bytes, context: bytes, client_id: bytes, server_id: bytes) -> tuple[bytes, bytes]:
    if not all(type(x) is bytes for x in (psk,context,client_id,server_id)):
        raise TypeError("all key schedule inputs must be bytes")
    if len(psk) < 32 or not client_id or not server_id or client_id == server_id:
        raise ValueError("reference model requires strong 32-byte PSK and distinct nonempty identity labels")
    # SHA-256 of canonical context is a public *salt*, not secret entropy.
    transcript = hashlib.sha256(encode_fields(DOMAIN,context,client_id,server_id)).digest()
    prk = hkdf_extract(transcript,psk)
    c2s = hkdf_expand(prk,encode_fields(DOMAIN,b"client-to-server",transcript),32)
    s2c = hkdf_expand(prk,encode_fields(DOMAIN,b"server-to-client",transcript),32)
    assert c2s != s2c
    return c2s,s2c


@dataclass
class AuthenticatedSession:
    psk: bytes
    context: bytes
    client_id: bytes
    server_id: bytes
    role: str
    outgoing_sequence: int = 0
    incoming: ReplayWindow = field(default_factory=ReplayWindow)

    def __post_init__(self) -> None:
        if self.role not in {"client","server"}:
            raise ValueError("role must be client/server")
        if type(self.outgoing_sequence) is not int or not 0 <= self.outgoing_sequence < 2**64:
            raise ValueError("invalid outbound state")
        self.c2s,self.s2c=derive_directional_keys(self.psk,self.context,self.client_id,self.server_id)

    def send(self, payload: bytes) -> bytes:
        if type(payload) is not bytes:
            raise TypeError("payload must be bytes")
        if self.outgoing_sequence >= 2**64-1:
            raise ValueError("outgoing sequence exhausted; new key/session required")
        key = self.c2s if self.role=="client" else self.s2c
        direction = b"C2S" if self.role=="client" else b"S2C"
        seq = self.outgoing_sequence
        core = encode_fields(DOMAIN,direction,self.context,self.client_id,self.server_id,seq.to_bytes(8,"big"),payload)
        tag = hmac_sha256(key,core)
        self.outgoing_sequence += 1
        return encode_fields(core,tag)

    def receive(self, encoded: bytes) -> bytes:
        try:
            core,tag=decode_fields(encoded)
            if len(tag)!=32:
                raise AuthenticationError("invalid tag length")
            domain,direction,context,client_id,server_id,raw_seq,payload=decode_fields(core)
            expected_direction=b"S2C" if self.role=="client" else b"C2S"
            if (domain,direction,context,client_id,server_id)!=(DOMAIN,expected_direction,self.context,self.client_id,self.server_id):
                raise AuthenticationError("domain or identity or context mismatch")
            if len(raw_seq)!=8:
                raise AuthenticationError("sequence must be eight bytes")
            seq=int.from_bytes(raw_seq,"big")
            key=self.s2c if self.role=="client" else self.c2s
            if not verify_tag(hmac_sha256(key,core),tag):
                raise AuthenticationError("authentication failure")
            if not self.incoming.accept(seq):
                raise AuthenticationError("replay or stale frame")
            return payload
        except (TypeError,ValueError) as exc:
            if isinstance(exc, AuthenticationError):
                raise
            raise AuthenticationError("invalid or malformed frame") from exc
