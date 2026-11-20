"""Secondary NumPy and exhaustive arithmetic checks on original, invented fixtures.

Not external multilingual data, translation accuracy, linguistic universals,
community consent, peer review or independent empirical validation.
"""
import json,random,math,sys
from pathlib import Path
from collections import Counter
from functools import lru_cache
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
try:import numpy as np
except ImportError as err:
 print(json.dumps({'status':'not_run','cause':repr(err)}));raise SystemExit(2)
from language_atlas.advanced import *
@lru_cache(maxsize=None)
def oracle_edit(a,b):
    if not a:return len(b)
    if not b:return len(a)
    return min(oracle_edit(a[1:],b)+1,oracle_edit(a,b[1:])+1,oracle_edit(a[1:],b[1:])+(a[0]!=b[0]))
seed=20261114;rng=random.Random(seed);counts={'edit_distance':0,'bleu_precision':0,'bleu_brevity':0,
  'bleu_unsmoothed':0,'typology_family_weight':0,'typology_naive':0,'pcfg_inside':0,'multimodal_overlap':0}
worst=0

def check(category,x,y):
 global worst
 x=float(x);y=float(y)
 err=abs(x-y);worst=max(worst,err)
 if not math.isfinite(err) or err>1e-11*max(1,abs(x),abs(y)):raise AssertionError(f'{category}: {x=} {y=} err={err}')
 counts[category]+=1

for _ in range(500):
 a=[rng.choice('abc') for i in range(rng.randrange(10))]
 b=[rng.choice('abc') for j in range(rng.randrange(10))]
 candidate=aligned_edit_distance(a,b)
 check('edit_distance',candidate['distance'],oracle_edit(tuple(a),tuple(b)))

for _ in range(400):
 r=[rng.choice('abcd') for j in range(rng.randrange(1,10))]
 c=[rng.choice('abcd') for j in range(rng.randrange(1,10))]
 out=corpus_bleu([c],[[r]],max_order=2)
 for order in (1,2):
  n=order;cc=Counter(tuple(c[k:k+n]) for k in range(len(c)-n+1));rr=Counter(tuple(r[k:k+n]) for k in range(len(r)-n+1))
  exact=sum(min(v,rr[t]) for t,v in cc.items());t=sum(cc.values())
  check('bleu_precision',out['precisions'][n-1],exact/t if t else 0)
 check('bleu_brevity',out['brevity_penalty'],1.0 if len(c)>=len(r) else math.exp(1-len(r)/len(c)))
 expected=out['brevity_penalty']*(math.sqrt(out['precisions'][0]*out['precisions'][1]))
 check('bleu_unsmoothed',out['bleu_unsmoothed'],expected)

for _ in range(450):
 rows=[];family={}
 for j in range(rng.randint(1,35)):
  fam=rng.choice(['f0','f1','f2','f3']);known=rng.choice([0,0,1,None]);family.setdefault(fam,[])
  if known is not None:family[fam].append(known)
  rows.append({'language_id':f'lang{j}','family_id':fam,'area_id':'toy-region','feature':bool(known) if known is not None else None})
 x=typology_by_family(rows)
 data=[v for z in family.values() for v in z]
 if data:
  check('typology_naive',x['naive_known_fraction'],float(np.mean(np.array(data,dtype=np.float64))))
  fam_means=[np.mean(np.array(z,dtype=np.float64)) for z in family.values() if z]
  check('typology_family_weight',x['equal_family_mean'],float(np.mean(fam_means)))
 else:
  assert x['naive_known_fraction'] is None and x['equal_family_mean'] is None

# Independent exhaustive CNF grammar on two tokens.
for _ in range(300):
 p=rng.uniform(.01,.99);q=rng.uniform(.01,.99)
 lex=[{'lhs':'N','token':'x','p':1},{'lhs':'V','token':'y','p':1},
      {'lhs':'Q','token':'x','p':1},{'lhs':'R','token':'y','p':1}]
 binary=[{'lhs':'S','left':'N','right':'V','p':p},
         {'lhs':'S','left':'Q','right':'R','p':1-p}]
 out=pcfg_inside(['x','y'],lex,binary)
 # Both derivations have lexical mass 1.
 check('pcfg_inside',out['sentence_probability'],p+(1-p))
 check('pcfg_inside',out['best_derivation_probability'],max(p,1-p))

for _ in range(300):
 rows=[];tiers={}
 for i in range(rng.randint(1,20)):
  tier=rng.choice(['hand','face','gaze'])
  a=rng.randrange(1,50);b=a+rng.randrange(1,20)
  rows.append({'event_id':str(i),'tier':tier,'start_ms':a,'end_ms':b,'label':'toy'})
  tiers.setdefault(tier,[]).append((a,b))
 r=multimodal_tier_audit(rows)
 for tier,events in tiers.items():
  # Independent vectorized check of neighboring ordered starts/ends, not parser code.
  arr=np.asarray(sorted(events),dtype=int)
  expected=int(np.sum(arr[1:,0]<arr[:-1,1]))
  check('multimodal_overlap',r['overlaps_within_tier'][tier],expected)

out={'schema':'atlas.language-v02-oracle/1','status':'passed','seed':seed,'counts':counts,'total_comparisons':sum(counts.values()),
 'max_absolute_difference':worst,'numpy_version':np.__version__,
 'authentic_language_or_speaker_data_loaded':0,'external_translation_systems_evaluated':0,
 'independently_reviewed_scientific_hypotheses':0,
 'limitations':['Independent formulas/checks on authored synthetic data are software evidence, not human language universals',
 'Small grammar demonstrates stipulated probability mass and not real syntactic competence']}
Path(__file__).resolve().parents[1].joinpath('evidence/numerical_oracle_v0.2.0.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
