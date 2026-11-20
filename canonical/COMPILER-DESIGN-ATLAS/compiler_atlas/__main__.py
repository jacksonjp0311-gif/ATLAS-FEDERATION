import argparse,json,sys
from .core import compile_program,run,serialize,CompileError,Trap
p=argparse.ArgumentParser(description='ATLAS bounded typed compiler educational reference')
p.add_argument('source',help='source file with let statements and return expression')
p.add_argument('--ir',action='store_true')
a=p.parse_args()
try:
    with open(a.source,'r',encoding='utf8') as f:src=f.read()
    code=compile_program(src)
    if a.ir:sys.stdout.buffer.write(serialize(code))
    else:print(json.dumps({'value':run(code),'semantics':'checked-i32'}))
except (CompileError,Trap) as e:
    print(json.dumps({'result':'rejected_or_trapped','reason':str(e)}),file=sys.stderr)
    sys.exit(2)
