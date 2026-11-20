"""Offline, intentionally scoped language science algorithms.

All language examples are synthetic/constructed. None is a universal grammar,
translation model, Unicode segmentation implementation or speech-recognition
system. Source bytes remain separate and external. Unknown != false.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from hashlib import sha256
from math import log2, isfinite
import re
import unicodedata

class LanguageModelError(ValueError):
    pass

MAX_TOKENS = 128


def _id(value, label='id'):
    if not isinstance(value,str) or not value or len(value)>128 or any(ord(c)<32 for c in value):
        raise LanguageModelError('invalid '+label)
    return value


def unicode_profile(text: str) -> dict:
    """Round-trip and normalization metadata; NOT UAX #29 segmentation.

    Raw source is represented by digest only. Normalization is not reversible
    when compatibility distinctions collapse, so original form isn't replaced.
    """
    if not isinstance(text,str) or len(text)>4000:raise LanguageModelError('text must be <= 4000 Unicode code points')
    try:raw=text.encode('utf-8',errors='strict')
    except UnicodeError as e:raise LanguageModelError('invalid UTF-8 input scalar (surrogate?)') from e
    nfc=unicodedata.normalize('NFC',text)
    nfkc=unicodedata.normalize('NFKC',text)
    return {'schema':'atlas.language-unicode-profile/1','raw_sha256':sha256(raw).hexdigest(),
        'utf8_bytes':len(raw),'code_point_count':len(text),
        'categories':dict(sorted(Counter(unicodedata.category(c) for c in text).items())),
        'nfc':nfc,'nfkc':nfkc,'nfc_changed':nfc!=text,'compatibility_mapping_changed':nfkc!=nfc,
        'grapheme_cluster_count':None,'unicode_database_version':unicodedata.unidata_version,
        'limitations':['Python code points are not user-perceived grapheme clusters',
                       'NFKC can erase distinctions; original raw text retained only as a hash here',
                       'This is not an implementation of UAX 29 grapheme, word or sentence boundaries']}


def utf8_decode_strict(data: bytes) -> dict:
    if not isinstance(data,bytes) or len(data)>20000:raise LanguageModelError('bounded bytes required')
    try:txt=data.decode('utf-8','strict')
    except UnicodeError as e:raise LanguageModelError('ill-formed UTF-8 rejected; never silently replace') from e
    return {'text':txt,'bytes_sha256':sha256(data).hexdigest(),'roundtrip':txt.encode('utf-8')==data}


def finite_lexicon_segment(text:str, lexicon:dict[str,int], *, cap:int=100) -> dict:
    """All segmentations of a bounded string under a supplied finite word lexicon.

    This is NOT word segmentation for natural languages or Unicode UAX 29.
    """
    if not isinstance(text,str) or not 1<=len(text)<=64:raise LanguageModelError('bounded nonempty string')
    if not isinstance(lexicon,dict) or not 1<=len(lexicon)<=300:raise LanguageModelError('bounded lexicon')
    if type(cap)!=int or not 1<=cap<=10000:raise LanguageModelError('bounded cap')
    words={}
    for token,weight in lexicon.items():
        if not isinstance(token,str) or not token or len(token)>64 or type(weight)!=int or not 0<=weight<=10000:
            raise LanguageModelError('lexicon requires nonempty word and nonnegative integer cost')
        words[token]=weight
    candidates=[[] for _ in range(len(text)+1)];candidates[len(text)]=[(0,())]
    saturated=False
    for i in range(len(text)-1,-1,-1):
        paths=[]
        for term,cost in words.items():
            if text.startswith(term,i):
                for tail_cost,tail in candidates[i+len(term)]:paths.append((cost+tail_cost,(term,)+tail))
        paths.sort(key=lambda x:(x[0],x[1]))
        if len(paths)>cap:saturated=True
        candidates[i]=paths[:cap]
    return {'schema':'atlas.language-segmentation/1','segmentations':[{'tokens':list(x),'cost':cost} for cost,x in candidates[0]],
        'count_listed':len(candidates[0]),'saturated':saturated,'complete_count_proven':not saturated,
        'limitations':['Results are relative to the supplied lexicon/cost; unknown words have no path',
            'Cap truncation prevents exact ambiguity counts','This does not implement script-specific word segmentation']}


def lexical_morphology(surface:str, entries:list[dict]) -> dict:
    """Explicit dictionary analysis: ambiguity remains, missing analyses unknown."""
    _id(surface,'surface')
    if not isinstance(entries,list) or len(entries)>500:raise LanguageModelError('entries must be a bounded list')
    found=[];seen=set()
    for row in entries:
        if not isinstance(row,dict) or set(row)!={'surface','lemma','features','source_id'}:
            raise LanguageModelError('exact morphology record fields')
        for k in ('surface','lemma','source_id'):_id(row[k],k)
        if not isinstance(row['features'],dict) or any(not isinstance(k,str) or not isinstance(v,str) for k,v in row['features'].items()):
            raise LanguageModelError('string morphological feature map required')
        key=(row['surface'],row['lemma'],tuple(sorted(row['features'].items())),row['source_id'])
        if key in seen:raise LanguageModelError('duplicate morphology entry')
        seen.add(key)
        if row['surface']==surface:found.append({'lemma':row['lemma'],'features':dict(sorted(row['features'].items())),'source_id':row['source_id']})
    return {'schema':'atlas.language-morphology/1','surface':surface,'analyses':found,'status':'found' if found else 'unknown_not_analyzed',
        'disambiguated_by_context':False,'limitations':['Lexicon is caller-supplied and incomplete','No universal morphology rules or semantics inferred']}


def phoneme_contrast(phonemes:dict[str,dict[str,str]],a:str,b:str) -> dict:
    """Hamming distance on explicitly declared feature vectors, not acoustic similarity."""
    if not isinstance(phonemes,dict) or not 2<=len(phonemes)<=300:raise LanguageModelError('bounded feature inventory')
    _id(a);_id(b)
    if a not in phonemes or b not in phonemes:raise LanguageModelError('phoneme not in supplied inventory')
    fs=None
    for p,features in phonemes.items():
        _id(p)
        if not isinstance(features,dict) or not features or any(not isinstance(x,str) or not isinstance(y,str) for x,y in features.items()):raise LanguageModelError('invalid features')
        if fs is None:fs=set(features)
        if set(features)!=fs:raise LanguageModelError('feature dimensions must match')
    diffs=sorted(k for k in fs if phonemes[a][k]!=phonemes[b][k]);return {'differences':diffs,'hamming':len(diffs),'features':len(fs),
        'limitations':['Feature-space differences are a stipulated analytical model, not universal phonetic distance',
                       'Distinctive features and phone inventories vary by analysis and language']}


def cyk_parse(tokens:list[str], lexical:dict[str,list[str]],binary_rules:list, *,start='S',limit:int=1000000)->dict:
    """Bottom-up CYK with one witness and capped derivation count.

    Grammar fragment: A->token and A->B C only (strict Chomsky normal form
    except start nonterminal). No epsilon, unary, unknown or semantic parsing.
    """
    if not isinstance(tokens,list) or not 1<=len(tokens)<=40 or any(not isinstance(t,str) or not t for t in tokens):raise LanguageModelError('1..40 tokens')
    if not isinstance(lexical,dict) or not isinstance(binary_rules,list) or not lexical or not binary_rules or len(binary_rules)>300:raise LanguageModelError('bounded lexical/binary grammar')
    if type(limit)!=int or not 1<=limit<=10**12:raise LanguageModelError('positive finite count cap')
    _id(start)
    terminals={}
    for term,nts in lexical.items():
        _id(term); 
        if not isinstance(nts,list) or not nts:raise LanguageModelError('terminal needs nonterminals')
        for nt in nts:_id(nt)
        if len(nts)!=len(set(nts)):raise LanguageModelError('duplicate lexical production')
        terminals[term]=sorted(nts)
    rules=[]
    for r in binary_rules:
        if not isinstance(r,(list,tuple)) or len(r)!=3 or any(not isinstance(a,str) or not a for a in r):raise LanguageModelError('binary rules require triple nonterminals')
        rules.append(tuple(r))
    if len(set(rules))!=len(rules):raise LanguageModelError('duplicate binary production')
    n=len(tokens);chart=[[defaultdict(lambda: {'count':0,'tree':None}) for _ in range(n+1)] for __ in range(n)]
    truncated=False
    for i,t in enumerate(tokens):
        for nt in terminals.get(t,[]):chart[i][i+1][nt]={'count':1,'tree':(nt,t)}
    for length in range(2,n+1):
        for i in range(n-length+1):
            j=i+length
            for k in range(i+1,j):
                left=chart[i][k];right=chart[k][j]
                for parent,a,b in rules:
                    if a in left and b in right:
                        old=chart[i][j][parent];new=old['count']+left[a]['count']*right[b]['count']
                        if new>limit:truncated=True;new=limit
                        chart[i][j][parent]={'count':new,'tree':old['tree'] or (parent,left[a]['tree'],right[b]['tree'])}
    top=chart[0][n].get(start)
    total=top['count'] if top else 0
    return {'schema':'atlas.language-cyk/1','accepted':total>0,'parse_count_cap':limit,'parse_count':total,
        'saturated':truncated,'count_is_exact':not truncated,'witness_tree':top['tree'] if top else None,
        'grammar_fragment':'CNF lexical and binary productions only',
        'limitations':['No universal/natural-language grammaticality inference','Specified grammar alone controls ambiguity',
                       'Parse count is not exact if cap saturated','Unknown tokens are rejected by this grammar, not impossible in human language']}


def _validate_predicates(model):
    if not isinstance(model,dict) or set(model)!={'domain','predicates'}:raise LanguageModelError('exact finite model fields required')
    domain=model['domain'];predicates=model['predicates']
    if not isinstance(domain,list) or not 1<=len(domain)<=50 or len(set(domain))!=len(domain):raise LanguageModelError('unique nonempty finite domain')
    for entity in domain:_id(entity,'entity')
    if not isinstance(predicates,dict) or len(predicates)>50:raise LanguageModelError('bounded predicates')
    for name,truth in predicates.items():
        _id(name)
        if not isinstance(truth,dict) or set(truth)!={'true','false'}:raise LanguageModelError('explicit positive/negative predicate sets')
        a=[tuple(x) for x in truth['true']];b=[tuple(x) for x in truth['false']]
        if set(a)&set(b):raise LanguageModelError('contradictory truth and false tuples')
        if any(len(x)>4 or not x or any(e not in domain for e in x) for x in a+b):raise LanguageModelError('tuple outside universe')
    return domain,predicates


def finite_truth(formula:dict,model:dict,assignment:dict|None=None) -> dict:
    """Kleene 3-valued finite-predicate fragment: true/false/unknown.

    Not full natural language semantics; predicates are supplied, not grounded.
    """
    domain,predicates=_validate_predicates(model)
    if assignment is None:assignment={}
    if not isinstance(assignment,dict) or any(not isinstance(k,str) or not k.startswith('?') or v not in domain for k,v in assignment.items()):raise LanguageModelError('assignment invalid')
    operations=[0]
    def go(f,env,depth):
        if depth>32:raise LanguageModelError('formula nesting cap')
        operations[0]+=1
        if operations[0]>100000:raise LanguageModelError('finite reasoning operation cap')
        if not isinstance(f,dict) or 'op' not in f:raise LanguageModelError('formula AST required')
        op=f['op']
        if op=='pred':
            if set(f)!={'op','name','args'} or not isinstance(f['args'],list) or not 1<=len(f['args'])<=4:raise LanguageModelError('predicate fields and arity')
            name=f['name'];_id(name)
            if name not in predicates:return None
            args=[]
            for a in f['args']:
                if not isinstance(a,str):raise LanguageModelError('term must be string')
                entity=env.get(a) if a.startswith('?') else a
                if entity not in domain:return None
                args.append(entity)
            tup=tuple(args);truth=predicates[name]
            return True if list(tup) in truth['true'] else False if list(tup) in truth['false'] else None
        if op=='not':
            if set(f)!={'op','arg'}:raise LanguageModelError('not unary')
            v=go(f['arg'],env,depth+1);return not v if v is not None else None
        if op in ('and','or'):
            if set(f)!={'op','args'} or not isinstance(f['args'],list) or not 2<=len(f['args'])<=20:raise LanguageModelError('and/or operands')
            vals=[go(a,env,depth+1) for a in f['args']]
            if op=='and':return False if False in vals else None if None in vals else True
            return True if True in vals else None if None in vals else False
        if op in ('forall','exists'):
            if set(f)!={'op','var','body'} or not isinstance(f['var'],str) or not f['var'].startswith('?') or len(f['var'])>50:raise LanguageModelError('quantifier fields')
            vals=[go(f['body'],dict(env,**{f['var']:entity}),depth+1) for entity in domain]
            if op=='forall':return False if False in vals else None if None in vals else True
            return True if True in vals else None if None in vals else False
        raise LanguageModelError('unsupported formula operator')
    val=go(formula,assignment.copy(),0)
    return {'schema':'atlas.language-three-valued/1','truth':'unknown' if val is None else ('true' if val else 'false'),
        'operations':operations[0],'world_truth_grounded':False,
        'limitations':['Finite three-valued first-order fragment only','Unknown is not equivalent to false',
                       'Predicate assignments are supplied, not observations verified from real world',
                       'Natural language interpretation and quantifier scope must be supplied separately']}


def validate_conllu_basic(text:str)->dict:
    """Validate strict subset of CoNLL-U basic word-lines only.

    Disallows multiword/empty nodes and enhanced edges, not full UD validator.
    """
    if not isinstance(text,str) or len(text)>100000:raise LanguageModelError('bounded text required')
    if '\r' in text or not text.endswith('\n'):raise LanguageModelError('LF-only and final newline required')
    sentences=[];comments=[];words=[]
    def finish():
        nonlocal words,comments
        if not words:
            if comments:raise LanguageModelError('comment-only sentence')
            return
        ids=[int(x[0]) for x in words]
        if ids!=list(range(1,len(words)+1)):raise LanguageModelError('word IDs must be sequential')
        heads=[int(row[6]) for row in words]
        if heads.count(0)!=1:raise LanguageModelError('one root required')
        if any(h<0 or h>len(words) or h==i for i,h in enumerate(heads,1)):raise LanguageModelError('invalid dependency head')
        for i in range(1,len(words)+1):
            seen=set();p=i
            while p:
                if p in seen:raise LanguageModelError('dependency cycle')
                seen.add(p);p=heads[p-1]
        sentences.append({'forms':[r[1] for r in words],'heads':heads,'root_index':heads.index(0)+1,
                          'comments':comments[:]})
        words=[];comments=[]
    for line in text.split('\n'):
        if not line:finish();continue
        if line.startswith('#'):
            if words:raise LanguageModelError('comments must precede words')
            comments.append(line);continue
        cols=line.split('\t')
        if len(cols)!=10 or any(not c for c in cols):raise LanguageModelError('CoNLL-U word line must have 10 tab fields')
        if not cols[0].isdigit() or '.' in cols[0] or '-' in cols[0]:raise LanguageModelError('only integer word IDs supported')
        if not cols[6].isdigit():raise LanguageModelError('HEAD integer required')
        if cols[8]!='_':raise LanguageModelError('enhanced DEPS not supported in basic subset')
        words.append(cols)
    if not sentences:raise LanguageModelError('at least one sentence required')
    return {'schema':'atlas.language-conllu-basic-subset/1','sentences':sentences,'sentence_count':len(sentences),
        'conllu_full_conformance_certified':False,'limitations':['Not a complete CoNLL-U validator: no multiword tokens, empty nodes, enhanced dependencies or full feature validation',
            'Valid dependency shape does not imply correct linguistic annotation or grammaticality']}


def train_bigram(docs:list[dict],alpha:float=1.0)->dict:
    """Toy sentence bigram model with separate train IDs and OOV token mapping."""
    if not isinstance(docs,list) or not 1<=len(docs)<=500:raise LanguageModelError('bounded training corpus')
    if type(alpha) not in (int,float) or not isfinite(alpha) or not .001<=alpha<=100:raise LanguageModelError('smoothing alpha')
    seen=set();vocab=set();counts=Counter();ctx=Counter()
    for doc in docs:
        if not isinstance(doc,dict) or set(doc)!={'id','tokens'}:raise LanguageModelError('training document id and tokens required')
        did=_id(doc['id']);
        if did in seen:raise LanguageModelError('duplicate train id')
        seen.add(did);tokens=doc['tokens']
        if not isinstance(tokens,list) or not 1<=len(tokens)<=MAX_TOKENS:raise LanguageModelError('sentence tokens 1..128')
        if any(not isinstance(t,str) or not t or len(t)>100 or t in ('<s>','</s>','<UNK>') for t in tokens):raise LanguageModelError('reserved or malformed token')
        vocab.update(tokens)
        seq=['<s>']+tokens+['</s>']
        for a,b in zip(seq,seq[1:]):counts[(a,b)]+=1;ctx[a]+=1
    v=sorted(vocab|{'</s>','<UNK>'})
    return {'schema':'atlas.language-bigram/1','alpha':float(alpha),'vocab':v,'train_ids':sorted(seen),
        'counts':{a+'\t'+b:k for (a,b),k in sorted(counts.items())},'contexts':dict(sorted(ctx.items())),
        'tokenization':'caller_supplied_whole_tokens','model_generalization_verified':False}


def score_bigram(model:dict,doc:dict)->dict:
    if not isinstance(model,dict) or model.get('schema')!='atlas.language-bigram/1':raise LanguageModelError('bigram model required')
    if not isinstance(doc,dict) or set(doc)!={'id','tokens'}:raise LanguageModelError('evaluation doc fields')
    did=_id(doc['id'])
    if did in model['train_ids']:raise LanguageModelError('training/evaluation ID leakage')
    tokens=doc['tokens']
    if not isinstance(tokens,list) or not 1<=len(tokens)<=MAX_TOKENS:raise LanguageModelError('tokens 1..128')
    vocab=set(model['vocab']);V=len(vocab);a=model['alpha']
    mapped=[t if t in vocab else '<UNK>' for t in tokens]
    seq=['<s>']+mapped+['</s>']
    logs=[]
    for old,new in zip(seq,seq[1:]):
        n=model['counts'].get(old+'\t'+new,0);den=model['contexts'].get(old,0)+a*V
        logs.append(log2((n+a)/den))
    average=sum(logs)/len(logs)
    return {'schema':'atlas.language-bigram-score/1','evaluation_id':did,
        'tokens_scored':len(logs),'log2_probability':sum(logs), 'perplexity':2**(-average),
        'train_id_disjoint':True,'independent_language_understanding_verified':False,
        'limitations':['This is a small-order surface distribution; low perplexity is not semantic understanding',
                       'Exact-sequence training leakage checks cannot detect paraphrases or other contamination',
                       'OOV mapping and caller-provided tokens determine all scores']}


def language_tag_profile(tag:str)->dict:
    """Restricted BCP-47-like skeleton; not registry validation or full BCP47."""
    if not isinstance(tag,str) or len(tag)>80 or not re.fullmatch(r'[A-Za-z]{2,3}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?',tag):
        raise LanguageModelError('only language[-Script][-Region] skeleton accepted; not full BCP47')
    bits=tag.split('-');lang=bits[0].lower();script=None;region=None
    for x in bits[1:]:
        if len(x)==4:script=x.title()
        else:region=x.upper()
    normalized='-'.join(x for x in (lang,script,region) if x)
    return {'schema':'atlas.language-tag-skeleton/1','canonical_casing_only':normalized,'language':lang,'script':script,'region':region,
        'registry_validated':False,'normative_BCP47_validated':False,
        'limitations':['No IANA language-subtag registry lookup, variants, extensions, private use, grandfathered tags or language matching',
                       'Well-formed skeleton does not guarantee actual language-tag registration']}


def corpus_leakage_report(train:list[dict],test:list[dict])->dict:
    """Exact normalized text and id overlap, not semantic or memorization audit."""
    def collect(rows):
        if not isinstance(rows,list) or len(rows)>500:raise LanguageModelError('bounded corpus split')
        ids=set();d={}
        for r in rows:
            if not isinstance(r,dict) or set(r)!={'id','text'}:raise LanguageModelError('id+text fields')
            rid=_id(r['id']);
            if rid in ids:raise LanguageModelError('duplicate split id')
            ids.add(rid)
            if not isinstance(r['text'],str) or len(r['text'])>10000:raise LanguageModelError('text required')
            digest=sha256(unicodedata.normalize('NFC',r['text']).encode('utf-8')).hexdigest()
            d[rid]=digest
        return d
    tr=collect(train);te=collect(test)
    shared=sorted(set(tr)&set(te));common=sorted(set(tr.values())&set(te.values()))
    return {'schema':'atlas.language-leakage-audit/1','overlapping_ids':shared,'exact_nfc_text_hashes':common,
            'clean_under_exact_tests':not(shared or common),'semantic_leakage_ruled_out':False,
            'limitations':['NFC exact hashes do not detect paraphrases, translations or answer exposure',
                           'A split that passes this test is not independently verified as held out']}
