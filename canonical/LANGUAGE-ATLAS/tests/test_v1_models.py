import unittest,random,hashlib,math
from language_atlas.v1_models import *
from language_atlas.v1_cases import casebook_v1
from language_atlas.models import LanguageModelError

class FiniteLanguages(unittest.TestCase):
 def graph(self,tokens,transitions=None):
  trs=transitions if transitions is not None else [{'from':'A','symbol':'x','to':'B'},{'from':'B','symbol':'y','to':'C'}]
  return finite_acceptor(tokens,['A','B','C'],'A',['C'],trs)
 def test_casebook(self):self.assertEqual(casebook_v1()['status'],'passed');self.assertEqual(casebook_v1()['count'],11)
 def test_accept(self):self.assertTrue(self.graph(['x','y'])['accepted_by_declared_machine'])
 def test_reject(self):self.assertFalse(self.graph(['y','x'])['accepted_by_declared_machine'])
 def test_epsilon(self):
  x=self.graph(['y'],[{'from':'A','symbol':None,'to':'B'},{'from':'B','symbol':'y','to':'C'}]);self.assertTrue(x['accepted_by_declared_machine'])
 def test_epsilon_cycle_terminates(self):
  t=[{'from':'A','symbol':None,'to':'B'},{'from':'B','symbol':None,'to':'A'},{'from':'B','symbol':'y','to':'C'}]
  self.assertTrue(self.graph(['y'],t)['accepted_by_declared_machine'])
 def test_duplicate_transition_rejected(self):
  t=[{'from':'A','symbol':'x','to':'B'}]*2
  with self.assertRaises(LanguageModelError):self.graph(['x'],t)
 def test_unknown_state(self):
  with self.assertRaises(LanguageModelError):self.graph(['x'],[{'from':'A','symbol':'x','to':'Z'}])
 def test_empty_accept(self):
  self.assertTrue(finite_acceptor([],['A'],'A',['A'],[])['accepted_by_declared_machine'])
 def test_invalid_token(self):
  with self.assertRaises(LanguageModelError):self.graph([''])
 def test_nondeterminism(self):
  t=[{'from':'A','symbol':'x','to':'B'},{'from':'A','symbol':'x','to':'C'}]
  self.assertTrue(self.graph(['x'],t)['accepted_by_declared_machine'])

class Semantics(unittest.TestCase):
 def test_scopes_differ(self):
  o=quantifier_scope_contrast(['a','b'],['x','y'],[['a','x'],['b','y']],[['a','y'],['b','x']]);self.assertEqual(o['forall_agent_exists_object'],'true');self.assertEqual(o['exists_object_forall_agent'],'false')
 def test_missing_is_unknown(self):self.assertEqual(quantifier_scope_contrast(['a'],['x'],[],[])['forall_agent_exists_object'],'unknown')
 def test_false_for_each(self):self.assertEqual(quantifier_scope_contrast(['a'],['x'],[],[['a','x']])['forall_agent_exists_object'],'false')
 def test_global_true(self):self.assertEqual(quantifier_scope_contrast(['a','b'],['x'],[['a','x'],['b','x']],[])['exists_object_forall_agent'],'true')
 def test_conflict_denied(self):
  with self.assertRaises(LanguageModelError):quantifier_scope_contrast(['a'],['x'],[['a','x']],[['a','x']])
 def test_unknown_relation_entity(self):
  with self.assertRaises(LanguageModelError):quantifier_scope_contrast(['a'],['x'],[['b','x']],[])
 def test_duplicate_fact(self):
  with self.assertRaises(LanguageModelError):quantifier_scope_contrast(['a'],['x'],[['a','x'],['a','x']],[])
 def test_random_matches_simple_two_valued(self):
  rng=random.Random(77)
  for _ in range(130):
   agents=['a','b','c'];objs=['x','y'];truth={(a,b):bool(rng.getrandbits(1)) for a in agents for b in objs}
   true=[list(p) for p,v in truth.items() if v];false=[list(p) for p,v in truth.items() if not v]
   out=quantifier_scope_contrast(agents,objs,true,false)
   self.assertEqual(out['forall_agent_exists_object'],str(all(any(truth[a,b] for b in objs) for a in agents)).lower())
   self.assertEqual(out['exists_object_forall_agent'],str(any(all(truth[a,b] for a in agents) for b in objs)).lower())

