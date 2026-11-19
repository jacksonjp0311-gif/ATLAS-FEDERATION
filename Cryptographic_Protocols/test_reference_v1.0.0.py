"""Constructed cases, published external vectors and adversarial negatives."""
import hashlib
import hmac
import random
import unittest
from crypto_atlas import (
    hmac_sha256,hkdf_extract,hkdf_expand,hkdf_sha256,hkdf_expand_label,tls13_record_nonce,
    encode_fields,decode_fields,ReplayWindow,derive_directional_keys,AuthenticatedSession,
    AuthenticationError,tree_hash,inclusion_proof,verify_inclusion)

RFC5869_A1_PRK='077709362c2e32df0ddc3f0dc47bba6390b6c73bb50f9c3122ec844ad7c2b3e5'
RFC5869_A1_OKM='3cb25f25faacd57a90434f64d0362f2a2d2d0a90cf1a5a4c5db02d56ecc4c5bf34007208d5b887185865'
RFC5869_A3_PRK='19ef24a32c717b167f33a91d6f648bdf96596776afdb6377ac434c1c293ccb04'
RFC5869_A3_OKM='8da4e775a563c18f715f802a063c5a31b8a11f5c5ee1879ec3454e5f3c738d2d9d201395faa4b61a96c8'

class HMACTest(unittest.TestCase):
    def test_rfc4231_case_1(self):
        self.assertEqual(hmac_sha256(bytes.fromhex('0b'*20),b'Hi There').hex(),'b0344c61d8db38535ca8afceaf0bf12b881dc200c9833da726e9376c2e32cff7')
    def test_rfc4231_case_2(self):
        self.assertEqual(hmac_sha256(b'Jefe',b'what do ya want for nothing?').hex(),'5bdcc146bf60754e6a042426089575c75a003f089d2739839dec58b964ec3843')
    def test_rfc4231_case_3(self):
        self.assertEqual(hmac_sha256(bytes.fromhex('aa'*20),bytes.fromhex('dd'*50)).hex(),'773ea91e36800e46854db8ebd09181a72959098b3ef8c122d9635514ced565fe')
    def test_rfc4231_case_4(self):
        self.assertEqual(hmac_sha256(bytes(range(1,26)),bytes.fromhex('cd'*50)).hex(),'82558a389a443c0ea4cc819899f2083a85f0faa3e578f8077a2e3ff46729665b')
    def test_not_plain_sha256(self):self.assertNotEqual(hmac_sha256(b'k',b'm'),hashlib.sha256(b'k'+b'm').digest())
    def test_types(self):
        with self.assertRaises(TypeError):hmac_sha256('secret',b'payload')
        with self.assertRaises(TypeError):hmac_sha256(b'k',bytearray(b'payload'))
    def test_message_binding(self):self.assertNotEqual(hmac_sha256(b'k',b'hello'),hmac_sha256(b'k',b'hell0'))
    def test_key_binding(self):self.assertNotEqual(hmac_sha256(b'k',b'x'),hmac_sha256(b'j',b'x'))
    def test_empty_data(self):self.assertEqual(len(hmac_sha256(b'',b'')),32)

