"""Offline energy casebooks only; no actual tool or equipment control."""
import json,sys
from .cases import casebook
from .survival_cases import casebook_survival
from .v1_cases import casebook_v1
choices={'casebook':casebook,'survival-casebook':casebook_survival,'v1-casebook':casebook_v1}
if len(sys.argv)>2 or len(sys.argv)==2 and sys.argv[1] not in choices:raise SystemExit('usage: python -m energy_atlas [casebook|survival-casebook|v1-casebook]')
result=choices[sys.argv[1] if len(sys.argv)>1 else 'casebook']()
print(json.dumps(result,indent=2,default=str))
raise SystemExit(result['status']!='passed')