class SoundAndText(unittest.TestCase):
 def test_weighted(self):
  o=weighted_segment_alignment(['p','a'],['f','a'],[{'source':'p','target':'f','cost':.3}]);self.assertAlmostEqual(o['minimum_cost'],.3)
 def test_weighted_insert(self):self.assertEqual(weighted_segment_alignment([],['x'],[],insert_cost=2)['minimum_cost'],2)
 def test_weighted_delete(self):self.assertEqual(weighted_segment_alignment(['x'],[],[],delete_cost=3)['minimum_cost'],3)
 def test_weighted_empty(self):self.assertEqual(weighted_segment_alignment([],[],[])['minimum_cost'],0)
 def test_bad_cost(self):
  with self.assertRaises(LanguageModelError):weighted_segment_alignment(['a'],['b'],[],default_substitute_cost=-1)
 def test_duplicate_rule_cost(self):
  a={'source':'a','target':'b','cost':1}
  with self.assertRaises(LanguageModelError):weighted_segment_alignment(['a'],['b'],[a,a])
 def test_alignment_cost_witness(self):
  rng=random.Random(65)
  for _ in range(150):
   src=[rng.choice(['a','b','c']) for _ in range(rng.randrange(7))];ref=[rng.choice(['a','b','c']) for _ in range(rng.randrange(7))]
   r=weighted_segment_alignment(src,ref,[],insert_cost=1,delete_cost=1,default_substitute_cost=1)
   self.assertEqual(r['minimum_cost'],sum(op['cost'] for op in r['operations']))
 def test_sound_stage(self):
  r=ordered_sound_changes(['p','a','t'],[{'id':'r','from':'p','to':'f','left':None,'right':'a'}]);self.assertEqual(r['output'],['f','a','t'])
 def test_simultaneous(self):
  r=ordered_sound_changes(['a','a'],[{'id':'r','from':'a','to':'b','left':None,'right':'a'}]);self.assertEqual(r['output'],['b','a'])
 def test_order_matters(self):
  a={'id':'1','from':'a','to':'b','left':None,'right':None};b={'id':'2','from':'b','to':'c','left':None,'right':None}
  self.assertNotEqual(ordered_sound_changes(['a'],[a,b])['output'],ordered_sound_changes(['a'],[b,a])['output'])
 def test_duplicate_stage_id(self):
  r={'id':'1','from':'a','to':'b','left':None,'right':None}
  with self.assertRaises(LanguageModelError):ordered_sound_changes(['a'],[r,r])
 def test_ngram_perfect(self):self.assertAlmostEqual(bounded_character_ngram_overlap('abc','abc',max_order=3)['score'],1.)
 def test_ngram_different(self):self.assertEqual(bounded_character_ngram_overlap('abc','xyz',max_order=2)['score'],0)
 def test_ngram_codepoint(self):
  self.assertLess(bounded_character_ngram_overlap('cafe\u0301','café',max_order=2)['score'],1)
 def test_ngram_empty_is_unknown(self):self.assertIsNone(bounded_character_ngram_overlap('','')['score'])
 def test_ngram_invalid_beta(self):
  with self.assertRaises(LanguageModelError):bounded_character_ngram_overlap('x','x',beta=0)
 def test_unicode_metadata(self):
  self.assertEqual(unicodedata.normalize('NFC','cafe\u0301'),'café')

class DocumentEthics(unittest.TestCase):
 def packet(self,**kw):
  blob=b'original fictional test';d={'document_id':'id','language_id':'toy','source_id':'author','community_permission':'documented',
    'speaker_permission':'documented','visibility':'public','declared_license':'author-fixture',
    'expected_sha256':hashlib.sha256(blob).hexdigest(),'reviewer_id':'r'};d.update(kw);return d,blob
 def test_eligible_only_external(self):
  a,b=self.packet();v=review_language_document(a,b);self.assertEqual(v['decision'],'eligible_for_external_rights_review_only');self.assertFalse(v['automatically_publishable'])
 def test_denied(self):
  a,b=self.packet(community_permission='denied');self.assertEqual(review_language_document(a,b)['decision'],'do_not_distribute')
 def test_restricted(self):
  a,b=self.packet(visibility='restricted');self.assertEqual(review_language_document(a,b)['decision'],'access_restricted_do_not_publish')
 def test_unknown_permission(self):
  a,b=self.packet(speaker_permission='unknown');self.assertEqual(review_language_document(a,b)['decision'],'permission_unresolved')
 def test_missing_source(self):
  a,b=self.packet();self.assertEqual(review_language_document(a,None)['decision'],'source_bytes_or_digest_missing')
 def test_wrong_hash(self):
  a,b=self.packet();self.assertEqual(review_language_document(a,b'other')['decision'],'byte_integrity_mismatch')
 def test_no_automatic_publish(self):
  a,b=self.packet();v=review_language_document(a,b);self.assertFalse(v['community_consent_authenticated'])
 def test_input_key_rejected(self):
  a,b=self.packet();a['execute_tool']='yes'
  with self.assertRaises(LanguageModelError):review_language_document(a,b)
 def test_empty_license(self):
  a,b=self.packet(declared_license='');self.assertEqual(review_language_document(a,b)['decision'],'license_unresolved')
 def test_bytes_limit(self):
  a,b=self.packet()
  with self.assertRaises(LanguageModelError):review_language_document(a,b'x'*2_000_001)
 def test_malformed_digest(self):
  a,b=self.packet(expected_sha256='x')
  with self.assertRaises(LanguageModelError):review_language_document(a,b)
if __name__=='__main__':unittest.main()
