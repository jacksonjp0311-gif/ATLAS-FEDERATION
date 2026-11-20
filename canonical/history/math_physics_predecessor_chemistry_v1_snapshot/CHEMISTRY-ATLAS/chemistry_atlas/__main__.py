"""Offline chemistry casebooks; no web or equipment control."""
import json,sys
from .cases import casebook
from .advanced_cases import advanced_casebook
from .v1_cases import casebook_v1
opts={'casebook':casebook,'advanced':advanced_casebook,'v1':casebook_v1}
if len(sys.argv)>2 or (len(sys.argv)==2 and sys.argv[1] not in opts):raise SystemExit('Usage: python -m chemistry_atlas [casebook|advanced|v1]')
r=opts[sys.argv[1] if len(sys.argv)>1 else 'casebook']()
print(json.dumps(r,ensure_ascii=False,indent=2))
raise SystemExit(r['status']!='passed')
