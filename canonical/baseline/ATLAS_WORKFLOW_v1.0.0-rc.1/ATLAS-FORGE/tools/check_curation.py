"""Structural source-card intake check. Never a scientific verification claim."""
from pathlib import Path
import argparse,json,sys
from urllib.parse import urlsplit
p=argparse.ArgumentParser(description=__doc__);p.add_argument('path',type=Path);a=p.parse_args()
errors=[]
try:
 d=json.loads(a.path.read_text(encoding='utf-8'));sources=d['sources'];records=d['records'];ids=[s['id'] for s in sources]
 if len(ids)!=len(set(ids)):errors.append('duplicate source IDs')
 if len({r['id'] for r in records})!=len(records):errors.append('duplicate record IDs')
 for s in sources:
  if urlsplit(s['url']).scheme!='https':errors.append(s['id']+': HTTPS required')
  for k in ['title','inspected_scope','rights','publication']:
   if not s.get(k):errors.append(s['id']+': missing '+k)
 for r in records:
  if r['source'] not in ids:errors.append(r['id']+': missing source')
  for k in ['locator','text','assumptions','limitations','kind','origin']:
   if not r.get(k):errors.append(r['id']+': missing '+k)
  if r['origin'] not in ['source_reported','formal_derivation']:errors.append(r['id']+': unexpected origin')
 out={'schema':'atlas.curation-check/1','valid':not errors,'records':len(records),'sources':len(sources),'errors':errors,
      'scientific_support_verified_by_this_tool':False,'check_scope':'required fields, source linkage and explicit limitations only'}
except (OSError,ValueError,TypeError,KeyError) as e:out={'valid':False,'errors':[str(e)]}
print(json.dumps(out,indent=2));sys.exit(0 if out['valid'] else 2)
