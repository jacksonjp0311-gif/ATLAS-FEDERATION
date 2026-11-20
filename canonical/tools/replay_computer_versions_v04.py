#!/usr/bin/env python3
"""One-command edition-aware AT8 regression: 86 v01 + 56 v02 + 54 v03 + 55 v04 tests.

Historical source is immutable in `history/computer_architecture_v0.1.0_test_snapshot`.
The active expanded node keeps old files unchanged; historical tests deliberately
assert original v01 file counts, so these must run on the original snapshot.
"""
from pathlib import Path
import subprocess,sys,json,os,hashlib,argparse
R=Path(__file__).resolve().parents[1]
NODE=R/'COMPUTER-ARCHITECTURE-ATLAS'
OLD=R/'history/computer_architecture_v0.1.0_test_snapshot/COMPUTER-ARCHITECTURE-ATLAS'
V02=R/'history/computer_architecture_v0.2.0_test_snapshot/COMPUTER-ARCHITECTURE-ATLAS'
V03=R/'history/computer_architecture_v0.3.0_test_snapshot/COMPUTER-ARCHITECTURE-ATLAS'


def sub(folder,pattern):
 code='''import unittest,json,sys
suite=unittest.defaultTestLoader.discover('tests',pattern=%r)
r=unittest.TextTestRunner(verbosity=1).run(suite)
print('RESULT_JSON='+json.dumps({'ran':r.testsRun,'passed':r.testsRun-len(r.failures)-len(r.errors)-len(r.skipped),'failed':len(r.failures),'errors':len(r.errors),'skipped':len(r.skipped)}))
sys.exit(not r.wasSuccessful())'''%pattern
 env=dict(os.environ,PYTHONPATH=os.pathsep.join([str(folder),str(R/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src')]),PYTHONDONTWRITEBYTECODE='1')
 p=subprocess.run([sys.executable,'-c',code],cwd=folder,text=True,capture_output=True,env=env,timeout=90)
 matches=[x[len('RESULT_JSON='):] for x in p.stdout.splitlines() if x.startswith('RESULT_JSON=')]
 if p.returncode or len(matches)!=1:raise RuntimeError('test runner failed: '+p.stderr[-600:])
 return json.loads(matches[0])


def main():
 a=argparse.ArgumentParser();a.add_argument('--out',type=Path);arg=a.parse_args()
 old=sub(OLD,'test_*.py');prior_v02=sub(V02,'test_v02_*.py');prior_v03=sub(V03,'test_v03_*.py');current=sub(NODE,'test_v04_*.py')
 if old['passed']!=86 or prior_v02['passed']!=56 or prior_v03['passed']!=54 or current['passed']!=55:raise RuntimeError('unexpected historical or current suite count')
 receipt={'schema':'atlas.computer-v04-local-versioned-tests/1','result':'passed',
  'historical_v01':old,'historical_v02':prior_v02,'historical_v03':prior_v03,'current_v04_new':current,'total_edition_partitioned_passes':old['passed']+prior_v02['passed']+prior_v03['passed']+current['passed'],
  'historical_snapshot_is_immutable':True,'real_hardware_tested':False}
 if arg.out:
  arg.out.parent.mkdir(parents=True,exist_ok=True);arg.out.write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
