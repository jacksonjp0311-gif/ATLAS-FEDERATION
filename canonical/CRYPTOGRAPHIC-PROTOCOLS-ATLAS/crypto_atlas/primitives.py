"""Standard-library reference to RFC 2104/4231, RFC 5869 and RFC 9846.

This is not a validated cryptographic module. Never use these wrappers as a
replacement for a maintained protocol library or hardware key protection.
"""
from __future__ import annotations
import hashlib
import hmac
import struct

HASHLEN = 32


def _bytes(value: bytes, name: str) -> bytes:
    if type(value) is not bytes:
        raise TypeError(f"{name} must be bytes")
    return value


def hmac_sha256(key: bytes, message: bytes) -> bytes:
    return hmac.digest(_bytes(key, "key"), _bytes(message, "message"), hashlib.sha256)


def hkdf_extract(salt: bytes | None, ikm: bytes) -> bytes:
    _bytes(ikm, "ikm")
    if salt is None:
        salt = bytes(HASHLEN)
    return hmac_sha256(_bytes(salt, "salt"), ikm)


def hkdf_expand(prk: bytes, info: bytes, length: int) -> bytes:
    _bytes(prk, "prk")
    _bytes(info, "info")
    if len(prk) < HASHLEN:
        raise ValueError("PRK must contain at least 32 bytes for SHA-256")
    if type(length) is not int or not (0 <= length <= 255 * HASHLEN):
        raise ValueError("HKDF expand length exceeds 255 HashLen or is invalid")
    t = b""
    output = bytearray()
    for block_num in range(1, (length + HASHLEN - 1) // HASHLEN + 1):
        t = hmac_sha256(prk, t + info + bytes([block_num]))
        output.extend(t)
    return bytes(output[:length])


def hkdf_sha256(ikm: bytes, salt: bytes | None, info: bytes, length: int) -> bytes:
    return hkdf_expand(hkdf_extract(salt, ikm), info, length)


def hkdf_expand_label(secret: bytes, label: bytes, context: bytes, length: int) -> bytes:
    """TLS 1.3 HKDF-Expand-Label. This is NOT a TLS implementation."""
    _bytes(label, "label"); _bytes(context, "context")
    if type(length) is not int or length < 0 or length > 65535:
        raise ValueError("invalid labeled expand length")
    full_label = b"tls13 " + label
    if len(full_label) > 255 or len(context) > 255:
        raise ValueError("TLS label or context too long")
    hkdf_label = struct.pack(">H", length) + bytes([len(full_label)]) + full_label + bytes([len(context)]) + context
    return hkdf_expand(secret, hkdf_label, length)


def tls13_record_nonce(write_iv: bytes, sequence: int) -> bytes:
    """RFC 9846 Section 5.3 XOR record nonce construction (12-byte IV case)."""
    _bytes(write_iv, "write_iv")
    if len(write_iv) != 12:
        raise ValueError("reference model supports 96-bit IV only")
    if type(sequence) is not int or not (0 <= sequence < 2**64):
        raise ValueError("TLS 1.3 record number must fit 64 bits; never wrap")
    nonce_mask = bytes(4) + sequence.to_bytes(8, "big")
    return bytes(x ^ y for x, y in zip(write_iv, nonce_mask))


def verify_tag(expected: bytes, provided: bytes) -> bool:
    _bytes(expected, "expected"); _bytes(provided, "provided")
    return hmac.compare_digest(expected, provided)
