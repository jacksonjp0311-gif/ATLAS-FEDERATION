"""Independent implementations on constructed inputs; no real-speaker data.

NumPy is optional. Finite comparisons increase code confidence, not scientific proof.
"""
from pathlib import Path
import hashlib,json,random,sys,math
from functools import lru_cache
from collections import Counter
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from language_atlas.v1_models import (finite_acceptor,quantifier_scope_contrast,weighted_segment_alignment,
 ordered_sound_changes,bounded_character_ngram_overlap,review_language_document)
seed=20261114;rng=random.Random(seed);cnt={}
def verify(label,valid):
 if not valid:raise AssertionError('independent disagreement '+label)
 cnt[label]=cnt.get(label,0)+1

# BFS on configuration (state,input-index), including epsilon moves, not repeated set-closure DP.
for _ in range(550):
 states=['s'+str(i) for i in range(4)];labels=['a','b'];trans=[]
 for s in states:
  for t in states:
   for sym in ['a','b',None]:
    if rng.random()<.10:trans.append({'from':s,'symbol':sym,'to':t})
 seq=[rng.choice(labels) for i in range(rng.randrange(6))]
 accepted=['s3']
 out=finite_acceptor(seq,states,'s0',accepted,trans)
 seen={(states[0],0)};stack=list(seen)
 while stack:
  s,i=stack.pop()
  for tr in trans:
   if tr['from']==s and (tr['symbol'] is None or (i<len(seq) and tr['symbol']==seq[i])):
    next=(tr['to'],i+(tr['symbol'] is not None))
    if next not in seen:seen.add(next);stack.append(next)
 expected=any(st in accepted and pos==len(seq) for st,pos in seen)
 verify('nfa_independent_graph_search',out['accepted_by_declared_machine']==expected)

# NumPy matrices for fully known two-valued relational models.
for _ in range(550):
 aa=['a','b','c'];bb=['x','y','z']
 matrix=np.asarray([[rng.getrandbits(1) for _ in bb] for _ in aa],dtype=np.bool_)
 tp=[[a,b] for i,a in enumerate(aa) for j,b in enumerate(bb) if matrix[i,j]]
 fp=[[a,b] for i,a in enumerate(aa) for j,b in enumerate(bb) if not matrix[i,j]]
 got=quantifier_scope_contrast(aa,bb,tp,fp)
 verify('quantifier_forall_exists',got['forall_agent_exists_object']==str(bool(np.all(np.any(matrix,axis=1)))).lower())
 verify('quantifier_exists_forall',got['exists_object_forall_agent']==str(bool(np.any(np.all(matrix,axis=0)))).lower())

# Exhaustive recursion for small weighted-alignment cases, distinct from forward DP.
for _ in range(350):
 a=[rng.choice(['p','t','k']) for i in range(rng.randrange(6))]
 b=[rng.choice(['p','t','k']) for i in range(rng.randrange(6))]
 custom=[{'source':'p','target':'t','cost':.4},{'source':'k','target':'p','cost':.7}]
 got=weighted_segment_alignment(a,b,custom,insert_cost=1.1,delete_cost=.9,default_substitute_cost=1.3)
 @lru_cache(None)
 def brute(i,j):
  if i==len(a):return (len(b)-j)*1.1
  if j==len(b):return (len(a)-i)*.9
  sub=0.0 if a[i]==b[j] else (.4 if (a[i],b[j])==('p','t') else .7 if (a[i],b[j])==('k','p') else 1.3)
  return min(.9+brute(i+1,j),1.1+brute(i,j+1),sub+brute(i+1,j+1))
 verify('weighted_alignment_exhaustive',abs(got['minimum_cost']-brute(0,0))<1e-9)
 verify('weighted_alignment_operation_cost',abs(got['minimum_cost']-sum(op['cost'] for op in got['operations']))<1e-9)

for _ in range(300):
 word=[rng.choice(['a','b','c']) for _ in range(rng.randrange(8))]
 rules=[{'id':'s1','from':'a','to':'b','left':None,'right':'c'},
        {'id':'s2','from':'b','to':'c','left':None,'right':None}]
 got=ordered_sound_changes(word,rules)
 # independently apply simultaneously to a copy for each stage
 q=word[:]
 r1=['b' if z=='a' and k+1<len(q) and q[k+1]=='c' else z for k,z in enumerate(q)]
 r2=['c' if z=='b' else z for z in r1]
 verify('ordered_rules_independent',got['output']==r2)

for _ in range(450):
 a=''.join(rng.choice('abcdef') for i in range(rng.randrange(3,25)))
 b=''.join(rng.choice('abcdef') for i in range(rng.randrange(3,25)))
 got=bounded_character_ngram_overlap(a,b,max_order=3,beta=2)
 pcs=[];rcs=[]
 for n in range(1,4):
  left=Counter(''.join(a[i:i+n]) for i in range(len(a)-n+1));right=Counter(''.join(b[i:i+n]) for i in range(len(b)-n+1))
  common=sum(min(v,right[k]) for k,v in left.items());pcs.append(common/sum(left.values()));rcs.append(common/sum(right.values()))
 P=sum(pcs)/3;Q=sum(rcs)/3;expected=5*P*Q/(4*P+Q) if P+Q>0 else 0
 verify('character_ngram_numpy_independent_counts',abs(got['score']-expected)<1e-12)

for _ in range(240):
 data=bytes(rng.randrange(0,256) for j in range(rng.randrange(120)))
 expected=hashlib.sha256(data).hexdigest()
 packet={'document_id':'synthetic','language_id':'fixture','source_id':'author','community_permission':'documented',
         'speaker_permission':'documented','visibility':'public','declared_license':'original-fixture','expected_sha256':expected,'reviewer_id':'simulated'}
 got=review_language_document(packet,data)
 verify('document_actual_byte_digest',got['computed_sha256']==expected and got['digest_matched'])
 verify('document_never_automatically_published',not got['automatically_publishable'] and not got['community_consent_authenticated'])
report={'schema':'atlas.language-v1-numerical-oracle/1','status':'passed','seed':seed,'comparisons':sum(cnt.values()),
 'by_method':cnt,'numpy_version':np.__version__,'authentic_language_corpora':0,
 'unicode18_normative_test_rows':0,'real_language_models':0,'independent_linguistic_review':False,
 'limitations':['Finite author-generated examples and independent calculations do not prove linguistic universals',
 'No human-speaker judgments, original media or community-consent records were acquired']}
Path(__file__).resolve().parents[1].joinpath('evidence/v1_numeric_oracle.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
