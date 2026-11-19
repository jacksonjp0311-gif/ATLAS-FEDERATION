"""Additional bounded network construction/verification reference.

These functions explicitly do NOT implement a production network stack,
PKI/TLS, live NIC integration, or any complete RFC protocol state machine.
"""
from __future__ import annotations
from dataclasses import dataclass
import ipaddress, struct, math
from .net_reference import PacketError,internet_checksum


@dataclass(frozen=True)
class EthernetFrame:
    destination: bytes
    source: bytes
    ethertype: int
    payload: bytes


def parse_ethernet_frame(frame: bytes) -> EthernetFrame:
    """14-byte Ethernet II header only; excludes preamble, FCS, VLAN and PHY.

    Since FCS and link padding are outside this model, a successful parse is
    NOT a claim of frame integrity or of application payload length.
    """
    if len(frame) < 14:raise PacketError('truncated ethernet header')
    dst,src,kind=frame[:6],frame[6:12],int.from_bytes(frame[12:14],'big')
    if kind < 1536:raise PacketError('802.3 length field unsupported')
    if kind in (0x8100,0x88a8):raise PacketError('VLAN tag unsupported')
    return EthernetFrame(dst,src,kind,frame[14:])


def build_ethernet_frame(dst:bytes,src:bytes,ethertype:int,payload:bytes)->bytes:
    if len(dst)!=6 or len(src)!=6 or not 1536<=ethertype<=65535 or ethertype in (0x8100,0x88a8):
        raise PacketError('invalid or unsupported ethernet fields')
    return dst+src+ethertype.to_bytes(2,'big')+payload


@dataclass(frozen=True)
class ARP:
    operation:int
    sender_hw:bytes
    sender_ip:str
    target_hw:bytes
    target_ip:str


def parse_arp_ethernet_ipv4(payload:bytes)->ARP:
    """RFC 826 classic ARP for Ethernet/IPv4 only. No trust assessment."""
    if len(payload)!=28:raise PacketError('unsupported ARP size')
    htype,ptype,hlen,plen,op=struct.unpack('!HHBBH',payload[:8])
    if (htype,ptype,hlen,plen)!=(1,0x0800,6,4) or op not in (1,2):
        raise PacketError('unsupported ARP hardware/protocol/operation')
    return ARP(op,payload[8:14],str(ipaddress.IPv4Address(payload[14:18])),
               payload[18:24],str(ipaddress.IPv4Address(payload[24:28])))


def udp_pseudoheader(src:str,dst:str,proto:int,length:int)->bytes:
    sa=ipaddress.ip_address(src);da=ipaddress.ip_address(dst)
    if type(sa)!=type(da) or not 0<=length<=65535:
        raise PacketError('invalid UDP address family/length')
    if isinstance(sa,ipaddress.IPv4Address):
        if proto!=17:raise PacketError('unsupported IPv4 next protocol')
        return sa.packed+da.packed+b'\0'+bytes([proto])+struct.pack('!H',length)
    return sa.packed+da.packed+struct.pack('!I',length)+b'\0'*3+bytes([proto])


def encode_udp_checked(src:str,dst:str,source_port:int,dest_port:int,payload:bytes)->bytes:
    """Build UDP checksum over IPv4/IPv6 pseudo-header and UDP segment.

    For IPv4 a computed arithmetic zero is transmitted as 0xffff to avoid
    confusion with optional absent UDP checksum. For IPv6 zero is prohibited.
    """
    if not 0<=source_port<=65535 or not 0<=dest_port<=65535:
        raise PacketError('UDP port out of range')
    if len(payload)+8>65535:raise PacketError('UDP size unsupported')
    length=8+len(payload)
    first=struct.pack('!HHHH',source_port,dest_port,length,0)+payload
    c=internet_checksum(udp_pseudoheader(src,dst,17,length)+first)
    if c==0:c=0xffff
    return struct.pack('!HHHH',source_port,dest_port,length,c)+payload


def validate_udp_checksum(src:str,dst:str,segment:bytes)->bool:
    if len(segment)<8:raise PacketError('truncated UDP')
    length=int.from_bytes(segment[4:6],'big')
    if length!=len(segment) or length<8:raise PacketError('invalid UDP length')
    checksum=int.from_bytes(segment[6:8],'big')
    is_v6=isinstance(ipaddress.ip_address(src),ipaddress.IPv6Address)
    # IPv4 optional omitted checksum is NOT an integrity check.
    if checksum==0:
        if is_v6:raise PacketError('IPv6 UDP zero checksum unsupported')
        return False
    if internet_checksum(udp_pseudoheader(src,dst,17,length)+segment)!=0:
        raise PacketError('UDP checksum mismatch')
    return True


def pmtu_payload_limit(path_mtu:int,ip_version:int,transport_header_bytes:int)->int:
    """Pure accounting only; ignores tunnels, extension headers and PMTU discovery."""
    if ip_version not in (4,6):raise ValueError('IP version must be 4 or 6')
    minimum=68 if ip_version==4 else 1280
    if path_mtu<minimum or transport_header_bytes<8:raise ValueError('invalid PMTU or transport overhead')
    overhead=(20 if ip_version==4 else 40)+transport_header_bytes
    if path_mtu<overhead:raise ValueError('negative payload capacity')
    return path_mtu-overhead


def tcp_rto_estimator(samples:list[float],granularity:float=0.01)->tuple[float,float,float]:
    """RFC 6298-style SRTT/RTTVAR/RTO with 1-second floor; no Karn algorithm.

    Samples must already be eligible (never from ambiguously retransmitted data).
    Do not apply these values to actual retransmission timers without Karn,
    backoff, timeouts, maximums and timer implementation testing.
    """
    if not samples or granularity<=0 or not math.isfinite(granularity):raise ValueError('bad samples/granularity')
    srtt=None;dev=None
    for measured in samples:
        if not math.isfinite(measured) or measured<=0:raise ValueError('nonpositive or nonfinite RTT')
        if srtt is None:srtt=measured;dev=measured/2
        else:
            dev=0.75*dev+0.25*abs(srtt-measured)
            srtt=0.875*srtt+0.125*measured
    rto=max(1.0,srtt+max(granularity,4*dev))
    return srtt,dev,rto


def icmpv4_checksum(message:bytes)->int:
    """Checksum ICMPv4 message bytes, zeroing existing checksum field first."""
    if len(message)<4:raise PacketError('truncated ICMP')
    return internet_checksum(message[:2]+b'\0\0'+message[4:])


def verify_icmpv4(message:bytes)->bool:
    if len(message)<4:raise PacketError('truncated ICMP')
    if internet_checksum(message)!=0:raise PacketError('ICMP checksum mismatch')
    return True


def prefix_length_from_mask(mask:int,bits:int=32)->int:
    """Verify contiguous prefix mask by enumerating all legal masks."""
    if bits not in (32,128) or not 0<=mask<(1<<bits):raise PacketError('mask out of range')
    for width in range(bits+1):
        if mask==(((1<<width)-1)<<(bits-width)):
            return width
    raise PacketError('noncontiguous prefix mask')
