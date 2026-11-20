"""Language Atlas 0.2 — bounded, evidence-qualified linguistic computation.

All inputs here are caller-supplied metadata, constructed example structures or
explicit reference token sequences. No speech, sign, field recording, real
multilingual corpus, community consent, model training or translation is implied.
"""
from __future__ import annotations
from collections import Counter,defaultdict
from math import exp,log,isfinite
from hashlib import sha256
from .models import LanguageModelError


def _id(x,what='identifier'):
    if not isinstance(x,str) or not x or len(x)>128 or any(ord(c)<32 for c in x):
        raise LanguageModelError('invalid '+what)
    return x


def _tokens(xs, *,allow_empty=False):
    if not isinstance(xs,list) or len(xs)>(256 if allow_empty else 128) or (not allow_empty and not xs):
        raise LanguageModelError('bounded list of tokens required')
    if any(not isinstance(x,str) or not x or len(x)>128 for x in xs):
        raise LanguageModelError('tokens must be nonempty bounded strings')
    return xs


def aligned_edit_distance(source:list[str],target:list[str])->dict:
    """Unit-cost edit distance with one alignment witness, NOT translation quality.

    Matches, substitutions, insertions and deletions act on caller-supplied
    tokens; different segmentation means a different metric.
    """
    a=_tokens(source,allow_empty=True);b=_tokens(target,allow_empty=True)
    if len(a)*len(b)>30000:raise LanguageModelError('edit grid exceeds resource cap')
    dp=[[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)+1):dp[i][0]=i
    for j in range(len(b)+1):dp[0][j]=j
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+(a[i-1]!=b[j-1]))
    i,j=len(a),len(b);ops=[];counts=Counter()
    while i or j:
        if i and j and dp[i][j]==dp[i-1][j-1]+(a[i-1]!=b[j-1]):
            op='match' if a[i-1]==b[j-1] else 'substitute';ops.append({'op':op,'source':a[i-1],'target':b[j-1]});i-=1;j-=1
        elif i and dp[i][j]==dp[i-1][j]+1:
            op='delete';ops.append({'op':op,'source':a[i-1],'target':None});i-=1
        elif j and dp[i][j]==dp[i][j-1]+1:
            op='insert';ops.append({'op':op,'source':None,'target':b[j-1]});j-=1
        else:raise LanguageModelError('invalid DP backtrace')
        counts[op]+=1
    ops.reverse()
    d=dp[-1][-1]
    assert d==counts['substitute']+counts['delete']+counts['insert']
    return {'schema':'atlas.language-token-alignment/1','distance':d,'operations':ops,
       'counts':{k:counts[k] for k in ('match','substitute','insert','delete')},
       'token_unit':'exact_caller_supplied_token_strings',
       'reference_normalized_error_rate':d/len(a) if a else None,
       'limitations':['One optimal alignment may not be unique',
         'Score and error types depend on tokenization, normalization and reference choice',
         'No language comprehension, transcript validity or translation adequacy is established']}


def corpus_bleu(candidate:list[list[str]],references:list[list[list[str]]],max_order:int=4)->dict:
    """Unsmooth corpus BLEU with explicit pre-tokenized sentence-level references.

    Not SacreBLEU: tokenization, case, Unicode, references, smoothing and version
    are caller choices. Zero n-gram precision for a required order -> BLEU zero.
    """
    if type(max_order)!=int or not 1<=max_order<=4:raise LanguageModelError('orders 1..4')
    if not isinstance(candidate,list) or not isinstance(references,list) or not 1<=len(candidate)==len(references)<=100:
        raise LanguageModelError('matching nonempty sentence arrays required')
    matched=[0]*max_order;total=[0]*max_order;cand_len=0;ref_len=0
    for cand,refs in zip(candidate,references):
        c=_tokens(cand,allow_empty=True)
        if not isinstance(refs,list) or not 1<=len(refs)<=10:raise LanguageModelError('one or more references per sentence')
        rr=[_tokens(r,allow_empty=True) for r in refs]
        cand_len+=len(c);ref_len+=min((len(r) for r in rr),key=lambda n:(abs(n-len(c)),n))
        for n in range(1,max_order+1):
            def ngrams(seq):return Counter(tuple(seq[i:i+n]) for i in range(max(0,len(seq)-n+1)))
            cc=ngrams(c);maxref=Counter()
            for r in rr:
                for k,v in ngrams(r).items():maxref[k]=max(maxref[k],v)
            matched[n-1]+=sum(min(v,maxref[k]) for k,v in cc.items())
            total[n-1]+=sum(cc.values())
    precisions=[matched[i]/total[i] if total[i] else 0.0 for i in range(max_order)]
    bp=0.0 if cand_len==0 else (1.0 if cand_len>=ref_len else exp(1-ref_len/cand_len))
    score=bp*exp(sum(log(p) for p in precisions)/max_order) if all(p>0 for p in precisions) else 0.0
    return {'schema':'atlas.language-corpus-bleu/1','bleu_unsmoothed':score,'max_order':max_order,
       'matched_ngrams':matched,'candidate_ngrams':total,'precisions':precisions,
       'candidate_tokens':cand_len,'effective_reference_tokens':ref_len,
       'brevity_penalty':bp,'tokenization':'caller_supplied','smoothing':'none',
       'semantic_translation_quality_verified':False,
       'limitations':['This is not a reproduction of SacreBLEU or a standardized WMT score',
        'Corpus BLEU depends on tokenization, case, reference set and selected n-gram order',
        'Translation adequacy, cultural appropriateness and rare language quality require independent assessment']}


