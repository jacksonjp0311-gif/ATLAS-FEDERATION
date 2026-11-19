"""ATLAS FORGE #16: bounded offline packet/algorithm reference models.

Not a deployable network stack, firewall, protocol security layer, or live-wire parser.
Requires only the Python 3 standard library.
"""
from __future__ import annotations
from dataclasses import dataclass
import ipaddress
import struct
from typing import Iterable

MAX_DNS_POINTER_HOPS = 64
MAX_IPV6_EXTENSIONS = 8
QUIC_VARINT_MAX = (1 << 62) - 1

class PacketError(ValueError):
    """A packet violates a supported structural condition."""


def internet_checksum(data: bytes) -> int:
    """RFC 1071 one's-complement checksum; zero on a valid full header."""
    if len(data) % 2:
        data += b"\x00"
    acc = sum((data[i] << 8) | data[i+1] for i in range(0, len(data), 2))
    while acc >> 16:
        acc = (acc & 0xffff) + (acc >> 16)
    return (~acc) & 0xffff


def ipv4_packet(src: str, dst: str, payload: bytes, *, protocol: int=17,
                ttl: int=64, identification: int=0) -> bytes:
    """Produce a minimal non-fragmented IPv4 datagram (RFC 791)."""
    try:
        a = ipaddress.IPv4Address(src).packed
        b = ipaddress.IPv4Address(dst).packed
    except ipaddress.AddressValueError as e:
        raise PacketError(str(e)) from e
    if not all((0 <= protocol <= 255, 1 <= ttl <= 255, 0 <= identification <= 65535)):
        raise PacketError("field out of range")
    if len(payload) > 65535 - 20:
        raise PacketError("IPv4 total length exceeds 65535")
    header = struct.pack('!BBHHHBBH4s4s', 0x45, 0, 20+len(payload),
                         identification, 0, ttl, protocol, 0, a, b)
    c = internet_checksum(header)
    return header[:10]+struct.pack('!H', c)+header[12:]+payload


@dataclass(frozen=True)
class IPv4Header:
    source: str
    destination: str
    protocol: int
    ttl: int
    identification: int
    total_length: int
    payload: bytes


def parse_ipv4(packet: bytes) -> IPv4Header:
    """Validate minimal IPv4 packets; deliberately reject options/fragmentation."""
    if len(packet) < 20:
        raise PacketError('truncated IPv4 header')
    version, ihl = packet[0] >> 4, packet[0] & 15
    if version != 4 or ihl != 5:
        raise PacketError('unsupported IPv4 version/header options')
    total = int.from_bytes(packet[2:4], 'big')
    if total < 20 or total != len(packet):
        raise PacketError('invalid total length or trailing bytes')
    if internet_checksum(packet[:20]) != 0:
        raise PacketError('IPv4 checksum mismatch')
    frag = int.from_bytes(packet[6:8], 'big')
    if frag & 0x3fff:  # MF flag or fragment offset
        raise PacketError('IPv4 fragmentation not supported')
    return IPv4Header(str(ipaddress.IPv4Address(packet[12:16])),
                      str(ipaddress.IPv4Address(packet[16:20])),
                      packet[9], packet[8], int.from_bytes(packet[4:6],'big'),
                      total, packet[20:])


@dataclass(frozen=True)
class IPv6Packet:
    source: str
    destination: str
    next_header: int
    hop_limit: int
    payload: bytes
    extension_count: int


def parse_ipv6(packet: bytes) -> IPv6Packet:
    """Bounded IPv6 parsing: only common 8-byte-unit option chains and atomic frag.

    Rejects jumbo payload, AH/ESP, non-atomic fragmentation and unknown extension
    interpretation. This is a limited educational validator, not RFC 8200 coverage.
    """
    if len(packet) < 40 or (packet[0] >> 4) != 6:
        raise PacketError('invalid IPv6 fixed header')
    length = int.from_bytes(packet[4:6],'big')
    if len(packet) != 40 + length or length == 0:
        raise PacketError('unsupported IPv6 length/jumbogram')
    nxt = packet[6]; offset = 40; count=0
    while nxt in (0, 43, 44, 60):
        count += 1
        if count > MAX_IPV6_EXTENSIONS or offset+8 > len(packet):
            raise PacketError('IPv6 extension cap or truncation')
        next_after = packet[offset]
        if nxt == 44:  # fragment: only atomic fragments; no reassembly
            if int.from_bytes(packet[offset+2:offset+4],'big') & 0xfff9:
                raise PacketError('IPv6 reassembly not supported')
            size=8
        else:
            size=8*(packet[offset+1]+1)
            if offset+size > len(packet):
                raise PacketError('truncated IPv6 extension')
        offset += size; nxt=next_after
    if nxt in (50, 51):
        raise PacketError('ESP/AH not interpreted by this reference')
    return IPv6Packet(str(ipaddress.IPv6Address(packet[8:24])),
                      str(ipaddress.IPv6Address(packet[24:40])),
                      nxt, packet[7], packet[offset:], count)


