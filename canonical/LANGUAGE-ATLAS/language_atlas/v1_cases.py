"""Author-created Language Atlas v1 cases. No speakers or authentic corpora."""
from hashlib import sha256
from .v1_models import *
from .models import LanguageModelError


def casebook_v1():
    cases=[]
    def add(name,result,valid):
        cases.append({'id':name,'passed':bool(valid),'origin':'original_constructed_fixture',
                      'result':result,'independent_speaker_validation':False})
    graph=finite_acceptor(['a','b'],['q0','q1','q2'],'q0',['q2'],[
      {'from':'q0','symbol':'a','to':'q1'},{'from':'q1','symbol':'b','to':'q2'}])
    add('regular_language_acceptance',graph,graph['accepted_by_declared_machine'])
    no=finite_acceptor(['b','a'],['q0','q1','q2'],'q0',['q2'],[
      {'from':'q0','symbol':'a','to':'q1'},{'from':'q1','symbol':'b','to':'q2'}])
    add('toy_machine_rejection_not_human_ungrammaticality',no,not no['accepted_by_declared_machine'])
    e=finite_acceptor(['a'],['q0','q1','q2'],'q0',['q2'],[
      {'from':'q0','symbol':None,'to':'q1'},{'from':'q1','symbol':'a','to':'q2'}])
    add('epsilon_closure',e,e['accepted_by_declared_machine'] and len(e['reachable_states_by_step'][0])==2)
    rel=quantifier_scope_contrast(['a','b'],['x','y'],[['a','x'],['b','y']],[['a','y'],['b','x']])
    add('scope_order_changes_truth',rel,rel['forall_agent_exists_object']=='true' and rel['exists_object_forall_agent']=='false')
    unknown=quantifier_scope_contrast(['a','b'],['x','y'],[['a','x']],[['b','x']])
    add('missing_semantic_relation_is_unknown',unknown,unknown['forall_agent_exists_object']=='unknown')
    w=weighted_segment_alignment(['p','a','t'],['f','a','t'],[{'source':'p','target':'f','cost':.25}],default_substitute_cost=1)
    add('weighted_sound_edit_is_not_cognacy',w,abs(w['minimum_cost']-.25)<1e-12 and not w['phonetic_distance_calibrated'])
    seq=ordered_sound_changes(['p','a','t'],[
      {'id':'stage1','from':'p','to':'f','left':None,'right':'a'},
      {'id':'stage2','from':'t','to':'s','left':'a','right':None}])
    add('stage_ordered_sound_changes',seq,seq['output']==['f','a','s'])
    a=bounded_character_ngram_overlap('cafe\u0301','café',max_order=2)
    b=bounded_character_ngram_overlap('café','café',max_order=2)
    add('normalization_changes_string_overlap',{'raw':a,'same':b},a['score']<1 and b['score']==1)
    blob=b'constructed linguistic notes';expected=sha256(blob).hexdigest()
    packet={'document_id':'demo','language_id':'fictional','source_id':'authored',
      'community_permission':'documented','speaker_permission':'documented','visibility':'public',
      'declared_license':'author-created illustrative fixture','expected_sha256':expected,'reviewer_id':'example'}
    audit=review_language_document(packet,blob)
    add('matching_bytes_do_not_authorize_public_release',audit,audit['decision']=='eligible_for_external_rights_review_only' and not audit['automatically_publishable'])
    denied=review_language_document(dict(packet,community_permission='denied'),blob)
    add('community_denial_overrides_local_hash',denied,denied['decision']=='do_not_distribute')
    wrong=review_language_document(packet,b'different payload')
    add('source_bytes_do_not_match_publisher_digest',wrong,wrong['decision']=='byte_integrity_mismatch')
    return {'schema':'atlas.language-v1-casebook/1','count':len(cases),'status':'passed' if all(x['passed'] for x in cases) else 'failed',
        'cases':cases,'original_unicode_18_conformance_file_acquired':False,'authentic_language_corpora_loaded':0,
        'speaker_reviewers':0,'community_permissions_authenticated':False,'live_language_models_run':0}
