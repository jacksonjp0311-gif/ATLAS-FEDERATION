"""Offline Language Atlas casebooks; no external model calls."""
import json,sys
from .cases import casebook
from .advanced_cases import advanced_casebook
from .v1_cases import casebook_v1
if len(sys.argv)>2 or (len(sys.argv)==2 and sys.argv[1] not in ('advanced','casebook','v1','describe')):
    print('Usage: python -m language_atlas [casebook|advanced|v1|describe]',file=sys.stderr);raise SystemExit(2)
if len(sys.argv)==2 and sys.argv[1]=='describe':
    print(json.dumps({'node':'language-atlas','version':'1.0.0','role':'offline_source_linked_research',
      'live_language_models':0,'human_subjects':0,'Bitwork_router_changes':0},indent=2));raise SystemExit(0)
r=(casebook_v1() if len(sys.argv)==2 and sys.argv[1]=='v1' else
   advanced_casebook() if len(sys.argv)==2 and sys.argv[1]=='advanced' else casebook())
print(json.dumps(r,ensure_ascii=False,indent=2));raise SystemExit(r['status']!='passed')
