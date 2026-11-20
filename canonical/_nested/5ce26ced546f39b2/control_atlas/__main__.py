"""Local-only explicit mathematical casebook CLI; never controls hardware."""
import json,sys
from .cases import casebook
from .extended_cases import casebook as extended_casebook
from .robust_cases import casebook as robust_casebook
from . import __version__
def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('casebook','extended-casebook','robust-casebook','describe'):
        print('Usage: python -m control_atlas casebook|extended-casebook|robust-casebook|describe',file=sys.stderr);return 2
    if sys.argv[1]=='describe':
        print(json.dumps({'name':'Control Atlas','version':__version__,'scope':'mathematical teaching, no real plant control','independent_review':False,'bitwork_integration':False},indent=2));return 0
    r=casebook() if sys.argv[1]=='casebook' else (robust_casebook() if sys.argv[1]=='robust-casebook' else extended_casebook())
    print(json.dumps(r,indent=2))
    return 0 if r.get('result',r.get('status'))=='passed' else 1
if __name__=='__main__':raise SystemExit(main())
