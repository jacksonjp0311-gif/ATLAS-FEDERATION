"""Independent finite constructed comparisons for Language Atlas 0.1.0.

These checks do NOT test native-language speaker accuracy or full Unicode/UD
normative conformance. The constructed corpus is not a real held-out dataset.
"""
from __future__ import annotations
import sys,random,itertools,math,json,unicodedata,hashlib
from pathlib import Path
from functools import lru_cache
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from language_atlas.models import *
try:import numpy as np
except ImportError:np=None
rng=random.Random(20261114)
counts={}
def check(label,yes):
    if not yes:raise AssertionError(label)
    counts[label]=counts.get(label,0)+1

# Enumerate every legal lexicon path independently, by raw recursive DFS.
lex={'a':3,'b':1,'aa':1,'ab':2,'ba':0,'bb':2}
def enumerate_paths(s):
    if not s:return [(0,())]
    result=[]
    for w,c in lex.items():
        if s.startswith(w):
            for rest,seg in enumerate_paths(s[len(w):]):result.append((rest+c,(w,)+seg))
    return sorted(result,key=lambda x:(x[0],x[1]))
for _ in range(350):
    text=''.join(rng.choice('ab') for i in range(rng.randint(1,10)))
    x=finite_lexicon_segment(text,lex,cap=10000)
    expected=enumerate_paths(text)
    check('independent_segmentation_enumeration',x['count_listed']==len(expected) and x['segmentations']==[{'cost':cost,'tokens':list(tokens)} for cost,tokens in expected] and not x['saturated'])

# Parse count on a smaller CFG verified against independent recursive grammar enumerator.
lexical={'a':['N','V'],'b':['N'],'p':['P']};rules=[('S','N','V'),('S','S','P'),('V','V','N'),('N','N','P'),('P','P','N')]
@lru_cache(None)
def brute_parse(tokens, symbol):
    if len(tokens)==1:return int(symbol in lexical.get(tokens[0],[]))
    total=0
    for lhs,a,b in rules:
        if lhs==symbol:
            for k in range(1,len(tokens)):
                total+=brute_parse(tokens[:k],a)*brute_parse(tokens[k:],b)
    return total
for _ in range(390):
    toks=tuple(rng.choice('abp') for i in range(rng.randint(1,6)))
    result=cyk_parse(list(toks),lexical,rules,start='S',limit=100000)
    check('independent_recursive_CYK_counts',result['parse_count']==brute_parse(toks,'S') and result['count_is_exact'])

# Independent direct multinomial Laplace bigram probability for held-out tokens.
for i in range(450):
    choices=['red','blue','green','up'];training=[]
    for t in range(rng.randint(2,7)):
        training.append({'id':'train-'+str(t),'tokens':[rng.choice(choices) for _ in range(rng.randint(1,7))]})
    alpha=rng.choice([0.1,0.5,1,2]);trained=train_bigram(training,alpha=alpha)
    held=[rng.choice(choices+['new']) for _ in range(rng.randint(1,7))]
    result=score_bigram(trained,{'id':'eval-'+str(i),'tokens':held})
    V=len(trained['vocab']); vocab=set(trained['vocab']);seq=['<s>']+[w if w in vocab else '<UNK>' for w in held]+['</s>']
    pair_counter=Counter();context_counter=Counter()
    for doc in training:
        toks=['<s>']+doc['tokens']+['</s>']
        for a,b in zip(toks,toks[1:]):pair_counter[a,b]+=1;context_counter[a]+=1
    logs=[math.log2((pair_counter[a,b]+alpha)/(context_counter[a]+alpha*V)) for a,b in zip(seq,seq[1:])]
    check('independent_bigram_probability',math.isclose(sum(logs),result['log2_probability'],abs_tol=1e-11) and math.isclose(2**(-sum(logs)/len(logs)),result['perplexity'],rel_tol=1e-11))

# Straight three-valued logic reference enumerated from independently defined tables.
for _ in range(420):
    truth=[rng.choice((True,False,None)) for _ in range(3)]
    m={'domain':['a','b','c'],'predicates':{'P':{'true':[[x] for x,v in zip('abc',truth) if v is True],
        'false':[[x] for x,v in zip('abc',truth) if v is False]}}}
    p={'op':'pred','name':'P','args':['?x']}
    for op in ['forall','exists']:
        result=finite_truth({'op':op,'var':'?x','body':p},m)['truth']
        expected=(False if False in truth else None if None in truth else True) if op=='forall' else (True if True in truth else None if None in truth else False)
        check('independent_three_valued_quantifiers',result==('unknown' if expected is None else str(expected).lower()))

# UTF-8/Unicode profile requires strict byte roundtrip and NFC idempotence.
chars=['a','a\u0301','d0','あ','\u2460','👩\u200d💻','\u00e9','\u1f7e']
for i in range(360):
    s=''.join(rng.choice(chars) for _ in range(rng.randint(1,8)))
    x=unicode_profile(s)
    check('unicode_canonical_and_raw_byte_integrity',unicodedata.normalize('NFC',x['nfc'])==x['nfc'] and x['raw_sha256']==hashlib.sha256(s.encode('utf8')).hexdigest() and x['utf8_bytes']==len(s.encode('utf8')))

# Toy dependency trees: independently validate root, reachability, no cycles.
for i in range(250):
    n=rng.randint(1,12)
    heads=[0]+[rng.randint(1,k) for k in range(1,n)]
    rows=['# sent_id = generated-'+str(i)]
    for j,h in enumerate(heads,1):rows.append('\t'.join([str(j),'x','x','NOUN','_','_',str(h),'dep' if h else 'root','_','_']))
    text='\n'.join(rows)+'\n\n';out=validate_conllu_basic(text)
    # independent parent-walk chain count exactly one source and no cycles
    okay=heads.count(0)==1 and all(0<=h<=n and h!=k for k,h in enumerate(heads,1))
    check('conllu_independent_tree_shape',okay and out['sentence_count']==1 and out['sentences'][0]['heads']==heads)

result={'schema':'atlas.language-model-oracle/1','result':'passed','seed':20261114,
   'comparisons':sum(counts.values()),'by_algorithm':counts,
   'numpy_installed':np is not None,'data_origin':'original_author_generated_synthetic_fixtures',
   'published_corpus_rows_loaded':0,'natural_language_grammar_validated':False,
   'normative_unicode_conformance_tested':False,'independent_human_linguistic_review':False,
   'limitations':['Independent enumeration and reference arithmetic on selected finite fixtures, not a general theorem prover',
       'No live speaker, audio, sign-language video, translation or authentic annotated corpus examined',
       'Unicode normalization checks use runtime Unicode database, not independent Unicode 18.0 test files']}
p=Path(__file__).resolve().parents[1]/'evidence/numerical_oracle_v0.1.0.json'
p.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result,indent=2))