def _p(x,what):
    if type(x) not in (float,int) or not isfinite(x) or not 0<=x<=1:raise LanguageModelError('invalid probability '+what)
    return float(x)


def pcfg_inside(tokens:list[str],lexical_rules:list[dict],binary_rules:list[dict],*,start='S')->dict:
    """Inside probability and Viterbi witness for a tiny CNF PCFG.

    Lexical {'lhs','token','p'}, binary {'lhs','left','right','p'}.
    For each LHS, all its lexical/binary probabilities must total 1.
    """
    t=_tokens(tokens)
    if len(t)>25:raise LanguageModelError('max 25 tokens')
    _id(start,'start symbol')
    if not isinstance(lexical_rules,list) or not isinstance(binary_rules,list) or not 1<=len(lexical_rules)+len(binary_rules)<=250:
        raise LanguageModelError('bounded grammar required')
    lex=defaultdict(list);binrules=[];sums=defaultdict(float);seen=set()
    for rule in lexical_rules:
        if not isinstance(rule,dict) or set(rule)!={'lhs','token','p'}:raise LanguageModelError('lexical rule fields')
        lhs=_id(rule['lhs']);terminal=_id(rule['token']);prob=_p(rule['p'],'lexical');key=('lex',lhs,terminal)
        if key in seen:raise LanguageModelError('duplicate production')
        seen.add(key);lex[terminal].append((lhs,prob));sums[lhs]+=prob
    for rule in binary_rules:
        if not isinstance(rule,dict) or set(rule)!={'lhs','left','right','p'}:raise LanguageModelError('binary rule fields')
        lhs,left,right=(_id(rule[k]) for k in ('lhs','left','right'));prob=_p(rule['p'],'binary');key=('bin',lhs,left,right)
        if key in seen:raise LanguageModelError('duplicate binary production')
        seen.add(key);binrules.append((lhs,left,right,prob));sums[lhs]+=prob
    if start not in sums or any(abs(q-1)>1e-9 for q in sums.values()):raise LanguageModelError('PCFG must normalize by LHS')
    n=len(t);inside=[[defaultdict(float) for _ in range(n+1)] for _ in range(n)]
    best=[[{} for _ in range(n+1)] for _ in range(n)]
    for i,token in enumerate(t):
        for lhs,p in lex.get(token,[]):
            inside[i][i+1][lhs]+=p
            if p>best[i][i+1].get(lhs,(0,None))[0]:best[i][i+1][lhs]=(p,(lhs,token))
    for size in range(2,n+1):
        for i in range(n-size+1):
            j=i+size
            for split in range(i+1,j):
                for lhs,left,right,p in binrules:
                    if left in inside[i][split] and right in inside[split][j]:
                        inside[i][j][lhs]+=p*inside[i][split][left]*inside[split][j][right]
                    if left in best[i][split] and right in best[split][j]:
                        a,b=best[i][split][left],best[split][j][right]
                        prob=p*a[0]*b[0]
                        if prob>best[i][j].get(lhs,(0,None))[0]:best[i][j][lhs]=(prob,(lhs,a[1],b[1]))
    total=inside[0][n].get(start,0.0)
    maximum,tree=best[0][n].get(start,(0.0,None))
    return {'schema':'atlas.language-pcfg-inside/1','sentence_probability':total,
       'best_derivation_probability':maximum,'best_tree':tree,'accepted_by_supplied_grammar':total>0,
       'grammar_fragment':'probabilistic CNF: lexical and binary only',
       'limitations':['Grammar and probabilities are caller-supplied and not learned from a real language',
         'Floating underflow may hide tiny nonzero probabilities; no log-space dynamic programming used',
         'Best derivation is not necessarily the most probable *syntactic tree* after summing derivation duplicates',
         'Grammar rejection is not a statement of human grammaticality']}


