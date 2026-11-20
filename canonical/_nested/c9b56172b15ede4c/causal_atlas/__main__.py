"""Command line: explicitly invoked teaching tools, not research instructions."""
import argparse,json,sys
from pathlib import Path
from importlib.resources import files
from . import __version__
from .models import DAG,ModelError,standardize_binary
from .cases import casebook

def load(path):
    p=Path(path)
    if p.stat().st_size>262144:raise ModelError('Input is limited to 256 KiB')
    def pairs(xs):
        d={}
        for k,v in xs:
            if k in d:raise ModelError('Duplicate JSON key')
            d[k]=v
        return d
    return json.loads(p.read_text(encoding='utf-8'),object_pairs_hook=pairs,
        parse_constant=lambda s: (_ for _ in ()).throw(ModelError('Nonfinite JSON')))

def main():
    p=argparse.ArgumentParser(description='Causal Atlas bounded reference and teaching tools')
    p.add_argument('--version',action='version',version=__version__)
    sub=p.add_subparsers(dest='cmd',required=True)
    sub.add_parser('casebook')
    s=sub.add_parser('separation');s.add_argument('file');s.add_argument('--x',required=True);s.add_argument('--y',required=True);s.add_argument('--given',nargs='*',default=[])
    s=sub.add_parser('adjustment');s.add_argument('file');s.add_argument('--exposure',required=True);s.add_argument('--outcome',required=True);s.add_argument('--observed',nargs='+',required=True)
    s=sub.add_parser('standardize');s.add_argument('file')
    s=sub.add_parser('reference');s.add_argument('question');s.add_argument('--max-bytes',type=int,default=32768)
    a=p.parse_args()
    try:
        if a.cmd=='casebook':out=casebook()
        elif a.cmd=='separation':out={'d_separated':DAG.from_dict(load(a.file)).d_separated([a.x],[a.y],a.given),'conditional_on_supplied_graph':True,'graph_truth_checked':False}
        elif a.cmd=='adjustment':out={'minimal_backdoor_sets':DAG.from_dict(load(a.file)).minimal_backdoor_sets(a.exposure,a.outcome,a.observed),'criterion':'single_exposure_sufficient_backdoor','complete_identification_algorithm':False}
        elif a.cmd=='standardize':
            d=load(a.file)
            if set(d)!={'rows','target_weights'}:raise ModelError('Expected rows and target_weights')
            out=standardize_binary(d['rows'],d['target_weights'])
        else:
            try:from atlas_forge.common import AtlasStore
            except ImportError as e:raise ModelError('Reference retrieval needs the bundled shared atlas_forge runtime; mathematical tools do not.') from e
            out=AtlasStore(str(files('causal_atlas')/'resources/common')).assemble_context(a.question,max_context_bytes=a.max_bytes)
        print(json.dumps(out,indent=2,ensure_ascii=False,allow_nan=False));return 0 if out.get('result')!='failed' else 1
    except (ModelError,ValueError,TypeError,KeyError,OSError) as e:
        print(json.dumps({'error':str(e),'result':'invalid_or_unsupported'}),file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
