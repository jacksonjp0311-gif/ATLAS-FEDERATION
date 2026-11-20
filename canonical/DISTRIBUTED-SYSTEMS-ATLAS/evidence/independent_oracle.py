"""Independent finite enumerators. These do not import production implementations.
Enumerates set-family intersection, counter joins via set maxima, and clock order.
No wall clock, physical network, Byzantine adversary, or operational guarantee.
"""
from itertools import combinations,product
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R))
from distributed_atlas.quorums import guaranteed_overlap,intersection_lower_bound
from distributed_atlas.clocks import precedes
from distributed_atlas.crdts import GCounter
checks=0
for n in range(1,9):
 family={q:[set(x) for x in combinations(range(n),q)] for q in range(1,n+1)}
 for qa in range(1,n+1):
  for qb in range(1,n+1):
   minimum=min(len(x&y) for x in family[qa] for y in family[qb])
   assert guaranteed_overlap(n,qa,qb)==(minimum>0)
   assert intersection_lower_bound(n,qa,qb)==minimum
   checks+=2
for a in product(range(4),repeat=3):
 for b in product(range(4),repeat=3):
  x=GCounter(dict(zip('abc',a)));y=GCounter(dict(zip('abc',b)))
  result=x.merge(y)
  assert result.value==sum(max(u,v) for u,v in zip(a,b))
  assert x.merge(y)==y.merge(x)
  checks+=2
for a in product(range(4),repeat=3):
 for b in product(range(4),repeat=3):
  ac=dict(zip('abc',a));bc=dict(zip('abc',b))
  independent=all(x<=y for x,y in zip(a,b)) and any(x<y for x,y in zip(a,b))
  assert precedes(ac,bc)==independent
  checks+=1
result={'schema':'atlas.distributed-independent-oracle/1','result':'passed','comparisons':checks,
        'scope':'finite exhaustive sets n<=8, 3D vector 0..3, 3D counters 0..3; no physical validation'}
print(json.dumps(result,indent=2))
