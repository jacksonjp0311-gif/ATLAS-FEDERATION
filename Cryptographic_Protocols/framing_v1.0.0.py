"""Unambiguous binary tuple framing, not a substitute for all TLS/CBOR parsing."""
from __future__ import annotations
import struct

MAX_FIELDS = 32
MAX_FIELD_BYTES = 1 << 20

def encode_fields(*fields: bytes) -> bytes:
    if len(fields) > MAX_FIELDS:
        raise ValueError("too many fields")
    parts = [struct.pack(">H", len(fields))]
    for field in fields:
        if type(field) is not bytes:
            raise TypeError("frame field must be bytes")
        if len(field) > MAX_FIELD_BYTES:
            raise ValueError("field too long")
        parts.append(struct.pack(">I", len(field)))
        parts.append(field)
    return b"".join(parts)


def decode_fields(data: bytes) -> tuple[bytes, ...]:
    if type(data) is not bytes or len(data) < 2:
        raise ValueError("truncated header")
    count = struct.unpack_from(">H", data, 0)[0]
    if count > MAX_FIELDS:
        raise ValueError("too many fields")
    pos = 2
    fields = []
    for _ in range(count):
        if pos + 4 > len(data):
            raise ValueError("truncated length")
        length = struct.unpack_from(">I", data, pos)[0]
        pos += 4
        if length > MAX_FIELD_BYTES or pos + length > len(data):
            raise ValueError("bad field length")
        fields.append(data[pos:pos + length])
        pos += length
    if pos != len(data):
        raise ValueError("trailing bytes / noncanonical framing")
    return tuple(fields)
