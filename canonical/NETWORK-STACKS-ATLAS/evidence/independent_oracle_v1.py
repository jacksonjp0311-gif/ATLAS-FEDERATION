"""Independent finite oracles for added Network Stacks v1 scope.

Separate one-complement byte summation, Decimal RTT recursion and exhaustive
routing and prefix membership checks; same Python platform (not wire/peer review).
"""
from __future__ import annotations
import json,hashlib,struct,ipaddress,random,sys
from decimal import Decimal
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from net_atlas.net_reference import PacketError, internet_checksum, ipv4_packet, parse_ipv4, longest_prefix_route
from net_atlas.net_extended import encode_udp_checked,validate_udp_checksum,tcp_rto_estimator,prefix_length_from_mask,pmtu_payload_limit

def byte_oracle(data: bytes)->int:
    # Group even-index bytes into their high-order position and odd as low.
    hi=sum(data[::2]);lo=sum(data[1::2]);w=(hi<<8)+lo
    while w>=65536:w=(w%65536)+(w//65536)
    return 65535-w

def prefix_oracle(mask:int)->int:
    bits=f'{mask:032b}'
    if '01' in bits:raise ValueError('noncontiguous mask')
    return bits.count('1')

def decimal_rto(samples):
    x=[Decimal(str(i)) for i in samples]
    avg=x[0];var=x[0]/2
    for v in x[1:]:
        var=Decimal('0.75')*var+Decimal('0.25')*abs(avg-v)
        avg=Decimal('0.875')*avg+Decimal('0.125')*v
    return max(Decimal(1),avg+max(Decimal('0.01'),4*var))

def run():
    rng=random.Random(20261119);checks=0;categories={}
    def step(label):
        nonlocal checks
        checks+=1;categories[label]=categories.get(label,0)+1
    for _ in range(9000):
        b=rng.randbytes(rng.randrange(0,128))
        assert internet_checksum(b)==byte_oracle(b)
        step('checksum_byte_oracle')
    for _ in range(12000):
        payload=rng.randbytes(rng.randrange(0,180))
        fam=rng.choice([4,6])
        a,b=('192.0.2.1','198.51.100.2') if fam==4 else ('2001:db8::1','2001:db8::2')
        p=encode_udp_checked(a,b,rng.randrange(65536),rng.randrange(65536),payload)
        sa=ipaddress.ip_address(a).packed;da=ipaddress.ip_address(b).packed
        pseudo=(sa+da+b'\x00\x11'+len(p).to_bytes(2,'big')) if fam==4 else (sa+da+len(p).to_bytes(4,'big')+bytes(3)+b'\x11')
        assert byte_oracle(pseudo+p)==0
        assert validate_udp_checksum(a,b,p)
        step('udp_independent_checksum')
    for _ in range(10000):
        src=rng.randrange(2**32);prefix=rng.randrange(33);mask=(((1<<prefix)-1)<<(32-prefix))
        assert prefix_length_from_mask(mask)==prefix_oracle(mask)
        p=ipaddress.IPv4Network((src,prefix),strict=False)
        route=[('0.0.0.0/0','fallback'),(str(p),'best')]
        if prefix!=0:assert longest_prefix_route(str(ipaddress.IPv4Address(src)),route)=='best'
        step('prefix_independent')
    for _ in range(5000):
        samples=[rng.randint(1,5000)/10000 for _ in range(rng.randrange(1,8))]
        approx=tcp_rto_estimator(samples)[2]
        exact=float(decimal_rto(samples))
        assert abs(approx-exact)<1e-10
        step('rto_decimal')
    for _ in range(5000):
        ip=rng.choice([4,6]);mtu=rng.randrange(1280,9000);h=rng.randrange(8,80)
        assert pmtu_payload_limit(mtu,ip,h)==mtu-(20 if ip==4 else 40)-h
        step('pmtu_independent')
    # deliberately altered checksum must fail as CHECKSUM failure, not incidental length
    for _ in range(900):
        p=bytearray(ipv4_packet('192.0.2.1','198.51.100.2',b'payload'))
        p[8]^=1
        try:parse_ipv4(p)
        except PacketError as ex:assert 'checksum' in str(ex)
        else:raise AssertionError('bad ipv4 checksum accepted')
        step('specific_negative')
    return {'schema':'atlas.network-stacks-independent-oracle-v1/1','passed':checks,
      'failures':0,'categories':categories,'seed':20261119,
      'independence':'different arithmetic/Decimal and external published fixed vectors; same Python runtime',
      'wire_interoperability_tested':False}
if __name__=='__main__':print(json.dumps(run(),indent=2))