def encode_quic_varint(n: int) -> bytes:
    """RFC 9000 §16 QUIC variable-length integer encoder."""
    if isinstance(n, bool) or not isinstance(n, int) or not 0 <= n <= QUIC_VARINT_MAX:
        raise PacketError('QUIC integer out of range')
    for width in (1,2,4,8):
        if n < (1 << (8*width-2)):
            return (({1:0,2:1,4:2,8:3}[width] << (8*width-2)) | n).to_bytes(width,'big')
    raise AssertionError('unreachable')


def decode_quic_varint(data: bytes, offset: int=0) -> tuple[int,int]:
    if offset < 0 or offset >= len(data):
        raise PacketError('missing QUIC integer')
    nbytes = 1 << (data[offset] >> 6)
    if offset+nbytes > len(data):
        raise PacketError('truncated QUIC integer')
    raw=int.from_bytes(data[offset:offset+nbytes],'big')
    return raw & ((1 << (8*nbytes-2))-1), offset+nbytes


def encode_dns_name(labels: Iterable[bytes]) -> bytes:
    """RFC 1035 wire labels; ASCII/IDNA encoding is caller responsibility."""
    encoded=bytearray()
    for lab in labels:
        if not isinstance(lab,bytes) or not 1 <= len(lab) <= 63:
            raise PacketError('invalid DNS label length/type')
        encoded.append(len(lab));encoded.extend(lab)
    encoded.append(0)
    if len(encoded) > 255:
        raise PacketError('DNS name too long')
    return bytes(encoded)


def decode_dns_name(packet: bytes, offset: int) -> tuple[tuple[bytes,...],int]:
    """Decode RFC 1035 DNS pointer compression without following cycles."""
    if not 0 <= offset < len(packet):
        raise PacketError('DNS offset out of bounds')
    parts=[]; seen=set(); cursor=offset; next_offset=None; hops=0; uncompressed_len=1
    while True:
        if cursor in seen or hops > MAX_DNS_POINTER_HOPS:
            raise PacketError('DNS compression cycle/limit')
        seen.add(cursor); hops += 1
        if cursor >= len(packet):
            raise PacketError('truncated DNS name')
        v=packet[cursor]
        if v & 0xc0 == 0xc0:
            if cursor+1 >= len(packet):
                raise PacketError('truncated DNS pointer')
            pointer=((v&0x3f)<<8)|packet[cursor+1]
            if pointer >= len(packet):
                raise PacketError('DNS pointer out of packet')
            if next_offset is None: next_offset=cursor+2
            cursor=pointer
        elif v & 0xc0:
            raise PacketError('reserved DNS label type')
        elif v == 0:
            if next_offset is None: next_offset=cursor+1
            return tuple(parts),next_offset
        else:
            length=v
            if cursor+1+length > len(packet):
                raise PacketError('truncated DNS label')
            uncompressed_len+=length+1
            if uncompressed_len > 255:
                raise PacketError('DNS name expanded length >255')
            parts.append(packet[cursor+1:cursor+1+length])
            cursor+=1+length


def seq_difference(a:int,b:int) -> int:
    """Distance from b to a in the 32-bit TCP sequence space."""
    for v in (a,b):
        if not isinstance(v,int) or isinstance(v,bool) or not 0<=v<=0xffffffff:
            raise PacketError('sequence not uint32')
    return (a-b) & 0xffffffff


def tcp_segment_acceptable(seq:int,length:int,rcv_nxt:int,rcv_wnd:int) -> bool:
    """RFC 9293 §3.4: segment acceptable for receive-window sequence test.

    Length includes SYN/FIN sequence occupancy if caller supplies it. Does not
    establish TCP connection state, checksum, PAWS, RST or security handling.
    """
    if length < 0 or not 0 <= rcv_wnd < (1 << 31):
        raise PacketError('negative length or unsupported window')
    if length >= (1 << 31):
        raise PacketError('unsupported segment length')
    if rcv_wnd==0:
        return length==0 and seq_difference(seq,rcv_nxt)==0
    first=seq_difference(seq,rcv_nxt)
    if length==0:
        return first < rcv_wnd
    last=seq_difference((seq+length-1)&0xffffffff,rcv_nxt)
    return first < rcv_wnd or last < rcv_wnd


def longest_prefix_route(address: str, routes: Iterable[tuple[str,str]]) -> str|None:
    """RFC 4632 longest-prefix match. Earlier route wins on equal prefix."""
    ip=ipaddress.ip_address(address);best=(-1,None)
    for cidr, next_hop in routes:
        net=ipaddress.ip_network(cidr,strict=False)
        if net.version==ip.version and ip in net and net.prefixlen>best[0]:
            best=(net.prefixlen,next_hop)
    return best[1]


def parse_udp_header(segment: bytes) -> tuple[int,int,bytes]:
    """RFC 768 length-only UDP framing; checksum must be separately validated.

    Deliberately DOES NOT claim valid IPv4 or IPv6 UDP checksums or security.
    """
    if len(segment)<8:raise PacketError('truncated UDP')
    src,dst,length,_checksum=struct.unpack('!HHHH',segment[:8])
    if length!=len(segment) or length<8:
        raise PacketError('invalid UDP length')
    return src,dst,segment[8:]
