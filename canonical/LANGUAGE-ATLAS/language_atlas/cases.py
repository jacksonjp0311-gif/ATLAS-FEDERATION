"""Transparent human-language science cases; all examples are constructed."""
from __future__ import annotations
from .models import *

def morphology_fixture():
    return [
        {'surface':'flies','lemma':'fly','features':{'POS':'NOUN','Number':'Plur'},'source_id':'toy-n1'},
        {'surface':'flies','lemma':'fly','features':{'POS':'VERB','Person':'3','Number':'Sing'},'source_id':'toy-v1'},
        {'surface':'mice','lemma':'mouse','features':{'POS':'NOUN','Number':'Plur'},'source_id':'toy-n2'}]

def grammar_fixture():
    # Two parses for: robots see astronomers with telescopes.
    return ({'robots':['NP'],'astronomers':['NP'],'telescopes':['NP'],'see':['V'],'with':['P']},
            [('S','NP','VP'),('VP','V','NP'),('VP','VP','PP'),('NP','NP','PP'),('PP','P','NP')])

def model_fixture():
    return {'domain':['ada','bea'],
            'predicates':{'scientist':{'true':[['ada']],'false':[['bea']]},
                          'reads':{'true':[['ada','bea']],'false':[]}}}

def conllu_fixture():
    return '# sent_id = toy1\n# text = Ada reads.\n1\tAda\tAda\tPROPN\t_\t_\t2\tnsubj\t_\t_\n2\treads\tread\tVERB\t_\t_\t0\troot\t_\t_\n3\t.\t.\tPUNCT\t_\t_\t2\tpunct\t_\t_\n\n'

def casebook():
    cases=[]
    def take(name,result,check,limits):
        if not check:raise AssertionError(name)
        cases.append({'id':name,'passed':True,'result':result,'data_origin':'original_constructed_fixture','limitations':limits})
    a=unicode_profile('cafe\u0301')
    take('canonical_norm',a,a['nfc']=='café' and a['nfc_changed'],['Not grapheme segmentation'])
    a=unicode_profile('①')
    take('compatibility_loss_warning',a,a['compatibility_mapping_changed'] and a['nfkc']=='1',['NFKC loses some distinctions'])
    t=utf8_decode_strict('mañana'.encode('utf-8'))
    take('utf8_roundtrip',t,t['roundtrip'],['No broken UTF-8 accepted'])
    try:utf8_decode_strict(b'\xff');bad=False
    except LanguageModelError:bad=True
    take('invalid_utf8_refusal',{'refused':bad},bad,['Malformed transport is rejected'])
    x=finite_lexicon_segment('therapist',{'the':0,'rapist':5,'therapist':0})
    take('word_boundary_ambiguity',x,len(x['segmentations'])==2 and x['segmentations'][0]['tokens']==['therapist'],['Toy lexicon, not UAX 29'])
    x=finite_lexicon_segment('unseen',{'un':1,'seen':0})
    take('segmentation_compositional',x,x['segmentations'][0]['tokens']==['un','seen'],['Not morphological truth'])
    m=lexical_morphology('flies',morphology_fixture())
    take('morphological_ambiguity',m,len(m['analyses'])==2 and not m['disambiguated_by_context'],['Analyses are corpus-supplied'])
    p=phoneme_contrast({'p':{'voice':'-','place':'bilabial','manner':'stop'},'b':{'voice':'+','place':'bilabial','manner':'stop'}},'p','b')
    take('phonemic_feature_contrast',p,p['hamming']==1,['Not acoustic distance'])
    lex,grammar=grammar_fixture();parse=cyk_parse('robots see astronomers with telescopes'.split(),lex,grammar)
    take('attachment_ambiguity',parse,parse['accepted'] and parse['parse_count']==2,['Grammar is constructed CNF'])
    no=cyk_parse('astronomers robots see'.split(),lex,grammar)
    take('grammar_rejection_not_human_rejection',no,not no['accepted'],['Unknown under this grammar, not universally ungrammatical'])
    world=model_fixture()
    f={'op':'forall','var':'?x','body':{'op':'pred','name':'scientist','args':['?x']}}
    out=finite_truth(f,world)
    take('finite_quantifier_false',out,out['truth']=='false',['Depends on provided domain and facts'])
    f={'op':'exists','var':'?x','body':{'op':'pred','name':'reads','args':['?x','ada']}}
    out=finite_truth(f,world)
    take('unreported_fact_unknown',out,out['truth']=='unknown',['Missing is not false'])
    p=validate_conllu_basic(conllu_fixture())
    take('ud_basic_dependency_shape',p,p['sentence_count']==1 and p['sentences'][0]['root_index']==2,['Not full UD conformance'])
    try:validate_conllu_basic(conllu_fixture().replace('2\tpunct','3\tpunct'));cycle=False
    except LanguageModelError:cycle=True
    take('dependency_cycle_refusal',{'refused':cycle},cycle,['No semantic annotation assessment'])
    docs=[{'id':'training-a','tokens':['cats','sleep']},{'id':'training-b','tokens':['dogs','sleep']}]
    bg=train_bigram(docs)
    out=score_bigram(bg,{'id':'heldout-c','tokens':['cats','sleep']})
    take('smoothing_and_probability',out,out['perplexity']>1 and out['train_id_disjoint'],['Perplexity is not understanding'])
    try:score_bigram(bg,{'id':'training-a','tokens':['cats','sleep']});leak=False
    except LanguageModelError:leak=True
    take('training_id_leakage_refusal',{'refused':leak},leak,['Paraphrase leakage not checked'])
    tag=language_tag_profile('sr-latn-rs')
    take('language_tag_skeleton_only',tag,tag['canonical_casing_only']=='sr-Latn-RS' and not tag['registry_validated'],['Not full BCP47'])
    leak=corpus_leakage_report([{'id':'a','text':'cafe\u0301'}],[{'id':'b','text':'café'}])
    take('canonical_text_leakage',leak,not leak['clean_under_exact_tests'],['No semantic duplicates checked'])
    clean=corpus_leakage_report([{'id':'a','text':'hello'}],[{'id':'b','text':'world'}])
    take('clean_does_not_prove_holdout',clean,clean['clean_under_exact_tests'] and not clean['semantic_leakage_ruled_out'],['Cannot certify independent benchmark'])
    return {'schema':'atlas.language-casebook/1','status':'passed','case_count':len(cases),'cases':cases,
        'real_multilingual_corpus_acquired':False,'human_subjects_tested':False,'complete_natural_language_model':False}
