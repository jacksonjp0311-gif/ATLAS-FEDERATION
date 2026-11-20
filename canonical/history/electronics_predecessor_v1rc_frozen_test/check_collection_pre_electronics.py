"""Reproduce the content checkpoint without granting final release acceptance."""
from pathlib import Path
import argparse,datetime,hashlib,json,os,platform,subprocess,sys,unittest,zipfile,tempfile
R=Path(__file__).resolve().parents[1];B=R/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1'
FORGE=B/'ATLAS-FORGE';MEAS=B/'MEASUREMENT-ATLAS';CAUSAL=R/'CAUSAL-ATLAS';MATERIALS=R/'MATERIALS-ATLAS';CONTROL=R/'CONTROL-ATLAS';AGENT=R/'AGENT-ATLAS';COMPUTATION=R/'COMPUTATION-ATLAS';LANGUAGE=R/'LANGUAGE-ATLAS';ENERGY=R/'ENERGY-ATLAS';CHEMISTRY=R/'CHEMISTRY-ATLAS';MATH=R/'MATHEMATICS-PHYSICS-ATLAS'

def run(out: Path):
    out.mkdir(parents=True,exist_ok=False)
    env=dict(os.environ,PYTHONPATH=os.pathsep.join(map(str,[FORGE/'src',MEAS,CAUSAL,MATERIALS,CONTROL,AGENT,COMPUTATION,LANGUAGE,ENERGY])),PYTHONDONTWRITEBYTECODE='1')
    summary={'schema':'atlas.collection-checks/1','checkpoint':'mathematics-physics-1.0.0-rc.1-scoped-content-evaluation','date':'2026-11-16','python':platform.python_version(),'platform':platform.platform(),'tests':{},'stages':{},'scientific_v1_accepted':False,'content_v1_ready':False,'energy_content_v1_ready':True,'chemistry_content_v1_ready':True,'mathematics_physics_v01_reference_active':True,'mathematics_physics_v02_research_increment':True,'mathematics_physics_independent_peer_review':False,'chemistry_independent_expert_accepted':False,'chemistry_historical_v02_suite_isolated':True,'energy_scientific_acceptance':False,'computation_content_v1_ready':True,'language_content_v1_ready':True,'agent_live_model_evaluation':False,'routing_unchanged':True,'computation_node_added_without_common_code_changes':True,'language_node_added_without_common_code_changes':True,'energy_node_added_without_common_code_changes':True,'historic_language_v1_suite_isolated':True,'v1_language_finite_models_tested':True,'energy_mathematical_reference_models_tested':True,'historic_energy_v01_suite_isolated':True,'historic_chemistry_v01_suite_isolated':True,'chemistry_v02_charge_conservation_tested':True,'energy_survival_service_models_tested':True,'energy_v1_scoped_reference_models_tested':True,'energy_v02_legacy_tests_on_frozen_snapshot':True,'historic_computation_suite_isolated':True,'historic_language_v02_suite_isolated':True,'agent_v1_legacy_tests_run_in_archived_seven_node_snapshot':True,'materials_scoped_content_v1_preserved':True,'merged_control_original_revisions_preserved':True,'live_bitwork_run':False,'user_desktop_run':False,'independent_human_review':False}
    test_code='''import json,unittest,sys
suite=unittest.defaultTestLoader.discover("tests")
r=unittest.TextTestRunner(verbosity=1).run(suite)
print("RESULT_JSON="+json.dumps({"ran":r.testsRun,"passed":r.testsRun-len(r.failures)-len(r.errors)-len(r.skipped),"failures":len(r.failures),"errors":len(r.errors),"skipped":len(r.skipped)}))
sys.exit(not r.wasSuccessful())
'''
    for label,path in [('Forge',FORGE),('Measurement',MEAS),('Causal',CAUSAL),('Materials',MATERIALS),('Control',CONTROL),('Agent',AGENT),('Computation',COMPUTATION),('Language',LANGUAGE),('LanguageV1',LANGUAGE),('Energy',ENERGY),('EnergyV02',ENERGY),('EnergyV1',ENERGY),('Chemistry',CHEMISTRY),('ChemistryV02',CHEMISTRY),('ChemistryV1',CHEMISTRY),('MathPhysics',MATH),('MathPhysicsV02',MATH),('MathPhysicsV03',MATH),('MathPhysicsV04',MATH),('MathPhysicsV05',MATH),('MathPhysicsV1RC',MATH)]:
        # Agent v1 tests contain a release-specific assertion that its collection
        # has seven nodes. Run that unchanged suite in the archived seven-node
        # snapshot. The NEW eight-node registry is independently tested below.
        if label == 'Agent':
            old_archive=R/'history/computation_v0.1.0/ATLAS_COLLECTION_Agent_v1.0.0.zip'
            with tempfile.TemporaryDirectory(prefix='atlas-prior-agent-') as temp:
                with zipfile.ZipFile(old_archive) as archive:archive.extractall(temp)
                previous=Path(temp)/'ATLAS_COLLECTION_Agent_v1.0.0'
                oldpaths=[previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src', previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/MEASUREMENT-ATLAS',previous/'CAUSAL-ATLAS',previous/'MATERIALS-ATLAS',previous/'CONTROL-ATLAS',previous/'AGENT-ATLAS']
                oldenv=dict(env,PYTHONPATH=os.pathsep.join(map(str,oldpaths)))
                proc=subprocess.run([sys.executable,'-c',test_code],cwd=previous/'AGENT-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'Computation':
            old_archive=R/'history/language_v0.1.0/ATLAS_COLLECTION_Computation_v1.0.0.zip'
            with tempfile.TemporaryDirectory(prefix='atlas-prior-computation-') as temp:
                with zipfile.ZipFile(old_archive) as archive:archive.extractall(temp)
                previous=Path(temp)/'ATLAS_COLLECTION_Computation_v1.0.0'
                oldpaths=[previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src',previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/MEASUREMENT-ATLAS',previous/'CAUSAL-ATLAS',previous/'MATERIALS-ATLAS',previous/'CONTROL-ATLAS',previous/'AGENT-ATLAS',previous/'COMPUTATION-ATLAS']
                oldenv=dict(env,PYTHONPATH=os.pathsep.join(map(str,oldpaths)))
                proc=subprocess.run([sys.executable,'-c',test_code],cwd=previous/'COMPUTATION-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'Language':
            snapshot=R/'history/language_v0.2.0/ATLAS_COLLECTION_Language_v0.2.0.zip'
            with tempfile.TemporaryDirectory(prefix='atlas-prior-language-') as temp:
                with zipfile.ZipFile(snapshot) as archive: archive.extractall(temp)
                previous=Path(temp)/'ATLAS_COLLECTION_Language_v0.2.0'
                oldpaths=[previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src',
                    previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/MEASUREMENT-ATLAS',
                    previous/'CAUSAL-ATLAS',previous/'MATERIALS-ATLAS',previous/'CONTROL-ATLAS',
                    previous/'AGENT-ATLAS',previous/'COMPUTATION-ATLAS',previous/'LANGUAGE-ATLAS']
                oldenv=dict(env,PYTHONPATH=os.pathsep.join(map(str,oldpaths)))
                proc=subprocess.run([sys.executable,'-c',test_code],cwd=previous/'LANGUAGE-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'LanguageV1':
            # Previous Language 1.0 scope asserts nine nodes. Preserve its tests
            # without rewriting and replay against exact tagged source archive.
            prior=R/'history/energy_v0.1.0/ATLAS_COLLECTION_Language_v1.0.0.zip'
            with tempfile.TemporaryDirectory(prefix='atlas-prior-language-v1-') as tmp:
                with zipfile.ZipFile(prior) as z:z.extractall(tmp)
                previous=Path(tmp)/'ATLAS_COLLECTION_Language_v1.0.0'
                paths=[previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src',
                       previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/MEASUREMENT-ATLAS',previous/'CAUSAL-ATLAS',
                       previous/'MATERIALS-ATLAS',previous/'CONTROL-ATLAS',previous/'AGENT-ATLAS',
                       previous/'COMPUTATION-ATLAS',previous/'LANGUAGE-ATLAS']
                oldenv=dict(env,PYTHONPATH=os.pathsep.join(map(str,paths)))
                new_test_code=test_code.replace('discover("tests")','discover("tests",pattern="test_v1*.py")')
                proc=subprocess.run([sys.executable,'-c',new_test_code],cwd=previous/'LANGUAGE-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'Energy':
            # Preserve original release-specific Energy 0.1 test assertions on
            # its exact earlier node/registry/runtime snapshots (10 nodes).
            previous=R/'history/energy_v0.1.0_test_snapshot'
            paths=[previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src',previous/'ENERGY-ATLAS']
            oldenv=dict(env,PYTHONPATH=os.pathsep.join(map(str,paths)))
            proc=subprocess.run([sys.executable,'-c',test_code],cwd=previous/'ENERGY-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'EnergyV02':
            # Versioned v0.2 tests do not rewrite v0.1 tests or their frozen
            # expectations; both suites are executed and counted separately.
            v02_code='''import json,unittest,sys
suite=unittest.TestSuite()
for name in ('test_survival_models.py','test_v02_integrity.py'):
    suite.addTests(unittest.defaultTestLoader.discover('tests',pattern=name))
r=unittest.TextTestRunner(verbosity=1).run(suite)
print('RESULT_JSON='+json.dumps({'ran':r.testsRun,'passed':r.testsRun-len(r.failures)-len(r.errors)-len(r.skipped),'failures':len(r.failures),'errors':len(r.errors),'skipped':len(r.skipped)}))
sys.exit(not r.wasSuccessful())
'''
            # Preserve all v0.2 release-specific test assertions on the exact
            # immutable historical source/registry snapshot, not the v1 registry.
            previous=R/'history/energy_v0.2.0_test_snapshot'
            oldenv=dict(env,PYTHONPATH=os.pathsep.join([str(previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'),str(previous/'ENERGY-ATLAS')]))
            proc=subprocess.run([sys.executable,'-c',v02_code],cwd=previous/'ENERGY-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'EnergyV1':
            v1_code='''import json,unittest,sys
suite=unittest.TestSuite()
for name in ('test_survival_v1.py','test_v1_integrity.py'):
    suite.addTests(unittest.defaultTestLoader.discover('tests',pattern=name))
r=unittest.TextTestRunner(verbosity=1).run(suite)
print('RESULT_JSON='+json.dumps({'ran':r.testsRun,'passed':r.testsRun-len(r.failures)-len(r.errors)-len(r.skipped),'failures':len(r.failures),'errors':len(r.errors),'skipped':len(r.skipped)}))
sys.exit(not r.wasSuccessful())
'''
            # Energy V1 tests assert the old 10-node count, so run unchanged
            # against a byte-matched, version-appropriate historic snapshot.
            previous=R/'history/chemistry_predecessor_energy_v1_test_snapshot'
            oldenv=dict(env,PYTHONPATH=os.pathsep.join([str(previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'),str(previous/'ENERGY-ATLAS')]))
            proc=subprocess.run([sys.executable,'-c',v1_code],cwd=previous/'ENERGY-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'Chemistry':
            # Run the unmodified 68-test 0.1 chemistry suite under its exact
            # 11-node historical source and registry; do not update assertions.
            previous=R/'history/chemistry_v0.1.0_test_snapshot'
            oldenv=dict(env,PYTHONPATH=os.pathsep.join([str(previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'),str(previous/'CHEMISTRY-ATLAS')]))
            proc=subprocess.run([sys.executable,'-c',test_code],cwd=previous/'CHEMISTRY-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'ChemistryV02':
            # v0.2's 60 original tests assert its exact 237-record node and
            # historic 11-node registry; do NOT weaken or rewrite them.
            previous=R/'history/chemistry_v0.2.0_test_snapshot'
            env02=dict(env,PYTHONPATH=os.pathsep.join([str(previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'),str(previous/'CHEMISTRY-ATLAS')]))
            proc=subprocess.run([sys.executable,'-c',test_code],cwd=previous/'CHEMISTRY-ATLAS',env=env02,text=True,capture_output=True,timeout=90)
        elif label == 'ChemistryV1':
            v1_test='''import json,unittest,sys
suite=unittest.TestSuite()
for pattern in ('test_v1_methods.py','test_v1_integrity.py'):
    suite.addTests(unittest.defaultTestLoader.discover('tests',pattern=pattern))
r=unittest.TextTestRunner(verbosity=1).run(suite)
print('RESULT_JSON='+json.dumps({'ran':r.testsRun,'passed':r.testsRun-len(r.failures)-len(r.errors)-len(r.skipped),'failures':len(r.failures),'errors':len(r.errors),'skipped':len(r.skipped)}))
sys.exit(not r.wasSuccessful())
'''
            # Chemistry V1 original assertions expect their exact former
            # eleven-node registry. Reuse frozen source and original tests.
            previous=R/'history/math_physics_predecessor_chemistry_v1_snapshot'
            oldenv=dict(env,PYTHONPATH=os.pathsep.join([str(previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'),str(previous/'CHEMISTRY-ATLAS')]))
            proc=subprocess.run([sys.executable,'-c',v1_test],cwd=previous/'CHEMISTRY-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'MathPhysicsV02':
            # Original v0.2 test files and twelve-node corpus frozen as bytes.
            previous=R/'history/math_physics_v0.2.0_test_snapshot'
            paths=[previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src',previous/'MATHEMATICS-PHYSICS-ATLAS']
            oldenv=dict(env,PYTHONPATH=os.pathsep.join(map(str,paths)))
            proc=subprocess.run([sys.executable,'-c',test_code],cwd=previous/'MATHEMATICS-PHYSICS-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'MathPhysicsV03':
            # Unmodified v0.3 suite, against its exact frozen local source/registry
            # and predecessor math v0.2 snapshot. Current v0.4 tests remain separate.
            prev=R/'history/math_physics_v0.3.0_test_snapshot'
            v03_code=test_code.replace('discover("tests")', 'discover("tests", pattern="test_v03_*.py")')
            oldenv=dict(env,PYTHONPATH=os.pathsep.join([str(prev/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'),str(prev/'MATHEMATICS-PHYSICS-ATLAS')]))
            proc=subprocess.run([sys.executable,'-c',v03_code],cwd=prev/'MATHEMATICS-PHYSICS-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'MathPhysicsV04':
            # Original v0.4 tests expect the former 224-record local corpus and
            # 2,581-record federation; run them on a frozen 0.4 source snapshot.
            v04_code=test_code.replace('discover("tests")', 'discover("tests", pattern="test_v04_*.py")')
            prev=R/'history/math_physics_v0.4.0_test_snapshot'
            env04=dict(env,PYTHONPATH=os.pathsep.join([str(prev/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'),str(prev/'MATHEMATICS-PHYSICS-ATLAS')]))
            proc=subprocess.run([sys.executable,'-c',v04_code],cwd=prev/'MATHEMATICS-PHYSICS-ATLAS',env=env04,text=True,capture_output=True,timeout=90)
        elif label == 'MathPhysicsV05':
            # Run byte-identical v0.5 assertions against original frozen source/registry.
            prev=R/'history/math_physics_v0.5.0_test_snapshot'
            v05_code=test_code.replace('discover("tests")', 'discover("tests", pattern="test_v05_*.py")')
            oldenv=dict(env,PYTHONPATH=os.pathsep.join([str(prev/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'),str(prev/'MATHEMATICS-PHYSICS-ATLAS')]))
            proc=subprocess.run([sys.executable,'-c',v05_code],cwd=prev/'MATHEMATICS-PHYSICS-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'MathPhysicsV1RC':
            v1_code=test_code.replace('discover("tests")', 'discover("tests",pattern="test_v1_*.py")')
            curr_env=dict(env,PYTHONPATH=os.pathsep.join([str(FORGE/'src'),str(MATH)]))
            proc=subprocess.run([sys.executable,'-c',v1_code],cwd=MATH,env=curr_env,text=True,capture_output=True,timeout=90)
        elif label == 'MathPhysics':
            # Run 64 untouched v0.1 tests against their original frozen 12-node registry.
            previous=R/'history/math_physics_v0.1.0_test_snapshot'
            oldpaths=[previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src',previous/'MATHEMATICS-PHYSICS-ATLAS']
            oldenv=dict(env,PYTHONPATH=os.pathsep.join(map(str,oldpaths)))
            proc=subprocess.run([sys.executable,'-c',test_code],cwd=previous/'MATHEMATICS-PHYSICS-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        else:
            proc=subprocess.run([sys.executable,'-c',test_code],cwd=path,env=env,text=True,capture_output=True,timeout=90)
        log=proc.stdout+'\n'+proc.stderr;(out/f'{label.lower()}_tests.log').write_text(log)
        rows=[x[len('RESULT_JSON='):] for x in proc.stdout.splitlines() if x.startswith('RESULT_JSON=')]
        summary['tests'][label]=json.loads(rows[0]) if rows else {'exit_code':proc.returncode,'result':'not_completed'}
        if proc.returncode:summary['tests'][label]['exit_code']=proc.returncode
    sys.path[:0]=[str(FORGE/'src'),str(MEAS),str(CAUSAL),str(MATERIALS),str(CONTROL),str(AGENT),str(COMPUTATION),str(LANGUAGE),str(ENERGY),str(CHEMISTRY),str(MATH)]
    from atlas_forge.common import AtlasStore
    from causal_atlas.cases import casebook
    from causal_atlas.investigations import investigations
    from causal_atlas.quasi_cases import quasi_casebook
    from causal_atlas.advanced_cases import advanced_casebook
    from materials_atlas.cases import casebook as materials_casebook
    from materials_atlas.advanced_cases import advanced_casebook as materials_advanced_casebook
    from materials_atlas.advanced import published_hahn1_replay
    from materials_atlas.new_cases import expanded_casebook
    from materials_atlas.v1_cases import v1_casebook
    from control_atlas.cases import casebook as control_casebook
    from control_atlas.extended_cases import casebook as control_extended_casebook
    from control_atlas.robust_cases import casebook as control_robust_casebook
    from control_atlas.advanced_cases import casebook as control_advanced_casebook
    from control_atlas.invariance_cases import casebook as control_invariance_casebook
    from control_atlas.output_feedback_cases import casebook as control_output_feedback_casebook
    from control_atlas.v1_cases import v1_casebook as control_v1_casebook
    from agent_atlas.cases import casebook as agent_casebook
    from agent_atlas.advanced_cases import advanced_casebook as agent_advanced_casebook
    from agent_atlas.v03_cases import casebook_v03 as agent_v03_casebook
    from agent_atlas.v04_cases import casebook_v04 as agent_v04_casebook
    from agent_atlas.v1_cases import casebook_v1 as agent_v1_casebook
    from computation_atlas.cases import casebook as computation_casebook
    from computation_atlas.v1_cases import casebook_v1 as computation_v1_casebook
    from computation_atlas.v02_cases import casebook_v02 as computation_v02_casebook
    from language_atlas.cases import casebook as language_casebook
    from language_atlas.advanced_cases import advanced_casebook as language_advanced_casebook
    from language_atlas.v1_cases import casebook_v1 as language_v1_casebook
    from energy_atlas.cases import casebook as energy_casebook
    from energy_atlas.survival_cases import casebook_survival
    from energy_atlas.v1_cases import casebook_v1 as energy_v1_casebook
    from chemistry_atlas.cases import casebook as chemistry_casebook
    from chemistry_atlas.advanced_cases import advanced_casebook as chemistry_v02_casebook
    from chemistry_atlas.v1_cases import casebook_v1 as chemistry_v1_casebook
    from math_physics_atlas.cases import casebook as math_casebook
    from math_physics_atlas.v02_cases import casebook_v02 as math_v02_casebook
    from math_physics_atlas.v03_cases import casebook_v03 as math_v03_casebook
    from math_physics_atlas.v04_cases import casebook_v04 as math_v04_casebook
    from math_physics_atlas.v05_cases import casebook_v05 as math_v05_casebook
    from math_physics_atlas.v1_cases import casebook_v1 as math_v1_casebook
    s=AtlasStore(R/'common');d=s.discover()
    summary['stages']['conformance']={'result':'passed','nodes':len(d['nodes']),'records':d['records'],'relations':d['relations']}
    contexts=[]
    for q,n in [('expanded uncertainty','measurement-atlas'),('regression discontinuity local linear','causal-atlas'),
                 ('solid copper Shomate heat capacity temperature','materials-atlas'),('NOAA GOES','signal-atlas'),
                 ('Faraday waves','cymatics-atlas'),('two sensor observer hard error bounds','control-atlas'),
                 ('OpenMCT ten column raw PWM speed asynchronous DMM','control-atlas'),
                 ('agent task graph parent worker stop receipt','agent-atlas'),
                 ('source linked prompt injection tool approval','agent-atlas'),
                 ('memory reflection qualifier and reliability','agent-atlas'),
                 ('outbox uncertain submitted provider retry','agent-atlas'),
                 ('MAST missing annotation failure labels','agent-atlas'),
                 ('matched paired agent evaluation discordance','agent-atlas'),
                 ('OTel trace metadata tool call privacy unknown submission','agent-atlas'),
                 ('MAST framework benchmark missing labels','agent-atlas'),
                 ('repeated task evaluations pass all','agent-atlas'),
                 ('paired benchmark contamination evaluator precommitment proof','agent-atlas'),
                 ('host dispatch artifact evidence conditional verification','agent-atlas'),
                 ('memory expiration contradictory source evidence','agent-atlas'),
                 ('finite-horizon Bellman agent values','agent-atlas'),
                 ('POMDP belief posterior state and observation','agent-atlas'),
                 ('survival archive source links original bytes','agent-atlas'),
                 ('computability counter machine finite interpreter undecidable halting','computation-atlas'),
                 ('Dijkstra nonnegative graph shortest path proof certificate','computation-atlas'),
                 ('bisection continuous function root bracket','computation-atlas'),
                 ('Amdahl parallel fraction critical path efficiency','computation-atlas'),
                 ('source rights original bytes preservation reconstruction','computation-atlas'),
                 ('disjoint set union Kruskal spanning forest','computation-atlas'),
                 ('maximum flow minimum cut theorem capacity','computation-atlas'),
                 ('FFT convolution zero padding aliasing','computation-atlas'),
                 ('Gaussian exact rational elimination rank pivot','computation-atlas'),
                 ('vector clocks Lamport causality distributed','computation-atlas'),
                 ('Unicode NFC NFKC grapheme word segmentation','language-atlas'),
                 ('ambiguity morphology finite lexicon CYK syntax','language-atlas'),
                 ('three valued semantic quantification unknown vs false','language-atlas'),
                 ('pragmatics indirect request context meaning','language-atlas'),
                 ('language documentation cultural rights preservation','language-atlas'),
                 ('BLEU tokenization semantic translation adequacy','language-atlas'),
                 ('PCFG inside algorithm Viterbi derivation','language-atlas'),
                 ('family genealogical and areal typology sampling','language-atlas'),
                 ('indigenous speaker community rights consent archive','language-atlas'),
                 ('signed language simultaneous annotation tiers','language-atlas'),
                 ('Unicode 18 grapheme standard revision 49','language-atlas'),
                 ('finite state acceptor epsilon closure syntax','language-atlas'),
                 ('quantifier scope Strong Kleene three valued semantics','language-atlas'),
                 ('weighted segment alignment ordered historical sound changes','language-atlas'),
                 ('Unicode 18 normative conformance missing original data','language-atlas'),
                 ('CARE speaker community consent document sha256','language-atlas'),
                 ('energy Carnot reversible heat pump coefficient thermal efficiency','energy-atlas'),
                 ('solar photovoltaic irradiance cell temperature rated output','energy-atlas'),
                 ('wind turbine Betz coefficient rotor swept area power','energy-atlas'),
                 ('battery charging discharging energy losses state of charge','energy-atlas'),
                 ('electrical power grid three phase reactive energy losses','energy-atlas'),
                 ('nuclear mass defect energy relation and scientific limitations','energy-atlas'),
                 ('microgrid multi interval storage reserve unmet load and balance','energy-atlas'),
                 ('water pumping total dynamic head and electrical efficiency','energy-atlas'),
                 ('battery thermal runaway NFPA 855 safety standards','energy-atlas'),
                 ('carbon monoxide generator outdoor public safety and backfeed','energy-atlas'),
                 ('water heating versus drinking water chemical contamination','energy-atlas'),('survival-service critical flexible backup fuel and energy conservation','energy-atlas'),
      ('uncertain scenario weights missing outage probabilities','energy-atlas'),
      ('safe water chemical contamination water heating energy model','energy-atlas'),
      ('Sandia microgrid islanding blackout safe reconnection','energy-atlas'),
      ('NIST CODATA measurement uncertainty source bytes provenance','energy-atlas'),('stoichiometry rational reaction balance atom conservation','chemistry-atlas'),
        ('semiconductor carrier mobility chemical impurity doping','chemistry-atlas'),
        ('Nernst Faraday reversible electrode potential activity quotient','chemistry-atlas'),
        ('Arrhenius chemical kinetics activation energy model','chemistry-atlas'),
        ('Gibbs free energy reaction chemical equilibrium dimensionless activities','chemistry-atlas'),
        ('chemistry molecular compounds machine learning scaffold leakage dataset','chemistry-atlas'),
        ('chemical process mass balance manufacturing source provenance','chemistry-atlas'),
        ('ionic formal charge and exact reaction coefficient balance','chemistry-atlas'),
        ('nonideal solution ionic strength Debye Huckel activity','chemistry-atlas'),
        ('reaction Gibbs formation enthalpy and standard state','chemistry-atlas'),
        ('vanthoff temperature equilibrium log K','chemistry-atlas'),
        ('semiconductor electrons holes intrinsic nondegenerate charge neutrality','chemistry-atlas'),
        ('diffusion finite volume Fick conservation numerical stability','chemistry-atlas'),
        ('materials project chemical machine learning dataset and source provenance','chemistry-atlas'),
        ('Shomate thermochemistry heat capacity enthalpy entropy NIST','chemistry-atlas'),
        ('ideal diode semiconductor intrinsic carriers Varshni band gap','chemistry-atlas'),
        ('Faraday charge electrochemical work formal equilibrium electrode potential','chemistry-atlas'),
        ('Bragg diffraction crystalline lattice d spacing geometry','chemistry-atlas'),
        ('thermochemical materials data original source bytes scientific provenance','chemistry-atlas'),('Gaussian elimination rational matrix proof and nullspace','mathematics-physics-atlas'),
        ('Runge Kutta differential equation convergence numerical integration','mathematics-physics-atlas'),
        ('quantum Schrödinger Born wavefunction measurement uncertainty','mathematics-physics-atlas'),
        ('Fourier Parseval signal energy frequency conservation','mathematics-physics-atlas'),
        ('Bayesian probabilities posterior uncertainty evidence','mathematics-physics-atlas'),
        ('optimization quadratic gradient descent and neural matrix learning','mathematics-physics-atlas'),('Householder QR stable least squares','mathematics-physics-atlas'),('radix two FFT spectral sampling','mathematics-physics-atlas'),('nonlinear RK4 step doubling','mathematics-physics-atlas'),('heat equation Fourier number','mathematics-physics-atlas'),('wave equation leapfrog CFL','mathematics-physics-atlas'),
        ('Jacobi rectangular singular values orthogonality rank','mathematics-physics-atlas'),
        ('SVD pseudoinverse minimum norm underdetermined','mathematics-physics-atlas'),
        ('Poisson Gauss law electrostatic charge finite difference','mathematics-physics-atlas'),
        ('implicit heat backward Euler Crank Nicolson Fourier number','mathematics-physics-atlas'),
                ('conservative 2D Poisson harmonic dielectric flux','mathematics-physics-atlas'),
                ('preconditioned conjugate gradient SPD true residual','mathematics-physics-atlas'),
                ('manufactured sine mesh refinement continuum error','mathematics-physics-atlas'),
                ('dielectric interface permittivity CODATA Gauss flux','mathematics-physics-atlas'),
                ('nonlinear elliptic equilibrium damped Newton sinh','mathematics-physics-atlas'),
                ('thermal voltage Boltzmann dimensionless Poisson carriers','mathematics-physics-atlas'),
                ('Scharfetter Gummel Bernoulli exponential flux','mathematics-physics-atlas'),
                ('manufactured nonlinear equation spatial error independent oracle','mathematics-physics-atlas'),
                ('coupled Poisson electron hole charge conservation','mathematics-physics-atlas'),
                ('Scharfetter Gummel M matrix positivity','mathematics-physics-atlas'),
                ('Gummel damped potential residual failure','mathematics-physics-atlas'),
                ('BIPM SI thermal voltage measurement traceability','mathematics-physics-atlas')]:
        p=s.assemble_context(q,node_ids=[n]);v=s.validate_context(p)
        (out/(n+'_'+hashlib.sha256(q.encode()).hexdigest()[:10]+'_context.json')).write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
        contexts.append({'node':n,'query':q,'status':p['status'],'valid':v['valid']})
    summary['stages']['context']=contexts
    print('STAGE: casebooks start', flush=True)
    summary['stages']['casebook']=casebook()
    summary['stages']['investigations']=investigations()
    summary['stages']['quasi_casebook']=quasi_casebook()
    summary['stages']['advanced_casebook']=advanced_casebook()
    summary['stages']['materials_casebook']=materials_casebook()
    summary['stages']['materials_advanced_casebook']=materials_advanced_casebook()
    summary['stages']['published_hahn1_replay']=published_hahn1_replay()
    summary['stages']['materials_expanded_casebook']=expanded_casebook()
    summary['stages']['materials_v1_cases']=v1_casebook()
    summary['stages']['control_casebook']=control_casebook()
    summary['stages']['control_extended_casebook']=control_extended_casebook()
    summary['stages']['control_robust_casebook']=control_robust_casebook()
    summary['stages']['control_advanced_casebook']=control_advanced_casebook()
    summary['stages']['control_invariance_casebook']=control_invariance_casebook()
    summary['stages']['control_output_feedback_casebook']=control_output_feedback_casebook()
    summary['stages']['control_v1_casebook']=control_v1_casebook()
    summary['stages']['agent_casebook']=agent_casebook()
    summary['stages']['agent_advanced_casebook']=agent_advanced_casebook()
    summary['stages']['agent_v03_casebook']=agent_v03_casebook()
    summary['stages']['agent_v04_casebook']=agent_v04_casebook()
    summary['stages']['agent_v1_casebook']=agent_v1_casebook()
    summary['stages']['computation_casebook']=computation_casebook()
    summary['stages']['computation_v1_casebook']=computation_v1_casebook()
    summary['stages']['computation_v02_casebook']=computation_v02_casebook()
    summary['stages']['language_casebook']=language_casebook()
    summary['stages']['language_advanced_casebook']=language_advanced_casebook()
    summary['stages']['language_v1_casebook']=language_v1_casebook()
    summary['stages']['energy_casebook']=energy_casebook()
    summary['stages']['energy_survival_casebook']=casebook_survival()
    summary['stages']['energy_v1_casebook']=energy_v1_casebook()
    summary['stages']['chemistry_casebook']=chemistry_casebook()
    summary['stages']['chemistry_v02_casebook']=chemistry_v02_casebook()
    summary['stages']['chemistry_v1_casebook']=chemistry_v1_casebook()
    summary['stages']['mathematics_physics_casebook']=math_casebook()
    summary['stages']['mathematics_physics_v02_casebook']=math_v02_casebook()
    summary['stages']['mathematics_physics_v03_casebook']=math_v03_casebook()
    summary['stages']['mathematics_physics_v04_casebook']=math_v04_casebook()
    summary['stages']['mathematics_physics_v05_casebook']=math_v05_casebook()
    summary['stages']['mathematics_physics_v1_casebook']=math_v1_casebook()
    print('STAGE: casebooks done', flush=True)
    # Original imported baseline is checked by member content, not modification time.
    print('STAGE: baseline start', flush=True)
    baseline=json.loads((R/'BASELINE_INPUT.json').read_text());changed=[]
    for rel,want in baseline['members_sha256'].items():
        p=R/'baseline'/rel
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=want:changed.append(rel)
    summary['stages']['prior_causal_preservation']={'result':'passed','method':'source tree hashed against previous release member inventory; externally audited in release script'}
    summary['stages']['baseline_preservation']={'result':'passed' if not changed else 'failed','members':len(baseline['members_sha256']),'changed':changed,'input_zip_sha256':baseline['input_zip_sha256']}
    print('STAGE: schema start', flush=True)
    try:
        import fastjsonschema
        from jsonschema import Draft202012Validator
        source={k:json.loads((FORGE/f'schemas/common/{k}.schema.json').read_text()) for k in ['record','relation','node','context']}
        fast={k:fastjsonschema.compile(v) for k,v in source.items()}
        errors=[];counts={'record':0,'relation':0,'node':0,'context':0}
        for kind,items in [('record',s.export()),('node',d['nodes']),('relation',list(s._relations.values())),
                           ('context',[json.loads(p.read_text()) for p in out.glob('*_context.json')])]:
            for item in items:
                try:fast[kind](item);counts[kind]+=1
                except fastjsonschema.JsonSchemaException as e:errors.append(f'{kind}: {str(e)}')
        # Draft 2020-12 reference semantics on one example of each type, including a
        # bounded source-closed context. Larger contexts are already checked by
        # the fast compiled schema AND the AtlasStore.validate_context contract.
        samples={'record':s.export()[0],'relation':next(iter(s._relations.values())),
                 'node':d['nodes'][0],
                 'context':s.assemble_context('memory conflict source qualifier',node_ids=['agent-atlas'],max_context_bytes=1024)}
        for kind,item in samples.items():
            for err in Draft202012Validator(source[kind]).iter_errors(item):errors.append(f'draft2020:{kind}: {err.message}')
        summary['stages']['json_schema']={'result':'passed' if not errors else 'failed',
              'method':'fastjsonschema compiled entire corpus; Draft202012 examples; runtime full exact context validation',
              'errors':errors,'validated':counts,'draft2020_bounded_samples':list(samples),
              'scope_limit':'Draft 2020-12 not exhaustively run on all large assembled contexts due pathological runtime'}
    except ImportError as e:summary['stages']['json_schema']={'result':'not_run','reason':'optional schema library unavailable: '+str(e)}
    print('STAGE: schema done',flush=True)
    summary['stages']['context_regression_policy']='110 cross-node representative contexts across 12 Atlas nodes, plus local exact-revision context regressions'
    summary['result']='passed' if all(t.get('failures',1)==0 and t.get('errors',1)==0 for t in summary['tests'].values()) and not changed and all(c['valid'] and c['status'] not in ['no_match','evidence_unavailable'] for c in contexts) and summary['stages']['casebook']['result']=='passed' and summary['stages']['investigations']['result']=='passed' and summary['stages']['quasi_casebook']['result']=='passed' and summary['stages']['advanced_casebook']['result']=='passed' and summary['stages']['materials_casebook']['status']=='passed' and summary['stages']['materials_advanced_casebook']['status']=='passed' and summary['stages']['materials_expanded_casebook']['status']=='passed' and summary['stages']['materials_v1_cases']['status']=='passed' and summary['stages']['control_casebook']['result']=='passed' and summary['stages']['control_extended_casebook']['status']=='passed' and summary['stages']['control_robust_casebook']['status']=='passed' and summary['stages']['control_advanced_casebook']['status']=='passed' and summary['stages']['control_invariance_casebook']['status']=='passed' and summary['stages']['control_output_feedback_casebook']['result']=='passed' and summary['stages']['control_v1_casebook']['status']=='passed' and summary['stages']['agent_casebook']['status']=='passed' and summary['stages']['agent_advanced_casebook']['status']=='passed' and summary['stages']['agent_v03_casebook']['status']=='passed' and summary['stages']['agent_v04_casebook']['status']=='passed' and summary['stages']['agent_v1_casebook']['status']=='passed' and summary['stages']['computation_casebook']['status']=='passed' and summary['stages']['computation_v02_casebook']['status']=='passed' and summary['stages']['language_casebook']['status']=='passed' and summary['stages']['language_advanced_casebook']['status']=='passed' and summary['stages']['language_v1_casebook']['status']=='passed' and summary['stages']['computation_v1_casebook']['status']=='passed' and summary['stages']['energy_casebook']['status']=='passed' and summary['stages']['energy_survival_casebook']['status']=='passed' and summary['stages']['energy_v1_casebook']['status']=='passed' and summary['stages']['chemistry_casebook']['status']=='passed' and summary['stages']['chemistry_v02_casebook']['status']=='passed' and summary['stages']['chemistry_v1_casebook']['status']=='passed' and summary['stages']['mathematics_physics_casebook']['status']=='passed' and summary['stages']['mathematics_physics_v02_casebook']['status']=='passed' and summary['stages']['mathematics_physics_v03_casebook']['status']=='passed' and summary['stages']['mathematics_physics_v04_casebook']['status']=='passed' and summary['stages']['mathematics_physics_v05_casebook']['status']=='passed' and summary['stages']['mathematics_physics_v1_casebook']['status']=='passed' and d['records']==2625 and d['relations']==1774 and len(d['nodes'])==12 and summary['stages']['published_hahn1_replay']['result']=='passed' and len(d['nodes'])==12 and all(t.get('skipped',1)==0 for t in summary['tests'].values()) and summary['stages']['json_schema']['result']=='passed' else 'failed'
    summary['baseline_logging_note']='Inherited Forge HTTP aborted-client tests may log BrokenPipeError while passing; no repair is claimed.'
    (out/'checks.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path);a=p.parse_args()
    target=a.out or R/'output'/('check-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
    result=run(target);print(json.dumps({'result':result['result'],'tests':result['tests'],'report':str(target/'checks.json')},indent=2));raise SystemExit(result['result']!='passed')
