"""Language Atlas v1: finite, offline reconstruction models.

Models are self-contained educational calculations with author-generated inputs;
they do not establish linguistic universals, speaker judgments, or permissions.
"""
from __future__ import annotations
from collections import Counter
from hashlib import sha256
from math import isfinite
import unicodedata
from .models import LanguageModelError


def _ids(values, name, cap):
    if not isinstance(values,list) or not 1 <= len(values) <= cap:
        raise LanguageModelError(f'{name}: require 1..{cap} identifiers')
    if any(not isinstance(v,str) or not v or len(v)>96 for v in values) or len(values)!=len(set(values)):
        raise LanguageModelError(f'{name}: distinct bounded string identifiers required')
    return values


def finite_acceptor(tokens:list[str],states:list[str],start:str,accepting:list[str],transitions:list[dict])->dict:
    """NFA with epsilon transitions; tokens are symbols, not linguistic words.

    A finite acceptance result is conditional on the supplied machine, and
    does not decide grammaticality or meaning in any living language.
    """
    state_set=set(_ids(states,'states',100))
    if start not in state_set:raise LanguageModelError('unknown start state')
    if not isinstance(accepting,list) or len(accepting)>len(states) or any(v not in state_set for v in accepting) or len(set(accepting))!=len(accepting):
        raise LanguageModelError('accept set must be subset of states')
    if not isinstance(tokens,list) or len(tokens)>100 or any(not isinstance(x,str) or not x or len(x)>96 for x in tokens):
        raise LanguageModelError('bounded token-symbol sequence required')
    if not isinstance(transitions,list) or len(transitions)>500:raise LanguageModelError('transition cap exceeded')
    outgoing={s:[] for s in states};seen=set()
    for r in transitions:
        if not isinstance(r,dict) or set(r)!={'from','symbol','to'}:raise LanguageModelError('NFA transition fields')
        a,b=r['from'],r['to'];sym=r['symbol']
        if a not in state_set or b not in state_set or (sym is not None and (not isinstance(sym,str) or not sym or len(sym)>96)):
            raise LanguageModelError('invalid NFA transition')
        key=(a,sym,b)
        if key in seen:raise LanguageModelError('duplicate transition')
        seen.add(key);outgoing[a].append((sym,b))
    def closure(inp):
        result=set(inp);stack=list(inp)
        while stack:
            u=stack.pop()
            for sym,v in outgoing[u]:
                if sym is None and v not in result:result.add(v);stack.append(v)
        return result
    reachable=closure({start});trajectory=[sorted(reachable)]
    for sym in tokens:
        reachable=closure({v for u in reachable for label,v in outgoing[u] if label==sym})
        trajectory.append(sorted(reachable))
    return {'schema':'atlas.language-finite-acceptor/1','accepted_by_declared_machine':bool(reachable & set(accepting)),
        'reachable_states_by_step':trajectory,'final_states':sorted(reachable),'epsilon_closure_used':True,
        'linguistic_grammaticality_verified':False,'limitations':['Only supplied states and labels, not all natural-language syntax',
        'A string rejected by a toy NFA can still be fully grammatical in the world','No semantics or speaker evidence']}


def quantifier_scope_contrast(agents:list[str],objects:list[str],true_pairs:list[list[str]],false_pairs:list[list[str]])->dict:
    """Strong Kleene 3-valued quantifiers for R(x,y), unknown distinct from F.

    Two formulae: ∀agent ∃object R vs ∃object ∀agent R. No default CWA.
    """
    ax=_ids(agents,'agents',40);ob=_ids(objects,'objects',40)
    def pairs(inp,name):
        if not isinstance(inp,list) or len(inp)>1600:raise LanguageModelError(f'{name} cap')
        out=set()
        for p in inp:
            if not isinstance(p,list) or len(p)!=2 or p[0] not in ax or p[1] not in ob:raise LanguageModelError('unknown relation argument')
            out.add(tuple(p))
        if len(out)!=len(inp):raise LanguageModelError('duplicate relation fact')
        return out
    yes=pairs(true_pairs,'positive');no=pairs(false_pairs,'negative')
    if yes & no:raise LanguageModelError('same fact cannot be true and false')
    def get(a,b):return 'true' if (a,b) in yes else 'false' if (a,b) in no else 'unknown'
    def every(vals):return 'false' if 'false' in vals else 'true' if all(v=='true' for v in vals) else 'unknown'
    def some(vals):return 'true' if 'true' in vals else 'false' if all(v=='false' for v in vals) else 'unknown'
    first=every([some([get(a,b) for b in ob]) for a in ax])
    second=some([every([get(a,b) for a in ax]) for b in ob])
    return {'schema':'atlas.language-scope-contrast/1','forall_agent_exists_object':first,'exists_object_forall_agent':second,
        'known_true':len(yes),'known_false':len(no),'unknown':len(ax)*len(ob)-len(yes)-len(no),
        'interpretation':'three-valued truth relative to explicitly supplied binary relation only',
        'natural_language_scope_disambiguated':False,
        'limitations':['Quantifier scope is a representation choice, not automatically selected from words',
                       'Unreported facts remain unknown; source model may omit relevant entities or relations']}


