"""Materials Atlas CLI. Never execute retrieved records or documents."""
import json,sys
from .cases import casebook
from .advanced_cases import advanced_casebook
from .advanced import published_hahn1_replay

def main():
    cmd=sys.argv[1:] if len(sys.argv)>1 else []
    if len(cmd)!=1 or cmd[0] not in ('casebook','advanced-cases','published-hahn1','describe'):
        print('Usage: python -m materials_atlas casebook|advanced-cases|published-hahn1|describe',file=sys.stderr)
        return 2
    if cmd[0]=='casebook':
        v=casebook();print(json.dumps(v,indent=2));return int(v['status']!='passed')
    if cmd[0]=='advanced-cases':
        v=advanced_casebook();print(json.dumps(v,indent=2));return int(v['status']!='passed')
    if cmd[0]=='published-hahn1':
        v=published_hahn1_replay();print(json.dumps(v,indent=2));return int(v['result']!='passed')
    print(json.dumps({'name':'Materials Atlas','version':'0.2.0','type':'science reference and bounded calculators',
       'scope':'materials reference; one published-data numeric reproduction; not specimen certification'},indent=2));return 0

if __name__=='__main__':raise SystemExit(main())
