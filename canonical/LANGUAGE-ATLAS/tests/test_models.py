"""Tests for explicitly restricted, offline Linguistics teaching examples."""
import unittest
import math
import random
import unicodedata
from language_atlas.models import *
from language_atlas.cases import *

class UnicodeTests(unittest.TestCase):
    def test_nfc(self):self.assertEqual(unicode_profile('e\u0301')['nfc'],'é')
    def test_nfkc_loss(self):self.assertTrue(unicode_profile('②')['compatibility_mapping_changed'])
    def test_codepoints_not_graphemes(self):self.assertIsNone(unicode_profile('👩\u200d💻')['grapheme_cluster_count'])
    def test_nfc_normalized(self):self.assertFalse(unicode_profile('é')['nfc_changed'])
    def test_invalid_surrogate(self):
        with self.assertRaises(LanguageModelError):unicode_profile('\ud800')
    def test_unicode_empty(self):self.assertEqual(unicode_profile('')['code_point_count'],0)
    def test_roundtrip_nonlatin(self):self.assertTrue(utf8_decode_strict('ภาษาไทย'.encode('utf-8'))['roundtrip'])
    def test_invalid_utf8(self):
        with self.assertRaises(LanguageModelError):utf8_decode_strict(b'\xf0\x28\x8c\x28')
    def test_replacement_not_silent(self):
        with self.assertRaises(LanguageModelError):utf8_decode_strict(b'\xff')
    def test_not_str(self):
        with self.assertRaises(LanguageModelError):unicode_profile(b'wrong')
    def test_explicit_unicode_version(self):self.assertEqual(unicode_profile('x')['unicode_database_version'],unicodedata.unidata_version)

class SegmentationTests(unittest.TestCase):
    def test_ambiguity(self):self.assertEqual(finite_lexicon_segment('aba',{'a':1,'b':1,'ab':0,'ba':0})['count_listed'],3)
    def test_lexicon_tie(self):self.assertEqual(finite_lexicon_segment('ab',{'ab':0,'a':0,'b':0})['count_listed'],2)
    def test_unknown_word(self):self.assertEqual(finite_lexicon_segment('xyz',{'a':1})['count_listed'],0)
    def test_cap_saturated(self):self.assertTrue(finite_lexicon_segment('aaaaa',{'a':1,'aa':1},cap=2)['saturated'])
    def test_no_exact_count_on_cap(self):self.assertFalse(finite_lexicon_segment('aaaaa',{'a':1,'aa':1},cap=2)['complete_count_proven'])
    def test_empty_token_reject(self):
        with self.assertRaises(LanguageModelError):finite_lexicon_segment('aa',{'':1})
    def test_negative_cost_reject(self):
        with self.assertRaises(LanguageModelError):finite_lexicon_segment('a',{'a':-1})
    def test_lexicon_choice_not_universal(self):self.assertIn('not',finite_lexicon_segment('x',{'x':0})['limitations'][2])

class MorphologyTests(unittest.TestCase):
    def test_ambiguous(self):self.assertEqual(len(lexical_morphology('flies',morphology_fixture())['analyses']),2)
    def test_unknown(self):self.assertEqual(lexical_morphology('geese',morphology_fixture())['status'],'unknown_not_analyzed')
    def test_duplicate_reject(self):
        with self.assertRaises(LanguageModelError):lexical_morphology('flies',morphology_fixture()*2)
    def test_no_features_inferred(self):self.assertFalse(lexical_morphology('flies',morphology_fixture())['disambiguated_by_context'])
    def test_feature_voice(self):
        inv={'p':{'voice':'-','place':'labial'},'b':{'voice':'+','place':'labial'}}
        self.assertEqual(phoneme_contrast(inv,'p','b')['differences'],['voice'])
    def test_incompatible_dimensions(self):
        with self.assertRaises(LanguageModelError):phoneme_contrast({'a':{'x':'1'},'b':{'y':'2'}},'a','b')

class SyntaxTests(unittest.TestCase):
    def test_ambiguity(self):
        lx,gr=grammar_fixture();r=cyk_parse('robots see astronomers with telescopes'.split(),lx,gr)
        self.assertTrue(r['accepted']);self.assertEqual(r['parse_count'],2)
    def test_reject(self):
        lx,gr=grammar_fixture();self.assertFalse(cyk_parse('robots robots'.split(),lx,gr)['accepted'])
    def test_unknown_word(self):
        lx,gr=grammar_fixture();self.assertFalse(cyk_parse('anyone see robots'.split(),lx,gr)['accepted'])
    def test_duplicate_rule(self):
        lx,gr=grammar_fixture()
        with self.assertRaises(LanguageModelError):cyk_parse(['robots'],lx,gr+gr)
    def test_count_saturation(self):
        lx,gr=grammar_fixture();r=cyk_parse('robots see astronomers with telescopes'.split(),lx,gr,limit=1)
        self.assertTrue(r['saturated']);self.assertFalse(r['count_is_exact'])
    def test_conllu_toy(self):self.assertEqual(validate_conllu_basic(conllu_fixture())['sentence_count'],1)
    def test_conllu_duplicate_root(self):
        with self.assertRaises(LanguageModelError):validate_conllu_basic(conllu_fixture().replace('2\tpunct','0\tpunct'))
    def test_conllu_self_loop(self):
        with self.assertRaises(LanguageModelError):validate_conllu_basic(conllu_fixture().replace('2\tpunct','3\tpunct'))
    def test_conllu_crlf(self):
        with self.assertRaises(LanguageModelError):validate_conllu_basic(conllu_fixture().replace('\n','\r\n'))
    def test_conllu_unknown_head(self):
        with self.assertRaises(LanguageModelError):validate_conllu_basic(conllu_fixture().replace('2\tpunct','10\tpunct'))
    def test_conllu_no_full_ud(self):self.assertFalse(validate_conllu_basic(conllu_fixture())['conllu_full_conformance_certified'])
    def test_conllu_not_9_fields(self):
        with self.assertRaises(LanguageModelError):validate_conllu_basic('1\tx\t_\t_\t_\t_\t0\troot\t_\n\n')

