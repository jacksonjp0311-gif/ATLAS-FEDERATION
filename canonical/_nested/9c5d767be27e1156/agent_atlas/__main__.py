"""Explicit research demonstration commands, not a live runtime."""
import json,sys
from .cases import casebook
from .advanced_cases import advanced_casebook
from .v03_cases import casebook_v03
from .v04_cases import casebook_v04
from . import __version__

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('casebook','advanced-casebook','v03-casebook','v04-casebook','describe'):
        print('Usage: python -m agent_atlas casebook|advanced-casebook|v03-casebook|v04-casebook|describe',file=sys.stderr);return 2
    if sys.argv[1]=='casebook':
        result=casebook();print(json.dumps(result,indent=2));return result['status']!='passed'
    if sys.argv[1]=='advanced-casebook':
        result=advanced_casebook();print(json.dumps(result,indent=2));return result['status']!='passed'
    if sys.argv[1]=='v03-casebook':
        result=casebook_v03();print(json.dumps(result,indent=2));return result['status']!='passed'
    if sys.argv[1]=='v04-casebook':
        result=casebook_v04();print(json.dumps(result,indent=2));return result['status']!='passed'
    print(json.dumps({'node':'agent-atlas','version':__version__,'kind':'offline_research_reference',
       'live_llm_calls':False,'live_tool_calls':False,'Atlas_or_Bitwork_router_changes':False},indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