class HKDFTest(unittest.TestCase):
    def test_rfc5869_case_a1_prk(self):
        self.assertEqual(hkdf_extract(bytes(range(13)),b'\x0b'*22).hex(),RFC5869_A1_PRK)
    def test_rfc5869_case_a1_okm(self):
        self.assertEqual(hkdf_sha256(b'\x0b'*22,bytes(range(13)),bytes(range(240,250)),42).hex(),RFC5869_A1_OKM)
    def test_rfc5869_case_a3_prk(self):
        self.assertEqual(hkdf_extract(b'',b'\x0b'*22).hex(),RFC5869_A3_PRK)
    def test_rfc5869_case_a3_okm(self):
        self.assertEqual(hkdf_sha256(b'\x0b'*22,b'',b'',42).hex(),RFC5869_A3_OKM)
    def test_absent_salt_equivalent_zero_salt(self):self.assertEqual(hkdf_extract(None,b'ikm'),hkdf_extract(bytes(32),b'ikm'))
    def test_extract_domain(self):self.assertNotEqual(hkdf_extract(b'a',b'secret'),hkdf_extract(b'b',b'secret'))
    def test_expand_prefix(self):
        prk=hkdf_extract(b'salt',b'ikm')
        self.assertEqual(hkdf_expand(prk,b'purpose',32),hkdf_expand(prk,b'purpose',42)[:32])
    def test_expand_info_separation(self):
        prk=hkdf_extract(b'salt',b'ikm')
        self.assertNotEqual(hkdf_expand(prk,b'left',32),hkdf_expand(prk,b'right',32))
    def test_max_length(self):self.assertEqual(len(hkdf_expand(bytes(32),b'',255*32)),255*32)
    def test_zero_length(self):self.assertEqual(hkdf_expand(bytes(32),b'',0),b'')
    def test_length_overflow(self):
        with self.assertRaises(ValueError):hkdf_expand(bytes(32),b'',255*32+1)
    def test_short_prk(self):
        with self.assertRaises(ValueError):hkdf_expand(b'weak',b'info',32)
    def test_bool_length_rejected(self):
        with self.assertRaises(ValueError):hkdf_expand(bytes(32),b'',True)
    def test_tls13_label_independence(self):
        prk=bytes(range(32))
        self.assertNotEqual(hkdf_expand_label(prk,b'key',b'',16),hkdf_expand_label(prk,b'iv',b'',16))
    def test_tls13_label_context(self):
        self.assertNotEqual(hkdf_expand_label(bytes(32),b'key',b'a',16),hkdf_expand_label(bytes(32),b'key',b'b',16))
    def test_tls_label_length(self):
        with self.assertRaises(ValueError):hkdf_expand_label(bytes(32),b'a'*250,b'',32)
    def test_tls_label_long_context(self):
        with self.assertRaises(ValueError):hkdf_expand_label(bytes(32),b'a',b'x'*256,32)
    def test_tls_nonce_zero(self):self.assertEqual(tls13_record_nonce(bytes(range(12)),0),bytes(range(12)))
    def test_tls_nonce_is_xor_last_8_bytes(self):
        iv=b'\x01'*12; self.assertEqual(tls13_record_nonce(iv,1),b'\x01'*11+b'\x00')
    def test_tls_nonce_changes(self):self.assertNotEqual(tls13_record_nonce(bytes(12),1),tls13_record_nonce(bytes(12),2))
    def test_tls_nonce_wrap_rejected(self):
        with self.assertRaises(ValueError):tls13_record_nonce(bytes(12),2**64)
    def test_tls_nonce_iv_length(self):
        with self.assertRaises(ValueError):tls13_record_nonce(bytes(8),0)

class FramingTest(unittest.TestCase):
    def test_roundtrip(self):self.assertEqual(decode_fields(encode_fields(b'a',b'b',b'\x00',b'')),(b'a',b'b',b'\x00',b''))
    def test_disjoint_tuples(self):self.assertNotEqual(encode_fields(b'a',b'bc'),encode_fields(b'ab',b'c'))
    def test_empty_fields(self):self.assertEqual(decode_fields(encode_fields()),())
    def test_truncated_header(self):
        with self.assertRaises(ValueError):decode_fields(b'\x00')
    def test_truncated_data(self):
        with self.assertRaises(ValueError):decode_fields(encode_fields(b'abc')[:-1])
    def test_trailing(self):
        with self.assertRaises(ValueError):decode_fields(encode_fields(b'abc')+b'junk')
    def test_huge_len(self):
        with self.assertRaises(ValueError):decode_fields(b'\x00\x01\xff\xff\xff\xff')
    def test_too_many_fields(self):
        with self.assertRaises(ValueError):encode_fields(*([b'a']*33))
    def test_wrong_type(self):
        with self.assertRaises(TypeError):encode_fields(b'a','b')

class ReplayTest(unittest.TestCase):
    def test_first(self):self.assertTrue(ReplayWindow().accept(0))
    def test_duplicate(self):
        w=ReplayWindow(); self.assertTrue(w.accept(3)); self.assertFalse(w.accept(3))
    def test_out_of_order(self):
        w=ReplayWindow(width=8)
        self.assertTrue(w.accept(7));self.assertTrue(w.accept(6));self.assertTrue(w.accept(5))
    def test_out_of_window(self):
        w=ReplayWindow(width=8);w.accept(20);self.assertFalse(w.accept(12))
    def test_shift(self):
        w=ReplayWindow(width=8);w.accept(1);w.accept(100);self.assertEqual(w.seen,1)
    def test_boolean_seq(self):
        with self.assertRaises(ValueError):ReplayWindow().accept(True)
    def test_negative(self):
        with self.assertRaises(ValueError):ReplayWindow().accept(-1)
    def test_width_invalid(self):
        with self.assertRaises(ValueError):ReplayWindow(width=0)