def typology_by_family(rows:list[dict])->dict:
    """Observed binary feature rates: naive vs equal-family weighted, no population inference."""
    if not isinstance(rows,list) or not 1<=len(rows)<=3000:raise LanguageModelError('1..3000 typology rows')
    seen=set();groups=defaultdict(list);total=0;positive=0;missing=0;areas=set()
    for row in rows:
        if not isinstance(row,dict) or set(row)!={'language_id','family_id','area_id','feature'}:
            raise LanguageModelError('exact typology fields')
        language=_id(row['language_id']);family=_id(row['family_id']);area=_id(row['area_id'])
        if language in seen:raise LanguageModelError('duplicate language identifier')
        seen.add(language);areas.add(area)
        f=row['feature']
        if f is None:missing+=1
        elif type(f) is bool:groups[family].append(int(f));total+=1;positive+=int(f)
        else:raise LanguageModelError('feature must be bool or unknown')
    byfam={f:sum(v)/len(v) for f,v in sorted(groups.items())}
    return {'schema':'atlas.language-typology-sampling/1','languages':len(rows),
        'known_values':total,'unknown_values':missing,'observed_positive_known':positive,
        'naive_known_fraction':positive/total if total else None,
        'equal_family_mean':sum(byfam.values())/len(byfam) if byfam else None,
        'per_family_known_fraction':byfam,'distinct_areas_reported':len(areas),
        'genealogical_independence_proved':False,'areal_independence_proved':False,
        'limitations':['Family balancing is one descriptive sensitivity check, not a statistically representative sample',
          'Relatedness and areal contact produce dependence; unknown feature values are not negatives',
          'Small families, classification uncertainty and data collection bias can distort both means']}


def aligned_sound_correspondences(rows:list[dict])->dict:
    """Count stipulated aligned segment pairs; cannot prove cognacy or reconstruction."""
    if not isinstance(rows,list) or not 1<=len(rows)<=2000:raise LanguageModelError('bounded rows required')
    seen=set();counts=Counter();skipped=Counter();langpairs=set();n=0
    for row in rows:
        if not isinstance(row,dict) or set(row)!={'item_id','language_a','language_b','segments_a','segments_b','source_id'}:
            raise LanguageModelError('alignment exact fields required')
        item=_id(row['item_id']);a=_id(row['language_a']);b=_id(row['language_b']);source=_id(row['source_id'])
        if a==b:raise LanguageModelError('different languages required')
        if item in seen:raise LanguageModelError('duplicate item id')
        seen.add(item);langpairs.add((a,b))
        seg_a=_tokens(row['segments_a']);seg_b=_tokens(row['segments_b'])
        if len(seg_a)!=len(seg_b):raise LanguageModelError('pre-aligned segments must have equal length')
        for u,v in zip(seg_a,seg_b):
            if u=='-' and v=='-':raise LanguageModelError('double gap has no correspondence')
            if u=='-' or v=='-':skipped['gap_columns']+=1
            else:counts[(u,v)]+=1;n+=1
    return {'schema':'atlas.language-historical-correspondence/1','rows':len(rows),
       'aligned_pairs_counted':n,'correspondences':[{'segment_a':a,'segment_b':b,'count':c} for (a,b),c in sorted(counts.items())],
       'excluded_gap_columns':skipped['gap_columns'],'language_pairs':sorted(langpairs),
       'cognacy_proven':False,'sound_change_law_proven':False,'shared_inheritance_proven':False,
       'limitations':['Aligned lists and cognate hypotheses are caller-supplied, not verified against speakers or archives',
         'Correspondence count is not a sound-change probability or a proof of language family relationship',
         'Borrowing, chance similarity, morphology and chronology need independent assessment']}


