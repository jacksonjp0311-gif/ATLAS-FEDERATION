"""Network Stacks v1.0.0 finite unit and negative controls, not wire conformance."""
import struct, unittest, ipaddress, random
from net_atlas.net_reference import *
from net_atlas.net_extended import *
class PrimitiveTests(unittest.TestCase):
 def test_ipv4_roundtrip(self):
  for n in [0,1,2,13,101,1490]:
   p=ipv4_packet('192.0.2.1','198.51.100.2',b'x'*n)
   self.assertEqual(parse_ipv4(p).payload,b'x'*n)
 def test_ipv4_checksum_corrupt(self):
  p=bytearray(ipv4_packet('192.0.2.1','198.51.100.2',b'hello'));p[8]^=2
  with self.assertRaisesRegex(PacketError,'checksum'):parse_ipv4(p)
 def test_ipv4_fragment_valid_checksum_rejected(self):
  p=bytearray(ipv4_packet('192.0.2.1','198.51.100.2',b'x'));p[6:8]=b'\x20\x00';p[10:12]=b'\0\0';p[10:12]=struct.pack('!H',internet_checksum(p[:20]))
  self.assertEqual(internet_checksum(p[:20]),0)
  with self.assertRaisesRegex(PacketError,'fragment'):parse_ipv4(p)
 def test_ipv6(self):
  p=bytes.fromhex('6000000000031140')+ipaddress.IPv6Address('2001:db8::1').packed+ipaddress.IPv6Address('2001:db8::2').packed+b'abc'
  self.assertEqual(parse_ipv6(p).payload,b'abc')
 def test_ipv6_bad(self):
  with self.assertRaises(PacketError):parse_ipv6(b'\x60'*39)
 def test_dns_simple(self):
  x=encode_dns_name((b'www',b'example',b'org'))
  self.assertEqual(decode_dns_name(x,0),((b'www',b'example',b'org'),len(x)))
 def test_dns_pointer_loop(self):
  with self.assertRaisesRegex(PacketError,'cycle'):decode_dns_name(b'\xc0\x00',0)
 def test_dns_label_length(self):
  with self.assertRaises(PacketError):encode_dns_name([b'x'*64])
 def test_quic_known_vectors(self):
  for n,h in {0:'00',63:'3f',64:'4040',16383:'7fff',16384:'80004000',2**30:'c000000040000000'}.items():
   self.assertEqual(encode_quic_varint(n).hex(),h)
   self.assertEqual(decode_quic_varint(bytes.fromhex(h)),(n,len(bytes.fromhex(h))))
 def test_quic_long_truncation(self):
  with self.assertRaises(PacketError):decode_quic_varint(b'\xc0')
 def test_tcp_zero_window(self):
  self.assertTrue(tcp_segment_acceptable(100,0,100,0))
  self.assertFalse(tcp_segment_acceptable(100,1,100,0))
 def test_tcp_wrap(self):
  self.assertTrue(tcp_segment_acceptable(0,1,0xfffffffe,4))
  self.assertFalse(tcp_segment_acceptable(4,1,0xfffffffe,4))
 def test_route_longest(self):
  self.assertEqual(longest_prefix_route('192.0.2.7',[('0.0.0.0/0','default'),('192.0.0.0/8','broad'),('192.0.2.0/24','specific')]),'specific')
 def test_route_ipv6(self):
  self.assertEqual(longest_prefix_route('2001:db8::1',[('::/0','d'),('2001:db8::/32','v6')]),'v6')
 def test_udp_length(self):
  self.assertEqual(parse_udp_header(struct.pack('!HHHH',12,53,11,0)+b'abc'),(12,53,b'abc'))
 def test_udp_bad_length(self):
  with self.assertRaises(PacketError):parse_udp_header(struct.pack('!HHHH',12,53,12,0)+b'abc')
