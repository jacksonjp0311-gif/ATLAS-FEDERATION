import unittest,random,itertools,math
from language_atlas.models import LanguageModelError
from language_atlas.advanced import *
from language_atlas.advanced_cases import advanced_casebook

class AlignmentTests(unittest.TestCase):
    def test_casebook(self):self.assertEqual(advanced_casebook()['status'],'passed');self.assertEqual(advanced_casebook()['count'],11)
    def test_identity(self):self.assertEqual(aligned_edit_distance(['a','b'],['a','b'])['distance'],0)
    def test_insert(self):self.assertEqual(aligned_edit_distance([],['a','b'])['counts']['insert'],2)
    def test_delete(self):self.assertEqual(aligned_edit_distance(['a','b'],[])['counts']['delete'],2)
    def test_undefined_empty_reference_rate(self):self.assertIsNone(aligned_edit_distance([],['a'])['reference_normalized_error_rate'])
    def test_unit_substitute(self):self.assertEqual(aligned_edit_distance(['a'],['b'])['distance'],1)
    def test_symmetry(self):
        r=random.Random(314)
        for _ in range(80):
            a=[r.choice('abc') for _ in range(r.randrange(9))];b=[r.choice('abc') for _ in range(r.randrange(9))]
            self.assertEqual(aligned_edit_distance(a,b)['distance'],aligned_edit_distance(b,a)['distance'])
    def test_operations_reconstruct(self):
        a=['one','two','three'];b=['one','four','three','extra']
        result=aligned_edit_distance(a,b);observed=[x['target'] for x in result['operations'] if x['target'] is not None]
        self.assertEqual(observed,b)
    def test_bad_token(self):
        with self.assertRaises(LanguageModelError):aligned_edit_distance([None],['a'])
    def test_resource_cap(self):
        with self.assertRaises(LanguageModelError):aligned_edit_distance(['a']*200,['b']*200)

class BLEUTests(unittest.TestCase):
    def score(self,c,r,order=1):return corpus_bleu([c],[[r]],order)
    def test_exact_match(self):self.assertEqual(self.score(['a','b'],['a','b'],2)['bleu_unsmoothed'],1)
    def test_mismatch_zero(self):self.assertEqual(self.score(['a'],['x'])['bleu_unsmoothed'],0)
    def test_ref_longer_penalty(self):
        r=self.score(['a','b'],['a','b','c','d'])
        self.assertAlmostEqual(r['brevity_penalty'],math.exp(1-4/2))
    def test_multi_ref(self):
        r=corpus_bleu([['we','work']],[[['we','study'],['we','work']]],2)
        self.assertEqual(r['bleu_unsmoothed'],1)
    def test_order_zero(self):
        with self.assertRaises(LanguageModelError):self.score(['a'],['a'],0)
    def test_no_smoothing(self):self.assertEqual(self.score(['a','b'],['a','b'],4)['bleu_unsmoothed'],0)
    def test_empty_corpus_sentence(self):
        r=self.score([],['a']);self.assertEqual(r['bleu_unsmoothed'],0)
    def test_cannot_claim_semantic_quality(self):self.assertFalse(self.score(['a'],['a'])['semantic_translation_quality_verified'])
    def test_invalid_empty_ref_collection(self):
        with self.assertRaises(LanguageModelError):corpus_bleu([['a']],[[]])

class PCFGTests(unittest.TestCase):
    def grammar(self):return ([{'lhs':'S','token':'x','p':.25},{'lhs':'A','token':'x','p':1},{'lhs':'B','token':'y','p':1}],
             [{'lhs':'S','left':'A','right':'B','p':.75}])
    def test_lexical(self):
        lex,bi=self.grammar();r=pcfg_inside(['x'],lex,bi);self.assertAlmostEqual(r['sentence_probability'],.25)
    def test_two_tokens(self):
        lex,bi=self.grammar();r=pcfg_inside(['x','y'],lex,bi);self.assertAlmostEqual(r['sentence_probability'],.75)
    def test_empty_rejected(self):
        lex,bi=self.grammar()
        with self.assertRaises(LanguageModelError):pcfg_inside([],lex,bi)
    def test_bad_lhs_mass(self):
        lex,bi=self.grammar();lex[0]['p']=.3
        with self.assertRaises(LanguageModelError):pcfg_inside(['x'],lex,bi)
    def test_undefined_nonterminals_not_produced(self):
        lex=[{'lhs':'S','token':'a','p':1}];r=pcfg_inside(['b'],lex,[])
        self.assertEqual(r['sentence_probability'],0)
    def test_duplicate_rule(self):
        lex=[{'lhs':'S','token':'a','p':1}]
        with self.assertRaises(LanguageModelError):pcfg_inside(['a'],lex*2,[])
    def test_viterbi_never_exceeds_total(self):
        lex,bi=self.grammar()
        for t in (['x'],['x','y']):
            a=pcfg_inside(t,lex,bi);self.assertLessEqual(a['best_derivation_probability'],a['sentence_probability']+1e-12)
    def test_outside_data_cannot_be_inferred(self):self.assertFalse(pcfg_inside(['z'],[{'lhs':'S','token':'x','p':1}],[])['accepted_by_supplied_grammar'])