def weighted_segment_alignment(source:list[str],target:list[str],substitutions:list[dict],*,insert_cost=1.0,delete_cost=1.0,default_substitute_cost=1.0)->dict:
    """Dynamic programming with declared substitution costs (not phonetic metric)."""
    def costs(x,name):
        if type(x) not in (float,int) or not isfinite(x) or x<0 or x>1e6:raise LanguageModelError(name+' nonnegative finite cost required')
        return float(x)
    ic=costs(insert_cost,'insert');dc=costs(delete_cost,'delete');default=costs(default_substitute_cost,'substitute')
    for s in (source,target):
        if not isinstance(s,list) or len(s)>80 or any(not isinstance(x,str) or not x or len(x)>80 for x in s):
            raise LanguageModelError('bounded segment arrays')
    if not isinstance(substitutions,list) or len(substitutions)>512:raise LanguageModelError('substitution table cap')
    override={}
    for p in substitutions:
        if not isinstance(p,dict) or set(p)!={'source','target','cost'} or not isinstance(p['source'],str) or not p['source'] or not isinstance(p['target'],str) or not p['target']:
            raise LanguageModelError('substitution row shape')
        key=(p['source'],p['target'])
        if key in override:raise LanguageModelError('duplicate substitution cost')
        override[key]=costs(p['cost'],'substitution row')
    n,m=len(source),len(target);dp=[[0.0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):dp[i][0]=i*dc
    for j in range(1,m+1):dp[0][j]=j*ic
    for i in range(1,n+1):
        for j in range(1,m+1):
            penalty=0.0 if source[i-1]==target[j-1] else override.get((source[i-1],target[j-1]),default)
            dp[i][j]=min(dp[i-1][j]+dc,dp[i][j-1]+ic,dp[i-1][j-1]+penalty)
    i,j=n,m;ops=[]
    while i or j:
        if i and j:
            penalty=0.0 if source[i-1]==target[j-1] else override.get((source[i-1],target[j-1]),default)
            if abs(dp[i][j]-(dp[i-1][j-1]+penalty))<1e-10:
                ops.append({'operation':'match' if penalty==0 and source[i-1]==target[j-1] else 'substitute',
                            'source':source[i-1],'target':target[j-1],'cost':penalty});i-=1;j-=1;continue
        if i and abs(dp[i][j]-(dp[i-1][j]+dc))<1e-10:
            ops.append({'operation':'delete','source':source[i-1],'target':None,'cost':dc});i-=1;continue
        if j and abs(dp[i][j]-(dp[i][j-1]+ic))<1e-10:
            ops.append({'operation':'insert','source':None,'target':target[j-1],'cost':ic});j-=1;continue
        raise LanguageModelError('alignment backtrace failure')
    ops.reverse()
    return {'schema':'atlas.language-weighted-segment-alignment/1','minimum_cost':dp[n][m],'operations':ops,
            'segment_unit':'caller_supplied','phonetic_distance_calibrated':False,
            'limitations':['Costs are declared by the caller, not trained from human perceptual judgments',
                           'An optimal edit path is not evidence of cognacy or historical sound change']}


def ordered_sound_changes(segments:list[str],rules:list[dict])->dict:
    """Stage-ordered local replacement rules; within-stage positions simultaneous.

    Each rule replaces a single segment in optional immediate left/right context.
    Does not infer historical sound laws from data or claim phonemic analysis.
    """
    if not isinstance(segments,list) or len(segments)>200 or any(not isinstance(x,str) or not x or len(x)>80 for x in segments):
        raise LanguageModelError('bounded segment sequence')
    if not isinstance(rules,list) or len(rules)>60:raise LanguageModelError('rule count 0..60')
    seq=segments[:];changes=[];seen=set()
    for i,r in enumerate(rules):
        if not isinstance(r,dict) or set(r)!={'id','from','to','left','right'}:raise LanguageModelError('rule exact shape')
        for k in ('id','from','to'):
            if not isinstance(r[k],str) or not r[k] or len(r[k])>80:raise LanguageModelError('rule label invalid')
        if r['id'] in seen:raise LanguageModelError('duplicate rule id')
        seen.add(r['id'])
        for k in ('left','right'):
            if r[k] is not None and (not isinstance(r[k],str) or not r[k] or len(r[k])>80):raise LanguageModelError('context token or null')
        changed=[];candidate=seq[:]
        for j,item in enumerate(seq):
            if item!=r['from']:continue
            if r['left'] is not None and (j==0 or seq[j-1]!=r['left']):continue
            if r['right'] is not None and (j+1>=len(seq) or seq[j+1]!=r['right']):continue
            candidate[j]=r['to'];changed.append(j)
        changes.append({'stage':i,'rule_id':r['id'],'changed_positions':changed,'before':seq[:],'after':candidate[:]})
        seq=candidate
    return {'schema':'atlas.language-ordered-sound-changes/1','input':segments[:],'output':seq,'stages':changes,
        'historical_sound_correspondences_verified':False,'rules_reversible_proven':False,
        'limitations':['Rules apply to supplied segments, not documented language family history',
                       'Stage ordering can change outputs; inverse mapping generally underdetermined']}


def bounded_character_ngram_overlap(candidate:str,reference:str,*,max_order=4,beta=2.0)->dict:
    """Illustrative Unicode *code-point* n-gram F-score, not standard chrF/chrF++."""
    if any(not isinstance(x,str) or len(x)>2000 for x in (candidate,reference)):
        raise LanguageModelError('bounded text strings required')
    if type(max_order)!=int or not 1<=max_order<=6 or type(beta) not in (float,int) or not isfinite(beta) or beta<=0 or beta>100:
        raise LanguageModelError('invalid order/beta')
    precision=[];recall=[];counts=[]
    for n in range(1,max_order+1):
        a=Counter(candidate[i:i+n] for i in range(max(0,len(candidate)-n+1)))
        b=Counter(reference[i:i+n] for i in range(max(0,len(reference)-n+1)))
        common=sum(min(k,b[g]) for g,k in a.items());ca=sum(a.values());cb=sum(b.values())
        if ca and cb:
            precision.append(common/ca);recall.append(common/cb)
        else:
            precision.append(None);recall.append(None)
        counts.append({'n':n,'matches':common,'candidate_total':ca,'reference_total':cb})
    valid=[(p,r) for p,r in zip(precision,recall) if p is not None]
    if not valid:score=None
    else:
        p=sum(x[0] for x in valid)/len(valid);r=sum(x[1] for x in valid)/len(valid)
        score=0.0 if p==0 and r==0 else (1+beta*beta)*p*r/(beta*beta*p+r)
    return {'schema':'atlas.language-codepoint-ngram-overlap/1','score':score,'beta':float(beta),'max_order':max_order,
        'n_gram_counts':counts,'unit':'Unicode code points (not grapheme clusters)','normalization':'none','casefold':'none',
        'standard_chrF_reproduction':False,'translation_meaning_verified':False,
        'limitations':['Illustrative char n-gram F-score; differs from official chrF implementations and WMT conventions',
                       'Unicode normalization and segmentation can change this metric',
                       'Surface overlap cannot establish translation adequacy or speaker acceptance']}


def review_language_document(packet:dict,raw_bytes:bytes|None)->dict:
    """Rights and local hash review without authentication or storage of source bytes."""
    keys={'document_id','language_id','source_id','community_permission','speaker_permission','visibility',
          'declared_license','expected_sha256','reviewer_id'}
    if not isinstance(packet,dict) or set(packet)!=keys:raise LanguageModelError('document accession exact fields')
    for k in ('document_id','language_id','source_id'):
        v=packet[k]
        if not isinstance(v,str) or not v or len(v)>128:raise LanguageModelError('invalid identifier')
    if packet['community_permission'] not in {'documented','denied','unknown'} or packet['speaker_permission'] not in {'documented','denied','unknown'} or packet['visibility'] not in {'public','restricted'}:
        raise LanguageModelError('invalid consent/access states')
    if not isinstance(packet['declared_license'],str) or len(packet['declared_license'])>128:raise LanguageModelError('invalid license text')
    expected=packet['expected_sha256']
    if expected is not None and (not isinstance(expected,str) or len(expected)!=64 or any(c not in '0123456789abcdef' for c in expected)):
        raise LanguageModelError('invalid expected digest')
    if packet['reviewer_id'] is not None and (not isinstance(packet['reviewer_id'],str) or not packet['reviewer_id']):raise LanguageModelError('reviewer id')
    if raw_bytes is not None and (type(raw_bytes)!=bytes or len(raw_bytes)>2_000_000):raise LanguageModelError('source bytes cap')
    computed=sha256(raw_bytes).hexdigest() if raw_bytes is not None else None
    if packet['community_permission']=='denied' or packet['speaker_permission']=='denied':decision='do_not_distribute'
    elif packet['visibility']=='restricted':decision='access_restricted_do_not_publish'
    elif packet['community_permission']!='documented' or packet['speaker_permission']!='documented':decision='permission_unresolved'
    elif expected is None or computed is None:decision='source_bytes_or_digest_missing'
    elif computed!=expected:decision='byte_integrity_mismatch'
    elif not packet['declared_license']:decision='license_unresolved'
    else:decision='eligible_for_external_rights_review_only'
    return {'schema':'atlas.language-document-accession/1','document_id':packet['document_id'],'decision':decision,
        'computed_sha256':computed,'digest_matched':computed is not None and expected==computed,
        'reviewer_identity_authenticated':False,'community_consent_authenticated':False,'automatically_publishable':False,
        'raw_bytes_retained_in_output':False,
        'limitations':['Caller-declared permissions and license are not authenticated human consent or lawful access',
                       'Matching local bytes establishes integrity relative to a supplied expected hash, not publisher authenticity',
                       'Community authority, context, restrictions, and withdrawal requests need a real rights governance process']}
