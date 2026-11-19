"""Cross-check bounded reference with independent algorithms and fixed vectors."""
import ipaddress
import json
import random
import unittest
from net_reference import (internet_checksum, ipv4_packet, parse_ipv4, encode_quic_varint,
                           decode_quic_varint, longest_prefix_route, tcp_segment_acceptable,
                           decode_dns_name, encode_dns_name)


def bytewise_checksum(buf):
    """Separate byte addition and end-around carry implementation."""
    acc=0
    for i,b in enumerate(buf):
        acc += (b<<8) if i%2==0 else b
    while acc>65535:acc=(acc&65535)+(acc//65536)
    return (~acc)&65535


def separate_quic_encode(value):
    if value < 64: width=1
    elif value < 16384: width=2
    elif value < 1073741824: width=4
    else:width=8
    b=list(value.to_bytes(width,'big'))
    b[0]=(b[0] & 0x3f) | ({1:0,2:0x40,4:0x80,8:0xc0}[width])
    return bytes(b)


def brute_route(addr,routes):
    ip=ipaddress.ip_address(addr)
    candidates=[(ipaddress.ip_network(n,False).prefixlen,-i,hop) for i,(n,hop) in enumerate(routes)
                if ipaddress.ip_network(n,False).version==ip.version and ip in ipaddress.ip_network(n,False)]
    return max(candidates)[2] if candidates else None


def brute_tcp_accept(seq,nbytes,nxt,window):
    # Separate literal set membership on tiny finite receive windows, including wrap.
    if window==0: return nbytes==0 and seq==nxt
    legal={(nxt+i)&0xffffffff for i in range(window)}
    if nbytes==0:return seq in legal
    return seq in legal or (seq+nbytes-1)&0xffffffff in legal


def verify():
    rng=random.Random(20261118)
    count=0
    for n in range(0,2049):
        buf=rng.randbytes(n%100)
        assert internet_checksum(buf)==bytewise_checksum(buf)
        count+=1
    for _ in range(12000):
        value=rng.randrange(0,1<<62)
        wire=encode_quic_varint(value)
        assert wire==separate_quic_encode(value)
        assert decode_quic_varint(wire)==(value,len(wire))
        count+=1
    for _ in range(2000):
        src='192.0.2.'+str(rng.randrange(1,255))
        dst='198.51.100.'+str(rng.randrange(1,255))
        payload=rng.randbytes(rng.randrange(0,200))
        wire=ipv4_packet(src,dst,payload,protocol=17,identification=rng.randrange(65536))
        assert bytewise_checksum(wire[:20])==0
        p=parse_ipv4(wire)
        assert p.source==src and p.destination==dst and p.payload==payload
        count+=1
    for _ in range(3000):
        routes=[]
        for j in range(rng.randrange(0,20)):
            prefix=rng.randrange(0,33)
            mask=(0xffffffff<<(32-prefix))&0xffffffff if prefix else 0
            address=int.from_bytes(rng.randbytes(4),'big')&mask
            routes.append((str(ipaddress.IPv4Address(address))+'/'+str(prefix),str(j)))
        addr=str(ipaddress.IPv4Address(int.from_bytes(rng.randbytes(4),'big')))
        assert longest_prefix_route(addr,routes)==brute_route(addr,routes)
        count+=1
    for _ in range(5000):
        nxt=rng.randrange(0,1<<32)
        offset=rng.randrange(-32,33)
        seq=(nxt+offset)&0xffffffff
        win=rng.randrange(0,18)
        nbytes=rng.randrange(0,20)
        assert tcp_segment_acceptable(seq,nbytes,nxt,win)==brute_tcp_accept(seq,nbytes,nxt,win)
        count+=1
    for _ in range(2000):
        labels=tuple(rng.randbytes(rng.randrange(1,16)) for _ in range(rng.randrange(0,6)))
        wire=encode_dns_name(labels)
        assert decode_dns_name(wire,0)==(labels,len(wire))
        count+=1
    return {'result':'passed','independent_finite_comparisons':count,
            'test_seed':20261118,'independent_oracles':['bytewise_checksum','separate_quic_encode',
            'independent_python_ipaddress_longest_prefix','literal_window_set_tcp','DNS_wire_roundtrip'],
            'scope':'educational finite software checks, not physical/network interoperability'}

if __name__=='__main__': print(json.dumps(verify(),indent=2,sort_keys=True))