class TypologyTests(unittest.TestCase):
    def base(self):return [{'language_id':'L1','family_id':'A','area_id':'x','feature':True},
        {'language_id':'L2','family_id':'A','area_id':'x','feature':True},
        {'language_id':'L3','family_id':'B','area_id':'y','feature':False}]
    def test_family_bias(self):
        a=typology_by_family(self.base());self.assertAlmostEqual(a['naive_known_fraction'],2/3)
        self.assertAlmostEqual(a['equal_family_mean'],.5)
    def test_unknown_not_false(self):
        x=self.base();x[-1]['feature']=None;r=typology_by_family(x)
        self.assertEqual(r['known_values'],2);self.assertEqual(r['unknown_values'],1)
    def test_all_missing(self):
        x=self.base()
        for r in x:r['feature']=None
        y=typology_by_family(x);self.assertIsNone(y['naive_known_fraction']);self.assertIsNone(y['equal_family_mean'])
    def test_duplicate_language(self):
        x=self.base();x[-1]['language_id']='L1'
        with self.assertRaises(LanguageModelError):typology_by_family(x)
    def test_no_random_sample_claim(self):self.assertFalse(typology_by_family(self.base())['genealogical_independence_proved'])
    def test_bool_only(self):
        x=self.base();x[0]['feature']=1
        with self.assertRaises(LanguageModelError):typology_by_family(x)

class HistoricalTests(unittest.TestCase):
    def row(self):return {'item_id':'t','language_a':'A','language_b':'B','segments_a':['p','a'],
           'segments_b':['f','a'],'source_id':'toy'}
    def test_correspondence(self):self.assertEqual(aligned_sound_correspondences([self.row()])['aligned_pairs_counted'],2)
    def test_cognacy_not_proven(self):self.assertFalse(aligned_sound_correspondences([self.row()])['cognacy_proven'])
    def test_unaligned_rejected(self):
        x=self.row();x['segments_b']=['f']
        with self.assertRaises(LanguageModelError):aligned_sound_correspondences([x])
    def test_double_gap(self):
        x=self.row();x['segments_a']=['-'];x['segments_b']=['-']
        with self.assertRaises(LanguageModelError):aligned_sound_correspondences([x])
    def test_duplicate(self):
        x=self.row()
        with self.assertRaises(LanguageModelError):aligned_sound_correspondences([x,x])

class CommunityRightsTests(unittest.TestCase):
    def row(self):return {'record_id':'R1','language_id':'L','source_id':'s','community_permission':'documented',
      'speaker_permission':'documented','access':'public','original_bytes_present':True,'raw_sha256':'a'*64,'license':'CC-BY'}
    def test_record_only_eligible(self):
        r=documentation_rights_audit([self.row()]);self.assertFalse(r['automatically_publishable'])
    def test_community_denied(self):
        r=self.row();r['community_permission']='denied'
        self.assertEqual(documentation_rights_audit([r])['records'][0]['accession_status'],'do_not_release')
    def test_speaker_denied(self):
        r=self.row();r['speaker_permission']='denied'
        self.assertEqual(documentation_rights_audit([r])['records'][0]['accession_status'],'do_not_release')
    def test_unverified_consent(self):
        r=self.row();r['speaker_permission']='unknown'
        self.assertEqual(documentation_rights_audit([r])['records'][0]['accession_status'],'consent_evidence_required')
    def test_restricted_blocks(self):
        r=self.row();r['access']='restricted'
        self.assertEqual(documentation_rights_audit([r])['records'][0]['accession_status'],'access_review_required')
    def test_bytes_required(self):
        r=self.row();r['original_bytes_present']=False;r['raw_sha256']=None
        self.assertEqual(documentation_rights_audit([r])['records'][0]['accession_status'],'primary_bytes_and_hash_required')
    def test_invalid_sha(self):
        r=self.row();r['raw_sha256']='nothex'
        with self.assertRaises(LanguageModelError):documentation_rights_audit([r])
    def test_digest_does_not_prove_origin(self):self.assertFalse(documentation_rights_audit([self.row()])['primary_bytes_rehashed'])

class MultimodalTests(unittest.TestCase):
    def row(self,e,t,a,b):return {'event_id':e,'tier':t,'start_ms':a,'end_ms':b,'label':'test'}
    def test_cross_tier_simultaneous(self):
        r=multimodal_tier_audit([self.row('one','hands',0,10),self.row('two','face',5,15)])
        self.assertTrue(r['simultaneous_channels_permitted'])
        self.assertEqual(sum(r['overlaps_within_tier'].values()),0)
    def test_within_tier_overlap_reported(self):
        r=multimodal_tier_audit([self.row('one','hands',0,10),self.row('two','hands',5,15)])
        self.assertEqual(r['overlaps_within_tier']['hands'],1)
    def test_zero_length_rejected(self):
        with self.assertRaises(LanguageModelError):multimodal_tier_audit([self.row('one','hands',0,0)])
    def test_duplicate_event_rejected(self):
        x=self.row('one','hands',0,10)
        with self.assertRaises(LanguageModelError):multimodal_tier_audit([x,x])
    def test_no_media_claim(self):self.assertFalse(multimodal_tier_audit([self.row('one','hands',0,1)])['original_media_acquired'])
