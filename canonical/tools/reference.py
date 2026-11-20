"""Data-root adapter to the unchanged Forge runtime; no new ranking algorithm."""
from pathlib import Path
import argparse,json,sys
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import AtlasStore,ContractError
p=argparse.ArgumentParser();p.add_argument('question');p.add_argument('--node',action='append');p.add_argument('--max-bytes',type=int,default=32768);a=p.parse_args()
try:print(json.dumps(AtlasStore(R/'common').assemble_context(a.question,node_ids=a.node,max_context_bytes=a.max_bytes),indent=2,ensure_ascii=False))
except (ContractError,OSError) as e:print(json.dumps({'error':str(e)}),file=sys.stderr);raise SystemExit(2)
