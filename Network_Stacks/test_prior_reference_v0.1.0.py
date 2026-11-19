"""Bounded unit and negative controls for offline scientific reference."""
import ipaddress
import random
import struct
import unittest
from net_reference import (
    PacketError, internet_checksum, ipv4_packet, parse_ipv4, parse_ipv6,
    encode_dns_name, decode_dns_name, encode_quic_varint, decode_quic_varint,
    tcp_segment_acceptable, longest_prefix_route, parse_udp_header,
)

class NetworkReferenceTests(unittest.TestCase):
    def test_checksum_odd(self): self.assertEqual(internet_checksum(b'\x00'),0xffff)
    def test_checksum_known(self): self.assertEqual(internet_checksum(bytes.fromhex('00010002')),0xfffc)
    def test_checksum_even(self): self.assertEqual(internet_checksum(bytes.fromhex('ffff0000')),0)
    def test_ipv4_round_trip(self):
        p=ipv4_packet('192.0.2.1','198.51.100.2',b'hello',identification=123)
        h=parse_ipv4(p)
        self.assertEqual((h.source,h.destination,h.identification,h.payload),('192.0.2.1','198.51.100.2',123,b'hello'))
    def test_ipv4_zero_payload(self): self.assertEqual(parse_ipv4(ipv4_packet('1.1.1.1','2.2.2.2',b'')).total_length,20)
    def test_ipv4_checksum_corruption(self):
        p=bytearray(ipv4_packet('1.1.1.1','2.2.2.2',b'hi'));p[8] ^= 1
        with self.assertRaisesRegex(PacketError,'checksum'): parse_ipv4(bytes(p))
    def test_ipv4_truncation(self):
        with self.assertRaises(PacketError):parse_ipv4(b'\x45'*19)
    def test_ipv4_options_rejected(self):
        p=bytearray(ipv4_packet('1.1.1.1','2.2.2.2',b''));p[0]=0x46
        with self.assertRaises(PacketError):parse_ipv4(bytes(p))
    def test_ipv4_fragment_rejected_after_valid_checksum(self):
        p=bytearray(ipv4_packet('1.1.1.1','2.2.2.2',b'hi'))
        p[6:8]=b'\x20\x00';p[10:12]=b'\0\0';p[10:12]=internet_checksum(bytes(p[:20])).to_bytes(2,'big')
        self.assertEqual(internet_checksum(p[:20]),0)
        with self.assertRaisesRegex(PacketError,'fragmentation'):parse_ipv4(bytes(p))
    def test_ipv4_large_packet(self):
        with self.assertRaises(PacketError):ipv4_packet('1.1.1.1','2.2.2.2',b'x'*65516)
    def test_ipv4_field_range(self):
        with self.assertRaises(PacketError):ipv4_packet('1.1.1.1','2.2.2.2',b'',ttl=0)
    def test_ipv6_valid_fixed(self):
        p=bytes.fromhex('6000000000031140')+ipaddress.IPv6Address('2001:db8::1').packed+ipaddress.IPv6Address('2001:db8::2').packed+b'abc'
        h=parse_ipv6(p);self.assertEqual((h.next_header,h.extension_count,h.payload),(17,0,b'abc'))
    def test_ipv6_hop_options(self):
        p=bytes.fromhex('60000000000b0040')+bytes(32)+bytes([17,0,0,0,0,0,0,0])+b'abc'
        h=parse_ipv6(p);self.assertEqual((h.next_header,h.extension_count,h.payload),(17,1,b'abc'))
    def test_ipv6_truncated_extension(self):
        p=bytes.fromhex('6000000000080040')+bytes(32)+bytes([17,1])+bytes(6)
        with self.assertRaisesRegex(PacketError,'truncated'):parse_ipv6(p)
    def test_ipv6_fragment_not_reassembled(self):
        p=bytes.fromhex('6000000000082c40')+bytes(32)+bytes([17,0,0,1,0,0,0,0])
        with self.assertRaisesRegex(PacketError,'reassembly'):parse_ipv6(p)
    def test_ipv6_bad_length(self):
        p=bytes.fromhex('6000000000031140')+bytes(32)+b'x'
        with self.assertRaises(PacketError):parse_ipv6(p)
    def test_quic_vectors(self):
        vectors={0:'00',63:'3f',64:'4040',16383:'7fff',16384:'80004000',(1<<30)-1:'bfffffff',1<<30:'c000000040000000',(1<<62)-1:'ffffffffffffffff'}
        for n,h in vectors.items():
            with self.subTest(n=n):
                wire=encode_quic_varint(n)
                self.assertEqual(wire.hex(),h)
                self.assertEqual(decode_quic_varint(wire),(n,len(wire)))
    def test_quic_nonminimal_decode(self):self.assertEqual(decode_quic_varint(bytes.fromhex('4001')),(1,2))
    def test_quic_bounds(self):
        for n in [-1,1<<62,1.0,True]:
            with self.assertRaises(PacketError):encode_quic_varint(n)
    def test_quic_truncated(self):
        with self.assertRaises(PacketError):decode_quic_varint(bytes.fromhex('4001')[:1])
    def test_dns_uncompressed(self):
        labels=(b'www',b'example',b'org');s=encode_dns_name(labels)
        self.assertEqual(decode_dns_name(s,0),(labels,len(s)))
    def test_dns_pointers(self):
        wire=encode_dns_name((b'example',b'org'))+b'\x03www\xc0\x00'
        self.assertEqual(decode_dns_name(wire,13),((b'www',b'example',b'org'),19))
    def test_dns_root(self):self.assertEqual(decode_dns_name(b'\0',0),((),1))
    def test_dns_pointer_loop(self):
        with self.assertRaisesRegex(PacketError,'cycle'):decode_dns_name(b'\xc0\x00',0)
    def test_dns_truncated_pointer(self):
        with self.assertRaises(PacketError):decode_dns_name(b'\xc0',0)
    def test_dns_long_label(self):
        with self.assertRaises(PacketError):encode_dns_name((b'a'*64,))
    def test_dns_long_name(self):
        with self.assertRaises(PacketError):encode_dns_name((b'x'*63,)*4)
    def test_tcp_seq(self):
        self.assertTrue(tcp_segment_acceptable(0,0,0,0))
        self.assertFalse(tcp_segment_acceptable(1,0,0,0))
        self.assertFalse(tcp_segment_acceptable(0,1,0,0))
    def test_tcp_window(self):
        self.assertTrue(tcp_segment_acceptable(109,1,100,10))
        self.assertFalse(tcp_segment_acceptable(110,1,100,10))
        self.assertTrue(tcp_segment_acceptable(98,4,100,10))
        self.assertFalse(tcp_segment_acceptable(80,4,100,10))
    def test_tcp_wrap(self):
        self.assertTrue(tcp_segment_acceptable(0,1,0xfffffffe,4))
        self.assertFalse(tcp_segment_acceptable(4,1,0xfffffffe,4))
    def test_route(self):
        routes=[('0.0.0.0/0','default'),('10.0.0.0/8','lan'),('10.12.0.0/16','specific')]
        self.assertEqual(longest_prefix_route('10.12.0.1',routes),'specific')
        self.assertEqual(longest_prefix_route('10.13.0.1',routes),'lan')
        self.assertEqual(longest_prefix_route('8.8.8.8',routes),'default')
    def test_route_ipv6(self):self.assertEqual(longest_prefix_route('2001:db8::a',[('2001:db8::/32','v6')]),'v6')
    def test_udp_length(self):
        p=struct.pack('!HHHH',12,53,11,0)+b'abc'
        self.assertEqual(parse_udp_header(p),(12,53,b'abc'))
        with self.assertRaises(PacketError):parse_udp_header(p[:-1])

if __name__ == '__main__': unittest.main()