class SemanticsTests(unittest.TestCase):
    def test_false_quantifier(self):
        f={'op':'forall','var':'?x','body':{'op':'pred','name':'scientist','args':['?x']}}
        self.assertEqual(finite_truth(f,model_fixture())['truth'],'false')
    def test_unknown_existence(self):
        f={'op':'exists','var':'?x','body':{'op':'pred','name':'reads','args':['?x','ada']}}
        self.assertEqual(finite_truth(f,model_fixture())['truth'],'unknown')
    def test_true_exist(self):
        f={'op':'exists','var':'?x','body':{'op':'pred','name':'scientist','args':['?x']}}
        self.assertEqual(finite_truth(f,model_fixture())['truth'],'true')
    def test_not_unknown(self):
        f={'op':'not','arg':{'op':'pred','name':'unreported','args':['ada']}}
        self.assertEqual(finite_truth(f,model_fixture())['truth'],'unknown')
    def test_false_dominates_unknown_and(self):
        f={'op':'and','args':[{'op':'pred','name':'scientist','args':['bea']},{'op':'pred','name':'unreported','args':['ada']} ]}
        self.assertEqual(finite_truth(f,model_fixture())['truth'],'false')
    def test_true_dominates_unknown_or(self):
        f={'op':'or','args':[{'op':'pred','name':'scientist','args':['ada']},{'op':'pred','name':'unreported','args':['ada']} ]}
        self.assertEqual(finite_truth(f,model_fixture())['truth'],'true')
    def test_unsupported_op(self):
        with self.assertRaises(LanguageModelError):finite_truth({'op':'execute','arg':'no'},model_fixture())
    def test_incompatible_truth_assignments(self):
        bad=model_fixture();bad['predicates']['scientist']['false']=[['ada']]
        with self.assertRaises(LanguageModelError):finite_truth({'op':'pred','name':'scientist','args':['ada']},bad)
    def test_unknown_not_false(self):self.assertFalse(finite_truth({'op':'pred','name':'new','args':['ada']},model_fixture())['world_truth_grounded'])

class StatisticalTests(unittest.TestCase):
    def setUp(self):self.bg=train_bigram([{'id':'a','tokens':['cat','sat']},{'id':'b','tokens':['dog','sat']}])
    def test_train_count(self):self.assertEqual(self.bg['counts']['<s>\tcat'],1)
    def test_smoothing_positive(self):self.assertGreater(score_bigram(self.bg,{'id':'test','tokens':['cat','sat']})['perplexity'],1)
    def test_train_id_refusal(self):
        with self.assertRaises(LanguageModelError):score_bigram(self.bg,{'id':'a','tokens':['cat','sat']})
    def test_oov(self):self.assertTrue(math.isfinite(score_bigram(self.bg,{'id':'unknown','tokens':['unseen']})['perplexity']))
    def test_duplicate_train(self):
        with self.assertRaises(LanguageModelError):train_bigram([{'id':'a','tokens':['cat']},{'id':'a','tokens':['dog']}])
    def test_reserved_token_refuse(self):
        with self.assertRaises(LanguageModelError):train_bigram([{'id':'a','tokens':['<UNK>']}])
    def test_exact_text_leakage(self):
        x=corpus_leakage_report([{'id':'train','text':'e\u0301'}],[{'id':'test','text':'é'}]);self.assertFalse(x['clean_under_exact_tests'])
    def test_same_id_leakage(self):
        x=corpus_leakage_report([{'id':'same','text':'a'}],[{'id':'same','text':'b'}]);self.assertEqual(x['overlapping_ids'],['same'])
    def test_clean_doesnt_prove_fairness(self):self.assertFalse(corpus_leakage_report([{'id':'a','text':'foo'}],[{'id':'b','text':'bar'}])['semantic_leakage_ruled_out'])
    def test_bcp47_skeleton(self):self.assertEqual(language_tag_profile('sr-latn-rs')['canonical_casing_only'],'sr-Latn-RS')
    def test_bcp47_extension_not_claimed(self):
        with self.assertRaises(LanguageModelError):language_tag_profile('en-US-u-ca-buddhist')
    def test_not_iana(self):self.assertFalse(language_tag_profile('en')['registry_validated'])

class CasebookTests(unittest.TestCase):
    def test_constructed_cases(self):self.assertEqual(casebook()['case_count'],19)
    def test_no_human_subjects(self):self.assertFalse(casebook()['human_subjects_tested'])
    def test_no_corpus(self):self.assertFalse(casebook()['real_multilingual_corpus_acquired'])

if __name__=='__main__':unittest.main()
