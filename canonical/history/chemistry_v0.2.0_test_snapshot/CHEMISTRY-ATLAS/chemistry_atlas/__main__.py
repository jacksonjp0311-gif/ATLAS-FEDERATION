"""Offline bounded Chemistry casebook; no external chemical equipment."""
import json,sys
from .cases import casebook
from .advanced_cases import advanced_casebook
if len(sys.argv)>2 or (len(sys.argv)==2 and sys.argv[1] not in ('advanced','casebook')):
 raise SystemExit('usage: python -m chemistry_atlas [casebook|advanced]')
r=advanced_casebook() if len(sys.argv)>1 and sys.argv[1]=='advanced' else casebook()
print(json.dumps(r,ensure_ascii=False,indent=2))
raise SystemExit(r['status']!='passed')
