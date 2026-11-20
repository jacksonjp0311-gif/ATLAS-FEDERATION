"""Measurement reference data, using Forge's common runtime rather than a fork."""
from importlib.resources import files
from pathlib import Path

def open_reference():
    try:from atlas_forge.common import AtlasStore
    except ImportError as exc:raise RuntimeError("Install the companion Atlas Forge 0.4.0 or newer compatible wheel to use reference retrieval. Numerical functions remain standalone.") from exc
    return AtlasStore(Path(str(files('measurement_atlas')/'resources/common')))

def main(argv=None):
    import argparse,json
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('question');p.add_argument('--max-bytes',type=int,default=32768);a=p.parse_args(argv)
    try:result=open_reference().assemble_context(a.question,max_context_bytes=a.max_bytes);print(json.dumps(result,ensure_ascii=False,indent=2));return 0
    except (ValueError,OSError,RuntimeError) as exc:print(json.dumps({'error':str(exc)}));return 2