class ChannelTest(unittest.TestCase):
    def make(self):
        return (AuthenticatedSession(bytes(range(32)),b'mission-1',b'reader',b'archive','client'),
                AuthenticatedSession(bytes(range(32)),b'mission-1',b'reader',b'archive','server'))
    def test_c2s(self):
        c,s=self.make();self.assertEqual(s.receive(c.send(b'original atlas')),b'original atlas')
    def test_s2c(self):
        c,s=self.make();self.assertEqual(c.receive(s.send(b'ack')),b'ack')
    def test_different_direction_keys(self):
        c,_=self.make();self.assertNotEqual(c.c2s,c.s2c)
    def test_replay_rejected(self):
        c,s=self.make();p=c.send(b'one');s.receive(p)
        with self.assertRaises(AuthenticationError):s.receive(p)
    def test_payload_tamper_rejected(self):
        c,s=self.make();f=c.send(b'one')
        f=f[:-33]+bytes([f[-33]^1])+f[-32:]
        with self.assertRaises(AuthenticationError):s.receive(f)
    def test_corrupt_tag_rejected(self):
        c,s=self.make();f=c.send(b'one')
        with self.assertRaises(AuthenticationError):s.receive(f[:-1]+bytes([f[-1]^1]))
    def test_context_mismatch(self):
        c,_=self.make()
        bad=AuthenticatedSession(bytes(range(32)),b'mission-2',b'reader',b'archive','server')
        with self.assertRaises(AuthenticationError):bad.receive(c.send(b'one'))
    def test_identity_mismatch(self):
        c,_=self.make()
        bad=AuthenticatedSession(bytes(range(32)),b'mission-1',b'reader',b'another','server')
        with self.assertRaises(AuthenticationError):bad.receive(c.send(b'one'))
    def test_wrong_psk(self):
        c,_=self.make()
        bad=AuthenticatedSession(b'x'*32,b'mission-1',b'reader',b'archive','server')
        with self.assertRaises(AuthenticationError):bad.receive(c.send(b'one'))
    def test_failed_auth_does_not_advance_window(self):
        c,s=self.make();f=c.send(b'one')
        with self.assertRaises(AuthenticationError):s.receive(f[:-1]+bytes([f[-1]^1]))
        self.assertEqual(s.receive(f),b'one')
    def test_cross_role_reflection_fails(self):
        c,_=self.make()
        with self.assertRaises(AuthenticationError):c.receive(c.send(b'reflect'))
    def test_direction_separation_on_context(self):
        a=derive_directional_keys(bytes(range(32)),b'x',b'a',b'b')
        b=derive_directional_keys(bytes(range(32)),b'y',b'a',b'b')
        self.assertNotEqual(a,b)
    def test_weak_key_reference_rejected(self):
        with self.assertRaises(ValueError):derive_directional_keys(b'x',b'c',b'a',b'b')
    def test_equal_id_reference_rejected(self):
        with self.assertRaises(ValueError):derive_directional_keys(bytes(32),b'c',b'a',b'a')
    def test_send_exhaustion(self):
        c,_=self.make();c.outgoing_sequence=2**64-1
        with self.assertRaises(ValueError):c.send(b'data')
    def test_two_frames(self):
        c,s=self.make();self.assertEqual(s.receive(c.send(b'one')),b'one');self.assertEqual(s.receive(c.send(b'two')),b'two')

class MerkleTest(unittest.TestCase):
    def test_empty(self):self.assertEqual(tree_hash([]),hashlib.sha256(b'').digest())
    def test_leaf_prefix(self):self.assertEqual(tree_hash([b'a']),hashlib.sha256(b'\x00a').digest())
    def test_two_leaves(self):
        a=hashlib.sha256(b'\x00a').digest();b=hashlib.sha256(b'\x00b').digest()
        self.assertEqual(tree_hash([b'a',b'b']),hashlib.sha256(b'\x01'+a+b).digest())
    def test_three_leaves_not_wrong_split(self):
        a=tree_hash([b'a',b'b']);b=tree_hash([b'c'])
        self.assertEqual(tree_hash([b'a',b'b',b'c']),hashlib.sha256(b'\x01'+a+b).digest())
    def test_root_changes_if_order_reversed(self):self.assertNotEqual(tree_hash([b'a',b'b']),tree_hash([b'b',b'a']))
    def test_all_proofs(self):
        for n in range(1,32):
            leaves=[bytes([i]) for i in range(n)]
            root=tree_hash(leaves)
            for i in range(n):
                self.assertTrue(verify_inclusion(leaves[i],i,n,inclusion_proof(leaves,i),root))
    def test_tamper_leaf(self):
        leaves=[b'a',b'b',b'c']; root=tree_hash(leaves)
        self.assertFalse(verify_inclusion(b'wrong',0,3,inclusion_proof(leaves,0),root))
    def test_tamper_proof(self):
        leaves=[b'a',b'b',b'c']; root=tree_hash(leaves)
        proof=list(inclusion_proof(leaves,1));proof[0]=bytes(32)
        self.assertFalse(verify_inclusion(leaves[1],1,3,tuple(proof),root))
    def test_extra_proof(self):
        leaves=[b'a',b'b'];root=tree_hash(leaves)
        self.assertFalse(verify_inclusion(leaves[0],0,2,inclusion_proof(leaves,0)+(bytes(32),),root))
    def test_bad_index(self):
        with self.assertRaises(ValueError):inclusion_proof([b'a'],1)
    def test_wrong_root(self):self.assertFalse(verify_inclusion(b'a',0,1,(),bytes(32)))

if __name__=='__main__':unittest.main()