def documentation_rights_audit(records:list[dict])->dict:
    """Metadata-only proposed accession review, not actual permission or legal approval."""
    if not isinstance(records,list) or not 1<=len(records)<=500:raise LanguageModelError('bounded document record list')
    seen=set();out=[]
    for row in records:
        if not isinstance(row,dict) or set(row)!={'record_id','language_id','source_id','community_permission','speaker_permission','access','original_bytes_present','raw_sha256','license'}:
            raise LanguageModelError('exact documentation fields required')
        rid=_id(row['record_id']);_id(row['language_id']);_id(row['source_id']);license_id=_id(row['license'])
        if rid in seen:raise LanguageModelError('duplicate record id')
        seen.add(rid)
        if row['community_permission'] not in {'documented','unknown','denied'} or row['speaker_permission'] not in {'documented','unknown','denied'}:
            raise LanguageModelError('permission metadata invalid')
        if row['access'] not in {'public','restricted','unknown'}:raise LanguageModelError('access classification invalid')
        if type(row['original_bytes_present']) is not bool:raise LanguageModelError('bytes present flag must be bool')
        digest=row['raw_sha256']
        if digest is not None and (not isinstance(digest,str) or len(digest)!=64 or any(c not in '0123456789abcdef' for c in digest)):
            raise LanguageModelError('SHA-256 field must be lowercase hex or null')
        if digest is not None and not row['original_bytes_present']:raise LanguageModelError('hash supplied without original bytes')
        if 'denied' in (row['community_permission'],row['speaker_permission']):state='do_not_release'
        elif row['access']!='public':state='access_review_required'
        elif row['community_permission']=='unknown' or row['speaker_permission']=='unknown':state='consent_evidence_required'
        elif not row['original_bytes_present'] or digest is None:state='primary_bytes_and_hash_required'
        else:state='conditionally_eligible_for_human_rights_review'
        out.append({'record_id':rid,'accession_status':state,'hash_of_bytes_recomputed':False})
    return {'schema':'atlas.language-documentation-rights-review/1','records':out,
        'publisher_rights_authenticated':False,'community_consent_authenticated':False,
        'speaker_consent_authenticated':False,'primary_bytes_rehashed':False,'automatically_publishable':False,
        'limitations':['Caller-provided permission labels and digests are unverified and cannot confer legal rights',
          'Sensitive community knowledge may require restricted access even when a generic license exists',
          'No speaker data, audio, sign video or community archive is imported by this method']}


def multimodal_tier_audit(rows:list[dict])->dict:
    """Check tier/time metadata for sign or speech annotations without original media."""
    if not isinstance(rows,list) or not 1<=len(rows)<=5000:raise LanguageModelError('bounded annotation events')
    groups=defaultdict(list);seen=set()
    for r in rows:
        if not isinstance(r,dict) or set(r)!={'event_id','tier','start_ms','end_ms','label'}:raise LanguageModelError('annotation fields')
        e=_id(r['event_id']);t=_id(r['tier']);lab=_id(r['label'])
        if e in seen:raise LanguageModelError('duplicate event id')
        seen.add(e);a=r['start_ms'];b=r['end_ms']
        if type(a) not in (int,float) or type(b) not in (int,float) or not isfinite(a) or not isfinite(b) or a<0 or b<=a:
            raise LanguageModelError('positive, finite time interval required')
        groups[t].append((float(a),float(b)))
    overlap={}
    for tier,intervals in groups.items():
        intervals.sort();overlap[tier]=sum(intervals[i][0]<intervals[i-1][1] for i in range(1,len(intervals)))
    return {'schema':'atlas.language-multimodal-tiers/1','tiers':sorted(groups),
      'events':len(rows),'overlaps_within_tier':overlap,
      'simultaneous_channels_permitted':True,'original_media_acquired':False,
      'limitations':['Timestamps and annotation labels are caller-supplied; no sign or speech verified',
         'Overlap across articulatory tiers can be meaningful; within-tier overlap can also be legitimate',
         'No linguistic interpretation or accessibility support established without original context and consent']}