class ExtendedTests(unittest.TestCase):
 def test_ethernet(self):
  frame=build_ethernet_frame(b'abcdef',b'123456',0x0800,b'ABC')
  self.assertEqual(parse_ethernet_frame(frame),EthernetFrame(b'abcdef',b'123456',0x0800,b'ABC'))
 def test_ethernet_short(self):
  with self.assertRaises(PacketError):parse_ethernet_frame(b'\x00'*13)
 def test_ethernet_vlan_hold(self):
  with self.assertRaisesRegex(PacketError,'VLAN'):parse_ethernet_frame(b'123456789012\x81\x00')
 def test_arp_rfc826(self):
  p=struct.pack('!HHBBH',1,0x800,6,4,1)+b'123456'+ipaddress.IPv4Address('192.0.2.1').packed+b'abcdef'+ipaddress.IPv4Address('192.0.2.2').packed
  parsed=parse_arp_ethernet_ipv4(p);self.assertEqual(parsed.sender_ip,'192.0.2.1');self.assertEqual(parsed.operation,1)
 def test_arp_nolength(self):
  with self.assertRaises(PacketError):parse_arp_ethernet_ipv4(b'\0'*14)
 def test_arp_unsupported(self):
  p=struct.pack('!HHBBH',1,0x86dd,6,16,1)+b'\0'*20
  with self.assertRaises(PacketError):parse_arp_ethernet_ipv4(p)
 def test_udp_checksum_v4(self):
  msg=encode_udp_checked('192.0.2.1','198.51.100.2',1000,53,b'hello world')
  self.assertTrue(validate_udp_checksum('192.0.2.1','198.51.100.2',msg))
 def test_udp_checksum_v6(self):
  msg=encode_udp_checked('2001:db8::1','2001:db8::2',1000,53,b'hello world')
  self.assertTrue(validate_udp_checksum('2001:db8::1','2001:db8::2',msg))
 def test_udp_checksum_corrupt_v4(self):
  msg=bytearray(encode_udp_checked('192.0.2.1','198.51.100.2',1000,53,b'hello world'));msg[9]^=1
  with self.assertRaisesRegex(PacketError,'checksum'):validate_udp_checksum('192.0.2.1','198.51.100.2',msg)
 def test_udp_checksum_corrupt_v6(self):
  msg=bytearray(encode_udp_checked('2001:db8::1','2001:db8::2',1000,53,b'hello world'));msg[12]^=1
  with self.assertRaisesRegex(PacketError,'checksum'):validate_udp_checksum('2001:db8::1','2001:db8::2',msg)
 def test_udp_omitted_checksum_ipv4(self):
  msg=struct.pack('!HHHH',123,53,11,0)+b'abc'
  self.assertFalse(validate_udp_checksum('192.0.2.1','198.51.100.2',msg))
 def test_udp_zero_checksum_v6(self):
  msg=struct.pack('!HHHH',123,53,11,0)+b'abc'
  with self.assertRaisesRegex(PacketError,'zero'):validate_udp_checksum('2001:db8::1','2001:db8::2',msg)
 def test_udp_mixed_address_family(self):
  with self.assertRaises(PacketError):udp_pseudoheader('192.0.2.1','2001:db8::2',17,11)
 def test_pmtu_v4(self):self.assertEqual(pmtu_payload_limit(1500,4,8),1472)
 def test_pmtu_v6(self):self.assertEqual(pmtu_payload_limit(1280,6,8),1232)
 def test_pmtu_bad(self):
  with self.assertRaises(ValueError):pmtu_payload_limit(1200,6,8)
 def test_rto_initial(self):
  srtt,rtv,rto=tcp_rto_estimator([.25]);self.assertAlmostEqual(srtt,.25);self.assertAlmostEqual(rtv,.125);self.assertEqual(rto,1)
 def test_rto_update(self):
  srtt,rtv,rto=tcp_rto_estimator([.25,.35]);self.assertAlmostEqual(srtt,.2625);self.assertGreaterEqual(rto,1)
 def test_rto_bad(self):
  with self.assertRaises(ValueError):tcp_rto_estimator([float('nan')])
 def test_icmp_v4(self):
  msg=b'\x08\x00\x00\x00'+b'abcd';cs=icmpv4_checksum(msg);msg=msg[:2]+struct.pack('!H',cs)+msg[4:]
  self.assertTrue(verify_icmpv4(msg))
 def test_icmp_corrupt(self):
  msg=b'\x08\x00\x00\x00'+b'abcd';cs=icmpv4_checksum(msg);msg=msg[:2]+struct.pack('!H',cs)+msg[4:]
  with self.assertRaises(PacketError):verify_icmpv4(msg[:-1]+b'X')
 def test_mask_prefix(self):
  for p in range(33):self.assertEqual(prefix_length_from_mask(((1<<p)-1)<<(32-p)),p)
 def test_mask_noncontiguous(self):
  with self.assertRaises(PacketError):prefix_length_from_mask(0xff00ff00)
if __name__=='__main__':unittest.main()
