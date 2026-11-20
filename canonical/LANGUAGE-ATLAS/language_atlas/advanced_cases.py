"""Constructed examples; not real speakers, translation systems or fieldwork."""
from .advanced import *

def advanced_casebook():
    cases=[]
    def add(name,output,ok):
        cases.append({'id':name,'passed':bool(ok),'result':output,'origin':'author_constructed_offline_fixture',
            'real_human_language_validation':False})
    a=aligned_edit_distance(['i','like','cats'],['i','adore','cats'])
    add('edit_alignment',a,a['distance']==1 and a['counts']['substitute']==1)
    b=aligned_edit_distance(['x','y'],[])
    add('empty_hypothesis',b,b['distance']==2 and b['reference_normalized_error_rate']==1)
    ble=corpus_bleu([['we','study','language']],[ [['we','study','language']] ],max_order=3)
    add('matched_translation_reference',ble,ble['bleu_unsmoothed']==1 and not ble['semantic_translation_quality_verified'])
    zero=corpus_bleu([['x','y']],[ [['a','b']] ],max_order=2)
    add('zero_precision_no_smoothing',zero,zero['bleu_unsmoothed']==0)
    lexical=[{'lhs':'N','token':'birds','p':1.0},{'lhs':'V','token':'sing','p':1.0}]
    binary=[{'lhs':'S','left':'N','right':'V','p':1.0}]
    parse=pcfg_inside(['birds','sing'],lexical,binary)
    add('pcfg_inside',parse,parse['accepted_by_supplied_grammar'] and parse['sentence_probability']==1)
    unknown=pcfg_inside(['birds','speak'],lexical,binary)
    add('unknown_word_not_universal_grammar',unknown,not unknown['accepted_by_supplied_grammar'])
    rows=[{'language_id':'a1','family_id':'A','area_id':'x','feature':True},
          {'language_id':'a2','family_id':'A','area_id':'x','feature':True},
          {'language_id':'a3','family_id':'A','area_id':'x','feature':True},
          {'language_id':'b1','family_id':'B','area_id':'y','feature':False},
          {'language_id':'b2','family_id':'B','area_id':'y','feature':None}]
    typ=typology_by_family(rows)
    add('family_sampling_bias',typ,typ['naive_known_fraction']==.75 and typ['equal_family_mean']==.5 and typ['unknown_values']==1)
    cor=aligned_sound_correspondences([{'item_id':'toy','language_a':'L1','language_b':'L2','segments_a':['p','a','t'],
        'segments_b':['f','a','t'],'source_id':'authored-demo'}])
    add('correspondence_not_cognacy',cor,cor['aligned_pairs_counted']==3 and not cor['cognacy_proven'])
    def rights(pid='documented',spid='documented',access='public',orig=True,digest='a'*64):
        return {'record_id':'r1','language_id':'L1','source_id':'toy','community_permission':pid,'speaker_permission':spid,
                'access':access,'original_bytes_present':orig,'raw_sha256':digest if orig else None,'license':'CC-BY'}
    x=documentation_rights_audit([rights(pid='denied')]);add('community_denial_blocks_release',x,x['records'][0]['accession_status']=='do_not_release')
    y=documentation_rights_audit([rights()]);add('metadata_not_consent_authentication',y,y['records'][0]['accession_status']=='conditionally_eligible_for_human_rights_review' and not y['automatically_publishable'])
    z=multimodal_tier_audit([{'event_id':'h1','tier':'hands','start_ms':0,'end_ms':250,'label':'tokenA'},
                            {'event_id':'f1','tier':'face','start_ms':100,'end_ms':200,'label':'expression'}])
    add('parallel_sign_tiers',z,z['events']==2 and z['overlaps_within_tier']=={'face':0,'hands':0} and not z['original_media_acquired'])
    return {'schema':'atlas.language-advanced-casebook/1','version':'0.2.0',
       'status':'passed' if all(x['passed'] for x in cases) else 'failed','count':len(cases),
       'cases':cases,'authentic_corpora_rows_loaded':0,'live_language_models_evaluated':0,
       'human_consented_recordings_acquired':0,'independent_linguistic_review':False}
