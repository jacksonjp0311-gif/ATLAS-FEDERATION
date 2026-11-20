from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys
root=Path(__file__).resolve().parent
out=root/'ATLAS-FORGE'/'output'/('check-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
raise SystemExit(subprocess.run([sys.executable,str(root/'ATLAS-FORGE/tools/run_workflow.py'),'--measurement',str(root/'MEASUREMENT-ATLAS'),'--out',str(out)],cwd=root).returncode)
