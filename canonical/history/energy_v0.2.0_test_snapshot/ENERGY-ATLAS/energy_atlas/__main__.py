"""Energy Atlas 0.2 offline casebook selection; no physical equipment operated."""
import json,sys
from .cases import casebook
from .survival_cases import casebook_survival
if len(sys.argv)>2 or (len(sys.argv)==2 and sys.argv[1] not in ('casebook','survival-casebook')):
    raise SystemExit('usage: python -m energy_atlas [casebook|survival-casebook]')
result=casebook_survival() if len(sys.argv)>1 and sys.argv[1]=='survival-casebook' else casebook()
print(json.dumps(result,indent=2,default=str))
raise SystemExit(result['status']!='passed')
